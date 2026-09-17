#!/usr/bin/env python3
"""Geometric overlap audit for BPMN DI layouts.

Checks per file:
  1. node-node bounding box overlaps,
  2. edge segments cutting through node interiors (excluding endpoints),
  3. edge label bounds overlapping node boxes,
  4. coincident (stacked) parallel edge segments.
Exit code 1 if any of 1-3 found.
"""
import os
import sys
import xml.etree.ElementTree as ET

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DIRS = [os.path.join(ROOT, "processes"), os.path.join(ROOT, "processes-to-be")]

NS_BPMN = "http://www.omg.org/spec/BPMN/20100524/MODEL"
NS_BPMNDI = "http://www.omg.org/spec/BPMN/20100524/DI"
NS_DC = "http://www.omg.org/spec/DD/20100524/DC"
NS_DI = "http://www.omg.org/spec/DD/20100524/DI"
Q = {"bpmn": "{%s}" % NS_BPMN, "bpmndi": "{%s}" % NS_BPMNDI,
     "dc": "{%s}" % NS_DC, "di": "{%s}" % NS_DI}

E = 3.0


def load(path):
    root = ET.parse(path).getroot()
    proc = root.find(".//%sprocess" % Q["bpmn"])
    lane_ids = {l.get("id") for l in proc.findall(".//%slane" % Q["bpmn"])}
    endpoints = {}
    for f in proc.findall("%ssequenceFlow" % Q["bpmn"]):
        endpoints[f.get("id")] = (f.get("sourceRef"), f.get("targetRef"))
    nodes = {}
    for sh in root.findall(".//%sBPMNShape" % Q["bpmndi"]):
        el = sh.get("bpmnElement")
        b = sh.find("%sBounds" % Q["dc"])
        if b is None or el in lane_ids:
            continue
        nodes[el] = (float(b.get("x")), float(b.get("y")),
                     float(b.get("width")), float(b.get("height")))
    edges = {}
    labels = {}
    for ed in root.findall(".//%sBPMNEdge" % Q["bpmndi"]):
        el = ed.get("bpmnElement")
        wps = [(float(w.get("x")), float(w.get("y")))
               for w in ed.findall("%swaypoint" % Q["di"])]
        edges[el] = wps
        lb = ed.find("%sBPMNLabel" % Q["bpmndi"])
        if lb is not None:
            b = lb.find("%sBounds" % Q["dc"])
            if b is not None:
                labels[el] = (float(b.get("x")), float(b.get("y")),
                              float(b.get("width")), float(b.get("height")))
    return nodes, edges, labels, endpoints


def box_overlap(a, b, tol):
    ox = min(a[0] + a[2], b[0] + b[2]) - max(a[0], b[0])
    oy = min(a[1] + a[3], b[1] + b[3]) - max(a[1], b[1])
    return ox > tol and oy > tol


def seg_hits_box(p, q, box, tol):
    x, y, w, h = box
    x0, x1 = x + tol, x + w - tol
    y0, y1 = y + tol, y + h - tol
    if x1 <= x0 or y1 <= y0:
        return False
    if abs(p[1] - q[1]) < 0.5:
        yy = p[1]
        lo, hi = min(p[0], q[0]), max(p[0], q[0])
        return y0 < yy < y1 and hi - max(lo, x0) > tol and min(hi, x1) - lo > tol \
            and min(hi, x1) - max(lo, x0) > tol
    if abs(p[0] - q[0]) < 0.5:
        xx = p[0]
        lo, hi = min(p[1], q[1]), max(p[1], q[1])
        return x0 < xx < x1 and min(hi, y1) - max(lo, y0) > tol
    return False


def audit(path):
    nodes, edges, labels, endpoints = load(path)
    ids = list(nodes)
    node_overlaps = []
    for i in range(len(ids)):
        for j in range(i + 1, len(ids)):
            if box_overlap(nodes[ids[i]], nodes[ids[j]], E):
                node_overlaps.append((ids[i], ids[j]))
    pierces = []
    for fid, wps in edges.items():
        src, tgt = endpoints.get(fid, (None, None))
        for p, q in zip(wps, wps[1:]):
            for nid, box in nodes.items():
                if nid in (src, tgt):
                    continue
                if seg_hits_box(p, q, box, E):
                    pierces.append((fid, nid))
                    break
    label_overlaps = []
    for fid, lb in labels.items():
        for nid, box in nodes.items():
            if box_overlap(lb, box, E):
                label_overlaps.append((fid, nid))
    coincident = 0
    hsegs = []
    vsegs = []
    for fid, wps in edges.items():
        for p, q in zip(wps, wps[1:]):
            if abs(p[1] - q[1]) < 0.5:
                hsegs.append((p[1], min(p[0], q[0]), max(p[0], q[0]), fid))
            elif abs(p[0] - q[0]) < 0.5:
                vsegs.append((p[0], min(p[1], q[1]), max(p[1], q[1]), fid))
    for a in hsegs:
        for b in hsegs:
            if a[3] >= b[3] or abs(a[0] - b[0]) > 0.5:
                continue
            if min(a[2], b[2]) - max(a[1], b[1]) > 24:
                coincident += 1
    for a in vsegs:
        for b in vsegs:
            if a[3] >= b[3] or abs(a[0] - b[0]) > 0.5:
                continue
            if min(a[2], b[2]) - max(a[1], b[1]) > 24:
                coincident += 1
    return node_overlaps, pierces, label_overlaps, coincident


def main():
    bad = 0
    for d in DIRS:
        for fn in sorted(os.listdir(d)):
            if not fn.endswith(".bpmn") or fn.endswith((".bak", ".prelayout")):
                continue
            path = os.path.join(d, fn)
            no, pc, lo, co = audit(path)
            flag = "OK " if not (no or pc or lo) else "BAD"
            if no or pc or lo:
                bad += 1
            print(f"{flag} {d.split('/')[-1]}/{fn}: node_overlaps={len(no)} "
                  f"edge_cut_node={len(pc)} label_over_node={len(lo)} coincident_seg_pairs={co}")
            for pair in no[:5]:
                print(f"     overlap: {pair[0]} <-> {pair[1]}")
            for pair in pc[:5]:
                print(f"     cut: {pair[0]} through {pair[1]}")
            for pair in lo[:5]:
                print(f"     label: {pair[0]} on {pair[1]}")
    print(f"\n{'FAIL' if bad else 'PASS'}: {bad} file(s) with overlaps")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()

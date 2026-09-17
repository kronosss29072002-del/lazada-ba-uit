#!/usr/bin/env python3
"""Re-layout BPMN DI so screenshots stop overlapping.

Per .bpmn file:
1. Break cycles (DFS back-edges) so ranking is well defined.
2. Rank flow nodes by longest path from sources => column index.
   Nodes sharing (lane, column) get distinct sub-rows so they never stack.
3. Lanes become stacked horizontal bands; nodes centered in (column, sub-row).
4. Every sequenceFlow is re-routed orthogonally through reserved empty
   vertical strips (between neighbouring columns) and horizontal channels
   (lane / sub-row boundaries, or a loop band outside the pool for
   back-edges), so edges never cut through node boxes and parallel edges
   get per-edge offsets instead of coincident segments.
5. Edge names are kept as BPMNLabel bounds placed on the longest segment.
   Artifacts (dataObjectReference/textAnnotation) go to a strip below pool.
Only the <bpmndi:BPMNDiagram> block is rewritten; semantics untouched.
Originals backed up to *.prelayout once.
"""
import os, shutil
import xml.etree.ElementTree as ET
from collections import defaultdict, deque

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DIRS = [os.path.join(ROOT, "processes"), os.path.join(ROOT, "processes-to-be")]

NS_BPMN = "http://www.omg.org/spec/BPMN/20100524/MODEL"
NS_DI = "http://www.omg.org/spec/BPMN/20100524/DI"
NS_DC = "http://www.omg.org/spec/DD/20100524/DC"
NS_DI2 = "http://www.omg.org/spec/DD/20100524/DI"
ET.register_namespace("bpmn", NS_BPMN)
ET.register_namespace("bpmndi", NS_DI)
ET.register_namespace("dc", NS_DC)
ET.register_namespace("di", NS_DI2)
Q = {"bpmn": "{%s}" % NS_BPMN, "bpmndi": "{%s}" % NS_DI,
     "dc": "{%s}" % NS_DC, "di": "{%s}" % NS_DI2}

SKIP_TAGS = {"laneSet", "extensionElements", "sequenceFlow", "association",
             "dataObject", "dataStore", "property", "ioSpecification",
             "documentation", "monitoring", "auditing", "categoryValueRef"}
ARTIFACT_TAGS = {"dataObjectReference", "textAnnotation", "group"}

COL_W = 240
LANE_H = 210
LEFT_PAD = 110
TOP_PAD = 140
LANE_X = 30
SUBROW_H = 96
TASK_W, TASK_H = 124, 72
GATE_W, GATE_H = 50, 50
EVENT_D = 36
HALF_MAX = 62
CORRIDOR = 16
LOOP_GAP = 34

OFFS = [-32, -16, 0, 16, 32]
OFFS_FINE = [-8, -4, 0, 4, 8]
OFFS_X = [-40, -28, -16, -6, 6, 16, 28, 40]


def parse(root):
    proc = root.find(".//%sprocess" % Q["bpmn"])
    if proc is None:
        return None
    laneset = proc.find("%slaneSet" % Q["bpmn"])
    lanes = []
    node_lane = {}
    if laneset is not None:
        for lane in laneset.findall("%slane" % Q["bpmn"]):
            refs = [fr.text for fr in lane.findall("%sflowNodeRef" % Q["bpmn"]) if fr.text]
            lanes.append((lane.get("id"), lane.get("name", lane.get("id")), refs))
            for r in refs:
                node_lane[r] = lane.get("id")
    nodes = {}
    artifacts = {}
    for el in proc:
        t = el.tag.split("}")[-1]
        nid = el.get("id")
        if not nid or t in SKIP_TAGS:
            continue
        if t in ARTIFACT_TAGS:
            artifacts[nid] = t
            continue
        nodes[nid] = t
    flows = {}
    for el in proc.findall("%ssequenceFlow" % Q["bpmn"]):
        flows[el.get("id")] = (el.get("sourceRef"), el.get("targetRef"), el.get("name"))
    return proc, lanes, node_lane, nodes, flows, artifacts


def break_cycles(nodes, flows):
    adj = defaultdict(list)
    ids = set(nodes)
    for fid, (s, t, _n) in flows.items():
        if s in ids and t in ids:
            adj[s].append((t, fid))
    back = set()
    WHITE, GRAY, BLACK = 0, 1, 2
    color = {n: WHITE for n in ids}

    def dfs(u):
        color[u] = GRAY
        for v, fid in adj[u]:
            if color[v] == GRAY:
                back.add(fid)
            elif color[v] == WHITE:
                dfs(v)
        color[u] = BLACK
    for n in sorted(ids):
        if color[n] == WHITE:
            dfs(n)
    return back


def rank_nodes(nodes, flows, back_edges):
    adj = defaultdict(list)
    indeg = defaultdict(int)
    ids = set(nodes)
    for fid, (s, t, _n) in flows.items():
        if fid in back_edges:
            continue
        if s in ids and t in ids:
            adj[s].append(t)
            indeg[t] += 1
    rank = {n: 0 for n in ids}
    q = deque(sorted(n for n in ids if indeg[n] == 0))
    while q:
        n = q.popleft()
        for m in adj[n]:
            if rank[m] < rank[n] + 1:
                rank[m] = rank[n] + 1
            indeg[m] -= 1
            if indeg[m] == 0:
                q.append(m)
    return rank


def size_of(tag):
    if "Gateway" in tag:
        return GATE_W, GATE_H
    if "Event" in tag:
        return EVENT_D, EVENT_D
    return TASK_W, TASK_H


def layout(proc, lanes, node_lane, nodes, flows, artifacts):
    if not lanes:
        lanes = [("_d", "Default", list(nodes))]
        node_lane = {n: "_d" for n in nodes}
    back = break_cycles(nodes, flows)
    rank = rank_nodes(nodes, flows, back)
    buckets = defaultdict(list)
    lane_ids = {l[0] for l in lanes}
    for nid in nodes:
        lid = node_lane.get(nid, lanes[0][0])
        if lid not in lane_ids:
            lid = lanes[0][0]
        node_lane[nid] = lid
        buckets[(lid, rank.get(nid, 0))].append(nid)
    subrow = {}
    max_sub = defaultdict(int)
    for (lid, _col), members in buckets.items():
        for k, nid in enumerate(sorted(members)):
            subrow[nid] = k
            max_sub[lid] = max(max_sub[lid], k + 1)
    for lid, _, _ in lanes:
        max_sub[lid] = max(max_sub[lid], 1)
    max_col = max(rank.values()) if rank else 0
    lane_h = {}
    for lid, _, _ in lanes:
        lane_h[lid] = max(LANE_H, 60 + max_sub[lid] * SUBROW_H)
    lane_y = {}
    y = TOP_PAD
    for lid, _, _ in lanes:
        lane_y[lid] = y
        y += lane_h[lid]
    pool_bottom = y
    total_w = LEFT_PAD + (max_col + 1) * COL_W + 80
    lane_bounds = {}
    for lid, _, _ in lanes:
        lane_bounds[lid] = (LANE_X, lane_y[lid], max(total_w - LANE_X - 20, 900), lane_h[lid])
    band_top = {}
    for lid, _, _ in lanes:
        band_top[lid] = lane_y[lid] + (lane_h[lid] - max_sub[lid] * SUBROW_H) / 2
    pos = {}
    for nid, tag in nodes.items():
        col = rank.get(nid, 0)
        lid = node_lane.get(nid, lanes[0][0])
        lx, ly, lw, lh = lane_bounds[lid]
        w, h = size_of(tag)
        cx = LEFT_PAD + col * COL_W + COL_W // 2
        cy = band_top[lid] + subrow.get(nid, 0) * SUBROW_H + SUBROW_H / 2
        pos[nid] = (cx - w / 2, cy - h / 2, w, h, cx, cy)
    apos = {}
    for i, nid in enumerate(sorted(artifacts)):
        apos[nid] = (LEFT_PAD + i * 160, pool_bottom + 120, 36, 48,
                     LEFT_PAD + i * 160 + 18, pool_bottom + 144)
    meta = {
        "rank": rank, "back": back, "subrow": subrow, "max_sub": max_sub,
        "lane_y": lane_y, "lane_h": lane_h, "band_top": band_top,
        "pool_bottom": pool_bottom, "n_lanes": len(lanes),
        "total_h": pool_bottom + 200, "node_lane": node_lane,
        "lanes": lanes,
    }
    return pos, apos, lane_bounds, meta


def strip_right(col, off):
    return LEFT_PAD + col * COL_W + COL_W // 2 + 120 + off


def strip_left(col, off):
    return LEFT_PAD + col * COL_W + COL_W // 2 - 120 + off


def _box4(v):
    return v[0], v[1], v[2], v[3]


def seg_blocked(ax, ay, bx, by, boxes, skip, tol=3.0, thru=True):
    if abs(ay - by) < 0.5:
        yy, lo, hi = ay, min(ax, bx), max(ax, bx)
        for nid, v in boxes.items():
            if nid in skip:
                continue
            x, y, w, h = _box4(v)
            if y + tol < yy < y + h - tol and min(hi, x + w - tol) - max(lo, x + tol) > tol:
                return True
        return False
    if abs(ax - bx) < 0.5:
        xx, lo, hi = ax, min(ay, by), max(ay, by)
        for nid, v in boxes.items():
            if nid in skip:
                continue
            x, y, w, h = _box4(v)
            if x + tol < xx < x + w - tol and min(hi, y + h - tol) - max(lo, y + tol) > tol:
                if thru or not (abs(lo - (y + h)) < 1.5 or abs(hi - y) < 1.5):
                    return True
        return False
    return True


def path_blocked(pts, boxes, skip, tol=3.0):
    for a, b in zip(pts, pts[1:]):
        if seg_blocked(a[0], a[1], b[0], b[1], boxes, skip, tol):
            return True
    return False


def channel_for(ls, lt, srs, srt, meta):
    bt = meta["band_top"]
    ly = meta["lane_y"]
    lh = meta["lane_h"]
    order = [l[0] for l in meta["lanes"]]
    if ls == lt:
        if srs == srt:
            return bt[ls] + srs * SUBROW_H
        return bt[ls] + (min(srs, srt) + 1) * SUBROW_H
    li_s = order.index(ls) if ls in order else 0
    li_t = order.index(lt) if lt in order else 0
    if abs(li_s - li_t) == 1:
        top = min(li_s, li_t)
        return ly[order[top]] + lh[order[top]]
    if li_s < li_t:
        return ly[order[li_s]] + lh[order[li_s]]
    return ly[order[li_t]] + lh[order[li_t]]


def route(s, t, pos, meta, idx):
    if s not in pos or t not in pos:
        return []
    sp, tp = pos[s], pos[t]
    cs, ct = meta["rank"].get(s, 0), meta["rank"].get(t, 0)
    ls, lt = meta["node_lane"].get(s), meta["node_lane"].get(t)
    sy, ty = sp[5], tp[5]
    sx, tx = sp[0] + sp[2], tp[0]
    boxes = pos
    skip = {s, t}
    srs, srt = meta["subrow"].get(s, 0), meta["subrow"].get(t, 0)
    if ct > cs:
        if abs(sy - ty) < 1.5 and not seg_blocked(sx, sy, tx, ty, boxes, skip):
            return [(sx, sy), (tx, ty)]
        ych = channel_for(ls, lt, srs, srt, meta)
        for yo in ([0] + OFFS_FINE):
            yc = ych + yo
            for xo1 in OFFS_X:
                for xo2 in OFFS_X:
                    x1 = strip_right(cs, xo1)
                    x2 = strip_left(ct, xo2)
                    pts = [(sx, sy), (x1, sy), (x1, yc), (x2, yc), (x2, ty), (tx, ty)]
                    if not path_blocked(dedupe(pts), boxes, skip):
                        return dedupe(pts)
        x1 = strip_right(cs, OFFS[idx % 5])
        x2 = strip_left(ct, OFFS[(idx // 5) % 5])
        pts = [(sx, sy), (x1, sy), (x1, ych), (x2, ych), (x2, ty), (tx, ty)]
        return dedupe(pts)
    else:
        for k in range(6):
            loop = meta["pool_bottom"] + LOOP_GAP + ((idx + k) % 12) * CORRIDOR
            for xo1 in OFFS_X:
                for xo2 in OFFS_X:
                    x1 = strip_right(cs, xo1)
                    x2 = strip_left(ct, xo2)
                    pts = [(sx, sy), (x1, sy), (x1, loop), (x2, loop), (x2, ty), (tx, ty)]
                    if not path_blocked(dedupe(pts), boxes, skip):
                        return dedupe(pts)
        loop = meta["pool_bottom"] + LOOP_GAP + (idx % 12) * CORRIDOR
        x1 = strip_right(cs, OFFS[idx % 5])
        x2 = strip_left(ct, OFFS[(idx // 5) % 5])
        pts = [(sx, sy), (x1, sy), (x1, loop), (x2, loop), (x2, ty), (tx, ty)]
        return dedupe(pts)


def dedupe(pts):
    out = [pts[0]]
    for p in pts[1:]:
        if abs(p[0] - out[-1][0]) > 0.5 or abs(p[1] - out[-1][1]) > 0.5:
            out.append(p)
    return out


def label_bounds(pts, pos):
    best = None
    bl = 0
    for a, b in zip(pts, pts[1:]):
        l = abs(a[0] - b[0]) + abs(a[1] - b[1])
        if l > bl:
            bl = l
            best = (a, b)
    if best is None or bl < 60:
        return None
    (ax, ay), (bx, by) = best
    cands = []
    if abs(ay - by) < 0.5:
        mx, my = (ax + bx) / 2, (ay + by) / 2
        cands = [(mx - 35, my - 24, 70, 14), (mx - 35, my + 10, 70, 14)]
    else:
        mx, my = (ax + bx) / 2, (ay + by) / 2
        cands = [(mx + 10, my - 7, 70, 14), (mx - 80, my - 7, 70, 14)]
    for lx, ly, lw, lh in cands:
        hit = False
        for nid, v in pos.items():
            x, y, w, h = _box4(v)
            ox = min(lx + lw, x + w) - max(lx, x)
            oy = min(ly + lh, y + h) - max(ly, y)
            if ox > 3 and oy > 3:
                hit = True
                break
        if not hit:
            return (lx, ly, lw, lh)
    return None


def build_di(root, pos, apos, lane_bounds, flows, meta):
    diagram = root.find(".//%sBPMNDiagram" % Q["bpmndi"])
    if diagram is None:
        diagram = ET.SubElement(root, "%sBPMNDiagram" % Q["bpmndi"])
        diagram.set("id", "BPMNDiagram_1")
    for child in list(diagram):
        diagram.remove(child)
    proc = root.find(".//%sprocess" % Q["bpmn"])
    plane = ET.SubElement(diagram, "%sBPMNPlane" % Q["bpmndi"])
    plane.set("id", "BPMNPlane_1")
    plane.set("bpmnElement", proc.get("id"))
    laneset = proc.find("%slaneSet" % Q["bpmn"])
    if laneset is not None:
        for lane in laneset.findall("%slane" % Q["bpmn"]):
            lid = lane.get("id")
            if lid in lane_bounds:
                lx, ly, lw, lh = lane_bounds[lid]
                sh = ET.SubElement(plane, "%sBPMNShape" % Q["bpmndi"])
                sh.set("id", lid + "_di")
                sh.set("bpmnElement", lid)
                b = ET.SubElement(sh, "%sBounds" % Q["dc"])
                b.set("x", str(int(lx))); b.set("y", str(int(ly)))
                b.set("width", str(int(lw))); b.set("height", str(int(lh)))
    for nid, (x, y, w, h, cx, cy) in pos.items():
        sh = ET.SubElement(plane, "%sBPMNShape" % Q["bpmndi"])
        sh.set("id", nid + "_di")
        sh.set("bpmnElement", nid)
        b = ET.SubElement(sh, "%sBounds" % Q["dc"])
        b.set("x", str(int(round(x)))); b.set("y", str(int(round(y))))
        b.set("width", str(int(round(w)))); b.set("height", str(int(round(h))))
    for nid, (x, y, w, h, cx, cy) in apos.items():
        sh = ET.SubElement(plane, "%sBPMNShape" % Q["bpmndi"])
        sh.set("id", nid + "_di")
        sh.set("bpmnElement", nid)
        b = ET.SubElement(sh, "%sBounds" % Q["dc"])
        b.set("x", str(int(round(x)))); b.set("y", str(int(round(y))))
        b.set("width", str(int(round(w)))); b.set("height", str(int(round(h))))
    ordered = sorted(flows.items(), key=lambda kv: (meta["rank"].get(kv[1][0], 0), kv[0]))
    for idx, (fid, (s, t, name)) in enumerate(ordered):
        pts = route(s, t, pos, meta, idx)
        if not pts:
            continue
        se = ET.SubElement(plane, "%sBPMNEdge" % Q["bpmndi"])
        se.set("id", fid + "_di")
        se.set("bpmnElement", fid)
        for px, py in pts:
            wp = ET.SubElement(se, "%swaypoint" % Q["di"])
            wp.set("x", str(int(round(px)))); wp.set("y", str(int(round(py))))
        if name:
            lb = label_bounds(pts, pos)
            if lb:
                lbl = ET.SubElement(se, "%sBPMNLabel" % Q["bpmndi"])
                bb = ET.SubElement(lbl, "%sBounds" % Q["dc"])
                bb.set("x", str(int(round(lb[0])))); bb.set("y", str(int(round(lb[1]))))
                bb.set("width", str(int(round(lb[2])))); bb.set("height", str(int(round(lb[3]))))


def relayout_file(path):
    try:
        tree = ET.parse(path)
    except ET.ParseError as e:
        print(f"  PARSE ERROR {path}: {e}")
        return False
    root = tree.getroot()
    parsed = parse(root)
    if parsed is None:
        print(f"  NO PROCESS {path}")
        return False
    proc, lanes, node_lane, nodes, flows, artifacts = parsed
    if not nodes:
        print(f"  EMPTY {path}")
        return False
    pos, apos, lane_bounds, meta = layout(proc, lanes, node_lane, nodes, flows, artifacts)
    build_di(root, pos, apos, lane_bounds, flows, meta)
    bak = path + ".prelayout"
    if not os.path.exists(bak):
        shutil.copy2(path, bak)
    tree.write(path, xml_declaration=True, encoding="UTF-8")
    print(f"  relaid out {os.path.basename(path)}: {len(nodes)} nodes, "
          f"{len(flows)} flows, {len(meta['back'])} back-edges, canvas {int(LEFT_PAD + (max(meta['rank'].values()) if meta['rank'] else 0) + 1) * COL_W + 80}x{int(meta['total_h'])}")
    return True


def main():
    files = []
    for d in DIRS:
        if os.path.isdir(d):
            for fn in sorted(os.listdir(d)):
                if fn.endswith(".bpmn") and not fn.endswith(".bak") and not fn.endswith(".prelayout"):
                    files.append(os.path.join(d, fn))
    if not files:
        print("No BPMN files found")
        return
    ok = 0
    for f in files:
        if relayout_file(f):
            ok += 1
    print(f"\nDone. Relaid out {ok}/{len(files)} files.")


if __name__ == "__main__":
    main()

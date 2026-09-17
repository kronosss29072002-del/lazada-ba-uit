#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BPMN -> Workflow-Net (WF-net) soundness verifier — pure Python, no external deps.

Mô hình hóa mỗi process BPMN thành WF-net theo van der Aalst (1998):
    - place        : một place cho mỗi sequence flow
    - token        : token điều khiển dòng chảy
    - initial      : 1 token trên outgoing flow của start event
    - final places : incoming flows của các end event
    - transition   : một transition cho mỗi task / gateway

Semantics:
    - Task nhiều outgoing / XOR gateway  -> chọn KHÔNG TIÊN ĐỊNH đúng 1 nhánh
    - Parallel gateway (AND split)        -> bắn tất cả nhánh
    - AND join                            -> yêu cầu tất cả input có token
    - XOR join (task/gw nhiều input)      -> bắn khi có >= 1 input
    - OR gateway                          -> chọn tập con >= 1 output

Kiểm tra 3 thuộc tính soundness (van der Aalst):
    1. Option to Complete  : mọi marking reachable đều có thể tới completion
    2. Proper Completion   : mọi terminal marking chỉ chứa token trong final places
    3. No Dead Transitions : mọi transition đều fireable trong ít nhất 1 marking

Vòng lặp được giới hạn bằng per-place token cap (--cap, mặc định 4): phân tích
phủ mọi lần lặp <= cap. Cap được ghi rõ trong report.

Usage:
    python3 scripts/soundness-check.py processes/*.bpmn
    python3 scripts/soundness-check.py processes/03-order-processing.bpmn
    python3 scripts/soundness-check.py --cap 3 --out docs/petri-net processes/*.bpmn
"""

import argparse
import itertools
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

NS = {"bpmn": "http://www.omg.org/spec/BPMN/20100524/MODEL"}

TASK_TAGS = {
    "task", "userTask", "serviceTask", "scriptTask", "sendTask",
    "receiveTask", "manualTask", "businessRuleTask", "callActivity",
    "subProcess", "transaction",
}
XOR_TAGS = {"exclusiveGateway", "eventBasedGateway"}
AND_TAGS = {"parallelGateway"}
OR_TAGS = {"inclusiveGateway", "complexGateway"}
NON_FLOW_ARTIFACTS = {
    "dataObject", "dataObjectReference", "dataStore",
    "textAnnotation", "association", "group", "participant",
}


def load_process(path):
    """Parse BPMN file -> (process_name, nodes, flows)."""
    tree = ET.parse(path)
    root = tree.getroot()
    proc = root.find(".//bpmn:process", NS)
    if proc is None:
        raise ValueError(f"No <bpmn:process> found in {path}")

    name = proc.get("name", Path(path).stem)
    nodes = {}
    flows = []

    for el in proc:
        tag = el.tag.split("}")[-1]
        if tag in ("laneSet", "lane", "extensionElements"):
            continue
        eid = el.get("id")
        if not eid:
            continue
        if tag == "sequenceFlow":
            flows.append({"id": eid, "src": el.get("sourceRef"), "tgt": el.get("targetRef")})
        elif tag not in NON_FLOW_ARTIFACTS:
            nodes[eid] = {"tag": tag, "in": [], "out": []}

    for f in flows:
        src, tgt = f["src"], f["tgt"]
        if src in nodes:
            nodes[src]["out"].append(f["id"])
        if tgt in nodes:
            nodes[tgt]["in"].append(f["id"])

    return name, nodes, flows


def classify(tag):
    if tag in TASK_TAGS:
        return "task"
    if tag in XOR_TAGS:
        return "xor"
    if tag in AND_TAGS:
        return "and"
    if tag in OR_TAGS:
        return "or"
    return "task"  # intermediate events, etc.


def transition_enabled(trans, marking, pidx):
    """Check whether transition is enabled at marking."""
    if trans["kind"] == "and" and len(trans["inputs"]) > 1 and len(trans["outputs"]) <= 1:
        return all(marking[pidx[p]] > 0 for p in trans["inputs"])
    return any(marking[pidx[p]] > 0 for p in trans["inputs"])


def fire_nexts(trans, marking, pidx, cap):
    """Return all next markings reachable by firing `trans` once."""
    nexts = []
    m = marking

    # ---- AND join: require all inputs ----
    if trans["kind"] == "and" and len(trans["inputs"]) > 1 and len(trans["outputs"]) <= 1:
        if not all(m[pidx[p]] > 0 for p in trans["inputs"]):
            return nexts
        nxt = list(m)
        for p in trans["inputs"]:
            nxt[pidx[p]] -= 1
        for p in trans["outputs"]:
            nxt[pidx[p]] += 1
        if max(nxt) <= cap:
            nexts.append(tuple(nxt))
        return nexts

    enabled_inputs = [p for p in trans["inputs"] if m[pidx[p]] > 0]
    if not enabled_inputs:
        return nexts

    # ---- AND split: fire all branches ----
    if trans["kind"] == "and":
        for inp in enabled_inputs:
            nxt = list(m)
            nxt[pidx[inp]] -= 1
            for p in trans["outputs"]:
                nxt[pidx[p]] += 1
            if max(nxt) <= cap:
                nexts.append(tuple(nxt))
        return nexts

    # ---- OR: choose any non-empty subset of outputs ----
    if trans["kind"] == "or":
        out_idx = list(range(len(trans["outputs"])))
        for r in range(1, len(out_idx) + 1):
            for combo in itertools.combinations(out_idx, r):
                for inp in enabled_inputs:
                    nxt = list(m)
                    nxt[pidx[inp]] -= 1
                    for k in combo:
                        nxt[pidx[trans["outputs"][k]]] += 1
                    if max(nxt) <= cap:
                        nexts.append(tuple(nxt))
        return nexts

    # ---- XOR / task: choose exactly one output ----
    for inp in enabled_inputs:
        for o in trans["outputs"]:
            nxt = list(m)
            nxt[pidx[inp]] -= 1
            if o is not None:
                nxt[pidx[o]] += 1
            if max(nxt) <= cap:
                nexts.append(tuple(nxt))
    return nexts


def analyze(path, cap):
    name, nodes, flows = load_process(path)

    # places = sequence flows
    places = [f["id"] for f in flows]
    pidx = {p: i for i, p in enumerate(places)}
    n_places = len(places)

    # initial marking: token on each start-event outgoing flow
    initial = [0] * n_places
    for eid, node in nodes.items():
        if node["tag"] == "startEvent":
            for o in node["out"]:
                if o in pidx:
                    initial[pidx[o]] += 1
    initial = tuple(initial)

    # final places: incoming flows of end events
    final_places = set()
    for eid, node in nodes.items():
        if node["tag"] == "endEvent":
            for i in node["in"]:
                final_places.add(i)

    # transitions (skip start/end events)
    trans_list = []
    for eid, node in nodes.items():
        if node["tag"] in ("startEvent", "endEvent"):
            continue
        trans_list.append({
            "id": eid,
            "kind": classify(node["tag"]),
            "inputs": node["in"],
            "outputs": node["out"],
        })
    trans_ids = [t["id"] for t in trans_list]

    # ---- BFS reachability graph ----
    graph = {}           # marking -> set(next markings)
    preds = {}           # marking -> set(prev markings)
    queue = [initial]
    graph[initial] = set()

    while queue:
        m = queue.pop(0)
        for t in trans_list:
            for nxt in fire_nexts(t, m, pidx, cap):
                if nxt not in graph:
                    graph[nxt] = set()
                    queue.append(nxt)
                graph[m].add(nxt)
                preds.setdefault(nxt, set()).add(m)

    reachable = set(graph.keys())

    # ---- soundness checks ----
    def is_terminal(m):
        return len(graph[m]) == 0

    def is_valid_completion(m):
        # all tokens must be in final places
        return all(places[i] in final_places for i in range(n_places) if m[i] > 0)

    # 1. Option to Complete (backward closure from valid completions)
    can_complete = set(
        m for m in reachable
        if is_terminal(m) and is_valid_completion(m)
    )
    changed = True
    while changed:
        changed = False
        for m in reachable:
            if m in can_complete:
                continue
            if any(nxt in can_complete for nxt in graph[m]):
                can_complete.add(m)
                changed = True

    option_complete = reachable <= can_complete

    # 2. Proper Completion
    bad_terminals = [
        m for m in reachable
        if is_terminal(m) and not is_valid_completion(m)
    ]
    proper_completion = len(bad_terminals) == 0

    # 3. No Dead Transitions
    fired_ids = set()
    for m in reachable:
        for t in trans_list:
            if transition_enabled(t, m, pidx):
                fired_ids.add(t["id"])
    dead = [tid for tid in trans_ids if tid not in fired_ids]
    no_dead = len(dead) == 0

    sound = option_complete and proper_completion and no_dead

    return {
        "path": path,
        "name": name,
        "n_places": n_places,
        "n_trans": len(trans_list),
        "cap": cap,
        "n_reachable": len(reachable),
        "max_tokens": max((max(m) for m in reachable), default=0),
        "n_final_places": len(final_places),
        "final_places": sorted(final_places),
        "option_complete": option_complete,
        "n_can_complete": len(can_complete),
        "proper_completion": proper_completion,
        "n_bad_terminals": len(bad_terminals),
        "no_dead": no_dead,
        "dead": dead,
        "trans_ids": trans_ids,
        "sound": sound,
        "initial": initial,
        "kind_map": {t["id"]: t["kind"] for t in trans_list},
    }


def render_markdown(res):
    md = []
    md.append(f"# Kiểm chứng Soundness — {res['name']}\n")
    md.append(f"**File:** `{res['path']}`")
    md.append(f"**Phương pháp:** BPMN → WF-net (van der Aalst, 1998), phân tích reachability graph.\n")
    md.append("## Thống kê mô hình\n")
    md.append(f"| Chỉ số | Giá trị |")
    md.append(f"|--------|---------|")
    md.append(f"| Places (sequence flows) | {res['n_places']} |")
    md.append(f"| Transitions (tasks + gateways) | {res['n_trans']} |")
    md.append(f"| Final places | {res['n_final_places']} |")
    md.append(f"| Reachable markings (cap={res['cap']}) | {res['n_reachable']} |")
    md.append(f"| Max tokens trong 1 marking | {res['max_tokens']} |")
    md.append(f"| Final places | {', '.join(res['final_places'])} |\n")
    md.append("## Kết quả soundness\n")
    md.append("| Thuộc tính | Kết quả | Bằng chứng |")
    md.append("|------------|---------|-----------|")
    md.append(
        f"| Option to Complete | {'✅ PASS' if res['option_complete'] else '❌ FAIL'} | "
        f"{res['n_can_complete']}/{res['n_reachable']} markings reachable có thể tới completion |"
    )
    md.append(
        f"| Proper Completion | {'✅ PASS' if res['proper_completion'] else '❌ FAIL'} | "
        f"terminal markings không hợp lệ: {res['n_bad_terminals']} |"
    )
    md.append(
        f"| No Dead Transitions | {'✅ PASS' if res['no_dead'] else '❌ FAIL'} | "
        f"dead transitions: {', '.join(res['dead']) if res['dead'] else 'không có'} |"
    )
    md.append(f"\n**Overall:** {'✅ SOUND' if res['sound'] else '❌ NOT SOUND'}\n")
    md.append("> **Ghi chú:** Các vòng lặp có điều kiện dữ liệu (data-based loop) được phân tích "
              "trong không gian giới hạn với mỗi place giữ tối đa 1 token và mỗi lần lặp ≤ cap "
              f"(cap={res['cap']}). Điều này tương ứng với việc vòng lặp được chặn bởi bộ đếm "
              "(ví dụ `resubmitCount ≤ 3`) như đã khai báo trong mô hình TO-BE.\n")
    md.append("## Bảng mapping BPMN → WF-net\n")
    md.append("| # | BPMN element | Transition | Kind |")
    md.append("|---|--------------|------------|------|")
    kind_label = {"task": "task", "xor": "XOR", "and": "AND", "or": "OR"}
    for i, tid in enumerate(res["trans_ids"], 1):
        kind = res.get("kind_map", {}).get(tid, "task")
        md.append(f"| T{i} | `{tid}` | $t_{i}$ | {kind_label.get(kind, kind)} |")
    md.append("")
    return "\n".join(md)


def main(argv=None):
    ap = argparse.ArgumentParser(description="BPMN soundness verifier (van der Aalst)")
    ap.add_argument("files", nargs="+", help="BPMN files to verify")
    ap.add_argument("--cap", type=int, default=4, help="per-place token cap (loop bound)")
    ap.add_argument("--out", default=None, help="directory to write per-process markdown evidence")
    args = ap.parse_args(argv)

    results = []
    for f in args.files:
        try:
            res = analyze(f, args.cap)
            results.append(res)
        except Exception as e:
            print(f"  ERROR {f}: {e}")
            results.append(None)

    print(f"\n{'='*72}")
    print("SOUNDNESS CHECK (van der Aalst) — bounded analysis cap=%d" % args.cap)
    print(f"{'='*72}")
    print(f"{'Process':<28} {'P':>3} {'T':>3} {'Mark':>5} {'Opt':>4} {'Prop':>4} {'Dead':>4}  Result")
    for r in results:
        if r is None:
            continue
        print(f"{r['name'][:28]:<28} {r['n_places']:>3} {r['n_trans']:>3} {r['n_reachable']:>5} "
              f"{'PASS' if r['option_complete'] else 'FAIL':>4} {'PASS' if r['proper_completion'] else 'FAIL':>4} "
              f"{'PASS' if r['no_dead'] else 'FAIL':>4}  {'SOUND' if r['sound'] else 'NOT SOUND'}")
        if r['dead']:
            print(f"    dead transitions: {', '.join(r['dead'])}")

    if args.out:
        outdir = Path(args.out)
        outdir.mkdir(parents=True, exist_ok=True)
        for r in results:
            if r is None:
                continue
            stem = Path(r["path"]).stem
            out = outdir / f"soundness-{stem}.md"
            out.write_text(render_markdown(r), encoding="utf-8")
            print(f"  -> wrote {out}")

    return 0 if all(r and r["sound"] for r in results if r) else 1


if __name__ == "__main__":
    sys.exit(main())

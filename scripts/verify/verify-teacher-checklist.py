#!/usr/bin/env python3
"""Verify GVHD teacher-checklist rules across all 20 BPMN files (AS-IS + TO-BE).

Rules extracted from GVHD ThS. Hà Lê Hoài Trung — Buổi 10 (17/09/2026):
  1. BRANCH LABELS — "Nhãn cổng thì có, nhãn nhánh thì không có": mọi split
     gateway (>= 2 outgoing) phải có nhãn trên TẤT CẢ các nhánh (name trên
     sequenceFlow).
  2. GATEWAY NAMES — mọi gateway phải có tên.
  3. 1-IN-1-OUT — mọi activity (task/callActivity/subProcess) có đúng 1
     incoming + 1 outgoing sequence flow.
  4. MESSAGE FLOW — messageFlow chỉ được nối 2 process/pool KHÁC NHAU
     (không có message flow giữa 2 node trong cùng 1 pool).
  5. REACHABILITY — mọi activity trong 1 process phải đạt được từ startEvent
     của process đó qua chuỗi sequenceFlow (BFS).
  6. FILE COVERAGE — 20 file bpmn (10 AS-IS + 10 TO-BE) bắt buộc đủ.

Usage:  python3 scripts/verify/verify-teacher-checklist.py
Exit:   0 = PASS toàn bộ, 1 = FAIL (in danh sách vi phạm).
"""
import os
import sys
import glob
try:
    from defusedxml import ElementTree as ET  # XXE-safe parser
except ImportError:
    import xml.etree.ElementTree as ET

BPMN_NS = 'http://www.omg.org/spec/BPMN/20100524/MODEL'
PROJECT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

TASK_TAGS = {
    'task', 'userTask', 'serviceTask', 'scriptTask', 'businessRuleTask',
    'manualTask', 'sendTask', 'receiveTask', 'callActivity', 'subProcess',
}
GATEWAY_TAGS = {
    'exclusiveGateway', 'parallelGateway', 'inclusiveGateway',
    'eventBasedGateway', 'complexGateway',
}
EVENT_TAGS = {
    'startEvent', 'endEvent', 'intermediateCatchEvent', 'intermediateThrowEvent',
    'boundaryEvent',
}
FLOW_TAGS = {'sequenceFlow', 'messageFlow', 'eventFlow'}


def q(tag):
    return f'{{{BPMN_NS}}}{tag}'


def walk(el):
    yield el
    for child in el:
        yield from walk(child)


def is_activity(el):
    return el.tag in {q(t) for t in TASK_TAGS}


def is_gateway(el):
    return el.tag in {q(t) for t in GATEWAY_TAGS}


def is_start(el):
    return el.tag == q('startEvent')


def node_kind(el):
    if is_activity(el):
        return 'activity'
    if is_gateway(el):
        return 'gateway'
    if el.tag in {q(t) for t in EVENT_TAGS}:
        return 'event'
    return 'other'


def load(path):
    return ET.parse(path).getroot()


def collect_nodes_and_flows(root):
    """Return (nodes_by_id, flows list, container info)."""
    nodes = {}
    flows = []
    for el in walk(root):
        eid = el.get('id')
        if eid:
            kind = node_kind(el)
            if kind != 'other':
                nodes[eid] = {'el': el, 'kind': kind, 'name': el.get('name')}
        if el.tag == q('sequenceFlow'):
            flows.append(el)
    return nodes, flows


def split_by_process(root):
    """Group elements into process containers (for reachability per process)."""
    containers = {}   # process_id -> element tag
    for el in walk(root):
        if el.tag == q('process'):
            containers[el.get('id')] = el
    return containers


def main():
    files = sorted(
        glob.glob(os.path.join(PROJECT, 'processes', '*.bpmn'))
        + glob.glob(os.path.join(PROJECT, 'processes-to-be', '*.bpmn'))
    )
    results = []          # (file, rule, message)
    passed_files = 0

    if len(files) != 20:
        results.append(('*', 'FILE_COVERAGE',
                        f'Cần đủ 20 file BPMN (10 AS-IS + 10 TO-BE), tìm thấy {len(files)}'))

    for path in files:
        rel = os.path.relpath(path, PROJECT)
        root = load(path)
        nodes, seq_flows = collect_nodes_and_flows(root)
        processes = split_by_process(root)

        # ---- message flow: only between different pools/processes ----
        for el in walk(root):
            if el.tag == q('messageFlow'):
                src = el.get('sourceRef')
                tgt = el.get('targetRef')
                # find owning process of src/tgt
                owner = {}
                for pid, proc in processes.items():
                    for sub in walk(proc):
                        if sub.get('id') in (src, tgt):
                            owner[sub.get('id')] = pid
                if src in owner and tgt in owner and owner[src] == owner[tgt]:
                    results.append((rel, 'MESSAGE_FLOW',
                                    f'messageFlow "{el.get("id")}" nối 2 node trong CÙNG pool (owner={owner[src]})'))
                elif src not in owner or tgt not in owner:
                    results.append((rel, 'MESSAGE_FLOW',
                                    f'messageFlow "{el.get("id")}" nối node không thuộc process nào'))

        # ---- outgoing-by-node ----
        outgoing = {}
        incoming = {}
        for el in seq_flows:
            src = el.get('sourceRef')
            tgt = el.get('targetRef')
            if src in nodes:
                outgoing.setdefault(src, []).append(el)
            if tgt in nodes:
                incoming.setdefault(tgt, []).append(el)

        # ---- R1: branch labels on split gateways ----
        for nid, info in nodes.items():
            if info['kind'] != 'gateway':
                continue
            outs = outgoing.get(nid, [])
            if len(outs) >= 2:
                for el in outs:
                    label = (el.get('name') or '').strip()
                    if not label:
                        results.append((rel, 'BRANCH_LABEL',
                                        f'Gateway "{nid}" ({info["name"] or "?"}) có nhánh KHÔNG nhãn: sequenceFlow "{el.get("id")}"'))

        # ---- R2: gateway names ----
        for nid, info in nodes.items():
            if info['kind'] == 'gateway' and not (info['name'] or '').strip():
                results.append((rel, 'GATEWAY_NAME', f'Gateway "{nid}" thiếu tên'))

        # ---- R3: 1-in-1-out on activities ----
        for nid, info in nodes.items():
            if info['kind'] != 'activity':
                continue
            n_in = len(incoming.get(nid, []))
            n_out = len(outgoing.get(nid, []))
            if n_in != 1 or n_out != 1:
                results.append((rel, '1IN1OUT',
                                f'Activity "{nid}" ({info["name"] or "?"}): in={n_in} out={n_out} (phải 1-1)'))

        # ---- R5: reachability per process ----
        for pid, proc in processes.items():
            proc_ids = {sub.get('id') for sub in walk(proc) if sub.get('id')}
            starts = [nid for nid in proc_ids
                      if nid in nodes and nodes[nid]['el'].tag == q('startEvent')]
            if not starts:
                results.append((rel, 'REACHABILITY', f'Process "{pid}" KHÔNG có startEvent'))
                continue
            # BFS over sequence flows restricted to this process
            seen = set(starts)
            queue = list(starts)
            # also treat flows crossing process boundary conservatively
            edge = {}
            for el in seq_flows:
                edge.setdefault(el.get('sourceRef'), []).append(el.get('targetRef'))
            while queue:
                cur = queue.pop()
                for nxt in edge.get(cur, []):
                    if nxt in nodes and nxt not in seen:
                        seen.add(nxt)
                        queue.append(nxt)
            for nid, info in nodes.items():
                if info['kind'] in ('activity', 'gateway') and nid not in seen and nid in proc_ids:
                    results.append((rel, 'REACHABILITY',
                                    f'Node "{nid}" ({info["name"] or "?"}) KHÔNG đạt được từ startEvent'))

        # ---- file-level pass count ----
        file_fail = any(r[0] == rel for r in results)
        if not file_fail:
            passed_files += 1

    # ---- report ----
    print(f'Teacher Checklist (GVHD Buổi 10) — {len(files)} files BPMN')
    print('=' * 78)
    if not results:
        print('✅ PASS — 0 vi phạm trên toàn bộ 5 quy tắc (branch labels / gateway names / 1-in-1-out / message-flow / reachability).')
        return 0

    # group by file
    from collections import defaultdict
    by_file = defaultdict(list)
    for rel, rule, msg in results:
        by_file[rel].append((rule, msg))
    for rel in sorted(by_file):
        print(f'\n❌ {rel}:')
        for rule, msg in by_file[rel]:
            print(f'   [{rule}] {msg}')
    print(f'\n⚠️  {len(results)} vi phạm trên {len(by_file)}/{len(files)} files — FAIL.')
    return 1


if __name__ == '__main__':
    sys.exit(main())
#!/usr/bin/env python3
"""Precise 1-in-1-out checker for BPMN tasks/events (gateways allowed multi).

Teacher rule (GHI-CHU-THAY-DAN.md):
- "Mỗi hoạt động chỉ có 1 input và 1 output" - activities only
- "Khi tách bằng gateway thì phải gom lại bằng gateway đóng (join) tương ứng"
- Gateways (exclusive/parallel/inclusive) may have N in / N out.
"""
import xml.etree.ElementTree as ET
import glob, sys

NS = 'http://www.omg.org/spec/BPMN/20100524/MODEL'
TASK_TAGS = ('task', 'userTask', 'serviceTask', 'businessRuleTask', 'manualTask',
             'scriptTask', 'sendTask', 'receiveTask', 'callActivity', 'subProcess',
             'transaction', 'task', 'startEvent', 'endEvent', 'intermediateCatchEvent',
             'intermediateThrowEvent', 'boundaryEvent')
FLOW_NODE_TAGS = TASK_TAGS + ('exclusiveGateway', 'parallelGateway',
                              'inclusiveGateway', 'complexGateway', 'eventBasedGateway')

def local(tag):
    return tag.split('}')[-1] if '}' in tag else tag

def analyze(path, check_gateways=False):
    tree = ET.parse(path)
    root = tree.getroot()

    seen_ids = {}
    elements = {}
    for elem in root.iter():
        tag = local(elem.tag)
        if tag in FLOW_NODE_TAGS or tag == 'sequenceFlow':
            eid = elem.get('id')
            if eid in seen_ids:
                seen_ids[eid].append(tag)
            else:
                seen_ids[eid] = [tag]
            if tag in FLOW_NODE_TAGS:
                elements[eid] = {
                    'tag': tag,
                    'name': (elem.get('name') or '').strip() or eid,
                    'ins': [], 'outs': [],
                }

    for flow in root.iter():
        if local(flow.tag) == 'sequenceFlow':
            src, tgt = flow.get('sourceRef'), flow.get('targetRef')
            if src in elements: elements[src]['outs'].append(flow.get('id'))
            if tgt in elements: elements[tgt]['ins'].append(flow.get('id'))

    issues = []
    dup_ids = {k: v for k, v in seen_ids.items() if len(v) > 1}
    if dup_ids:
        issues.append(f"  [CRITICAL] Duplicate element IDs: {dup_ids}")

    for eid, info in elements.items():
        tag = info['tag']
        nin, nout = len(info['ins']), len(info['outs'])

        if tag == 'startEvent':
            if nin != 0: issues.append(f"  [VIOLATION] startEvent '{info['name']}' has {nin} inputs")
            if nout > 1 and not check_gateways:
                issues.append(f"  [INFO] startEvent '{info['name']}' splits to {nout} outputs")
        elif tag == 'endEvent':
            if nout != 0: issues.append(f"  [VIOLATION] endEvent '{info['name']}' has {nout} outputs")
            if nin > 1:
                issues.append(f"  [VIOLATION] endEvent '{info['name']}' has {nin} inputs (merge via join gateway)")
        elif tag in ('exclusiveGateway', 'parallelGateway', 'inclusiveGateway',
                     'complexGateway', 'eventBasedGateway'):
            if not check_gateways:
                continue
            if nin <= 1 and nout <= 1:
                issues.append(f"  [INFO] gateway '{info['name']}' has {nin} in / {nout} out (no real split/merge)")
        else:
            if nin != 1:
                issues.append(f"  [VIOLATION] {tag} '{info['name']}' [{eid}] has {nin} inputs (must be 1)")
            if nout != 1:
                issues.append(f"  [VIOLATION] {tag} '{info['name']}' [{eid}] has {nout} outputs (must be 1)")
    return issues, dup_ids

def main():
    files = sys.argv[1:] if len(sys.argv) > 1 else \
        sorted(glob.glob('processes/*.bpmn')) + sorted(glob.glob('processes-to-be/*.bpmn'))
    total_violations = 0
    for path in files:
        issues, dups = analyze(path)
        violations = [i for i in issues if '[VIOLATION]' in i]
        critical = [i for i in issues if '[CRITICAL]' in i]
        if issues:
            print(f"\n{'='*70}\n{path}:")
            for i in issues:
                print(i)
            total_violations += len(violations)
        else:
            print(f"✅ {path}: CLEAN (all tasks 1-in/1-out, no duplicate IDs)")
    print(f"\n{'='*70}\nTOTAL VIOLATIONS: {total_violations}")

if __name__ == '__main__':
    main()
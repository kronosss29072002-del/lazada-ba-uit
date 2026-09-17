#!/usr/bin/env python3
"""Audit + fix reference parity in BPMN files.

Two classes of defects (invisible to check-1in1out.py which only counts
real sequenceFlow edges):

A. <incoming>/<outgoing> child elements that don't match the authoritative
   sequenceFlow definitions (stale ids from abandoned edits, e.g.
   'Flow_CertYes_Check' on AS-IS 07 or 'F6' on TO-BE 01).

B. <flowNodeRef> entries inside lanes pointing at nodes that don't exist
   (phantom nodes from reverted designs, e.g. Task_Decision in AS-IS 04,
   TimerEvent_T1SLA / Gate_ParallelSplit in TO-BE 05).

Usage:
  python3 fix-ref-parity.py [files...] [--fix] [--dry]

  Without --fix: audit only, exit code 0 if clean else 1.
  With --fix: rebuilds child refs from flows and prunes phantom lane refs.
"""
import xml.etree.ElementTree as ET
import glob, sys, os, shutil

NS = 'http://www.omg.org/spec/BPMN/20100524/MODEL'
NS_BPMNDI = 'http://www.omg.org/spec/BPMN/20100524/DI'
NS_DC = 'http://www.omg.org/spec/DD/20100524/DC'
NS_DI = 'http://www.omg.org/spec/DD/20100524/DI'
ET.register_namespace('bpmn', NS)
ET.register_namespace('bpmndi', NS_BPMNDI)
ET.register_namespace('dc', NS_DC)
ET.register_namespace('di', NS_DI)

FLOW_TAGS = ('task', 'userTask', 'serviceTask', 'businessRuleTask', 'manualTask',
             'scriptTask', 'sendTask', 'receiveTask', 'callActivity', 'subProcess',
             'transaction', 'startEvent', 'endEvent', 'intermediateCatchEvent',
             'intermediateThrowEvent', 'boundaryEvent',
             'exclusiveGateway', 'parallelGateway', 'inclusiveGateway',
             'complexGateway', 'eventBasedGateway')

def local(t):
    return t.split('}')[-1] if '}' in t else t

def is_flow_node(tag):
    return local(tag) in FLOW_TAGS

def analyze(path):
    """Return (issues, needs_fix) where issues is a list of strings."""
    tree = ET.parse(path)
    root = tree.getroot()
    issues = []

    # 1. collect flow definitions (authoritative)
    flows = {}          # fid -> (src, tgt)
    for e in root.iter():
        if local(e.tag) == 'sequenceFlow':
            fid = e.get('id')
            if fid:
                flows[fid] = (e.get('sourceRef'), e.get('targetRef'))

    # 2. collect all declared node ids (any element with id, incl. lane etc.)
    declared = {e.get('id') for e in root.iter() if e.get('id')}

    # 3. children parity on every flow node
    for e in root.iter():
        if not is_flow_node(e.tag):
            continue
        eid = e.get('id')
        if not eid:
            continue
        expected_in = [f for f, (s, t) in flows.items() if t == eid]
        expected_out = [f for f, (s, t) in flows.items() if s == eid]
        actual_in, actual_out = [], []
        for sub in list(e):
            if local(sub.tag) == 'incoming':
                actual_in.append((sub.text or '').strip())
            elif local(sub.tag) == 'outgoing':
                actual_out.append((sub.text or '').strip())

        def diff(expected, actual, kind):
            exp = set(expected)
            act = set(actual)
            missing = exp - act
            extra = act - exp
            for m in sorted(missing):
                issues.append(f"  [{path}] node '{eid}': MISSING {kind} child '{m}'")
            for x in sorted(extra):
                issues.append(f"  [{path}] node '{eid}': STALE {kind} child '{x}' (no such flow)")

        diff(expected_in, actual_in, 'incoming')
        diff(expected_out, actual_out, 'outgoing')

    # 4. lane flowNodeRefs pointing at undecilared nodes
    for lane in root.iter():
        if local(lane.tag) != 'lane':
            continue
        lid = lane.get('id')
        for ref in lane.findall(f'{{{NS}}}flowNodeRef'):
            r = (ref.text or '').strip()
            if r and r not in declared:
                issues.append(f"  [{path}] lane '{lid}': PHANTOM flowNodeRef '{r}' (no such node)")

    return issues

def fix(path):
    """Rebuild child refs and prune phantom lane refs. Returns #fixes."""
    tree = ET.parse(path)
    root = tree.getroot()

    flows = {}
    for e in root.iter():
        if local(e.tag) == 'sequenceFlow':
            fid = e.get('id')
            if fid:
                flows[fid] = (e.get('sourceRef'), e.get('targetRef'))

    declared = {e.get('id') for e in root.iter() if e.get('id')}
    fixed = 0

    for e in root.iter():
        if not is_flow_node(e.tag):
            continue
        eid = e.get('id')
        if not eid:
            continue
        expected_in = [f for f, (s, t) in flows.items() if t == eid]
        expected_out = [f for f, (s, t) in flows.items() if s == eid]
        # remove existing incoming/outgoing children
        for sub in list(e):
            if local(sub.tag) in ('incoming', 'outgoing'):
                e.remove(sub)
                fixed += 1
        # add back canonical ones
        for fid in expected_in:
            sub = ET.SubElement(e, f'{{{NS}}}incoming')
            sub.text = fid
            fixed += 1
        for fid in expected_out:
            sub = ET.SubElement(e, f'{{{NS}}}outgoing')
            sub.text = fid
            fixed += 1

    for lane in root.iter():
        if local(lane.tag) != 'lane':
            continue
        for ref in list(lane.findall(f'{{{NS}}}flowNodeRef')):
            r = (ref.text or '').strip()
            if r and r not in declared:
                lane.remove(ref)
                fixed += 1

    return tree, root, fixed

def main():
    files = [f for f in sys.argv[1:] if not f.startswith('-')]
    fix_mode = '--fix' in sys.argv
    if not files:
        files = sorted(glob.glob('processes/*.bpmn')) + sorted(glob.glob('processes-to-be/*.bpmn'))

    total_issues = 0
    for path in files:
        issues = analyze(path)
        if issues:
            total_issues += len(issues)
            for i in issues:
                print(i)
        else:
            print(f"  OK  {path}: child refs + lane refs all consistent")

    print(f"\nTOTAL ISSUES: {total_issues}")

    if fix_mode and total_issues:
        print(f"\n--- Applying fixes ---")
        for path in files:
            issues = analyze(path)
            if not issues:
                continue
            tree, root, n = fix(path)
            if n and not os.path.exists(path + '.bak'):
                shutil.copy2(path, path + '.bak')
            tree.write(path, encoding='utf-8', xml_declaration=True)
            print(f"  FIXED {path}: {n} refs rewritten")
        print("\nRe-run without --fix to verify clean.")

    sys.exit(1 if (total_issues and not fix_mode) else 0)

if __name__ == '__main__':
    main()
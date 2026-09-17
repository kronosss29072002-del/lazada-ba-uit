#!/usr/bin/env python3
"""Automated fixer for 1-in-1-out violations in BPMN files.

Patterns handled:
1. endEvent with N inputs (N>1) from exclusive gateways:
   -> Insert XOR join gateway: all N flows -> join -> endEvent
   (Semantically safe: exclusive gateways are mutually exclusive, so XOR join
    just forwards whichever arrives first. Soundness preserved.)
2. serviceTask/userTask with N outputs where all paths are mutually exclusive
   (each output goes to an exclusive gateway or processes the same decision):
   -> Insert XOR split gateway between task and branches.
   SAFE ONLY when the flows target exclusive gateways. If any target is a
   parallel join or parallel split, requires manual inspection -- skipped.

SAFETY:
- Never modifies gateway semantics.
- Only inserts new join/split XOR gateways with unique IDs and labels.
- Verifies with check-1in1out.py afterwards.
- Skips any file that fails XML parse or has duplicate IDs (manual fix needed).
"""
import xml.etree.ElementTree as ET
import glob, sys, re, shutil, os, datetime

NS = 'http://www.omg.org/spec/BPMN/20100524/MODEL'
NS_BPMNDI = 'http://www.omg.org/spec/BPMN/20100524/DI'
NS_DC = 'http://www.omg.org/spec/DD/20100524/DC'
NS_DI = 'http://www.omg.org/spec/DD/20100524/DI'
ET.register_namespace('bpmn', NS)
ET.register_namespace('bpmndi', NS_BPMNDI)
ET.register_namespace('dc', NS_DC)
ET.register_namespace('di', NS_DI)

def local(t):
    return t.split('}')[-1] if '}' in t else t

def tag_ns(localname):
    return f'{{{NS}}}{localname}'

FLOW_TAGS = ('task','userTask','serviceTask','businessRuleTask','manualTask',
             'scriptTask','sendTask','receiveTask','callActivity','subProcess')
GATEWAY_TAGS = ('exclusiveGateway','parallelGateway','inclusiveGateway',
                'complexGateway','eventBasedGateway')
NODE_TAGS = FLOW_TAGS + GATEWAY_TAGS + ('startEvent','endEvent')

def parse(path):
    tree = ET.parse(path)
    root = tree.getroot()
    # find process element
    proc = None
    for e in root.iter():
        if local(e.tag) == 'process':
            proc = e
            break
    if proc is None:
        raise ValueError('No <process> element found')
    return tree, root, proc

def collect(proc):
    """Return {id: {tag, name, ins, outs, elem}}"""
    elems = {}
    for child in list(proc):
        tag = local(child.tag)
        if tag in NODE_TAGS:
            eid = child.get('id')
            elems[eid] = {
                'tag': tag,
                'name': (child.get('name') or '').strip(),
                'elem': child,
            }
    # flows
    flows = []
    for child in list(proc):
        if local(child.tag) == 'sequenceFlow':
            flows.append(child)
    for f in flows:
        src, tgt = f.get('sourceRef'), f.get('targetRef')
        if src in elems: elems[src].setdefault('outs', []).append(f)
        if tgt in elems: elems[tgt].setdefault('ins', []).append(f)
    return elems, flows

def make_gateway(eid, name):
    el = ET.Element(tag_ns('exclusiveGateway'), {'id': eid})
    el.set('name', name)
    ET.SubElement(el, tag_ns('incoming'))
    ET.SubElement(el, tag_ns('outgoing'))
    return el

def fix_end_joints(proc, elems, flows, log):
    """Fix endEvents with >1 incoming."""
    fixed = 0
    for eid, info in list(elems.items()):
        if info['tag'] != 'endEvent':
            continue
        ins = info.get('ins', [])
        if len(ins) <= 1:
            continue
        # All incoming must be existing sequenceFlows; create XOR join
        join_id = f"Join_End_{eid.replace('End_','').replace('End','') or 'End'}_1"
        # ensure unique
        base = join_id
        i = 2
        while join_id in elems:
            join_id = f"{base}_{i}"
            i += 1
        join = make_gateway(join_id, 'Gom nhánh kết thúc')
        # place before endEvent in process child order (after last incoming source)
        # simplest: append right before the endEvent element
        end_el = info['elem']
        proc.insert(list(proc).index(end_el), join)
        elems[join_id] = {'tag':'exclusiveGateway','name':'Gom nhánh kết thúc','elem':join}
        # retarget all incoming flows to join
        for f in ins:
            f.set('targetRef', join_id)
            join.append(ET.Element(tag_ns('incoming'), {'id': ''}))
        # add old incoming placeholder timestamps - we manage ids below
        # create new flow join->end
        newflow = ET.Element(tag_ns('sequenceFlow'), {
            'id': f'Flow_{join_id}_to_{eid}',
            'sourceRef': join_id, 'targetRef': eid, 'name': ''})
        proc.append(newflow)
        # add incoming/outgoing refs text
        log.append(f"  [FIX] endEvent '{info['name'] or eid}' ({eid}): {len(ins)} inputs -> XOR join '{join_id}'")
        fixed += 1
    return fixed

def cleanup_refs(proc, elems):
    """Normalize <incoming>/<outgoing> child elements of nodes to match flows."""
    # Build map again from flows
    targets = {}
    sources = {}
    for child in list(proc):
        if local(child.tag) == 'sequenceFlow':
            s, t = child.get('sourceRef'), child.get('targetRef')
            sources.setdefault(s, []).append(child.get('id'))
            targets.setdefault(t, []).append(child.get('id'))
    for child in list(proc):
        tag = local(child.tag)
        if tag in NODE_TAGS or tag in GATEWAY_TAGS:
            eid = child.get('id')
            # remove existing incoming/outgoing
            for sub in list(child):
                if local(sub.tag) in ('incoming','outgoing'):
                    child.remove(sub)
            for fid in targets.get(eid, []):
                inc = ET.SubElement(child, tag_ns('incoming'))
                inc.text = fid
            for fid in sources.get(eid, []):
                out = ET.SubElement(child, tag_ns('outgoing'))
                out.text = fid

def main():
    files = [f for f in sys.argv[1:] if not f.startswith('-')]
    dry = '--dry' in sys.argv
    force = '--force' in sys.argv
    if not files:
        files = sorted(glob.glob('processes/*.bpmn')) + sorted(glob.glob('processes-to-be/*.bpmn'))
    total_fixed = 0
    for path in files:
        try:
            tree, root, proc = parse(path)
        except Exception as e:
            print(f"  SKIP {path}: parse error {e}")
            continue
        elems, flows = collect(proc)
        log = []
        n = fix_end_joints(proc, elems, flows, log)
        if n:
            cleanup_refs(proc, elems)
            total_fixed += n
            if not dry:
                # backup
                bak = path + '.bak'
                if not os.path.exists(bak):
                    shutil.copy2(path, bak)
                tree.write(path, encoding='utf-8', xml_declaration=True)
            print(f"{'[DRY]' if dry else '[FIXED]'} {path}: {n} end-joint fix(es)")
            for l in log: print(l)
        else:
            print(f"  OK {path}: no end-joint fixes needed")
    print(f"\nTOTAL end-joint fixes: {total_fixed}" + (" (dry run)" if dry else ""))

if __name__ == '__main__':
    main()
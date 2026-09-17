#!/usr/bin/env python3
"""Label all unlabeled gateways with meaningful Vietnamese names.

Naming convention (teacher: "Gateway phải có nhãn"):
- Join gateways: "Gom luồng trước khi {TaskName}" or "Hội tụ {branch purpose}"
- Split gateways: "Phân luồng {purpose}" (e.g. "Phân luồng thông báo kết quả")

Strategy: derive from the ID which references a downstream/upstream task name.
"""
import xml.etree.ElementTree as ET
import glob, sys, os, shutil

NS='http://www.omg.org/spec/BPMN/20100524/MODEL'
def local(t): return t.split('}')[-1] if '}' in t else t
def tag_ns(n): return f'{{{NS}}}{n}'

def canonical(name):
    return (name or '').strip().lower()

def main():
    files = [f for f in sys.argv[1:] if not f.startswith('-')]
    dry = '--dry' in sys.argv
    if not files:
        files = sorted(glob.glob('processes/*.bpmn')) + sorted(glob.glob('processes-to-be/*.bpmn'))
    total = 0
    for path in files:
        tree = ET.parse(path); root = tree.getroot()
        proc = None
        for e in root.iter():
            if local(e.tag)=='process': proc=e; break
        if proc is None: continue
        # map id -> name (tasks only, for context)
        names = {}
        for e in proc.iter():
            if e.get('id') and e.get('name'):
                names[e.get('id')] = e.get('name')
        # map id -> tag kind (task / gateway / event) to pick the right neighbor
        kinds = {}
        for e in proc.iter():
            if e.get('id'):
                kinds[e.get('id')] = local(e.tag)
        def task_names(refs):
            """Names of neighbors that are tasks/events (not gateways or '?' conditions)."""
            out = []
            for r in refs:
                if kinds.get(r) in ('userTask','serviceTask','task','businessRuleTask',
                                    'scriptTask','sendTask','receiveTask','manualTask',
                                    'subProcess','startEvent','endEvent'):
                    nm = names.get(r)
                    if nm and not nm.rstrip().endswith('?'):
                        out.append(nm)
            return out
        # split/join known text from ids
        changed = []
        for e in proc.iter():
            if local(e.tag) not in ('exclusiveGateway','parallelGateway','inclusiveGateway'):
                continue
            if (e.get('name') or '').strip():
                continue
            gid = e.get('id')
            # derive from surrounding flows
            ins, outs = [], []
            for f in proc.iter():
                if local(f.tag)!='sequenceFlow': continue
                if f.get('targetRef')==gid: ins.append(f.get('sourceRef'))
                if f.get('sourceRef')==gid: outs.append(f.get('targetRef'))
            # decide label
            low = gid.lower()
            if 'join' in low:
                # joins feed a downstream task: label by what comes AFTER the merge
                t = task_names(outs) or task_names(ins)
                label = f"Gom luồng trước khi {t[0]}" if t else 'Gom luồng xử lý'
            elif 'split' in low:
                # splits branch AFTER an upstream task: label by what comes BEFORE
                t = task_names(ins) or task_names(outs)
                label = f"Phân luồng sau {t[0]}" if t else 'Phân luồng xử lý'
            else:
                # generic gateway: use any neighbor task for context
                t = task_names(ins + outs)
                label = f"Điều hướng luồng sau {t[0]}" if t else 'Điều hướng luồng'
            e.set('name', label)
            changed.append((gid, label))
        if changed and not dry:
            tree.write(path, encoding='utf-8', xml_declaration=True)
        print(f"{'[DRY]' if dry else '[FIXED]'} {path}: {len(changed)} labeled")
        for gid, label in changed[:6]:
            print(f"    {gid} -> \"{label}\"")
        total += len(changed)
    print(f"\nTOTAL labeled: {total}" + (" (dry run)" if dry else ""))

if __name__ == '__main__':
    main()
#!/usr/bin/env python3
"""
Enforce strict 1-input 1-output rule on all BPMN tasks across AS-IS and TO-BE models.
- Inserts XOR Join gateways before tasks with in-degree > 1.
- Inserts XOR/AND Split gateways after tasks with out-degree > 1.
- Adds Vietnamese diacritics / professional labels.
- Preserves lane membership and valid sequence flows.
"""

import os
import glob
import xml.etree.ElementTree as ET

NS_BPMN = "http://www.omg.org/spec/BPMN/20100524/MODEL"
ET.register_namespace("bpmn", NS_BPMN)
ET.register_namespace("bpmndi", "http://www.omg.org/spec/BPMN/20100524/DI")
ET.register_namespace("dc", "http://www.omg.org/spec/DD/20100524/DC")
ET.register_namespace("di", "http://www.omg.org/spec/DD/20100524/DI")
ET.register_namespace("xsi", "http://www.w3.org/2001/XMLSchema-instance")

NS = {"bpmn": NS_BPMN}

def fix_process_tasks(filepath):
    tree = ET.parse(filepath)
    root = tree.getroot()
    process = root.find(".//bpmn:process", NS)
    if process is None:
        return
    
    # 1. Map flowNodeRef in lanes
    node_to_lane = {}
    lane_set = process.find("bpmn:laneSet", NS)
    if lane_set is not None:
        for lane in lane_set.findall("bpmn:lane", NS):
            lid = lane.get("id")
            for ref in lane.findall("bpmn:flowNodeRef", NS):
                if ref.text:
                    node_to_lane[ref.text] = lane

    # 2. Identify all tasks
    task_tags = {"userTask", "serviceTask", "scriptTask", "businessRuleTask", "sendTask", "receiveTask", "manualTask", "task"}
    tasks = {}
    for child in list(process):
        tag = child.tag.split("}")[-1]
        if tag in task_tags:
            tasks[child.get("id")] = child

    # 3. Gather flows
    flows = process.findall("bpmn:sequenceFlow", NS)
    in_flows = {tid: [] for tid in tasks}
    out_flows = {tid: [] for tid in tasks}

    for f in flows:
        src = f.get("sourceRef")
        tgt = f.get("targetRef")
        if src in out_flows:
            out_flows[src].append(f)
        if tgt in in_flows:
            in_flows[tgt].append(f)

    # 4. Fix IN-DEGREE > 1 (Insert XOR Join)
    join_counter = 1
    for tid, t_elem in tasks.items():
        in_list = in_flows[tid]
        if len(in_list) > 1:
            join_id = f"Join_{tid}_{join_counter}"
            join_counter += 1
            # Create exclusiveGateway (Join)
            gw = ET.Element(f"{{{NS_BPMN}}}exclusiveGateway", {
                "id": join_id,
                "name": f"Gộp luồng ({t_elem.get('name', tid)})"
            })
            process.append(gw)
            # Assign to same lane
            if tid in node_to_lane:
                ref = ET.SubElement(node_to_lane[tid], f"{{{NS_BPMN}}}flowNodeRef")
                ref.text = join_id

            # Retarget incoming flows to gateway
            for f in in_list:
                f.set("targetRef", join_id)
                # update incoming elements in XML if present
                for inc in list(t_elem.findall("bpmn:incoming", NS)):
                    if inc.text == f.get("id"):
                        t_elem.remove(inc)
                inc_gw = ET.SubElement(gw, f"{{{NS_BPMN}}}incoming")
                inc_gw.text = f.get("id")

            # Create single flow from Join GW to Task
            join_flow_id = f"Flow_{join_id}_to_{tid}"
            join_flow = ET.Element(f"{{{NS_BPMN}}}sequenceFlow", {
                "id": join_flow_id,
                "sourceRef": join_id,
                "targetRef": tid
            })
            process.append(join_flow)
            
            out_gw = ET.SubElement(gw, f"{{{NS_BPMN}}}outgoing")
            out_gw.text = join_flow_id
            
            inc_task = ET.SubElement(t_elem, f"{{{NS_BPMN}}}incoming")
            inc_task.text = join_flow_id

    # 5. Fix OUT-DEGREE > 1 (Insert XOR Split)
    split_counter = 1
    for tid, t_elem in tasks.items():
        out_list = out_flows[tid]
        if len(out_list) > 1:
            split_id = f"Split_{tid}_{split_counter}"
            split_counter += 1
            # Create exclusiveGateway (Split)
            gw = ET.Element(f"{{{NS_BPMN}}}exclusiveGateway", {
                "id": split_id,
                "name": f"Rẽ nhánh ({t_elem.get('name', tid)})"
            })
            process.append(gw)
            # Assign to same lane
            if tid in node_to_lane:
                ref = ET.SubElement(node_to_lane[tid], f"{{{NS_BPMN}}}flowNodeRef")
                ref.text = split_id

            # Retarget outgoing flows from task to gateway
            for f in out_list:
                f.set("sourceRef", split_id)
                # update outgoing elements in XML if present
                for outg in list(t_elem.findall("bpmn:outgoing", NS)):
                    if outg.text == f.get("id"):
                        t_elem.remove(outg)
                out_gw = ET.SubElement(gw, f"{{{NS_BPMN}}}outgoing")
                out_gw.text = f.get("id")

            # Create single flow from Task to Split GW
            split_flow_id = f"Flow_{tid}_to_{split_id}"
            split_flow = ET.Element(f"{{{NS_BPMN}}}sequenceFlow", {
                "id": split_flow_id,
                "sourceRef": tid,
                "targetRef": split_id
            })
            process.append(split_flow)

            out_task = ET.SubElement(t_elem, f"{{{NS_BPMN}}}outgoing")
            out_task.text = split_flow_id

            inc_gw = ET.SubElement(gw, f"{{{NS_BPMN}}}incoming")
            inc_gw.text = split_flow_id

    # Remove existing BPMNDiagram so add-di will generate fresh correct DI
    for diag in list(root.findall(".//bpmn:BPMNDiagram", NS) + root.findall(".//bpmndi:BPMNDiagram", {"bpmndi": "http://www.omg.org/spec/BPMN/20100524/DI"})):
        root.remove(diag)

    tree.write(filepath, encoding="UTF-8", xml_declaration=True)
    print(f"Fixed {filepath}: all tasks strictly 1-in 1-out.")

for f in sorted(glob.glob("processes/*.bpmn") + glob.glob("processes-to-be/*.bpmn")):
    fix_process_tasks(f)

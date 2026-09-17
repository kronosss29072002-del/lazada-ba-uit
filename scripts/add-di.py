#!/usr/bin/env python3
"""
Enterprise BPMNDI Layout Generator for BPMN 2.0 XML files.

Standard Enterprise Gateway Routing:
- Downward branch: exits BOTTOM diamond vertex -> drops to target Y -> enters LEFT target
- Upward branch: exits TOP diamond vertex -> rises to target Y -> enters LEFT target
- Forward horizontal: exits RIGHT diamond vertex -> straight to target LEFT
- Backward retry loop: exits TOP node -> routes overhead along lane boundary -> drops to target TOP
- Labels positioned on horizontal segments (above line) or vertical segments (to right of line)
"""

import xml.etree.ElementTree as ET
import sys
from pathlib import Path
from collections import deque

NS_BPMN = "http://www.omg.org/spec/BPMN/20100524/MODEL"
NS_BPMNDI = "http://www.omg.org/spec/BPMN/20100524/DI"
NS_DC = "http://www.omg.org/spec/DD/20100524/DC"
NS_DI = "http://www.omg.org/spec/DD/20100524/DI"

ET.register_namespace("bpmn", NS_BPMN)
ET.register_namespace("bpmndi", NS_BPMNDI)
ET.register_namespace("dc", NS_DC)
ET.register_namespace("di", NS_DI)
ET.register_namespace("xsi", "http://www.w3.org/2001/XMLSchema-instance")

NS = {"bpmn": NS_BPMN, "bpmndi": NS_BPMNDI, "dc": NS_DC, "di": NS_DI}

# Geometry Configuration
X_START = 80
X_STEP = 220
LANE_HEIGHT = 200
MARGIN_LEFT = 50

SIZES = {
    "startEvent": (36, 36),
    "endEvent": (36, 36),
    "intermediateCatchEvent": (36, 36),
    "boundaryEvent": (36, 36),
    "userTask": (110, 70),
    "serviceTask": (110, 70),
    "task": (110, 70),
    "businessRuleTask": (110, 70),
    "scriptTask": (110, 70),
    "sendTask": (110, 70),
    "receiveTask": (110, 70),
    "manualTask": (110, 70),
    "exclusiveGateway": (46, 46),
    "parallelGateway": (46, 46),
    "inclusiveGateway": (46, 46),
    "complexGateway": (46, 46),
    "eventBasedGateway": (46, 46),
}

FLOW_NODE_TAGS = {
    f"{{{NS_BPMN}}}startEvent",
    f"{{{NS_BPMN}}}endEvent",
    f"{{{NS_BPMN}}}intermediateCatchEvent",
    f"{{{NS_BPMN}}}boundaryEvent",
    f"{{{NS_BPMN}}}userTask",
    f"{{{NS_BPMN}}}serviceTask",
    f"{{{NS_BPMN}}}task",
    f"{{{NS_BPMN}}}businessRuleTask",
    f"{{{NS_BPMN}}}scriptTask",
    f"{{{NS_BPMN}}}sendTask",
    f"{{{NS_BPMN}}}receiveTask",
    f"{{{NS_BPMN}}}manualTask",
    f"{{{NS_BPMN}}}exclusiveGateway",
    f"{{{NS_BPMN}}}parallelGateway",
    f"{{{NS_BPMN}}}inclusiveGateway",
    f"{{{NS_BPMN}}}complexGateway",
    f"{{{NS_BPMN}}}eventBasedGateway",
}


def local_tag(tag):
    return tag.split("}", 1)[1] if "}" in tag else tag


def get_size(element):
    return SIZES.get(local_tag(element.tag), (110, 70))


def is_flow_node(element):
    return element.tag in FLOW_NODE_TAGS


def build_graph(process):
    nodes = {}
    flows = []
    adj = {}
    radj = {}
    flow_elems = {}

    for child in process:
        if is_flow_node(child):
            nid = child.get("id")
            if nid:
                nodes[nid] = child
                adj.setdefault(nid, [])
                radj.setdefault(nid, [])
        elif child.tag == f"{{{NS_BPMN}}}sequenceFlow":
            fid = child.get("id")
            src = child.get("sourceRef")
            tgt = child.get("targetRef")
            if fid and src and tgt:
                flows.append((fid, src, tgt))
                adj.setdefault(src, []).append(tgt)
                radj.setdefault(tgt, []).append(src)
                flow_elems[fid] = child

    return nodes, adj, radj, flows, flow_elems


def assign_lanes(process, nodes):
    node_to_lane = {}
    lanes = []

    lane_set = process.find(f"{{{NS_BPMN}}}laneSet")
    if lane_set is not None:
        for lane in lane_set.findall(f"{{{NS_BPMN}}}lane"):
            lid = lane.get("id")
            if lid:
                lanes.append(lane)
                for ref in lane.findall(f"{{{NS_BPMN}}}flowNodeRef"):
                    if ref.text and ref.text in nodes:
                        node_to_lane[ref.text] = lid

    return lanes, node_to_lane


def infer_unassigned_lanes(nodes, adj, radj, node_to_lane, lanes):
    if not lanes:
        return
    default_lane = lanes[0].get("id")
    queue = deque([nid for nid in node_to_lane])
    visited = set(node_to_lane.keys())

    while queue:
        nid = queue.popleft()
        lane_id = node_to_lane[nid]
        for tgt in adj.get(nid, []):
            if tgt not in visited and tgt in nodes:
                node_to_lane[tgt] = lane_id
                visited.add(tgt)
                queue.append(tgt)

    for nid in nodes:
        if nid not in node_to_lane:
            node_to_lane[nid] = default_lane


def compute_dag_levels(nodes, adj, radj):
    STATE_UNVISITED, STATE_VISITING, STATE_VISITED = 0, 1, 2
    state = {nid: STATE_UNVISITED for nid in nodes}
    back_edges = set()

    starts = [nid for nid, elem in nodes.items() if local_tag(elem.tag) == "startEvent"]
    if not starts:
        starts = [nid for nid in nodes if not radj.get(nid)]
    if not starts:
        starts = list(nodes.keys())[:1]

    def dfs(u):
        state[u] = STATE_VISITING
        for v in adj.get(u, []):
            if v not in nodes:
                continue
            if state[v] == STATE_VISITING:
                back_edges.add((u, v))
            elif state[v] == STATE_UNVISITED:
                dfs(v)
        state[u] = STATE_VISITED

    for s in starts:
        if state[s] == STATE_UNVISITED:
            dfs(s)
    for n in nodes:
        if state[n] == STATE_UNVISITED:
            dfs(n)

    dag_adj = {nid: [] for nid in nodes}
    dag_radj = {nid: [] for nid in nodes}
    for u, targets in adj.items():
        if u not in nodes:
            continue
        for v in targets:
            if v in nodes and (u, v) not in back_edges:
                dag_adj[u].append(v)
                dag_radj[v].append(u)

    in_degree = {nid: len(dag_radj[nid]) for nid in nodes}
    queue = deque([nid for nid in nodes if in_degree[nid] == 0])
    topo_order = []

    while queue:
        u = queue.popleft()
        topo_order.append(u)
        for v in dag_adj[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    for nid in nodes:
        if nid not in topo_order:
            topo_order.append(nid)

    levels = {nid: 0 for nid in nodes}
    for u in topo_order:
        for v in dag_adj[u]:
            levels[v] = max(levels[v], levels[u] + 1)

    return levels, back_edges


def compute_positions(nodes, levels, node_to_lane, lanes):
    lane_index = {lane.get("id"): i for i, lane in enumerate(lanes)}

    slot_nodes = {}
    for nid, elem in nodes.items():
        level = levels.get(nid, 0)
        lid = node_to_lane.get(nid)
        slot_nodes.setdefault((level, lid), []).append(nid)

    positions = {}
    for (level, lid), nids in slot_nodes.items():
        li = lane_index.get(lid, 0)
        lane_y = li * LANE_HEIGHT
        x = X_START + level * X_STEP
        k = len(nids)

        if k == 1:
            nid = nids[0]
            w, h = get_size(nodes[nid])
            y = lane_y + (LANE_HEIGHT - h) // 2
            positions[nid] = (x, y, w, h)
        else:
            for idx, nid in enumerate(nids):
                w, h = get_size(nodes[nid])
                avail_space = LANE_HEIGHT - 30
                step_y = avail_space / k
                y = int(lane_y + 15 + idx * step_y + (step_y - h) / 2)
                positions[nid] = (x, y, w, h)

    return positions


def compute_edge_waypoints(flows, positions, nodes, back_edges, flow_elems, node_to_lane, lanes):
    lane_index = {lane.get("id"): i for i, lane in enumerate(lanes)}
    edges = []

    for fid, src, tgt in flows:
        if src not in positions or tgt not in positions:
            continue
        sx, sy, sw, sh = positions[src]
        tx, ty, tw, th = positions[tgt]

        src_elem = nodes.get(src)
        src_tag = local_tag(src_elem.tag) if src_elem is not None else ""
        is_src_gw = "Gateway" in src_tag

        s_lid = node_to_lane.get(src)
        t_lid = node_to_lane.get(tgt)
        s_lane_idx = lane_index.get(s_lid, 0)
        t_lane_idx = lane_index.get(t_lid, 0)

        is_back = (src, tgt) in back_edges or tx <= (sx + sw - 10)

        label_box = None
        flow_elem = flow_elems.get(fid)
        flow_name = flow_elem.get("name") if flow_elem is not None else None

        if is_back:
            # Overhead loop routing
            x1 = sx + sw // 2
            y1 = sy
            x2 = tx + tw // 2
            y2 = ty

            lane_top_y = min(s_lane_idx, t_lane_idx) * LANE_HEIGHT + 14
            waypoints = [
                (x1, y1),
                (x1, lane_top_y),
                (x2, lane_top_y),
                (x2, y2)
            ]
            if flow_name:
                mid_x = (x1 + x2) // 2
                label_box = (mid_x - 30, lane_top_y - 14, 70, 14)
        else:
            if s_lane_idx == t_lane_idx and abs(sy - ty) < 12:
                # Direct straight horizontal flow
                x1 = sx + sw
                y1 = sy + sh // 2
                x2 = tx
                y2 = ty + th // 2
                waypoints = [(x1, y1), (x2, y2)]
                if flow_name:
                    mid_x = (x1 + x2) // 2
                    label_box = (mid_x - 35, y1 - 16, 75, 14)
            elif is_src_gw and (s_lane_idx != t_lane_idx or abs(sy - ty) >= 12):
                # Standard Gateway branching
                if ty > sy + 20:
                    # Branch DOWN: exit bottom vertex of gateway diamond
                    x1 = sx + sw // 2
                    y1 = sy + sh
                    x2 = tx
                    y2 = ty + th // 2
                    waypoints = [
                        (x1, y1),
                        (x1, y2),
                        (x2, y2)
                    ]
                    if flow_name:
                        label_box = (x1 + 6, (y1 + y2) // 2 - 7, 75, 14)
                elif ty < sy - 20:
                    # Branch UP: exit top vertex of gateway diamond
                    x1 = sx + sw // 2
                    y1 = sy
                    x2 = tx
                    y2 = ty + th // 2
                    waypoints = [
                        (x1, y1),
                        (x1, y2),
                        (x2, y2)
                    ]
                    if flow_name:
                        label_box = (x1 + 6, (y1 + y2) // 2 - 7, 75, 14)
                else:
                    x1 = sx + sw
                    y1 = sy + sh // 2
                    x2 = tx
                    y2 = ty + th // 2
                    turn_x = (x1 + x2) // 2
                    waypoints = [(x1, y1), (turn_x, y1), (turn_x, y2), (x2, y2)]
                    if flow_name:
                        label_box = (x1 + 8, y1 - 16, 75, 14)
            else:
                # Normal task-to-node orthogonal step
                x1 = sx + sw
                y1 = sy + sh // 2
                x2 = tx
                y2 = ty + th // 2

                turn_x = sx + sw + 35
                if turn_x >= x2 - 15:
                    turn_x = (x1 + x2) // 2

                waypoints = [
                    (x1, y1),
                    (turn_x, y1),
                    (turn_x, y2),
                    (x2, y2)
                ]
                if flow_name:
                    label_box = (x1 + 8, y1 - 16, 75, 14)

        edges.append((fid, src, tgt, waypoints, label_box))

    return edges


def generate_di(process, root):
    nodes, adj, radj, flows, flow_elems = build_graph(process)
    lanes, node_to_lane = assign_lanes(process, nodes)
    infer_unassigned_lanes(nodes, adj, radj, node_to_lane, lanes)
    levels, back_edges = compute_dag_levels(nodes, adj, radj)
    positions = compute_positions(nodes, levels, node_to_lane, lanes)
    edges = compute_edge_waypoints(flows, positions, nodes, back_edges, flow_elems, node_to_lane, lanes)

    process_id = process.get("id", "Process_1")

    max_x = max((x + w for x, y, w, h in positions.values()), default=1000)
    lane_start_x = MARGIN_LEFT - 20
    lane_width = max_x - lane_start_x + 60

    diagram = ET.SubElement(root, f"{{{NS_BPMNDI}}}BPMNDiagram")
    diagram.set("id", "BPMNDiagram_1")

    plane = ET.SubElement(diagram, f"{{{NS_BPMNDI}}}BPMNPlane")
    plane.set("id", "BPMNPlane_1")
    plane.set("bpmnElement", process_id)

    # Lane shapes
    for i, lane in enumerate(lanes):
        lid = lane.get("id")
        lane_y = i * LANE_HEIGHT

        shape = ET.SubElement(plane, f"{{{NS_BPMNDI}}}BPMNShape")
        shape.set("id", f"{lid}_di")
        shape.set("bpmnElement", lid)

        bounds = ET.SubElement(shape, f"{{{NS_DC}}}Bounds")
        bounds.set("x", str(lane_start_x))
        bounds.set("y", str(lane_y))
        bounds.set("width", str(lane_width))
        bounds.set("height", str(LANE_HEIGHT))

    # Node shapes
    for nid, (x, y, w, h) in positions.items():
        shape = ET.SubElement(plane, f"{{{NS_BPMNDI}}}BPMNShape")
        shape.set("id", f"{nid}_di")
        shape.set("bpmnElement", nid)

        bounds = ET.SubElement(shape, f"{{{NS_DC}}}Bounds")
        bounds.set("x", str(x))
        bounds.set("y", str(y))
        bounds.set("width", str(w))
        bounds.set("height", str(h))

    # Edge shapes
    for fid, src, tgt, waypoints, label_box in edges:
        edge = ET.SubElement(plane, f"{{{NS_BPMNDI}}}BPMNEdge")
        edge.set("id", f"{fid}_di")
        edge.set("bpmnElement", fid)

        for wx, wy in waypoints:
            wp = ET.SubElement(edge, f"{{{NS_DI}}}waypoint")
            wp.set("x", str(wx))
            wp.set("y", str(wy))

        if label_box:
            lx, ly, lw, lh = label_box
            lbl = ET.SubElement(edge, f"{{{NS_BPMNDI}}}BPMNLabel")
            lbounds = ET.SubElement(lbl, f"{{{NS_DC}}}Bounds")
            lbounds.set("x", str(lx))
            lbounds.set("y", str(ly))
            lbounds.set("width", str(lw))
            lbounds.set("height", str(lh))

    return diagram


def add_diagram(file_path):
    print(f"\n{'='*60}")
    print(f"Processing: {file_path}")
    print(f"{'='*60}")

    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
    except ET.ParseError as e:
        print(f"  ERROR: XML PARSE ERROR: {e}")
        return False

    force = "--force" in sys.argv or "-f" in sys.argv

    existing = root.find(f".//{{{NS_BPMNDI}}}BPMNDiagram")
    if existing is not None:
        if force:
            root.remove(existing)
            print("  REPLACE: Re-generating BPMNDiagram (--force)")
        else:
            print("  SKIP: BPMNDiagram already present (use --force to overwrite)")
            return True

    process = root.find(f".//{{{NS_BPMN}}}process")
    if process is None:
        print("  ERROR: NO PROCESS FOUND")
        return False

    print(f"  Process: {process.get('name', process.get('id'))}")

    nodes, adj, radj, flows, _ = build_graph(process)
    lanes, _ = assign_lanes(process, nodes)
    print(f"  Flow nodes: {len(nodes)}")
    print(f"  Lanes: {len(lanes)}")
    print(f"  Sequence flows: {len(flows)}")

    diagram = generate_di(process, root)

    plane = diagram.find(f"{{{NS_BPMNDI}}}BPMNPlane")
    n_shapes = len(plane.findall(f"{{{NS_BPMNDI}}}BPMNShape"))
    n_edges = len(plane.findall(f"{{{NS_BPMNDI}}}BPMNEdge"))
    print(f"  Generated: {n_shapes} shapes, {n_edges} edges")

    ET.indent(tree, space="  ")
    tree.write(file_path, encoding="UTF-8", xml_declaration=True)

    print(f"  OK: DI written to {file_path}")
    return True


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 add-di.py <file.bpmn> [file2.bpmn ...]")
        print("  python3 add-di.py processes/*.bpmn")
        sys.exit(1)

    files = [f for f in sys.argv[1:] if not f.startswith("-")]
    results = []

    for file_path in files:
        if not Path(file_path).exists():
            print(f"  ERROR: File not found: {file_path}")
            results.append(False)
            continue
        results.append(add_diagram(file_path))

    print(f"\n{'='*60}")
    print("SUMMARY")
    print(f"{'='*60}")
    print(f"  Total files: {len(results)}")
    print(f"  Processed: {sum(results)}")
    print(f"  Failed: {len(results) - sum(results)}")

    if all(results):
        print("\n  All BPMN files processed. OK!")
        return 0
    else:
        print("\n  Some files failed. Check errors above.")
        return 1


if __name__ == "__main__":
    sys.exit(main())

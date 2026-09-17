#!/usr/bin/env python3
"""
Validate BPMN 2.0 XML files.

Usage:
    python3 validate-bpmn.py [file.bpmn]
    python3 validate-bpmn.py processes/*.bpmn

Checks:
    - XML well-formed
    - No orphan nodes (all nodes have incoming/outgoing flows)
    - No duplicate flow IDs
    - All references valid (sourceRef/targetRef exist)
"""

import xml.etree.ElementTree as ET
import sys
from pathlib import Path

NS = {"bpmn": "http://www.omg.org/spec/BPMN/20100524/MODEL"}


def validate_bpmn(file_path):
    """Validate a single BPMN file."""
    print(f"\n{'='*60}")
    print(f"Validating: {file_path}")
    print(f"{'='*60}")

    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
    except ET.ParseError as e:
        print(f"  ERROR: XML PARSE ERROR: {e}")
        return False

    process = root.find(".//bpmn:process", NS)
    if process is None:
        print("  ERROR: NO PROCESS FOUND")
        return False

    print(f"  Process: {process.get('name')}")

    # Count elements (filter out non-flow elements like laneSet/lane)
    flow_elements = [
        e
        for e in process
        if not (
            e.tag.endswith("}laneSet")
            or e.tag.endswith("}lane")
            or e.tag.endswith("}extensionElements")
        )
    ]
    tasks = [e for e in flow_elements if "Task" in e.tag]
    gateways = [e for e in flow_elements if "Gateway" in e.tag]
    events = [e for e in flow_elements if "Event" in e.tag]
    flows = [e for e in flow_elements if "sequenceFlow" in e.tag]

    print(f"  Tasks: {len(tasks)}")
    print(f"  Gateways: {len(gateways)}")
    print(f"  Events: {len(events)}")
    print(f"  Sequence flows: {len(flows)}")

    # Build node connectivity map (exclude data objects, annotations, groups)
    non_flow_artifacts = (
        "dataObject", "dataObjectReference", "dataStore",
        "textAnnotation", "association", "group"
    )
    node_ids = {
        e.get("id")
        for e in flow_elements
        if e.get("id")
        and "sequenceFlow" not in e.tag
        and not any(e.tag.endswith(a) for a in non_flow_artifacts)
    }
    all_sources = {f.get("sourceRef") for f in flows}
    all_targets = {f.get("targetRef") for f in flows}
    start_ids = {e.get("id") for e in flow_elements if "startEvent" in e.tag}
    end_ids = {e.get("id") for e in flow_elements if "endEvent" in e.tag}
    boundary_ids = {e.get("id") for e in flow_elements if "boundaryEvent" in e.tag}

    has_errors = False

    # Find orphans
    orphans_in = node_ids - all_targets - start_ids - boundary_ids
    orphans_out = node_ids - all_sources - end_ids - boundary_ids

    if orphans_in:
        print(f"  WARNING: Nodes with no incoming flow:")
        for oid in sorted(orphans_in):
            print(f"    - {oid}")
        has_errors = True

    if orphans_out:
        print(f"  WARNING: Nodes with no outgoing flow:")
        for oid in sorted(orphans_out):
            print(f"    - {oid}")
        has_errors = True

    if not orphans_in and not orphans_out:
        print("  OK: No orphan nodes")

    # Check for duplicate flow IDs
    flow_ids = [f.get("id") for f in flows]
    dupes = set([x for x in flow_ids if flow_ids.count(x) > 1])
    if dupes:
        print(f"  ERROR: DUPLICATE FLOW IDS: {dupes}")
        has_errors = True
    else:
        print("  OK: No duplicate flows")

    # Reference validation
    defined = node_ids | set(flow_ids)
    missing = (all_sources | all_targets) - defined
    if missing:
        print(f"  ERROR: MISSING REFERENCES: {missing}")
        has_errors = True
    else:
        print("  OK: All references valid")

    # Final result
    print(f"{'='*60}")
    if has_errors:
        print("  RESULT: FAILED")
    else:
        print("  RESULT: PASSED")
    print(f"{'='*60}\n")

    return not has_errors


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 validate-bpmn.py <file.bpmn> [file2.bpmn ...]")
        print("  python3 validate-bpmn.py processes/*.bpmn")
        sys.exit(1)

    files = sys.argv[1:]
    results = []

    for file_path in files:
        if not Path(file_path).exists():
            print(f"  ERROR: File not found: {file_path}")
            results.append(False)
            continue
        results.append(validate_bpmn(file_path))

    # Summary
    print(f"\n{'='*60}")
    print("SUMMARY")
    print(f"{'='*60}")
    print(f"  Total files: {len(results)}")
    print(f"  Passed: {sum(results)}")
    print(f"  Failed: {len(results) - sum(results)}")

    if all(results):
        print("\n  All BPMN files are valid. OK!")
        return 0
    else:
        print("\n  Some BPMN files have errors. Please fix them.")
        return 1


if __name__ == "__main__":
    sys.exit(main())

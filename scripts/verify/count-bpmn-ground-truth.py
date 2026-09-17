#!/usr/bin/env python3
"""
Ground-truth BPMN counter — LAZADA BA Project (IE203.P11)

Đếm chính xác mọi task type trong file BPMN 2.0 XML theo chuẩn BPMN:
  userTask | serviceTask | task (generic) | scriptTask | manualTask |
  receiveTask | sendTask | businessRuleTask | callActivity

Và gateways:
  exclusiveGateway | parallelGateway | inclusiveGateway | eventBasedGateway | complexGateway

LỊCH SỬ BUG (quan trọng): biểu thức `<...Task\b` KHÔNG khớp tag generic `<bpmn:task>`.
Luôn dùng regex đầy đủ dưới đây — không rút gọn.

Cách dùng:
  python3 scripts/verify/count-bpmn-ground-truth.py             # toàn bộ processes/ + processes-to-be/
  python3 scripts/verify/count-bpmn-ground-truth.py processes/03-order-flow.bpmn
"""
import re
import sys
from pathlib import Path

PROJ = Path(__file__).resolve().parents[2]

TASK_PATTERN = re.compile(
    r"<(?:bpmn:)?(?:user|service|script|manual|receive|send|businessRule)?"
    r"(?:task|Task|callActivity)\b"
)
GATEWAY_PATTERN = re.compile(
    r"<(?:bpmn:)?(?:exclusive|parallel|inclusive|eventBased|complex)?"
    r"(?:gateway|Gateway)\b"
)

# Chỉ đếm định nghĩa dạng self-closing hoặc mở — không đếm tag đóng
TASK_TAGS = ("<bpmn:task", "<task", "<bpmn:userTask", "<userTask", "<bpmn:serviceTask",
             "<serviceTask", "<bpmn:scriptTask", "<scriptTask", "<bpmn:manualTask",
             "<manualTask", "<bpmn:receiveTask", "<receiveTask", "<bpmn:sendTask",
             "<sendTask", "<bpmn:businessRuleTask", "<businessRuleTask",
             "<bpmn:callActivity", "<callActivity")
GATEWAY_TAGS = ("<bpmn:exclusiveGateway", "<exclusiveGateway", "<bpmn:parallelGateway",
                "<parallelGateway", "<bpmn:inclusiveGateway", "<inclusiveGateway",
                "<bpmn:eventBasedGateway", "<eventBasedGateway", "<bpmn:complexGateway",
                "<complexGateway")


def count_file(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    tasks = [t for t in TASK_PATTERN.findall(text) if str(t).startswith(TASK_TAGS)]
    gateways = [g for g in GATEWAY_PATTERN.findall(text) if str(g).startswith(GATEWAY_TAGS)]
    return {"file": path.name, "tasks": len(tasks), "gateways": len(gateways)}


def main() -> int:
    if len(sys.argv) > 1:
        paths = [Path(a) for a in sys.argv[1:]]
        paths = [p if p.is_absolute() else PROJ / p for p in paths]
    else:
        paths = sorted((PROJ / "processes").glob("*.bpmn")) + sorted(
            (PROJ / "processes-to-be").glob("*.bpmn"))

    rows, at, tt, ag, tg = [], 0, 0, 0, 0
    for p in paths:
        r = count_file(p)
        rows.append(r)
        at += r["tasks"]
        tt += r["gateways"]
        if "as-is" in p.name.lower() or "asis" in p.name.lower():
            ag += r["tasks"]
            tg += r["gateways"]

    print(f"{'File':<42}{'Tasks':>6}{'Gateways':>10}")
    print("-" * 62)
    for r in rows:
        print(f"{r['file']:<42}{r['tasks']:>6}{r['gateways']:>10}")

    print("-" * 62)
    print(f"{'TOTAL':<42}{at:>6}{tt:>10}")

    expected = {"tasks": 348, "gateways": 267}  # AS-IS 181/152 + TO-BE 167/115
    ok = at == expected["tasks"] and tt == expected["gateways"]
    print(f"\nGRAND TOTAL expected {expected['tasks']}/{expected['gateways']} -> {'PASS' if ok else 'FAIL (ground truth mismatch)'}")
    if not ok:
        print(f"  AS-IS  : {ag} tasks / {tg} gateways (expect 181 / 152)")
        print(f"  TO-BE  : {at - ag} tasks / {tt - tg} gateways (expect 167 / 115)")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
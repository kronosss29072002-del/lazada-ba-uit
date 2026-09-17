# Development Guide

Hướng dẫn development cho đồ án BA-BPMS Lazada Việt Nam.

---

## Quick Start

### 1. Clone repository
```bash
git clone <repo-url>
cd lazada-ba-project
```

### 2. Install tools

**Required:**
- [Camunda Modeler](https://camunda.com/download/modeler/) — vẽ BPMN 2.0
- Python 3.8+ — validation scripts

**Optional:**
- Node.js 18+ — bpmn-js viewer
- VS Code + BPMN extension — edit BPMN XML trực tiếp

### 3. Validate BPMN files
```bash
python3 scripts/validate-bpmn.py processes/*.bpmn
```

### 4. Xem BPMN diagrams
```bash
camunda-modeler processes/04-order-processing.bpmn
# Hoặc upload lên https://demo.bpmn.io/
```

---

## Project Structure

```
lazada-ba-project/
├── README.md                    # Giới thiệu dự án
├── DEVELOPMENT.md               # Hướng dẫn development (file này)
├── PROCESSES.md                 # Tổng quan 10 BPMN processes (3 lớp)
├── docs/
│   ├── bpmn/                    # BPMN modeling guide
│   ├── analysis/                # Chi tiết từng quy trình + Fishbone + 5-Why
│   ├── petri-net/               # Soundness verification evidence
│   └── screenshots/             # Screenshots cho report
├── processes/                   # BPMN 2.0 XML AS-IS (validated)
│   └── 01..10.bpmn
├── processes-to-be/             # BPMN 2.0 XML TO-BE (validated)
│   └── 01..10-tobe.bpmn
├── report/                      # Report chapters
├── metrics/                     # Dashboard + data.json
├── stakeholder/                 # RACI + Stakeholder matrix
├── presentation/                # Slides (Marp/reveal.js)
├── viewer/                      # BPMN viewer (bpmn-js)
└── scripts/                     # Validation & utility scripts
```

---

## BPMN Modeling Guide

### Quy ước đặt tên

**File:** `{STT}-{process-name}.bpmn`

**Elements:**
```
StartEvent: StartEvent_{Description}
Task:       Task_{Verb}{Noun}
Gateway:    Gate_{Question}
EndEvent:   End_{Outcome}
Flow:       Flow_{Source}_{Target}
```

### BPMN Checklist

**Structure:**
- [ ] Pool chính với lanes cho mỗi actor
- [ ] Start event (duy nhất)
- [ ] End events (có thể nhiều)
- [ ] Sequence flows nối tất cả activities
- [ ] Không dead ends, không infinite loops

**Elements:**
- [ ] >= 7 gateways (đạt 1 điểm rubric)
- [ ] User tasks cho human steps
- [ ] Service tasks cho automated steps
- [ ] Condition expressions trên gateway outputs
- [ ] Exception handling

**Validation:**
```bash
python3 scripts/validate-bpmn.py processes/XX-name.bpmn
```

---

## Analysis Framework

### Template phân tích

Copy từ `docs/analysis/analysis-template.md` cho mỗi quy trình mới.

**Cấu trúc:**
1. Mô tả quy trình — Phạm vi, actors, outcomes
2. Mô hình BPMN — Diagram + thống kê
3. Phân tích định tính — VA/BVA/NVA, Waste, Root cause (5 Why)
4. Phân tích định lượng — Time, Cost, Quality
5. Đề xuất cải tiến (TO-BE) — So sánh AS-IS vs TO-BE

### Metrics cần có

**Time:** Cycle time, task time, wait time, best/worst case
**Cost:** Cost per unit, infrastructure, labor, net margin
**Quality:** Success rate, error rate, CSAT, benchmarks

---

## Writing Report

### Chapter structure

**Chapter 1: Introduction** — Lazada overview, org structure, scope
**Chapter 2: Architecture** — 3-layer process architecture, system design
**Chapter 3: Analysis** (CORE) — 10 processes with full analysis
**Chapter 4: Conclusion** — Findings, recommendations, limitations

### Tips

1. Bắt đầu với Chapter 3 — core content
2. Dùng analysis docs — copy từ `docs/analysis/` vào report
3. Chèn BPMN diagrams — export PNG từ Camunda Modeler
4. So sánh AS-IS vs TO-BE — tables với metrics

---

## Decision Gates

| Gate | Thời điểm | Criteria |
|------|-----------|----------|
| 1 | End Week 2 | 10 BPMN AS-IS validated, pain points documented |
| 2 | End Week 4 | 10 BPMN TO-BE validated, improvements quantified |
| 3 | End Week 6 | All chapters written, diagrams exported, analysis complete |

---

## Resources

- [BPMN 2.0 Specification](https://www.omg.org/spec/BPMN/2.0/)
- [Camunda BPMN Guide](https://docs.camunda.org/guides/bpmn-guide/)
- [Lazada Seller Center VN](https://sellercenter.lazada.vn)
- [Lazada Help Center VN](https://helpcenter.lazada.vn)
- [bpmn-js GitHub](https://github.com/bpmn-io/bpmn-js)

---

## Petri Net Evidence (Soundness Verification)

Script Python mô hình hóa mỗi BPMN thành WF-net và kiểm tra soundness.

**Cách dùng:**
```bash
# Kiểm tra tất cả processes
python3 scripts/soundness-check.py processes/*.bpmn

# Sinh markdown evidence
python3 scripts/soundness-check.py --out docs/petri-net processes/*.bpmn
```

**Các thuộc tính kiểm tra:**
- **Option to Complete:** mọi marking reachable đều có path tới completion
- **Proper Completion:** mọi terminal marking chỉ chứa token trong final places
- **No Dead Transitions:** mọi transition fireable trong ≥1 marking reachable

---

## BPMN Notation Checklist (Tránh -0.25/lỗi)

Theo rubric: mỗi ký hiệu sai trừ 0.25 điểm.

| # | Quy tắc | Kiểm tra | Lỗi thường gặp |
|---|---------|----------|----------------|
| 1 | Activity = hình chữ nhật **bo tròn 4 góc** | ☐ | Hình chữ nhật vuông góc |
| 2 | Start Event = vòng tròn mỏng, duy nhất per process | ☐ | Nhiều start events |
| 3 | End Event = vòng tròn đậm | ☐ | Dùng vòng tròn mỏng |
| 4 | XOR Gateway = hình thoi + dấu X | ☐ | Thiếu dấu X |
| 5 | AND Gateway = hình thoi + dấu + | ☐ | Nhầm lẫn XOR vs AND |
| 6 | OR Gateway = hình thoi + dấu O | ☐ | Ít dùng, dễ nhầm |
| 7 | Sequence Flow = mũi tên liền nét | ☐ | Dùng nét đứt (Association) |
| 8 | Message Flow = mũi tên nét đứt (giữa pools) | ☐ | Dùng sequence flow giữa pools |
| 9 | Split gateway PHẢI có Join tương ứng | ☐ | Quên join → deadlock |
| 10 | Gateway label trên nhánh outgoing | ☐ | Thiếu label điều kiện |
| 11 | Task naming: **Động từ + Danh từ** | ☐ | "Đơn hàng" thay vì "Xác nhận đơn" |
| 12 | Event naming: **Danh từ + Động từ** | ☐ | "Nhận" thay vì "Đơn được nhận" |
| 13 | Pool/Lane có tên rõ ràng | ☐ | Lane trống tên |
| 14 | Không orphan nodes (validate script) | ☐ | Node không có flow |
| 15 | Data Object dùng đúng ký hiệu | ☐ | Dùng hình chữ nhật thường |

---

## Rubric Checklist — Đồ án IE203

### Mô hình quy trình (30%)

| Tiêu chí | Điểm | Kiểm tra |
|----------|------|----------|
| 10 quy trình được mô tả đầy đủ | /8 | ☐ Mỗi quy trình có: mô tả, actors, customer, outcomes |
| 3 lớp: Management / Core / Support | /3 | ☐ Chia đúng theo mô hìnhrops (Management=3, Core=4, Support=3) |
| BPMN 2.0 notation đúng chuẩn | /4 | ☐ Đúng 15 quy tắc BPMN notation |
| >= 7 gateways per process | /3 | ☐ Verify bằng `validate-bpmn.py` |

### Phân tích định tính (20%)

| Tiêu chí | Điểm | Kiểm tra |
|----------|------|----------|
| VA/BVA/NVA analysis | /4 | ☐ Mỗi quy trình có classification rõ ràng |
| Fishbone diagram | /3 | ☐ Root cause cho top 3 pain points |
| 5-Why analysis | /3 | ☐ Approaches root cause cho ít nhất 3 issues |
| Pareto chart | /3 | ☐ 80/20 cho categories lỗi |

### Phân tích định lượng (20%)

| Tiêu chí | Điểm | Kiểm tra |
|----------|------|----------|
| Time analysis | /4 | ☐ Cycle time, task time, wait time per process |
| Cost analysis | /4 | ☐ Cost per unit, infrastructure cost |
| Quality metrics | /4 | ☐ Success rate, error rate, benchmarks |
| Comparison tables | /3 | ☐ AS-IS vs TO-BE với numerical targets |

### Đề xuất TO-BE (20%)

| Tiêu chí | Điểm | Kiểm tra |
|----------|------|----------|
| TO-BE diagrams | /5 | ☐ 10 BPMN TO-BE files, soundness verified |
| Improvements quantified | /5 | ☐ Mỗi improvement có before/after metrics |
| Root cause → solution mapping | /5 | ☐ Solutions address identified root causes |
| Implementation feasibility | /5 | ☐ Realistic, costed, prioritized |

### Presentation & Report (10%)

| Tiêu chí | Điểm | Kiểm tra |
|----------|------|----------|
| Report structure | /3 | ☐ 4 chapters, properly formatted |
| BPMN diagrams trong report | /2 | ☐ PNG export từ Camunda |
| Slides | /3 | ☐ Max 20 slides, clear narrative |
| Demo | /2 | ☐ Live BPMN viewer hoặc trace |

---

## Troubleshooting

**"No incoming flow" warning:** Check sequence flows — every node (except StartEvent) needs incoming flow

**"Invalid XML" error:** Escape special characters: `&` → `&amp;`, `<` → `&lt;`, `>` → `&gt;`

**Modeler crashes:** Split into sub-processes or simplify diagram

**Soundness verification fails:** Check AND gateways have matching splits/joins

# Kế hoạch Thực hiện Đồ án — Gantt Chart (Lazada Vietnam)

> Rubric yêu cầu: "Kế hoạch làm việc - nếu có" (mục Phương pháp thực hiện).
> Đồ án: Phân tích & Tái thiết kế quy trình nghiệp vụ (BPM) của **Lazada Vietnam** — mô hình hóa 10 quy trình cốt lõi bằng BPMN 2.0, phân tích AS-IS, thiết kế TO-BE.

---

## Timeline Dự án (12 tuần)

```
Tuần:  1    2    3    4    5    6    7    8    9    10   11   12
       ├────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┤

Phase 1: Research & Data Collection
       ████████████
       W1-W2
       ├── Thu thập tài liệu Lazada (báo cáo, news, marketplace)
       ├── Xác định 10 quy trình BPM của sàn TMĐT
       ├── Thiết kế câu hỏi phỏng vấn (20 câu)
       └── Nghiên cứu framework BPMN 2.0 + Camunda Modeler

Phase 2: AS-IS Modeling
            ████████████
            W3-W4
            ├── Vẽ 10 BPMN AS-IS (Camunda Modeler)
            ├── Mô tả actors, flows, gateways
            ├── Validate Petri Net soundness
            └── Review chéo nhóm

Phase 3: Analysis (Qualitative + Quantitative)
                 ████████████
                 W5-W6
                 ├── VA/BVA/NVA analysis (10 quy trình)
                 ├── Waste analysis (Move/Hold/Overdo)
                 ├── Fishbone diagrams (2 vấn đề)
                 ├── Tính toán Cycle Time, Cost, Quality
                 └── Benchmarking vs Lazada/TikTok Shop

Phase 4: TO-BE Design
                      ████████████
                      W7-W8
                      ├── Thiết kế 10 BPMN TO-BE
                      ├── So sánh AS-IS vs TO-BE metrics
                      ├── ROI/Payback calculation
                      ├── Risk assessment
                      └── Implementation roadmap

Phase 5: Report Writing
                           ████████████
                           W9-W10
                           ├── Viết Chapter 1-4
                           ├── Format theo mẫu UIT
                           ├── Tạo mục lục hình/bảng
                           ├── Glossary 30 terms
                           └── Org chart + Gantt chart

Phase 6: Review, Slides & Submission
                                ████████████
                                W11-W12
                                ├── Review chính tả, formatting
                                ├── Sync số liệu cross-files
                                ├── Phỏng vấn bổ sung + workshop với khách mời
                                ├── Prepare slides Marp
                                ├── Rehearse presentation
                                └── Nộp bài: Elearning + Google Drive
```

---

## Bảng Chi tiết Công việc

| Phase | Tuần | Công việc | Output | Người thực hiện | Dependencies |
|-------|------|-----------|--------|-----------------|--------------|
| **1. Research** | W1 | Thu thập tài liệu Lazada | Folder `/research` | Cả nhóm | - |
| | W1 | Xác định 10 quy trình sàn TMĐT | `PROCESSES.md` | Cả nhóm | - |
| | W2 | Thiết kế câu hỏi phỏng vấn (20 câu) | `interview-questions.md` | Member A | Xác định quy trình |
| | W2 | Nghiên cứu BPMN 2.0 + tooling | Notes cá nhân | Cả nhóm | - |
| **2. AS-IS** | W3 | Vẽ BPMN 01-05 (Seller, Dispute, Order, Return, CS) | `.bpmn` files | Member A | Hiểu quy trình |
| | W3 | Vẽ BPMN 06-10 (Marketing, HR, Payment, Logistics, IT) | `.bpmn` files | Member B | Hiểu quy trình |
| | W4 | Mô tả actors, flows | `docs/analysis/*.md` | Cả nhóm | BPMN hoàn thành |
| | W4 | Validate Petri Net soundness | `docs/analysis/petri-net/` | Member A | BPMN hoàn thành |
| **3. Analysis** | W5 | VA/BVA/NVA analysis | Tables trong analysis | Member A | AS-IS docs |
| | W5 | Waste analysis | Tables trong analysis | Member B | AS-IS docs |
| | W6 | Fishbone diagrams (2 vấn đề) | `fishbone-diagrams.md` | Member A | Waste analysis |
| | W6 | Quantitative metrics (Cycle Time/Cost) | `metrics/data.json` | Member B | AS-IS docs |
| | W6 | Benchmarking vs Lazada/TikTok Shop | `benchmarking.md` | Cả nhóm | Metrics hoàn thành |
| **4. TO-BE** | W7 | Thiết kế 10 BPMN TO-BE | `processes-to-be/*.bpmn` | Cả nhóm | Analysis hoàn thành |
| | W7 | So sánh AS-IS vs TO-BE metrics | `docs/analysis/comparison/` | Member A | TO-BE BPMN |
| | W8 | ROI/Payback calculation | Financial analysis | Member B | Metrics + Cost data |
| | W8 | Risk assessment | Risk matrix | Cả nhóm | TO-BE design |
| **5. Report** | W9 | Viết Chapter 1-2 | `report/chapter-1/2.md` | Member A | Tất cả analysis |
| | W9 | Viết Chapter 3-4 | `report/chapter-3/4.md` | Member B | Tất cả analysis |
| | W10 | Format UIT template | `report/report.html` | Member A | Chapters hoàn thành |
| | W10 | Glossary + Org chart + Gantt | `appendix/` | Member B | - |
| **6. Polish & Submit** | W11 | Review chính tả, sync số liệu | Final docs | Cả nhóm | Report draft |
| | W11 | Phỏng vấn bổ sung + workshop | `appendix/interviews/` | Cả nhóm | Analysis hoàn thành |
| | W12 | Prepare slides | `slides.md` | Member A | Report final |
| | W12 | Rehearse presentation | Practice session | Cả nhóm | Slides hoàn thành |
| | W12 | Nộp bài Elearning + Google Drive | Word + Slides + PDF | Cả nhóm | Everything done |

---

## Milestones & Deliverables

| Milestone | Deadline | Deliverable | Status |
|-----------|----------|-------------|--------|
| M1: Research Complete | End W2 | 10 processes identified, interview questions | ✅ Done |
| M2: AS-IS Models | End W4 | 10 BPMN files + petri-net soundness report | ✅ Done |
| M3: Analysis Complete | End W6 | VA/NVA/Waste/Fishbone/Metrics | ✅ Done |
| M4: TO-BE Design | End W8 | 10 TO-BE BPMN + ROI analysis | ✅ Done |
| M5: Report Draft | End W10 | Full report + appendix | 🔄 In Progress |
| M6: Final Submission | End W12 | Elearning + Google Drive (Word + Slides) | ⏳ Pending |

---

## Phân bổ Nguồn lực

| Thành viên | Vai trò chính | Trách nhiệm |
|------------|--------------|-------------|
| Member A | BPMN Modeler + Analyst | Vẽ BPMN, VA/NVA analysis, Fishbone, Petri Net, Chapter 1-2, Slides |
| Member B | Quantitative Analyst + Writer | Metrics, ROI, Waste analysis, Chapter 3-4, Formatting, phỏng vấn/workshop |

---

## Rủi ro & Mitigation

| Rủi ro | Xác suất | Tác động | Mitigation |
|--------|----------|----------|------------|
| Thiếu dữ liệu thực tế của Lazada | Cao | Trung bình | Sử dụng industry benchmarks + ghi rõ giả định |
| BPMN quá phức tạp | Trung bình | Cao | Giới hạn scope, focus 10 core processes |
| Số liệu không consistent | Trung bình | Cao | Single source of truth: `metrics/data.json` |
| Lịch phỏng vấn/workshop bị trễ | Trung bình | Trung bình | Chốt lịch trước 1 tuần, phỏng vấn online fallback |
| Deadline trượt | Thấp | Cao | Weekly check-in, buffer 1 tuần cuối |

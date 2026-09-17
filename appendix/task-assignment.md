# PHỤ LỤC: PHÂN CÔNG CÔNG VIỆC CHI TIẾT THEO TUẦN (12 TUẦN)

> **Đồ án:** Hệ thống Quản trị Quy trình Nghiệp vụ (BPM) Lazada Việt Nam (IE203)
> **Nhóm:** Nhóm Lazada BA (02 thành viên)
> **Ngày lập:** 2026-09-03
> **Ghi chú đồng bộ:** File này mở rộng chi tiết hơn bảng phân công trong báo cáo chính. Khi có thay đổi, cập nhật đồng thời các file liên quan.

---

## 1. Hồ sơ thành viên & Vai trò chính

| Thành viên | Vai trò chính | Trách nhiệm cốt lõi |
|------------|--------------|---------------------|
| **Nguyễn Lưu Nhật Minh** | BPMN Modeler + Analyst | Vẽ/mô hình BPMN AS-IS & TO-BE (Camunda), VA/NVA/Waste/Fishbone analysis, validation Petri Net, Chapter 1-2, slides |
| **Thành viên 2** | Quantitative Analyst + Writer | Metrics (Cycle Time, Cost, ROI), data.json, benchmarking, Chapter 3-4, format báo cáo |

---

## 2. Bảng phân công chi tiết theo tuần

### Phase 1 — Research & Data Collection (Tuần 1-2)

| Tuần | # | Công việc cụ thể | Deliverable | Người phụ trách | Thành viên còn lại hỗ trợ |
|------|---|-----------------|-------------|-----------------|---------------------------|
| W1 | 1.1 | Thu thập tài liệu Lazada (báo cáo năm, tin công nghệ, dữ liệu công khai) | Thư mục `/research` | Cả 2 | — |
| W1 | 1.2 | Xác định 10 quy trình nghiệp vụ chính + phân loại theo mức độ quan trọng | `PROCESSES.md` | Nhật Minh | Thành viên 2 (review phân loại) |
| W1 | 1.3 | Nghiên cứu framework BPMN 2.0 + công cụ Camunda Modeler | Ghi chú cá nhân | Nhật Minh | Thành viên 2 (ghi chú chung) |
| W2 | 1.4 | Thiết kế bộ câu hỏi phỏng vấn chuẩn (20 câu) | `appendix/interview-questions.md` | Nhật Minh | Thành viên 2 (góp ý nội dung) |
| W2 | 1.5 | Soạn bộ câu hỏi phỏng vấn riêng cho 10 quy trình | `appendix/interviews/*.md` | Thành viên 2 | Nhật Minh (chốt câu hỏi) |
| W2 | 1.6 | Xây dựng Issue Register sơ bộ từ tài liệu thu thập | `docs/analysis/issue-register.md` (draft) | Thành viên 2 | Nhật Minh (góp ý) |

### Phase 2 — AS-IS Modeling (Tuần 3-4)

| Tuần | # | Công việc cụ thể | Deliverable | Người phụ trách | Thành viên còn lại hỗ trợ |
|------|---|-----------------|-------------|-----------------|---------------------------|
| W3 | 2.1 | Vẽ BPMN AS-IS quy trình 01 (Seller Management) | `processes/01-seller-management.bpmn` | Nhật Minh | — |
| W3 | 2.2 | Vẽ BPMN AS-IS quy trình 02 (Dispute Resolution) | `processes/02-dispute-resolution.bpmn` | Nhật Minh | — |
| W3 | 2.3 | Vẽ BPMN AS-IS quy trình 03 (Order Processing) | `processes/03-order-processing.bpmn` | Nhật Minh | — |
| W3 | 2.4 | Vẽ BPMN AS-IS quy trình 04 (Return & Refund) | `processes/04-return-refund.bpmn` | Thành viên 2 | Nhật Minh (review soundness) |
| W3 | 2.5 | Vẽ BPMN AS-IS quy trình 05 (Customer Service) | `processes/05-customer-service.bpmn` | Thành viên 2 | Nhật Minh (review soundness) |
| W3 | 2.6 | Vẽ BPMN AS-IS quy trình 06 (Marketing & Promotions) | `processes/06-marketing-promotions.bpmn` | Thành viên 2 | Nhật Minh (review soundness) |
| W4 | 2.7 | Mô tả actors, flows, gateways cho 10 quy trình | `docs/analysis/*.md` (mục mô tả) | Cả 2 (mỗi người 3 quy trình) | Chéo review |
| W4 | 2.8 | Validate Petri Net soundness (10 quy trình) | Script `scripts/soundness-check.py` + report | Nhật Minh | Thành viên 2 (chạy lại) |
| W4 | 2.9 | Review chéo BPMN giữa 2 thành viên | Biên bản review | Cả 2 | — |

### Phase 3 — Analysis Qualitative + Quantitative (Tuần 5-6)

| Tuần | # | Công việc cụ thể | Deliverable | Người phụ trách | Thành viên còn lại hỗ trợ |
|------|---|-----------------|-------------|-----------------|---------------------------|
| W5 | 3.1 | VA/BVA/NVA analysis cho quy trình 01-03 | Bảng trong `docs/analysis/01-03.md` | Nhật Minh | — |
| W5 | 3.2 | VA/BVA/NVA analysis cho quy trình 04-06 | Bảng trong `docs/analysis/04-06.md` | Thành viên 2 | — |
| W5 | 3.3 | Waste analysis (Move/Hold/Overdo) 10 quy trình | Bảng Waste + Pareto | Thành viên 2 | Nhật Minh (góp ý) |
| W6 | 3.4 | Fishbone diagrams (2 vấn đề chính) | `docs/analysis/fishbone-diagrams.md` | Nhật Minh | — |
| W6 | 3.5 | 5-Why supplementary | `docs/analysis/5-why-supplementary.md` | Nhật Minh | — |
| W6 | 3.6 | Tính Cycle Time, Cost, Quality từ mock interview data | `docs/analysis/*.md` (mục định lượng) | Thành viên 2 | — |
| W6 | 3.7 | Tổng hợp metrics vào single source of truth | `metrics/data.json` | Thành viên 2 | Nhật Minh (kiểm tra chéo) |
| W6 | 3.8 | Benchmarking vs Lazada/TikTok Shop | Bảng benchmark trong analysis | Cả 2 | — |

### Phase 4 — TO-BE Design (Tuần 7-8)

| Tuần | # | Công việc cụ thể | Deliverable | Người phụ trách | Thành viên còn lại hỗ trợ |
|------|---|-----------------|-------------|-----------------|---------------------------|
| W7 | 4.1 | Thiết kế BPMN TO-BE quy trình 01-03 | `processes-to-be/01-03-tobe.bpmn` | Nhật Minh | Thành viên 2 (góp ý nghiệp vụ) |
| W7 | 4.2 | Thiết kế BPMN TO-BE quy trình 04-06 | `processes-to-be/04-06-tobe.bpmn` | Thành viên 2 | Nhật Minh (review soundness) |
| W7 | 4.3 | Viết bảng comparison AS-IS vs TO-BE quy trình 01-03 | `docs/analysis/comparison/01-03.md` | Nhật Minh | — |
| W7 | 4.4 | Viết bảng comparison AS-IS vs TO-BE quy trình 04-06 | `docs/analysis/comparison/04-06.md` | Thành viên 2 | — |
| W8 | 4.5 | ROI/Payback calculation (10 quy trình) | Mục ROI trong comparison + data.json | Thành viên 2 | Nhật Minh (review giả định) |
| W8 | 4.6 | Risk assessment (10 quy trình) | Mục Rủi ro trong comparison | Cả 2 | — |
| W8 | 4.7 | Hoàn thiện Issue Register (thêm giải pháp TO-BE, trạng thái) | `docs/analysis/issue-register.md` (final) | Thành viên 2 | Nhật Minh (góp ý) |
| W8 | 4.8 | Vẽ Pareto waste | `scripts/generate-pareto.py` + ảnh | Nhật Minh | Thành viên 2 (số liệu) |

### Phase 5 — Report Writing (Tuần 9-10)

| Tuần | # | Công việc cụ thể | Deliverable | Người phụ trách | Thành viên còn lại hỗ trợ |
|------|---|-----------------|-------------|-----------------|---------------------------|
| W9 | 5.1 | Viết Chapter 1 (Giới thiệu) + Chapter 2 (Kiến trúc quy trình) | `report/chapter-1-2.md` | Nhật Minh | — |
| W9 | 5.2 | Viết Chapter 3 (Phân tích 10 quy trình) | `report/chapter-3-analysis.md` | Thành viên 2 | Nhật Minh (số liệu BPMN) |
| W9 | 5.3 | Viết Chapter 4 (Kết luận & đề xuất) | `report/chapter-4-conclusion.md` | Thành viên 2 | Nhật Minh (góp ý) |
| W10 | 5.4 | Format báo cáo theo mẫu + mục lục hình/bảng | Báo cáo cuối cùng | Thành viên 2 | — |
| W10 | 5.5 | Glossary 30 terms + Org chart | Phụ lục | Thành viên 2 | Nhật Minh (duyệt nội dung) |
| W10 | 5.6 | Biên bản workshop + kịch bản phỏng vấn | `appendix/workshop-meeting-minutes.md` | Nhật Minh | Thành viên 2 (số liệu) |

### Phase 6 — Review & Polish (Tuần 11-12)

| Tuần | # | Công việc cụ thể | Deliverable | Người phụ trách | Thành viên còn lại hỗ trợ |
|------|---|-----------------|-------------|-----------------|---------------------------|
| W11 | 6.1 | Review chính tả, formatting toàn bộ tài liệu | Final docs | Nhật Minh | — |
| W11 | 6.2 | Sync số liệu cross-files (data.json, comparison, report, slides) | Kiểm tra nhất quán | Thành viên 2 | Nhật Minh (verify BPMN) |
| W11 | 6.3 | Chuẩn bị slides Marp | `presentation/slides.md` + `.html` | Nhật Minh | Thành viên 2 (số liệu) |
| W12 | 6.4 | Rehearse presentation + chia vai thuyết trình | Practice session | Cả 2 | — |
| W12 | 6.5 | Final submission (GitHub + Word + Slides) | Commit + push | Cả 2 | — |

---

## 3. Tỷ lệ đóng góp cuối kỳ

| Hạng mục | Nhật Minh | Thành viên 2 | Ghi chú |
|----------|-----------|--------------|---------|
| BPMN modeling (AS-IS + TO-BE) | 60% | 40% | Nhật Minh: 01-03, Thành viên 2: 04-06 (Thành viên 2 nhận 04-06 nhiều hơn) |
| Qualitative analysis (VA/NVA/Waste/Fishbone) | 60% | 40% | Nhật Minh: VA/NVA + Fishbone, Thành viên 2: Waste |
| Quantitative analysis (Metrics/ROI/data.json) | 20% | 80% | Thành viên 2 là Quantitative Analyst chính |
| Report writing | 50% | 50% | Nhật Minh: Ch1-2, Thành viên 2: Ch3-4 |
| Interviews & Issue Register | 30% | 70% | Thành viên 2 soạn bộ câu hỏi riêng + Issue Register |
| Slides & Presentation | 60% | 40% | Nhật Minh chuẩn bị slides, cả 2 thuyết trình |
| Formatting & Final polish | 30% | 70% | Thành viên 2 phụ trách format chính |
| **Tỷ lệ đóng góp tổng thể** | **~45%** | **~55%** | Cân bằng, nghiêng nhẹ về Thành viên 2 (quantitative) |

> **Lưu ý:** Tỷ lệ này là ước tính dựa trên khối lượng công việc; hai thành viên thống nhất không đòi hỏi chính xác tuyệt đối mà đánh giá theo chất lượng + tính hoàn thành.

---

## 4. Bảng tự đánh giá (Self-Assessment)

> Điền theo thang 1-5 (5 = xuất sắc) trước khi nộp.

| Tiêu chí | Nhật Minh (tự chấm) | Thành viên 2 (tự chấm) |
|----------|---------------------|------------------------|
| Hoàn thành đúng hạn các deliverable | 4 | 4 |
| Chất lượng BPMN models (chuẩn BPMN 2.0, soundness) | 5 | 4 |
| Chất lượng phân tích định tính (VA/NVA/Waste/Fishbone) | 5 | 4 |
| Chất lượng phân tích định lượng (metrics, ROI, data consistency) | 4 | 5 |
| Khả năng hợp tác, phản hồi chéo | 5 | 5 |
| Viết báo cáo & trình bày | 4 | 4 |
| **Điểm trung bình** | **~4.5** | **~4.3** |

---

## 5. Bảng đánh giá chéo (Cross-check)

> Mỗi thành viên chấm điểm cho người kia (thang 1-5) kèm nhận xét cụ thể. Mục đích: phát hiện blind spot, minh bạch, công bằng khi chia điểm cuối kỳ.

### 5.1. Nhật Minh đánh giá Thành viên 2

| Tiêu chí | Điểm (1-5) | Nhận xét cụ thể |
|----------|-----------|-----------------|
| Chất lượng BPMN (04-06) | 4 | BPMN chuẩn, đủ lanes/gateways; cần chú ý sắp xếp layout cho dễ đọc |
| Phân tích định lượng (metrics, ROI) | 5 | Chính xác, có cơ sở giả định rõ ràng, sync tốt với data.json |
| Viết báo cáo (Ch3-4) | 5 | Cấu trúc rõ ràng, số liệu nhất quán |
| Soạn bộ câu hỏi phỏng vấn riêng | 5 | Rất cụ thể theo từng quy trình, đúng yêu cầu |
| Hợp tác & giao tiếp | 5 | Chủ động, phản hồi nhanh, tôn trọng ý kiến |
| **Trung bình** | **~4.8** | — |

### 5.2. Thành viên 2 đánh giá Nhật Minh

| Tiêu chí | Điểm (1-5) | Nhận xét cụ thể |
|----------|-----------|-----------------|
| Chất lượng BPMN (01-03) | 5 | Mô hình chuẩn BPMN 2.0, đủ event/gateway, soundness tốt |
| Phân tích định tính (VA/NVA/Fishbone) | 5 | Phân tích sâu, root cause rõ ràng, có đề xuất actionable |
| Validation Petri Net / soundness | 5 | Chặt chẽ, có script kiểm tra tự động |
| Viết báo cáo (Ch1-2) | 4 | Tốt, cần bổ sung thêm số liệu định lượng ở một số đoạn |
| Chuẩn bị slides & trình bày | 5 | Slides đẹp, logic mạch lạc, thuyết trình rõ ràng |
| Hợp tác & giao tiếp | 5 | Luôn sẵn sàng hỗ trợ, review chéo kỹ |
| **Trung bình** | **~4.8** | — |

---

## 6. Kết luận phân công

1. **Chia việc theo thế mạnh:** Nhật Minh phụ trách mô hình hóa + phân tích định tính; Thành viên 2 phụ trách định lượng + viết báo cáo — đúng khuyến nghị của giảng viên về "chia theo vai trò, không chia theo phòng ban".
2. **Luôn có người review chéo:** Mỗi deliverable quan trọng (BPMN, metrics, comparison) đều có thành viên còn lại kiểm tra để đảm bảo chất lượng + nhất quán số liệu.
3. **Đồng bộ với Gantt:** Lịch trình trong file này khớp với báo cáo chính (6 phase, 12 tuần). Bất kỳ thay đổi deadline nào phải cập nhật cả file này và các file liên quan.

---

> **Rubric tham chiếu:** Điểm số được tính theo chiều: (1) Số lượng deliverable hoàn thành đúng hạn, (2) Chất lượng (đúng BPMN 2.0, số liệu nhất quán, logic rõ ràng), (3) Hợp tác (review chéo, phản hồi kịp thời), (4) Trình bày (slides, báo cáo format chuẩn).

# So sánh AS-IS vs TO-BE: Quy trình Trả hàng & Hoàn tiền

> **Quy trình:** 04 - Trả hàng & Hoàn tiền (Return & Refund)
> **Nguồn AS-IS:** `processes/04-return-refund.bpmn`
> **Nguồn TO-BE:** `processes-to-be/04-return-refund.bpmn`
> **Ngày phân tích:** 2026-09-03
>
> **Ghi chú số liệu:** Các con số không nằm trong tài liệu gốc đều được **dán nhãn "ước tính"**. Bảng hoạt động và số liệu cấu trúc dựa trên **file BPMN thực tế**.

---

## 1. Tóm tắt thay đổi chính (TO-BE)

| # | Thay đổi TO-BE | Mục tiêu | Kết quả mong đợi |
|---|----------------|----------|------------------|
| 1 | **Loại bỏ HandleLateRequest** — xử lý trễ bỏ qua, tập trung vào flow chính | Giảm 20% flow phức tạp, tập trung CSR | Giảm average handling time -15% |
| 2 | **AI Triage** tự động phân loại return (thay CS thủ công) | Giảm load CS cho việc phân loại | Auto-triage trong <2 phút, giảm 60% CS effort |
| 3 | **AI Evidence Verify** tự động kiểm tra bằng chứng (tích hợp vào CheckEligibility) | Cắt bước Manual ReviewEvidence, CS chỉ xử lý exception | Giảm review time -70%, CS chỉ xử lý edge case |
| 4 | **InstantRefund** — hoàn tiền ngay khi AI approve (không cần CS confirm) | Tăng trải nghiệm buyer, giảm processing time | Instant refund 40% case, cycle time giảm -50% |
| 5 | **DynamicPickup** thay SchedulePickup | Tự động hóa lịch pickup | Giảm failed pickup -40%, tiết kiệm logistics cost |
| 6 | **AI Inspection** thay InspectItem thủ công | Giảm reliance inspector vật lý | Tự động inspect 60% case (electronics, clothing) |
| 7 | **CSReview (exception only)** — CS chỉ review khi AI không chắc chắn | Giảm 70% CS workload | CS xử lý 15% case (edge case), 85% tự động |
| 8 | **Timer PT24H refund SLA** — đảm bảo hoàn tiền đúng hạn | Tránh hoàn tiền trễ, tăng trust buyer | SLA compliance từ 65% lên 92% |

---

## 2. Bảng so sánh hoạt động (Activity Comparison Table)

**Phân loại:** KEPT (giữ) | AUTOMATED (tự động hóa) | REMOVED (loại bỏ - NVA) | NEW (thêm mới)

| # | Hoạt động AS-IS | Hoạt động TO-BE (thay thế) | Phân loại | Giải thích thay đổi |
|---|-----------------|----------------------------|-----------|---------------------|
| 1 | Buyer yêu cầu hoàn tiền (Task_SubmitRequest) | Buyer gửi yêu cầu hoàn tiền (Task_SubmitRequest) | **KEPT** | Giữ nguyên |
| 2 | CS xử lý yêu cầu trễ (Task_HandleLateRequest) + Gateway CheckValidTimeWindow | *(loại bỏ — xử lý trễ bỏ qua, tập trung flow chính)* | **REMOVED (NVA)** | Bỏ flow exceptions: CS chỉ xử lý khi cần |
| 3 | Upload bằng chứng (Task_UploadEvidence) | Upload bằng chứng (Task_UploadEvidence) | **KEPT** | Giữ nguyên |
| 4 | Bàn giao/trả hàng (Task_HandoverReturn) | Bàn giao/trả hàng (Task_HandoverReturn) | **KEPT** | Giữ nguyên |
| 5 | Kiểm tra điều kiện hoàn tiền (Task_CheckEligibility) | Kiểm tra điều kiện + Verify bằng chứng (Task_CheckEligibility) | **KEPT (cải tiến)** | Gộp eligibility check + evidence verify thành 1 task |
| 6 | Phân loại bằng chứng CS (Task_TriageEvidence) + 3 gateways (CSLoad, SLA, ReturnCaseType) | AI Triage phân loại hoàn tiền (Task_AITriage) | **AUTOMATED** | AI phân loại replaces manual triage |
| 7 | CS gửi thông báo tình trạng (Task_NotifyStatus) | CS thông báo tình trạng (Task_NotifyStatus) | **KEPT** | Giữ nguyên |
| 8 | CS xem xét bằng chứng (Task_ReviewEvidence) + Gateway ValidEvidence | *(loại bỏ — AI Evidence Verify tích hợp trong CheckEligibility)* | **REMOVED (NVA)** | AI verify tự động, CS chỉ xử lý khi AI không chắc chắn |
| 9 | Hẹn lịch pickup (Task_SchedulePickup) | Dynamic Pickup tự động (Task_DynamicPickup) | **AUTOMATED** | AI tính toán route + lịch optimal; lịch pickup tự động hóa, giảm tần suất cần reschedule |
| 10 | Pickup hàng trả (Task_PickupReturn) | Pickup hàng trả (Task_PickupReturn) | **KEPT** | Giữ nguyên |
| 11 | Trả lại lịch pickup (Task_ReschedulePickup) | Đặt lại lịch pickup (Task_ReschedulePickup, userTask) | **KEPT (cải tiến)** | Giữ retry loop qua Gate_PickupRetry; lịch đặt lại được tự động hóa bởi DynamicPickup, giảm tần suất reschedule |
| 12 | Kiểm tra chất lượng (Task_InspectItem) | AI kiểm tra + CS review exception (Task_AIInspection) | **AUTOMATED** | AI inspection + CS review edge case |
| 13 | Process hoàn tiền (Task_ProcessRefund) | Process hoàn tiền + InstantRefund (Task_ProcessRefund + Task_InstantRefund) | **AUTOMATED** | Thêm instant refund path cho case auto-approved |
| 14 | *(không có)* | CS Review exception (Task_CSReview) | **NEW** | CS chỉ xử lý khi AI không chắc chắn |
| 15 | *(không có)* | Execute hoàn tiền (Task_ExecuteRefund) | **NEW** | Task tách riêng để xử lý payment refund |

### Tổng hợp phân loại

| Phân loại | Số lượng | Danh sách |
|-----------|----------|-----------|
| **KEPT** | 7 | #1, 3, 4, 5, 7, 10, 11 |
| **AUTOMATED** | 4 | #6 (AI Triage), #9 (DynamicPickup), #12 (AIInspection), #13 (InstantRefund) |
| **NEW** | 2 | #14 (CSReview), #15 (ExecuteRefund) |
| **REMOVED (NVA)** | 2 | #2 (HandleLateRequest), #8 (ReviewEvidence) |

---

## 3. So sánh cấu trúc mô hình (Structure Comparison)

| Tiêu chí | AS-IS (file BPMN) | TO-BE (file BPMN) | Thay đổi |
|----------|-------------------|-------------------|----------|
| Số lanes | 5 (Buyer, System, CS, Warehouse, Payment) | 5 (Buyer, System, CS, Warehouse, Payment) | 0 |
| Số activities (tasks) | 13 (user: 6, service: 6+1) | 16 (user: 5, service: 10+1) | +3 (thêm AI + InstantRefund, bỏ 2 NVA) |
| Số named gateways (decision) | 9 | 5 | **-4** (gộp 3 gateway triage, bỏ NeedReschedule) |
| Số all gateways (incl join/split) | 18 | 9 | **-9** |
| Số timer events (SLA) | 0 | 1 (PT24H refund SLA) | **+1** (mới) |
| Số start events | 1 | 1 | 0 |
| Số end events | 2 | 2 | 0 |
| Số sequence flows | 43 | 33 | **-10 (-23%)** |

**Phân bố task theo lane:**

| Lane | AS-IS | TO-BE | Thay đổi |
|------|-------|-------|----------|
| Buyer | 2 (SubmitRequest, UploadEvidence) | 2 (SubmitRequest, UploadEvidence) | 0 |
| System | 4 (HandleLateRequest, CheckEligibility, TriageEvidence, NotifyStatus) | 5 (CheckEligibility, AITriage, AIEvidenceVerify, InstantRefund, NotifyStatus) | +1 (thêm AI modules) |
| CS | 2 (ReviewEvidence, ProcessRefund) | 3 (CSReview, ProcessRefund, ExecuteRefund) | +1 (tách CSReview + ExecuteRefund) |
| Warehouse | 3 (HandoverReturn, SchedulePickup, ReschedulePickup, InspectItem) | 3 (HandoverReturn, DynamicPickup, PickupReturn, AIInspection) | 0 (Dynamic replaces Schedule+Reschedule) |
| Payment | 1 | 1 | 0 |

---

## 4. Bảng so sánh Metrics (Định lượng)

| Metric | AS-IS (ước tính) | TO-BE (expected) | Cải thiện |
|--------|------------------|------------------|-----------|
| **Cycle time trung bình** | **8,5 ngày** | **1,8 ngày** | **-78,8%** |
| **Cycle time instant refund** | **Không có** | **<24 giờ** | **NEW** |
| **Tỷ lệ instant refund** | **15%** | **45%** (AI auto-approve) | **+30%** |
| **CS effort per case** | **45 phút** (ước tính) | **15 phút** (ước tính) | **-67%** |
| **Failed pickup rate** | **10%** (ước tính) | **4%** (DynamicPickup) | **-60%** |
| **SLA compliance (hoàn tiền ≤7 ngày)** | **65%** | **92%** (Timer 24h SLA) | **+42%** |
| **Buyer satisfaction (CSAT)** | **64%** (3,2/5) | **90%** (4,5/5) | **+40,6%** |
| **Gateways** | **18** | **9** | **-50%** |
| **Sequence flows** | **43** | **33** | **-23%** |

### 4.1. Chi tiết chi phí (ước tính, per return/refund)

| Thành phần chi phí | AS-IS | TO-BE | Thay đổi |
|--------------------|-------|-------|----------|
| CS review time (CS Staff) | 52,000 VND | 18,000 VND | **-34,000** (CS effort 45 phút → 15 phút) |
| Reverse logistics (pickup + vận chuyển ngược) | 30,000 VND | 15,000 VND | **-15,000** (pickup fail 10%→4%, route optimization) |
| Warehouse inspection | 15,000 VND | 5,000 VND | **-10,000** (AI inspection, 8h→2h) |
| Payment processing / refund fee | 2,000 VND | 2,000 VND | 0 (giữ nguyên gateway fee) |
| Hàng tồn kho hư hao | 10,000 VND | 5,000 VND | **-5,000** (giảm spoilage qua AI inspection) |
| **TỔNG CHI PHÍ** | **109,000 VND** | **45,000 VND** | **-64,000 (-59%)** |

### 4.2. Cycle time chi tiết (ước tính)

| Giai đoạn | AS-IS | TO-BE (ước tính) | Ghi chú |
|-----------|-------|------------------|---------|
| Buyer submit request | instant | instant | Giữ |
| Late request handling | 1-3 ngày | 0 (bỏ) | **NVA removed** |
| AI Triage + evidence verify | 1 ngày (CS thủ công) | 10 phút (AI) | **AI tự phân loại** |
| CS review | 2-3 ngày (CS load) | 0-1 ngày (edge case only) | CS chỉ xử lý 15% |
| Dynamic pickup | 1-2 ngày | 6 giờ (auto) | **Auto scheduling** |
| AI Inspection + Return decision | 1 ngày | 2 giờ (AI + CS exception) | AI inspect 60% |
| Refund processing | 1-2 ngày | Instant-24h | **InstantRefund + SLA timer** |
| **Tổng trung bình** | **~8,5 ngày** | **~1,8 ngày** | **-78,8%** |

---

## 5. ROI — Ước tính đầu tư và thời gian hoàn vốn

> Toàn bộ số liệu mục này là **ước tính** cho mục đích trình bày BA (business case).

### 5.1. Đầu tư ban đầu (one-time, ước tính)

| Hạng mục | Chi phí (tỷ VND) | Ghi chú |
|----------|------------------|---------|
| AI Triage + Evidence Verify Model | 1.2 | ML training trên historical returns |
| AI Inspection Model (computer vision) | 1.0 | Product image analysis + classification |
| DynamicPickup Engine | 0.7 | Route optimization + scheduling algorithm |
| InstantRefund + Payment integration | 0.8 | Payment gateway instant refund feature |
| CSReview (exception handling) workflow | 0.4 | Workflow redesign + CS training |
| Timer SLA 24h + monitoring | 0.3 | SLA engine + dashboard |
| Testing, QA, rollout | 0.4 | UAT + phased rollout |
| **TỔNG ĐẦU TƯ BAN ĐẦU** | **4.8 tỷ VND** (~200K USD) | |

**Chi phí vận hành hằng năm:** ~1.3 tỷ VND/năm (AI inference, pickup routing, instant refund fees, monitoring).

### 5.2. Lợi ích hàng năm (ước tính)

**Giả định:** ~300,000 return/refund cases/năm trên Lazada VN.

| Nguồn lợi ích | Công thức | Giá trị (tỷ VND/năm) |
|---------------|-----------|----------------------|
| Tiết kiệm CS effort | 34,000 VND x 300K cases | 10.2 |
| Tiết kiệm warehouse (AI inspection) | 10,000 VND x 300K cases | 3.0 |
| Giảm failed pickup | 6% x 300K x 5,000 VND | 0.09 |
| Tăng buyer retention (better experience) | 5% x 300K x 10,000 LTV | 0.15 |
| **Tổng lợi ích tiềm năng** | | **13.44** |
| Lợi ích năm đầu thực thu (55%) | 13.44 x 55% | **7.4** |
| Trừ chi phí vận hành hằng năm | | -1.3 |
| **Lợi ích ròng năm đầu** | | **~6.1 tỷ VND/năm** |

> **Ghi chú tính toán:** Delta CS 34,000 VND (= 52,000 → 18,000, Mục 4.1 & Bảng 3.9 report) và delta warehouse 10,000 VND (= 15,000 → 5,000, Mục 4.1) là số của chính tài liệu này. Failed pickup 6% (= 10% → 4%, Mục 4.1/KPI) thay vì 7% cũ — số cũ không khớp delta chuẩn. Hệ số thực thu 55% phản ánh ramp-up theo phased rollout và dự phòng rủi ro lạm dụng InstantRefund (Mục 6, Rủi ro #2).

### 5.3. Thời gian hoàn vốn (Payback)

| Kịch bản | Giả định | Payback |
|----------|----------|---------|
| **Cơ sở (Base)** | 300K cases/năm, 55% thực thu | 4.8 / 6.1 ≈ **~10 tháng** |
| **Thận trọng (Conservative)** | 150K cases/năm, 45% hiệu quả | 4.8 / 2.4 ≈ **~24 tháng** |

> **Conservative:** 13.44 x (150K/300K) x 45% = ~3.0 tỷ; opex co giãn theo volume (~0.65 tỷ); ròng ~2.4 tỷ/năm → payback ~24 tháng.

- **Kết luận ROI:** Kịch bản cơ sở hoàn vốn ~10 tháng; kịch bản thận trọng ~24 tháng (2 năm). ROI hấp dẫn nhờ chi phí lãng phí hiện hữu lớn (Pickup thất bại 28 tỷ/tháng + inspection chậm 22 tỷ/tháng + CS manual 7 tỷ/tháng, Analysis 04 §3.4.5). Khuyến nghị phased rollout: VN → TH → ID.

---

## 6. Rủi ro của TO-BE và giải pháp giảm thiểu

| # | Rủi ro | Mức độ | Giải pháp giảm thiểu (Mitigation) |
|---|--------|--------|------------------------------------|
| 1 | **AI Evidence Verify chấp nhận evidence giả** | Cao | (a) Multi-signal: image hash + metadata + order data cross-check; (b) Human review cho high-value; (c) Anti-fraud model |
| 2 | **InstantRefund bị lợi dụng (buyer/gian lận)** | Cao | (a) Ngưỡng confidence >95%; (b) Fraud scoring cho buyer; (c) Daily limit auto-refund; (d) Audit 15% instant refunds |
| 3 | **DynamicPickup fail khi 3PL overload** | Trung bình | (a) Real-time 3PL capacity monitoring; (b) Fallback manual scheduling; (c) Multi-provider failover |
| 4 | **AI Inspection sai khi qualitate item** | Trung bình | (a) Training trên đa dạng sản phẩm; (b) Human fallback cho expensive items; (c) Confidence threshold + CS review |
| 5 | **Timer SLA 24h không resolve được hoàn tiền** | Thấp | (a) Multi-tier escalation; (b) Dashboard realtime tracking; (c) Auto-escalate khi timer expiry |

---

## 7. Kết luận

1. **TO-BE giữ 7 hoạt động gốc**, tự động hóa 4 hoạt động (Triage, Pickup, Inspection, Refund), thêm 2 hoạt động mới (CSReview exception, ExecuteRefund), và loại bỏ 2 hoạt động NVA (HandleLateRequest, ReviewEvidence, NVA-related gateways). CS chỉ xử lý 15% edge case — phân công đúng trọng tâm.
2. **Metrics:** Cycle time giảm 78,8% (8,5 ngày → 1,8 ngày), chi phí/return giảm 59% (109K → 45K VND, Mục 4.1), gateway giảm 18 → 9 (-50%), flows 43 → 33 (-23%), SLA compliance +42%, buyer satisfaction (CSAT) +40,6% (3,2/5 → 4,5/5).
3. **ROI:** Đầu tư 4.8 tỷ VND, payback ~10 tháng (cơ sở) / ~24 tháng (thận trọng). Cần scale region-wide để amortize AI training costs.
4. **Hành động tiếp theo:** (a) Phê duyệt Phase 1 (AI Triage + InstantRefund ~2.0 tỷ); (b) Chuẩn bị training data returns 12 tháng; (c) Pilot DynamicPickup tại HCM; (d) Xác thực instant refund fraud risk với Risk team.

---

## 8. Tham chiếu

- AS-IS BPMN: `processes/04-return-refund.bpmn`
- TO-BE BPMN: `processes-to-be/04-return-refund.bpmn`

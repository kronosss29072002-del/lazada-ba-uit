# So sánh AS-IS vs TO-BE: Quy trình Quản lý Tranh chấp

> **Quy trình:** 02 - Quản lý Tranh chấp (Dispute Management)
> **Nguồn AS-IS:** `processes/02-dispute-management.bpmn`
> **Nguồn TO-BE:** `processes-to-be/02-dispute-management.bpmn`
> **Ngày phân tích:** 2026-09-03
>
> **Ghi chú số liệu:** Các con số không nằm trong tài liệu gốc đều được **dán nhãn "ước tính"**. Bảng hoạt động và số liệu cấu trúc dựa trên **file BPMN thực tế**.

---

## 1. Tóm tắt thay đổi chính (TO-BE)

| # | Thay đổi TO-BE | Mục tiêu | Kết quả mong đợi |
|---|----------------|----------|------------------|
| 1 | Thêm **AI Engine lane** (tầng mới) — AI Triage + AI Evidence Verify | Phân loại tranh chấp tự động, giảm load CS | Auto-triage tranh chấp trong <1 phút, giảm 60% case CS xử lý thủ công |
| 2 | **Structured Upload** thay Text Upload (buyer/seller evidence) | Chuẩn hóa bằng chứng, hỗ trợ AI verify | Giảm thời gian thu thập evidence -40%, tăng accuracy AI phân loại |
| 3 | **Auto Refund cho case rõ ràng <200K VND** | Loại bỏ bottleneck CS cho case nhỏ | ~35% case tự động refund, giảm 70% effort CS cho tier thấp |
| 4 | **Dynamic SLA** — 24h case đơn giản, 48h case phức tạp | Phân tầng thời gian xử lý theo mức độ | Case đơn giản xử lý nhanh hơn -50%, SLA compliance tăng |
| 5 | **Timer SLA** (PT24H, PT48H, PT12H escalation) | Đảm bảo đúng hạn, tránh case treo | Giảm case overdue -80%, escalation tự động đúng 12h |
| 6 | **Settle Service Task** (thay manual settlement) | Hỗ trợ CS đưa ra đề xuất giải quyết | Giảm time-to-resolution -30%, CS đưa ra quyết định nhanh hơn |

---

## 2. Bảng so sánh hoạt động (Activity Comparison Table)

**Phân loại:** KEPT (giữ) | AUTOMATED (tự động hóa) | REMOVED (loại bỏ - NVA) | NEW (thêm mới)

| # | Hoạt động AS-IS | Hoạt động TO-BE (thay thế) | Phân loại | Giải thích thay đổi |
|---|-----------------|----------------------------|-----------|---------------------|
| 1 | Buyer tạo tranh chấp (Task_CreateDispute) | Buyer tạo tranh chấp (Task_CreateDispute) | **KEPT** | Giữ nguyên |
| 2 | Buyer tải lên bằng chứng (Task_ReplyEvidence) | Upload bằng chứng có cấu trúc (Task_StructuredUpload) | **KEPT (cải tiến)** | Structured upload: buyer/seller upload đúng format, AI verify tự động |
| 3 | CS yêu cầu thêm bằng chứng (Task_RequestMoreEvidence) + Gateway NeedsMoreInfo | *(loại bỏ — structured upload giảm yêu cầu bổ sung)* | **REMOVED (NVA)** | Structured upload đảm bảo đủ info ngay từ đầu |
| 4 | CS thu thập thông tin bổ sung (Task_CollectData) | AI thu thập & phân loại tranh chấp (Task_CollectData) | **AUTOMATED** | AI tự trích xuất thông tin từ structured evidence + order data |
| 5 | CS phân loại đánh giá sơ bộ (Task_AuthTriage) | AI Triage tự động phân loại (Task_AITriage) | **AUTOMATED** | AI Engine lane mới, tự phân loại case đơn/gấp/tổng hợp |
| 6 | Kiểm tra SLA & lịch sử xử lý (Task_CheckSLAHistory) + 3 gateways (CheckSLAHistory, AutoRefund, CheckCSLoad) | Tính toán SLA động theo mức độ phức tạp (Task_ComputeDynamicSLA) | **AUTOMATED** | Gộp 3 task + 3 gateways thành 1 service task SLA tính toán |
| 7 | *(không có)* | Auto Refund case đơn giản <200K VND (Task_AutoRefund) | **NEW** | AI xác định case rõ ràng, refund tự động không cần CS |
| 8 | CS thông báo các bên (Task_NotifyParties) | CS thông báo các bên (Task_NotifyParties) | **KEPT** | Giữ nguyên |
| 9 | Seller phản hồi (Task_SellerReply) + Gateway SellerReplied? | Seller phản hồi (Task_SellerReply) | **KEPT** | Bỏ gateway check — timer SLA tự xử lý nếu seller không reply |
| 10 | CS xem xét tranh chấp (Task_ReviewCase) | CS xem xét tranh chấp (Task_ReviewCase) | **KEPT** | Giữ nguyên |
| 11 | CS ra quyết định (Task_Decide) | CS ra quyết định (Task_Decide) | **KEPT** | Giữ nguyên |
| 12 | *(không có)* | CS đưa ra đề xuất giải quyết (Task_Settle) | **NEW** | Service task hỗ trợ CS tính toán phương án settle tối ưu |
| 13 | Escalate lên CS Higher (Task_Escalate) | Escalate lên CS Higher (Task_Escalate) | **KEPT** | Giữ nguyên |
| 14 | CS Higher xem xét lại (Task_SeniorReview) | CS Higher xem xét lại (Task_SeniorReview) | **KEPT** | Giữ nguyên |
| 15 | **End events:** Buyer/Seller approved + Settlement reached | **End events:** Buyer/Seller approved + Settlement reached | **KEPT** | Giữ nguyên |

### Tổng hợp phân loại

| Phân loại | Số lượng | Danh sách |
|-----------|----------|-----------|
| **KEPT** | 8 | #1, 8, 9, 10, 11, 14, 15, #12 (partial) |
| **AUTOMATED** | 4 | #4 (AI CollectData), #5 (AI Triage), #6 (Dynamic SLA), #2 (cải tiến structured) |
| **NEW** | 2 | #7 (Auto Refund), #12 (Settle) |
| **REMOVED (NVA)** | 1 | #3 (RequestMoreEvidence + NeedsMoreInfo gateway) |

---

## 3. So sánh cấu trúc mô hình (Structure Comparison)

| Tiêu chí | AS-IS (file BPMN) | TO-BE (file BPMN) | Thay đổi |
|----------|-------------------|-------------------|----------|
| Số lanes | 5 (Buyer, System, Seller, CS, Escalation) | 6 (Buyer, System, Seller, CS, Escalation, **AI Engine**) | **+1** (AI Engine lane mới) |
| Số activities (tasks) | 12 (user: 8, service: 4) | 13 (user: 7, service: 6) | +1 (thêm AutoRefund + Settle, bỏ RequestMoreEvidence) |
| Số named gateways (decision) | 8 | 4 | **-4** (gộp 3 gateway SLA thành 1, bỏ NeedsMoreInfo) |
| Số all gateways (incl join/split) | 16 | 9 | **-7** |
| Số timer events (SLA) | 0 | 3 (PT24H, PT48H, PT12H) | **+3** (mới — Dynamic SLA timers) |
| Số start events | 1 | 1 | 0 |
| Số end events | 3 | 3 | 0 |
| Số sequence flows | 38 | 32 | **-6 (-16%)** |

**Phân bố task theo lane:**

| Lane | AS-IS | TO-BE | Thay đổi |
|------|-------|-------|----------|
| Buyer | 2 (CreateDispute, ReplyEvidence) | 2 (CreateDispute, StructuredUpload) | 0 (cải tiến upload) |
| System | 4 (CollectData, AuthTriage, CheckSLAHistory, NotifyParties) | 3 (CollectData, ComputeDynamicSLA, NotifyParties) | -1 (gộp SLA checks) |
| Seller | 1 (SellerReply) | 1 (SellerReply) | 0 |
| CS | 3 (ReviewCase, Decide, Escalate) | 4 (ReviewCase, Decide, Settle, Escalate) | +1 (thêm Settle) |
| Escalation | 1 (SeniorReview) | 1 (SeniorReview) | 0 |
| **AI Engine** | **0** | **2 (AITriage, AutoRefund)** | **+2 (lane mới)** |

---

## 4. Bảng so sánh Metrics (Định lượng)

| Metric | AS-IS (ước tính) | TO-BE (expected) | Cải thiện |
|--------|------------------|------------------|-----------|
| **Cycle time trung bình** | **5,2 ngày** (phức tạp lên đến 14 ngày) | **2,8 ngày** (SLA timer) | **-46%** |
| **Effort CS / case** | **45 phút** (ước tính) | **20 phút** (ước tính) | **-56%** |
| **First-Contact Resolution (FCR)** | **45%** (ước tính) | **80-85%** (ước tính) | **+35-40 điểm %** |
| **Case overdue (>7 ngày)** | **25%** (ước tính) | **5%** (ước tính) | **-80%** |
| **CS cost / case** | **68,000 VND** | **19,000 VND** | **-72%** |
| **Escalation rate** | **20%** (ước tính) | **5-8%** (ước tính) | **-60-75%** |
| **Named gateways** | **8** | **4** | **-50%** |

### 4.1. Chi tiết chi phí (ước tính, per case)

| Thành phần chi phí | AS-IS | TO-BE | Thay đổi |
|--------------------|-------|-------|----------|
| CS agent time (45 phút → 20 phút) | 45,000 VND | 10,000 VND | **-35,000** (AI hỗ trợ quyết định) |
| Escalation handling (20% → 5-8% cases) | 16,000 VND | 4,000 VND | **-12,000** (giảm escalation) |
| System infrastructure (AI, notification) | 3,000 VND | 3,000 VND | 0 |
| Payment processing fee | 1,000 VND | 1,000 VND | 0 |
| Re-work evidence rounds (30% → 10%) | 3,000 VND | 1,000 VND | **-2,000** (AI evidence verify) |
| **TỔNG CHI PHÍ** | **68,000 VND** | **19,000 VND** | **-49,000 (-72%)** |

### 4.2. Cycle time chi tiết (ước tính)

| Giai đoạn | AS-IS | TO-BE (ước tính) | Ghi chú |
|-----------|-------|------------------|---------|
| Buyer tạo tranh chấp + upload evidence | 10 phút | 5 phút | Structured upload nhanh hơn |
| AI Triage + phân loại | 30 phút (CS làm) | <1 phút (AI tự động) | **AI Engine mới** |
| Thu thập + phân tích dữ liệu | 60 phút | 15 phút (AI auto) | AI trích xuất order data |
| Tính toán SLA + phân tầng | 15 phút (3 task riêng) | Instant (1 service task) | Gộp 3 task thành 1 |
| Auto Refund (nếu apply) | Không có | Instant | **Case <200K, clear evidence** |
| CS xem xét + quyết định | 30-60 phút | 20-40 phút | Settle suggestions giúp nhanh hơn |
| Notify + Escalation (nếu cần) | 30 phút | 15 phút | Timer tự escalate 12h |
| **Tổng trung bình** | **~5,2 ngày** | **~2,8 ngày** | **-46%** |

---

## 5. ROI — Ước tính đầu tư và thời gian hoàn vốn

> Toàn bộ số liệu mục này là **ước tính** cho mục đích trình bày BA (business case).

### 5.1. Đầu tư ban đầu (one-time, ước tính)

| Hạng mục | Chi phí (tỷ VND) | Ghi chú |
|----------|------------------|---------|
| AI Triage Model (ML classification) | 1.5 | Training trên historical disputes, multi-class |
| AI Evidence Verification (NLP + image analysis) | 1.0 | Verify uploaded evidence automatically |
| Dynamic SLA Engine + Timer System | 0.5 | Rule engine + timer orchestration |
| Auto Refund Logic + Fraud Prevention | 0.6 | Case routing + fraud detection |
| Structured Upload UI redesign | 0.4 | Frontend Buyer + Seller portals |
| Settle Suggestion Engine | 0.3 | Decision support for CS |
| Testing, QA, pilot rollout | 0.4 | UAT + phased rollout |
| **TỔNG ĐẦU TƯ BAN ĐẦU** | **4.7 tỷ VND** (~195K USD) | |

**Chi phí vận hành hằng năm:** ~1.2 tỷ VND/năm (AI inference, timer system, monitoring).

### 5.2. Lợi ích hàng năm (ước tính)

**Giả định:** ~150,000 tranh chấp/năm trên Lazada VN.

| Nguồn lợi ích | Công thức | Giá trị (tỷ VND/năm) |
|---------------|-----------|----------------------|
| Tiết kiệm CS staff time | 13,000 VND x 150K cases | 1.95 |
| Auto-resolve case nhỏ (<200K) | 35% x 150K x 15,000 VND saved | 0.79 |
| Giảm escalation (20% → 5-8%) | 12% x 130.6K x 80,000 VND | 1.25 |
| Tăng buyer satisfaction → repeat purchase | 10% improvement x 150K x 5,000 VND | 0.075 |
| **Tổng lợi ích tiềm năng** | | **4.065** |
| Lợi ích năm đầu thực thu (55%) | 4.065 x 55% | **2.24** |
| Trừ chi phí vận hành hằng năm | | -1.2 |
| **Lợi ích ròng năm đầu** | | **~1.04 tỷ VND/năm** |

### 5.3. Thời gian hoàn vốn (Payback)

| Kịch bản | Giả định | Payback |
|----------|----------|---------|
| **Cơ sở (Base)** | 150K cases/năm, 55% efficiency gain | 4.7 / 1.04 ≈ **~54 tháng** |
| **Thận trọng (Conservative)** | 80K cases/năm, 30% efficiency gain | 4.7 / (0.52 - 1.2) → **Chưa hoàn vốn trong 3 năm** |

- **Kết luận ROI:** Kịch bản cơ sở hoàn vốn sau ~4,5 năm (54 tháng) — ROI chậm nhất trong nhóm, do lợi ích/ca thấp và chi phí vận hành cao. DRAGON expansion (VN, TH, ID, PH, MY) giúp cắt giảm chi phí AI model qua re-use → break-even sớm hơn. Khuyến nghị **pilot trước tại VN** và scale khi có trên 200K cases/năm.

---

## 6. Rủi ro của TO-BE và giải pháp giảm thiểu

| # | Rủi ro | Mức độ | Giải pháp giảm thiểu (Mitigation) |
|---|--------|--------|------------------------------------|
| 1 | **AI Triage phân loại sai — case phức tạp bị auto-refund** | Cao | (a) Ngưỡng confidence >95% cho auto-refund; (b) Human-in-the-loop cho case >200K; (c) Shadow mode 3 tháng; (d) Audit 10% auto-refund cases |
| 2 | **AI Evidence Verify chấp nhận evidence giả** | Cao | (a) Multi-signal verification (image hash + metadata + order data); (b) Human review cho high-value cases; (c) Anti-fraud model cross-check |
| 3 | **Dynamic SLA timer miss — case overdue không escalate** | Trung bình | (a) Multi-tier timer monitoring (24h → 48h → 12h); (b) Dashboard realtime SLA tracking; (c) Auto-escalation khi timer expiry |
| 4 | **Seller không reply trong SLA (48h)** | Trung bình | (a) Timer auto-escalate sau 48h; (b) Auto-decide favoring buyer nếu seller silent; (c) Seller penalty points cho late reply |
| 5 | **Phụ thuộc AI vendor (model drift)** | Thấp-Trung bình | (a) Monthly model retraining; (b) Performance monitoring dashboard; (c) Fallback manual triage khi AI unavailable |

---

## 7. Kết luận

1. **TO-BE giữ 8 hoạt động gốc**, tự động hóa 4 hoạt động (CollectData, AI Triage, Dynamic SLA, Structured Upload), thêm 2 hoạt động mới (Auto Refund, Settle), và loại bỏ 1 hoạt động NVA (RequestMoreEvidence). Thêm **AI Engine lane** là thay đổi kiến trúc lớn nhất — tách AI reasoning ra khỏi System lane.
2. **Metrics:** Cycle time giảm 46% (5,2 ngày → 2,8 ngày), CS cost/case giảm 72% (68K → 19K VND), First-Contact Resolution tăng từ 45% lên 80-85% (+35-40 điểm %), escalation giảm 60-75% (20% → 5-8%). Auto-resolve 35% case nhỏ là cải tiến lớn nhất.
3. **ROI:** đầu tư ban đầu ~4.7 tỷ VND (ước tính), payback ~5 năm (cơ sở). Cần scale DRM region-wide để đạt economies of scale. Khuyến nghị pilot VN trước.
4. **Hành động tiếp theo:** (a) Phê duyệt pilot Phase 1 (AI Triage + Dynamic SLA ~2.0 tỷ); (b) Chuẩn bị training data historical disputes 12 tháng; (c) Xác thực ngưỡng confidence với CS team; (d) Draft SLA policy mới cho seller response time.

---

## 8. Tham chiếu

- AS-IS BPMN: `processes/02-dispute-management.bpmn`
- TO-BE BPMN: `processes-to-be/02-dispute-management.bpmn`

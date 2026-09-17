# So sánh AS-IS vs TO-BE: Quy trình Quản lý Nhà bán hàng

> **Quy trình:** 01 - Quản lý Nhà bán hàng (Seller Management)
> **Nguồn AS-IS:** `processes/01-seller-management.bpmn`
> **Nguồn TO-BE:** `processes-to-be/01-seller-management.bpmn`
> **Ngày phân tích:** 2026-09-03
>
> **Ghi chú số liệu:** Các con số không nằm trong tài liệu gốc đều được **dán nhãn "ước tính"**. Bảng hoạt động và số liệu cấu trúc dựa trên **file BPMN thực tế**.

---

## 1. Tóm tắt thay đổi chính (TO-BE)

| # | Thay đổi TO-BE | Mục tiêu | Kết quả mong đợi |
|---|----------------|----------|------------------|
| 1 | Smart Scan upload CCCD & GPKD (gộp upload + validate) | Giảm bước nhập liệu trùng lặp | Giảm thời gian đăng ký -40% |
| 2 | AI OCR + Chống giấy tờ giả + Real-time eKYC sinh trắc học (gộp 3 bước) | Loại bỏ validate trùng, tăng bảo mật | Giảm thời gian từ 10 phút xuống 3 phút |
| 3 | AI Risk Scoring tự động → Auto-approve low-risk 3 giây | Loại bỏ bottleneck compliance cho ~90% seller | SLA auto-approve giảm từ 24h xuống 3 giây |
| 4 | Timer SLA 24h cho compliance review | Tránh case bị treo vô thời hạn | Compliance review giảm từ 48h xuống 24h SLA |
| 5 | Giám sát vi phạm AI realtime (thay rule-based) | Phát hiện sớm vi phạm | Giảm time-to-detect vi phạm -60% |
| 6 | Giảm 3.join/split gate + 3 named gateway | Đơn giản hóa luồng | Giảm 31% sequence flows (42 → 29) |

---

## 2. Bảng so sánh hoạt động (Activity Comparison Table)

**Phân loại:** KEPT (giữ) | AUTOMATED (tự động hóa) | REMOVED (loại bỏ - NVA) | NEW (thêm mới)

| # | Hoạt động AS-IS | Hoạt động TO-BE (thay thế) | Phân loại | Giải thích thay đổi |
|---|-----------------|----------------------------|-----------|---------------------|
| 1 | Seller đăng ký gian hàng (start) | Seller đăng ký mới (start) | **KEPT** | Giữ nguyên |
| 2 | Điền thông tin định danh Seller (Task_Register) | Điền thông tin định danh Seller (T_Reg) | **KEPT** | Giữ nguyên |
| 3 | Xác thực SĐT qua OTP (Task_VerifyPhone) + Gateway SĐT đã xác thực? | *(loại bỏ — gộp vào Smart Scan)* | **REMOVED (NVA)** | Bước OTP riêng lẻ bị loại, xác thực được tích hợp vào flow upload Smart Scan |
| 4 | Upload CMND/CCCD + GPKD (Task_UploadDocs) | Upload CCCD & GPKD — Smart Scan (T_Upload) | **KEPT (cải tiến)** | Smart Scan giúp seller upload 1 lần, OCR tự động trích xuất thông tin |
| 5 | Validate định danh tự động (Task_ValidateIdentity) | Validate tự động qua API (T_Validate) | **AUTOMATED** | Nâng cấp API validation realtime, không cần chờ batch |
| 6 | Validate tài khoản ngân hàng (Task_FixBankInfo) + Gateway BankValid | *(loại bỏ — kiểm tra tích hợp trong API)* | **REMOVED (NVA)** | Kiểm tra tài khoản NH được tích hợp vào API validate, không cần task riêng |
| 7 | Quét OCR + kiểm tra giấy tờ giả (Task_OCRCheck) | AI OCR & Chống giấy tờ giả (T_AI_Doc) | **AUTOMATED** | Nâng cấp từ OCR cơ bản sang AI OCR + chống giả mạo |
| 8 | Gateway: Giấy tờ hợp lệ? (Gate_DocValid) | *(loại bỏ — AI tự xử lý pass/fail)* | **REMOVED (NVA)** | AI tự phân loại và quyết định, không cần gateway riêng |
| 9 | Bổ sung/sửa hồ sơ (Task_FixRejection) + Gateway ResubmitLimit | *(loại bỏ — Smart Scan giảm lỗi)* | **REMOVED (NVA)** | Smart Scan giảm đáng kể lỗi upload, bỏ loop resubmit |
| 10 | *(không có)* | Real-time eKYC sinh trắc học (T_KYC) | **NEW** | Bổ sung liveness detection + face matching, tăng bảo mật |
| 11 | Chấm điểm rủi ro (Task_ScoreRisk) | AI Risk Scoring tự động (T_Risk) | **AUTOMATED** | Nâng cấp rule-based sang AI/ML scoring |
| 12 | Gateway: Có nghi vấn rủi ro cao? + Gateway Phân tầng rủi ro (Gate_RiskDoubt + Gate_AutoApprove) | Gateway: Mức độ rủi ro? (G_Risk) — 3 nhánh: Auto/Appr, Manual, Timeout | **AUTOMATED** | Gộp 2 gateway thành 1 gateway thông minh với 3 nhánh rõ ràng |
| 13 | Compliance review thủ công 24-48h (Task_ManualReview) + Gateway Approve | Compliance review hồ sơ nghi vấn + Timer SLA 24h (T_Manual) | **KEPT (+ SLA)** | Giữ manual review nhưng giới hạn 24h SLA, chỉ xử lý hồ sơ >10% rủi ro |
| 14 | *(không có)* | Tự động kích hoạt — Low-risk 3 giây (T_AutoAppr) | **NEW** | ~90% seller low-risk được approve trong 3 giây, không cần compliance |
| 15 | Thông báo kết quả duyệt Seller Centre (Task_NotifyResult) | Thông báo kết quả tức thì (T_Notify) | **KEPT (cải tiến)** | Nâng cấp thành real-time notification |
| 16 | Giám sát điểm đánh giá & vi phạm (Task_MonitorViolations) | Giám sát vi phạm AI realtime (T_Monitor) | **AUTOMATED** | Nâng cấp sang AI anomaly detection real-time |
| 17 | Gateway: Mức độ vi phạm? (Gate_ViolationSeverity) | Gateway: Mức độ vi phạm? (G_Viol) | **KEPT** | Giữ nguyên logic 3 nhánh warn/suspend/ban |
| 18 | Gửi cảnh cáo Seller (Task_Warn) | Gửi cảnh cáo & trừ điểm sao (T_Warn) | **KEPT** | Bổ sung auto-deduct sao |
| 19 | Tạm khóa gian hàng 7 ngày (Task_Suspend) | Tạm khóa gian hàng 7 ngày (T_Suspend) | **KEPT** | Giữ nguyên |
| 20 | Khóa gian hàng vĩnh viễn (Task_Ban) | Khóa vĩnh viễn gian hàng (T_Ban) | **KEPT** | Giữ nguyên |

### Tổng hợp phân loại

| Phân loại | Số lượng | Danh sách |
|-----------|----------|-----------|
| **KEPT** | 8 | #1, 2, 4, 15, 17, 18, 19, 20 |
| **AUTOMATED** | 4 | #5 (validate API), #7 (AI OCR), #11 (AI Risk), #16 (AI Monitor) |
| **NEW** | 1 | #14 (Auto-approve 3s low-risk) |
| **REMOVED (NVA)** | 7 | #3 (OTP riêng), #6 (bank fix), #8 (OCR gate), #9 (fix rejection), #10→KEPT |

**Nhận xét:** Quy trình TO-BE giảm mạnh số bước thủ công: Compliance team chỉ xử lý ~10% hồ sơ rủi ro TB/Cao (thay vì 100% như AS-IS). Bổ sung eKYC sinh trắc học tăng bảo mật. Giảm từ 8 named gateway xuống 2, luồng đơn giản hơn đáng kể. Tỷ lệ VA/BVA/NVA ước tính sau TO-BE: **~55% / ~35% / ~10%** (so với ~45% / ~35% / ~20% AS-IS).

---

## 3. So sánh cấu trúc mô hình (Structure Comparison)

| Tiêu chí | AS-IS (file BPMN) | TO-BE (file BPMN) | Thay đổi |
|----------|-------------------|-------------------|----------|
| Số lanes | 4 (Seller, System, Compliance, Legal) | 4 (Seller, System AI, Compliance, Legal) | 0 (giữ nguyên, lane System đổi tên) |
| Số activities (tasks) | 14 (user: 8, service: 6) | 13 (user: 6, service: 7) | -1 (gộp OTP + bank fix, thêm eKYC) |
| Số named gateways (decision) | 15 | 7 | **-8** (gộp gateway, AI tự xử lý) |
| Số all gateways (incl join/split) | 15 | 7 | **-8** |
| Số timer events (SLA) | 0 | 1 (SLA 24h) | **+1** (mới) |
| Số start events | 1 | 1 | 0 |
| Số end events | 5 (Kích hoạt, Từ chối, Cảnh cáo, Tạm khóa, Khóa vĩnh viễn) | 5 (Kích hoạt, Cảnh cáo, Tạm khóa, Khóa vĩnh viễn, Từ chối do giấy tờ nghi vấn) | 0 (giữ 5, đổi end "Từ chối vĩnh viễn" → "Từ chối do giấy tờ nghi vấn") |
| Số sequence flows | 42 | 29 | **-13 (-31%)** |
| Độ phức tạp | Cao (15 decision gateways, loop resubmit) | Trung bình (7 gateways, AI tự xử lý) | **Giảm đáng kể** |

**Phân bố task theo lane:**

| Lane | AS-IS | TO-BE | Thay đổi |
|------|-------|-------|----------|
| Seller | 4 (Register, UploadDocs, FixBankInfo, FixRejection) | 2 (T_Reg, T_Upload) | -2 (bỏ FixBankInfo, FixRejection) |
| System | 6 (VerifyPhone, ValidateIdentity, OCRCheck, ScoreRisk, NotifyResult, MonitorViolations) | 7 (T_Validate, T_AI_Doc, T_KYC, T_Risk, T_AutoAppr, T_Notify, T_Monitor) | +1 (thêm eKYC, AutoAppr; bỏ VerifyPhone) |
| Compliance | 1 (ManualReview) | 1 (T_Manual) | 0 |
| Legal | 3 (Warn, Suspend, Ban) | 3 (T_Warn, T_Suspend, T_Ban) | 0 |

---

## 4. Bảng so sánh Metrics (Định lượng)

> Giá trị TO-BE là **ước tính** dựa trên giả định rằng AI auto-approve ~90% seller.

| Metric | AS-IS (ước tính) | TO-BE (expected) | Cải thiện |
|--------|------------------|------------------|-----------|
| **Cycle time trung bình (đăng ký)** | **40 giờ ≈ 5 ngày** (weighted: compliance 24-48h chiếm đa số) | **2 giờ** (ước tính) | **-95%** |
| **Cycle time fast track (low-risk)** | **~4 giờ** | **3 giây** | **-99.98%** |
| **Cycle time complex case** | **48 giờ** | **24 giờ SLA** | **-50%** |
| **Chi phí/registration** | **24,500 VND** | **12,000 VND** | **-51%** |
| **Tỷ lệ error rate** | **9%** (ước tính) | **3,8%** (ước tính) | **-58%** |
| **Seller churn 30 ngày đầu** | **18%** (ước tính) | **10%** (ước tính) | **-44%** |
| **Compliance review time** | **24-48 giờ** | **≤24 giờ (SLA)** | **-50%** |
| **Gateways (AS-IS → TO-BE)** | **15** | **7** | **-53%** |
| **Sequence flows** | **42** | **29** | **-31%** |

### 4.1. Chi tiết chi phí TO-BE (ước tính, per registration)

| Thành phần chi phí | AS-IS | TO-BE | Thay đổi |
|--------------------|-------|-------|----------|
| System infrastructure (OCR, KYC API) | 2,000 VND | 2,500 VND | +500 (nâng cấp eKYC) |
| Compliance staff time | 15,000 VND | 3,000 VND | **-12,000** (risk-based auto-approve >90%) |
| OTP SMS cost | 500 VND | 500 VND | — |
| Risk scoring engine | 1,000 VND | 1,500 VND | +500 (ML inference nâng cấp) |
| Rework (bổ sung hồ sơ) — 40%→10% | 6,000 VND | 1,500 VND | **-4,500** (guided upload + realtime validation) |
| Buffer / overhead | — | 3,000 VND | +3,000 (monitoring, QA) |
| **TỔNG CHI PHÍ** | **24,500 VND** | **12,000 VND** | **-12,500 (-51%)** |

### 4.2. Cycle time chi tiết (ước tính)

| Giai đoạn | AS-IS | TO-BE (ước tính) | Ghi chú |
|-----------|-------|------------------|---------|
| Seller đăng ký + điền thông tin | 10 phút | 5 phút | Giữ |
| Upload docs (Smart Scan) | 10 phút | 3 phút | OCR tự extract |
| Validate + KYC + OCR | 5 phút (3 API riêng) | 1 phút (pipeline gộp) | Gộp 3 bước thành 1 |
| AI Risk Scoring | 1 phút | 3 giây (auto) | Real-time |
| Compliance review | 24-48 giờ | 0 (auto, 90%) / ≤24h (10%) | **Bottleneck lớn nhất bị loại** |
| Notify + Monitoring | instant | instant | Giữ |
| **Tổng trung bình** | **~40 giờ (≈5 ngày)** | **~2 giờ** | **-95%** |

---

## 5. ROI — Ước tính đầu tư và thời gian hoàn vốn

> Toàn bộ số liệu mục này là **ước tính** cho mục đích trình bày BA (business case).

### 5.1. Đầu tư ban đầu (one-time, ước tính)

| Hạng mục | Chi phí (tỷ VND) | Ghi chú |
|----------|------------------|---------|
| AI Risk Scoring model (ML) | 1.2 | Training data, model, integration |
| AI OCR + Chống giấy tờ giả | 0.5 | OCR engine nâng cấp, liveness detection |
| Real-time eKYC sinh trắc học | 0.8 | Face matching, liveness check, API |
| Smart Scan UX redesign (Seller Centre) | 0.4 | Frontend + backend integration |
| Auto-approve engine + SLA timer | 0.3 | Rule engine, SLA monitoring |
| AI monitoring vi phạm (anomaly detection) | 0.6 | Real-time stream processing + ML |
| Testing, QA, rollout | 0.3 | UAT, phased rollout |
| **TỔNG ĐẦU TƯ BAN ĐẦU** | **4.1 tỷ VND** (~170K USD, ước tính) | |

**Chi phí vận hành hằng năm:** ~1.0 tỷ VND/năm (AI inference, OCR API, liveness API, monitoring).

### 5.2. Lợi ích hàng năm (ước tính)

**Giả định:** ~80,000 seller đăng ký mới/năm trên Lazada VN.

| Nguồn lợi ích | Công thức | Giá trị (tỷ VND/năm) |
|---------------|-----------|----------------------|
| Tiết kiệm compliance staff | 12,000 VND x 80K x 90% auto-approve | 0.864 |
| Tăng doanh thu seller mới (onboard sớm hơn) | 20h x 5,000 VND/h x 80K | 8.0 |
| Giảm error rework (40% → 10%, rework cost 15K) | 30% x 80K x 15,000 VND | 0.36 |
| Giảm seller churn (18% → 10%) | 8% x 80K x 50,000 VND LTV | 0.32 |
| **Tổng lợi ích tiềm năng** | | **9.544** |
| Lợi ích năm đầu thực thu (60%) | 9.544 x 60% | **5.73** |
| Trừ chi phí vận hành hằng năm | | -1.0 |
| **Lợi ích ròng năm đầu** | | **~4.73 tỷ VND/năm** |

### 5.3. Thời gian hoàn vốn (Payback)

| Kịch bản | Giả định | Payback |
|----------|----------|---------|
| **Cơ sở (Base)** | 80K seller/năm, đạt 60% tiềm năng | 4.1 / 4.73 ≈ **~10.4 tháng** |
| **Thận trọng (Conservative)** | 40K seller/năm (½ volume), đạt 30% tiết kiệm | 4.1 / (1.85 - 0.5) ≈ **~36 tháng** |

- **Kết luận ROI:** Kịch bản cơ sở hoàn vốn ~10,4 tháng (< 1 năm), đạt chuẩn phê duyệt đầu tư nội bộ. Kịch bản thận trọng ~3 năm — cần mở rộng volume seller để cải thiện. Lợi ích ròng 5 năm (cơ sở): (4.73 x 5) - 4.1 - (1.0 x 5) ≈ **~14.55 tỷ VND**.

---

## 6. Rủi ro của TO-BE và giải pháp giảm thiểu

| # | Rủi ro | Mức độ | Giải pháp giảm thiểu (Mitigation) |
|---|--------|--------|------------------------------------|
| 1 | **AI Risk Scoring sai sót — auto-approve nhầm seller gian lận** | Cao | (a) Ngưỡng confidence >95% cho auto-approve; (b) Shadow mode 3 tháng đầu; (c) Retrain model hàng tháng; (d) Audit ngẫu nhiên 5% auto-approved |
| 2 | **eKYC sinh trắc học bị bypass (deepfake)** | Trung bình | (a) Liveness detection 3D; (b) Challenge-response ngẫu nhiên; (c) Multi-vendor anti-spoofing; (d) Cross-check CCCD với CSDL QG |
| 3 | **Smart Scan OCR sai thông tin** | Trung bình | (a) User xác nhận OCR extract trước khi submit; (b) Fallback upload thủ công; (c) Confidence threshold 90% |
| 4 | **Seller không hoàn thành eKYC** | Thấp-Trung bình | (a) Fallback về flow thủ công cũ; (b) Hướng dẫn video step-by-step; (c) Support hotline eKYC |
| 5 | **Phụ thuộc AI vendor (downtime)** | Trung bình | (a) Multi-vendor OCR + KYC; (b) Circuit breaker fallback manual; (c) SLA uptime ≥99.5% trong hợp đồng |

---

## 7. Kết luận

1. **TO-BE giữ 8/20 hoạt động gốc**, tự động hóa 4 hoạt động (validate, OCR, risk scoring, monitoring), thêm 1 hoạt động mới (eKYC), và loại bỏ 7 hoạt động NVA (OTP riêng, bank fix, OCR gate, fix rejection loop) — đúng trọng tâm bottleneck lớn nhất: compliance review 24-48h cho mọi seller.
2. **Metrics:** Cycle time giảm 95% (≈5 ngày/40h → 2h trung bình), chi phí giảm 51% (24,5K → 12K VND), error rate giảm 58% (9% → 3,8%), seller churn giảm 44% (18% → 10%). Gateway giảm từ 15 xuống 7 (-53%), sequence flows giảm 31% (42→29).
3. **ROI:** đầu tư ban đầu ~4.1 tỷ VND (ước tính), payback ~10,4 tháng (cơ sở) / ~36 tháng (thận trọng). Lợi ích ròng 5 năm ~14,55 tỷ VND.
4. **Hành động tiếp theo:** (a) Phê duyệt Phase 1 (Smart Scan + AI OCR ~0.9 tỷ); (b) Chuẩn bị training data cho AI risk model; (c) Pilot eKYC sinh trắc học với 10% seller mới; (d) Xác thực lại số liệu chi phí/registration với đội Seller Operations.

---

## 8. Tham chiếu

- AS-IS BPMN: `processes/01-seller-management.bpmn`
- TO-BE BPMN: `processes-to-be/01-seller-management.bpmn`

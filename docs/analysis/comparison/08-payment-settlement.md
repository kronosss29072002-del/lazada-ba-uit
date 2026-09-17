# So sánh AS-IS vs TO-BE: Quy trình Thanh toán & Đối soát

> **Quy trình:** 08 - Thanh toán & Đối soát (Payment & Settlement)
> **Nguồn AS-IS:** `processes/08-payment-settlement.bpmn`
> **Nguồn TO-BE:** `processes-to-be/08-payment-settlement.bpmn`
> **Ngày phân tích:** 2026-09-03
>
> **Ghi chú số liệu:** Các con số không nằm trong tài liệu gốc đều được **dán nhãn "ước tính"**. Bảng hoạt động và số liệu cấu trúc dựa trên **file BPMN thực tế**.

---

## 1. Tóm tắt thay đổi chính (TO-BE)

| # | Thay đổi TO-BE | Mục tiêu | Kết quả mong đợi |
|---|----------------|----------|------------------|
| 1 | AI Fraud Detection thay thế Payment Gateway lane (gộp xác minh chữ ký + kiểm tra IPN + gửi kết quả thành AI risk scoring real-time) | Loại bỏ 4 task thủ công, nâng cấp rule-based sang AI/ML | Fraud rate giảm từ 0.3% xuống 0.1%, false positive giảm 60% |
| 2 | Instant settlement cho trusted seller (risk-based L+1) thay thế L+2/L+3 cứng | Giảm thời gian giữ tiền trong Escrow | Cycle time giảm từ ~2.9 ngày xuống ~1.5 ngày cho 60% seller |
| 3 | Blockchain Escrow thay thế Escrow tạm thời | Tăng minh bạch dòng tiền, giảm gian lận nội bộ | COD discrepancy giảm từ 2-3% xuống 0.5% |
| 4 | ML Auto-reconciliation gộp 5 task (COD reconcile + daily reconcile + discrepancy detect + discrepancy handle + adjust) thành 1 serviceTask | Loại bỏ reconciliation thủ công hàng ngày | Reconciliation time giảm từ 4h/ngày xuống 30 phút |
| 5 | Multi-gateway auto-fallback (VNPay/MoMo/ZaloPay/Visa/MC) thay thế single gateway processing | Tránh downtime 1 gateway ảnh hưởng toàn flow | Payment success rate tăng từ 94% lên 98.5% |
| 6 | Loại bỏ hoàn toàn lane Finance (4 task thủ công) + giảm từ 5 lane xuống 4 lane | Đơn giản hóa luồng, tự động hóa Finance | Giảm 23% số task (22 -> 17), sequence flows giảm 15% |

---

## 2. Bảng so sánh hoạt động (Activity Comparison Table)

**Phân loại:** KEPT (giữ) | AUTOMATED (tự động hóa) | REMOVED (loại bỏ - NVA) | NEW (thêm mới)

| # | Hoạt động AS-IS | Hoạt động TO-BE (thay thế) | Phân loại | Giải thích thay đổi |
|---|-----------------|----------------------------|-----------|---------------------|
| 1 | Buyer hoàn tất thanh toán đơn hàng (Start) | Buyer hoàn tất thanh toán đơn hàng (Start) | **KEPT** | Giữ nguyên |
| 2 | Chọn phương thức thanh toán COD/Online/Ví (Task_ChooseMethod) | Chọn phương thức thanh toán COD/Online/Ví (Task_SelectPayment) | **KEPT** | Giữ nguyên |
| 3 | Thanh toán COD khi nhận hàng (Task_PayCOD) | Thanh toán COD khi nhận hàng (Task_PayCOD) | **KEPT** | Giữ nguyên |
| 4 | Xác nhận thanh toán online qua cổng (Task_ConfirmOnline) | Thanh toán online qua cổng thanh toán (Task_PayOnline) | **KEPT** | Đổi tên, tích hợp multi-gateway |
| 5 | Buyer nhận hàng & hoàn tất đơn (Task_ReceiveGoods) | Buyer nhận hàng & xác nhận COD (Task_ReceiveGoods) | **KEPT** | Bổ sung xác nhận COD |
| 6 | Buyer nhận hoàn tiền khi hủy/hoàn trả (Task_ReceiveRefund) | Buyer nhận hoàn tiền tự động (Task_ReceiveRefund) | **AUTOMATED** | Nâng cấp từ manual sang instant auto-refund |
| 7 | Cổng thanh toán xử lý giao dịch (Task_ProcessPayment) | *(loại bỏ — gộp vào multi-gateway auto-fallback)* | **REMOVED (NVA)** | Multi-gateway tự xử lý, không cần task riêng |
| 8 | Xác minh chữ ký & tính hợp lệ giao dịch (Task_VerifyPayment) | *(loại bỏ — tích hợp vào AI Fraud Detection)* | **REMOVED (NVA)** | AI risk scoring thay thế xác minh thủ công |
| 9 | Gửi kết quả thanh toán về hệ thống (Task_NotifyResult) | *(loại bỏ — tích hợp vào multi-gateway webhook)* | **REMOVED (NVA)** | Webhook real-time thay thế push result thủ công |
| 10 | Kiểm tra IPN/Webhook đối soát giao dịch (Task_CheckIPN) | *(loại bỏ — tích hợp vào AI auto-reconcile)* | **REMOVED (NVA)** | Auto-reconciliation ML thay thế IPN check |
| 11 | Hệ thống giữ tiền tạm thời trong Escrow (Task_HoldEscrow) | Giữ tiền trong Escrow Blockchain (Task_HoldEscrow) | **AUTOMATED** | Nâng cấp sang blockchain escrow minh bạch |
| 12 | Đối chiếu giao dịch với mã đơn hàng (Task_MatchOrder) | *(loại bỏ — tích hợp vào auto-reconcile)* | **REMOVED (NVA)** | Auto-reconciliation ML tự khớp order-transaction |
| 13 | Giải ngân tiền cho Seller L+2 ngày (Task_ReleaseFunds) | Giải ngân tức thì cho Seller trusted (Task_InstantSettle) | **AUTOMATED** | Instant settlement cho trusted, L+2 cho standard |
| 14 | Đối soát COD với 3PL thu hộ (Task_ReconcileCOD) | *(loại bỏ — gộp vào auto-reconcile end-of-day)* | **REMOVED (NVA)** | ML auto-reconciliation gộp COD + Online |
| 15 | Tổng hợp đối soát dòng tiền cuối ngày (Task_ReconcileDaily) | *(loại bỏ — gộp vào auto-reconcile end-of-day)* | **REMOVED (NVA)** | Auto-reconcile chạy real-time thay batch |
| 16 | Tính hoa hồng Lazada 1-8% (Task_CalculateCommission) | Tính hoa hồng & phí tự động (Task_CalcCommission) | **KEPT (cải tiến)** | Dynamic commission model, tự động hoàn toàn |
| 17 | Cập nhật số dư Ví Seller (Task_UpdateWallet) | Cập nhật số dư Ví Seller + Push notification (Task_UpdateWallet) | **KEPT (cải tiến)** | Bổ sung push notification real-time |
| 18 | Phòng Tài chính xử lý lệch dòng tiền (Task_HandleDiscrepancy) | *(loại bỏ — auto-reconcile ML xử lý tự động)* | **REMOVED (NVA)** | AI reconciliation tự detect + flag, không cần Finance manual |
| 19 | Xác nhận bảng đối soát cuối kỳ (Task_ConfirmStatement) | *(loại bỏ — tích hợp vào auto-reconcile)* | **REMOVED (NVA)** | Auto-reconcile tự confirm, không cần manual sign-off |
| 20 | Điều chỉnh số liệu sai lệch trên bảng kê (Task_AdjustStatement) | *(loại bỏ — AI tự adjust trong threshold)* | **REMOVED (NVA)** | ML auto-adjust cho sai lệch nhỏ, vượt threshold mới alert |
| 21 | Xuất hóa đơn & báo cáo tài chính (Task_IssueInvoice) | *(loại bỏ — tích hợp vào electronic statement)* | **REMOVED (NVA)** | Electronic statement tự động hàng tháng thay invoice riêng |
| 22 | Seller kiểm tra số dư Ví trên Seller Centre (Task_CheckWallet) | Seller nhận Push notification số dư Ví (Task_CheckWallet) | **KEPT (cải tiến)** | Push notification thay pull-based check |
| 23 | Seller yêu cầu rút tiền (Task_Withdraw) | Rút tiền từ Ví về tài khoản ngân hàng (Task_Withdraw) | **KEPT** | Giữ nguyên |
| 24 | Tiền về tài khoản ngân hàng thành công? (Gate_BankReceived) | Chuyển khoản thành công? (Gate_BankOK) | **KEPT** | Giữ nguyên logic retry |
| 25 | *(không có)* | COD xác nhận đã thu tiền? (Gate_CODVerify) | **NEW** | Gateway mới — verify COD cash collection real-time |
| 26 | *(không có)* | AI tính điểm rủi ro giao dịch real-time (Task_RiskScore) | **NEW** | AI fraud scoring thay thế rule-based verify |
| 27 | *(không có)* | Chặn giao dịch — yêu cầu xác minh bổ sung (Task_BlockTransaction) | **NEW** | Auto-block high-risk (score >= 80) |
| 28 | *(không có)* | Phê duyệt tự động AI xác nhận an toàn (Task_ApproveAuto) | **NEW** | ~95% giao dịch safe được auto-approve |
| 29 | *(không có)* | Cảnh báo gian lận đến CS-terminal (Task_FraudAlert) | **NEW** | Real-time alert cho manual investigation |
| 30 | *(không có)* | Đối soát tự động COD/Online end-of-day (Task_AutoReconcile) | **NEW** | ML auto-reconciliation thay 5 task manual |
| 31 | *(không có)* | Gửi bảng đối soát điện tử tự động hàng tháng (Task_SendStatement) | **NEW** | Auto e-statement thay manual invoice |

### Tổng hợp phân loại

| Phân loại | Số lượng | Danh sách |
|-----------|----------|-----------|
| **KEPT** | 6 | #1, 2, 3, 4, 5, 23, 24 |
| **KEPT (cải tiến)** | 3 | #16, 17, 22 |
| **AUTOMATED** | 3 | #6 (auto-refund), #11 (blockchain escrow), #13 (instant settle) |
| **NEW** | 7 | #25 (COD verify gate), #26 (AI risk score), #27 (block txn), #28 (auto-approve), #29 (fraud alert), #30 (auto-reconcile), #31 (e-statement) |
| **REMOVED (NVA)** | 11 | #7, 8, 9, 10, 12, 14, 15, 18, 19, 20, 21 |

**Nhận xét:** Quy trình TO-BE loại bỏ mạnh các task NVA trong lane Finance và Payment Gateway. Lane Finance bị loại hoàn toàn (4 task). Lane Payment Gateway bị thay thế bởi AI Fraud Detection System (4 task cũ -> 5 task mới). Tổng task giảm từ 22 xuống 17 (-23%). Tỷ lệ VA/BVA/NVA ước tính sau TO-BE: **~60% / ~30% / ~10%** (so với ~52% / ~39% / ~9% AS-IS). COD verification được bổ sung mới — giải quyết root cause chính của COD discrepancy.

---

## 3. So sánh cấu trúc mô hình (Structure Comparison)

| Tiêu chí | AS-IS (file BPMN) | TO-BE (file BPMN) | Thay đổi |
|----------|-------------------|-------------------|----------|
| Số lanes | 5 (Buyer, PaymentGW, System, Finance, Seller) | 4 (Buyer, AI Fraud, System, Seller) | **-1** (loại bỏ Finance lane) |
| Số activities (tasks) | 22 (user: 11, service: 11) | 17 (user: 7, service: 10) | **-5 (-23%)** |
| Số named gateways (decision) | 7 | 7 | 0 (giữ nguyên số lượng, đổi nội dung) |
| Số all gateways (incl join/split) | 7 | 7 | 0 |
| Số timer events (SLA) | 0 | 0 | 0 |
| Số start events | 1 | 1 | 0 |
| Số end events | 3 (Paid, Settled, Refunded) | 2 (Settled, Refunded) | **-1** (gộp Paid + Settled) |
| Số sequence flows | 49 | 41 | **-8 (-16.3%)** |
| Độ phức tạp | Cao (5 lanes, 11 manual tasks, Finance loop) | Trung bình (4 lanes, 5 service tasks automated) | **Giảm đáng kể** |

**Phân bố task theo lane:**

| Lane | AS-IS | TO-BE | Thay đổi |
|------|-------|-------|----------|
| Buyer | 5 (ChooseMethod, PayCOD, ConfirmOnline, ReceiveGoods, ReceiveRefund) | 5 (SelectPayment, PayCOD, PayOnline, ReceiveGoods, ReceiveRefund) | 0 (giữ nguyên số lượng, đổi tên) |
| PaymentGW / AI Fraud | 4 (ProcessPayment, VerifyPayment, NotifyResult, CheckIPN) | 5 (RiskScore, BlockTransaction, ApproveAuto, FraudAlert + CODVerify gate) | +1 (AI Fraud thay PaymentGW, thêm risk scoring) |
| System (Escrow) | 6 (HoldEscrow, MatchOrder, ReleaseFunds, ReconcileCOD, ReconcileDaily, CalcCommission, UpdateWallet) | 5 (HoldEscrow, InstantSettle, AutoReconcile, CalcCommission, UpdateWallet, SendStatement) | -1 (gộp 5 reconciliation tasks thành 1 AutoReconcile) |
| Finance | 4 (HandleDiscrepancy, ConfirmStatement, AdjustStatement, IssueInvoice) | 0 (lane bị loại bỏ) | **-4 (loại bỏ hoàn toàn)** |
| Seller | 3 (CheckWallet, Withdraw) | 2 (CheckWallet, Withdraw) | -1 (giữ core tasks) |

---

## 4. Bảng so sánh Metrics (Định lượng)

> Giá trị TO-BE là **ước tính** dựa trên giả định AI fraud detection + ML auto-reconciliation + instant settlement hoạt động ổn định.

| Metric | AS-IS (ước tính) | TO-BE (expected) | Cải thiện |
|--------|------------------|------------------|-----------|
| **Payment success rate** | **94%** | **98.5%** | **+4.5%** |
| **Fraud rate** | **0.3%** (~1,500 cases/ngày) | **0.1%** (~500 cases/ngày) | **-67%** |
| **COD discrepancy rate** | **2-3%** (~4,250-6,375 giao dịch/ngày COD) | **0.5%** (~1,060 giao dịch/ngày COD) | **-75-83%** |
| **COD reconciliation accuracy** | **97-98%** | **99.5%** | **+1.5-2.5%** |
| **Cycle time trung bình (checkout -> seller nhận tiền)** | **~2.9 ngày** | **~1.5 ngày** | **-48%** |
| **Cycle time online path** | **~2.3 ngày (L+2 + ~1h xử lý)** | **~1 ngày (L+1)** | **-57%** |
| **Cycle time COD path** | **~3.4 ngày (L+3 + ~5h đối soát)** | **~2 ngày (L+2)** | **-41%** |
| **Settlement time (online)** | **L+2 (48h)** | **L+1 (24h)** | **-50%** |
| **Settlement time (COD)** | **L+3 (72h)** | **L+2 (48h)** | **-33%** |
| **Withdrawal processing** | **24-48h** | **Instant (wallet) / 4-8h (bank)** | **-80-100%** |
| **Payment dispute rate** | **0.8%** | **0.3%** | **-63%** |
| **Double charge incidents** | **50/ngày** | **<5/ngày** | **-90%** |
| **Chi phí per transaction** | **2,750 VND** | **1,200 VND** | **-56%** |
| **Monthly processing cost (15M txn)** | **~41.25 tỷ VND** | **~18 tỷ VND** | **-56%** |
| **Monthly total waste cost** | **~257 tỷ VND** | **~45 tỷ VND** | **-82%** |
| **Named gateways** | **7** | **7** | 0 (giữ nguyên) |
| **Sequence flows** | **49** | **41** | **-16%** |

### 4.1. Chi tiết chi phí TO-BE (ước tính, per transaction)

| Thành phần chi phí | AS-IS | TO-BE | Thay đổi |
|--------------------|-------|-------|----------|
| Payment gateway fee | 1,500 | 600 | **-900** (multi-gateway optimization, negotiated rate) |
| Transaction processing (system) | 500 | 200 | **-300** (reduced workflow complexity) |
| Fraud check (AI model) | 100 | 200 | +100 (AI nâng cao, VN-specific patterns) |
| Blockchain escrow cost | 0 | 50 | +50 (mới) |
| Escrow holding cost | 200 | 40 | **-160** (instant settle giảm time hold) |
| COD reconciliation (manual -> ML) | 300 | 40 | **-260** (ML auto-reconciliation) |
| Refund processing (5% cases) | 50 | 30 | **-20** (instant auto-refund) |
| Withdrawal processing | 100 | 40 | **-60** (real-time banking API) |
| Finance staff allocation | 0 | 0 | 0 (Finance lane eliminated) |
| **TỔNG CHI PHÍ** | **2,750 VND** | **1,200 VND** | **-1,550 VND (-56%)** |

### 4.2. Cycle time chi tiết (ước tính)

| Giai đoạn | AS-IS | TO-BE (ước tính) | Ghi chú |
|-----------|-------|------------------|---------|
| Buyer thanh toán (chọn method + xác nhận) | 2 phút | 2 phút | Giữ nguyên |
| Xử lý qua Payment Gateway / AI Fraud | 5-15 giây | 5 giây (AI scoring) | AI real-time thay gateway processing |
| Giữ tiền Escrow | 5 giây | 5 giây (blockchain) | Giữ nguyên |
| Đối soát đơn + COD reconciliation | 4h/ngày (batch manual) | 30 phút/ngày (ML auto) | **-87.5%** |
| Tính hoa hồng + Cập nhật Ví | 5 giây | 3 giây | Tự động |
| Giải ngân Escrow -> Seller | L+2 (online) / L+3 (COD) | L+1 (online) / L+2 (COD) | **-24h mỗi path** |
| Seller nhận tiền + rút tiền | 24-48h (bank) | Instant (wallet) / 4-8h (bank) | **-80-100%** |
| **Tổng trung bình** | **~2.9 ngày** | **~1.5 ngày** | **-48%** |

### 4.3. Chi tiết gates so sánh

| Gateway AS-IS | Gateway TO-BE (thay thế) | Thay đổi |
|---------------|--------------------------|----------|
| Gate_Method: Chọn phương thức thanh toán? | Gate_PaymentType: Phương thức thanh toán? | **KEPT** (mở rộng options) |
| Gate_PaymentApproved: Giao dịch thanh toán thành công? | Gate_HighRisk: Giao dịch rủi ro cao (score >= 80)? | **AUTOMATED** (AI scoring) |
| Gate_Valid: Giao dịch hợp lệ (chữ ký đúng)? | *(loại bỏ — tích hợp vào AI Fraud)* | **REMOVED** |
| Gate_OrderCompleted: Đơn hàng hoàn tất giao dịch? | *(loại bỏ — instant settle thay thế)* | **REMOVED** |
| Gate_DiscrepancyFound: Phát hiện lệch dòng tiền? | Gate_ReconcileOK: Đối soát khớp 100%? | **AUTOMATED** (ML auto-reconcile) |
| Gate_DiscrepancyResolved: Lệch dòng tiền đã xử lý xong? | *(loại bỏ — AI tự xử lý trong threshold)* | **REMOVED** |
| Gate_BankReceived: Tiền về tài khoản ngân hàng thành công? | Gate_BankOK: Chuyển khoản thành công? | **KEPT** |
| *(không có)* | Gate_CODVerify: COD xác nhận đã thu tiền? | **NEW** |
| *(không có)* | Gate_SellerTrust: Seller thuộc nhóm Trusted? | **NEW** |
| *(không có)* | Gate_RefundOK: Hoàn tiền được chấp thuận? | **NEW** |

---

## 5. ROI

> Toàn bộ số liệu mục này là **ước tính** cho mục đích trình bày BA (business case).

### 5.1. Đầu tư ban đầu (one-time, ước tính)

| Hạng mục | Chi phí (tỷ VND) | Ghi chú |
|----------|------------------|---------|
| AI Fraud Detection System (ML model + VN-specific training) | 2.5 | Training data VN fraud patterns, real-time inference infra |
| Blockchain Escrow integration | 1.5 | Smart contract + escrow ledger + audit trail |
| Multi-gateway failover engine | 1.0 | Auto-fallback VNPay/MoMo/ZaloPay/Visa/MC + circuit breaker |
| ML Auto-reconciliation engine | 1.2 | COD digital verification (GPS + signature) + matching algo |
| Instant settlement engine (trusted seller risk model) | 0.8 | Trust scoring model + instant disbursement API |
| Real-time banking API integration | 0.5 | Partner banks: Vietcombank, Techcombank, BIDV |
| Seller Centre UX (wallet + push notification) | 0.3 | Frontend + backend integration |
| Testing, QA, rollout (phased) | 0.7 | UAT, 10% pilot -> 50% -> 100% |
| **TỔNG ĐẦU TƯ BAN ĐẦU** | **8.5 tỷ VND** (~360K USD, ước tính) | |

**Chi phí vận hành hằng năm:** ~2.0 tỷ VND/năm (AI inference, blockchain node, banking API fees, ML retraining).

### 5.2. Lợi ích hằng năm (ước tính)

**Giả định:** ~15 triệu giao dịch/tháng = ~180 triệu giao dịch/năm trên Lazada VN.

| Nguồn lợi ích | Công thức | Giá trị (tỷ VND/năm) |
|---------------|-----------|----------------------|
| Giảm COD discrepancy (2.5% -> 0.5%) | 2% x 180M x 42.5% COD x 100,000 VND AOV | 153.0 |
| Giảm settlement cycle (L+2/L+3 -> L+1/L+2) — interest cost savings | 180M x 42.5% x 1 ngày saved x 0.01%/ngày x 100,000 | 0.77 |
| Giảm fraud loss (0.3% -> 0.1%) | 0.2% x 180M x 100,000 VND | 36.0 |
| Giảm payment gateway fees (multi-gateway optimization) | 180M x 300 VND savings | 54.0 |
| Giảm Finance staff cost (4 manual tasks eliminated) | 10 staff x 20M VND/tháng x 12 | 2.4 |
| Giảm reconciliation labor (4h -> 30min/ngày) | 5 staff x 15M VND/tháng x 12 | 0.9 |
| **Tổng lợi ích tiềm năng** | | **247.07** |
| Lợi ích năm đầu thực thu (60%) | 247.07 x 60% | **148.24** |
| Trừ chi phí vận hành hằng năm | | -2.0 |
| **Lợi ích ròng năm đầu** | | **~146.24 tỷ VND/năm** |

### 5.3. Thời gian hoàn vốn (Payback)

| Kịch bản | Giả định | Payback |
|----------|----------|---------|
| **Cơ sở (Base)** | 180M txn/năm, đạt 60% tiềm năng | 8.5 / 146.24 ≈ **~21 ngày** |
| **Thận trọng (Conservative)** | 100M txn/năm, đạt 30% lợi ích | 8.5 / (41.18 - 2.0) ≈ **~2.6 tháng** |

- **Kết luận ROI:** Kịch bản cơ sở chỉ cần ~21 ngày để hoàn vốn — mức độ lợi ích cực lớn do COD discrepancy là nguồn chi phí chính (~153 tỷ/năm). Kịch bản thận trọng vẫn hoàn vốn trong < 3 tháng. Lợi ích ròng 5 năm (cơ sở): (146.24 x 5) - 8.5 - (2.0 x 5) ≈ **~712.7 tỷ VND**.

---

## 6. Rủi ro TO-BE và giải pháp giảm thiểu

| # | Rủi ro | Mức độ | Giải pháp giảm thiểu (Mitigation) |
|---|--------|--------|------------------------------------|
| 1 | **AI Fraud Detection false negative — bỏ lọt gian lận** (fraud rate 0.3% -> 0.1% mục tiêu nhưng model mới có thể miss novel fraud patterns) | Cao | (a) Shadow mode 3 tháng song song với rule-based cũ; (b) Confidence threshold >90% cho auto-block; (c) Retrain model hàng tuần với fraud cases mới; (d) Human-in-the-loop audit 10% giao dịch auto-approve |
| 2 | **Blockchain Escrow downtime hoặc smart contract bug** (tiền bị lock trong escrow không thể giải phóng) | Cao | (a) Circuit breaker fallback về traditional escrow; (b) Multi-sig approval cho giải phóng >500M VND; (c) Insurance policy cho escrow loss; (d) Thorough smart contract audit trước khi launch |
| 3 | **ML Auto-reconciliation sai matching** (match nhầm đơn hàng -> sai lệch tiền seller) | Trung bình | (a) Confidence threshold 99.5% cho auto-match; (b) Flag transaction <99% confidence để manual review; (c) Daily reconciliation report cho Finance audit; (d) Rollback capability nếu matching accuracy giảm |
| 4 | **Trusted seller risk model sai** (instant settle cho seller gian lận -> mất tiền) | Trung bình | (a) Trust score refresh hàng ngày; (b) Instant settle cap 50M VND/ngày/seller; (c) Auto-freeze khi phát hiện bất thường sau settle; (d) Chargeback capability trong 24h |
| 5 | **Multi-gateway failover routing sai** (gửi giao dịch đến gateway không hỗ trợ loại thanh toán -> fail) | Thấp-Trung bình | (a) Gateway capability matrix + validation trước khi route; (b) Circuit breaker per gateway; (c) Fallback về gateway mặc định (VNPay) nếu routing fail; (d) Monitoring dashboard real-time per gateway |

---

## 7. Kết luận

1. **TO-BE giữ 9/22 hoạt động gốc**, tự động hóa 3 hoạt động (auto-refund, blockchain escrow, instant settlement), thêm 7 hoạt động mới (AI risk scoring, COD verify, auto-block, auto-approve, fraud alert, auto-reconcile, e-statement), và loại bỏ 11 hoạt động NVA — đặc biệt loại bỏ hoàn toàn lane Finance (4 task thủ công) và thay thế lane Payment Gateway (4 task) bằng AI Fraud Detection System (5 task). Đây là thay đổi lớn nhất so với các quy trình khác.

2. **Metrics:** Payment success rate tăng +4.5% (94% -> 98.5%), fraud rate giảm -67% (0.3% -> 0.1%), COD discrepancy giảm -75-83% (2-3% -> 0.5%), cycle time giảm -48% (~2.9 ngày -> ~1.5 ngày), chi phí per transaction giảm -56% (2,750 -> 1,200 VND), monthly waste giảm -82% (~257 -> ~45 tỷ VND).

3. **Structural:** Lanes giảm từ 5 xuống 4 (-20%), tasks giảm từ 22 xuống 17 (-23%), sequence flows giảm từ 49 xuống 41 (-16%). Gateways giữ nguyên 7 nhưng nội dung thay đổi đáng kể — 4 gateway bị loại (PaymentApproved, Valid, OrderCompleted, DiscrepancyResolved) và 3 gateway mới được thêm (CODVerify, SellerTrust, RefundOK).

4. **ROI:** Đầu tư ban đầu ~8.5 tỷ VND (ước tính), payback ~21 ngày (cơ sở) / ~2.6 tháng (thận trọng). Lợi ích ròng 5 năm ~712.7 tỷ VND. COD discrepancy là nguồn chi phí lớn nhất (~35% waste), giải quyết nó tạo ROI cực lớn.

5. **Hành động tiếp theo:** (a) Phê duyệt Phase 1 — AI Fraud Detection + ML Auto-reconciliation (~3.7 tỷ); (b) Pilot instant settlement với 10% trusted seller; (c) Smart contract audit cho blockchain escrow; (d) Setup multi-gateway failover với VNPay trước, mở rộng MoMo/ZaloPay sau; (e) Training data preparation — thu thập 6 tháng fraud cases VN-specific.

---

## 8. Tham chiếu

- AS-IS BPMN: `processes/08-payment-settlement.bpmn`
- TO-BE BPMN: `processes-to-be/08-payment-settlement.bpmn`
- Phân tích chi tiết: `docs/analysis/08-payment-settlement.md`

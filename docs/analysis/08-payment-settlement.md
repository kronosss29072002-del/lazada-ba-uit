# 3.8. Quy trình Thanh toán & Đối soát (Payment & Settlement)

## 3.8.1. Mô tả quy trình

**Phạm vi:** Bắt đầu từ khi Buyer thực hiện thanh toán tại Checkout → Chọn phương thức (COD/Online/Ví) → Thanh toán COD hoặc xác nhận thanh toán online qua cổng → Payment Gateway xử lý giao dịch và xác minh chữ ký → Hệ thống giữ tiền tạm thời trong Escrow → Đối chiếu giao dịch với mã đơn hàng → Đối soát COD với 3PL thu hộ → Tổng hợp đối soát dòng tiền cuối ngày → Tính hoa hồng Lazada → Cập nhật số dư Ví Seller → Xử lý lệch dòng tiền (nếu có) → Xác nhận bảng đối soát cuối kỳ → Xuất hóa đơn & báo cáo tài chính → Seller rút tiền về tài khoản ngân hàng. Đây là quy trình cốt lõi của dòng tiền trên sàn, ảnh hưởng trực tiếp đến trải nghiệm Buyer và doanh thu Seller.

**Các tác nhân tham gia:**
- **Buyer:** Người mua — chọn phương thức thanh toán, hoàn tất checkout
- **Payment Gateway:** Cổng thanh toán (VNPay, MoMo, ZaloPay, Visa/MC) — xác thực, xử lý giao dịch, hoàn tiền
- **Lazada System (Escrow):** Hệ thống ký quỹ tự động — giữ tiền tạm ứng, đối soát, tính hoa hồng, quản lý ledger
- **Finance:** Bộ phận tài chính — giám sát đối soát, xử lý chênh lệch, phê duyệt giải ngân đặc biệt
- **Seller:** Người bán — nhận giải ngân, rút tiền, kiểm tra sao kê

**Kết quả có thể xảy ra:**
- Thanh toán thành công — tiền về Escrow, đơn hàng được xử lý
- Thanh toán thất bại — OTP sai, hết hạn, insufficient funds, gateway timeout
- COD thu hộ — shipper thu tiền mặt, đối soát L+3
- Refund/giải ngân — hoàn tiền cho Buyer hoặc giải ngân cho Seller
- Phát hiện gian lận — freeze giao dịch, điều tra, khiếu nại

### SiPOC

| SiPOC | Chi tiết |
|-------|----------|
| **Supplier** | Buyer (thanh toán COD/Online/Wallet), Payment Gateway (xác thực + xử lý), 3PL/Shipper (thu COD), Ngân hàng (chuyển khoản) |
| **Input** | Phương thức thanh toán, thông tin tài khoản/giấy tờ, mã OTP, đơn hàng cần thanh toán, yêu cầu rút tiền |
| **Process** | Checkout → Chọn phương thức → Thanh toán COD / Xác nhận online → Gateway xử lý + xác minh → Giữ Escrow → Đối chiếu đơn → Đối soát COD → Tổng hợp dòng tiền → Tính hoa hồng → Cập nhật Ví → Xử lý lệch → Xác nhận đối soát → Xuất hóa đơn → Rút tiền → Bank transfer |
| **Output** | Thanh toán thành công/thất bại, Tiền giải ngân cho Seller, Hóa đơn, COD reconciliation report, Báo cáo gian lận |
| **Customer** | Buyer (thanh toán an toàn, nhanh chóng), Seller (nhận tiền đúng hạn, sao kê minh bạch) |

## 3.8.2. Mô hình BPMN

*(File: `processes/08-payment-settlement.bpmn`)*

**Thống kê mô hình:**
- Số lanes: 5 (Buyer, Payment Gateway (VNPay/MoMo/ZaloPay), Lazada System (Escrow), Finance, Seller)
- Số activities: 22 (11 userTask + 11 serviceTask)
- Số gateways: 16 (14 XOR + 2 AND)
- End events: 3 (Seller đã nhận tiền thanh toán, Đối soát đã hoàn tất, Đã hoàn tiền về Buyer)
- Độ phức tạp: High (quy trình tài chính phức tạp nhất, nhiều exception flow)

## 3.8.3. Phân tích định tính

### A. Value-Added Analysis

| STT | Hoạt động (tên từ BPMN) | VA | BVA | NVA | Giải thích | Đề xuất TO-BE |
|-----|--------------------------|----|-----|-----|------------|---------------|
| 1 | Chọn phương thức thanh toán (COD/Online/Ví) | ✓ |  |  | Buyer quyết định cách trả — core choice | Gợi ý phương thức ưu đãi |
| 2 | Thanh toán COD khi nhận hàng | ✓ |  |  | COD = ~40-45% giao dịch (giảm dần từ ~55-60% năm 2022) — thu hộ critical flow | Digital POD + xác thực cash |
| 3 | Xác nhận thanh toán online qua cổng |  | ✓ |  | Xác thực bảo mật bắt buộc | Nâng facial recognition + SCA |
| 4 | Buyer nhận hàng & hoàn tất đơn | ✓ |  |  | Hoàn tất chuỗi mua — giá trị | Giữ nguyên |
| 5 | Buyer nhận hoàn tiền khi hủy/hoàn trả | ✓ |  |  | Hoàn tiền đúng hạn cho Buyer | Instant refund qua wallet |
| 6 | Cổng thanh toán xử lý giao dịch | ✓ |  |  | Heartbeat — tiền thực sự được xử lý | Multi-gateway fallback |
| 7 | Xác minh chữ ký & tính hợp lệ giao dịch |  | ✓ |  | Bảo mật bắt buộc | Giữ nguyên |
| 8 | Gửi kết quả thanh toán về hệ thống | ✓ |  |  | Cập nhật trạng thái đơn | Giữ nguyên |
| 9 | Kiểm tra IPN/Webhook đối soát giao dịch |  | ✓ |  | Đối soát tự động — kiểm soát | Auto-reconcile real-time |
| 10 | Hệ thống giữ tiền tạm thời trong Escrow |  | ✓ |  | Ký quỹ bảo vệ 2 bên | Blockchain escrow minh bạch |
| 11 | Đối chiếu giao dịch với mã đơn hàng | ✓ |  |  | Core reconciliation — tiền khớp đơn | Auto-reconciliation ML |
| 12 | Giải ngân tiền cho Seller (L+2 ngày) | ✓ |  |  | Seller nhận tiền — giá trị cuối cùng | Instant settlement cho trusted |
| 13 | Đối soát COD với 3PL thu hộ |  | ✓ |  | Matching cash từ shipper — 97-98% accuracy | ML auto-matching |
| 14 | Tổng hợp đối soát dòng tiền cuối ngày | ✓ |  |  | Báo cáo dòng tiền chính xác | Auto tổng hợp real-time |
| 15 | Tính hoa hồng Lazada (1-8% theo danh mục) | ✓ |  |  | Doanh thu cốt lõi của sàn | Dynamic commission model |
| 16 | Cập nhật số dư Ví Seller | ✓ |  |  | Seller thấy tiền chính xác | Real-time wallet sync |
| 17 | Phòng Tài chính xử lý lệch dòng tiền |  |  | ✓ | NVA — xử lý chênh lệch thủ công từng case | Auto-triage + AI detect root cause |
| 18 | Xác nhận bảng đối soát cuối kỳ | ✓ |  |  | Kiểm soát tài chính cuối kỳ — minh bạch | Dashboard số liệu thống nhất |
| 19 | Điều chỉnh số liệu sai lệch trên bảng kê |  |  | ✓ | NVA — sửa sai thủ công | Auto-adjust + audit trail |
| 20 | Xuất hóa đơn & báo cáo tài chính |  | ✓ |  | Bắt buộc theo quy định pháp luật | Auto-e-invoice integration |
| 21 | Seller kiểm tra số dư Ví trên Seller Centre | ✓ |  |  | Minh bạch dòng tiền cho Seller | Real-time dashboard |
| 22 | Seller yêu cầu rút tiền về tài khoản ngân hàng | ✓ |  |  | Seller cần nhận tiền | Ví Lazada instant + bank API |

**Tỷ lệ VA/BVA/NVA:**
- VA: 14/22 (63%)
- BVA: 6/22 (27%)
- NVA: 2/22 (9%)

→ **Nhận xét:** VA cao (64%) — quy trình thanh toán tạo giá trị trực tiếp qua mỗi giao dịch. BVA 27% là cần thiết cho bảo mật và compliance. NVA thấp (9%) nhưng chi phí xử lý chênh lệch COD rất lớn (~90-135 tỷ VND/tháng).

### B. Waste Analysis

| STT | Hoạt động | Move | Hold | Overdo | Mô tả | Thời gian chờ | Giải pháp |
|-----|-----------|------|------|--------|-------|---------------|-----------|
| 1 | Phòng Tài chính xử lý lệch dòng tiền | ✓ | | | Finance phải kiểm tra manual từng khoản chênh lệch | 4-24h/case | Auto-reconciliation ML |
| 2 | Đối soát COD với 3PL thu hộ | ✓ | | | Matching thủ công giữa cash từ shipper và ledger hệ thống | 2-4h/ngày team | Auto-matching algorithm |
| 3 | Giải ngân tiền cho Seller (L+2 ngày) | | ✓ | | Seller chờ L+2 (online) / L+3 (COD) để nhận tiền | 2-3 ngày | Instant settlement cho trusted |
| 4 | Điều chỉnh số liệu sai lệch trên bảng kê | ✓ | | | Sửa sai thủ công sau đối soát cuối kỳ | 1-2 ngày | Auto-adjust + audit trail |
| 5 | Seller yêu cầu rút tiền về tài khoản ngân hàng | | ✓ | | Bank processing 24-48h sau khi lệnh rút | 1-2 ngày | Real-time banking API |
| 6 | Kiểm tra IPN/Webhook đối soát giao dịch | | ✓ | | Gateway timeout → phải retry, check manual | 5-30 phút | Circuit breaker + auto-fallback |

**Tổng lãng phí:** 6 hoạt động
- Move: 3 (50%)
- Hold: 3 (50%)
- Overdo: 0 (0%)

→ **Lãng phí phân bố đều giữa Move (reconciliation manual) và Hold (chờ settlement/banking).** COD reconciliation là nguồn lãng phí lớn nhất do COD chiếm ~40-45% giao dịch (~200,000-225,000 giao dịch/ngày).

### C. Root Cause Analysis — Fishbone (Ishikawa) 5 Cấp

```
Vấn đề: Tỷ lệ chênh lệch COD reconciliation 2-3% (~4,250-6,375 giao dịch/ngày) và thời gian đối soát chậm

Level 1 — Nguyên nhân lớn:
├── Con người (Man)
│   ├── Level 2: Shipper gian lận COD (thu tiền không nộp đủ)
│   │   ├── Level 3: Thiếu kiểm soát cash collection từ shipper
│   │   │   ├── Level 4: Không có GPS tracking + signature verification realtime
│   │   │   │   └── Level 5: COD verification technology chưa invest
│   │   └── Level 3: Finance team reconciliation thủ công
│   │       ├── Level 4: Quá nhiều giao dịch COD cần match manual
│   │       │   └── Level 5: COD volume ~40-45% quá lớn cho manual reconciliation
├── Quy trình (Process)
│   ├── Level 2: Settlement cycle L+2/L+3 quá chậm
│   │   ├── Level 3: Hold tiền trong Escrow quá lâu
│   │   │   ├── Level 4: Seller chưa có risk-based instant settlement
│   │   │   │   └── Level 5: Trust scoring model chưa mature enough
│   │   └── Level 3: COD reconciliation batch processing
│   │       ├── Level 4: Reconciliation chạy end-of-day thay vì real-time
│   │       │   └── Level 5: Legacy batch architecture chưa migrate
├── Công nghệ (Technology)
│   ├── Level 2: Payment gateway timeout + failures
│   │   ├── Level 3: Single gateway dependency
│   │   │   ├── Level 4: Không có multi-gateway failover
│   │   │   │   └── Level 5: Gateway contract chưa hỗ trợ auto-failover
│   │   └── Level 3: Fraud detection AI false positive cao
│   │       ├── Level 4: Fraud rate 0.3% nhưng chặn nhiều giao dịch hợp lệ
│   │       │   └── Level 5: Training data fraud VN-specific chưa đủ
└── Vật liệu (Material)
    ├── Level 2: COD cash flow opacity
    │   ├── Level 3: Không track được cash at each step
    │   │   ├── Level 4: Thiếu digital POD cho COD payments
    │   │   │   └── Level 5: Shipper handheld chưa capture payment proof
    │   └── Level 3: Double charge / duplicate transactions
    │       ├── Level 4: Thiếu idempotency key trong payment requests
    │       │   └── Level 5: Legacy payment API design
```

### 5-Why Analysis

**Vấn đề:** Tỷ lệ chênh lệch COD reconciliation 2-3%

| Level | Câu hỏi | Câu trả lời |
|-------|---------|-------------|
| Why 1 | Tại sao COD reconciliation có 2-3% chênh lệch? | Số tiền shipper nộp không khớp với hệ thống ghi nhận |
| Why 2 | Tại sao shipper nộp tiền không khớp? | Một số shipper thu tiền nhưng không nộp đủ hoặc nộp sai |
| Why 3 | Tại sao shipper có thể thu mà không nộp đủ? | Thiếu verification cash collection — không track real-time |
| Why 4 | Tại sao không track được? | COD verification technology chưa invest — shipper handheld không capture payment proof |
| Why 5 | Tại sao chưa invest? | Chi phí thiết bị + phát triển COD digital verification cao + COD đang giảm dần trend |

**Root Cause:** COD volume lớn (~40-45%) nhưng verification technology chưa theo kịp + reconciliation batch processing end-of-day tạo cơ hội cho gian lận/lỗi + manual reconciliation không scale được.

## 3.8.4. Phân tích định lượng

### A. Thời gian

| STT | Hoạt động | Min | Max | Avg | Ghi chú |
|-----|-----------|-----|-----|-----|---------|
| 1 | Chọn phương thức thanh toán (COD/Online/Ví) | 30 giây | 3 phút | 1 phút | Buyer |
| 2 | Thanh toán COD khi nhận hàng | 1 phút | 5 phút | 2 phút | Shipper thu hộ — ~40-45% đơn |
| 3 | Xác nhận thanh toán online qua cổng | 30 giây | 3 phút | 1 phút | Buyer + Gateway |
| 4 | Buyer nhận hàng & hoàn tất đơn | 2 phút | 10 phút | 5 phút | Nhận hàng tại cửa |
| 5 | Buyer nhận hoàn tiền khi hủy/hoàn trả | 5 phút | 48 giờ | 6 giờ | Per refund |
| 6 | Cổng thanh toán xử lý giao dịch | 3 giây | 30 giây | 5 giây | Automated |
| 7 | Xác minh chữ ký & tính hợp lệ giao dịch | 2 giây | 15 giây | 5 giây | Automated |
| 8 | Gửi kết quả thanh toán về hệ thống | 1 giây | 10 giây | 3 giây | Automated |
| 9 | Kiểm tra IPN/Webhook đối soát giao dịch | 3 giây | 30 giây | 10 giây | Automated |
| 10 | Hệ thống giữ tiền tạm thời trong Escrow | 3 giây | 10 giây | 5 giây | Automated |
| 11 | Đối chiếu giao dịch với mã đơn hàng | 3 giây | 30 giây | 10 giây | Automated |
| 12 | Giải ngân tiền cho Seller (L+2 ngày) | 1 ngày | 3 ngày | 2 ngày (online), 3 ngày (COD) | SLA L+2/L+3 |
| 13 | Đối soát COD với 3PL thu hộ | 2 giờ | 8 giờ | 4 giờ | Manual + batch |
| 14 | Tổng hợp đối soát dòng tiền cuối ngày | 2 giờ | 6 giờ | 3 giờ | End-of-day batch |
| 15 | Tính hoa hồng Lazada (1-8% theo danh mục) | 2 giây | 10 giây | 3 giây | Automated |
| 16 | Cập nhật số dư Ví Seller | 2 giây | 10 giây | 5 giây | Automated |
| 17 | Phòng Tài chính xử lý lệch dòng tiền | 30 phút | 24 giờ | 4 giờ | Per case |
| 18 | Xác nhận bảng đối soát cuối kỳ | 1 giờ | 8 giờ | 3 giờ | Finance |
| 19 | Điều chỉnh số liệu sai lệch trên bảng kê | 30 phút | 12 giờ | 2 giờ | Thủ công |
| 20 | Xuất hóa đơn & báo cáo tài chính | 5 phút | 30 phút | 10 phút | Automated |
| 21 | Seller kiểm tra số dư Ví trên Seller Centre | 1 phút | 10 phút | 3 phút | Seller |
| 22 | Seller yêu cầu rút tiền về tài khoản ngân hàng | 1 phút | 10 phút | 3 phút | Seller |

### B. Phân tích Cycle Time Probability-Weighted

| Hoạt động | Thời gian (phút) | Xác suất | Thời gian kỳ vọng (phút) | Ghi chú |
|-----------|-------------------|----------|--------------------------|---------|
| Chọn phương thức thanh toán | 1 | 100% | 1.0 | Bắt buộc |
| Thanh toán COD khi nhận hàng | 2 | 55% | 1.1 | COD path |
| Xác nhận thanh toán online qua cổng | 1 | 45% | 0.45 | Online path |
| Cổng thanh toán xử lý giao dịch | 0.08 | 100% | 0.08 | Tức thì |
| Xác minh chữ ký & tính hợp lệ | 0.08 | 100% | 0.08 | Tức thì |
| Gửi kết quả thanh toán về hệ thống | 0.05 | 100% | 0.05 | Tức thì |
| Kiểm tra IPN/Webhook đối soát giao dịch | 0.17 | 100% | 0.17 | Tức thì |
| Hệ thống giữ tiền tạm thời trong Escrow | 0.08 | 100% | 0.08 | Tức thì |
| Đối chiếu giao dịch với mã đơn hàng | 0.17 | 100% | 0.17 | Tức thì |
| Giải ngân tiền cho Seller — Online | 2,880 (2 ngày) | 45% | 1,296.0 | L+2 |
| Giải ngân tiền cho Seller — COD | 4,320 (3 ngày) | 55% | 2,376.0 | L+3 |
| Đối soát COD với 3PL thu hộ | 240 (4 giờ) | 55% | 132.0 | Daily batch |
| Tổng hợp đối soát dòng tiền cuối ngày | 180 (3 giờ) | 100% | 180.0 | End-of-day |
| Tính hoa hồng Lazada | 0.05 | 100% | 0.05 | Tức thì |
| Cập nhật số dư Ví Seller | 0.08 | 100% | 0.08 | Tức thì |
| Phòng Tài chính xử lý lệch dòng tiền | 240 (4 giờ) | 2.5% | 6.0 | 2-3% discrepancy |
| Xác nhận bảng đối soát cuối kỳ | 180 (3 giờ) | 100% | 180.0 | Finance |
| Điều chỉnh số liệu sai lệch trên bảng kê | 120 (2 giờ) | 1% | 1.2 | Rare |
| Xuất hóa đơn & báo cáo tài chính | 10 | 100% | 10.0 | Automated |
| Seller kiểm tra số dư Ví trên Seller Centre | 3 | 100% | 3.0 | Per request |
| Seller yêu cầu rút tiền về tài khoản ngân hàng | 3 | 100% | 3.0 | Per withdrawal |

**Tổng Cycle Time kỳ vọng (checkout đến seller nhận tiền) = 4,191 phút ≈ 70 giờ ≈ 2.9 ngày**

- Online path: ~3,266 phút ≈ 54 giờ ≈ 2.3 ngày
- COD path: ~4,947 phút ≈ 82 giờ ≈ 3.4 ngày

### C. Chi phí (per transaction)

| STT | Thành phần | Chi phí (VND) | Ghi chú |
|-----|-----------|---------------|---------|
| 1 | Payment gateway fee | 1,500 | 1.5% × AOV 100,000 VND |
| 2 | Transaction processing (system) | 500 | Infrastructure allocated |
| 3 | Fraud check (AI model) | 100 | Machine learning inference |
| 4 | Escrow holding cost | 200 | Cash cost 0.5%/30 ngày × 3 ngày avg |
| 5 | COD reconciliation (manual allocated) | 300 | 2.5% discrepancy × labor cost |
| 6 | Refund processing (5% cases) | 50 | 5% × 1,000 VND refund cost |
| 7 | Withdrawal processing | 100 | Bank transfer fee shared |
| **TỔNG** | | **2,750 VND** | Per transaction |

**Volume ước tính:** ~15 triệu giao dịch/tháng
**Monthly cost:** ~41.25 tỷ VND/tháng (processing cost)
**Payment gateway fees toàn sàn:** ~67.5-112.5 tỷ VND/tháng (1.5-2.5% × 4,500 tỷ)

### D. Chất lượng

| Metric | Current | Benchmark (VN e-commerce) | Gap |
|--------|---------|---------------------------|-----|
| Payment success rate | 94% | 98% | -4% |
| Fraud detection rate | 85% | 95% | -10% |
| COD reconciliation accuracy | 97-98% | 99.5% | -1.5-2.5% |
| Average settlement time (online) | L+2 (48h) | L+1 (24h) | +24h |
| Average settlement time (COD) | L+3 (72h) | L+2 (48h) | +24h |
| Withdrawal processing time | 24-48h | 4-8h | +16-40h |
| Payment dispute rate | 0.8% | 0.3% | +0.5% |
| Double charge incidents | 50/ngày | <5/ngày | +45/ngày |

## 3.8.5. Phân tích Pareto

### Bảng Vấn đề — Giả thuyết — Chi phí ảnh hưởng

| STT | Vấn đề | Giả thuyết | Chi phí ảnh hưởng/tháng (VND) | Tỷ trọng |
|-----|--------|-----------|-------------------------------|----------|
| 1 | COD reconciliation chênh lệch 2-3% | Shipper gian lận COD + batch reconciliation tạo window fraud | 90,000,000,000-135,000,000,000 (2.5% × 4,500 tỷ ÷ 12) | 35.0% |
| 2 | Settlement cycle chậm (L+2/L+3) | Hold tiền Escrow quá lâu → seller cash flow ảnh hưởng | 75,000,000,000 (interest cost + seller churn risk) | 29.2% |
| 3 | Payment gateway failures + timeout | Single gateway dependency, failover chưa có | 45,000,000,000 (lost sales + CS cost) | 17.5% |
| 4 | Fraud rate 0.3% (~1,500 cases/ngày) | AI model chưa đủ VN-specific fraud patterns | 30,000,000,000 (direct loss + investigation cost) | 11.7% |
| 5 | Withdrawal processing 24-48h | Banking integration chưa real-time | 17,000,000,000 (seller satisfaction + churn) | 6.6% |
| **TỔNG** | | | **~257,000,000,000** | **100%** |

### Kết luận 80/20

**Top 3 vấn đề (chiếm ~82% chi phí):**
1. COD reconciliation chênh lệch (35.0%) — giải pháp: auto-reconciliation ML + COD digital verification
2. Settlement cycle chậm (29.2%) — giải pháp: instant settlement cho trusted seller + giảm L+1
3. Payment gateway failures (17.5%) — giải pháp: multi-gateway failover + circuit breaker

→ **Giải quyết 3 vấn đề này sẽ giảm ~82% chi phí lãng phí (~211 tỷ VND/tháng).**

## 3.8.6. Kết luận và hướng cải tiến TO-BE

### Tóm tắt AS-IS
- Cycle time checkout đến seller nhận tiền: ~2.9 ngày (online ~2.3 ngày, COD ~3.4 ngày)
- Chi phí per transaction: ~2,750 VND
- COD reconciliation accuracy: 97-98% (2-3% chênh lệch)
- Payment success rate: 94%
- Fraud rate: 0.3% (~1,500 cases/ngày)
- Withdrawal processing: 24-48h
- COD chiếm ~40-45% giao dịch — tạo phần lớn reconciliation work

### Hướng cải tiến TO-BE

| STT | Cải tiến | Mục tiêu | Giảm chi phí (tháng) |
|-----|---------|----------|----------------------|
| 1 | Auto-reconciliation ML + COD digital verification (GPS + signature) | COD discrepancy: 2-3% → 0.5%, reconciliation time: 4h → 30 phút | -90-135 tỷ VND |
| 2 | Instant settlement cho trusted seller (risk-based L+1) + giảm overall settlement cycle | Settlement: L+2/L+3 → L+1 cho 60% seller | -75 tỷ VND |
| 3 | Multi-gateway failover + circuit breaker + auto-fallback | Payment success: 94% → 98.5% | -45 tỷ VND |
| 4 | AI fraud detection nâng cao (risk scoring real-time, VN-specific patterns) | Fraud: 0.3% → 0.1%, false positive giảm 60% | -30 tỷ VND |
| 5 | Real-time banking API + ví Lazada instant withdrawal | Withdrawal: 24-48h → instant (wallet) / 4-8h (bank) | -17 tỷ VND |
| **TỔNG GIẢM** | | | **-257-262 tỷ VND/tháng** |

### So sánh AS-IS vs TO-BE

| Metric | AS-IS | TO-BE | Cải thiện |
|--------|-------|-------|-----------|
| Payment success rate | 94% | 98.5% | +4.5% |
| COD reconciliation accuracy | 97-98% | 99.5% | +1.5-2.5% |
| Settlement time (online) | L+2 (48h) | L+1 (24h) | -50% |
| Settlement time (COD) | L+3 (72h) | L+2 (48h) | -33% |
| Fraud rate | 0.3% | 0.1% | -67% |
| Withdrawal processing | 24-48h | Instant (wallet) / 4-8h (bank) | -80-100% |
| COD discrepancy rate | 2-3% | 0.5% | -75-83% |
| Chi phí per transaction | 2,750 VND | 1,200 VND | -56% |
| Monthly processing cost | 41.25 tỷ VND | 18 tỷ VND | -23.25 tỷ VND |
| Monthly total cost (waste) | ~257 tỷ VND | ~45 tỷ VND | -212 tỷ VND (-82%) |

# 3.3. Quy trình Xử lý Đơn hàng Online (Order Fulfillment)

## 3.3.1. Mô tả quy trình

**Phạm vi:** Bắt đầu từ khi Buyer xem lại đơn hàng và thanh toán → Validate thông tin → Xác nhận đơn → Fulfillment → Giao hàng → Hoàn tất/Thanh toán/Giải ngân. Đây là quy trình trọng tâm, phức tạp nhất của sàn.

**Các tác nhân tham gia:**
- **Buyer:** Người mua — xem đơn, thanh toán, nhận hàng, xác nhận
- **Lazada System (Automated):** Validate, khóa tồn kho, kiểm tra gian lận AI, vận đơn, định vị, auto-confirm
- **Seller:** Người bán — xác nhận đơn, đóng gói, bàn giao
- **3PL/Shipper:** Đơn vị vận chuyển — lấy hàng, giao hàng
- **Payment Gateway:** Cổng thanh toán — verify, giữ tiền tạm thời (COD), hoàn tiền

**Kết quả có thể xảy ra:**
- Đơn hoàn tất — giao thành công, buyer xác nhận/auto-confirm
- Đã hoàn tiền — đơn hủy sau khi thanh toán online
- Đơn bị hủy — seller quá hạn 48h, buyer hủy, hoặc auto-cancel

### SiPOC

| SiPOC | Chi tiết |
|-------|----------|
| **Supplier** | Buyer (đơn hàng + thanh toán), Seller (hàng hóa), 3PL/LEX (logistics), Payment Gateway (xác thực thanh toán) |
| **Input** | Đơn hàng, phương thức thanh toán (COD/Thẻ/Ví/CK), thông tin giao hàng, tồn kho |
| **Process** | Xem đơn → Thanh toán → Validate → Khóa tồn kho → Check fraud → Seller xác nhận → Đóng gói → Vận đơn → Lấy hàng → Giao → Xác nhận → Auto-confirm → Giải ngân |
| **Output** | Đơn hoàn tất, Đã hoàn tiền, Đơn bị hủy, Giải ngân cho Seller |
| **Customer** | Buyer (nhận hàng đúng hạn), Seller (nhận tiền đúng chu kỳ) |

## 3.3.2. Mô hình BPMN

*(File: `processes/03-order-processing.bpmn`)*

**Thống kê mô hình:**
- Số lanes: 5 (Buyer, Lazada System (Automated), Seller, 3PL/Shipper, Payment Gateway)
- Số activities: 26 (7 userTask + 16 serviceTask + 3 task)
- Số gateways: 17 (XOR); data object retryCount
- End events: 3
- Độ phức tạp: High (quy trình phức tạp nhất)

## 3.3.3. Phân tích định tính

### A. Value-Added Analysis

| STT | Hoạt động (tên từ BPMN) | VA | BVA | NVA | Giải thích | Đề xuất TO-BE |
|-----|--------------------------|----|-----|-----|------------|---------------|
| 1 | Xem lại đơn hàng | ✓ |  |  | KH xác nhận giỏ hàng — tránh nhầm lẫn | Giữ nguyên |
| 2 | Thanh toán đơn hàng (COD / Thẻ / Ví / Chuyển khoản) | ✓ |  |  | Giao dịch trực tiếp — tạo doanh thu | Giữ nguyên; one-tap checkout |
| 3 | Nhận hàng từ shipper | ✓ |  |  | KH nhận hàng — hoàn tất giá trị | Giữ nguyên |
| 4 | Xác nhận đã nhận hàng | ✓ |  |  | Chốt giao dịch hoàn chỉnh | Auto-confirm sau 7 ngày |
| 5 | Buyer hủy đơn | ✓ |  |  | Quyền lợi KH trước khi giao | Giữ nguyên; auto-refund |
| 6 | Validate thông tin đơn |  | ✓ |  | Kiểm tra hợp lệ — prevent errors | Nâng cấp rule real-time |
| 7 | Khóa tồn kho + tạo đơn |  | ✓ |  | Chống bán quá — quản trị tồn kho | Auto reservation ngay khi đặt |
| 8 | Kiểm tra gian lận (AI) |  | ✓ |  | Chống fraud — bảo vệ hệ thống | Nâng cấp model liên tục |
| 9 | Kiểm tra tồn kho |  | ✓ |  | Đảm bảo khả năng giao — tránh hủy đơn | Real-time sync với warehouse |
| 10 | Tạo vận đơn tự động (LEX / 3PL) | ✓ |  |  | Đầu vào thiết yếu cho vận chuyển | Tạo nhãn vận đơn QR số hóa |
| 11 | Cập nhật định vị đơn hàng realtime | ✓ |  |  | KH theo dõi đơn — trải nghiệm giá trị | API auto-sync tracking |
| 12 | Đếm số lần giao lại |  | ✓ |  | Kiểm soát tối đa 3 lần — vận hành | Kết nối auto-cancel khi đạt limit |
| 13 | Auto-confirm (7 ngày) |  | ✓ |  | Chốt đơn khi KH im lặng | Rút ngắn còn 24-72h cho Shop uy tín (Bảng 3.13 P1) |
| 14 | Hủy đơn do Seller quá hạn 48h |  | ✓ |  | Bảo vệ KH khi Seller không phản hồi | **Giảm còn 2h** kết hợp auto-accept |
| 15 | Giải ngân cho Seller |  | ✓ |  | Thanh toán theo escrow — vận hành tài chính | Giữ nguyên (auto) |
| 16 | Auto-cancel đơn |  | ✓ |  | Hủy tự động khi thất bại/permissions | Giữ nguyên |
| 17 | Thông báo hủy đơn | ✓ |  |  | KH biết trạng thái — giao tiếp minh bạch | Smart notification (Push > SMS) |
| 18 | Tự động hoàn tiền cho Buyer | ✓ |  |  | Hoàn tiền — giá trị trực tiếp cho KH | Instant refund |
| 19 | Seller xác nhận đơn |  | ✓ |  | Bước điều phối — KHÔNG tạo giá trị trực tiếp | **Auto-accept sau 2h** (giảm Hold 2-24h) |
| 20 | Seller đóng gói |  | ✓ |  | Chuẩn bị hàng — bước chuẩn bị vận chuyển | Quy chuẩn đóng gói + ảnh xác nhận |
| 21 | Bàn giao hàng cho 3PL / LEX |  | ✓ |  | Kích hoạt vận chuyển | API auto-sync (bỏ nhập tay tracking) |
| 22 | Giao hàng (attempt) |  | ✓ |  | Hoàn tất phân phối | Pre-delivery call + time slot |
| 23 | LEX (Lazada Express) lấy hàng & quét barcode tại kho |  | ✓ |  | Vận hành logistics nội bộ | Tự động lên lịch lấy hàng với 3PL |
| 24 | Gateway verify thanh toán |  | ✓ |  | Xác minh giao dịch — bảo mật | Giữ nguyên |
| 25 | Giữ tiền tạm thời (COD) |  | ✓ |  | Escrow chống rủi ro | Giữ nguyên |
| 26 | Cổng thanh toán xử lý hoàn tiền |  | ✓ |  | Xử lý hoàn tiền qua gateway | Giữ nguyên |

**Tỷ lệ VA/BVA/NVA:**
- VA: 9/26 (34%)
- BVA: 17/26 (65%)
- NVA: 0/26 (0%)

→ **Nhận xét:** NVA 0% — nhưng BVA rất cao (65%) là cần thiết cho kiểm soát fulfillment (fraud check, stock check, xác nhận đơn) và có thể tối ưu bằng tự động hóa để giảm chi phí xử lý đơn.

### B. Waste Analysis

| STT | Hoạt động | Move | Hold | Overdo | Mô tả | Thời gian chờ | Giải pháp |
|-----|-----------|------|------|--------|-------|---------------|-----------|
| 1 | Seller xác nhận đơn (SLA 48h) | | ✓ | | Seller chậm phản hồi → đơn chờ | 48h max, avg 24h | Giảm SLA xuống 24h + reminder |
| 2 | Hủy đơn do Seller quá hạn 48h | | ✓ | | Hàng chờ 48h rồi bị hủy | 48h | Auto-remind + nút quick-accept |
| 3 | Giao hàng (attempt) thất bại | | ✓ | | Vắng nhà, sai địa chỉ → retry | 1-3 ngày/lần | OTP + slot hẹn giờ, trước giao gọi lại |
| 4 | Đếm số lần giao lại (tối đa 3) | | ✓ | | Retry tối đa 3 lần gây chậm | 3-5 ngày | Giảm xuống 2 lần + hẹn giờ |
| 5 | Auto-confirm (7 ngày) | | ✓ | | Chờ 7 ngày để auto-confirm | 7 ngày | Rút ngắn còn 24-72h (Shop uy tín) |
| 6 | Buyer hủy đơn sau khi đặt | | | ✓ | Đổi ý → hủy → vận hành wasted | Tức thì-24h | Nút hủy giới hạn + phí nhỏ |

**Tổng lãng phí:** 6 hoạt động
- Move: 0 (0%)
- Hold: 5 (83%)
- Overdo: 1 (17%)

→ **Hold time chiếm 83%** — seller xác nhận, giao lại, và auto-confirm là các bottleneck chính.

### C. Root Cause Analysis — Fishbone (Ishikawa) 5 Cấp

```
Vấn đề: Tỷ lệ hủy đơn cao (7-10%) và thời gian giao hàng trung bình 3-5 ngày

Level 1 — Nguyên nhân lớn:
├── Con người (Man)
│   ├── Level 2: Seller không phản hồi đơn trong SLA
│   │   ├── Level 3: Seller không online vào thời điểm đơn đến
│   │   │   ├── Level 4: Không có mobile push reminder hiệu quả
│   │   │   │   └── Level 5: Seller app chưa có real-time notification tối ưu
│   │   └── Level 3: Seller chủ động hủy vì hết hàng
│   │       ├── Level 4: Inventory sync không realtime
│   │       │   └── Level 5: Seller không cập nhật tồn kho thường xuyên
├── Quy trình (Process)
│   ├── Level 2: SLA 48h quá dài
│   │   ├── Level 3: SLA được thiết kế chung cho mọi seller
│   │   │   ├── Level 4: Không phân biệt seller FBL vs tự giao
│   │   │   │   └── Level 5: Thiếu differentiated SLA theo fulfillment model
│   │   └── Level 3: Giao lại tối đa 3 lần
│   │       ├── Level 4: Không có slot hẹn giờ cho buyer
│   │       │   └── Level 5: Logistics design chưa customer-centric
├── Công nghệ (Technology)
│   ├── Level 2: Auto-confirm 7 ngày vẫn quá lâu
│   │   ├── Level 3: Sợ buyer chưa nhận hàng
│   │   │   ├── Level 4: Không có POD (proof of delivery) xác nhận realtime
│   │   │   │   └── Level 5: Thiếu digital POD integration với 3PL
│   │   └── Level 3: Fraud check AI chưa hoàn thiện
│   │       ├── Level 4: False positive cao → chặn đơn hợp lệ
│   │       │   └── Level 5: Training data chưa đủ VN-specific fraud patterns
└── Vật liệu (Material)
    ├── Level 2: Hàng hóa không có sẵn lúc bán
    │   ├── Level 3: Seller oversell do inventory lag
    │   │   ├── Level 4: Không tích hợp API với hệ thống kho seller
    │   │   │   └── Level 5: Sellers nhỏ không đủ năng lực integrate
    │   └── Level 3: Sai địa chỉ giao
    │       ├── Level 4: Buyer nhập sai/nhập tắt
    │       │   └── Level 5: Thiếu address validation trước khi checkout
```

### 5-Why Analysis

**Vấn đề:** Tỷ lệ hủy đơn do Seller quá hạn 48h cao (~20% tổng hủy đơn)

| Level | Câu hỏi | Câu trả lời |
|-------|---------|-------------|
| Why 1 | Tại sao seller quá hạn 48h? | Seller không phản hồi đơn kịp |
| Why 2 | Tại sao seller không phản hồi kịp? | SLA 48h quá dài + không có reminder hiệu quả |
| Why 3 | Tại sao SLA 48h quá dài? | Thiết kế chung cho mọi seller, không phân biệt |
| Why 4 | Tại sao không phân biệt? | Chưa có differentiated SLA theo fulfillment model (FBL vs tự giao) |
| Why 5 | Tại sao chưa có differentiated SLA? | System chưa phân loại seller performance để set SLA động |

**Root Cause:** SLA cố định 48h không tối ưu + thiếu real-time inventory sync + POD integration chưa hoàn thiện.

## 3.3.4. Phân tích định lượng

### A. Thời gian

| STT | Hoạt động | Min | Max | Avg | Ghi chú |
|-----|-----------|-----|-----|-----|---------|
| 1 | Xem lại đơn hàng | 1 phút | 10 phút | 3 phút | Buyer review |
| 2 | Thanh toán đơn hàng (COD / Thẻ / Ví / Chuyển khoản) | 30 giây | 5 phút | 2 phút | Phương thức khác nhau |
| 3 | Validate thông tin đơn | 2 giây | 10 giây | 5 giây | Automated |
| 4 | Khóa tồn kho + tạo đơn | 2 giây | 10 giây | 5 giây | Automated |
| 5 | Kiểm tra gian lận (AI) | 3 giây | 30 giây | 10 giây | Automated |
| 6 | Kiểm tra tồn kho | 2 giây | 10 giây | 5 giây | Automated |
| 7 | Seller xác nhận đơn | 5 phút | 48 giờ | 12 giờ | SLA 48h |
| 8 | Hủy đơn do Seller quá hạn 48h | 1 giờ | 24 giờ | 6 giờ | ~10% đơn |
| 9 | Seller đóng gói | 30 phút | 3 giờ | 1 giờ | Manual |
| 10 | Tạo vận đơn tự động (LEX / 3PL) | 1 phút | 5 phút | 2 phút | Automated |
| 11 | Bàn giao hàng cho 3PL / LEX | 10 phút | 2 giờ | 30 phút | Theo lịch chuyến |
| 12 | LEX (Lazada Express) lấy hàng & quét barcode tại kho | 10 phút | 1 giờ | 20 phút | Pickup |
| 13 | Cập nhật định vị đơn hàng realtime | 1 phút | 5 phút | 2 phút | Automated |
| 14 | Giao hàng (attempt) | 5 phút | 30 phút | 10 phút | Per attempt |
| 15 | Đếm số lần giao lại | 1 giờ | 3 ngày | 1 ngày | Retry loop |
| 16 | Nhận hàng từ shipper | 2 phút | 10 phút | 5 phút | Buyer |
| 17 | Xác nhận đã nhận hàng | 1 phút | 5 phút | 2 phút | Buyer confirm |
| 18 | Auto-confirm (7 ngày) | 7 ngày | 7 ngày | 7 ngày | Timer P7D — đúng Bảng 3.2 |
| 19 | Giải ngân cho Seller (L+2) | 1 ngày | 2 ngày | 1.5 ngày | L+2: funds sau 1-2 ngày (Bảng 3.4 WT 36h) |
| 20 | Buyer hủy đơn | 1 phút | 24 giờ | 1 giờ | Đổi ý |
| 21 | Auto-cancel đơn | 1 giờ | 24 giờ | 6 giờ | Hệ thống |
| 22 | Thông báo hủy đơn | 1 phút | 5 phút | 2 phút | Automated |
| 23 | Tự động hoàn tiền cho Buyer | 5 phút | 48 giờ | 6 giờ | Qua gateway |
| 24 | Gateway verify thanh toán | 5 giây | 30 giây | 10 giây | Automated |
| 25 | Giữ tiền tạm thời (COD) | 1 ngày | 2 ngày | 1.5 ngày | COD escrow (L+2 cycle) |
| 26 | Cổng thanh toán xử lý hoàn tiền | 5 phút | 5 ngày | 12 giờ | Refund |

### B. Phân tích Cycle Time Probability-Weighted

| Hoạt động | Thời gian (phút) | Xác suất | Thời gian kỳ vọng (phút) | Ghi chú |
|-----------|-------------------|----------|--------------------------|---------|
| Xem lại đơn hàng | 3 | 100% | 3.0 | Bắt buộc |
| Thanh toán đơn hàng (COD / Thẻ / Ví / Chuyển khoản) | 2 | 100% | 2.0 | Bắt buộc |
| Validate thông tin đơn | 0.08 | 100% | 0.08 | Tức thì |
| Khóa tồn kho + tạo đơn | 0.08 | 100% | 0.08 | Tức thì |
| Kiểm tra gian lận (AI) | 0.17 | 100% | 0.17 | Tức thì |
| Kiểm tra tồn kho | 0.08 | 100% | 0.08 | Tức thì |
| Seller xác nhận đơn | 720 (12h avg) | 100% | 720.0 | SLA 48h |
| Hủy đơn do Seller quá hạn 48h | 360 (6h) | 10% | 36.0 | 10% đơn bị hủy |
| Seller đóng gói | 60 | 100% | 60.0 | Manual |
| Tạo vận đơn tự động (LEX / 3PL) | 2 | 100% | 2.0 | Automated |
| Bàn giao hàng cho 3PL / LEX | 30 | 100% | 30.0 | Theo lịch |
| LEX lấy hàng & quét barcode tại kho | 20 | 100% | 20.0 | Pickup |
| Cập nhật định vị đơn hàng realtime | 2 | 100% | 2.0 | Automated |
| Giao hàng (attempt) | 10 | 100% | 10.0 | Per attempt |
| Đếm số lần giao lại | 1,440 (1 ngày) | 8% | 115.2 | 8% đơn cần retry |
| Nhận hàng từ shipper | 5 | 100% | 5.0 | Buyer |
| Xác nhận đã nhận hàng | 2 | 70% | 1.4 | 70% buyer confirm nhanh |
| Auto-confirm (7 ngày) | 10,080 (7 ngày) | 30% | 3,024.0 | 30% auto-confirm |
| Giải ngân cho Seller (L+2) | 2,160 (1.5 ngày) | 100% | 2,160.0 | L+2: WT 36h (Bảng 3.4) |
| Tự động hoàn tiền cho Buyer | 360 (6h) | 10% | 36.0 | Chỉ khi hủy |
| Gateway verify thanh toán | 0.17 | 100% | 0.17 | Tức thì |
| Giữ tiền tạm thời (COD) | 2,160 (1.5 ngày) | 45% | 972.0 | 45% COD escrow (L+2) |
| Cổng thanh toán xử lý hoàn tiền | 720 (12h) | 10% | 72.0 | Chỉ khi hủy |

**Tổng Cycle Time kỳ vọng (từ đặt đến giải ngân) = 7,271 phút ≈ 121 giờ ≈ 5.0 ngày**
**Tổng Cycle Time từ đặt hàng đến giao thành công (happy path, không gồm hoàn tiền/giữ tiền COD) = 6,191 phút ≈ 103 giờ ≈ 4.3 ngày** (giữ nguyên — auto-confirm không nằm trong happy path)

### C. Chi phí (per order)

| STT | Thành phần | Chi phí (VND) | Ghi chú |
|-----|-----------|---------------|---------|
| 1 | Payment gateway fee | 4,000 | 1,43% của AOV 280.000 VNĐ (Bảng 3.5) |
| 2 | Logistics cost (chặng đầu + sort + last-mile) | 23,300 | Pickup 5,500 + Sort 2,800 + Last-mile 15,000 (Bảng 3.5) |
| 3 | IT infrastructure & bandwidth | 900 | Alibaba Cloud, API Gateway (Bảng 3.5) |
| 4 | Đóng gói (Seller chịu) | 5,000 | Hộp carton, băng dính, xốp nổ, phiếu in (Bảng 3.5) |
| 5 | Dự phòng giao hỏng / COD refusal | 3,500 | Chi phí xử lý khiếu nại + reverse logistics (Bảng 3.5) |
| 6 | CSKH / Khiếu nại phân bổ | 2,200 | Phân bổ chi phí CS theo đơn (Bảng 3.5) |
| **TỔNG** | | **38,900 VNĐ** | Per order (khớp Bảng 3.5 — chi phí vận hành biên) |

**Volume ước tính:** ~20 triệu đơn/tháng (Lazada VN)
**Monthly cost:** ~778 tỷ VND/tháng (38.900 VNĐ × ~20 triệu đơn/tháng, bao gồm chi phí logistics trực tiếp)

### D. Chất lượng (Quality Metrics)

| Metric (Chỉ số) | Hiện tại (AS-IS) | Benchmark (VN e-commerce) | Gap | Mục tiêu TO-BE |
|-----------------|------------------|---------------------------|-----|----------------|
| Tỷ lệ giao thành công lần đầu (First-attempt delivery) | 75-80% | 82-88% | -5-8% | **92%** |
| Thời gian xử lý đơn trung bình (Avg Order Processing Time) | 24-48h | 12-24h | +12-24h | **4-8h** |
| Tỷ lệ lỗi đóng gói (Packaging Error Rate) | 5% | 1-2% | +3-4% | **<1%** |
| Tỷ lệ hủy đơn tự động (Auto-Cancellation Rate) | 8% | 3-5% | +3-5% | **1-2%** |
| Chi phí vận hành biên/đơn (Unit Cost) | 38,900 VNĐ | 20,000 VND | +18,900 VNĐ | **19,000 VNĐ** |
| Throughput kho (đơn/ngày) (Warehouse Throughput) | 5,000 | 8,000 | -3,000 | **15,000** |
| Tỷ lệ accuracy lấy hàng (Picking Accuracy) | 95% | 98% | -3% | **99.5%** |
| Tỷ lệ hủy đơn (Cancellation Rate) | 7-10% | 3-5% | +4-5% | **1-2%** |
| Thời gian giao hàng trung bình (Avg Delivery Time) | 3-5 ngày | 2-3 ngày | +1-2 ngày | **1-2 ngày** |
| Tỷ lệ trả hàng (Return Rate) | 8% | 3-5% | +3-5% | **2-3%** |

> **Ghi chú:** Các số liệu benchmark dựa trên khảo sát industry VN e-commerce 2025-2026. Mục tiêu TO-BE dựa trên mô hình cải tiến AI/automation.

## 3.3.5. Phân tích Pareto

### Bảng Vấn đề — Giả thuyết — Chi phí ảnh hưởng

| STT | Vấn đề | Giả thuyết | Chi phí ảnh hưởng/tháng (VND) | Tỷ trọng |
|-----|--------|-----------|-------------------------------|----------|
| 1 | Seller xác nhận chậm + hủy do quá hạn | SLA 48h quá dài, thiếu reminder real-time | 300,000,000,000 (lost GMV + rework) | 44.1% |
| 2 | Auto-confirm 7 ngày → giải ngân chậm | Thiếu POD realtime integration | 180,000,000,000 (cash flow lock) | 26.5% |
| 3 | Giao lại nhiều lần (tối đa 3) | Thiếu slot hẹn giờ + sai địa chỉ | 110,000,000,000 (phí ship phụ) | 16.2% |
| 4 | Buyer hủy đơn đổi ý | Thiếu nút hủy giới hạn + phí | 60,000,000,000 (wasted fulfillment) | 8.8% |
| 5 | Fraud check false positive | AI model chưa đủ VN-specific data | 30,000,000,000 (chặn đơn hợp lệ) | 4.4% |
| **TỔNG** | | | **680,000,000,000** | **100%** |

### Kết luận 80/20

**Top 3 vấn đề (chiếm ~87% chi phí):**
1. Seller xác nhận chậm + hủy đơn (44.1%) — giải pháp: SLA 24h + real-time reminder
2. Auto-confirm 7 ngày → chậm giải ngân — giải pháp: POD digital + giảm 24-72h cho Shop uy tín
3. Giao lại nhiều lần (16.2%) — giải pháp: slot hẹn giờ + address validation

→ **Giải quyết 3 vấn đề này sẽ giảm ~87% chi phí lãng phí (~590 tỷ VND/tháng).**

## 3.3.6. Kết luận và hướng cải tiến TO-BE

### Tóm tắt AS-IS
- Cycle time từ đặt đến giao: ~4.3 ngày
- Cycle time đến giải ngân: ~5.8 ngày (L+2 settlement)
- Chi phí per order: ~38,900 VNĐ (Bảng 3.5)
- Cancellation rate: 7-10%
- Bottleneck: Seller xác nhận 48h + auto-confirm 7 ngày

### Hướng cải tiến TO-BE

| STT | Cải tiến | Mục tiêu | Giảm chi phí (tháng) |
|-----|---------|----------|----------------------|
| 1 | SLA 24h + real-time seller reminder (push + SMS) | Seller confirm: 12h → 4h, hủy: 10% → 4% | -300 tỷ VND |
| 2 | Digital POD + auto-confirm 24-72h (Shop uy tín) | Cash flow unlock nhanh gấp đôi | -180 tỷ VND |
| 3 | Slot hẹn giờ + address validation + tối đa 2 lần retry | Giao lại: 8% → 4% | -110 tỷ VND |
| 4 | Nút hủy giới hạn + phí hủy nhỏ | Hủy đổi ý: 3% → 1.5% | -60 tỷ VND |
| 5 | Upgrade fraud AI model | False positive giảm 50% | -30 tỷ VND |
| **TỔNG GIẢM** | | | **-680 tỷ VND/tháng** |

### So sánh AS-IS vs TO-BE

| Metric | AS-IS | TO-BE | Cải thiện |
|--------|-------|-------|-----------|
| On-time delivery (lần đầu) | 75-80% | 92% | +12-17 điểm % |
| Cancellation rate | 7-10% | 3-5% | -50% |
| Seller confirm time | 12h avg | 4h avg | -67% |
| Auto-confirm | 7 ngày | 24-72h | -86~-96% |
| Time to disburse | L+2 (~36h) | T+1 (~24h) | -33% |
| Giao lại rate | 8% | 4% | -50% |
| Chi phí per order | 38,900 VNĐ | 19,000 VNĐ | -51% |

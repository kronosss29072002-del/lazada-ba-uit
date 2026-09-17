# 3.9. Quy trình Logistics & Giao nhận (Logistics & Delivery)

## 3.9.1. Mô tả quy trình

**Phạm vi:** Bắt đầu từ khi đơn hàng được Seller chuẩn bị và đóng gói hàng hóa → Đặt lịch hẹn lấy hàng từ 3PL → Tạo vận đơn tự động (AWB) + gửi mã theo dõi cho Buyer → Phân công 3PL phù hợp → 3PL nhận hàng từ kho Seller → Phân loại hàng tại kho trung tâm 3PL → Vận chuyển hàng qua các trung tâm phân loại → Hàng xuất kho, shipper nhận giao → Giao hàng cho Buyer tại địa chỉ → Buyer nhận/kiểm tra hoặc từ chối → Hẹn giao lại (nếu thất bại) → Hàng hoàn về kho Seller sau 3 lần giao thất bại. Đây là quy trình chiếm tỷ trọng chi phí lớn nhất trong toàn bộ chuỗi giá trị, với khoảng 400.000 kiện hàng/ngày tại Lazada Việt Nam.

**Các tác nhân tham gia:**
- **Seller:** Đóng gói hàng, bàn giao cho đơn vị vận chuyển hoặc chờ LEX lấy hàng
- **Lazada System (Automated):** Tạo vận đơn AWB, phân bổ 3PL, cập nhật tracking realtime, tính ETA dự đoán, tối ưu tuyến đường
- **LEX (Lazada Express) / 3PL:** LEX xử lý ~60% đơn hàng, các đối tác 3PL (GHN, GHTK, J&T, Ninja Van) xử lý ~40%; lấy hàng, phân loại Hub, vận chuyển, giao hàng
- **Shipper:** Người giao hàng trực tiếp — liên hệBuyer, giao hàng, thu COD, ghi nhận POD
- **Buyer:** Nhận hàng, kiểm tra, xác nhận hoặc từ chối, đánh giá trải nghiệm giao hàng

**Kết quả có thể xảy ra:**
- Giao hàng thành công — Buyer nhận và xác nhận (POD), đơn hoàn tất
- Giao lại — Lần 1 thất bại (vắng nhà, sai địa chỉ), giao lại tối đa 3 lần
- Hàng hoàn về — Giao thất bại sau 3 lần → hoàn về kho trung chuyển → hoàn về Seller
- Tranh chấp vận chuyển — Hàng hư hỏng, mất, sai đơn → khiếu nại logistics

### SiPOC

| SiPOC | Chi tiết |
|-------|----------|
| **Supplier** | Seller (hàng hóa đóng gói), LEX/3PL (hạ tầng logistics, kho Hub, xe vận chuyển, shipper) |
| **Input** | Đơn hàng đã xác nhận, hàng hóa đóng gói sẵn sàng, thông tin giao hàng (địa chỉ, SĐT, khung giờ), AWB barcode |
| **Process** | Chuẩn bị & đóng gói hàng → Đặt lịch lấy hàng → Tạo AWB → Phân công 3PL → 3PL nhận hàng → Sort Hub → Trung chuyển → Xuất kho giao → Giao hàng → Nhận/từ chối → Hẹn giao lại → Hoàn về kho Seller |
| **Output** | Hàng giao thành công (POD xác nhận), hàng hoàn về kho/Seller, tracking realtime cho Buyer, COD thu hộ, chi phí vận chuyển |
| **Customer** | Buyer (nhận hàng đúng hạn, đúng trạng thái), Seller (chi phí vận chuyển hợp lý, hàng hoàn về nguyên vẹn) |

## 3.9.2. Mô hình BPMN

*(File: `processes/09-logistics-delivery.bpmn`)*

**Thống kê mô hình:**
- Số lanes: 5 (Seller, Lazada System, LEX / 3PL (GHN, GHTK, J&T, NINJAVAN), Shipper (Giao hàng), Buyer)
- Số activities: 20 (12 userTask + 8 serviceTask)
- Số gateways: 13 (13 XOR; retry loop cho giao lại)
- End events: 2 (Đơn hàng đã giao thành công, Hàng đã hoàn về Seller)
- Độ phức tạp: High (nhiều bước trung chuyển, retry loop giao lại, tương tác nhiều bên)

## 3.9.3. Phân tích định tính

### A. Value-Added Analysis

| STT | Hoạt động (tên từ BPMN) | VA | BVA | NVA | Giải thích | Đề xuất TO-BE |
|-----|--------------------------|----|-----|-----|------------|---------------|
| 1 | Seller chuẩn bị hàng hóa đóng gói | ✓ |  |  | Chuẩn bị hàng vận chuyển — bắt buộc | Hướng dẫn đóng gói chuẩn LEX |
| 2 | Đóng gói hàng hóa & gắn nhãn vận chuyển | ✓ |  |  | Hàng sẵn sàng cho AWB | Auto-print label |
| 3 | Đặt lịch hẹn lấy hàng từ 3PL | ✓ |  |  | Chủ động schedule pickup | Auto-schedule theo vị trí Seller |
| 4 | Gửi mã theo dõi vận chuyển cho Buyer |  | ✓ |  | Buyercần biết tracking | Auto-send qua app/SMS |
| 5 | Tạo vận đơn tự động (AWB) |  | ✓ |  | Bắt buộc cho tracking — không trực tiếp tạo giá trị | Giữ nguyên |
| 6 | Phân công 3PL phù hợp (LEX/GHN/J&T) |  | ✓ |  | Phân bổ hợp lý — tối ưu chi phí | AI phân bổ theo tuyến + chi phí |
| 7 | Tạo lô hàng vận chuyển trên hệ thống |  | ✓ |  | Gom lô cho line-haul | Giữ nguyên |
| 8 | 3PL nhận hàng từ kho Seller | ✓ |  |  | Hàng bắt đầu di chuyển trong mạng | Auto-confirm pickup |
| 9 | Phân loại hàng tại kho trung tâm 3PL |  | ✓ |  | Sort bắt buộc — Hold 2-6h, capacity 75% | AI sorting + automated Hub |
| 10 | Vận chuyển hàng qua các trung tâm phân loại | ✓ |  |  | Di chuyển hàng giữa Hub — core | Giữ nguyên |
| 11 | Hàng xuất kho — shipper nhận giao | ✓ |  |  | Out for delivery | Giữ nguyên |
| 12 | Shipper giao hàng cho Buyer tại địa chỉ | ✓ |  |  | Giao hàng cốt lõi — first attempt 75-80% | Slot hẹn giờ + gọi trước 15 phút |
| 13 | Hẹn giao lại lần tiếp theo |  |  | ✓ | NVA — giao lại lần 1 (20-25% đơn) | Giảm tối đa 2 lần + address verify |
| 14 | Buyer nhận hàng & kiểm tra tại chỗ | ✓ |  |  | Buyer verify chất lượng — giá trị | Giữ nguyên |
| 15 | Buyer xác nhận đã nhận hàng | ✓ |  |  | POD xác nhận giao thành công | Digital POD + chữ ký |
| 16 | Buyer từ chối nhận hàng (lý do) |  |  | ✓ | NVA — từ chối → reverse logistics | Ghi nhận lý do + giảm retry |
| 17 | Seller đóng gói lại hàng hóa theo yêu cầu |  |  | ✓ | NVA — repack sau hoàn về | Giảm return rate (8-12% → 4-7%) |
| 18 | Nhận hàng hoàn về từ 3PL (giao thất bại 3 lần) |  |  | ✓ | NVA — reverse logistics tốn kém | Giảm retry xuống 2 lần |
| 19 | Cập nhật trạng thái COD trên hệ thống |  | ✓ |  | COD tracking cho đối soát | Auto-update realtime |
| 20 | Chuyển hoàn hàng về kho Seller |  |  | ✓ | NVA — hoàn về gốc, chi phí cao nhất | Đánh giá trước khi hoàn |

**Tỷ lệ VA/BVA/NVA:**
- VA: 38% (theo trọng số thời gian — khớp Bảng 3.13.2)
- BVA: 32%
- NVA: 30%
  (Lưu ý: Bảng 3.13.2 báo cáo dùng tỷ trọng thời gian VA 38% / BVA 32% / NVA 30% — khác cơ sở đếm hoạt động: 9/20 (45%) / 6/20 (30%) / 5/20 (25%))

→ **Nhận xét:** NVA 30% là tỷ trọng cao nhất trong 10 quy trình, chủ yếu đến từ giao lại (hẹn giao lại lần tiếp theo), từ chối nhận hàng, repack và chuỗi hoàn về — chiếm ~20-25% đơn giao thất bại lần đầu. Chi phí NVA logistics là gánh nặng lớn nhất.

### B. Waste Analysis

| STT | Hoạt động | Move | Hold | Overdo | Mô tả | Thời gian chờ | Giải pháp |
|-----|-----------|------|------|--------|-------|---------------|-----------|
| 1 | Phân loại hàng tại kho trung tâm 3PL (sort) | | ✓ | | Hàng chờ sort 2-6 giờ, capacity utilization chỉ ~75% | 2-6 giờ | AI sorting + tăng capacity Hub |
| 2 | Hẹn giao lại lần tiếp theo (vắng nhà) | ✓ | ✓ | | Shipper di chuyển + chờ, giao lại 1-3 ngày | 1-3 ngày | Slot hẹn giờ + gọi trước |
| 3 | Buyer từ chối nhận hàng (lý do) | ✓ | ✓ | | Lặp lại thao tác giao + reverse | 2-5 ngày | SMS nhắc nhở + khung giờ hẹn |
| 4 | Nhận hàng hoàn về từ 3PL (giao thất bại 3 lần) | ✓ | ✓ | | Chi phí cao, xác suất thành công thấp | 3-7 ngày | Giảm xuống 2 lần + address verify |
| 5 | Seller đóng gói lại hàng hóa (repack) | ✓ | | | Hàng bị trả về phải đóng gói lại | 5-10 ngày | Giảm retry rate |
| 6 | Chuyển hoàn hàng về kho Seller | ✓ | ✓ | | Hàng quay về điểm gốc — lãng phí toàn tuyến | 7-15 ngày | Đánh giá trước khi hoàn |
| 7 | Shipper chờ Buyer (khi giao) | | ✓ | | Thời gian chờ không productive | 10-30 phút/lần | Gọi trước + hẹn giờ |

**Tổng lãng phí:** 7 hoạt động
- Move: 4 (57%)
- Hold: 6 (86%) — nhiều hoạt động có cả Hold và Move
- Overdo: 0 (0%)

→ **Hold time chiếm ưu thế** — sort Hub chờ 2-6h và giao lại nhiều lần là bottleneck chính. Chi phí mỗi lần giao lại ~15.000-25.000 VND nhiên liệu + nhân công.

### C. Root Cause Analysis — Fishbone (Ishikawa) 5 Cấp

```
Vấn đề: First-attempt delivery success rate chỉ ~75-80%, return rate 8-12%, average delivery time 3-7 ngày

Level 1 — Nguyên nhân lớn:
├── Con người (Man)
│   ├── Level 2: Shipper giao hàng không liên hệ được Buyer
│   │   ├── Level 3: Số điện thoại sai/không đúng hợp lệ
│   │   │   ├── Level 4: Buyer nhập sai SĐT khi đặt hàng
│   │   │   │   └── Level 5: Thiếu validation SĐT real-time ở checkout
│   │   └── Level 3: Shipper không gọi trước khi giao
│   │       ├── Level 4: Không có quy định gọi trước 15 phút
│   │           └── Level 5: SLA shipper chưa enforce gọi trước
├── Phương pháp (Method)
│   ├── Level 2: Giao lại tối đa 3 lần — quá nhiều lần giao
│   │   ├── Level 3: Mỗi lần giao lại cần 1-3 ngày chờ
│   │   │   ├── Level 4: Không có slot hẹn giờ cho Buyer chọn
│   │   │   │   └── Level 5: UX design chưa hỗ trợ hẹn giờ giao
│   │   └── Level 3: Không có khung giờ giao chính xác
│   │       ├── Level 4: Ước tính ETA không đủ chính xác
│   │       │   └── Level 5: Chưa dùng ML cho predictive ETA
│   ├── Level 2: Sort Hub thủ công / semi-automation
│   │   ├── Level 3: Warehouse sort time 2-6 giờ
│   │   │   ├── Level 4: Hub capacity utilization chỉ ~75%
│   │   │   │   └── Level 5: Thiếu AI routing cho phân loại Hub
│   │   └── Level 3: Hub capacity bottleneck vào giờ cao điểm
│   │       ├── Level 4: Peak season overload chưa dự báo
│   │           └── Level 5: Thiếu predictive capacity planning
├── Công nghệ (Technology)
│   ├── Level 2: GPS tracking chưa realtime ổn định
│   │   ├── Level 3: Cập nhật vị trí trễ 5-15 phút
│   │   │   ├── Level 4: 3PL chưa tích hợp GPS API đầy đủ
│   │   │   │   └── Level 5: Thiếu standardized GPS API contract cho 3PL
│   │   └── Level 3: ETA hiển thị không chính xác
│   │       ├── Level 4: ETA dựa trên distance thay vì ML model
│   │       │   └── Level 5: Chưa có traffic/weather data integration
│   └── Level 2: Thiếu drone delivery cho remote area
│       ├── Level 3: Province delivery time 5-7 ngày
│           ├── Level 4: Remote area giao hàng khó, đường xa
│               └── Level 5: Infrastructure logistics chưa phủ hết
├── Vật liệu (Material)
│   ├── Level 2: Địa chỉ giao hàng sai / không đầy đủ
│   │   ├── Level 3: Buyer nhập địa chỉ viết tắt
│   │   │   ├── Level 4: Không có address auto-fill từ GPS
│   │   │   │   └── Level 5: Chưa tích hợp Google Map API cho address validation
│   │   └── Level 3: Địa chỉ mới nhưng chưa cập nhật trên bản đồ
│   │       ├── Level 4: Khu vực mới phát triển, bản đồ cũ
│   │           └── Level 5: Geo-database chưa update thường xuyên
└── Máy móc (Machine)
    ├── Level 2: Xe vận chuyển capacity không tối ưu
    │   ├── Level 3: Lộ trình chưa tối ưu → tiêu hao nhiên liệu
    │   │   ├── Level 4: Chưa dùng AI route optimization
    │   │   │   └── Level 5: Thiếu real-time traffic data feed
    │   └── Level 3: Hub capacity utilization ~75%
    │       ├── Level 4: Máy sortbán tự động, throughput thấp
    │           └── Level 5: Chưa invest automated sorting system
    └── Level 2: Drone delivery chưa pilot
        ├── Level 3: Remote area delivery cost cao (~40,000 VND/kiện)
            ├── Level 4: Chi phí nhiên liệu + nhân công cao
                └── Level 5: Drone pilot chưa được regulatory approval đầy đủ
```

### 5-Why Analysis

**Vấn đề:** First-attempt delivery success rate chỉ ~75-80% (thấp hơn ngành 82-88%), gây ra chi phí giao lại (~15.000-25.000 VND/lần) và return rate 8-12%

| Level | Câu hỏi | Câu trả lời |
|-------|---------|-------------|
| Why 1 | Tại sao 20-25% đơn giao lần đầu thất bại? | Buyer vắng nhà, sai địa chỉ, hoặc không liên hệ được |
| Why 2 | Tại sao Buyer vắng nhà khi shipper giao? | Không có slot hẹn giờ, Buyer không biết khung giờ giao chính xác |
| Why 3 | Tại sao không có slot hẹn giờ? | ETA dự đoán chưa đủ chính xác (dựa trên distance, chưa dùng ML) |
| Why 4 | Tại sao ETA không chính xác? | Chưa tích hợp traffic/weather data + chưa dùng predictive ML model |
| Why 5 | Tại sao chưa dùng predictive ML? | Data historical delivery chưa được khai thác + chưa invest AI routing |

**Root Cause:** Thiếu hệ thống slot hẹn giờ + ETA dự đoán không chính xác do chưa dùng ML +_address validation chưa đủ tốt → 20-25% giao lại + 8-12% return rate = chi phí logistics lãng phí lớn.

## 3.9.4. Phân tích định lượng

### A. Thời gian

| STT | Hoạt động | Min | Max | Avg | Ghi chú |
|-----|-----------|-----|-----|-----|---------|
| 1 | Seller chuẩn bị hàng hóa đóng gói | 15 phút | 3 giờ | 30 phút | Theo loại hàng |
| 2 | Đóng gói hàng hóa & gắn nhãn vận chuyển | 10 phút | 1 giờ | 20 phút | Đóng gói + label |
| 3 | Đặt lịch hẹn lấy hàng từ 3PL | 5 phút | 30 phút | 10 phút | Online booking |
| 4 | Gửi mã theo dõi vận chuyển cho Buyer | 30 giây | 2 phút | 1 phút | Automated |
| 5 | Tạo vận đơn tự động (AWB) | 30 giây | 2 phút | 1 phút | Automated |
| 6 | Phân công 3PL phù hợp (LEX/GHN/J&T) | 1 phút | 5 phút | 3 phút | Automated |
| 7 | Tạo lô hàng vận chuyển trên hệ thống | 1 phút | 10 phút | 3 phút | Automated |
| 8 | 3PL nhận hàng từ kho Seller | 10 phút | 1 giờ | 20 phút | Pickup theo lịch |
| 9 | Phân loại hàng tại kho trung tâm 3PL | 2 giờ | 6 giờ | 4 giờ | Sort Hub capacity ~75% |
| 10 | Vận chuyển hàng qua các trung tâm phân loại | 4 giờ | 48 giờ | 18 giờ | Metro vs Province |
| 11 | Hàng xuất kho — shipper nhận giao | 30 phút | 2 giờ | 1 giờ | Phân cho shipper |
| 12 | Shipper giao hàng cho Buyer tại địa chỉ | 5 phút | 30 phút | 10 phút | Per attempt |
| 13 | Hẹn giao lại lần tiếp theo | 1 ngày | 3 ngày | 1.5 ngày | Chờ 1-3 ngày |
| 14 | Buyer nhận hàng & kiểm tra tại chỗ | 2 phút | 10 phút | 5 phút | Kiểm tra chất lượng |
| 15 | Buyer xác nhận đã nhận hàng | 1 phút | 5 phút | 2 phút | Digital POD |
| 16 | Buyer từ chối nhận hàng (lý do) | 2 phút | 10 phút | 5 phút | Khi hư hỏng/sai đơn |
| 17 | Seller đóng gói lại hàng hóa theo yêu cầu | 15 phút | 2 giờ | 45 phút | Repack sau hoàn về |
| 18 | Nhận hàng hoàn về từ 3PL (giao thất bại 3 lần) | 3 ngày | 7 ngày | 5 ngày | Reverse logistics |
| 19 | Cập nhật trạng thái COD trên hệ thống | 30 giây | 2 phút | 1 phút | Automated |
| 20 | Chuyển hoàn hàng về kho Seller | 5 ngày | 15 ngày | 10 ngày | Hoàn về gốc |

### B. Phân tích Cycle Time Probability-Weighted

| Hoạt động | Thời gian (phút) | Xác suất | Thời gian kỳ vọng (phút) | Ghi chú |
|-----------|-------------------|----------|--------------------------|---------|
| Seller chuẩn bị hàng hóa đóng gói | 30 | 100% | 30.0 | Bắt buộc |
| Đóng gói hàng hóa & gắn nhãn vận chuyển | 20 | 100% | 20.0 | Bắt buộc |
| Đặt lịch hẹn lấy hàng từ 3PL | 10 | 100% | 10.0 | Online booking |
| Gửi mã theo dõi vận chuyển cho Buyer | 1 | 100% | 1.0 | Automated |
| Tạo vận đơn tự động (AWB) | 1 | 100% | 1.0 | Automated |
| Phân công 3PL phù hợp | 3 | 100% | 3.0 | Automated |
| Tạo lô hàng vận chuyển trên hệ thống | 3 | 100% | 3.0 | Automated |
| 3PL nhận hàng từ kho Seller | 20 | 100% | 20.0 | Bắt buộc (LEX 60%) |
| Phân loại hàng tại kho trung tâm 3PL | 240 (4h avg) | 100% | 240.0 | Sort 2-6h |
| Vận chuyển hàng qua các trung tâm phân loại | 1,080 (18h avg) | 100% | 1,080.0 | Metro: 8h, Province: 36h |
| Hàng xuất kho — shipper nhận giao | 60 | 100% | 60.0 | Phân cho shipper |
| Shipper giao hàng cho Buyer tại địa chỉ | 10 | 75-80% | 7.8 | 75-80% giao thành công lần đầu |
| Hẹn giao lại lần tiếp theo | 2,160 (1.5 ngày) | 20-25% | 486.0 | 20-25% cần giao lại lần 1 |
| Buyer nhận hàng & kiểm tra tại chỗ | 5 | 75-80% | 3.9 | 75-80% nhận thành công |
| Buyer xác nhận đã nhận hàng | 2 | 75-80% | 1.6 | 75-80% POD |
| Buyer từ chối nhận hàng (lý do) | 5 | 8% | 0.4 | 8-12% từ chối/hoàn |
| Seller đóng gói lại hàng hóa theo yêu cầu | 45 | 5% | 2.25 | Repack sau hoàn về |
| Nhận hàng hoàn về từ 3PL (giao thất bại 3 lần) | 7,200 (5 ngày) | 3% | 216.0 | 3% hàng hoàn |
| Cập nhật trạng thái COD trên hệ thống | 1 | 45% | 0.45 | 45% COD |
| Chuyển hoàn hàng về kho Seller | 14,400 (10 ngày) | 2% | 288.0 | 2% hoàn về Seller |

**Tổng Cycle Time kỳ vọng (từ đóng gói đến giao thành công) = 1,468 phút ≈ 24.5 giờ ≈ 1.0 ngày (metro)**
**Tổng Cycle Time bao gồm giao lại & hoàn về = ~2,474 phút ≈ 41.2 giờ ≈ 1.7 ngày (metro)**
**Trường hợp Province + giao lại: Cycle Time lên đến 5-7 ngày; báo cáo tổng hợp (Bảng 3.13.2) khớp khoảng 75-80% giao thành công lần đầu**

### C. Chi phí (per parcel)

| STT | Thành phần | Chi phí (VND) | Ghi chú |
|-----|-----------|---------------|---------|
| 1 | Lấy hàng (pickup) | 3,000 | Phí pickup tại kho Seller |
| 2 | Sort Hub / Phân loại | 2,000 | Phân bổ overhead Hub |
| 3 | Vận chuyển trung chuyển (line-haul) | 5,000 | Metro; province: 8,000-12,000 |
| 4 | Giao hàng cuối (last-mile delivery) | 8,000 | Metro; province: 12,000-15,000 |
| 5 | COD thu hộ (nếu COD) | 1,500 | ~45% đơn COD × 1.5% |
| 6 | Chi phí giao lại (15% × 20,000 VND) | 3,000 | ~20-25% đơn cần giao lại lần đầu; 15% là trọng số chi phí bình quân |
| 7 | Chi phí hàng hoàn (3% × 15,000 VND) | 450 | Reverse logistics |
| 8 | Insurance / Bảo hiểm kiện hàng | 500 | ~2% risk premium |
| **TỔNG (Metro)** | | **~25,000 VND** | Làm tròn từ 23,450 — dùng làm chi phí bình quân đơn vị |
| **TỔNG (Province)** | | **40,000 VND** | Roughly matching benchmark |

**Volume ước tính:** ~400.000 kiện hàng/ngày = ~12 triệu kiện/tháng (Lazada VN ~20 triệu đơn/tháng, ~60% qua logistics LEX/3PL)
**Monthly logistics cost (metro):** ~8.400.000 × 25,000 = **210 tỷ VND/tháng**
**Monthly logistics cost (province):** ~3.600.000 × 40,000 = **144 tỷ VND/tháng**
**Tổng monthly logistics cost: ~354 tỷ VND/tháng**

### D. Chất lượng

| Metric | Current | Benchmark (VN e-commerce) | Gap |
|--------|---------|---------------------------|-----|
| First-attempt delivery success rate | 75-80% | 92% (TO-BE mục tiêu) | -12-17 điểm % |
| Average delivery time (metro) | 3-5 ngày | 1-2 ngày | +1-3 ngày |
| Average delivery time (province) | 5-7 ngày | 3-5 ngày | +2 ngày |
| Return/re-delivery rate | 8-12% | 5-8% | +3-4% |
| Hub sort time | 2-6 giờ | 1-3 giờ | +1-3 giờ |
| Hub capacity utilization | 75% | 85% | -10% |
| Tracking accuracy (realtime) | ~90% | 98% | -8% |
| COD collection rate | 95% | 98% | -3% |
| Average cost per parcel (metro) | ~23,450 VND | 20,000 VND | +3,450 VND |
| Average cost per parcel (province) | ~40,000 VND | 30,000-35,000 VND | +5,000-10,000 VND |

## 3.9.5. Phân tích Pareto

### Bảng Vấn đề — Giả thuyết — Chi phí ảnh hưởng

| STT | Vấn đề | Giả thuyết | Chi phí ảnh hưởng/tháng (VND) | Tỷ trọng |
|-----|--------|-----------|-------------------------------|----------|
| 1 | Giao lại nhiều lần (20-25% đơn cần retry, avg 2-3 lần) | Không có slot hẹn giờ + ETA không chính xác + shipper không gọi trước | 85,000,000,000 (chi phí retry: nhiên liệu, nhân công, thời gian — khớp Mục 3.13.1) | 24.0% |
| 2 | Return/hoàn về kho (8-12% đơn) | Địa chỉ sai + Buyer vắng nhà + giao thất bại 3 lần | 90,000,000,000 (reverse logistics + mất giá trị hàng) | 25.4% |
| 3 | Sort Hub inefficiency (2-6h, capacity 75%) | Semi-automation + peak season overload chưa dự báo | 55,000,000,000 (chậm trễ + overhead Hub — khớp Mục 3.13.1) | 15.5% |
| 4 | Tracking không realtime (90% vs 98%) | 3PL chưa tích hợp GPS API đầy đủ | 40,500,000,000 (CS handle tracking queries + mất niềm tin Buyer) | 11.4% |
| 5 | Chi phí last-mile cao (province 40k vs benchmark 30-35k) | Route chưa tối ưu + remote area infrastructure | 83,500,000,000 (transit delay + phí vận chuyển vượt benchmark; trong đó thành phần transit delay 40 tỷ — FINAL §3.13.2) | 23.6% |
| **TỔNG** | | | **354,000,000,000** | **100%** |

### Kết luận 80/20

**Top 3 vấn đề (chiếm ~65% chi phí):**
1. Giao lại nhiều lần (24.0%) — giải pháp: slot hẹn giờ + predictive ETA ML + shipper gọi trước 15 phút
2. Return/hoàn về kho (25.4%) — giải pháp: address validation realtime + giảm retry xuống tối đa 2 lần + GPS pickup verification
3. Chi phí last-mile cao / transit delay (23.6%) — giải pháp: AI Route Optimization + xử lý trước nguyên nhân giao lại + smart Hub sorting

→ **Giải quyết các vấn đề này sẽ giảm phần lớn chi phí lãng phí (~50-60 tỷ VND/tháng, ước tính từ top-3 cải tiến liên quan trong Bảng TO-BE: Route Optimization, Predictive ETA, Smart Hub Sorting). Chi phí giao lại + hoàn về (85 + 90 tỷ) gần bằng mức giảm net -89 tỷ của kịch bản TO-BE tổng thể.**

## 3.9.6. Kết luận và hướng cải tiến TO-BE

### Tóm tắt AS-IS
- Cycle time metro: 3-5 ngày, province: 5-7 ngày
- First-attempt delivery success: ~75-80%
- Return rate: 8-12%
- Chi phí per parcel: ~23,450 VND (metro, ≈ 25,000 làm tròn), ~40,000 VND (province)
- Bottleneck: Giao lại nhiều lần + Sort Hub inefficiency + ETA không chính xác
- LEX xử lý ~60%, 3PL ~40%

### Hướng cải tiến TO-BE

| STT | Cải tiến | Mục tiêu | Giảm chi phí (tháng) |
|-----|---------|----------|----------------------|
| 1 | **AI Route Optimization** — Tối ưu tuyến đường shipper realtime dựa trên traffic, khoảng cách, ưu tiên giao | First-attempt success: 75-80% → 92%; Chi phí last-mile giảm 15% | -30 tỷ VND |
| 2 | **Real-time GPS Tracking** — Integrated GPS API cho tất cả LEX/3PL, hiển thị vị trí realtime cho Buyer | Tracking accuracy: 90% → 98%; Giảm CS queries 40% | -15 tỷ VND |
| 3 | **Drone Delivery Pilot** — Thử nghiệm giao hàng bằng drone cho remote area / province xa | Province delivery: 5-7 ngày → 3-4 ngày cho khu vực phù hợp | -5 tỷ VND (long-term) |
| 4 | **Automated Pickup Scheduling** — Tự động lịch pickup theo vị trí Seller + capacity LEX/3PL | Pickup time: 30 phút → 15 phút avg | -8 tỷ VND |
| 5 | **Predictive ETA using ML** — Machine learning model dự đoán ETA chính xác dựa trên historical data + traffic + weather | ETA accuracy: ±1 ngày → ±3 giờ; Buyer biết chính xác giờ giao | -25 tỷ VND |
| 6 | **Smart Hub Sorting** — Automated sorting tại Hub + AI phân loại theo tuyến giao | Sort time: 2-6 giờ → 1-2 giờ; Capacity: 75% → 90% | -25 tỷ VND |
| **TỔNG GIẢM (riêng lẻ, chồng lấn — không cộng dồn)** | | | **-108 tỷ VND/tháng** |

> **Lưu ý:** Các con số giảm ở trên tính theo từng sáng kiến riêng lẻ nên có chồng lấn; không cộng dồn thành tổng net. Kịch bản TO-BE kết hợp (so sánh AS-IS vs TO-BE bên dưới) cho mức giảm net ~-89 tỷ VND/tháng (-24%, từ 369 tỷ xuống 280 tỷ theo cách định nghĩa của Báo cáo tổng hợp).

### So sánh AS-IS vs TO-BE

| Metric | AS-IS | TO-BE | Cải thiện |
|--------|-------|-------|-----------|
| First-attempt delivery success | 75-80% | 92% | +12-17 điểm % |
| Average delivery time (metro) | 3-5 ngày | 1-2 ngày | -50% |
| Average delivery time (province) | 5-7 ngày | 3-5 ngày | -30% |
| Return/re-delivery rate | 8-12% | 4-7% | -40% |
| Hub sort time | 2-6 giờ | 1-2 giờ | -60% |
| Hub capacity utilization | 75% | 90% | +15% |
| Tracking accuracy (realtime) | 90% | 98% | +8% |
| Average cost per parcel (metro) | ~23,450 VND | ~18,000 VND | -23% |
| Average cost per parcel (province) | ~40,000 VND | ~30,000 VND | -25% |
| Monthly logistics cost (chi tiết tự tính) | 354 tỷ VND | 246 tỷ VND | -108 tỷ VND net (-31%) |

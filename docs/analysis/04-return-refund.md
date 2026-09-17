# 3.4. Quy trình Hoàn trả & Hoàn tiền (Return & Refund)

## 3.4.1. Mô tả quy trình

**Phạm vi:** Bắt đầu từ khi Buyer khởi tạo yêu cầu hoàn trả → Kiểm tra tính hợp lệ → Tải bằng chứng → AI phân loại → CS thẩm định → Lấy hàng hoàn → Kiểm định kho → Kích hoạt lệnh hoàn tiền → Hoàn tiền hoàn tất / Yêu cầu bị từ chối.

**Các tác nhân tham gia:**
- **Buyer:** Người mua — gửi yêu cầu đổi trả, tải bằng chứng, bàn giao hàng trả
- **Lazada System (Automated):** Kiểm tra tính hợp lệ, AI phân loại, gửi thông báo, đặt lịch pickup
- **CS Agent:** Thẩm định hồ sơ khiếu nại, phê duyệt/ từ chối
- **3PL/Warehouse:** LEX/3PL pickup hàng trả, kiểm định hàng hoàn tại kho
- **Payment Gateway:** Kích hoạt lệnh hoàn tiền

**Kết quả có thể xảy ra:**
- Hoàn tiền hoàn tất — buyer nhận lại tiền (hoàn về phương thức gốc hoặc credit/ví)
- Yêu cầu bị từ chối — không hợp lệ, bằng chứng không đạt, hoặc hàng hoàn sai hiện trạng
- Refund nhanh (Instant Refund) — đơn giá trị <200k & buyer tín nhiệm cao, hoàn tiền trước khi nhận hàng về

### SiPOC

| SiPOC | Chi tiết |
|-------|----------|
| **Supplier** | Buyer (yêu cầu + bằng chứng + hàng trả), LEX/3PL (pickup + vận chuyển ngược), Warehouse (kiểm định) |
| **Input** | Yêu cầu đổi trả, lý do, bằng chứng ảnh/video, hàng hoàn trả |
| **Process** | Gửi yêu cầu → Kiểm tra hợp lệ → Upload bằng chứng → AI phân loại → CS thẩm định → Pickup → Kiểm định kho → Kích hoạt hoàn tiền → Hoàn tiền |
| **Output** | Hoàn tiền hoàn tất (đủ/phần), Yêu cầu bị từ chối, Refund nhanh |
| **Customer** | Buyer (được hoàn tiền đúng hạn), Seller (nhận hàng hoàn/hòa giải công bằng) |

## 3.4.2. Mô hình BPMN

*(File: `processes/04-return-refund.bpmn`)*

**Thống kê mô hình:**
- Số lanes: 5 (Buyer, Lazada System (Automated), CS Agent, 3PL/Warehouse, Payment Gateway)
- Số activities: 13 (6 userTask + 6 serviceTask + 1 task)
- Số gateways: 18 (XOR)
- End events: 2
- Độ phức tạp: High

## 3.4.3. Phân tích định tính

### A. Value-Added Analysis

| STT | Hoạt động (tên từ BPMN) | VA | BVA | NVA | Giải thích | Đề xuất TO-BE |
|-----|--------------------------|----|-----|-----|------------|---------------|
| 1 | Gửi yêu cầu đổi trả và lý do | ✓ |  |  | Nhu cầu chính đáng của KH | Guided form + lý do chuẩn hóa |
| 2 | Tải lên bằng chứng ảnh và video | ✓ |  |  | Bằng chứng cần thiết cho quyết định | Checklist guided + AI quality check |
| 3 | Xử lý yêu cầu trễ hạn |  | ✓ |  | Xử lý ngoại lệ khi KH bỏ lỡ deadline | Auto-extend 1 lần, nhắc reminder |
| 4 | Bàn giao hàng trả cho LEX / 3PL | ✓ |  |  | Bắt đầu logistics ngược | Drop-off point + QR code |
| 5 | CS thẩm định hồ sơ khiếu nại |  | ✓ |  | Cần cho fair decision — Hold lớn | **AI triage evidence** + CS chỉ review ngoại lệ |
| 6 | Kiểm định hàng hoàn tại kho (≤12h) |  |  | ✓ | Inspection thủ công tại kho — waste (bỏ qua khi return-less <200k) | **Return-less refund** low-risk + AI image analysis |
| 7 | Kiểm tra tính hợp lệ tự động |  | ✓ |  | Lọc yêu cầu không hợp lệ — chống lạm dụng | Auto instant; mở rộng luật |
| 8 | AI phân loại bằng chứng khiếu nại |  | ✓ |  | Phân loại nhanh — rút ngắn thời gian xử lý | Mở rộng auto-approve path |
| 9 | Gửi thông báo cập nhật tiến độ tự động | ✓ |  |  | KH theo dõi trạng thái — minh bạch | Giữ nguyên (auto) |
| 10 | Đặt lịch hẹn Shipper đến lấy hàng hoàn | ✓ |  |  | Lên lịch pickup — giảm Hold | Smart scheduling + drop-off point |
| 11 | Đặt lại lịch pickup |  | ✓ |  | Xử lý ngoại lệ (KH bận) | Tự động đề xuất 3 slot kế tiếp |
| 12 | Kích hoạt lệnh hoàn tiền |  |  | ✓ | Hoàn tiền thủ công sau khi đã duyệt — waste (nhiều bước click) | Auto-execute refund qua payment gateway |
| 13 | LEX / 3PL pickup hàng trả | ✓ |  |  | Vận chuyển hàng trả — logistics ngược | Scheduled pickup slot (giảm Hold 4-24h) |

**Tỷ lệ VA/BVA/NVA:**
- VA: 6/13 (46%)
- BVA: 5/13 (39%)
- NVA: 2/13 (15%)

→ **Nhận xét:** VA cao (46%) — quy trình hoàn trả có nhiều hoạt động tạo giá trị trực tiếp. NVA 15% từ kiểm định hàng hoàn tại kho và kích hoạt lệnh hoàn tiền thủ công.

### B. Waste Analysis

| STT | Hoạt động | Move | Hold | Overdo | Mô tả | Thời gian chờ | Giải pháp |
|-----|-----------|------|------|--------|-------|---------------|-----------|
| 1 | CS thẩm định hồ sơ khiếu nại | ✓ | | | CS phải đọc manual bằng chứng | 30 phút-4h | AI tóm tắt + highlight |
| 2 | LEX / 3PL pickup hàng trả | | ✓ | | Buyer phải chờ pickup theo lịch | 1-2 ngày | Tối ưu slot + drop-off option |
| 3 | Đặt lại lịch pickup | | ✓ | | Pickup thất bại → delay thêm 1-2 ngày | 1-3 ngày | Nhắc trước + đổi khung giờ linh hoạt |
| 4 | Kiểm định hàng hoàn tại kho (≤12h) | ✓ | | | Nhân viên kho kiểm tra manual | 4-12h | AI image classification hỗ trợ |
| 5 | Kích hoạt lệnh hoàn tiền thủ công | ✓ | | | CS phải bấm nhiều bước để hoàn tiền | 1-6h | Auto-execute khi kiểm định pass |

**Tổng lãng phí:** 5 hoạt động
- Move: 3 (60%)
- Hold: 2 (40%)
- Overdo: 0 (0%)

→ **Move waste chiếm 60%** — reverse logistics và thẩm định thủ công là các điểm kém hiệu quả chính.

### C. Root Cause Analysis — Fishbone (Ishikawa) 5 Cấp

```
Vấn đề: Thời gian hoàn tiền trung bình 8,5 ngày (chậm so với benchmark 2-3 ngày)

Level 1 — Nguyên nhân lớn:
├── Con người (Man)
│   ├── Level 2: Nhân viên kho kiểm định chậm
│   │   ├── Level 3: Mỗi kiện phải kiểm tra manual từng mục
│   │   │   ├── Level 4: Không có AI hỗ trợ so sánh ảnh
│   │   │   │   └── Level 5: Warehouse tooling chưa được đầu tư
│   │   └── Level 3: CS review hồ sơ manual
│   │       ├── Level 4: Bằng chứng không structured
│   │       │   └── Level 5: Thiếu guided upload + AI summarization
├── Quy trình (Process)
│   ├── Level 2: Pickup thất bại phải đặt lại
│   │   ├── Level 3: Buyer không có mặt đúng giờ
│   │   │   ├── Level 4: Không có khung giờ linh hoạt
│   │   │   │   └── Level 5: Logistics scheduling chưa customer-centric
│   │   └── Level 3: Reverse logistics 1-2 ngày vận chuyển
│   │       ├── Level 4: Không có drop-off network rộng
│   │       │   └── Level 5: Chi phí đầu tư điểm trả hàng chưa đủ
├── Công nghệ (Technology)
│   ├── Level 2: Chưa có Instant Refund rộng rãi
│   │   ├── Level 3: Chỉ áp dụng <200k & buyer tín nhiệm cao
│   │   │   ├── Level 4: Sợ rủi ro fraud khi hoàn tiền trước
│   │   │   │   └── Level 5: Risk model chưa đủ tự tin cho limit cao hơn
│   │   └── Level 3: Hoàn tiền về thẻ 5-15 ngày
│   │       ├── Level 4: Phụ thuộc chu kỳ bank/gateway
│   │       │   └── Level 5: Không có credit/instant wallet cho mọi trường hợp
└── Vật liệu (Material)
    ├── Level 2: Hàng hoàn sai hiện trạng
    │   ├── Level 3: Buyer gửi hàng không đúng mô tả
    │   │   ├── Level 4: Thiếu checklist kiểm định chuẩn
    │   │   │   └── Level 5: Không có image baseline từ lúc bán
    │   └── Level 3: Thiếu phụ kiện/bao bì
    │       ├── Level 4: Buyer không biết yêu cầu đóng gói
    │       │   └── Level 5: Thiếu hướng dẫn return packaging
```

### 5-Why Analysis

**Vấn đề:** Thời gian hoàn tiền trung bình 8,5 ngày

| Level | Câu hỏi | Câu trả lời |
|-------|---------|-------------|
| Why 1 | Tại sao hoàn tiền mất 8,5 ngày? | Phải chờ pickup, vận chuyển ngược, kiểm định kho, rồi mới hoàn tiền |
| Why 2 | Tại sao phải chờ kiểm định kho? | Phải xác nhận hàng về đúng hiện trạng mới dám hoàn tiền |
| Why 3 | Tại sao kiểm định chậm? | Nhân viên kho kiểm tra manual, không có AI hỗ trợ |
| Why 4 | Tại sao không có AI hỗ trợ? | Warehouse tooling chưa đầu tư image comparison |
| Why 5 | Tại sao chưa đầu tư? | Chi phí đầu tư cao + chưa ưu tiên so với các dự án khác |

**Root Cause:** Chưa có Instant Refund rộng rãi cho low-risk + warehouse inspection chưa AI hóa + reverse logistics chưa tối ưu.

## 3.4.4. Phân tích định lượng

### A. Thời gian

| STT | Hoạt động | Min | Max | Avg | Ghi chú |
|-----|-----------|-----|-----|-----|---------|
| 1 | Gửi yêu cầu đổi trả và lý do | 3 phút | 15 phút | 5 phút | Buyer |
| 2 | Xử lý yêu cầu trễ hạn | 5 phút | 30 phút | 10 phút | ~5% yêu cầu |
| 3 | Kiểm tra tính hợp lệ tự động | 3 giây | 30 giây | 10 giây | Automated |
| 4 | Tải lên bằng chứng ảnh và video | 2 phút | 15 phút | 5 phút | Buyer |
| 5 | AI phân loại bằng chứng khiếu nại | 3 giây | 15 giây | 5 giây | Automated |
| 6 | CS thẩm định hồ sơ khiếu nại | 20 phút | 3 giờ | 45 phút | Per case |
| 7 | Đặt lịch hẹn Shipper đến lấy hàng hoàn | 1 phút | 30 phút | 5 phút | Automated |
| 8 | Bàn giao hàng trả cho LEX / 3PL | 5 phút | 30 phút | 10 phút | Buyer |
| 9 | LEX / 3PL pickup hàng trả | 1 ngày | 3 ngày | 2 ngày | Theo lịch |
| 10 | Đặt lại lịch pickup | 1 ngày | 3 ngày | 1.5 ngày | 10% pickup thất bại |
| 11 | Kiểm định hàng hoàn tại kho (≤12h) | 4 giờ | 12 giờ | 8 giờ | SLA 12h |
| 12 | Kích hoạt lệnh hoàn tiền | 1 giờ | 24 giờ | 6 giờ | Manual |
| 13 | Gửi thông báo cập nhật tiến độ tự động | 1 phút | 5 phút | 2 phút | Automated |

### B. Phân tích Cycle Time Probability-Weighted

| Hoạt động | Thời gian (phút) | Xác suất | Thời gian kỳ vọng (phút) | Ghi chú |
|-----------|-------------------|----------|--------------------------|---------|
| Gửi yêu cầu đổi trả và lý do | 5 | 100% | 5.0 | Bắt buộc |
| Xử lý yêu cầu trễ hạn | 10 | 5% | 0.5 | Chỉ khi trễ hạn |
| Kiểm tra tính hợp lệ tự động | 0.17 | 100% | 0.17 | Tức thì |
| Tải lên bằng chứng ảnh và video | 5 | 100% | 5.0 | Bắt buộc |
| AI phân loại bằng chứng khiếu nại | 0.08 | 100% | 0.08 | Tức thì |
| CS thẩm định hồ sơ khiếu nại | 45 | 100% | 45.0 | Core |
| Đặt lịch hẹn Shipper đến lấy hàng hoàn | 5 | 80% | 4.0 | 20% instant refund không cần |
| Bàn giao hàng trả cho LEX / 3PL | 10 | 80% | 8.0 | 20% instant refund |
| LEX / 3PL pickup hàng trả | 2,880 (2 ngày) | 80% | 2,304.0 | 80% cần pickup |
| Đặt lại lịch pickup | 2,160 (1.5 ngày) | 8% | 172.8 | 10% pickup thất bại × 80% |
| Kiểm định hàng hoàn tại kho (≤12h) | 480 (8h) | 80% | 384.0 | 80% cần kiểm định |
| Kích hoạt lệnh hoàn tiền | 360 (6h) | 100% | 360.0 | Manual |
| Gửi thông báo cập nhật tiến độ tự động | 2 | 100% | 2.0 | Automated |

**Tổng Cycle Time kỳ vọng = 3,291 phút ≈ 55 giờ ≈ 6.9 ngày làm việc**
*(Instant refund case: ~57 phút; Full return case: ~4,009 phút ≈ 66,8 giờ ≈ 8,3 ngày làm việc)*

### C. Chi phí (per return/refund)

| STT | Thành phần | Chi phí (VND) | Ghi chú |
|-----|-----------|---------------|---------|
| 1 | CS agent time (CS Staff cost) | 52,000 | Chi phí xử lý thủ công/ca (Bảng 3.9) |
| 2 | Reverse logistics (pickup + vận chuyển ngược) | 30,000 | Trung bình phí ship ngược nội địa |
| 3 | Warehouse inspection | 15,000 | 8h inspection allocated per kiện |
| 4 | Payment processing / refund fee | 2,000 | Gateway fee |
| 5 | Hàng tồn kho hư hao (10% không bán lại được) | 10,000 | 10% × AOV 100,000 VND |
| **TỔNG** | | **109,000 VNĐ** | Per return/refund (CS Staff 52.000 đồng Bảng 3.9 + logistics + kiểm định) |

**Volume ước tính:** ~5-6% total orders → ~1.1 triệu returns/month
**Monthly cost:** ~120 tỷ VND/tháng (109.000 VNĐ × ~1,1 triệu returns/tháng)

### D. Chất lượng

| Metric | Current | Benchmark (VN e-commerce) | Gap |
|--------|---------|---------------------------|-----|
| Avg refund time | 8,5 ngày | 2-3 ngày | +5,5-6,5 ngày |
| Instant refund rate | 15% | 40-50% | -25-35% |
| Pickup success rate (first attempt) | 90% | 95% | -5% |
| Inspection SLA compliance | 80% | 95% | -15% |
| Refund to original method | 70% | 85% | -15% |
| Buyer satisfaction (return experience) | 3,2/5 | 4,5/5 | -1,3 |

## 3.4.5. Phân tích Pareto

### Bảng Vấn đề — Giả thuyết — Chi phí ảnh hưởng

| STT | Vấn đề | Giả thuyết | Chi phí ảnh hưởng/tháng (VND) | Tỷ trọng |
|-----|--------|-----------|-------------------------------|----------|
| 1 | Instant refund rate thấp 15% | Risk model quá thận trọng, chỉ mở <200k | 35,000,000,000 (buyer wait cost + CS churn) | 33.6% |
| 2 | Pickup thất bại → đặt lại lịch | Thiếu slot linh hoạt + nhắc trước | 28,000,000,000 (logistics rework) | 26.9% |
| 3 | Warehouse inspection chậm manual | Thiếu AI image classification | 22,000,000,000 (kho labor cost) | 21.2% |
| 4 | Refund về thẻ 5-15 ngày | Phụ thuộc bank/gateway cycle | 12,000,000,000 (cash flow + CS) | 11.5% |
| 5 | CS review hồ sơ manual | Bằng chứng không structured | 7,000,000,000 (CS labor) | 6.7% |
| **TỔNG** | | | **120,000,000,000** | **100%** |

### Kết luận 80/20

**Top 3 vấn đề (chiếm ~82% chi phí):**
1. Instant refund rate thấp (33.6%) — giải pháp: mở rộng risk-based instant refund lên limit cao hơn
2. Pickup thất bại (26.9%) — giải pháp: slot linh hoạt + nhắc trước + drop-off network
3. Warehouse inspection chậm (21.2%) — giải pháp: AI image classification hỗ trợ

→ **Giải quyết 3 vấn đề này sẽ giảm ~82% chi phí lãng phí (~101 tỷ VND/tháng).**

## 3.4.6. Kết luận và hướng cải tiến TO-BE

### Tóm tắt AS-IS
- Cycle time kỳ vọng: ~6.9 ngày; Avg CT theo report: 8,5 ngày (full return ~8,3 ngày làm việc)
- Chi phí per return: ~109,000 VNĐ (CS Staff 52.000 Bảng 3.9 + logistics + kiểm định)
- Instant refund rate: chỉ 15%
- Bottleneck: Pickup + kiểm định kho + refund thủ công

### Hướng cải tiến TO-BE

| STT | Cải tiến | Mục tiêu | Giảm chi phí (tháng) |
|-----|---------|----------|----------------------|
| 1 | Mở rộng risk-based instant refund (limit 500k, buyer tốt) | Instant refund: 15% → 45% | -35 tỷ VND |
| 2 | Slot pickup linh hoạt + nhắc trước + drop-off network | Pickup fail: 10% → 4% | -28 tỷ VND |
| 3 | AI image classification hỗ trợ kiểm định kho | Inspection: 8h → 2h | -22 tỷ VND |
| 4 | Đẩy mạnh hoàn tiền về Lazada Wallet/credit | Refund nhanh: 70% → 90% | -12 tỷ VND |
| 5 | Guided evidence upload + AI summarization | CS review: 45 phút → 15 phút | -7 tỷ VND |
| **TỔNG GIẢM** | | | **-70,5 tỷ VND/tháng** |

### So sánh AS-IS vs TO-BE

| Metric | AS-IS | TO-BE | Cải thiện |
|--------|-------|-------|-----------|
| Avg refund time | 8,5 ngày | 1,8 ngày | -78,8% |
| Instant refund rate | 15% | 45% | +30% |
| Pickup success (first attempt) | 90% | 96% | +6% |
| Inspection time | 8h | 2h | -75% |
| Chi phí per return | 109,000 VNĐ | 45,000 VNĐ | -59% |
| Monthly cost | 120 tỷ VND | 49,5 tỷ VND | -70,5 tỷ VND (-59%) |

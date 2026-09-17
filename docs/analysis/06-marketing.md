# 3.6. Quy trình Marketing & Khuyến mãi (Campaign & Promotion)

## 3.6.1. Mô tả quy trình

**Phạm vi:** Bắt đầu từ khi ý tưởng chiến dịch được đề xuất → Nghiên cứu thị trường → Thiết kế concept → Kiểm tra tuân thủ pháp lý (Nghị định 81) → Thẩm định ngân sách → Mời Seller tham gia → Cấu hình chiến dịch → Kiểm thử voucher → QA → Kích hoạt → Theo dõi hiệu năng → Báo cáo ROI.

**Các tác nhân tham gia:**
- **Marketing Team:** Nghiên cứu, thiết kế concept, theo dõi hiệu năng, báo cáo
- **Approval (Compliance/Budget):** Kiểm tra tuân thủ, thẩm định ngân sách; phê duyệt: Trưởng bộ phận (dưới 100 triệu) / CMO-CFO (trên 100 triệu)
- **Lazada System:** Gửi lời mời Seller, cấu hình chiến dịch, test voucher, QA, launch, báo cáo
- **Sellers:** Xem xét thư mời, xác nhận tham gia, chuẩn bị tồn kho & giá
- **Buyers:** Truy cập săn deal, thanh toán áp voucher

**Kết quả có thể xảy ra:**
- Chiến dịch kết thúc thành công — hoàn thành vòng đời campaign + báo cáo ROI
- Seller đồng ý / không đồng ý tham gia
- Launch thành công — campaign kích hoạt, buyer mua hàng, seller chuẩn bị xong

### SiPOC

| SiPOC | Chi tiết |
|-------|----------|
| **Supplier** | Marketing Team (ý tưởng), Finance (ngân sách), Legal (tuân thủ), Sellers (hàng hóa/giá), System (công cụ) |
| **Input** | Ý tưởng chiến dịch, ngân sách, đối tượng mục tiêu, thư mời Seller |
| **Process** | Nghiên cứu → Thiết kế → Compliance check → Budget review → Mời Seller → Config campaign → Test voucher → QA → Launch → Monitor → Report ROI |
| **Output** | Chiến dịch kết thúc thành công (GMV đạt), Campaign launched, Báo cáo ROI |
| **Customer** | Buyer (deal tốt), Seller (doanh số), Lazada (GMV + thị phần) |

## 3.6.2. Mô hình BPMN

*(File: `processes/06-marketing.bpmn`)*

**Thống kê mô hình:**
- Số lanes: 5 (Marketing Team, Approval, Lazada System, Sellers, Buyers)
- Số activities: 21 (13 userTask + 8 serviceTask)
- Số gateways: 15 (XOR)
- End events: 1
- Độ phức tạp: High

## 3.6.3. Phân tích định tính

### A. Value-Added Analysis

| STT | Hoạt động (tên từ BPMN) | VA | BVA | NVA | Giải thích | Đề xuất TO-BE |
|-----|--------------------------|----|-----|-----|------------|---------------|
| 1 | Nghiên cứu thị trường & lập bản đề xuất | ✓ |  |  | Tạo insight — nền tảng campaign | Data-driven research + AI phân bổ ngân sách |
| 2 | Phân khúc lại nhóm đối tượng mục tiêu | ✓ |  |  | Chọn đúng đối tượng — tăng hiệu quả ngân sách | Auto-segment từ dữ liệu |
| 3 | Thiết kế concept & lập kế hoạch chi tiết | ✓ |  |  | Sáng tạo cốt lõi | A/B test concept |
| 4 | Theo dõi hiệu năng hệ thống & doanh số realtime |  | ✓ |  | Giám sát — kiểm soát mid-flight | Real-time ROAS dashboard |
| 5 | Lập báo cáo tổng kết & đánh giá ROI |  | ✓ |  | Đo lường hiệu quả — kiểm soát post-campaign | Template chuẩn hóa + ML insight |
| 6 | Kiểm tra tính tuân thủ pháp lý khuyến mãi (Nghị định 81) |  | ✓ |  | Tuân thủ pháp lý — tránh sai sót pháp lý | Auto-compliance check |
| 7 | Thẩm định ngân sách & tỷ suất ROI |  | ✓ |  | Kiểm soát chi tiêu — governance | Budget real-time dashboard |
| 8 | Phê duyệt ngân sách (Trưởng bộ phận <100M / CMO-CFO >100M) |  | ✓ |  | Governance — kiểm soát ngân sách | Risk-tiering: duyệt 1 cấp cho budget nhỏ |
| 9 | Seller xem xét thư mời chiến dịch | ✓ |  |  | Seller tự xem — tăng coverage | Self-serve portal |
| 10 | Seller xác nhận tham gia trên Seller Centre | ✓ |  |  | Xác nhận cam kết seller | Auto-confirm + template |
| 11 | Seller chuẩn bị tồn kho & cài đặt giá sốc | ✓ |  |  | Chuẩn bị đầu vào bán hàng | Checklist + reminder |
| 12 | Buyer truy cập săn deal 12.12 Siêu Sale | ✓ |  |  | KH xem promotion — tiếp cận | Personalization engine |
| 13 | Buyer thanh toán áp mã FreeShip & Lazada Voucher | ✓ |  |  | Doanh thu — giá trị cuối cùng | One-tap checkout + voucher auto-apply |
| 14 | Hệ thống gửi lời mời tham gia đến Sellers | ✓ |  |  | Tự động mời — thay manual outreach | Cá nhân hóa lời mời seller |
| 15 | Cấu hình chiến dịch trên hệ thống |  |  | ✓ | Config copy-paste thủ công — waste (lỗi ~10%, ước tính phỏng vấn, khớp NVA 10%) | Config campaign tự động từ template |
| 16 | Tự động phân tách & giải quyết xung đột mã | ✓ |  |  | Chống chồng voucher — bảo vệ lợi nhuận | Auto-stack rules theo policy |
| 17 | Hệ thống kiểm tra & giả lập áp mã voucher |  | ✓ |  | QA kỹ thuật — tránh lỗi tại launch | Auto-QA checklist |
| 18 | Kiểm toán QA toàn diện trước giờ G |  | ✓ |  | Prevent errors | Automated QA suite |
| 19 | Kích hoạt Chiến dịch 12.12 Siêu Hội Mua Sắm | ✓ |  |  | Thực thi campaign | Realtime launch monitor |
| 20 | Hệ thống tự động xuất báo cáo sơ bộ | ✓ |  |  | Tự động báo cáo — thay báo cáo tay | Auto-report + ML insight |
| 21 | Thu thập bổ sung số liệu đối soát |  |  | ✓ | Thu thập data thủ công sau campaign — waste | Auto-extend từ data warehouse |

**Tỷ lệ VA/BVA/NVA:**
- VA: 12/21 (57%)
- BVA: 7/21 (33%)
- NVA: 2/21 (10%)

→ **Nhận xét:** NVA 10% từ cấu hình chiến dịch thủ công và thu thập số liệu đối soát. BVA 33% do nhiều bước compliance/budget cần thiết — đây là các bottleneck thời gian lớn nhất (phê duyệt nhiều cấp).

### B. Waste Analysis

| STT | Hoạt động | Move | Hold | Overdo | Mô tả | Thời gian chờ | Giải pháp |
|-----|-----------|------|------|--------|-------|---------------|-----------|
| 1 | Kiểm tra tính tuân thủ pháp lý khuyến mãi (Nghị định 81) | | ✓ | | Legal review thủ công, chờ duyệt | 1-3 ngày | Checklist số hóa + auto-validation |
| 2 | Thẩm định ngân sách & tỷ suất ROI | | ✓ | | Finance review, nhiều vòng hỏi lại | 2-5 ngày | Dashboard ROI + template chuẩn |
| 3 | Phê duyệt ngân sách (Trưởng bộ phận <100M / CMO-CFO >100M) | | ✓ | | Chờ lịch phê duyệt, bottleneck multi-layer | 1-3 ngày | Delegation theo hạn mức |
| 4 | Seller xem xét thư mời chiến dịch | | ✓ | | Seller không phản hồi kịp | 2-7 ngày | Nhắc + thời hạn rõ |
| 5 | Tự động phân tách & giải quyết xung đột mã | ✓ | | | Trùng voucher phải xử lý lại | 1-4 giờ | Rule engine thông minh hơn |
| 6 | Thu thập bổ sung số liệu đối soát | | ✓ | | Báo cáo thiếu data, phải thu thập lại | 1-2 ngày | Auto-validate data trước |

**Tổng lãng phí:** 6 hoạt động
- Move: 1 (17%)
- Hold: 5 (83%)

→ **Hold time chiếm 83%** — các vòng phê duyệt (compliance, budget, director) là bottleneck lớn nhất của quy trình marketing.

### C. Root Cause Analysis — Fishbone (Ishikawa) 5 Cấp

```
Vấn đề: Time-to-market chiến dịch dài (3-4 tuần / 21-28 ngày chuẩn bị) và chậm cập nhật theo thị trường

Level 1 — Nguyên nhân lớn:
├── Con người (Man)
│   ├── Level 2: Nhiều bên phê duyệt (Marketing, Legal, Finance, Trưởng bộ phận / CMO-CFO)
│   │   ├── Level 3: Mỗi bên review tuần tự, chờ đợi nhau
│   │   │   ├── Level 4: Không có parallel approval workflow
│   │   │   │   └── Level 5: Legacy process design — tuần tự hóa mọi bước
│   │   └── Level 3: Phê duyệt multi-layer (Trưởng bộ phận / CMO-CFO) là bottleneck
│   │       ├── Level 4: Mọi budget đều phải phê duyệt qua nhiều cấp
│   │       │   └── Level 5: Không có hạn mức phân quyền theo level
├── Quy trình (Process)
│   ├── Level 2: Compliance check thủ công
│   │   ├── Level 3: Legal phải đọc từng campaign material
│   │   │   ├── Level 4: Không có checklist auto-validate
│   │   │   │   └── Level 5: Thiếu số hóa quy trình tuân thủ
│   │   └── Level 3: Seller chậm xác nhận tham gia
│   │       ├── Level 4: Thư mời không rõ ràng/không có deadline
│   │       │   └── Level 5: Thiếu automated reminder + deadline enforcement
├── Công nghệ (Technology)
│   ├── Level 2: Báo cáo phải thu thập thủ công
│   │   ├── Level 3: Dữ liệu từ nhiều nguồn chưa tự động hợp nhất
│   │   │   ├── Level 4: Thiếu data pipeline tự động
│   │   │   │   └── Level 5: Data warehouse chưa tích hợp đủ
│   │   └── Level 3: Rule engine xung đột mã còn thủ công
│   │       ├── Level 4: Config campaign thiếu kiểm tra xung đột
│   │       │   └── Level 5: Rule engine phát triển chưa đầy đủ
└── Đo lường (Measurement)
    ├── Level 2: Không có KPI time-to-market
    │   ├── Level 3: Không đo được campaign launch lead time
    │   │   ├── Level 4: Thiếu metrics cho approval cycle
    │   │   │   └── Level 5: Management chưa ưu tiên speed-to-market
    │   └── Level 3: ROI đánh giá sau campaign (reactive)
    │       ├── Level 4: Không có real-time ROI trong campaign
    │       │   └── Level 5: Dashboard real-time chưa được xây
```

### 5-Why Analysis

**Vấn đề:** Time-to-market chiến dịch dài 3-4 tuần (21-28 ngày), chậm phản ứng thị trường

| Level | Câu hỏi | Câu trả lời |
|-------|---------|-------------|
| Why 1 | Tại sao time-to-market dài 3-4 tuần (21-28 ngày)? | Nhiều vòng phê duyệt tuần tự + chờ seller + config thủ công |
| Why 2 | Tại sao nhiều vòng phê duyệt? | Compliance, Finance, Trưởng bộ phận / CMO-CFO mỗi bên review riêng |
| Why 3 | Tại sao review tuần tự? | Không có parallel approval workflow |
| Why 4 | Tại sao không có parallel workflow? | Legacy process design — mọi thứ tuần tự hóa |
| Why 5 | Tại sao thiết kế tuần tự? | Không có KPI speed-to-market để thúc đẩy đổi mới process |

**Root Cause:** Approval workflow tuần tự không tối ưu + thiếu KPI speed-to-market + data pipeline chưa tự động.

## 3.6.4. Phân tích định lượng

### A. Thời gian

| STT | Hoạt động | Min | Max | Avg | Ghi chú |
|-----|-----------|-----|-----|-----|---------|
| 1 | Nghiên cứu thị trường & lập bản đề xuất | 2 ngày | 7 ngày | 4 ngày | Marketing |
| 2 | Phân khúc lại nhóm đối tượng mục tiêu | 1 ngày | 3 ngày | 2 ngày | 30% cases |
| 3 | Thiết kế concept & lập kế hoạch chi tiết | 3 ngày | 10 ngày | 5 ngày | Creative |
| 4 | Kiểm tra tính tuân thủ pháp lý khuyến mãi (Nghị định 81) | 1 ngày | 3 ngày | 2 ngày | Legal |
| 5 | Thẩm định ngân sách & tỷ suất ROI | 1 ngày | 5 ngày | 3 ngày | Finance |
| 6 | Phê duyệt ngân sách (Trưởng bộ phận <100M / CMO-CFO >100M) | 1 ngày | 3 ngày | 2 ngày | 40% budget lớn |
| 7 | Hệ thống gửi lời mời tham gia đến Sellers | 1 giờ | 1 ngày | 4 giờ | Automated |
| 8 | Seller xem xét thư mời chiến dịch | 1 ngày | 7 ngày | 3 ngày | Seller |
| 9 | Seller xác nhận tham gia trên Seller Centre | 1 giờ | 1 ngày | 4 giờ | Seller |
| 10 | Seller chuẩn bị tồn kho & cài đặt giá sốc | 1 ngày | 3 ngày | 2 ngày | Seller |
| 11 | Cấu hình chiến dịch trên hệ thống | 2 giờ | 1 ngày | 6 giờ | System |
| 12 | Tự động phân tách & giải quyết xung đột mã | 1 giờ | 4 giờ | 2 giờ | 20% cases |
| 13 | Hệ thống kiểm tra & giả lập áp mã voucher | 30 phút | 2 giờ | 1 giờ | Automated |
| 14 | Kiểm toán QA toàn diện trước giờ G | 2 giờ | 1 ngày | 6 giờ | QA |
| 15 | Kích hoạt Chiến dịch 12.12 Siêu Hội Mua Sắm | 5 phút | 30 phút | 10 phút | Automated |
| 16 | Buyer truy cập săn deal 12.12 Siêu Sale | — | — | — | Trong campaign |
| 17 | Buyer thanh toán áp mã FreeShip & Lazada Voucher | — | — | — | Trong campaign |
| 18 | Theo dõi hiệu năng hệ thống & doanh số realtime | — | — | — | Trong campaign |
| 19 | Hệ thống tự động xuất báo cáo sơ bộ | 1 giờ | 1 ngày | 4 giờ | Sau campaign |
| 20 | Thu thập bổ sung số liệu đối soát | 1 ngày | 2 ngày | 1.5 ngày | 25% cases thiếu data |
| 21 | Lập báo cáo tổng kết & đánh giá ROI | 2 ngày | 7 ngày | 4 ngày | Marketing + BI |

### B. Phân tích Cycle Time Probability-Weighted

| Hoạt động | Thời gian (phút) | Xác suất | Thời gian kỳ vọng (phút) | Ghi chú |
|-----------|-------------------|----------|--------------------------|---------|
| Nghiên cứu thị trường & lập bản đề xuất | 5,760 (4 ngày) | 100% | 5,760 | Marketing |
| Phân khúc lại nhóm đối tượng mục tiêu | 2,880 (2 ngày) | 30% | 864 | 30% cần re-segment |
| Thiết kế concept & lập kế hoạch chi tiết | 7,200 (5 ngày) | 100% | 7,200 | Creative |
| Kiểm tra tính tuân thủ pháp lý khuyến mãi (Nghị định 81) | 2,880 (2 ngày) | 100% | 2,880 | Legal |
| Thẩm định ngân sách & tỷ suất ROI | 4,320 (3 ngày) | 100% | 4,320 | Finance |
| Phê duyệt ngân sách (Trưởng bộ phận <100M / CMO-CFO >100M) | 2,880 (2 ngày) | 40% | 1,152 | 40% budget lớn |
| Hệ thống gửi lời mời tham gia đến Sellers | 240 (4h) | 100% | 240 | Automated |
| Seller xem xét thư mời chiến dịch | 4,320 (3 ngày) | 100% | 4,320 | Seller response |
| Seller xác nhận tham gia trên Seller Centre | 240 (4h) | 90% | 216 | 90% đồng ý |
| Seller chuẩn bị tồn kho & cài đặt giá sốc | 2,880 (2 ngày) | 90% | 2,592 | Seller |
| Cấu hình chiến dịch trên hệ thống | 360 (6h) | 100% | 360 | System |
| Tự động phân tách & giải quyết xung đột mã | 120 (2h) | 20% | 24 | 20% xung đột |
| Hệ thống kiểm tra & giả lập áp mã voucher | 60 | 100% | 60 | Automated |
| Kiểm toán QA toàn diện trước giờ G | 360 (6h) | 100% | 360 | QA |
| Kích hoạt Chiến dịch 12.12 Siêu Hội Mua Sắm | 10 | 100% | 10 | Automated |
| Hệ thống tự động xuất báo cáo sơ bộ | 240 (4h) | 100% | 240 | Sau campaign |
| Thu thập bổ sung số liệu đối soát | 2,160 (1.5 ngày) | 25% | 540 | 25% thiếu data |
| Lập báo cáo tổng kết & đánh giá ROI | 5,760 (4 ngày) | 100% | 5,760 | Marketing + BI |

**Tổng Cycle Time kỳ vọng (pre-launch) = 30,358 phút ≈ 21.1 ngày** *(trong khoảng 3-4 tuần / 21-28 ngày của report)*
**Tổng Cycle Time kỳ vọng (đến báo cáo ROI) = 36,898 phút ≈ 25.6 ngày**

### C. Chi phí (per campaign 12.12)

| STT | Thành phần | Chi phí (VND) | Ghi chú |
|-----|-----------|---------------|---------|
| 1 | Marketing team labor (nghiên cứu + concept) | 32,000,000 | 4 nhân sự × 10 ngày × 800,000/ngày |
| 2 | Legal/Compliance review | 4,800,000 | 0.5 FTE × 2 ngày |
| 3 | Finance budget review | 4,800,000 | 0.5 FTE × 2 ngày |
| 4 | Seller management (mời + chăm sóc) | 8,000,000 | 1 FTE × 5 ngày |
| 5 | System config + QA | 6,000,000 | Tech/Ops support |
| 6 | BI reporting | 6,400,000 | 1 FTE × 4 ngày |
| **TỔNG (chi phí vận hành trực tiếp, chưa gồm ngân sách khuyến mãi/voucher)** | | **62,000,000 VND** | Per campaign 12.12 |

**Voucher/ngân sách khuyến mãi (ngoài phạm vi chi phí vận hành):** ước tính 5-10 tỷ VND/campaign (FreeShip + voucher + subsidy) — ngoài phạm vi Bảng 3.11 report

> **Ghi chú phạm vi chi phí:** Bảng 3.11 của report ghi chi phí vận hành Campaign 420.000.000 VNĐ/Mega Campaign (gồm ngân sách khuyến mãi, voucher, subsidy phân bổ); con số 62.000.000 VNĐ trong tài liệu này là chi phí vận hành trực tiếp (labor + system/ops), chưa gồm ngân sách khuyến mãi. So sánh giảm 62 → 30 triệu giữ nguyên ở mức chi phí vận hành trực tiếp.

### D. Chất lượng (Quality Metrics)

| Metric (Chỉ số) | Hiện tại (AS-IS) | Benchmark (VN e-commerce) | Gap | Mục tiêu TO-BE |
|-----------------|------------------|---------------------------|-----|----------------|
| Thời gian phê duyệt campaign (Campaign Approval Time) | 5-7 ngày | 2-3 ngày | +2-5 ngày | **<1 ngày** |
| Tỷ lệ coupon fraud (Coupon Fraud Rate) | 3-5% | 1-2% | +2-3% | **<0.5%** |
| ROI trung bình campaign (Avg Campaign ROI) | 2.5x | 3.5x | -1.0x | **5x** |
| Tỷ lệ click-through rate CTR (Click-Through Rate) | 1.5% | 2.5% | -1.0% | **4%** |
| Chi phí thu hút khách hàng CAC (Customer Acquisition Cost) | 80,000 VND | 50,000 VND | +30,000 VND | **25,000 VND** |
| Thời gian A/B test (A/B Test Duration) | 7-14 ngày | 3-5 ngày | +4-9 ngày | **1-2 ngày** |
| Tỷ lệ conversion rate (Conversion Rate) | 2% | 3.5% | -1.5% | **5%** |
| Time-to-market (Thời gian đến thị trường) | 3-4 tuần (21-28 ngày) | 7-10 ngày | +11-21 ngày | **1 tuần (~7 ngày)** |
| Tỷ lệ seller participation (Seller Participation Rate) | 60% | 80% | -20% | **90%** |
| Chi phí vận hành/campaign (Cost per Campaign Ops) | 62,000,000 VND | 30,000,000 VND | +32,000,000 VND | **15,000,000 VND** |

> **Ghi chú:** Các số liệu benchmark dựa trên khảo sát industry VN e-commerce 2025-2026. Mục tiêu TO-BE dựa trên mô hình cải tiến AI/automation.

## 3.6.5. Phân tích Pareto

### Bảng Vấn đề — Giả thuyết — Chi phí ảnh hưởng

| STT | Vấn đề | Giả thuyết | Chi phí ảnh hưởng/campaign (VND) | Tỷ trọng |
|-----|--------|-----------|----------------------------------|----------|
| 1 | Approval cycle multi-layer ước tính 5-8 ngày (compliance + budget + Trưởng bộ phận/CMO-CFO) | Workflow tuần tự, không parallel | 25,000,000 (labor + lost speed-to-market) | 40.3% |
| 2 | Seller tham gia rate thấp 60% | Thư mời không rõ + không có deadline enforcement | 18,000,000 (lost GMV do thiếu seller) | 29.0% |
| 3 | Báo cáo phải thu thập thủ công 25% | Data pipeline chưa tự động | 10,000,000 (BI labor + delay) | 16.1% |
| 4 | Xung đột mã voucher 20% | Rule engine chưa thông minh | 6,000,000 (rework config) | 9.7% |
| 5 | Re-segment 30% tốn thời gian | Segmentation thiếu data-driven | 3,000,000 (marketing labor) | 4.8% |
| **TỔNG** | | | **62,000,000** | **100%** |

### Kết luận 80/20

**Top 3 vấn đề (chiếm ~85% chi phí):**
1. Approval cycle dài (40.3%) — giải pháp: parallel approval + hạn mức phân quyền
2. Seller tham gia thấp (29.0%) — giải pháp: thư mời rõ ràng + deadline enforcement
3. Báo cáo thủ công (16.1%) — giải pháp: data pipeline tự động

→ **Giải quyết 3 vấn đề này sẽ giảm ~85% chi phí lãng phí (~53 triệu VND/campaign).**

## 3.6.6. Kết luận và hướng cải tiến TO-BE

### Tóm tắt AS-IS
- Time-to-market: 3-4 tuần / 21-28 ngày (pre-launch ~21.1 ngày kỳ vọng, trong khoảng 21-28 ngày của report)
- Cycle time đến báo cáo ROI: ~25.6 ngày
- Chi phí vận hành per campaign: ~62 triệu VND
- Bottleneck: Approval cycle multi-layer (ước tính 5-8 ngày phỏng vấn; report ghi bottleneck multi-layer approval, không nêu số ngày cụ thể) + seller participation

### Hướng cải tiến TO-BE

| STT | Cải tiến | Mục tiêu | Giảm chi phí (campaign) |
|-----|---------|----------|-------------------------|
| 1 | Parallel approval workflow + hạn mức phân quyền | Approval: multi-layer → 1 cấp (giảm đáng kể) | -25 triệu VND |
| 2 | Thư mời rõ ràng + deadline + automated reminder | Seller participation: 60% → 80% | -18 triệu VND |
| 3 | Data pipeline tự động + auto-validate | Report: 7 ngày → 3 ngày | -10 triệu VND |
| 4 | Nâng cấp rule engine chống xung đột mã | Xung đột: 20% → 5% | -6 triệu VND |
| 5 | AI-driven segmentation | Re-segment: 30% → 10% | -3 triệu VND |
| **TỔNG GIẢM** | | | **-62 triệu VND/campaign** |

### So sánh AS-IS vs TO-BE

| Metric | AS-IS | TO-BE | Cải thiện |
|--------|-------|-------|-----------|
| Time-to-market | 3-4 tuần (21-28 ngày) | 1 tuần (~7 ngày) | -65~75% |
| Approval cycle | 5-8 ngày | 2 ngày | -65% (ước tính; report ghi multi-layer approval) |
| Seller participation | 60% | 80% | +20% |
| Report timeliness | 7 ngày | 3 ngày | -57% |
| Chi phí vận hành/campaign | 62 triệu VND | 30 triệu VND | -52% |

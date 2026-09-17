# 3.1. Quy trình Quản lý Nhà bán hàng (Seller Onboarding & Lifecycle)

## 3.1.1. Mô tả quy trình

**Phạm vi:** Bắt đầu từ khi Seller đăng ký tài khoản Lazada → KYC → Phê duyệt → Kích hoạt gian hàng → Giám sát vi phạm.

**Các tác nhân tham gia:**
- **Seller:** Người bán — đăng ký, tải giấy tờ, cập nhật thông tin
- **Lazada System (Automated):** OCR, kiểm tra giấy tờ giả, chấm điểm rủi ro, gửi thông báo, cảnh cáo tự động
- **Compliance Team:** Thẩm định thủ công hồ sơ, phân tầng rủi ro
- **Legal / Giám sát Vận hành:** Xử lý vi phạm nghiêm trọng, khóa gian hàng vĩnh viễn

**Kết quả có thể xảy ra:**
- Gian hàng Lazada được kích hoạt — seller hoạt động bình thường
- Hồ sơ bị từ chối vĩnh viễn — seller không đạt yêu cầu KYC
- Đã cảnh cáo — vi phạm mức nhẹ (1-2 sao)
- Đã tạm khóa — vi phạm mức trung bình (3-5 sao), khóa 7 ngày
- Đã khóa vĩnh viễn — vi phạm nghiêm trọng (>6 sao)

### SiPOC

| SiPOC | Chi tiết |
|-------|----------|
| **Supplier** | Seller (cung cấp giấy tờ, thông tin định danh), Cơ quan nhà nước (CCCD/CMND/GPKD) |
| **Input** | Thông tin định danh, CMND/CCCD, GPKD, Giấy chứng nhận LazMall (nếu có), SĐT OTP |
| **Process** | Đăng ký → OTP xác thực → Upload giấy tờ → Validate OCR tự động → Compliance review → Phân tầng rủi ro → Phê duyệt/Từ chối → Giám sát vi phạm |
| **Output** | Gian hàng được kích hoạt HOẶC Hồ sơ bị từ chối HOẶC Cảnh cáo/Tạm khóa/Khóa vĩnh viễn |
| **Customer** | Seller (nhận kết quả), Buyer (mua hàng từ seller đáng tin) |

## 3.1.2. Mô hình BPMN

*(File: `processes/01-seller-management.bpmn`)*

**Thống kê mô hình:**
- Số lanes: 4 (Seller, Lazada System (Automated), Compliance Team, Legal / Giám sát Vận hành)
- Số activities: 14 (8 userTask + 6 serviceTask)
- Số gateways: 15 (XOR)
- End events: 5
- Sequence flows: 42
- Độ phức tạp: Medium-High

> **Ghi chú:** Các số liệu trên được kiểm tra trực tiếp từ BPMN XML (`processes/01-seller-management.bpmn`). Mermaid/sơ đồ minh họa AS-IS được trình bày tại báo cáo chính (DOAN-LAZADA-FINAL.md, Mục 3.6.2 — Hình 3.4), cần đồng bộ về 4 lanes / 14 activities / 15 gateways / 5 end events / 42 flows tương ứng.

## 3.1.3. Phân tích định tính

### A. Value-Added Analysis

| STT | Hoạt động (tên từ BPMN) | VA | BVA | NVA | Giải thích | Đề xuất TO-BE |
|-----|--------------------------|----|-----|-----|------------|---------------|
| 1 | Điền thông tin định danh Seller | ✓ |  |  | Tạo hồ sơ Seller — đầu vào giá trị | Giữ nguyên; guided form |
| 2 | Upload CMND/CCCD + GPKD + Giấy chứng nhận (LazMall) | ✓ |  |  | Bắt buộc để xác minh danh tính & LazMall badge | Smart Scan OCR tự động |
| 3 | Bổ sung / sửa hồ sơ |  | ✓ |  | Cần khi hồ sơ thiếu — kiểm soát chất lượng | Auto-check trước khi submit (giảm vòng sửa) |
| 4 | Cập nhật tài khoản ngân hàng (giải ngân) |  | ✓ |  | Bắt buộc cho giải ngân — tuân thủ tài chính | Xác thực IBAN tự động |
| 5 | Compliance review thủ công (24-48h) |  | ✓ |  | Cần cho legal compliance nhưng chậm — Hold lớn | **Semi-automate:** auto-approve low-risk 3s, review chỉ high-risk |
| 6 | Gửi cảnh cáo Seller |  | ✓ |  | Quản trị vi phạm — cần thiết duy trì chất lượng sàn | Template cảnh cáo chuẩn hóa |
| 7 | Tạm khóa gian hàng (7 ngày) |  | ✓ |  | Kiểm soát rủi ro khi vi phạm nghiêm trọng | Tự động hóa theo mức risk score |
| 8 | Khóa gian hàng vĩnh viễn |  | ✓ |  | Kiểm soát rủi ro tối đa — hiếm khi dùng | Giữ nguyên; SLA phản hồi khiếu nại |
| 9 | Gửi OTP xác thực SĐT |  | ✓ |  | Xác minh chủ sở hữu — bảo mật | Giữ nguyên (auto) |
| 10 | Validate định danh tự động |  | ✓ |  | Lọc hồ sơ sai — prevent fraud | Nâng cấp rule engine real-time |
| 11 | Quét OCR + kiểm tra giấy tờ giả |  | ✓ |  | Chống gian lận giấy tờ — bảo vệ sàn | Nâng cấp eKYC sinh trắc học real-time |
| 12 | Chấm điểm rủi ro (Risk scoring) |  | ✓ |  | Phân loại mức rủi ro — nền tảng auto-decision | Kết nối auto-approve path (Low-risk 3s) |
| 13 | Thông báo kết quả duyệt Seller Centre | ✓ |  |  | Người dùng nhận kết quả — giao tiếp giá trị | Đa kênh (push + email) tức thì |
| 14 | Giám sát điểm đánh giá & vi phạm (auto) | ✓ |  |  | Chủ động bảo vệ sàn — giảm tỷ lệ khóa tài khoản | Cảnh báo sớm trước khi vi phạm |

**Tỷ lệ VA/BVA/NVA:**
- VA: 4/14 (29%)
- BVA: 10/14 (71%)
- NVA: 0/14 (0%)

→ **Nhận xét:** Tỷ lệ NVA 0% nhưng BVA rất cao (71%) — nhiều bước compliance/kiểm soát cần thiết nhưng có thể tự động hóa mạnh hơn. Bottleneck chính là Compliance review thủ công 24-48h.

### B. Waste Analysis

| STT | Hoạt động | Move | Hold | Overdo | Mô tả | Thời gian chờ | Giải pháp |
|-----|-----------|------|------|--------|-------|---------------|-----------|
| 1 | Compliance review thủ công (24-48h) | | ✓ | | Manual bottleneck — hồ sơ xếp hàng chờ reviewer | 24-48h | Auto-approve low-risk, chỉ review cases > ngưỡng rủi ro |
| 2 | Bổ sung / sửa hồ sơ | | ✓ | | Seller phải sửa lại hồ sơ do hướng dẫn không rõ ràng | 2-7 ngày | Guided upload với validation real-time |
| 3 | Quét OCR + kiểm tra giấy tờ giả | ✓ | | | Manual QC overlap với auto-check | 15-30 phút | Bỏ manual QC nếu OCR accuracy >98% |
| 4 | Cập nhật tài khoản ngân hàng (giải ngân) | | | ✓ | Bắt buộc trước khi activate nhưng không liên quan trực tiếp đến KYC | Ngại chờ | Cho phép submit sau activate, tự verify sau |

**Tổng lãng phí:** 4 hoạt động
- Move: 1 (25%)
- Hold: 2 (50%)
- Overdo: 1 (25%)

### C. Root Cause Analysis — Fishbone (Ishikawa) 5 Cấp

```
Vấn đề: Thời gian phê duyệt Seller trung bình 24-48h (quá lâu)

Level 1 — Nguyên nhân lớn:
├── Con người (Man)
│   ├── Level 2: Compliance reviewer thiếu
│   │   ├── Level 3: Số lượng reviewer không tăng theo volume đăng ký
│   │   │   ├── Level 4: Hiring plan không dự báo đúng demand
│   │   │   │   └── Level 5: Không có forecast model cho seller registration volume
│   │   └── Level 3: Training reviewer mất 2-3 tuần
│   │       ├── Level 4: Quy trình review phức tạp, nhiều edge cases
│   │       │   └── Level 5: Thiếu standardized decision matrix
├── Quy trình (Process)
│   ├── Level 2: Compliance review bottleneck
│   │   ├── Level 3: Mọi hồ sơ đều vào queue thủ công
│   │   │   ├── Level 4: Không phân loại auto-approve vs manual
│   │   │   │   └── Level 5: Thiếu risk-based routing
│   │   └── Level 3: Không có SLA enforcement cho reviewer
│   │       ├── Level 4: Reviewer không có KPI processing time
│   │       │   └── Level 5: Management focus vào accuracy hơn speed
├── Công nghệ (Technology)
│   ├── Level 2: OCR + KYC engine còn hạn chế
│   │   ├── Level 3: False positive rate cao → nhiều cases cần manual
│   │   │   ├── Level 4: OCR model chưa train trên CMND/CCCD VN mới nhất
│   │   │   │   └── Level 5: Thiếu update data training từ cơ quan nhà nước
│   │   └── Level 3: Risk scoring model chưa tối ưu
│   │       ├── Level 4: Ngưỡng rủi ro cứng, không adapts
│   │       │   └── Level 5: Không có feedback loop từ kết quả review
└── Vật liệu (Material/Data)
    ├── Level 2: Hồ sơ seller không nhất quán
    │   ├── Level 3: Seller upload giấy tờ sai/đầy đủ
    │   │   ├── Level 4: UX form không validate realtime
    │   │   │   └── Level 5: Thiếu pre-upload checklist
    │   └── Level 3: Dữ liệu từ cơ quan nhà nước không tích hợp
    │       ├── Level 4: Không API trực tiếp với CSDL CCCD
    │       │   └── Level 5: Hạn chế pháp lý về chia sẻ data
```

### 5-Why Analysis

**Vấn đề:** Compliance review thủ công chiếm 24-48h trong quy trình onboarding

| Level | Câu hỏi | Câu trả lời |
|-------|---------|-------------|
| Why 1 | Tại sao review thủ công mất 24-48h? | Mỗi hồ sơ cần reviewer đọc, so sánh giấy tờ, check database |
| Why 2 | Tại sao phải đọc so sánh thủ công? | OCR + auto-check chưa đủ tin cậy để approve tự động |
| Why 3 | Tại sao auto-check chưa đủ tin cậy? | False positive rate ~15%, model chưa train đủ data VN |
| Why 4 | Tại sao model chưa train đủ data? | Thiếu partnership với cơ quan nhà nước, data gathering chậm |
| Why 5 | Tại sao data gathering chậm? | Chưa có budget dự phòng cho KYC AI improvement |

**Root Cause:** Thiếu đầu tư vào AI KYC model + không có risk-based routing để phân loại auto vs manual review.

## 3.1.4. Phân tích định lượng

### A. Thời gian

| STT | Hoạt động | Min | Max | Avg | Ghi chú |
|-----|-----------|-----|-----|-----|---------|
| 1 | Điền thông tin định danh Seller | 5 phút | 15 phút | 10 phút |Seller preparation |
| 2 | Gửi OTP xác thực SĐT | 30 giây | 2 phút | 1 phút | SMS delivery |
| 3 | Upload CMND/CCCD + GPKD + Giấy chứng nhận (LazMall) | 5 phút | 20 phút | 10 phút | Phụ thuộc preparation |
| 4 | Validate định danh tự động | 3 giây | 30 giây | 10 giây | Automated |
| 5 | Cập nhật tài khoản ngân hàng (giải ngân) | 3 phút | 10 phút | 5 phút | Nhập thông tin NH |
| 6 | Quét OCR + kiểm tra giấy tờ giả | 5 giây | 60 giây | 15 giây | Automated + manual QC |
| 7 | Bổ sung / sửa hồ sơ | 1 giờ | 7 ngày | 2 ngày | Nếu cần bổ sung (40% cases) |
| 8 | Chấm điểm rủi ro (Risk scoring) | 3 giây | 10 giây | 5 giây | Automated |
| 9 | Compliance review thủ công (24-48h) | 4 giờ | 72 giờ | 24 giờ | Manual bottleneck chính |
| 10 | Thông báo kết quả duyệt Seller Centre | 1 phút | 5 phút | 2 phút | Automated |

### B. Phân tích Cycle Time Probability-Weighted

| Hoạt động | Thời gian (phút) | Xác suất | Thời gian kỳ vọng (phút) | Ghi chú |
|-----------|-------------------|----------|--------------------------|---------|
| Điền thông tin định danh Seller | 10 | 100% | 10.0 | Bắt buộc |
| Gửi OTP xác thực SĐT | 1 | 100% | 1.0 | Bắt buộc |
| Upload CMND/CCCD + GPKD + Giấy chứng nhận (LazMall) | 10 | 100% | 10.0 | Bắt buộc |
| Validate định danh tự động | 0.17 | 100% | 0.17 | Tức thì |
| Cập nhật tài khoản ngân hàng (giải ngân) | 5 | 100% | 5.0 | Bắt buộc |
| Quét OCR + kiểm tra giấy tờ giả | 0.25 | 100% | 0.25 | Tức thì |
| Bổ sung / sửa hồ sơ | 2,880 (2 ngày = 48h) | 40% | 1,152.0 | 40% cases cần bổ sung |
| Compliance review thủ công (24-48h) | 1,440 (24h) | 85% | 1,224.0 | 85% vào manual queue |
| Thông báo kết quả duyệt | 2 | 100% | 2.0 | Automated |

**Tổng Cycle Time kỳ vọng = 2,404 phút ≈ 40 giờ ≈ 5 ngày làm việc**

### C. Chi phí (per seller registration)

| STT | Thành phần | Chi phí (VND) | Ghi chú |
|-----|-----------|---------------|---------|
| 1 | System infrastructure (OCR, KYC API) | 2,000 | Allocated per registration |
| 2 | Compliance staff time | 15,000 | 30 phút review × 50,000 VND/h ( VN e-commerce avg) |
| 3 | OTP SMS cost | 500 | ~500 VND/SMS VN |
| 4 | Risk scoring engine | 1,000 | ML inference cost |
| 5 | Chi phí bổ sung hồ sơ (40% cases × retry) | 6,000 | 40% × 15,000 VND rework |
| **TỔNG** | | **24,500 VND** | Per registration |

**Volume ước tính:** ~20,000 seller đăng ký mới/tháng (Lazada VN)
**Monthly cost:** ~490 triệu VND/tháng

### D. Chất lượng

| Metric | Current | Benchmark (VN e-commerce) | Gap |
|--------|---------|---------------------------|-----|
| Approval rate | 85-90% | 92-95% | -5% |
| Avg approval time | 24-48h | 4-8h | +20-40h |
| Seller churn (30 ngày đầu) | 15-20% | 8-12% | +7-8% |
| OCR accuracy | 85% | 95-98% | -10-13% |
| Rework rate (bổ sung hồ sơ) | 40% | 10-15% | +25-30% |

## 3.1.5. Phân tích Pareto

### Bảng Vấn đề — Giả thuyết — Chi phí ảnh hưởng

| STT | Vấn đề | Giả thuyết | Chi phí ảnh hưởng/tháng (VND) | Tỷ trọng |
|-----|--------|-----------|-------------------------------|----------|
| 1 | Compliance review bottleneck 24-48h | Thiếu auto-approve cho low-risk + reviewer shortage | 180,000,000 (delay cost + lost sellers) | 36.7% |
| 2 | Rework rate 40% — seller bổ sung hồ sơ | UX form không guide, thiếu validation realtime | 120,000,000 (rework labor + re-registration cost) | 24.5% |
| 3 | OCR accuracy thấp 85% | Model chưa train đủ data VN | 95,000,000 (manual QC overlap) | 19.4% |
| 4 | Seller churn 15-20% trong 30 ngày đầu | Onboarding education không đủ + activation time quá lâu | 65,000,000 (acquisition cost waste) | 13.3% |
| 5 | Risk scoring chưa tối ưu | Ngưỡng cứng, không adapts theo market conditions | 30,000,000 (false positive review cost) | 6.1% |
| **TỔNG** | | | **490,000,000** | **100%** |

### Kết luận 80/20

**Top 3 vấn đề (chiếm ~80% chi phí):**
1. Compliance review bottleneck (36.7%) — giải pháp: risk-based auto-approve
2. Rework rate cao (24.5%) — giải pháp: guided upload + realtime validation
3. OCR accuracy thấp (19.4%) — giải pháp: upgrade AI model + training data VN

→ **Invest 3 vấn đề này sẽ giảm ~80% chi phí lãng phí (~395 triệu VND/tháng).**

## 3.1.6. Kết luận và hướng cải tiến TO-BE

### Tóm tắt AS-IS
- Tổng cycle time kỳ vọng: ~40 giờ (5 ngày làm việc)
- Chi phí per registration: ~24,500 VND
- Bottleneck chính: Compliance review thủ công (24-48h)
- Rework rate: 40% (quá cao)
- Tỷ lệ VA/BVA/NVA: 29%/71%/0%

### Hướng cải tiến TO-BE

| STT | Cải tiến | Mục tiêu | Giảm chi phí (tháng) |
|-----|---------|----------|----------------------|
| 1 | Risk-based auto-approve (>90% low-risk cases) | Review time: 24h → 2-4h | -180 triệu VND |
| 2 | Guided upload form + realtime validation | Rework rate: 40% → 10% | -120 triệu VND |
| 3 | Upgrade OCR AI model + VN training data | Accuracy: 85% → 98% | -95 triệu VND |
| 4 | Onboarding education automation | Seller churn 30 ngày: 20% → 10% | -65 triệu VND |
| 5 | Adaptive risk scoring model | False positive: 15% → 5% | -30 triệu VND |
| **TỔNG GIẢM** | | | **-490 triệu VND/tháng** |

### So sánh AS-IS vs TO-BE

| Metric | AS-IS | TO-BE | Cải thiện |
|--------|-------|-------|-----------|
| Avg approval time | 40h (trước đây ước tính 24-48h) | 2h | -95% |
| Rework rate | 40% | 10% | -75% |
| OCR accuracy | 85% | 98% | +13% |
| Chi phí per registration | 24,500 VND | 12,000 VND | -51% |
| Monthly cost | 490 triệu VND | 150 triệu VND | -340 triệu VND (-69%) |

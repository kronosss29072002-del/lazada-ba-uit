# 3.2. Quy trình Quản lý Tranh chấp (Dispute Resolution)

## 3.2.1. Mô tả quy trình

**Phạm vi:** Bắt đầu từ khi Buyer khởi tạo tranh chấp → Thu thập bằng chứng → Phân loại AI → Đối soát hai bên → CS thẩm định → Quyết định xử lý → Giải quyết xong.

**Các tác nhân tham gia:**
- **Buyer:** Người mua — tạo tranh chấp, tải bằng chứng
- **Seller:** Người bán — phản hồi tranh chấp trong 48h
- **CS Agent:** Nhân viên CSKH — thẩm định hồ sơ, ban hành quyết định
- **Lazada System (Automated):** Thu thập dữ liệu đơn hàng, phân loại AI, gửi thông báo
- **Escalation Team:** Nhóm chuyên trách Lazada — xử lý vụ việc phức tạp

**Kết quả có thể xảy ra:**
- Giải quyết xong — Buyer thắng, hoàn tiền/hoàn hàng
- Tranh chấp bác bỏ — không đủ bằng chứng hoặc không hợp lệ
- AI tự giải quyết — trường hợp đơn giản, giá trị thấp
- Chuyển lên nhóm chuyên trách — vụ việc phức tạp, cần hội đồng thẩm định

### SiPOC

| SiPOC | Chi tiết |
|-------|----------|
| **Supplier** | Buyer (cung cấp bằng chứng khiếu nại), Seller (cung cấp phản hồi/bằng chứng), Shipping carrier (tracking data) |
| **Input** | Đơn hàng, bằng chứng ảnh/video, lý do tranh chấp, thông tin giao hàng |
| **Process** | Tạo tranh chấp → Thu thập dữ liệu → AI phân loại → Đối soát hai bên → Seller phản hồi → CS thẩm định → Ra quyết định → (Kháng cáo → Hội đồng thẩm định) |
| **Output** | Giải quyết xong (Buyer/Seller thắng), Tranh chấp bác bỏ, AI tự giải quyết |
| **Customer** | Buyer (được bảo vệ quyền lợi), Seller (công bằng trong xử lý) |

## 3.2.2. Mô hình BPMN

*(File: `processes/02-dispute-management.bpmn`)*

**Thống kê mô hình:**
- Số lanes: 5 (Buyer, Lazada System (Automated), Seller, CS Agent, Escalation Team)
- Số activities: 12 (8 userTask + 4 serviceTask)
- Số gateways: 16 (XOR)
- End events: 3
- Độ phức tạp: High

## 3.2.3. Phân tích định tính

### A. Value-Added Analysis

| STT | Hoạt động (tên từ BPMN) | VA | BVA | NVA | Giải thích | Đề xuất TO-BE |
|-----|--------------------------|----|-----|-----|------------|---------------|
| 1 | Tạo tranh chấp + lý do | ✓ |  |  | Nhu cầu chính đáng của KH — mở quy trình | Guided form + checklist lý do |
| 2 | Bổ sung bằng chứng (nếu có) | ✓ |  |  | Bằng chứng giúp giải quyết đúng | Upload evidence có cấu trúc (ảnh/video theo danh mục) |
| 3 | Yêu cầu bổ sung bằng chứng |  | ✓ |  | Đảm bảo đủ thông tin — fairness | Auto-check nội dung trước khi gửi |
| 4 | Seller phản hồi (≤48h) | ✓ |  |  | Phản hồi từ bên liên quan — due process | Dynamic deadline 12h/48h theo độ phức tạp |
| 5 | CS thẩm định toàn bộ hồ sơ tranh chấp | ✓ |  |  | Phán xét — giá trị cốt lõi của quy trình | AI-assisted review (summary + gợi ý) |
| 6 | CS ban hành quyết định xử lý | ✓ |  |  | Kết quả giải quyết — giá trị cốt lõi | Decision template theo category |
| 7 | Chuyển lên nhóm chuyên trách (Lazada Escalation) |  | ✓ |  | Complex cases cần chuyên môn | Clear escalation criteria tự động gợi ý |
| 8 | Hội đồng thẩm định & ra quyết định cuối |  | ✓ |  | Phán quyết cuối cho case phức tạp | Decision framework + checklist |
| 9 | Tự động thu thập dữ liệu đơn hàng |  | ✓ |  | Cung cấp context — hỗ trợ review | Fully automate (đã auto) |
| 10 | AI phân loại tranh chấp (Đơn giản/Phức tạp) |  | ✓ |  | Routing đúng luồng — giảm tải CS | Nâng cấp accuracy, auto-assign straight |
| 11 | Kiểm tra lịch sử SLA |  | ✓ |  | Kiểm soát tuân thủ cam kết | Tự động penalty/compensation |
| 12 | Gửi thông báo đối soát đến hai bên | ✓ |  |  | Minh bạch thông tin — giảm khiếu nại kép | Auto update status theo sự kiện |

**Tỷ lệ VA/BVA/NVA:**
- VA: 6/12 (50%)
- BVA: 6/12 (50%)
- NVA: 0/12 (0%)

→ **Nhận xét:** NVA 0% — không có hoạt động lãng phí thuần, nhưng BVA cao (50%) cho thấy nhiều bước auditing/kiểm soát cần thiết (bổ sung bằng chứng, thẩm định, đối soát) gây delay và có thể tối ưu bằng tự động hóa.

### B. Waste Analysis

| STT | Hoạt động | Move | Hold | Overdo | Mô tả | Thời gian chờ | Giải pháp |
|-----|-----------|------|------|--------|-------|---------------|-----------|
| 1 | Seller phản hồi (≤48h) | | ✓ | | Seller có thể phản hồi chậm,Buyer chờ đợi | 48h max, avg 18h | Dynamic SLA: 12h simple, 48h complex |
| 2 | Bổ sung bằng chứng (nếu có) | | ✓ | | Multiple rounds back-and-forth | 2-5 ngày/round | Structured checklist từ đầu, cap 1 round |
| 3 | CS thẩm định toàn bộ hồ sơ tranh chấp | ✓ | | | CS phải đọc manual toàn bộ hồ sơ dài | 30 phút-4h/case | AI summarization + highlight key evidence |
| 4 | Chờ CS agent assignment | | ✓ | | Queue-based, chờ CS available | 4-24h | Auto-assign by category + priority |
| 5 | Hội đồng thẩm định & ra quyết định cuối | | ✓ | | Phức tạp, nhiều bên involved | 3-7 ngày | Clear criteria giảm số cases vào hội đồng |

**Tổng lãng phí:** 5 hoạt động
- Move: 1 (20%)
- Hold: 4 (80%)
- Overdo: 0 (0%)

→ **Hold time chiếm 80% lãng phí** — seller response window và CS assignment là bottleneck lớn nhất.

### C. Root Cause Analysis — Fishbone (Ishikawa) 5 Cấp

```
Vấn đề: Thời gian giải quyết tranh chấp trung bình 5-7 ngày (quá lâu)

Level 1 — Nguyên nhân lớn:
├── Con người (Man)
│   ├── Level 2: CS agent xử lý chậm mỗi case
│   │   ├── Level 3: Mỗi case phải đọc manual toàn bộ evidence
│   │   │   ├── Level 4: Evidence không structured, phải scroll/search
│   │   │   │   └── Level 5: Buyer upload random photos không có guidance
│   │   └── Level 3: CS không có tool tóm tắt evidence
│   │       ├── Level 4: Thiếu AI summarization
│   │       │   └── Level 5: Chưa đầu tư NLP/image classification cho dispute
├── Quy trình (Process)
│   ├── Level 2: Seller 48h response window quá dài
│   │   ├── Level 3: SLA cứng 48h cho mọi cases
│   │   │   ├── Level 4: Không phân biệt simple vs complex
│   │   │   │   └── Level 5: Thiếu dynamic SLA framework
│   │   └── Level 3: Multiple evidence rounds không bị limit
│   │       ├── Level 4: Không có cap số lần bổ sung
│   │       │   └── Level 5: Design principle emphasis on thoroughness over speed
├── Công nghệ (Technology)
│   ├── Level 2: AI classification accuracy chưa đủ
│   │   ├── Level 3: AI phân loại sai → cases phức tạp đi vào manual
│   │   │   ├── Level 4: Training data imbalance (phức tạp > đơn giản)
│   │   │   │   └── Level 5:Dataset VN-specific chưa đủ lớn
│   │   └── Level 3: Auto-refund chưa được implement
│   │       ├── Level 4: Refund phải qua CS click manual
│   │       │   └── Level 5: Risk aversion — sợ auto-refund sai
└── Đo lường (Measurement)
    ├── Level 2: Không có SLA enforcement cho CS review
    │   ├── Level 3: CS không có KPI time-to-resolution
    │   │   ├── Level 4: Management focus vào accuracy > speed
    │   │   │   └── Level 5: No balanced scorecard for dispute team
    │   └── Level 3: Không có real-time dashboard cho pending cases
    │       ├── Level 4: Manual tracking bằng spreadsheet
    │       │   └── Level 5: Thiếu investment trong operations tooling
```

### 5-Why Analysis

**Vấn đề:** Thời gian giải quyết tranh chấp trung bình 5-7 ngày

| Level | Câu hỏi | Câu trả lời |
|-------|---------|-------------|
| Why 1 | Tại sao giải quyết mất 5-7 ngày? | CS mất 1-2 ngày review mỗi case + seller 48h response |
| Why 2 | Tại sao CS mất 1-2 ngày review? | Evidence không structured, phải đọc manual từng cái |
| Why 3 | Tại sao evidence không structured? | Buyer upload random photos, không có guided flow |
| Why 4 | Tại sao không có guided flow? | System design emphasis on flexibility over efficiency |
| Why 5 | Tại sao design như vậy? | Product team prioritize feature coverage over operational efficiency |

**Root Cause:** Thiếu structured evidence collection + không có dynamic SLA framework + CSthiếu AI-assisted tools.

## 3.2.4. Phân tích định lượng

### A. Thời gian

| STT | Hoạt động | Min | Max | Avg | Ghi chú |
|-----|-----------|-----|-----|-----|---------|
| 1 | Tạo tranh chấp + lý do | 5 phút | 30 phút | 15 phút | Evidence upload |
| 2 | Tự động thu thập dữ liệu đơn hàng | 5 giây | 30 giây | 10 giây | Automated |
| 3 | AI phân loại tranh chấp (Đơn giản/Phức tạp) | 3 giây | 15 giây | 5 giây | Automated |
| 4 | Kiểm tra lịch sử SLA | 2 giây | 10 giây | 5 giây | Automated |
| 5 | Gửi thông báo đối soát đến hai bên | 1 phút | 5 phút | 2 phút | Automated |
| 6 | Seller phản hồi (≤48h) | 1 giờ | 48 giờ | 18 giờ | SLA 48h |
| 7 | Bổ sung bằng chứng (nếu có) | 2 giờ | 5 ngày | 2 ngày | 30% cases |
| 8 | Yêu cầu bổ sung bằng chứng | 5 phút | 30 phút | 10 phút | CS action |
| 9 | CS thẩm định toàn bộ hồ sơ tranh chấp | 30 phút | 4 giờ | 1.5 giờ | Per case |
| 10 | CS ban hành quyết định xử lý | 10 phút | 30 phút | 15 phút | CS decision |
| 11 | Chuyển lên nhóm chuyên trách (Lazada Escalation) | 1 giờ | 24 giờ | 4 giờ | 20% cases |
| 12 | Hội đồng thẩm định & ra quyết định cuối | 1 ngày | 7 ngày | 3 ngày | Complex cases |

### B. Phân tích Cycle Time Probability-Weighted

| Hoạt động | Thời gian (phút) | Xác suất | Thời gian kỳ vọng (phút) | Ghi chú |
|-----------|-------------------|----------|--------------------------|---------|
| Tạo tranh chấp + lý do | 15 | 100% | 15.0 | Bắt buộc |
| Tự động thu thập dữ liệu đơn hàng | 0.17 | 100% | 0.17 | Tức thì |
| AI phân loại tranh chấp (Đơn giản/Phức tạp) | 0.08 | 100% | 0.08 | Tức thì |
| Kiểm tra lịch sử SLA | 0.08 | 100% | 0.08 | Tức thì |
| Gửi thông báo đối soát đến hai bên | 2 | 100% | 2.0 | Automated |
| Seller phản hồi (≤48h) | 1,080 (18h avg) | 100% | 1,080.0 | SLA 48h |
| Bổ sung bằng chứng (nếu có) | 2,880 (2 ngày) | 30% | 864.0 | 30% cases |
| Yêu cầu bổ sung bằng chứng | 10 | 30% | 3.0 | Chỉ khi bổ sung (only if needed) |
| CS thẩm định toàn bộ hồ sơ tranh chấp | 90 | 100% | 90.0 | Core step |
| CS ban hành quyết định xử lý | 15 | 100% | 15.0 | Decision |
| Chuyển lên nhóm chuyên trách (Lazada Escalation) | 240 (4h) | 20% | 48.0 | 20% cases |
| Hội đồng thẩm định & ra quyết định cuối | 4,320 (3 ngày) | 20% | 864.0 | 20% escalated |

**Tổng Cycle Time kỳ vọng = 2,981 phút ≈ 50 giờ ≈ 6.2 ngày làm việc (8h/ngày)**

> **Ghi chú:** Báo cáo tổng hợp (Bảng 3.7) công bố Cycle Time trung bình **5,2 ngày** tính theo ngày dương lịch, **bao gồm cả các vụ leo thang lên đến 14 ngày**; bảng trên tính **6,2 ngày làm việc (8h/ngày) theo trọng số từng bước** — chênh lệch do hiệu ứng cuối tuần/ngày lễ trong cửa sổ phản hồi 48h của Seller (50 giờ thao tác thuần ÷ 8 = 6,25 ≈ 6,2).

### C. Chi phí (per dispute)

| STT | Thành phần | Chi phí (VND) | Ghi chú |
|-----|-----------|---------------|---------|
| 1 | CS agent time | 45,000 | 0.9h × 50,000 VND/h (thao tác thực tế ~54 phút/ca; bảng CT ghi 1.5h gồm thời gian chờ phản hồi) |
| 2 | System infrastructure (AI, notification) | 3,000 | Allocated |
| 3 | Escalation cost (20% cases × extra review) | 16,000 | 20% × 80,000 VND (Tier-2 agent) |
| 4 | Payment processing fee | 1,000 | Refund execution |
| 5 | Re-work evidence rounds (30% cases) | 3,000 | 30% × 10,000 VND (extra CS time cho vòng bổ sung bằng chứng) |
| **TỔNG** | | **68,000 VND** | Per dispute (khớp Bảng 3.7 báo cáo tổng hợp) |

**Volume ước tính:** ~130,600 vụ/tháng ≈ 0,65% của ~20 triệu đơn/tháng (ước tính từ phỏng vấn vận hành CS)
**Monthly cost:** ~8.88 tỷ VND/tháng

### D. Chất lượng (Quality Metrics)

| Metric (Chỉ số) | Hiện tại (AS-IS) | Benchmark (VN e-commerce) | Gap | Mục tiêu TO-BE |
|-----------------|------------------|---------------------------|-----|----------------|
| Thời gian giải quyết trung bình (Avg Resolution Time) | 5-7 ngày | 2-3 ngày | +3-4 ngày | **1-2 ngày** |
| Tỷ lệ hài lòng Buyer (Buyer CSAT) | 3.2/5 | 4.0/5 | -0.8 | **4.3/5** |
| Tỷ lệ hài lòng Seller (Seller CSAT) | 3.5/5 | 4.0/5 | -0.5 | **4.2/5** |
| Tỷ lệ escalate lên cấp trên (Escalation Rate) | 20% | 10-12% | +8-10% | **5-8%** |
| Tỷ lệ giải quyết lần đầu (First-Contact Resolution) | 45% | 70-75% | -25-30% | **80-85%** |
| Tỷ lệ tự động giải quyết AI (AI Auto-Resolve Rate) | 5% | 25-30% | -20-25% | **40-50%** |
| Chi phí xử lý/tranh chấp (Cost per Dispute) | 68,000 VND | 80,000 VND | -12,000 (đã dưới benchmark) | **19,000 VND** |
| Tỷ lệ khiếu nại tái phát (Recurring Complaint Rate) | 12% | 5-7% | +5-7% | **2-3%** |
| Tỷ lệ khớp phân loại AI (AI Classification Accuracy) | 75% | 90% | -15% | **95%** |
| Thời gian phản hồi lần đầu (First Response Time) | 24-48h | 4-8h | +20-40h | **<2h** |

> **Ghi chú:** Các số liệu benchmark dựa trên khảo sát industry VN e-commerce 2025-2026. Mục tiêu TO-BE dựa trên mô hình cải tiến AI/automation.

## 3.2.5. Phân tích Pareto

### Bảng Vấn đề — Giả thuyết — Chi phí ảnh hưởng

| STT | Vấn đề | Giả thuyết | Chi phí ảnh hưởng/tháng (VND) | Tỷ trọng |
|-----|--------|-----------|-------------------------------|----------|
| 1 | Seller 48h response window quá dài | SLA cứng không phân biệt simple/complex | 2,500,000,000 (hold cost + buyer wait cost) | 28.2% |
| 2 | Evidence không structured → CS review manual | Thiếu guided upload + AI summarization | 2,100,000,000 (CS labor cost + rework) | 23.6% |
| 3 | Auto-resolve rate thấp 5% | AI classification accuracy chưa đủ + thiếu auto-refund | 1,800,000,000 (manual processing cost) | 20.3% |
| 4 | Escalation rate cao 20% | Clear criteria chưa có + CS thiếu authority | 1,200,000,000 (Tier-2 cost + delay) | 13.5% |
| 5 | Multiple evidence rounds không limit | Không có cap + không có structured checklist | 780,000,000 (rework + delay) | 8.8% |
| 6 | CS không có SLA enforcement | Không có KPI time-to-resolution | 500,000,000 (productivity loss) | 5.6% |
| **TỔNG** | | | **8,880,000,000** | **100%** |

### Kết luận 80/20

**Top 3 vấn đề (chiếm ~72% chi phí):**
1. Seller 48h response window (28.2%) — giải pháp: dynamic SLA 12h/24h/48h
2. Evidence không structured (23.6%) — giải pháp: guided upload + AI summarization
3. Auto-resolve rate thấp (20.3%) — giải pháp: upgrade AI + auto-refund cho cases đơn giản

→ **Giải quyết 3 vấn đề này sẽ giảm ~72% chi phí lãng phí (~6.4 tỷ VND/tháng).**

## 3.2.6. Kết luận và hướng cải tiến TO-BE

### Tóm tắt AS-IS
- Tổng cycle time kỳ vọng: ~50 giờ (6.2 ngày làm việc)
- Chi phí per dispute: ~68,000 VND (khớp Bảng 3.7)
- Bottleneck: Seller response 48h + CS manual review
- Auto-resolve rate: chỉ 5%
- Escalation rate: 20% (quá cao)

### Hướng cải tiến TO-BE

| STT | Cải tiến | Mục tiêu | Giảm chi phí (tháng) |
|-----|---------|----------|----------------------|
| 1 | Dynamic SLA: 12h (simple <200k), 24h (medium), 48h (complex) | Response time: avg 18h → 10h | -1,800 triệu VND |
| 2 | Guided evidence upload + AI summarization cho CS | CS review: 1.5h → 30 phút | -1,510 triệu VND |
| 3 | Upgrade AI classification + auto-refund cho low-risk | Auto-resolve: 5% → 40-50% | -1,290 triệu VND |
| 4 | Clear escalation criteria + CS authority increase | Escalation: 20% → 5-8% | -860 triệu VND |
| 5 | Structured evidence checklist + cap 1 round | Rework: 30% → 8% | -560 triệu VND |
| 6 | SLA enforcement dashboard cho CS team | Time-to-assign: 4-24h → 1h | -360 triệu VND |
| **TỔNG GIẢM (riêng lẻ)** | | | **-6,380 triệu VND/tháng** |

> **Ghi chú:** Tổng giảm riêng lẻ của 6 sáng kiến = -6.380 triệu VND/tháng ≈ **-6,38 tỷ VND/tháng (-72%)** so với chi phí AS-IS 8,88 tỷ VND — khớp với bảng "So sánh AS-IS vs TO-BE" bên dưới (8,88 tỷ → 2,5 tỷ).

### So sánh AS-IS vs TO-BE

| Metric | AS-IS | TO-BE | Cải thiện |
|--------|-------|-------|-----------|
| Avg resolution time | 5-7 ngày | 1-2 ngày | -60-70% |
| Auto-resolve rate | 5% | 40-50% | +35-45 điểm % |
| Escalation rate | 20% | 5-8% | -60-75% |
| First-contact resolution | 45% | 80-85% | +35-40 điểm % |
| Chi phí per dispute | 68,000 VND | 19,000 VND | -72% |
| Monthly cost | 8.88 tỷ VND | 2.5 tỷ VND | -6.38 tỷ VND (-72%) |

> **Ghi chú:** Chi phí TO-BE **19.000 VNĐ/ca** quy đổi trên cùng cơ sở ~130.600 ca/tháng: 19.000 × 130.600 ≈ 2,48 tỷ → làm tròn **2,5 tỷ VNĐ/tháng** (tương ứng mức giảm -6,38 tỷ VND = -72% so với AS-IS).

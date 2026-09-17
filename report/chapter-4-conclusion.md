# CHƯƠNG 4: KẾT LUẬN VÀ ĐỀ XUẤT CẢI TIẾN TO-BE

## 4.1. Tổng kết phát hiện (Findings Summary)

### 4.1.1. Điểm mạnh (Strengths)

| STT | Điểm mạnh | Bằng chứng |
|-----|-----------|-----------|
| 1 | Hệ sinh thái logistics mạnh (LEX) | LEX Express tích hợp sâu với OMS, cùng ngày tại HN/HCM |
| 2 | LazMall — hàng chính hãng 100% | Khác biệt hóa so với Shopee/TikTok, cam kết hoàn tiền nếu hàng giả |
| 3 | Hệ sinh thái Alibaba (TMall/Gmarket) | Cross-border commerce, AI tech stack mạnh |
| 4 | Escrow system an toàn | Bảo vệ cả Buyer và Seller |
| 5 | Tất cả 10 quy trình đạt SOUND | Đảm bảo kỹ thuật, không có deadlock |
| 6 | Đội ngũ CSKH đa kênh | Chat, hotline, email, social — chatbot AI triage |

### 4.1.2. Điểm yếu (Weaknesses) — có số liệu

| STT | Điểm yếu | Số liệu | So sánh |
|-----|----------|---------|---------|
| 1 | Thị phần giảm mạnh | 10-18% (2024), từ ~22% (2022) | Shopee ~62-70%, TikTok ~12-20% |
| 2 | Delivery chậm hơn | 3-5 ngày (nội thành) | Shopee 2-3 ngày |
| 3 | Unit economics âm | -28,420 VND/đơn (est.) | COD 60-70% + failed delivery 15-20% |
| 4 | Return/refund chậm | 7-15 ngày | Lazada 5-7 ngày |
| 5 | Seller churn cao | 7,000+ seller rời H1/2025 | Metric.vn |
| 6 | CSAT thấp | 6.0-6.8/10 | Lazada 7.2-7.8/10 |
| 7 | Layoffs làm giảm năng lực | 25-50% nhân sự SEA (01/2024) | Reuters/CNA |

## 4.2. Đề xuất TO-BE

### 4.2.1. Mô hình mục tiêu (To-Be Vision)

```
┌───────────────────────────────────────────────────────────────┐
│   CORE IMPROVEMENT THESIS: "Automate + Personalize + Protect" │
│                                                               │
│   T1. AUTOMATE  → Nâng tự động hóa từ 40-70% lên 85%+         │
│   T2. PERSONALIZE → AI-driven UX, pricing, logistics routing  │
│   T3. PROTECT   → Giữ vững LazMall authentic + escrow trust   │
│                                                               │
│   KPI mục tiêu 2027:                                          │
│   • Thị phần: 10-18% → 18-25%                                 │
│   • Refund time: 7-15 ngày → 3-5 ngày                         │
│   • COD failure: 15-20% → <8%                                 │
│   • Seller churn: 5-10%/quý → <3%                             │
│   • CSAT: 6.0-6.8 → 7.5/10                                    │
└───────────────────────────────────────────────────────────────┘
```

### 4.2.2. Lộ trình cải tiến 3 giai đoạn

#### GIAI ĐOẠN 1: Ngắn hạn (0-3 tháng) — Quick Wins

| STT | Sáng kiến | Quy trình | Chi phí ước tính | Kỳ vọng |
|-----|-----------|-----------|------------------|---------|
| 1 | **Auto-accept đơn sau 2h** cho seller chuẩn | Xử lý đơn hàng | Thấp (config) | Giảm 40% lost sale do delay |
| 2 | **Auto-refund <100k VND** (trusted buyer) | Hoàn trả & hoàn tiền | Thấp (rule engine) | Giảm 30% refund time |
| 3 | **Pre-call/SMS trước khi giao COD** | Logistics | Trung bình (telecom) | Giảm COD rejection 15→10% |
| 4 | **Email/SMS reminder seller** (1h SLA) | Xử lý đơn hàng | Thấp | Tăng confirm rate |
| 5 | **1-question CSAT** sau mỗi ticket | CSKH | Thấp | Feedback rate +50% |
| 6 | **AI dispute pre-screening** (evidence score) | Tranh chấp | Trung bình (ML) | Giảm 50% review time |
| 7 | **Voucher/commission hỗ trợ seller chiến lược** | Marketing | Trung bình | Giảm churn 2% |

**Tác động gộp:** Giảm 20-30% chi phí vận hành, tăng CSAT +0.5-1.0

#### GIAI ĐOẠN 2: Trung hạn (3-6 tháng) — Process Redesign

| STT | Sáng kiến | Quy trình | Chi phí | Kỳ vọng |
|-----|-----------|-----------|---------|---------|
| 8 | **AI listing quality scoring** (mô tả vs ảnh) | Quản lý chất lượng SP | Cao (ML pipeline) | Giảm return rate 8-12%→6% |
| 9 | **Tiered dispute resolution** (auto <200k) | Tranh chấp | Trung bình | Giảm 60% resolution time |
| 10 | **Chatbot 2.0** (55% deflection) | CSKH | Cao (NLP) | Giảm 30% CS cost |
| 11 | **Smart COD routing** (xác suất accept cao) | Logistics | Trung bình | Giảm failed delivery 20% |
| 12 | **Seller score-based benefits** (giảm fee) | Quản lý seller | Trung bình | Tăng retention |
| 13 | **Unified seller dashboard** (real-time) | Quản lý seller | Trung bình | Tăng seller engagement |

**Tác động gộp:** Tự động hóa trung bình 40-70% → 70-85%, refund 7-15 ngày → 5-7 ngày

#### GIAI ĐOẠN 3: Dài hạn (6-12 tháng) — Platform Transformation

| STT | Sáng kiến | Quy trình | Chi phí | Kỳ vọng |
|-----|-----------|-----------|---------|---------|
| 14 | **AI/ML Fraud Engine 2.0** (real-time) | Thanh toán | Rất cao | Giảm fraud loss 50% |
| 15 | **Full LEX route optimization + FBL expansion** | Logistics | Rất cao | Nội thành <24h, giảm cost 15% |
| 16 | **Cross-border deep integration** (TMall 2.0) | Marketing, đơn hàng | Rất cao | Mở rộng catalog, GMV +20% |
| 17 | **Seller incubation program** (chống churn) | Quản lý seller | Trung bình | Tăng seller base 20% |
| 18 | **Adaptive pricing engine** (COD vs online incentive) | Thanh toán | Cao | Chuyển 20% COD → online payment |

**Tác động gộp:** Tự động hóa 85%+, thị phần 18-25%, unit economics dương

### 4.2.3. Ma trận đối chiếu AS-IS → TO-BE

| Tiêu chí | AS-IS (hiện tại) | TO-BE (mục tiêu) | Delta |
|----------|-------------------|-------------------|-------|
| Tự động hóa trung bình | 45-55% | 85%+ | +30-40% |
| Refund time | 7-15 ngày | 3-5 ngày | -60% |
| Dispute resolution | 5-7 ngày | 2-3 ngày | -60% |
| COD failure | 15-20% | <8% | -50% |
| Delivery (nội thành) | 3-5 ngày | 1-2 ngày | -50% |
| Seller churn | 5-10%/quý | <3%/quý | -60% |
| CSAT | 6.0-6.8/10 | 7.5/10 | +0.7-1.5 |
| Cost/đơn (est.) | -28,420 VND | Dương (+) | Unit economics |

## 4.3. Rủi ro triển khai đề xuất (Implementation Risks)

| ID | Rủi ro | Xác suất | Tác động | Mitigation |
|----|--------|----------|----------|------------|
| IR1 | Seller phản đối auto-accept | 30% | TB | Chỉ áp dụng seller rating tốt |
| IR2 | Auto-refund bị lạm dụng | 20% | Cao | Chỉ trusted buyer score >80 |
| IR3 | Chi phí AI triển khai cao | 40% | TB | Phân kỳ, ưu tiên quick wins |
| IR4 | Nhân sự (sau layoffs) không đủ | 50% | Cao | Ưu tiên automation trước |
| IR5 | Thị trường tiếp tục ép giá (TikTok) | 60% | Cao | Khác biệt hóa LazMall + logistics |
| IR6 | Thay đổi chính sách (quy định TMĐT) | 25% | TB | Theo dõi sát luật bảo vệ người tiêu dùng |

## 4.4. Hạn chế của nghiên cứu

1. **Không có internal access:** Toàn bộ phân tích dựa trên external observation + chính sách công khai
2. **Data estimates:** Số liệu định lượng là industry benchmarks, không phải actual Lazada data
3. **Scope giới hạn:** Đã phân tích chi tiết toàn bộ 10 quy trình bằng BPMN 2.0
4. **Static snapshot:** Quy trình Lazada thay đổi liên tục; mô hình có thể outdated nhanh
5. **Giả định phỏng vấn:** Câu hỏi phỏng vấn là template, chưa thực hiện thực tế

## 4.5. Hướng phát triển tương lai (Future Work)

- **Benchmark định lượng chi tiết** với Lazada/TikTok/Tiki từng quy trình
- **Phân tích nâng cao:** Discrete-event simulation (SimPy/Arena) để kiểm chứng TO-BE
- **Data analytics:** Phân tích dữ liệu GMV, conversion, return rate theo category
- **Tính toán ROI** cụ thể cho từng sáng kiến TO-BE
- **Nghiên cứu thực tế:** Phỏng vấn seller/buyer, đo thời gian thực trên app
- **Mở rộng mô hình hóa** cho 4 quy trình còn lại (thanh toán, logistics, chất lượng SP, IT)

## 4.6. Bài học kinh nghiệm (Lessons Learned)

1. **COD là con dao hai lưỡi:** Dễ tiếp cận người mua không thẻ nhưng tạo chi phí ẩn lớn (rejection, reverse logistics, đối soát). Cần chiến lược chuyển dịch dần sang online payment.
2. **Tự động hóa ≠ thay người:** Mục tiêu là tăng năng lực xử lý (processing capacity), không phải cắt giảm nhân sự — đặc biệt khi đang thiếu hụt nguồn lực.
3. **Trust là tài sản quan trọng nhất:** LazMall authentic + escrow là khác biệt cốt lõi. Mọi automation phải giữ vững trust này (human-in-the-loop cho quyết định lớn).
4. **Quy trình và dữ liệu đi cùng nhau:** Muốn AI hiệu quả, phải chuẩn hóa dữ liệu quy trình (event logs, SLA tracking) trước.
5. **Ưu tiên theo tác động:** Áp dụng Pareto — tập trung vào 20% hoạt động tạo ra 80% chi phí/lãng phí (COD rejection, seller delay, return inspection).

## 4.7. Kết luận cuối cùng

Lazada Việt Nam sở hữu nền tảng quy trình **SOUND về mặt kỹ thuật** (10/10 quy trình đạt Petri Net soundness) nhưng đang đối mặt với **thách thức cạnh tranh nghiêm trọng** về tốc độ, chi phí và trải nghiệm. Ba vấn đề cốt lõi — **COD-dominated economy, seller churn, và tự động hóa thấp** — là gốc rễ của phần lớn các pain point khác.

**Đề xuất ưu tiên hàng đầu (Priority Roadmap):**
1. **Tháng 0-3:** Auto-refund <100k + auto-accept đơn 2h + pre-call COD (chi phí thấp, tác động nhanh)
2. **Tháng 3-6:** AI listing scoring + tiered dispute resolution + Chatbot 2.0 (tự động hóa nhảy vọt)
3. **Tháng 6-12:** Fraud Engine 2.0 + LEX route optimization + cross-border deep integration (nền tảng dài hạn)

Với việc tận dụng thế mạnh logistics (LEX) và thương hiệu chính hãng (LazMall), cùng lộ trình tự động hóa có trọng tâm, Lazada có thể chuyển hóa từ vị thế "kẻ bám đuổi" sang "người dẫn đầu về chất lượng dịch vụ" trong giai đoạn 2026-2027.

# CHƯƠNG 2: HỆ THỐNG QUY TRÌNH NGHIỆP VỤ LAZADA VIỆT NAM

## 2.1. Kiến trúc quy trình nghiệp vụ

Hệ thống quy trình của Lazada được phân loại theo mô hình 3 tầng (House Diagram) dựa trên **APQC Process Classification Framework (PCF):**
- **Tầng 1 (trên):** Quy trình Quản lý — định hướng, giám sát, kiểm soát
- **Tầng 2 (giữa):** Quy trình Cốt lõi — tạo giá trị trực tiếp cho khách hàng
- **Tầng 3 (dưới):** Quy trình Hỗ trợ — hỗ trợ 2 tầng trên hoạt động hiệu quả

## 2.2. Danh sách 10 quy trình nghiệp vụ

### 2.2.1. Quy trình Quản lý (Management Processes) — 3 quy trình

| # | Quy trình | Mô tả | Actors | Customer |
|---|-----------|-------|--------|----------|
| 1 | **Quản lý nhà bán hàng** | Onboarding seller, KYC, đánh giá rating, xử lý vi phạm, Lazada University | Seller Ops, Compliance, Seller | Seller |
| 2 | **Quản lý chất lượng sản phẩm** | Listing review, QC, chống hàng giả, LazMall brand guarantee | QC Team, Seller, IP Team, Brand owners | Buyer |
| 3 | **Quản lý tranh chấp & khiếu nại** | Dispute resolution, mediation, escrow management, fraud detection | Dispute Team, CS, Buyer, Seller, Finance | Buyer/Seller |

### 2.2.2. Quy trình Cốt lõi (Core Processes) — 4 quy trình

| # | Quy trình | Mô tả | Actors | Customer |
|---|-----------|-------|--------|----------|
| 4 | **Xử lý đơn hàng online** ⭐ | Cart → Checkout → Payment → Fulfillment → Delivery → COD → Settlement | Buyer, System, Seller, Warehouse, LEX/3PL, Payment | Buyer |
| 5 | **Thanh toán & đối soát** | Payment gateway, COD collection, reconciliation, escrow release | Payment Team, Finance, 3PL | Buyer/Seller |
| 6 | **Vận chuyển & giao nhận** | LEX pickup → Sorting → Transport → Last-mile delivery | Warehouse, LEX, 3PL, Courier, Buyer | Buyer |
| 7 | **Hoàn trả & hoàn tiền** | Return request → Inspection → Refund processing | Buyer, CS, Logistics, Finance | Buyer |

### 2.2.3. Quy trình Hỗ trợ (Support Processes) — 3 quy trình

| # | Quy trình | Mô tả | Actors | Customer |
|---|-----------|-------|--------|----------|
| 8 | **Chăm sóc khách hàng** | Chat, hotline, email, social — Chatbot → Agent → Tier-2 | CS Agents, Chatbot | Buyer/Seller |
| 9 | **Marketing & promotions** | Campaign planning, voucher/flash sale, launch, monitoring | Marketing, Finance, Seller | Buyer |
| 10 | **Quản lý hệ thống IT** | Platform uptime, bug fixes, AI/ML deployment | DevOps, Engineering | Internal |

## 2.3. Ma trận tương tác giữa các quy trình

| Trigger | Quy trình gốc | Kích hoạt quy trình phụ | Loại liên kết |
|---------|--------------|------------------------|---------------|
| Seller đăng ký | Quản lý nhà bán hàng | Marketing (onboard campaign) | Kế tiếp |
| Buyer đặt hàng | Xử lý đơn hàng | Thanh toán → Vận chuyển | Song song |
| COD collection | Thanh toán & đối soát | Vận chuyển (COD cash flow) | Song song |
| Giao hàng thất bại | Vận chuyển & giao nhận | Xử lý đơn hàng (retry/cancel) | Quay lại |
| Buyer khiếu nại | Xử lý đơn hàng | Quản lý tranh chấp | Rẽ nhánh |
| Tranh chấp thắng | Quản lý tranh chấp | Hoàn trả & hoàn tiền | Kế tiếp |
| Return request | Hoàn trả & hoàn tiền | CSKH (follow-up CSAT) | Kế tiếp |
| Campaign launch | Marketing | Xử lý đơn hàng (volume spike) | Song song |

**Insight:** Quy trình xử lý đơn hàng (order processing) là trung tâm — nó kích hoạt và bị kích hoạt bởi hầu hết các quy trình khác. COD dominant (~60-70% giao dịch) tạo ra mối liên hệ đặc biệt giữa xử lý đơn hàng và đối soát thanh toán.

## 2.4. Sơ đồ kiến trúc nghiệp vụ

```
┌─────────────────────────────────────────────────────────────────┐
│            QUY TRÌNH QUẢN LÝ (Management)                       │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐           │
│  │ 1. Quản lý   │  │ 2. Quản lý   │  │ 3. Quản lý   │           │
│  │   seller     │  │ CL sản phẩm  │  │ tranh chấp   │           │
│  └──────────────┘  └──────────────┘  └──────────────┘           │
├─────────────────────────────────────────────────────────────────┤
│            QUY TRÌNH CỐT LÕI (Core)                             │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐           │
│  │4. Xu ly  │ │5. Thanh  │ │6. Van    │ │7. Hoan   │           │
│  │don hang⭐ │ │toan&DS   │ │chuyen    │ │tra&Refund│           │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘           │
├─────────────────────────────────────────────────────────────────┤
│            QUY TRÌNH HỖ TRỢ (Support)                          │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐           │
│  │ 8. CSKH      │  │ 9. Marketing │  │10. Quản ly IT│           │
│  └──────────────┘  └──────────────┘  └──────────────┘           │
└─────────────────────────────────────────────────────────────────┘
```

## 2.5. Kiến trúc hệ thống kỹ thuật

### 2.5.1. Tổng quan kiến trúc

Lazada vận hành nền tảng TMĐT dựa trên microservices architecture kế thừa từ Alibaba tech stack.

```
┌─────────────────────────────────────────────────────────────────┐
│                      USER LAYER                                  │
│   Lazada App (Mobile)    Lazada Website    Seller Center API     │
└──────────────┬───────────────────────────────┬──────────────────┘
               │                               │
┌──────────────▼───────────────────────────────▼──────────────────┐
│                      API GATEWAY                                 │
│    Rate limiting · Auth · Routing · Logging · AI Search          │
└──────┬────────┬────────┬────────┬────────┬────────┬─────────────┘
       │        │        │        │        │        │
┌──────▼──┐ ┌──▼──────┐ ┌▼──────┐ ┌▼──────┐ ┌▼─────┐ ┌▼────────┐
│ Order   │ │Payment  │ │Product│ │User   │ │Logist│ │AI/ML    │
│ Service │ │Service  │ │Service│ │Service│ │ics   │ │Engine   │
│         │ │         │ │       │ │       │ │Svc   │ │         │
│ Cart/   │ │Escrow/  │ │Search/│ │Auth/  │ │LEX/  │ │Search/  │
│ Checkout│ │COD/Wallet│ │Catalog│ │Profile│ │3PL   │ │Reco/Pri │
└────┬────┘ └────┬────┘ └──┬────┘ └──┬───┘ └──┬───┘ └────┬────┘
     │           │         │         │         │          │
┌────▼───────────▼─────────▼─────────▼─────────▼──────────▼───────┐
│                    DATA LAYER                                     │
│   MySQL/PostgreSQL (OLTP)   Redis (Cache)   ElasticSearch (Search)│
│   Kafka (Event Bus)   Alibaba Cloud Analytics   S3 (Object)      │
└──────────────────────────────────────────────────────────────────┘
```

### 2.5.2. Ma trận hệ thống hỗ trợ quy trình

| Quy trình | Hệ thống hỗ trợ chính | Tự động hóa |
|-----------|----------------------|-------------|
| **Xử lý đơn hàng ⭐** | OMS, WMS, TMS, Payment Gateway, Escrow | ~70% |
| **Hoàn trả & refund** | Return Management, Inspection Tracking, Refund Engine | ~45% |
| **Quản lý seller** | Seller Center, Performance Dashboard, KYC Engine | ~55% |
| **Quản lý tranh chấp** | Dispute Management, Case System, AI Classifier | ~40% |
| **CSKH** | CRM, Chatbot (NLP), Ticket System | ~45% |
| **Marketing** | Campaign Hub, Analytics BI, Voucher Engine | ~50% |

**Insight:** Quy trình hoàn trả và quản lý tranh chấp có mức tự động hóa thấp nhất (40-45%) — đây là cơ hội cải tiến lớn nhất. AI pre-screening evidence có thể nâng tự động hóa lên 70%+.

## 2.6. Tổng hợp Quy trình cốt lõi: Xử lý đơn hàng online

### 2.6.1. Mô tả tổng quan

Quy trình xử lý đơn hàng online là quy trình phức tạp nhất và quan trọng nhất của Lazada, bắt đầu từ thời điểm Buyer thêm sản phẩm vào giỏ hàng và kết thúc khi đơn hàng được hoàn tất (giao thành công + thanh toán) hoặc bị hủy/hoàn trả.

**Các tác nhân tham gia:**
- **Buyer:** Người mua hàng trên Lazada App/Web
- **Lazada System:** OMS, Payment, Inventory, Notification ( tự động)
- **Seller:** Người bán hàng (FBS hoặc FBL)
- **Warehouse / Fulfillment:** Kho hàng Lazada (FBL) hoặc kho seller
- **LEX / 3PL:** Đơn vị vận chuyển (Lazada Express, GHN, GHTK, J&T, Ninja Van)
- **Payment Gateway:** VNPay, OnePay, Napas, MoMo, ZaloPay
- **COD Provider:** Đơn vị thu hộ COD

### 2.6.2. Mô hình BPMN

*(File: processes/03-order-processing.bpmn — importable vào Camunda Modeler / Bizagi)*

**Thống kê mô hình AS-IS:**
- Số lanes: 7 (Buyer, Seller, Lazada System, Warehouse, LEX/3PL, Payment, Finance)
- Số activities: 26
- Số gateways: 17 (17 XOR)
- End events: 3 (Completed, Auto-cancelled, Return-initiated)
- Độ phức tạp: Rất cao

### 2.6.3. Kiểm chứng Petri Net (Soundness Verification)

**Bảng tổng hợp kết quả Soundness cho toàn bộ 10 quy trình:**

| Process | Places (P) | Transitions (T) | Markings | Option to Complete | Proper Completion | No Dead Transitions | Overall |
|---------|------------|-----------------|----------|--------------------|--------------------|--------------------|---------|
| 01-seller-management | 42 | 29 | 42 | PASS | PASS | PASS | SOUND |
| 02-dispute-management | 37 | 27 | 37 | PASS | PASS | PASS | SOUND |
| 03-order-processing | 56 | 43 | 56 | PASS | PASS | PASS | SOUND |
| 04-return-refund | 42 | 30 | 42 | PASS | PASS | PASS | SOUND |
| 05-customer-service | 39 | 29 | 39 | PASS | PASS | PASS | SOUND |
| 06-marketing | 46 | 35 | 46 | PASS | PASS | PASS | SOUND |
| 07-hr-training | 40 | 36 | 40 | PASS | PASS | PASS | SOUND |
| 08-payment-settlement | 34 | 24 | 38 | PASS | PASS | PASS | SOUND |
| 09-logistics-delivery | 37 | 31 | 42 | PASS | PASS | PASS | SOUND |
| 10-it-platform | 39 | 28 | 39 | PASS | PASS | PASS | SOUND |

> **Kết luận:** Tất cả 10 quy trình đều đạt **SOUND** — thỏa mãn 3 thuộc tính soundness theo van der Aalst (1998).

**Giải thích:**
- **Option to Complete:** Mọi marking reachable đều có đường đến end event
- **Proper Completion:** Không có residual token trong places ngoài final places
- **No Dead Transitions:** Mọi transition đều fireable trong ít nhất 1 reachable marking

## 2.7. Kiến trúc Logistics Lazada VN

### 2.7.1. Ma trận Logistics Options

| Model | Mô tả | Ưu điểm | Nhược điểm |
|-------|-------|---------|------------|
| **FBL (Fulfilled by Lazada)** | Seller gửi hàng vào kho Lazada; Lazada pick, pack, ship | Nhanh hơn, higher ranking, badge "Fulfilled by Lazada" | Chi phí lưu kho, yêu cầu tồn kho cao |
| **FBS + LEX** | Seller tự pack, giao cho LEX pickup | Phổ biến nhất, tích hợp tốt | Phụ thuộc vào LEX availability |
| **FBS + 3PL** | Seller tự giao cho GHN/GHTK/J&T | seller control chi phí | Phức tạp hơn, phải manage nhiều 3PL |

### 2.7.2. LEX Service Levels

| Service | Timeframe | Vùng áp dụng |
|---------|-----------|--------------|
| Standard Delivery | 2-5 ngày (nội thành), 5-7 ngày (ngoại thành) | Toàn quốc |
| Express Delivery | 1-2 ngày | Nội thành lớn |
| Same-Day Delivery | Trong ngày (4-8 giờ) | HN, HCMC nội thành (FBL only) |

### 2.7.3. 3PL Partners tại Việt Nam

| 3PL | COD Cycle | COD Fee | Đặc điểm |
|-----|-----------|---------|-----------|
| LEX | Daily deposit | Included | Seamless integration |
| GHN | 2-3 business days | 1-1.5% | Reliable |
| GHTK | 2-4 business days | 1-1.5% | Cheapest option |
| J&T Express | 1-2 business days | 1.5-2% | Fast COD settlement |
| Viettel Post | 3-5 business days | 1-2% | Rural coverage |

## 2.8. Tổng hợp Pain Points Cross-Cutting

| Pain Point | Quy trình ảnh hưởng | Mức độ | Mô tả |
|------------|---------------------|--------|-------|
| COD dominates (~60-70%) | Payment, Settlement, Logistics | **Cao** | Cash-intensive, reconciliation phức tạp |
| Seller delay confirm (24-48h) | Order Processing | **Cao** | Auto-cancel → lost sale |
| Failed delivery 15-20% | Logistics, Order Processing | **Cao** | COD rejection rate cao |
| Return abuse | Return & Refund, Dispute | **Cao** | Buyer mua trả nhiều |
| Dispute resolution chậm (3-7 ngày) | Dispute Management | **Trung bình** | Buyer & seller frustration |
| Inspection time dài (3-5 ngày) | Return & Refund | **Trung bình** | Buyer chờ đợi lâu |
| Late dispatch from seller | Order Processing, Seller Rating | **Trung bình** | Giảm seller score |
| COD reconciliation complexity | Payment & Settlement | **Trung bình** | Cash deposit mismatch |

## 2.9. Technology Stack Summary

| Technology Layer | Systems | Vai trò |
|-----------------|---------|---------|
| **Order Management** | OMS, Cart & Checkout Engine | Quản lý vòng đời đơn hàng |
| **Payment** | Payment Gateway, Escrow System, COD Collection | Xử lý thanh toán, ký quỹ |
| **Logistics** | TMS, WMS, Tracking System, Route Optimization | Quản lý vận chuyển, kho |
| **Quality** | QC Management, Inspection Tracking, AI detection | Kiểm soát chất lượng |
| **Seller Management** | Seller Center Portal, Performance Dashboard, Rating Algorithm | Quản lý seller lifecycle |
| **Customer Service** | Help Center, Chat System, Dispute Resolution | Hỗ trợ khách hàng |
| **Fraud Detection** | AI/ML Fraud Engine, Device Fingerprinting, Behavioral Analytics | Chống gian lận |
| **Finance** | Settlement Engine, Wallet System, Reconciliation Engine | Đối soát, thanh toán |
| **AI/ML** | Search Engine, Recommendation, Personalization, NLP Chatbot | Trí tuệ nhân tạo |

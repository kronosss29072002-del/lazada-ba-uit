# CHƯƠNG 3: MÔ HÌNH HÓA VÀ PHÂN TÍCH QUY TRÌNH LAZADA VIỆT NAM

## 3.1. Quy trình Xử lý đơn hàng online (Core Process) ⭐

### 3.1.1. Mô tả quy trình

Quy trình xử lý đơn hàng online là quy trình cốt lõi nhất của Lazada, bắt đầu từ thời điểm Buyer thêm sản phẩm vào giỏ hàng và kết thúc khi đơn hàng hoàn tất (giao thành công + thanh toán) hoặc bị hủy/hoàn trả.

**Các tác nhân tham gia:**
- **Buyer:** Người mua hàng trên Lazada App/Web
- **Lazada System:** OMS, Payment, Inventory, Notification (tự động)
- **Seller:** Người bán hàng (FBS hoặc FBL)
- **Warehouse / Fulfillment:** Kho hàng Lazada (FBL) hoặc kho seller
- **LEX / 3PL:** Đơn vị vận chuyển (Lazada Express, GHN, GHTK, J&T, Ninja Van)
- **Payment Gateway:** VNPay, OnePay, Napas, MoMo, ZaloPay
- **COD Provider:** Đơn vị thu hộ COD

**Đối tượng khách hàng:** Buyer (người kích hoạt và hưởng lợi ích từ quy trình)

**Kết quả có thể xảy ra:**
- Giao hàng thành công → Buyer nhận hàng, seller nhận tiền (COD hoặc Escrow release)
- Hủy đơn (Seller từ chối / hết hàng / không xác nhận trong SLA) → Refund cho Buyer
- Giao hàng thất bại (2-3 lần attempt) → Hoàn hàng về seller, trigger Return flow
- Khiếu nại/Tranh chấp → Chuyển sang Quy trình Quản lý Tranh chấp

### 3.1.2. Mô hình BPMN

*(File BPMN 2.0 XML: `processes/03-order-processing.bpmn` — importable vào Camunda Modeler / Bizagi. TO-BE: `processes-to-be/03-order-processing-tobe.bpmn`)*

**Thống kê mô hình AS-IS:**
- Số lanes: 7 (Buyer, Seller, Lazada System, Warehouse, LEX/3PL, Payment, Finance)
- Số activities: 26
- Số gateways: 17 (17 XOR)
- End events: 3 (Completed, Auto-cancelled, Return-initiated)
- Places (WF-net): 56, Transitions: 43, Markings: 56

### 3.1.3. Kiểm chứng Soundness

Áp dụng phương pháp WF-net (van der Aalst, 1998), quy trình 03-order-processing đạt **SOUND** — thỏa mãn cả 3 thuộc tính:

| Property | Result | Ghi chú |
|----------|--------|---------|
| Option to Complete | PASS | 3/3 paths reach end event |
| Proper Completion | PASS | Residual tokens = 0 |
| No Dead Transitions | PASS | 43/43 transitions fireable |

**Các loop trong quy trình:**
- Retry delivery (≤3 lần): bounded by DataObject `retryCount` + XOR-gateway `Gate_RetryLimit`
- Seller confirmation timeout (24-48h): timer event trigger auto-cancel

### 3.1.4. Phân tích định tính

#### A. Phân tích giá trị gia tăng (Value-Added Analysis)

| STT | Hoạt động | VA | BVA | NVA | Giải thích |
|-----|-----------|----|-----|-----|------------|
| 1 | Buyer thêm SP vào giỏ hàng & checkout | ✓ | | | KH sẵn sàng mua |
| 2 | System validate đơn hàng | | ✓ | | Cần để prevent fraud |
| 3 | Payment processing (online) | | ✓ | | Cần cho transaction |
| 4 | Fraud check tự động | | ✓ | | Prevent gian lận |
| 5 | Kiểm tra tồn kho real-time | ✓ | | | Prevent oversell |
| 6 | Seller xác nhận đơn (24-48h) | ✓ | | | KH cần xác nhận từ seller |
| 7 | Seller đóng gói sản phẩm | ✓ | | | KH cần SP được bảo vệ |
| 8 | QC inspection tại kho | | ✓ | | Đảm bảo đúng SKU |
| 9 | LEX/3PL pickup & sorting | ✓ | | | Vận chuyển cần thiết |
| 10 | Last-mile delivery | ✓ | | | Giao hàng đến KH |
| 11 | COD collection (nếu COD) | | ✓ | | Cần cho COD transactions |
| 12 | Auto-confirm sau 7 ngày | | ✓ | | Protect seller nếu buyer quên |
| 13 | Escrow release & settlement | | ✓ | | Giải ngân cho seller |

**Tỷ lệ VA/BVA/NVA:**
- VA: 7/13 (54%)
- BVA: 6/13 (46%)
- NVA: 0/13 (0%)

→ **Nhận xét:** Quy trình xử lý đơn hàng có tỷ lệ NVA rất thấp (0%), cho thấy tất cả hoạt động đều tạo giá trị trực tiếp hoặc gián tiếp. Cải tiến nên tập trung vào tối ưu BVA thay vì loại bỏ NVA.

#### B. Phân tích lãng phí (Waste Analysis)

| STT | Hoạt động | Lãng phí | Mô tả | Giải pháp |
|-----|-----------|----------|-------|-----------|
| 1 | Chờ Seller xác nhận đơn (24-48h) | Hold | Hold time 24-48 giờ nếu seller offline | Auto-accept sau 2h + penalty |
| 2 | COD rejection (15-20%) | Overdo | Reverse logistics cost | Pre-call/SMS trước khi giao |
| 3 | Split shipment confusion | Overdo | Buyer không hiểu tại sao nhận nhiều gói | UX improvement, grouped notification |
| 4 | Manual tracking number entry | Move | Copy-paste từ 3PL portal | API auto-sync tracking |

**Tổng lãng phí identified:** 4 activities — Hold (25%), Overdo (50%), Move (25%)

### 3.1.5. Phân tích định lượng

#### A. Định lượng thời gian (Probability-Weighted)

**Bảng thời gian hoạt động:**

| ID | Hoạt động | Thời gian ($T_i$) | Loại |
|----|-----------|-------------------|------|
| A1 | Buyer checkout | 3 phút | VA |
| A2 | System processing + Fraud check | 3 giây | BVA |
| A3 | Payment verification | 10 giây | BVA |
| A4 | Seller xác nhận đơn | 24 giờ (max 48h) | VA |
| A5 | Seller đóng gói + Warehouse QC | 12 giờ (avg) | VA |
| A6 | LEX/3PL pickup + sorting | 12 giờ (avg) | VA |
| A7 | Vận chuyển nội thành | 2 ngày | VA |
| A8 | Last-mile delivery attempt | 30 phút | VA |
| A9 | Auto-confirm window | 7 ngày | BVA |

**Phân nhánh xác suất (Delivery outcomes):**

| Nhánh | Xác suất ($P_j$) | Thời gian thêm | Ghi chú |
|-------|------------------|----------------|--------|
| Success (lần 1) | 80% | 0 | Best case |
| Retry 1 (lần 2) | 10% | +1 ngày | COD rejection / vắng nhà |
| Retry 2 (lần 3) | 5% | +2 ngày | Persistent issue |
| Failed (hoàn về) | 5% | +5 ngày | Return to seller |

**Tính toán Cycle Time (CT):**

$$CT = (3 \text{ phút} + 3 \text{ giây} + 10 \text{ giây}) + 24 \text{ giờ} + 12 \text{ giờ} + 12 \text{ giờ} + 2 \text{ ngày} + 30 \text{ phút} + 7 \text{ ngày}$$
$$+ 0.80 \times 0 + 0.10 \times 1 \text{ ngày} + 0.05 \times 2 \text{ ngày} + 0.05 \times 5 \text{ ngày}$$

$$CT = 33.5 \text{ giờ} + 7 \text{ ngày} + 0.35 \text{ ngày} \approx 8.4 \text{ ngày} \approx 201.6 \text{ giờ}$$

**Thời gian xử lý thực (PT - chỉ tính VA + BVA):**
$$PT = 3 \text{ phút} + 13 \text{ giây} + 30 \text{ phút} \approx 33.2 \text{ phút} \approx 0.55 \text{ giờ}$$

**Hiệu suất thời gian:**
$$\text{Efficiency} = \frac{PT}{CT} \times 100\% = \frac{0.55}{201.6} \times 100\% = 0.27\%$$

**Nhận xét:** Hiệu suất 0.27% cho thấy 99.73% thời gian là chờ đợi — thấp hơn cả benchmark Lazada (~0.63%) do seller confirmation window dài hơn (24-48h vs 2-24h) và COD-dominated workflow phức tạp hơn.

#### B. Định lượng chi phí (per order)

**Giả định:** Average Order Value (AOV) = 280,000 VND

| STT | Thành phần chi phí | Chi phí/đơn | Ghi chú |
|-----|-------------------|-------------|--------|
| 1 | Infrastructure (server, CDN) | 120 VND | Allocated per order |
| 2 | Payment gateway fee | 2,000 VND | ~2% transaction |
| 3 | COD collection fee (65% orders) | 1,300 VND | 65% × 2% × 100,000 avg COD |
| 4 | Seller packaging materials | 4,500 VND | Box, tape, label |
| 5 | LEX/3PL shipping fee | 28,000 VND | Average domestic |
| 6 | Failed delivery cost (15% rate) | 4,200 VND | 15% × 28,000 reverse logistics |
| 7 | CS handling (6% contact rate) | 1,800 VND | 6% × 30,000 CS cost |
| 8 | COD reconciliation overhead | 500 VND | Administrative cost |
| **TỔNG CHI PHÍ** | | **42,420 VND** | |
| **Doanh thu (Commission 5% avg)** | | **14,000 VND** | 5% × 280,000 |
| **NET MARGIN** | | **-28,420 VND** | Lazada subsidizes logistics heavily |

→ **Insight:** Unit economics âm nghiêm trọng — mỗi đơn hàng lỗ khoảng 28,000 VND. COD dominant + failed delivery rate cao = double cost burden. Đây là lý do chính cho đợt sa thải 2024.

#### C. Chất lượng

| Metric | Current | Industry Benchmark | Gap |
|--------|---------|-------------------|-----|
| Order success rate | 80-85% | 90-95% | -5 to -10% |
| First-attempt delivery | 75-80% | 82-88% | -3 to -7% |
| COD collection success | 80-85% | 88-92% | -3 to -7% |
| Avg delivery time | 3-5 ngày | 2-3 ngày | +1 to +2 ngày |
| Buyer CSAT | 6.0-6.8/10 | 7.2-7.8/10 (Lazada) | -0.4 to -1.8 |

#### D. Phân tích Root Cause (Why-Why)

**Vấn đề:** COD failure rate 15-20% (cao hơn nhiều so với Shopee ~10%)

```
Why? → Buyer từ chối nhận hàng COD
  Why? → Buyer changed mind hoặc so sánh giá
    Why? → Không đủ thông tin sản phẩm trước khi đặt
      Why? → Seller listing mô tả không chính xác
        Why? → QC review listing không đủ chặt
          Why? → Automated QC misses subtle issues
            Why? → Manual review capacity reduced (layoffs 2024)

ROOT CAUSE: Staffing reduction + Listing quality control gap
```

**Giải pháp đề xuất:**
1. AI-powered listing quality scoring (auto-flag mô tả không match ảnh)
2. Thêm SLA clause cho seller listing accuracy
3. Buyer education (video review, unboxing comparison)
4. Bonus cho seller có return rate thấp

## 3.2. Quy trình Hoàn trả & Hoàn tiền (Core Process)

### 3.2.1. Mô tả quy trình

Quy trình xử lý yêu cầu hoàn trả từ Buyer: tạo request → review evidence → approve/reject → pickup return → inspection → refund.

**Actors:** Buyer, Lazada System, Seller, Return/Inspection Center, Finance
**Customer:** Buyer (trực tiếp), Seller (gián tiếp)

**Chính sách chính:**
- Return Window: 7 ngày (standard); 15 ngày (LazMall)
- Free Return: Lazada chịu phí return shipping (trong chính sách Free Return)
- COD orders: Chỉ hoàn tiền về Lazada Wallet, KHÔNG hoàn tiền mặt

### 3.2.2. Mô hình BPMN

*(File: processes/04-return-refund.bpmn)*
- Activities: 13
- Gateways: 18 (18 XOR)
- Lanes: 5 (Buyer, Lazada System, Seller, Inspection Center, Finance)
- Places: 43, Transitions: 31

### 3.2.3. Phân tích định tính

| STT | Hoạt động | VA | BVA | NVA | Đề xuất |
|-----|-----------|----|-----|-----|----------|
| 1 | Buyer tạo return request | ✓ | | | Simplify form, AI suggest reason |
| 2 | Upload bằng chứng (ảnh/video) | ✓ | | | Auto-enhance image quality |
| 3 | Auto-check return window + eligibility | | ✓ | | Rule engine |
| 4 | Seller phản hồi (đồng ý/từ chối) trong 48h | | | ✓ | Auto-approve timeout |
| 5 | LEX pickup + vận chuyển hàng về | ✓ | | | Self-service slot booking |
| 6 | Inspection (kiểm tra tình trạng SP) | ✓ | | | Standardized checklist |
| 7 | Refund processing theo payment method | ✓ | | | Auto-refund qua Lazada Wallet |
| 8 | Cập nhật seller return rate | | ✓ | | Real-time dashboard |
| 9 | Notify buyer completion | ✓ | | | Real-time push notification |

**VA/BVA/NVA:** VA 5/9 (56%), BVA 3/9 (33%), NVA 1/9 (11%)

#### Waste Analysis

| STT | Hoạt động | Lãng phí | Giải pháp |
|-----|-----------|----------|-----------|
| 1 | Chờ seller approve (48h) | Hold | Auto-approve timeout + penalty |
| 2 | Inspection time 3-5 ngày | Hold | AI pre-screening giảm 60% |
| 3 | Reverse logistics (ship ngược) | Move | Consolidate returns theo khu vực |
| 4 | COD refund limitation (chỉ về Wallet) | Hold | Faster bank transfer option |

### 3.2.4. Phân tích định lượng

#### A. Định lượng thời gian

| Nhánh | Xác suất | Thời gian | Ghi chú |
|-------|----------|-----------|--------|
| Auto-approve (giá trị thấp, lý do rõ) | 35% | 5 phút | Instant refund |
| Manual review + seller respond | 50% | 3-5 ngày | CS + Seller review |
| Investigation (giá trị cao / fraud) | 15% | 7-10 ngày | Deep inspection |

$$CT \approx 10\text{phút} + 0.35 \times 5\text{phút} + 0.50 \times 96\text{giờ} + 0.15 \times 192\text{giờ} + 24\text{giờ} + 72\text{giờ}$$
$$CT \approx 134.5\text{giờ} \approx 5.6\text{ngày}$$

**Efficiency:** PT (45 phút) / CT (134.5 giờ) = 0.56%

#### B. Chi phí xử lý/return

| Thành phần | Chi phí | Ghi chú |
|------------|---------|--------|
| Reverse shipping | 28,000 VND | Avg domestic (buyer's cost nếu đổi ý) |
| CS handling time | 18,000 VND | 15 phút × ~1.200 VND/phút (khớp Bảng 3.9: 52.000 VNĐ → 18.000 VNĐ / ca) |
| Inspection labor | 6,000 VND | Warehouse staff |
| Refund transaction fee | 3,500 VND | Payment gateway |
| **TỔNG** | **51,500 VND** | Per return case |

#### C. Chất lượng

| Metric | Current | Target | Gap |
|--------|---------|--------|-----|
| Return resolution time | 7-15 ngày | 3-5 ngày | -57% to -67% |
| Auto-approve rate | 35% | 55% | +20% |
| Buyer CSAT (return process) | 3.2/5 | 4.0/5 | +0.8 |
| Fraud detection rate | 80% | 95% | +15% |

### 3.2.5. Sổ đăng ký rủi ro

| ID | Rủi ro | Xác suất | Tác động | Giải pháp |
|----|--------|----------|----------|-----------|
| R1 | Bằng chứng giả mạo | 5% | Cao | Image forensics + metadata check |
| R2 | Return abuse (lặp lại) | 8% | Cao | User behavior scoring |
| R3 | Inspection subjectivity | 6% | Trung bình | Standardized checklist + AI assist |
| R4 | COD refund limitation | 100% | Trung bình | Expand refund channels |

## 3.3. Quy trình Quản lý nhà bán hàng (Management Process)

### 3.3.1. Mô tả quy trình

Quy trình quản lý vòng đời Seller: đăng ký → KYC → phê duyệt → onboarding (Lazada University) → kinh doanh → giám sát vi phạm.

**Actors:** Seller, Seller Ops, Compliance Team, Lazada System, Lazada University
**Customer:** Seller (trực tiếp), Buyer (gián tiếp)

**Thang phạt vi phạm:**
```
Warning (cảnh báo) → Delist sản phẩm / giới hạn quyền → 
Suspended tạm thời (7-30 ngày) → Deactivated vĩnh viễn
```

### 3.3.2. Mô hình BPMN

*(File: processes/01-seller-management.bpmn)*
- Activities: 14, Gateways: 15 (15 XOR)
- Lanes: 4 (Seller, Lazada System, Ops, Compliance)
- Places: 42, Transitions: 29

### 3.3.3. Phân tích định tính

| STT | Hoạt động | VA | BVA | NVA | Đề xuất |
|-----|-----------|----|-----|-----|----------|
| 1 | Seller nộp hồ sơ online (KYC) | ✓ | | | Giữ nguyên UX |
| 2 | Auto-check hồ sơ (OCR, đối chiếu MST) | | ✓ | | Tối ưu OCR accuracy |
| 3 | Ops review thủ công (1-3 ngày) | | | ✓ | AI pre-screening giảm 60% |
| 4 | Onboard education (Lazada University) | ✓ | | | Gamification + certification |
| 5 | Performance monitoring (score hàng tuần) | ✓ | | | Real-time dashboard |
| 6 | Violation detection (AI + manual) | | ✓ | | Auto-detect image recognition |
| 7 | Kháng cáo vi phạm (3-7 ngày) | | | ✓ | Self-service appeal portal |
| 8 | LazMall brand authentication (tuần) | | ✓ | | Accelerated vetting |

**VA/BVA/NVA:** VA 3/8 (37%), BVA 3/8 (37%), NVA 2/8 (25%)

### 3.3.4. Phân tích định lượng

#### A. Định lượng thời gian

| Nhánh | Xác suất | Thời gian | Ghi chú |
|-------|----------|-----------|--------|
| Auto-approve (low risk, clean docs) | 60% | 2 giờ | OCR match + clean record |
| Manual review (medium risk) | 30% | 3 ngày | Ops verification |
| Investigation (high risk, brand auth) | 10% | 7-14 ngày | Compliance deep dive |

$$CT = 30\text{phút} + 0.60 \times 2\text{giờ} + 0.30 \times 72\text{giờ} + 0.10 \times 168\text{giờ} + 1\text{giờ}$$
$$CT = 43.3\text{giờ} \approx 1.8\text{ngày}$$

**Efficiency:** PT (1.5 giờ) / CT (43.3 giờ) = 3.46%

#### B. Chất lượng

| Metric | Current | Target | Gap |
|--------|---------|--------|-----|
| Avg approval time | 3-7 ngày | <24 giờ | -60% to -85% |
| Cost per review | 35,000 VND | 15,000 VND | -57% |
| Seller violation rate | 5-8%/tháng | <3% | -50% to -63% |
| False suspension rate | 8-12% | <3% | -63% to -75% |
| Active seller churn | 5-10%/quý | <3% | -60% to -70% |

### 3.3.5. Sổ đăng ký rủi ro

| ID | Rủi ro | Xác suất | Tác động | Giải pháp |
|----|--------|----------|----------|-----------|
| R5 | Fake business registration | 5% | Rất cao | OCR + government DB cross-check |
| R6 | LazMall brand auth delay | 15% | Cao | Accelerated vetting + AI matching |
| R7 | Mass false suspensions | 2% | Rất cao | Human-in-the-loop for bulk actions |
| R8 | Seller exodus acceleration | 10% | Cao | Incentive programs, reduced fees |

## 3.4. Quy trình Quản lý tranh chấp & Khiếu nại (Management Process)

### 3.4.1. Mô tả quy trình

Xử lý dispute giữa Buyer và Seller: opening ticket → evidence collection → mediation → decision → appeal → enforcement.

**Actors:** Buyer, Seller, CS Agent, Dispute Team, AI System, Finance
**Customer:** Buyer & Seller

### 3.4.2. Mô hình BPMN

*(File: processes/02-dispute-management.bpmn)*
- Activities: 12, Gateways: 16 (16 XOR)
- Lanes: 5 (Buyer, Seller, CS Agent, Dispute Team, AI System)
- Places: 38, Transitions: 28

### 3.4.3. Phân tích định tính

| STT | Hoạt động | VA | BVA | NVA | Đề xuất |
|-----|-----------|----|-----|-----|----------|
| 1 | Buyer tạo khiếu nại | ✓ | | | Simplify form, AI suggestion |
| 2 | AI auto-categorize dispute type | | ✓ | | NLP classification accuracy |
| 3 | Thu thập evidence từ cả 2 bên | ✓ | | | Structured upload flow |
| 4 | CS review evidence thủ công | | | ✓ | AI pre-score evidence validity |
| 5 | Mediation (negotiation) | ✓ | | | Chatbot-mediated first step |
| 6 | Phán quyết (decision) | ✓ | | | Decision tree automation |
| 7 | Appeal process (7 ngày) | | ✓ | | Accelerated review |
| 8 | Thực thi refund/penalty | | ✓ | | Auto-execute trong 24h |

**VA/BVA/NVA:** VA 4/8 (50%), BVA 3/8 (37.5%), NVA 1/8 (12.5%)

#### Root Cause Analysis (Why-Why)

**Vấn đề:** Thời gian giải quyết tranh chấp trung bình 5-7 ngày (rất chậm so với Shopee 3-7 ngày)

```
Why? → CS Agent overloaded, queue dài
  Why? → 75% disputes là cases đơn giản (hàng không đúng mô tả <200k)
    Why? → Không có auto-resolution cho low-value disputes
      Why? → Risk management chưa trust automation
        Why? → Thiếu tiered resolution framework

ROOT CAUSE: Policy quá conservative + thiếu tiered auto-resolution
```

### 3.4.4. Phân tích định lượng

#### A. Định lượng thời gian

| Nhánh | Xác suất | Thời gian | Ghi chú |
|-------|----------|-----------|--------|
| Auto-resolve (<200k, clean seller history) | 30% | 2 giờ | Rule-based instant decision |
| Mediation (200k-1M) | 50% | 3-5 ngày | CS-facilitated negotiation |
| Investigation (>1M / fraud suspected) | 20% | 7-10 ngày | Deep evidence review |

$$CT = 15\text{phút} + 0.30 \times 2\text{giờ} + 0.50 \times 96\text{giờ} + 0.20 \times 192\text{giờ}$$
$$CT \approx 86.3\text{giờ} \approx 3.6\text{ngày}$$

**Efficiency:** PT (40 phút) / CT (86.3 giờ) = 0.77%

#### B. Chất lượng

| Metric | Current | Target | Gap |
|--------|---------|--------|-----|
| Avg resolution time | 5-7 ngày | 2-3 ngày | -57% to -60% |
| Mediation success rate | 60-65% | 80% | +15% to +20% |
| Cost per dispute | 55,000 VND | 25,000 VND | -55% |
| Escalation rate | 8-12% | <5% | -58% to -60% |
| Buyer satisfaction | 3.5/5 | 4.3/5 | +0.8 |
| Seller satisfaction | 3.0/5 | 4.0/5 | +1.0 |

#### C. Top dispute types

```
Hàng không đúng mô tả    ████████████████████████████████████ 45%
Không nhận hàng (COD)    ██████████████████████               25%
Hàng giả/nhái            ██████████████                       15%
Thái độ seller           ████████                             8%
Khác                     ██████                               7%
```

### 3.4.5. Sổ đăng ký rủi ro

| ID | Rủi ro | Xác suất | Tác động | Giải pháp |
|----|--------|----------|----------|-----------|
| R9 | False evidence submission | 5% | Cao | Image forensics + metadata check |
| R10 | Bias in dispute resolution | 3% | Cao | Blind review + QA audit |
| R11 | Legal escalation delay | 8% | Rất cao | Pre-approved legal templates |
| R12 | Seller collusion (review bombing) | 4% | Cao | Network analysis + anomaly detection |

## 3.5. Quy trình Chăm sóc khách hàng (Support Process)

### 3.5.1. Mô tả quy trình

Tiếp nhận yêu cầu hỗ trợ đa kênh (chat, hotline, email, social) → Chatbot triage → Agent → Tier-2 → Resolution → CSAT feedback.

**Actors:** Customer, Chatbot/AI, CS Agent Tier 1, Tier-2 Team, QA
**Customer:** Buyer & Seller

### 3.5.2. Mô hình BPMN

*(File: processes/05-customer-service.bpmn)*
- Activities: 18, Gateways: 11 (11 XOR)
- Lanes: 5 (Customer, Chatbot/AI, CS Agent, Tier-2 Team, QA)
- Places: 39, Transitions: 29

### 3.5.3. Phân tích định tính

| STT | Hoạt động | VA | BVA | NVA | Đề xuất |
|-----|-----------|----|-----|-----|----------|
| 1 | User gửi yêu cầu hỗ trợ (multi-channel) | ✓ | | | Omni-channel unified inbox |
| 2 | Chatbot triage & auto-respond | ✓ | | | Expand knowledge base |
| 3 | Routing đến đúng department | | ✓ | | Intent-based AI routing |
| 4 | CS Agent Tier 1 xử lý | ✓ | | | Empowerment: tăng quyền |
| 5 | Escalate Tier 2/3 | | ✓ | | Better triage criteria |
| 6 | Tra cứu thông tin đơn hàng | | ✓ | | Integrated CRM view |
| 7 | Gửi resolution confirmation | ✓ | | | Proactive update |
| 8 | CSAT survey + QC | ✓ | | | Shorten to 1-question CSAT |
| 9 | Log ticket vào hệ thống | | | ✓ | Auto-log từ chat transcript |

**VA/BVA/NVA:** VA 5/9 (56%), BVA 3/9 (33%), NVA 1/9 (11%)

### 3.5.4. Phân tích định lượng

#### A. Định lượng thời gian

| Nhánh | Xác suất | Thời gian | Ghi chú |
|-------|----------|-----------|--------|
| Bot resolve (Tier 0) | 35% | 2 phút | FAQ, order status |
| Tier 1 resolve | 40% | 10 phút | Simple issues |
| Tier 2 escalation | 18% | 45 phút | Complex disputes |
| Tier 3 escalation | 7% | 4 giờ | Critical/legal |

$$CT = 1\text{phút} + 0.35 \times 2\text{phút} + 0.40 \times 10\text{phút} + 0.18 \times 45\text{phút} + 0.07 \times 240\text{phút}$$
$$CT = 28.2\text{phút}$$

**Efficiency:** PT (8 phút) / CT (28.2 phút) = 28.4%

#### B. Chất lượng

| Metric | Current | Target | Gap |
|--------|---------|--------|-----|
| FRT (Chat) | 45s | <15s | -67% |
| FRT (Hotline) | 3 phút | <1 phút | -67% |
| Resolution Rate Tier 1 | 65-70% | 85% | +15% to +20% |
| AHT | 10-15 phút | 6 phút | -50% to -60% |
| CSAT | 6.0-6.5/10 | 8.0/10 | +1.5 to +2.0 |
| Bot deflection | 30-35% | 55% | +20% |
| Cost per contact | 20,000 VND | 10,000 VND | -50% |

#### C. Top contact reasons

```
Trạng thái đơn hàng     ████████████████████████████████████ 35%
Hoàn trả/Refund          ██████████████████████               22%
Vấn đề thanh toán        ██████████████                       15%
Khiếu nại sản phẩm       ██████████                           12%
Tài khoản/Đăng nhập      ██████                               8%
Khác                     █████                                8%
```

## 3.6. Quy trình Marketing & Promotions (Support Process)

### 3.6.1. Mô tả quy trình

Lên kế hoạch campaign → duyệt ngân sách → thiết kế creative → seller đăng ký tham gia → launch → monitor real-time → post-campaign analysis.

**Actors:** Marketing Team, Finance, Creative Team, Seller, Lazada System
**Customer:** Buyer (end beneficiary)

### 3.6.2. Mô hình BPMN

*(File: processes/06-marketing.bpmn)*
- Activities: 21, Gateways: 15 (15 XOR)
- Lanes: 5 (Marketing Team, Finance, Creative, Seller, Lazada System)
- Places: 47, Transitions: 36

### 3.6.3. Phân tích định tính

| STT | Hoạt động | VA | BVA | NVA | Đề xuất |
|-----|-----------|----|-----|-----|----------|
| 1 | Lên kế hoạch chiến dịch (1-4 tuần) | ✓ | | | Template chuẩn hóa |
| 2 | Dự toán ngân sách | | ✓ | | Pre-approved budget tiers |
| 3 | Duyệt ngân sách (theo hạng mức) | | ✓ | | Automation approval workflows |
| 4 | Thiết kế creative (banner, KV) | ✓ | | | AI-generated creative variants |
| 5 | Seller đăng ký tham gia | ✓ | | | Self-service seller tools |
| 6 | Kiểm tra điều kiện seller | | ✓ | | Eligibility engine |
| 7 | Launch campaign | ✓ | | | Scheduled auto-launch |
| 8 | Giám sát real-time | ✓ | | | Live dashboard + alert |
| 9 | Post-campaign analysis (ROI) | | ✓ | | Auto-generated analytics |
| 10 | Đối soát chi phí promotion | | | ✓ | Real-time budget tracking |

**VA/BVA/NVA:** VA 5/10 (50%), BVA 4/10 (40%), NVA 1/10 (10%)

### 3.6.4. Phân tích định lượng

#### A. Định lượng thời gian

| Nhánh | Xác suất | Thời gian | Ghi chú |
|-------|----------|-----------|--------|
| Mega Sale campaign (9.9, 11.11, 12.12) | 25% | 3 tuần | Full platform event |
| Mini campaign (brand day, category) | 75% | 4 ngày | Category/brand specific |

$$CT = 2\text{ngày} + 0.25 \times 21\text{ngày} + 0.75 \times 4\text{ngày} + 1\text{ngày} + 7\text{ngày}$$
$$CT = 18.25\text{ngày}$$

**Efficiency:** PT (3 ngày active work) / CT (18.25 ngày) = 16.4%

#### B. Chất lượng

| Metric | Current | Target | Gap |
|--------|---------|--------|-----|
| Lead time (Mega) | 3-4 tuần | 2 tuần | -40% |
| Lead time (Mini) | 3-5 ngày | 2 ngày | -40% to -50% |
| ROI avg | 2-4x | 5-8x | +60% to +100% |
| Voucher redemption | 20-30% | 45% | +15% to +25% |
| CPA | 18k-28k VND | <12k VND | -50% |

## 3.7. Quy trình Quản lý Nhân sự & Đào tạo (HR & Training)

### 3.7.1. Mô tả quy trình

Quy trình quản lý nhân sự & đào tạo (HR & Training) bao trùm vòng đời nhân sự tại Lazada VN: tuyển dụng, onboarding, đào tạo nội bộ, chứng chỉ tuân thủ (compliance), và đánh giá năng lực. Quy trình hiện tại phụ thuộc lớn vào thao tác thủ công của bộ phận HR và quản lý trực tiếp, với vòng duyệt tài chính kéo dài 5–10 ngày.

**Các tác nhân tham gia:** Nhân viên (Employee), Quản lý trực tiếp (Line Manager), Phòng Nhân sự (HR), Phòng Tài chính (Finance), Nền tảng đào tạo LMS.

**Thống kê mô hình AS-IS:** Activities 17 (15 userTask + 2 serviceTask), Gateways 15 (14 XOR + 1 AND), End events 2, WF-net: 43 places / 32 transitions.

**Điểm yếu chính:**
- Duyệt tài chính 5–10 ngày (bottleneck lớn nhất)
- Tỷ lệ hoàn thành khóa đào tạo chỉ 60%
- Gán khóa đào tạo thủ công theo từng nhân viên
- Không có phân tích khoảng trống kỹ năng (skill gap analysis)

### 3.7.2. TO-BE

Mô hình TO-BE (`processes-to-be/07-hr-training.bpmn`) tự động hóa gán khóa học theo vị trí + đề xuất dựa trên skill gap (AI), cảnh báo chứng chỉ hết hạn, và rút gọn quy trình duyệt tài chính xuống SLA 24h với ngưỡng ủy quyền tự động. Kết quả kiểm chứng WF-net: **SOUND** (Option to Complete PASS, Proper Completion PASS, No Dead Transitions PASS).

---

## 3.8. Quy trình Thanh toán & Đối soát (Payment & Settlement)

### 3.8.1. Mô tả quy trình

Quy trình thanh toán & đối soát xử lý toàn bộ dòng tiền: thanh toán đơn hàng (COD, thẻ, ví điện tử, chuyển khoản), escrow, đối soát với ngân hàng/gateway, và giải ngân (settlement) cho seller. Đây là quy trình có chi phí lãng phí lớn nhất trong toàn hệ thống do COD discrepancy 2–3% và chu kỳ settlement chậm L+2/L+3.

**Các tác nhân tham gia:** Buyer, Seller, Payment Gateway (VNPay, OnePay, Napas, MoMo, ZaloPay), Lazada Finance, Ngân hàng đối tác, COD Provider.

**Thống kê mô hình AS-IS:** Activities 22, Gateways 16 (XOR + exception flows), End events 3, WF-net: 49 places / 38 transitions.

**Điểm yếu chính:**
- COD discrepancy 2–3% (~40 tỷ VND/tháng) — nguyên nhân lớn nhất
- Settlement chậm L+2/L+3 (~32 tỷ VND/tháng ảnh hưởng dòng tiền seller)
- Lỗi gateway (~19 tỷ VND/tháng)
- Đối soát thủ công, phát hiện gian lận còn thiếu

### 3.8.2. TO-BE

Mô hình TO-BE (`processes-to-be/08-payment-settlement.bpmn`) đưa vào AI fraud detection theo thời gian thực, tự động hóa đối soát (reconciliation) với matching engine, rút ngắn settlement xuống L+1 (online) / L+2 (COD), và smart COD routing giảm discrepancy xuống 0,5%. Kết quả kiểm chứng WF-net: **SOUND**.

---

## 3.9. Quy trình Logistics & Giao nhận (Logistics & Delivery)

### 3.9.1. Mô tả quy trình

Quy trình logistics & giao nhận quản lý toàn bộ chuỗi từ lấy hàng (pickup), phân loại tại hub, vận chuyển đường dài, giao hàng chặng cuối (last-mile), đến xử lý giao lại (return attempt). LEX (Lazada Express) kết hợp 3PL (GHN, GHTK, J&T, Ninja Van) phục vụ giao hàng. Đây là quy trình có tần suất lãng phí cao nhất do giao lại (85 tỷ VND/tháng) và lỗi phân loại hub (55 tỷ VND/tháng).

**Các tác nhân tham gia:** Buyer, Seller, Warehouse, Hub phân loại, LEX, 3PL (GHN, GHTK, J&T, Ninja Van), CS.

**Thống kê mô hình AS-IS:** Activities 20, Gateways 13 (XOR retry loop + AND sort hub), End events 2, WF-net: 42 places / 33 transitions.

**Điểm yếu chính:**
- Giao lại lần 2/lần 3: 85 tỷ VND/tháng
- Lỗi phân loại hub: 55 tỷ VND/tháng
- Chậm trễ vận chuyển: 40 tỷ VND/tháng
- Sai địa chỉ: 30 tỷ VND/tháng

### 3.9.2. TO-BE

Mô hình TO-BE (`processes-to-be/09-logistics-delivery.bpmn`) thêm smart routing, AI dự đoán cửa sổ giao hàng, tối ưu lịch giao lại (≤3 lần có chặn), và tự động hóa phân loại hub bằng vision AI. Kết quả kiểm chứng WF-net: **SOUND**.

---

## 3.10. Quy trình Vận hành Nền tảng Công nghệ (IT Operations)

### 3.10.1. Mô tả quy trình

Quy trình vận hành nền tảng công nghệ quản lý phát hành phần mềm (release), sửa lỗi (bug fix), CI/CD pipeline, và ứng phó sự cố bảo mật tại Lazada VN. Chu kỳ bug fix hiện kéo dài 2–5 ngày với tỷ lệ deploy fail 15%, gây chi phí lãng phí ước tính 1170 tỷ VND/tháng (đơn vị tham chiếu).

**Các tác nhân tham gia:** Developer, QA, DevOps/SRE, Release Manager, Bảo mật (Security), Infra, User/Internal.

**Thống kê mô hình AS-IS:** Activities 18, Gateways 16 (XOR/AND), End events 2, WF-net: 45 places / 34 transitions.

**Điểm yếu chính:**
- Bug fix loop 2–5 ngày (1170 tỷ VND/tháng)
- Deploy failure 15% (780 tỷ VND/tháng)
- CI/CD pipeline chậm (585 tỷ VND/tháng)
- Ứng phó bảo mật 7–14 ngày (468 tỷ VND/tháng)

### 3.10.2. TO-BE

Mô hình TO-BE (`processes-to-be/10-it-platform.bpmn`) đưa vào release automation với canary deploy + auto-rollback, pipeline CI/CD tối ưu (giảm thời gian build 50%), và Security Operations Center (SOC) 24/7 với automated response. Kết quả kiểm chứng WF-net: **SOUND**.

---

## 3.11. Sổ đăng ký vấn đề tổng hợp (Issue Register)

### Vấn đề hiện tại (Open Issues)

| ID | Vấn đề | Mức độ | Tác động | Giải pháp đề xuất | Trạng thái |
|----|--------|--------|----------|-------------------|------------|
| I1 | Seller delay confirm >24h (8-10% đơn) | Cao | Lost sale, churn | Auto-accept 2h + penalty | Open |
| I2 | COD rejection rate 15-20% | **Rất cao** | Chi phí reverse logistics +30% | Pre-call SLA, smart COD routing | Open |
| I3 | Return/refund time 7-15 ngày | Cao | Buyer satisfaction thấp | Auto-refund <100k, SLA 3-5 ngày | Open |
| I4 | Dispute resolution 5-7 ngày | TB | Buyer & seller frustration | AI pre-screening, tiered resolution | Open |
| I5 | Seller churn 5-10%/quý | Cao | Platform erosion | Fee reduction, incentive programs | Open |
| I6 | Chatbot deflection rate thấp (30-35%) | TB | CS workload cao | KB expansion + NLP improve | Open |
| I7 | Listing quality gap (mô tả vs sản phẩm thật) | Cao | Return rate tăng | AI listing quality scoring | Open |
| I8 | LEX fleet underutilization | TB | Logistics cost/unit tăng | Optimize route, increase 3PL mix | Open |

### Vấn đề đã giải quyết (Resolved Issues)

| ID | Vấn đề | Giải pháp đã áp dụng | Kết quả |
|----|--------|----------------------|---------|
| I9 | Payment gateway downtime | Multi-gateway failover | Giảm đáng kể sự cố uptime |
| I10 | Manual address entry errors 12% | Auto-complete API | Giảm còn 4% |
| I11 | Seller onboarding 5-7 ngày | OCR + auto-verify | Giảm còn 2-3 ngày |

### Trend Analysis

**Top 3 vấn đề tái diễn:**
1. COD rejection (I2) — root cause: buyer behavior + incomplete product info
2. Seller churn (I5) — root cause: fee structure + competitor incentives (TikTok Shop)
3. Slow dispute resolution (I4) — root cause: manual review dependency + staffing

**Root cause chung:** Thiếu automation + reduced staffing (layoffs 2024) + COD-dominated payment ecosystem

## 3.12. Nguồn dữ liệu & Trích dẫn

| Số liệu | Nguồn | Năm | Ghi chú |
|---------|-------|-----|----------|
| COD failure rate 15-20% | Industry estimates + seller forums | 2024-2025 | Lazada-specific estimate |
| Avg refund time 7-15 ngày | Lazada Help Center + industry benchmark | 2025 | SEA e-commerce median |
| First-attempt delivery 75-80% | Industry estimates | 2024 | Lower than Lazada benchmark |
| Market share 10-18% | YouNet ECI, Metric.vn, Momentum Works | 2024 | Declining trend |
| Return rate 8-12% (fashion 20-25%) | McKinsey + industry reports | 2025 | SEA benchmark |
| CSAT 6.0-6.8/10 | App Store rating + third-party surveys | 2025 | Lower than Lazada |
| Total Alibaba investment ~$4.2B | Wikipedia, CafeF | 2016-2022 | Verified sources |
| Headcount reduction 25-50% | Reuters, CNA, Wikipedia | Jan 2024 | Reported layoffs |
| Seller churn 7,000+ H1/2025 | Metric.vn | 2025 | Public data |

> **Lưu ý:** Nhóm nghiên cứu không có quyền truy cập vào hệ thống dữ liệu nội bộ của Lazada VN. Các số liệu được ước tính dựa trên: (1) chính sách công khai từ Seller Center/Help Center, (2) benchmark từ báo cáo ngành, (3) phân tích heuristic từ quan sát UX flow.

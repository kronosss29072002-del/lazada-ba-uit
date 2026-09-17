# QUY TRÌNH NGHIỆP VỤ LAZADA VIỆT NAM
## Nhóm QUẢN LÝ & CỐT LÕI

> **Nguồn tổng hợp:** Lazada Seller Center (sellercenter.lazada.vn), Lazada Help Center, Lazada University, seller community forums, và các bài phân tích từ Third-party sources.
> **Lưu ý:** Chính sách Lazada có thể thay đổi theo thời gian. Các thông tin dưới đây phản ánh trạng thái được xác nhận đến Q3 2026.

---

## PHẦN A: QUY TRÌNH QUẢN LÝ (MANAGEMENT)

---

## 1. QUẢN LÝ NHÀ BÁN HÀNG (Seller Management)

### 1.1 Quy trình Onboarding Seller

#### Actors tham gia
- **Internal:** Seller Acquisition Team, KYC/Verification Team, Seller Operations Team, Quality Assurance Team
- **External:** Người bán (cá nhân/doanh nghiệp), Đại lý đăng ký kinh doanh

#### Quy trình chi tiết

```
[Step 1] Đăng ký tài khoản
         ├── Truy cập sellercenter.lazada.vn
         ├── Nhập email/số điện thoại Việt Nam
         ├── Xác thực OTP
         └── Tạo mật khẩu

[Step 2] Chọn loại hình bán hàng
         ├── Người bán cá nhân (Individual Seller)
         │   → CCCD/CMND
         ├── Doanh nghiệp (Company Seller)
         │   → Giấy phép kinh doanh, MST
         └── Cross-border Seller (nếu bán từ nước ngoài)
             → Giấy phép kinh doanh quốc tế

[Step 3] Cung cấp giấy tờ KYC
         ├── Cá nhân: CCCD/CMND (mặt trước + mặt sau)
         ├── Doanh nghiệp: GPKD + CCCD người đại diện
         ├── Mã số thuế (MST)
         ├── Thông tin tài khoản ngân hàng Việt Nam
         └── Photo selfie với CCCD (một số trường hợp)

[Step 4] Xác minh tài khoản
         ├── Lazada review hồ sơ (1-3 ngày làm việc)
         ├── Có thể yêu cầu bổ sung giấy tờ
         └── Thông báo kết quả qua email/app

[Step 5] Thiết lập cửa hàng
         ├── Đặt tên shop
         ├── Upload banner/avatar shop
         ├── Upload sản phẩm (title, ảnh, giá, mô tả)
         ├── Cấu hình đơn vị vận chuyển (FBL/FBS)
         └── Cấu hình phương thức thanh toán

[Step 6] Huấn luyện onboarding
         ├── Lazada University (university.lazada.vn)
         ├── Video hướng dẫn trong Seller Center
         └── Webinar/hội thảo trực tuyến

[Step 7] Go Live
         ├── Kích hoạt shop
         └── Bắt đầu bán hàng
```

**Thời gian onboarding trung bình:** 1-5 ngày làm việc (tùy tốc độ chuẩn bị giấy tờ của seller)

#### Các giấy tờ bắt buộc theo loại hình

| Loại Seller | Giấy tờ KYC | Giấy tờ ngành hàng đặc biệt |
|---|---|---|
| Cá nhân | CCCD/CMND, Photo selfie | -- |
| Doanh nghiệp | GPKD, MST, CCCD đại diện | -- |
| Bán mỹ phẩm | -- | Giấy phép lưu hành mỹ phẩm |
| Bán thực phẩm | -- | Chứng nhận ATTP (VSATTP) |
| Bán thiết bị điện tử | -- |_tem bảo hành, tài liệu nhập khẩu |
| Bán thuốc/dược phẩm | -- | Giấy phép kinh doanh Dược |

> **Nguồn:** Seller Center Help Center (sellercenter.lazada.vn), Lazada University onboarding guides

---

### 1.2 Hệ thống Rating Seller (Seller Rating Tiers)

#### Actors tham gia
- **Internal:** Seller Performance Team, Algorithm/AI Team
- **External:** Người bán

#### Các Tier và tiêu chí

| Tier | Score | Đánh giá | Quyền lợi |
|---|---|---|---|
| **Diamond** | 4.8 - 5.0 | Xuất sắc | Badge "Diamond Seller", ưu tiên flash sale, hiển thị cao nhất trong search, reduced commission trên một số danh mục |
| **Gold** | 4.5 - 4.79 | Rất tốt | Badge "Preferred Seller", tham gia campaign độc quyền, ưu tiên hiển thị |
| **Silver** | 4.0 - 4.49 | Tốt | Visible trong search, tham gia flash sale cơ bản |
| **Standard** | 2.0 - 3.99 | Cơ bản | Hiển thị bình thường, ít quyền lợi promotion |
| **Below Standard** | < 2.0 | Kém | Giảm visibility mạnh, bị cảnh cáo, nguy cơ suspension |

#### Các chỉ số quyết định Seller Score

```
Seller Score = f(Cancellation Rate, Late Dispatch Rate, 
                 Return Rate, Customer Satisfaction, 
                 Order Fulfillment Rate)
```

| Chỉ số | Target | Mức phạt nếu vượt |
|---|---|---|
| **Cancellation Rate** (tỷ lệ hủy đơn seller) | < 2% | Giảm score, cảnh cáo lần 1, suspension lần 2 |
| **Late Dispatch Rate** (tỷ lệ giao hàng trễ) | < 5% | Giảm score, cảnh cáo |
| **Return Rate** (tỷ lệ trả hàng) | < 5% (tùy danh mục) | Cảnh cáo, yêu cầu cải thiện QC |
| **Customer Satisfaction** (đánh giá khách hàng) | >= 4.5 sao | Giảm visibility |
| **Order Fulfillment Rate** (tỷ lệ đơn xử lý thành công) | >= 95% | Giảm score, cảnh cáo |

#### Thay đổi Score theo chu kỳ
- Seller Score được **cập nhật hàng tuần**
- Tính trên cơ sở dữ liệu 90 ngày gần nhất
- Seller có thể theo dõi trong Seller Center > Dashboard > Seller Performance

> **Nguồn:** Seller Center Seller Performance Dashboard, Lazada University seller education materials

---

### 1.3 Hệ thống Vi Phạm & Phạt (Seller Violation & Penalization)

#### Loại vi phạm và hình phạt

| Mức độ | Ví dụ vi phạm | Hình phạt |
|---|---|---|
| **Minor** | Delayed shipment, incomplete product description, wrong category listing | Cảnh cáo lần 1;ഴquảng bị gỡ nếu tái phạm |
| **Moderate** | Falsifying product info, manipulated reviews, substandard packaging | Gỡ sản phẩm, trừ tiền cọc (security deposit), giảm score |
| **Major** | Selling counterfeit goods, deliberate overcharging, repeat moderate violations | Suspension tài khoản 7-30 ngày, freeze escrow funds |
| **Severe** | Escrow fraud, identity fraud, repeated major violations, coordinated fraud rings | Permanent ban + freeze all funds |

#### Quy trình xử lý vi phạm

```
[1] Phát hiện vi phạm
    ├── Tự động bởi hệ thống AI/Lazada Risk Engine
    ├── Báo cáo từBuyer (buyer complaint)
    └── Kiểm tra ngẫu nhiên bởi QC team

[2] Thông báo seller
    ├── Email notification + Seller Center alert
    ├── Mô tả vi phạm cụ thể
    └── Cho seller cơ hội giải trình (24-72h)

[3] Phân tích và quyết định
    ├── Seller Operations Team review
    ├── seller giải trình (nếu có)
    └── Ra quyết định phạt

[4] Áp dụng hình phạt
    ├── Gỡ sản phẩm / Giảm visibility
    ├── Cảnh cáo (lần 1-2)
    ├── Suspension (lần 3+)
    └── Permanent ban (vi phạm nghiêm trọng)

[5] Kháng nghị (appeal)
    ├── Seller gửi appeal qua Seller Center
    ├── Team review lại (5-7 ngày làm việc)
    └── Quyết định cuối cùng
```

> **Nguồn:** Lazada Seller Center Policies, Anti-counterfeit Policy pages

---

### 1.4 Lazada University (Seller Education)

#### Actors
- **Internal:** Lazada Education Team, Seller Success Managers
- **External:** Người bán mới và hiện tại

#### Các chương trình đào tạo

| Chương trình | Nội dung | Đối tượng |
|---|---|---|
| **Onboarding Course** | Hướng dẫn sử dụng Seller Center, tạo listing, xử lý đơn hàng | Seller mới |
| **Product Listing Masterclass** | Cách tạo listing hấp dẫn, SEO trên Lazada, chụp ảnh sản phẩm | Tất cả seller |
| **Marketing & Ads** | Sponsored Solutions, flash sale, voucher, campaign participation | Seller muốn tăng doanh số |
| **Logistics & Fulfillment** | FBL setup, packaging standards, handover procedures | Seller tự vận hành |
| **Seller Performance** | Cách cải thiện score, xử lý dispute, tăng review | Seller muốn lên tier |
| **Advanced Analytics** | Đọc dashboard, phân tích conversion, A/B testing | Seller nâng cao |

#### Kênh học
- **Online:** university.lazada.vn (video, quiz, certification)
- **Offline:** Hội thảo seller tại Hà Nội, TP.HCM
- **In-app:** Lazada Seller University trong Seller Center
- **Social:** Facebook seller groups, Zalo community

> **Nguồn:** Lazada University (university.lazada.vn)

---

### 1.5 3PL Seller Fulfillment (Model FBS - Fulfilled by Seller)

#### Actors
- **Internal:** Lazada Logistics Team, Seller Operations
- **External:** 3PL Partners (GHN, GHTK, J&T Express, BEST Express, Viettel Post, VNPost), Seller

#### Quy trình FBS

```
[1] Seller nhận đơn hàng trong Seller Center

[2] Seller đóng gói sản phẩm
    ├── Đúng kích thước, tiêu chuẩn packaging của Lazada
    ├── Đính shipping label (in từ Seller Center)
    └── Hand over cho 3PL partner

[3] 3PL Pickup
    ├── Seller book pickup hoặc drop-off tại hub
    ├── Cutoff time: thường trước 14:00-17:00 (tùy khu vực)
    └── Đơn pickup sau cutoff sẽ xử lý ngày hôm sau

[4] 3PL Processing
    ├── Sorting tại hub
    ├── Transport đến sorting center khu vực
    └── Hand off cho last-mile delivery partner

[5] Last-mile Delivery
    ├── Giao đến tay khách hàng
    ├── Thu COD (nếu có)
    └── Xác nhận giao hàng thành công
```

**SLA cơ bản cho FBS:**
- **Handover time:** Trong vòng 24-48 giờ sau khi đơn hàng được confirm
- **Late dispatch nếu:** Không handover trong thời gian SLA

> **Nguồn:** Seller Center Help Center, Lazada Logistics documentation

---

## 2. QUẢN LÝ CHẤT LƯỢNG (Quality Management)

### 2.1 Kiểm soát Chất lượng Sản phẩm

#### Actors
- **Internal:** QC Team, Product Quality Assurance, Intellectual Property Team, Seller Quality Team
- **External:** Người bán, Brand owners (đối tác brands), Third-party QC labs

#### Quy trình QC cho sản phẩm trên Lazada

```
[1] LISTING REVIEW (Khi seller upload sản phẩm)
    ├── Automated checks:
    │   ├── Ảnh sản phẩm hợp lệ (kích thước, chất lượng)
    │   ├── Mô tả không chứa từ khóa cấm
    │   ├── Giá không bất thường (quá thấp/quá cao)
    │   └── Danh mục phù hợp
    └── Manual review (nếu flagged):
        ├── QC team check thủ công
        └── Yêu cầu seller chỉnh sửa nếu không đạt

[2] ONGOING MONITORING (Trong suốt vòng đời sản phẩm)
    ├── Customer reviews & ratings monitoring
    ├── Return reason analysis
    ├── Complaint pattern detection
    └── AI anomaly detection (giá thay đổi đột ngột, review giả...)

[3] ENFORCEMENT (Khi phát hiện vi phạm)
    ├── Gỡ listing vi phạm
    ├── Cảnh cáo seller
    ├── Freeze escrow funds (trường hợp nghiêm trọng)
    └── Suspension account (tái phạm)
```

#### Các tiêu chuẩn listing bắt buộc

| Tiêu chuẩn | Yêu cầu |
|---|---|
| **Ảnh sản phẩm** | >= 3 ảnh, nền trắng/sạch, >= 500x500px, không watermark |
| **Mô tả** | >= 300 từ, không copy từ shop khác, đúng thông số kỹ thuật |
| **Giá** | Phù hợp thị trường, không pricing fraud |
| **Danh mục** | Đúng danh mục, không miscategorize |
| **Thông số** | Fill đầy đủ các trường bắt buộc theo danh mục |

> **Nguồn:** Seller Center Listing Standards, Lazada Product Quality Guidelines

---

### 2.2 Chính sách Chống Hàng Giả (Counterfeit & Authenticity)

#### LazMall - Cam kết Hàng chính hãng

| Tiêu chí | Chi tiết |
|---|---|
| **100% Authentic** | Tất cả sản phẩm trên LazMall được cam kết chính hãng |
| **100% Return Guarantee** | Trả hàng trong 15 ngày nếu phát hiện hàng giả |
| **Brand Authorization** | Seller phải cung cấp giấy ủy quyền từ brand |
| **Vetting Process** | Lazada kiểm tra kỹ trước khi duyệt vào LazMall |

#### Quy trình xử lý hàng giả

```
[1] PHÁT HIỆN
    ├── Buyer complaint + bằng chứng
    ├── Brand owner report (IP Protection Portal)
    ├── QC random check
    └── AI counterfeit detection

[2] XÁC MINH
    ├── Seller cung cấp chứng từ nhập hàng/hóa đơn
    ├── So sánh với database hàng chính hãng
    └── Nếu cần: QC team test sản phẩm vật lý

[3] XỬ LÝ
    ├── Hàng giả confirmed:
    │   ├── Gỡ TOÀN BỘ listing sản phẩm đó
    │   ├── Freeze escrow funds liên quan
    │   ├── Seller bị suspension (lần đầu: 7-30 ngày)
    │   ├── Tái phạm: Permanent ban + giữ tiền
    │   └── Buyer được hoàn tiền 100%
    └── Hàng chính hãng:
        └── Seller được minh oan, listing khôi phục
```

#### IP Protection Portal
- Brand owners có thể đăng ký trên **Lazada IP Protection Portal**
- Lazada sẽ chủ động gỡ listing vi phạm bản quyền
- Hợp tác với tổ chức chống hàng giả quốc tế

> **Nguồn:** LazMall brand guarantee pages, Lazada Anti-counterfeit Policy, Seller Center IP Protection

---

### 2.3 Customer Complaint Handling và Impact lên Seller Score

#### Quy trình xử lý khiếu nại

```
[1] Buyer gửi khiếu nại
    ├── Qua Lazada Help Center
    ├── Qua chat với seller
    └── Qua hotline 1900 1720

[2] Phân loại khiếu nại
    ├── Product Quality (chất lượng SP)
    ├── Wrong Item (sai hàng)
    ├── Not as Described (không đúng mô tả)
    ├── Late Delivery (giao trễ)
    ├── Counterfeit (hàng giả)
    └── Other

[3] Xử lý theo phân loại
    ├── Simple cases: Auto-resolved bởi hệ thống
    ├── Medium: Seller must respond trong 24-48h
    └── Complex: Lazada CScan thiệp mediation

[4] Ghi nhận kết quả
    ├── Complaint resolved: +0 penalty (neutral)
    ├── Seller fault confirmed: -score point, tăng complaint rate
    └── Repeat complaints về cùng seller: Escalate to QC team
```

**Impact lên Seller Score:**
- Mỗi complaint hợp lệ làm giảm seller score
- Tỷ lệ complaint > 5% trong 30 ngày: Cảnh cáo
- Tỷ lệ complaint > 10%: Giảm tier, có thể suspension

> **Nguồn:** Lazada Seller Center Quality Score documentation

---

## 3. QUẢN LÝ TRANH CHẤP & RỦI RO (Dispute & Risk Management)

### 3.1 Dispute Resolution Flow

#### Actors
- **Internal:** Dispute Resolution Team (DR Team), Risk & Fraud Team, Customer Service
- **External:** Buyer, Seller, Logistics Partner

#### Quy trình chi tiết

```
[Stage 1] DIRECT COMMUNICATION (0-72h)
    Buyer ──chat──► Seller
    ├── Buyer mô tả vấn đề
    ├── Seller respond trong 24-72h
    ├── Seller đề xuất giải pháp (refund, replacement, partial refund)
    └── Nếu agreed → Resolution tại đây

[Stage 2] FORMAL DISPUTE/CLAIM (nếu Stage 1 fail)
    Buyer ──raise claim──► Lazada System
    ├── Buyer submit evidence (ảnh, video, screenshot)
    ├── Gán dispute reason code
    └── Lazada tạo Case ID

    ├── Seller nhậnthông báo
    │   ├── Respond trong 3-7 ngày
    │   └── Submit bằng chứng bảo vệ

    └── Lazada DR Team review
        ├── Phân tích evidence từ cả 2 bên
        ├── Check logistics data (shipping status, weight...)
        └── Ra quyết định sơ bộ

[Stage 3] LAZADA MEDIATION (5-10 business days)
    ├── DR Team gọi tên người đúng
    ├── Quyết định binding:
    │   ├── Full refund → Buyer
    │   ├── Partial refund → Buyer
    │   ├── Return & exchange
    │   ├── Reject claim (Seller wins)
    │   └── No further action
    └── Thông báo cho cả 2 bên

[Stage 4] APPEAL (nếu không đồng ý)
    ├── Appeal phải gửi trong 7 ngày sau quyết định
    ├── Lazada Senior DR Manager review
    └── Quyết định cuối cùng (final & binding)

[Stage 5] ESCROW ADJUSTMENT
    ├── Nếu Buyer wins: Escrow release → Buyer refund
    ├── Nếu Seller wins: Escrow release → Seller payout
    └── Commission vẫn được trừ (Lazada không hoàn commission)
```

#### Timeline tóm tắt

| Stage | Thời gian |
|---|---|
| Buyer mở claim | Trong vòng 7-15 ngày sau delivery |
| Seller response window | 24-72h (direct) / 3-7 ngày (formal) |
| Lazada review & decision | 5-10 ngày làm việc |
| Refund processing | 1-7 ngày làm việc sau quyết định |
| Appeal window | 7 ngày sau quyết định đầu tiên |

> **Nguồn:** Lazada Buyer Protection Program, Dispute Resolution Policy

---

### 3.2 Escrow Management

#### Khái niệm
Lazada sử dụng hệ thống **Escrow** (ký quỹ) để bảo vệ cả buyer và seller:
- Buyer thanh toán → Tiền vào escrow account Lazada
- Seller giao hàng → Buyer nhận + confirm → Escrow release → Seller nhận tiền

#### Quy trình Escrow

```
[1] Buyer thanh toán
    ├── COD: Tiền giữ tại logistics partner → chuyển về Lazada
    ├── Online: Tiền trừ từ thẻ/ví → vào escrow Lazada
    └── Status: "Payment Received - In Escrow"

[2] Escrow Hold Period
    ├── Đơn không tranh chấp: Hold đến khi buyer confirm nhận
    ├── Auto-confirm sau 7 ngày nếu buyer không confirm/claim
    └── Đơn có tranh chấp: Holdcho đến khi dispute resolved

[3] Escrow Release
    ├── Order completed → Release funds
    ├── Trừ commission + fees
    └── Chuyển vào Lazada Wallet của seller

[4] Escrow Hold (Trường hợp tranh chấp)
    ├── Buyer raise claim → Escrow bị hold thêm
    ├── Seller raise claim → Escrow bị hold thêm
    └── Release khi quyết định cuối cùng
```

#### Phí liên quan khi Escrow xử lý

| Loại phí | Mức | Ghi chú |
|---|---|---|
| **Commission** | 1-8% (tùy danh mục) | Trừ trên tổng giá trị đơn |
| **Payment handling fee** | ~2% | Phí xử lý thanh toán |
| **COD collection fee** | 1-2% | Phí thu hộ COD |
| **VAT on commission** | 10% | Thuế GTGT trên commission |

> **Nguồn:** Seller Center Fee Schedule, Escrow Policy pages

---

### 3.3 Fraud Detection & Prevention

#### Loại fraud thường gặp trên Lazada

| Loại fraud | Mô tả | Lazy detection method |
|---|---|---|
| **Fake Orders** | Tạo đơn hàng giả để tăng doanh số/chạy quảng cáo | AI pattern detection (IP, device, order frequency) |
| **Refund Abuse** | Mua hàng → claim giả → nhận refund | Behavioral analytics |
| **Collusion** | NhómSeller/Buyer cấu kết đánh giá giả | Network graph analysis |
| **Escrow Fraud** | Giả mạo shipping status để release escrow | Cross-check logistics data |
| **Identity Fraud** | Đăng ký seller với giấy tờ giả | KYC verification + document verification AI |
| **Price Manipulation** | Thuê account khác tạo đơn với giá ưu đãi | Anomaly detection |

#### Hệ thống chống fraud

```
[Real-time Detection]
├── AI/ML model phân tích hành vi bất thường
├── Device fingerprinting
├── IP geolocation check
├── Order velocity monitoring
└── Payment pattern analysis

[Post-transaction Review]
├── Seller analytics dashboard alerts
├── Customer complaint pattern detection
├── Return rate anomaly flagging
└── Manual investigation by Risk Team

[Enforcement]
├── Warning → Temporary restriction → Permanent ban
├── Fund freeze
├── Legal action (trường hợp serious)
└── Report to authorities (nếu cần)
```

> **Nguồn:** Lazada Risk & Fraud Prevention documentation, Seller Center security guidelines

---

## PHẦN B: QUY TRÌNH CỐT LÕI (CORE PROCESSES)

---

## 4. XỬ LÝ ĐƠN HÀNG ONLINE (Order Processing) ⭐

> Đây là quy trình cốt lõi nhất, kết nối buyer journey từ đặt hàng đến nhận hàng và thanh toán.

#### Actors
- **Internal:** Order Management System (OMS), Payment Team, Logistics Team, Fulfillment Team
- **External:** Buyer, Seller, Payment Gateway, 3PL/Logistics Partner

#### Quy trình chi tiết (Step-by-Step)

```

 PHASE 1: CART → CHECKOUT (Buyer-side)

[Step 1] Add to Cart
    ├── Buyer browse/search products
    ├── Select variant (size, color...)
    ├── Add to cart
    └── Cart shows: product, qty, estimated shipping fee

[Step 2] Checkout
    ├── Select shipping address
    ├── Select shipping method (standard/express/same-day*)
    ├── Select payment method:
    │   ├── COD (Cash on Delivery) - ~60-70% giao dịch VN
    │   ├── Credit/Debit Card (Visa, MasterCard, JCB)
    │   ├── ATM Card (thẻ nội địa)
    │   ├── E-wallet (MoMo, ZaloPay, VNPay)
    │   ├── Buy Now Pay Later / Installment
    │   └── Lazada Wallet
    ├── Apply voucher/promo code
    └── Review order summary

[Step 3] Place Order
    ├── Buyer click "Đặt hàng" (Place Order)
    ├── System validates:
    │   ├── Payment method valid
    │   ├── Stock availability
    │   ├── Shipping address serviceable
    │   └── Promo code valid
    └── If COD: Order created immediately
        If online payment: Redirect to payment gateway

[Step 4] Payment Processing
    ├── Online payment: Payment gateway processes
    │   ├── Success → Order confirmed
    │   └── Failed → Buyer notified, order cancelled
    ├── COD: No payment processing at this stage
    └── Funds held in Lazada Escrow

 PHASE 2: ORDER CONFIRMATION & FULFILLMENT

[Step 5] Order Sent to Seller
    ├── OMS sends order to Seller Center
    ├── Seller sees order in "To Ship" tab
    ├── Seller has window to confirm (24-48h)
    │   └── Auto-cancel if not confirmed
    └── Seller confirm → Order status: "Confirmed"

[Step 6] Seller Preparation
    ├── Seller pick product from inventory
    ├── Quality check (self-QC)
    ├── Pack product:
    │   ├── Standard packaging
    │   ├── Attach shipping label (in từ Seller Center)
    │   ├── Include invoice/receipt
    │   └── Seal package
    └── Ready for handover

[Step 7] Handover to Logistics
    ├── FBL (Fulfilled by Lazada):
    │   ├── Seller ship inventory to Lazada warehouse
    │   ├── Lazada pick, pack, ship
    │   └── Lazada handle CS & returns
    ├── FBS (Fulfilled by Seller):
    │   ├── Seller hand over package to 3PL partner
    │   ├── Pickup hoặc drop-off tại hub
    │   ├── Cutoff time: 14:00-17:00 (tùy khu vực)
    │   └── 3PL scan & confirm receipt
    └── Tracking number generated

 PHASE 3: SHIPPING & DELIVERY

[Step 8] In-Transit Processing
    ├── 3PL Sorting Center:
    │   ├── Package sorted by destination zone
    │   ├── Re-sorted at regional hub
    │   └── Dispatched to last-mile delivery station
    ├── Seller tracks via Seller Center
    └── Buyer tracks via Lazada App

[Step 9] Last-Mile Delivery
    ├── Courier delivers to buyer's address
    ├── Multiple attempts allowed (2-3 lần)
    ├── If COD: Courier collects cash from buyer
    ├── Buyer signs/receives package
    └── Tracking updated: "Delivered"

[Step 10] Delivery Confirmation
    ├── Auto-confirm after 7 days nếu buyer không action
    ├── Buyer click "Đã nhận hàng" → Status: "Completed"
    └── If COD: Cash collected by courier → settlement process

 PHASE 4: POST-DELIVERY

[Step 11] Buyer Confirmation Window (7 ngày)
    ├── Buyer có 7 ngày để:
    │   ├── Confirm received hàng ("Đã nhận hàng")
    │   ├── Raise dispute/claim
    │   └── hoặc Waiting for auto-confirm
    └── Auto-confirm sau 7 ngày → Order status: "Completed"

[Step 12] Escrow Release & Settlement
    ├── Order Completed → Escrow release
    ├── Commission + fees deducted
    ├── Remaining funds → Lazada Wallet
    └── Seller withdraw to bank account
```

### Split Shipment

```
Khi đơn hàng có nhiều SP từ nhiều seller hoặc kho khác nhau:

│ ORDER #123456                           │
│ ├── Item A (Seller 1) → Shipment 1     │
│ ├── Item B (Seller 2) → Shipment 2     │
│ └── Item C (FBL warehouse) → Shipment 3│

Mỗi shipment có tracking riêng, giao riêng
```

### Bundled Shipping

```
Khi nhiều SP cùng seller, cùng kho:

│ ORDER #123456                           │
│ ├── Item A ─┐                          │
│ ├── Item B ─┤── Gói chung → 1 tracking │
│ └── Item C ─┘                          │

Tiết kiệm chi phí shipping, giao cùng lúc
```

### Order Hold Period & Auto-Cancel

| Trạng thái | Hold Period | Action |
|---|---|---|
| Chờ seller confirm | 24-48h | Auto-cancel nếu seller không confirm |
| Chờ seller giao hàng | 24-48h sau confirm | Auto-cancel nếu không handover |
| Đơn COD bị từ chối | Courier attempt 2-3 lần | Auto-cancel, buyer refund (COD: nothing charged) |
| Đơn online - payment fail | Immediate | Auto-cancel |

### Pain Points

| Pain Point | Mô tả | Ảnh hưởng |
|---|---|---|
| Seller delay confirm | Seller không xác nhận đơn trong thời gian SLA | Auto-cancel → lost sale |
| Wrong item | Seller gửi sai sản phẩm | Return + complaint |
| Late shipping | Seller handover trễ | Giảm seller score, buyer complaint |
| COD rejection | Buyer từ chối nhận hàng COD | Reverse logistics cost |
| Split shipment confusion | Buyer không hiểu tại sao nhận nhiều gói | Complaints, poor experience |

### Technology Hỗ trợ

| Technology | Chức năng |
|---|---|
| **OMS (Order Management System)** | Quản lý vòng đời đơn hàng end-to-end |
| **Seller Center App** | Seller quản lý đơn, in label, theo dõi |
| **Lazada App/Buyer Dashboard** | Buyer track order real-time |
| **WMS (Warehouse Management System)** | Quản lý kho FBL, pick/pack |
| **TMS (Transportation Management System)** | Quản lý vận chuyển 3PL |
| **Payment Gateway** | Xử lý thanh toán online |
| **Escrow System** | Quản lý ký quỹ, settlement |

> **Nguồn:** Lazada Seller Center order management documentation, Lazada logistics SLA pages, seller community reports

---

## 5. THANH TOÁN & ĐỐI SOÁT (Payment & Settlement)

### 5.1 Phương thức Thanh toán

#### Actors
- **Internal:** Payment Operations Team, Finance/Reconciliation Team, Anti-fraud Team
- **External:** Payment Gateways (VNPay, OnePay, Napas), Banks, E-wallet providers (MoMo, ZaloPay), Card networks (Visa, MasterCard, JCB)

#### Phương thức thanh toán chi tiết

| Phương thức | Tỷ lệ GD | Phí seller | Timeline nhận tiền |
|---|---|---|---|
| **COD (Cash on Delivery)** | ~60-70% | COD collection fee: 1-2% | Sau khi order completed + settlement cycle |
| **Credit/Debit Card** | ~15-20% | Payment handling fee: ~2% | Settlement cycle |
| **ATM/Internal Bank Card** | ~5-10% | Payment handling fee: ~1-1.5% | Settlement cycle |
| **E-wallet (MoMo, ZaloPay)** | ~5-10% | Payment handling fee: ~1.5-2% | Settlement cycle |
| **Buy Now Pay Later (Installment)** | ~2-5% | Higher commission rate | Settlement cycle |
| **Lazada Wallet** | ~3-5% | Lowest/no fee | Settlement cycle |

### 5.2 Quy trình thanh toán COD chi tiết

```
[1] Buyer nhận hàng + trả tiền COD cho courier
    └── Courier ghi nhận thu COD amount

[2] Courier/Liability partner → deposit COD cash về Lazada
    ├── Hàng ngày (daily deposit)
    └── reconciliation với OMS data

[3] Lazada Finance Team → reconciliation
    ├── Cross-check: OMS data vs Cash deposited by courier
    ├── Identify discrepancies
    └── Resolve conflicts (không khớp)

[4] Settlement
    ├── Lazada calculates seller payout:
    │   └── Order Amount - Commission - Payment Fee - COD Fee - VAT
    ├── Funds credited to Lazada Wallet
    └── Seller withdraws to bank account
```

### 5.3 Payment Gateway Integration Flow

```
[Buyer checkout] → [Payment Gateway (VNPay/OnePay)]

                        ├── Bank authorization
                        ├── 3D Secure (nếu có)
                        ├── Fraud check

                        ├── Success → Callback → OMS
                        │   └── Order confirmed, escrow locked
                        └── Failed → Notification → Buyer retry
```

### 5.4 Settlement Cycle (Đối soát)

#### Settlement Model

```

│           LAZADA SETTLEMENT FLOW                 │

│  Order Delivered/Completed                       │

│  Escrow Release (sau 7 ngày auto-confirm         │
│  hoặc buyer confirm)                             │

│  Lazada calculates:                              │

│  │ Order Value          100.000đ   │            │
│  │ - Commission (5%)     -5.000đ   │            │
│  │ - Payment fee (2%)   -2.000đ   │            │
│  │ - COD fee (1.5%)    -1.500đ   │            │
│  │ - VAT on fees (10%)   -850đ     │            │

│  │ = Seller Payout     90.650đ    │            │

│  Credited to Lazada Wallet                       │

│  Seller withdraws to bank account                │
│  (Instant / T+1 tùy ngân hàng)                  │

```

#### Settlement Timeline

| Milestone | Thời gian |
|---|---|
| Order completed (buyer confirm hoặc auto-confirm) | Day 0 |
| Escrow release + calculation | Day 0-1 |
| Funds in Lazada Wallet | Day 1-2 (L+2 model) |
| Seller withdraw to bank | Instant hoặc T+1 |
| Settlement report available | Hàng tuần |

**L+2 Model chi tiết:**
- **L (Last Mile Delivery)** = Ngày buyer nhận hàng hoặc auto-confirm
- **+2 business days** = Thời gian Lazada xử lý settlement
- Seller nhận tiền trong Lazada Wallet sau L+2
- Settlement reports: Available hàng tuần trong Seller Center > Finance

### 5.5 Fee Structure Tổng hợp

| Loại phí | Mức phổ biến | Ghi chú |
|---|---|---|
| **Commission** | 1-8% | Tùy danh mục; Fashion 5-8%, Electronics 1-4% |
| **Payment Handling Fee** | ~2% | Áp dụng cho online payment |
| **COD Collection Fee** | 1-2% | Chỉ áp dụng cho COD orders |
| **VAT on fees** | 10% | Thuế GTGT trên tổng fees |
| **Fulfillment Fee (FBL)** | Variable | Tùy weight/dimension/zone |
| **Promoted Ads Fee** | CPC/CPM | Lazada Sponsored Solutions |

### Pain Points

| Pain Point | Mô tả |
|---|---|
| COD reconciliation discrepancy | Cash deposit từ courier không khớp với OMS |
| Settlement delay | L+2 có thể kéo dài hơn nếu holiday/weekend |
| Commission opaque | Seller không luôn hiểu rõ breakdown fees |
| Wallet withdrawal minimum | Có minimum withdrawal amount |
| Refund reversal complication | Khi buyer refund, quá trình reverse settlement phức tạp |

### Technology Hỗ trợ

| Technology | Chức năng |
|---|---|
| **Payment Gateway Integration** | VNPay, OnePay, Napas, Visa/MC SDKs |
| **Escrow System** | Hold & release funds theo order lifecycle |
| **Finance Dashboard** | Seller xem settlement reports, withdrawal |
| **COD Reconciliation Engine** | Cross-check cash collection vs OMS |
| **Fraud Detection** | Real-time payment fraud screening |

> **Nguồn:** Seller Center Finance section, Lazada Payment Policy, COD reconciliation documentation

---

## 6. VẬN CHUYỂN & GIAO NHẬN (Logistics & Delivery)

### 6.1 Tổng quan Hệ thống Logistics

#### Actors
- **Internal:** Lazada Logistics Team, Fulfillment Operations, Last-mile Delivery Team
- **External:** 3PL Partners, Courier/Riders, Warehouse operators

#### Ma trận Logistics Options

```

│                    LAZADA VN LOGISTICS MATRIX                 │

│    Model        │    Mô tả                                    │

│ FBL             │ Seller giao hàng vào kho Lazada            │
│ (Fulfilled by   │ Lazada pick, pack, ship, handle returns    │
│  Lazada)        │ Badge: "Fulfilled by Lazada"               │
│                 │ Ưu: nhanh hơn, higher ranking              │

│ FBS + LEX       │ Seller tự pack, giao cho LEX pickup        │
│ (LEX Express    │ LEX xử lý last-mile                       │
│  pickup)        │ Phổ biến nhất với seller vừa và nhỏ        │

│ FBS + 3PL       │ Seller tự giao cho 3PL partner             │
│ (GHN/GHTK/      │ seller book pickup hoặc drop-off hub      │
│  J&T/etc.)      │ Phổ biến với seller muốn control chi phí  │

│ Seller Self-    │ Seller tự giao hàng (chỉ cho đơn nội      │
│ Delivery        │ thành, special case)                       │

```

### 6.2 LEX Express (Lazada Express)

#### Actors
- **Internal:** Lazada Logistics Division
- **External:** Riders/couriers, Sorting hub operators

#### Quy trình LEX

```
[1] Pickup
    ├── Seller book pickup trong Seller Center
    ├── LEX rider đến pickup tại kho/seller location
    ├── Cutoff: 14:00-17:00 (tùy khu vực)
    └── Package scanned & in system

[2] Sorting
    ├── Package về Regional Sorting Hub
    │   ├── Hub Hà Nội (North)
    │   ├── Hub TP.HCM (South)
    │   └── Hub trung gian (nếu cần)
    ├── Scan & sort by destination zone
    └── Loaded onto transport vehicle

[3] Transport
    ├── Inter-city: Truck transport giữa hubs
    ├── Overnight processing (nếu cần)
    └──đến destination hub

[4] Last-Mile Delivery
    ├── Last-mile courier nhận package
    ├── Delivery attempt 1
    │   ├── Success → Delivered
    │   └── Fail → Reason noted (không có người, sai địa chỉ...)
    ├── Delivery attempt 2 (1-2 ngày sau)
    ├── Delivery attempt 3 (final)
    └── If all fail → Return to seller
```

**LEX Service Levels:**

| Service | Timeframe | Chi phí |
|---|---|---|
| **Standard Delivery** | 2-5 ngày (nội thành), 5-7 ngày (ngoại thành) | Phổ thông |
| **Express Delivery** | 1-2 ngày (nội thành) | Cao hơn |
| **Same-Day Delivery** | Trong ngày (nội thành lớn: HN, HCMC) | Cao nhất, limited zones |

### 6.3 3PL Partners

#### Danh sách chính

| 3PL | Tên đầy đủ | Coverage | Đặc điểm |
|---|---|---|---|
| **GHN** | Giao Hàng Nhanh | Toàn quốc | Nhanh, reliable, cost-effective |
| **GHTK** | Giao Hàng Tiết Kiệm | Toàn quốc | Rẻ nhất, phù hợp đơn giá trị thấp |
| **J&T Express** | J&T Express VN | Toàn quốc | Mạnh COD, app hiện đại |
| **BEST Express** | BEST Express VN | Toàn quốc | Growth nhanh |
| **Viettel Post** | Viettel Post | Toàn quốc | Network phủ rộng nhất (huyện/xã) |
| **VNPost** | Bưu chính VN | Toàn quốc | Nhà nước, phủ nông thôn |

#### So sánh COD Handling

| 3PL | COD cycle | COD fee | Ghi chú |
|---|---|---|---|
| LEX | Daily deposit | Included in shipping fee | Seamless integration |
| GHN | 2-3 business days | 1-1.5% | Reliable COD processing |
| GHTK | 2-4 business days | 1-1.5% | Cheapest option |
| J&T | 1-2 business days | 1.5-2% | Fast COD settlement |
| Viettel Post | 3-5 business days | 1-2% | Rural coverage |

### 6.4 Warehouse & Fulfillment Centers

#### FBL Warehouse Network (Vietnam)

| Warehouse Location | Zone Coverage | Primary Categories |
|---|---|---|
| **Hà Nội** (North) | Northern Vietnam | General merchandise |
| **TP.HCM** (South) | Southern Vietnam | General merchandise |
| **Regional Sorting Hubs** | In-transit sorting | N/A |

#### FBL Process

```
[1] Seller sends inventory to Lazada warehouse
    ├── Create inbound shipment order trong Seller Center
    ├── Pack products theo FBL packaging guidelines
    ├── Ship to designated warehouse
    └── Warehouse receives & counts inventory

[2] Storage
    ├── Products stored in designated zones
    ├── Inventory tracked in WMS
    ├── Seller pays storage fee (per cbm/day)
    └── Inventory aging alerts

[3] Order Processing (Pick & Pack)
    ├── Order received → WMS generates pick list
    ├── Picker picks from shelf
    ├── Packer verifies & packs
    ├── Shipping label printed
    └── Ready for handover

[4] Returns Processing
    ├── Returned items received at warehouse
    ├── Inspection: condition check
    ├── Restock (nếu còn tốt) hoặc dispose
    └── Inventory updated
```

### 6.5 Last-Mile Delivery Challenges

| Challenge | Mô tả | Lazada's approach |
|---|---|---|
| **COD rejection** | Buyer từ chối nhận hàng | Multiple attempts, SMS/call confirmation |
| **Wrong address** | Sai địa chỉ giao hàng | Verification at checkout |
| **Remote/rural areas** | Vùng sâu vùng xa | Partnership with Viettel Post/VNPost |
| **Traffic congestion** | ùn tắc giao thông urban | Optimized route planning, time windows |
| **Package damage** | Hỏng trong quá trình vận chuyển | Quality packaging standards |
| **Theft/pilferage** | Mất cắp | Package tracking, insurance |

### 6.6 Same-Day Delivery

| Tiêu chí | Chi tiết |
|---|---|
| **Khu vực** | Hà Nội nội thành, TP.HCM nội thành |
| **Cutoff** | Order trước 12:00 noon |
| **Delivery window** | Trong ngày (4-8 giờ) |
| **Applies to** | FBL products (ở kho gần buyer) |
| **Phí** | Premium shipping fee |
| **Limitations** | Không áp dụng COD, chỉ online payment |

### Technology Hỗ trợ

| Technology | Chức năng |
|---|---|
| **TMS (Transportation Management System)** | Quản lý toàn bộ logistics flow |
| **WMS (Warehouse Management System)** | Quản lý kho FBL, inventory |
| **Route Optimization** | Tối ưu lộ trình giao hàng |
| **Real-time Tracking** | GPS tracking trên app |
| **COD Reconciliation System** | Đối soát COD |
| **Delivery Management App** | Cho courier/rider |
| **Seller Logistics Dashboard** | Theo dõi shipment status |

> **Nguồn:** Lazada Logistics documentation, Seller Center Shipping section, 3PL partner announcements, seller community feedback

---

## 7. HOÀN TRẢ & HOÀN TIỀN (ỀN  

### 7.1 Return Policy Overview

#### Actors
- **Internal:** Return Operations Team, Quality Inspection Team, Customer Service, Finance Team
- **External:** Buyer, Seller, Logistics Partner (pickup/return shipping)

#### Chính sách trả hàng

| Tiêu chí | Chi tiết |
|---|---|
| **Return Window** | 7 ngày sau khi nhận hàng (standard); 15 ngày cho LazMall |
| **Return Condition** | Sản phẩm phải nguyên vẹn, đầy đủ phụ kiện, original packaging |
| **Free Return** | Lazada chịu phí return shipping (trong chính sách Free Return) |
| **Excluded Items** | Sản phẩm hygiene (bloomers, underwear), perishables, digital goods, custom items |

#### Các lý do trả hàng được chấp nhận

| Lý do | Category | Buyer/Seller chịu |
|---|---|---|
| **Hàng bị hư hỏng** (Damaged) | Product Quality | Seller |
| **Hàng giả** (Counterfeit) | Authenticity | Seller |
| **Sai hàng** (Wrong item) | Order Accuracy | Seller |
| **Không đúng mô tả** (Not as described) | Product Match | Seller |
| **Hàng không hoạt động** (Defective) | Product Quality | Seller |
| **Giao trễ** (Late delivery) | Logistics | Seller/Lazada |
| **Thay đổi ý thích** (Change of mind) | Preference | Buyer (nếu đủ điều kiện) |

### 7.2 Return & Refund Process (Step-by-Step)

```

 PHASE 1: BUYER INITIATES RETURN

[Step 1] Buyer submits return request
    ├── Lazada App → My Orders → Select order → Return/Refund
    ├── Select reason code từ dropdown
    ├── Upload evidence (photos/videos)
    ├── Write description
    └── Submit request

[Step 2] System validates request
    ├── Check return window (<= 7 ngày từ delivery)
    ├── Check eligible category (không excluded)
    ├── Auto-approve nếu reason hợp lệ + trong window
    └── Notify buyer: Return approved

 PHASE 2: RETURN SHIPPING

[Step 3] Logistics arrangement
    ├── Lazada arranged pickup (most common):
    │   ├── Courier hẹn ngày pickup
    │   ├── Buyer pack lại sản phẩm
    │   └── Courier pickup tại địa chỉ buyer
    ├── Seller arranged pickup (some cases):
    │   └── Seller tự arranges return logistics
    └── Drop-off (some cases):
        └── Buyer drop-off tạichỉ định hub

[Step 4] Product in transit (it  
    ├── Tracking available cho buyer & seller
    └── Delivery to return hub/seller warehouse

 PHASE 3: INSPECTION

[Step 5] Inspection Process
    ├── Returned product arrives tại inspection hub
    ├── QC team inspects:
    │   ├── Product condition (new/good/damaged/used)
    │   ├── Completeness (accessories, packaging)
    │   ├── Matches buyer's claim
    │   ├── Authenticity check (if counterfeit claimed)
    │   └── Document findings
    ├── Inspection timeline: 1-5 business days
    └── Inspection result → Decide next step

[Step 6] Inspection Decision
    ├── APPROVED (Return accepted :
    │   ├── Product matches claim
    │   └── Proceed to refund
    ├── PARTIAL APPROVED:
    │   ├── Product damaged more than expected
    │   └── Partial refund (deducted damage fee)
    └── REJECTED (Return deniedD  :
        ├── Product condition doesn't match claim
        ├── No defect found
        ├── Product used/damaged by buyer
        └── Returned to seller, buyer notified
```

### 7.3 Refund Process & Timeline

```

 PHASE 4: REFUND PROCESSING

[Step 7] Refund calculation
    ├── Full refund: 100% order value
    ├── Partial refund: Negotiated amount
    └── Includes shipping fee refund (nếu lỗi seller)

[Step 8] Refund execution
    ├── Refund destination priority:
    │   ├── 1st: Lazada Wallet (instant - 24h)
    │   ├── 2nd: Credit/Debit Card (3-10 business days)
    │   ├── 3rd: E-wallet (5-7 business days)
    │   └── 4th: Bank transfer (3-7 business days)

    ├── COD orders:
    │   └── Refund to Lazada Wallet (không thể refund cash)

    └── Online payment orders:
        └── Refund to original payment method

[Step 9] Refund confirmation
    ├── Buyer receives notification
    ├── Refund visible in order details
    └── Buyer can use Lazada Wallet balance cho lần sau
```

#### Refund Timeline Summary

| Payment Method | Refund Timeline | Refund Destination |
|---|---|---|
| **COD** | 1-3 business days | Lazada Wallet (only) |
| **Credit/Debit Card** | 3-10 business days | Original card |
| **ATM Card** | 3-7 business days | Original bank account |
| **MoMo/ZaloPay** | 5-7 business days | Original e-wallet |
| **Lazada Wallet** | Instant - 24h | Lazada Wallet |
| **Installment** | 5-14 business days | Original installment account |

### 7.4 Cost Responsibility Matrix

| Scenario | Who pays return shipping? | Who bears product cost loss? | Full refund? |
|---|---|---|---|
| **Damaged on arrival** | Seller/Lazada | Seller | Yes |
| **Counterfeit** | Seller/Lazada | Seller | Yes (100% + penalty) |
| **Wrong item** | Seller/Lazada | Seller | Yes |
| **Not as described** | Seller/Lazada | Seller | Yes |
| **Defective** | Seller/Lazada | Seller | Yes |
| **Late delivery** | N/A | Seller (partial refund shipping) | Partial |
| **Change of mind** | Buyer | Buyer | Yes (minus return shipping) |

### 7.5 Inspection Process Detail

```
INSPECTION WORKFLOW AT HUB:

│ 1. RECEIVE RETURN                           │
│    ├── Scan tracking number                 │
│    ├── Verify order ID                      │
│    └── Log into inspection system           │

│ 2. OPEN & INSPECT                           │
│    ├── Check outer packaging condition      │
│    ├── Open package                         │
│    ├── Count items vs packing list          │
│    ├── Check product condition:             │
│    │   ├── Physical damage?                 │
│    │   ├── Signs of use?                    │
│    │   ├── All accessories present?         │
│    │   └── Authenticity check?              │
│    ├── Take photos at each stage            │
│    └── Record inspection result             │

│ 3. DECIDE                                   │
│    ├── PASS → Return to seller inventory    │
│    ├── FAIL → Quarantine for disposal       │
│    └── PARTIAL → Note condition for         │
│         partial refund calculation          │

│ 4. UPDATE SYSTEM                            │
│    ├── Inspection result uploaded           │
│    ├── Decision trigger refund/reject       │
│    └── Inventory updated (nếu restock)      │

```

### 7.6 Buyer Protection Program

| Protection | Coverage |
|---|---|
| **Authenticity Guarantee** | 100% refund nếu hàng giả (LazMall) |
| **7-Day Free Return** | Free return shipping trong 7 ngày |
| **15-Day Return (LazMall)** | Extended return window cho LazMall products |
| **Dispute Resolution** | Lazada mediates nếu buyer-seller không agree |
| **Refund Guarantee** | Buyer được hoàn tiền nếu seller không giao đúng |

### Pain Points

| Pain Point | Mô tả | Ảnh hưởng |
|---|---|---|
| **Long inspection time** | Inspection 3-5 ngày → buyer chờ đợi | Poor experience |
| **COD refund limitation** | COD orders chỉ refund về Wallet, không cash | Buyer inconvenience |
| **Dispute resolution speed** | DR process 5-10 ngày | Buyer & seller frustration |
| **Inspection subjectivity** | QC inspector có thể ra quyết định khác nhau | Inconsistent outcomes |
| **Return shipping delays** | Product mất 1-2 tuần để return đến inspection hub |kéo dài refund timeline |
| **Seller false positives** | Some buyers abuse return policy | Seller cost increase |

### Technology Hỗ trợ

| Technology | Chức năng |
|---|---|
| **Return Management System** | Quản lý toàn bộ flow return/refund |
| **Inspection Tracking App** | QC team ghi nhận inspection result |
| **Refund Processing Engine** | Tự động xử lý refund theo payment method |
| **Inventory Reconciliation** | Cập nhật inventory khi product returned |
| **Buyer-facing Dashboard** | Theo dõi return/refund status |
| **Seller Notification System** | Alert seller về return request + inspection result |

> **Nguồn:** Lazada Buyer Protection Program, Return Policy pages (Lazada Help Center), seller community reports

---

## TỔNG HỢP: MÂU TRANH & THÔNG SỐ QUAN TRỌNG

### Key Pain Points Cross-Cutting

| Pain Point | Quy trình ảnh hưởng | Mức độ |
|---|---|---|
| **COD dominates** (~60-70%) | Payment, Settlement, Logistics | Cao - cash-intensive |
| **Return abuse** | Return & Refund, Dispute | Cao - seller cost |
| **Late dispatch from seller** | Order Processing, Seller Rating | Cao - buyer experience |
| **COD reconciliation complexity** | Payment & Settlement | Trung bình - operational |
| **Inspection speed** | Return & Refund | Trung bình - buyer waiting |
| **Split shipment confusion** | Order Processing | Thấp - UX issue |
| **Multi-3PL coordination** | Logistics | Trung bình - integration |

### Technology Stack Summary

| Technology Layer | Systems |
|---|---|
| **Order Management** | OMS, Cart & Checkout Engine |
| **Payment** | Payment Gateway Integration, Escrow System, COD Collection |
| **Logistics** | TMS, WMS, Tracking System, Route Optimization |
| **Quality** | QC Management System, Inspection Tracking, AI detection |
| **Seller Management** | Seller Center Portal, Performance Dashboard, Rating Algorithm |
| **Customer Service** | Help Center, Chat System, Dispute Resolution System |
| **Fraud Detection** | AI/ML Fraud Engine, Device Fingerprinting, Behavioral Analytics |
| **Finance** | Settlement Engine, Wallet System, Reconciliation Engine |

---

## NGUỒN THAM KHẢO

| Nguồn | URL | Sử dụng cho |
|---|---|---|
| **Lazada Seller Center VN** | [sellercenter.lazada.vn](https://sellercenter.lazada.vn) | Seller onboarding, policies, fees, dashboard |
| **Lazada Help Center VN** | [helpcenter.lazada.vn](https://helpcenter.lazada.vn) | Return/refund policy, buyer protection |
| **Lazada University** | [university.lazada.vn](https://university.lazada.vn) | Seller education, training programs |
| **Lazada.vn** | [lazada.vn](https://www.lazada.vn) | Main marketplace, buyer experience |
| **Seller Community Forums** | Facebook groups, Zalo communities | Seller feedback, operational pain points |
| **Vietnam Ministry of Industry and Trade** | [moit.gov.vn](https://moit.gov.vn) | E-commerce regulations |
| **Lazada Official Blog/Announcements** | Lazada.vn/blogs | Policy updates, feature announcements |

---

**Bản quyền:** Tài liệu tổng hợp nghiên cứu cho mục đích học thuật/phân tích nghiệp vụ.
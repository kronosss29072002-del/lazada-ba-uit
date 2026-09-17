# Nghiên cứu chi tiết 10 Quy trình Lazada VN — Chuẩn bị vẽ BPMN 2.0

> **Mục đích tài liệu:** Cung cấp đủ chi tiết (actor, tools, thời gian, gateway, end event) để vẽ BPMN 2.0 cho 10 quy trình Lazada Việt Nam. Mỗi quy trình đều được thiết kế để đạt **≥7 gateways**.
>
> **Nguồn tham khảo:** Seller Center Lazada VN ([sellercenter.lazada.vn](https://sellercenter.lazada.vn)), Help Center Lazada ([helpcenter.lazada.vn](https://helpcenter.lazada.vn/s/faq)), [Trang "Bán hàng cùng Lazada"](https://pages.lazada.vn/wow/i/vn/sell-on-lazada/register_now/), [Wikipedia — Lazada Group](https://en.wikipedia.org/wiki/Lazada), các tài liệu Seller Performance / Return Policy của Lazada, và case studies BPMN e-commerce (Camunda, Bizagi).
>
> **Lưu ý độ tin cậy:** Phần lớn thông tin định lượng (SLA, thời gian, ngưỡng) được tổng hợp từ chính sách công khai của Lazada và dữ liệu huấn luyện; con số có thể thay đổi theo cập nhật chính sách. Khi vẽ BPMN, hãy ưu tiên kiểm tra lại các SLA trọng yếu (thời gian auto-cancel, thời gian seller phản hồi return, vòng đời thanh toán) trên Seller Center hiện tại.

---

## 0. Tổng quan kiến trúc BPMN đề xuất

| Quy trình | Pools / Lanes chính | Số gateway mục tiêu | End events |
|---|---|---|---|
| 1. Quản lý Nhà bán hàng | Seller, Lazada Ops, Compliance Team, Lazada System | 8 | Approved, Rejected, Suspended, Re-registered |
| 2. Quản lý Tranh chấp | Buyer, Seller, CS Agent, Dispute Team, AI System | 8 | Resolved-buyer wins, Resolved-seller wins, Escalated, Withdrawn |
| 3. Xử lý Đơn hàng Online ⭐ | Buyer, Seller, Lazada System, Payment Gateway, Warehouse, LEX/3PL, COD provider | 10 | Completed, Auto-cancelled, Seller-rejected, Return-initiated, COD-settled, Failed-delivery |
| 4. Hoàn trả & Hoàn tiền | Buyer, Seller, Lazada System, Return/Inspection Center, Finance | 8 | Refunded, Rejected-return, Seller-compensated, Buyer-keeps-item |
| 5. Chăm sóc Khách hàng | Customer, Chatbot/AI, CS Agent, Tier-2 Team, QA | 7 | Resolved, Escalated, Closed-unresolved, CSAT-collected |
| 6. Marketing & Khuyến mãi | Marketing Team, Finance, Creative, Seller, Lazada System | 7 | Launched, Rejected, Completed, Auto-renewed |

**Quy ước chung khi vẽ:**
- **Actor ghi rõ trong annotation của từng task.**
- **Tools** = hệ thống sử dụng (Seller Center, LEX CMS, Payment Gateway, CRM/Helpdesk, Marketing Campaign Hub).
- **Timer event** dùng cho mọi SLA deadline (auto-cancel, hết hạn phản hồi return...).
- **Message flow** giữa các pool dùng cho thông báo (notification seller/buyer).
- Tránh mô hình hóa "bao lô": mỗi gateway exclusive chỉ rẽ 1 nhánh xác định, không OR-ghép nhiều kết quả không liên quan.

---

## 1. Quản lý Nhà bán hàng (Seller Onboarding & Lifecycle)

**Mục tiêu:** Đăng ký → KYC → Phê duyệt → Onboarding → Kinh doanh → Giám sát vi phạm.

### 1.1 Luồng chi tiết từng bước

| # | Bước | Actor | Tools | Ước tính thời gian |
|---|---|---|---|---|
| 1 | Đăng ký tài khoản seller (email/SĐT, OTP) | Seller | sellercenter.lazada.vn, email/SMS OTP | ~5–10 phút |
| 2 | Chọn loại tài khoản (Cá nhân / Doanh nghiệp / LazMall) | Seller | Form đăng ký | ~2 phút |
| 3 | Nhập thông tin doanh nghiệp (tên, MST, địa chỉ, người đại diện) | Seller | Form KYC | ~10–15 phút |
| 4 | Upload hồ sơ (CCCD/CMND, Giấy ĐKKD, MST, giấy ủy quyền thương hiệu nếu có) | Seller | Seller Center — Document Upload | ~10 phút |
| 5 | **Auto-check hồ sơ** (OCR, đối chiếu MST, check danh sách cấm) | Lazada System | OCR + KYC engine + DB đăng ký doanh nghiệp | Tức thì (vài giây) |
| 6 | Kiểm tra tính đầy đủ & hợp lệ hồ sơ | Lazada Ops | Seller Center Review Queue | 1–3 ngày làm việc |
| 7 | **Manual review** rủi ro (nghi ngờ gian lận, thương hiệu nhạy cảm) | Compliance Team | Case management, AML/KYB tools | 1–5 ngày làm việc |
| 8 | Thông báo kết quả phê duyệt / từ chối (kèm lý do) | Lazada System | Email + Seller Center notification | Tức thì sau quyết định |
| 9 | **Onboard education** (Lazada University: listing, vận hành, chính sách) | Seller | Lazada University, video/webinar | 2–4 giờ học (trong 7 ngày) |
| 10 | Thiết lập shop (logo, banner, mô tả, category, ngân hàng nhận tiền) | Seller | Seller Center | 30–60 phút |
| 11 | **First listing** (tạo sản phẩm đầu tiên, đăng tải) | Seller | Seller Center — Product Management | 15–30 phút/sản phẩm |
| 12 | Phê duyệt listing (nếu category yêu cầu) | Lazada Ops | Product moderation queue | 1–3 ngày |
| 13 | Kích hoạt shop, bắt đầu nhận đơn | Lazada System | Seller Center | Tức thì |
| 14 | **Performance monitoring** (điểm chất lượng, tỉ lệ hủy, ship trễ, phản hồi) | Lazada System | Seller Performance Dashboard, Quality Score | Liên tục / theo chu kỳ tuần–tháng |
| 15 | Phát hiện vi phạm (tự động hoặc do report) | Lazada System / Ops | Rule engine, complaint channel | Tức thì / định kỳ |
| 16 | **Violation handling** theo mức độ | Compliance Team + Lazada System | Penalty system, Seller Center | Theo mức độ (xem 1.3) |
| 17 | Kháng cáo vi phạm (nếu seller không đồng ý) | Seller | Seller Center Appeal | 3–7 ngày xử lý |

### 1.2 Gateway đề xuất (≥8)

| # | Gateway | Loại | Điều kiện rẽ nhánh |
|---|---|---|---|
| G1 | **Loại tài khoản** | Exclusive | Cá nhân → luồng KYC cá nhân; Doanh nghiệp → luồng KYC DN; LazMall → thêm yêu cầu thương hiệu |
| G2 | **Auto-check hồ sơ pass/fail** | Exclusive | Hồ sơ đủ + đối chiếu khớp → manual review; thiếu/khớp sai → yêu cầu bổ sung (loop bổ sung tối đa N lần) |
| G3 | **Bổ sung hồ sơ quá hạn?** | Exclusive + Timer | Hết hạn bổ sung (vd 7 ngày) không bổ sung → Rejected |
| G4 | **Manual review: approve/reject** | Exclusive | Chấp thuận → onboarding; từ chối → Rejected (kèm lý do, có thể kháng cáo) |
| G5 | **Hoàn tất khóa học onboarding?** | Exclusive | Chưa hoàn thành trong 7 ngày → khóa luồng listing (hoặc tài khoản tạm khóa); hoàn thành → cho phép listing |
| G6 | **Category listing cần duyệt?** | Exclusive | Category thường → publish ngay; category nhạy cảm (mỹ phẩm, thực phẩm chức năng, điện tử) → chờ duyệt |
| G7 | **Chỉ số performance đạt chuẩn?** | Exclusive | Đạt → tiếp tục kinh doanh; dưới ngưỡng → cảnh báo |
| G8 | **Mức độ vi phạm** | Exclusive (3 nhánh) | Nhẹ → cảnh báo (warning); Trung bình → phạt + delist sản phẩm; Nặng/lặp lại → treo tài khoản (Suspended) |
| G9 | **Kháng cáo được chấp thuận?** | Exclusive | Đồng ý → gỡ phạt, phục hồi; từ chối → giữ nguyên phạt |
| G10 | **Vi phạm nghiêm trọng / tái phạm?** | Exclusive | Suspended vĩnh viễn → yêu cầu re-register (hồ sơ mới, chờ duyệt lại) |

### 1.3 Cơ chế phạt vi phạm (thang xử lý)

```
Warning (cảnh báo) → Delist sản phẩm / giới hạn quyền (flash sale, ads) → 
Suspended tạm thời → Deactivated vĩnh viễn
```
- **Chỉ số chính:** Cancellation Rate (ngưỡng ~5%), Late Shipment Rate (~5%), Order Defect Rate, phản hồi chat, điểm chất lượng shop.
- **Vi phạm điển hình:** hàng giả, mô tả sai, hủy đơn quá nhiều, ship trễ, thao túng review/giá, vi phạm IP.
- Vi phạm nặng 1 lần (hàng giả, sản phẩm cấm) → có thể deactivate ngay, không qua cảnh báo.

### 1.4 End events

- **Approved** — seller active, đủ quyền.
- **Rejected** — hồ sơ không đạt (có thể đăng ký lại).
- **Suspended** — treo do vi phạm.
- **Re-registered** — sau khi treo/deactivate, đăng ký lại qua luồng KYC mới.

---

## 2. Quản lý Tranh chấp (Dispute Resolution)

**Mục tiêu:** Khiếu nại → Phân loại → Điều tra → Quyết định → Kháng cáo → Kết thúc.

### 2.1 Luồng chi tiết từng bước

| # | Bước | Actor | Tools | Ước tính thời gian |
|---|---|---|---|---|
| 1 | Buyer gửi khiếu nại (chọn đơn, loại khiếu nại, mô tả) | Buyer | Lazada app/web — Resolution Center | ~5 phút |
| 2 | Upload bằng chứng (ảnh, video, screenshot chat) | Buyer | App upload | ~5–10 phút |
| 3 | **Auto-categorize** khiếu nại (hàng hư, sai mô tả, thiếu hàng, hàng giả, giao trễ...) | AI System | AI classifier + rule engine | Tức thì |
| 4 | Kiểm tra đủ điều kiện mở tranh chấp (trong thời hạn, đơn hợp lệ) | Lazada System | Rule check | Tức thì |
| 5 | **Gán handler** (CS Agent hoặc Dispute Team tùy độ phức tạp/giá trị) | Lazada System | Workflow/ACD routing | Tức thì |
| 6 | Thông báo seller, yêu cầu phản hồi + bằng chứng trong hạn | Lazada System | Seller Center notification, timer SLA | Seller trả lời trong 48h (thường) |
| 7 | Điều tra (đối chiếu bằng chứng buyer–seller, tracking, QC record, chat log) | CS Agent / Dispute Team | Case management, tracking system, chat log | 2–5 ngày làm việc |
| 8 | Quyết định sơ bộ (buyer thắng / seller thắng / hủy tranh chấp) | Dispute Team | Case decision tool | Sau điều tra |
| 9 | Gửi quyết định cho 2 bên | Lazada System | Email/app notification | Tức thì |
| 10 | **Kháng cáo?** (bên thua kháng cáo trong hạn) | Seller hoặc Buyer | Resolution Center Appeal | Kháng cáo trong 7 ngày (thường) |
| 11 | Điều tra cấp 2 (xem xét kháng cáo, bằng chứng bổ sung) | Dispute Team cấp cao | Case management | 3–7 ngày |
| 12 | Quyết định cuối cùng (final & binding) | Dispute Team / Lazada Legal | Final decision | Theo hồ sơ |
| 13 | Thực thi (hoàn tiền/hoàn hàng hoặc đóng tranh chấp) | Lazada System + Finance | Refund engine, order system | 1–3 ngày |
| 14 | Cập nhật chỉ số dispute rate cho seller | Lazada System | Seller Performance | Tức thì |

### 2.2 Gateway đề xuất (≥8)

| # | Gateway | Loại | Điều kiện rẽ nhánh |
|---|---|---|---|
| G1 | **Loại khiếu nại** | Exclusive (multi-branch) | Hàng hư hỏng / Sai mô tả / Thiếu hàng / Hàng giả / Giao trễ → mỗi loại 1 quy trình điều tra riêng |
| G2 | **Trong thời hạn & hợp lệ?** | Exclusive | Hợp lệ → tiếp tục; quá hạn/không hợp lệ → Withdrawn/Rejected |
| G3 | **Bằng chứng đủ?** | Exclusive | Đủ → điều tra; thiếu → yêu cầu bổ sung (timer, hết hạn → tự đóng/điều tra trên dữ liệu có) |
| G4 | **Giá trị/độ phức tạp cao?** | Exclusive | Thấp → CS Agent tự xử lý; Cao → chuyển Dispute Team / chuyên viên |
| G5 | **Seller phản hồi đúng hạn?** | Exclusive + Timer | Có phản hồi → điều tra có ý kiến seller; hết hạn không phản hồi → xử lý theo bằng chứng buyer / nghiêng về buyer |
| G6 | **Sơ bộ: buyer/seller thắng?** | Exclusive | Buyer thắng → hoàn tiền/hoàn hàng; Seller thắng → đóng tranh chấp |
| G7 | **Bên thua kháng cáo?** | Exclusive + Timer | Kháng cáo trong hạn → điều tra cấp 2; không kháng cáo → chốt quyết định |
| G8 | **Kháng cáo có bằng chứng mới?** | Exclusive | Có → mở lại điều tra; không → giữ nguyên |
| G9 | **Quyết định cấp 2: buyer/seller thắng?** | Exclusive | Đảo ngược hoặc giữ nguyên quyết định |
| G10 | **Cần thực thi hoàn tiền/hoàn hàng?** | Exclusive | Cần → kích hoạt refund flow; không → đóng hồ sơ |

### 2.3 End events

- **Resolved-buyer wins** — hoàn tiền/hoàn hàng cho buyer.
- **Resolved-seller wins** — giữ tiền/hàng cho seller, đóng tranh chấp.
- **Escalated** — đưa lên cấp cao hơn / Lazada Legal / cơ quan bảo vệ người tiêu dùng.
- **Withdrawn** — khiếu nại bị rút hoặc quá hạn không bổ sung.

---

## 3. Xử lý Đơn hàng Online ⭐ (QUY TRÌNH TRỌNG TÂM)

**Mục tiêu:** Giỏ hàng → Thanh toán → Xác nhận → Fulfillment → Giao hàng → COD → Hoàn tất. Đây là quy trình phức tạp nhất, vẽ với nhiều pool và tối thiểu **10 gateways**.

### 3.1 Luồng chi tiết từng bước

| # | Bước | Actor | Tools | Ước tính thời gian |
|---|---|---|---|---|
| 1 | Thêm sản phẩm vào giỏ hàng | Buyer | Lazada app/web | Tức thì |
| 2 | Nhập địa chỉ giao, chọn phương thức vận chuyển (LEX, GHN, Ninja Van, JT, Grab...) | Buyer | Checkout form | ~2–3 phút |
| 3 | Chọn phương thức thanh toán (COD, thẻ, ví Lazada Wallet, chuyển khoản, trả góp) | Buyer | Payment options | ~1 phút |
| 4 | **Xác nhận đơn hàng** (tạo order, khóa giá, kiểm tra tồn kho ảo) | Lazada System | Order engine, inventory service | Tức thì |
| 5 | **Payment processing** (nếu online) — authorize → capture | Payment Gateway + Lazada System | Payment gateway (Visa/Master, Zalopay, Momo, VNPAY...), fraud check | 2–10 giây |
| 6 | Thông báo đơn mới cho seller | Lazada System | Seller Center + app push + email | Tức thì |
| 7 | **Seller accept/reject đơn** (kiểm tra kho, giá, khả năng giao) | Seller | Seller Center — Order Management | Trong 24h–48h (SLA) |
| 8 | **Auto-cancel nếu seller không phản hồi** | Lazada System | Timer event + auto-cancel engine | Hết hạn SLA → auto-cancel |
| 9 | Tạo lệnh lấy hàng (pickup request) cho seller (nếu seller tự giao) hoặc chuyển vào FBL | Lazada System | LEX CMS / FBL system | Tức thì |
| 10 | Seller đóng gói + dán waybill (nếu seller-arranged) | Seller | Seller Center — in waybill | 1–2 giờ (trong SLA ship) |
| 11 | **Warehouse/LEX nhận hàng** (tại điểm gom hoặc FBL) | Warehouse / LEX | WMS, scanning | Theo chuyến lấy hàng (ngày) |
| 12 | **QC inspection** (đối chiếu SKU, số lượng, tình trạng, hạn dùng, waybill) | Warehouse QC | QC checklist, WMS | 5–15 phút/kiện |
| 13 | **Pack** (đóng gói đúng chuẩn, chống vỡ) | Warehouse | Packing station | 2–5 phút |
| 14 | **Label** (in nhãn vận đơn, mã barcode) | Warehouse System | Label printer, WMS | Tức thì |
| 15 | **Handoff** cho LEX/3PL (bàn giao kiện, cập nhật status) | Warehouse → LEX/3PL | Handoff scan, LEX CMS | Theo lịch chuyến |
| 16 | **In-transit** (trung chuyển qua sorting center) | LEX/3PL | Hub/sorting system, tracking | 1–3 ngày (tùy vùng) |
| 17 | **Out-for-delivery** (giao cho tài xế chốt) | LEX/3PL | Rider app, route planning | Sáng/chiều ngày giao |
| 18 | **Delivery attempt** | LEX Rider | Rider app, POD | 1 lần/ngày (có thể retry) |
| 19 | **Giao thành công?** | LEX Rider + Buyer | POD (chữ ký/OTP), scan | Tức thì |
| 20 | **COD settle** (nếu COD) — thu tiền, đối soát, chuyển về seller | COD provider + Finance | COD settlement engine | Thu ngay; đối soát theo chu kỳ (tuần) |
| 21 | Cập nhật trạng thái "Delivered", giải phóng tiền cho seller (trừ hoa hồng, phí ship) | Lazada System + Finance | Settlement engine | Sau giao thành công, theo chu kỳ 7–15 ngày |
| 22 | Buyer xác nhận / hết thời hạn xác nhận tự động | Buyer / System | App, timer | Tự động sau N ngày |

### 3.2 Gateway đề xuất (≥10)

| # | Gateway | Loại | Điều kiện rẽ nhánh |
|---|---|---|---|
| G1 | **Phương thức thanh toán** | Exclusive | COD → luồng thu hộ; Online → payment processing; Ví → e-wallet flow |
| G2 | **Payment thành công?** | Exclusive | Thành công → xác nhận đơn; Thất bại (thẻ bị từ chối, fraud flag) → hủy đơn / yêu cầu thanh toán lại (timer hủy) |
| G3 | **Fraud risk cao?** | Exclusive | Rủi ro thấp → tiếp tục; cao → manual review / hủy đơn |
| G4 | **Seller accept hay reject?** | Exclusive + Timer | Accept → fulfillment; Reject (hết hàng) → cancel; **Hết 24–48h không phản hồi → auto-cancel** |
| G5 | **Phương thức fulfillment** | Exclusive | FBL (hàng trong kho Lazada) → warehouse nội bộ; LGS/Seller-arranged → pickup từ seller |
| G6 | **QC pass/fail** | Exclusive | Pass → pack; Fail (sai SKU, hư, hết hạn) → trả về seller / hủy kiện (loop trả hàng) |
| G7 | **Split shipment?** | Exclusive | Đơn 1 kiện → giao 1 luồng; Đơn nhiều kiện từ nhiều kho → tách thành nhiều sub-order giao song song |
| G8 | **Delivery attempt thành công?** | Exclusive | Thành công → Delivered; Thất bại (vắng nhà, sai địa chỉ) → retry / lịch hẹn |
| G9 | **Retry tối đa đạt?** | Exclusive + Timer | Còn lượt retry → lên lịch lại; hết lượt → trả về kho / hủy → trigger Return flow |
| G10 | **COD hay Online (ở bước settle)?** | Exclusive | COD → thu tiền tại chốt, đối soát; Online → giải phóng tiền qua gateway |
| G11 | **Buyer khiếu nại/hủy sau giao?** | Exclusive | Không → Completed; Có → chuyển Return & Refund process |
| G12 | **Kiện trả về kho: còn dùng được?** | Exclusive | Còn tốt → nhập lại kho (restock); hư hỏng → xử lý tổn thất/bảo hiểm |

### 3.3 Ghi chú logistics Lazada VN

- **LEX (Lazada Express)** = logistics nội bộ; các 3PL bên ngoài: GHN, Ninja Van, Best Inc, AhaMove, JT Express, Grab (theo footer chính thức lazada.vn).
- **FBL / Fulfillment by Lazada**: seller gửi hàng vào kho Lazada, Lazada lo lưu kho → pick → pack → ship (mô hình giống FBA).
- **LGS / Logistics by Seller**: seller tự giao tới điểm gom, LEX/3PL lo last-mile.
- Cắt giờ lấy hàng (cut-off), SLA giao nội địa thường 2–5 ngày; có tùy chọn giao nhanh (next-day).

### 3.4 End events

- **Completed** — giao thành công, xác nhận, settle.
- **Auto-cancelled** — seller không phản hồi trong SLA.
- **Seller-rejected** — seller chủ động hủy (phạt chỉ số).
- **Return-initiated** — sau giao có khiếu nại/hoàn trả.
- **COD-settled** — COD thu hộ + đối soát xong.
- **Failed-delivery** — giao thất bại, trả hàng.

---

## 4. Hoàn trả & Hoàn tiền (Ret 

**Mục tiêu:** Yêu cầu hoàn trả → Duyệt → Gửi hàng về → Kiểm tra → Quyết định hoàn tiền → Bồi thường seller.

### 4.1 Luồng chi tiết từng bước

| # | Bước | Actor | Tools | Ước tính thời gian |
|---|---|---|---|---|
| 1 | Buyer mở yêu cầu hoàn trả trong cửa sổ (thường 7–15 ngày sau giao, tùy category; điện tử có thể 7 ngày; hàng số/hàng tươi không hoàn trả) | Buyer | Lazada app — My Orders → Return/Refund | ~5 phút |
| 2 | Chọn loại yêu cầu: **Full Return / Partial Refund (giữ hàng) / Only Refund (không cần gửi về)** | Buyer | Form lựa chọn | ~2 phút |
| 3 | Chọn lý do hoàn trả (sai mô tả, hư hỏng, thiếu hàng, hàng giả, đổi ý...) | Buyer | Danh sách lý do | ~1 phút |
| 4 | Upload ảnh/video bằng chứng | Buyer | Upload | ~5 phút |
| 5 | **Auto-approve / cần duyệt thủ công?** | Lazada System + Ops | Rule engine (giá trị thấp, lý do rõ ràng → auto) | Tức thì / 1–3 ngày |
| 6 | Thông báo seller, yêu cầu phản hồi (đồng ý / từ chối / kháng nghị) | Lazada System | Seller Center + timer | Seller trả lời trong 48h (nếu không phản hồi → auto-approve) |
| 7 | Seller đồng ý hoặc từ chối | Seller | Seller Center — Return Management | Trong 48h |
| 8 | Nếu từ chối → chuyển sang Dispute Process | Dispute Team | Case system | — |
| 9 | Lịch lấy hàng / điểm trả hàng cho buyer (LEX pickup hoặc drop-off) | Lazada System + LEX | LEX CMS, return label | Sắp lịch trong 1–2 ngày |
| 10 | Buyer gửi hàng về (free ship nếu lỗi seller) | Buyer + LEX | Return waybill | 1–5 ngày vận chuyển |
| 11 | Nhận hàng tại Return/Inspection Center | Warehouse | WMS receiving | Tức thì sau nhận |
| 12 | **Inspection** (đối chiếu SKU, tình trạng, đủ phụ kiện, khớp lý do) | Inspection Team | QC checklist, ảnh lưu hồ sơ | 3–7 ngày làm việc |
| 13 | Quyết định hoàn tiền (pass → hoàn; fail → từ chối hoàn, trả hàng về seller) | Inspection/Dispute Team | Decision tool | Theo kết quả inspection |
| 14 | **Refund processed** theo phương thức | Finance + Lazada System | Refund engine | Xem 4.3 |
| 15 | **Seller compensation / khấu trừ** (trừ vào số dư seller, bồi thường nếu lỗi seller) | Finance | Settlement engine | Theo chu kỳ thanh toán |
| 16 | Cập nhật chỉ số return rate cho seller | Lazada System | Seller Performance | Tức thì |

### 4.2 Gateway đề xuất (≥8)

| # | Gateway | Loại | Điều kiện rẽ nhánh |
|---|---|---|---|
| G1 | **Loại yêu cầu** | Exclusive | Full Return → gửi hàng về; Partial Refund → giữ hàng + hoàn 1 phần; Only Refund → hoàn tiền không cần trả hàng (giá trị thấp / hư khi vận chuyển) |
| G2 | **Trong cửa sổ & hợp lệ?** | Exclusive | Hợp lệ → tiếp tục; quá hạn/ngoài điều kiện → từ chối yêu cầu |
| G3 | **Lý do hoàn trả** | Exclusive (multi-branch) | Lỗi seller (sai, hư, thiếu) → seller chịu phí; Đổi ý/không thích → chính sách theo category; Hàng giả → ưu tiên cao, vào IP/Compliance |
| G4 | **Giá trị đơn & độ rõ ràng → auto hay manual** | Exclusive | Thấp + rõ ràng → auto-approve; Cao/không rõ → duyệt thủ công |
| G5 | **Seller phản hồi?** | Exclusive + Timer | Đồng ý → tiếp; Từ chối → Dispute Process; Hết 48h im lặng → auto-approve |
| G6 | **Inspection pass/fail** | Exclusive | Pass → hoàn tiền; Fail → từ chối, trả hàng về seller, buyer có thể kháng nghị |
| G7 | **Kháng nghị kết quả inspection?** | Exclusive | Buyer kháng nghị → mở lại review; không → đóng hồ sơ |
| G8 | **Phương thức hoàn tiền** | Exclusive | Lazada Wallet (nhanh, gần tức thì); Thẻ/bank transfer (5–15 ngày); COD → hoàn vào ví/bank, KHÔNG hoàn tiền mặt |
| G9 | **Lỗi thuộc về seller?** | Exclusive | Có → seller chịu toàn bộ chi phí + bồi thường; Không (đổi ý) → chính sách/chi phí khác |
| G10 | **Hàng trả về còn bán được?** | Exclusive | Còn tốt → restock lại; hư/hết hạn → tổn thất/loại bỏ |

### 4.3 Thời gian hoàn tiền tham khảo

- **Lazada Wallet:** nhanh nhất (gần tức thì – 1 ngày).
- **Thẻ tín dụng / ngân hàng:** 5–15 ngày làm việc.
- **COD:** không trả tiền mặt; hoàn qua ví/bank sau khi đối soát.
- Seller bị trừ tiền theo chu kỳ thanh toán (thường tuần/nửa tháng), khấu trừ hoa hồng + phí ship + phí hoàn trả.

### 4.4 End events

- **Refunded** — buyer được hoàn tiền.
- **Rejected-return** — không đủ điều kiện / inspection fail.
- **Seller-compensated** — seller được bồi thường (khi lỗi không thuộc seller).
- **Buyer-keeps-item** — partial refund, buyer giữ hàng.

---

## 5. Chăm sóc Khách hàng (Customer Service)

**Mục tiêu:** Tiếp nhận vấn đề (chat/hotline/email) → Chatbot triage → Tự phục vụ / Agent → Điều tra → Xử lý → CSAT.

### 5.1 Luồng chi tiết từng bước

| # | Bước | Actor | Tools | Ước tính thời gian |
|---|---|---|---|---|
| 1 | Khách hàng báo vấn đề qua kênh: Chat (app/web), Hotline, Email, Fanpage/social | Customer | App, hotline IVR, email, social inbox | ~1–3 phút |
| 2 | **Chatbot triage** — nhận diện ý định, phân loại (đơn hàng, hoàn tiền, tài khoản, thanh toán, giao hàng...) | Chatbot / AI | NLP, intent classifier, FAQ KB | Tức thì |
| 3 | **Self-service?** — gợi ý FAQ/tự tra cứu trạng thái đơn | Chatbot / AI | Knowledge base, tự động tra cứu order | Tức thì |
| 4 | Tạo ticket nếu không tự giải quyết được | AI + System | CRM/Helpdesk (ticket auto-create) | Tức thì |
| 5 | **Phân hạng ưu tiên & gán agent** (theo issue type, giá trị đơn, khách VIP) | ACD/System | Routing engine, skill-based routing | Tức thì |
| 6 | CS Agent nhận ticket, xác minh danh tính/đơn hàng | CS Agent | CRM, order lookup | 1–5 phút |
| 7 | Điều tra (tracking, payment record, chat log, chính sách) | CS Agent | Tra cứu order/payment, KB | 10–30 phút |
| 8 | **Escalation?** — vượt thẩm quyền/giá trị cao/khiếu nại phức tạp | CS Agent + System | Escalation rule | Theo ngưỡng |
| 9 | Xử lý cấp 2 (Dispute Team, Tech, Finance, Compliance) | Tier-2 Team | Case management | 1–5 ngày |
| 10 | Đưa ra giải pháp & giải quyết | CS Agent / Tier-2 | Solution toolkit (refund, reship, coupon) | Tức thì – 3 ngày |
| 11 | Xác nhận với khách hàng, đóng ticket | CS Agent + Customer | CRM close, notification | Tức thì |
| 12 | **CSAT survey** (đánh giá 1–5 sao, feedback) | Customer | Survey tool (sau khi đóng ticket) | ~1 phút |
| 13 | Phân tích CSAT, QC chất lượng tương tác | QA/BI | QA scorecard, BI dashboard | Định kỳ (tuần/tháng) |

### 5.2 Gateway đề xuất (≥7)

| # | Gateway | Loại | Điều kiện rẽ nhánh |
|---|---|---|---|
| G1 | **Kênh tiếp nhận** | Exclusive | Chat / Hotline / Email / Social → mỗi kênh có SLA & xử lý riêng |
| G2 | **Chatbot giải quyết được?** | Exclusive | Intent rõ + tự phục vụ thành công → Resolved (không cần agent); phức tạp → tạo ticket |
| G3 | **Tự phục vụ thành công?** | Exclusive | Tra cứu FAQ/trạng thái đủ → đóng; không → chuyển agent |
| G4 | **Loại vấn đề** | Exclusive (multi-branch) | Đơn hàng / Hoàn tiền / Tài khoản & bảo mật / Thanh toán / Giao hàng / Khiếu nại khác |
| G5 | **Khách hàng tier / giá trị đơn** | Exclusive | Khách VIP / đơn giá trị cao → ưu tiên agent giàu kinh nghiệm (priority queue); thường → normal queue |
| G6 | **Vượt ngưỡng escalation?** | Exclusive | Trong thẩm quyền → tự xử lý; vượt ngưỡng (giá trị, rủi ro pháp lý, lỗi hệ thống) → Tier-2 |
| G7 | **Khách hàng đồng ý giải pháp?** | Exclusive | Đồng ý → đóng ticket; không đồng ý → escal thêm / mở dispute |
| G8 | **Ticket mở lại?** | Exclusive | Khách phản hồi lại trong hạn → mở lại ticket; không → đóng hẳn |
| G9 | **CSAT thấp?** | Exclusive | Điểm thấp → QC review + gọi lại (follow-up); đạt → kết thúc |

### 5.3 End events

- **Resolved** — giải quyết xong, CSAT thu được.
- **Escalated** — chuyển cấp 2 / bộ phận khác / cơ quan ngoài.
- **Closed-unresolved** — khách không phản hồi / từ chối giải pháp, đóng ticket.
- **CSAT-collected** — kết thúc có dữ liệu đánh giá.

---

## 6. Marketing & Khuyến mãi (Campaign & Promotion)

**Mục tiêu:** Lập kế hoạch → Duyệt ngân sách → Thiết kế → Seller tham gia → Launch → Giám sát → Đánh giá.

### 6.1 Luồng chi tiết từng bước

| # | Bước | Actor | Tools | Ước tính thời gian |
|---|---|---|---|---|
| 1 | Lập kế hoạch chiến dịch (mục tiêu GMV, ngân sách, thời gian: 9.9, 10.10, 11.11, 12.12, sinh nhật, brand day) | Marketing Team | Campaign planning tool, calendar | 1–4 tuần trước launch |
| 2 | Dự toán ngân sách & đề xuất (voucher, flash sale subsidy, ads, logistics subsidy) | Marketing Team | Finance planning | 3–7 ngày |
| 3 | **Duyệt ngân sách** theo hạng mức | Finance / CMO | Approval workflow | Theo hạng (xem G2) |
| 4 | Thiết kế creative (banner, landing page, KV, video) | Creative Team | Design tools | 3–7 ngày |
| 5 | Duyệt nội dung & tuân thủ (không phóng đại, đúng quy định quảng cáo) | Marketing Lead + Legal | Content approval | 1–2 ngày |
| 6 | Mở cổng đăng ký cho seller tham gia (chọn SKU, đề xuất giá khuyến mãi) | Lazada System + Seller | Campaign Hub / Seller Center | Cổng mở 7–14 ngày |
| 7 | **Kiểm tra điều kiện seller** (điểm chất lượng, tỉ lệ hủy, lịch sử vi phạm) | Lazada System | Eligibility engine | Tức thì |
| 8 | **Kiểm tra giá khuyến mãi** (đủ giảm giá tối thiểu, không bán cao hơn giá gốc đã đăng ký) | Lazada System | Price validation | Tức thì |
| 9 | Duyệt SKU tham gia (tự động hoặc thủ công với category nhạy cảm) | Lazada Ops | Campaign review | 1–3 ngày |
| 10 | **Launch** (kích hoạt banner, voucher, flash sale theo khung giờ) | Lazada System | Campaign engine, scheduling | Đúng giờ hẹn |
| 11 | **Giám sát realtime** (GMV, lượng đặt, tồn kho, tỉ lệ hủy, khiếu nại giá) | Lazada System + Marketing | BI dashboard, alert | Liên tục trong chiến dịch |
| 12 | **Xử lý sự cố trong chiến dịch** (hết kho, lỗi giá, scam seller) | Marketing + Ops + Compliance | War room, rule engine | Tức thì / trong ngày |
| 13 | Rà soát tồn kho & kích hoạt flash sale phụ (nếu cần) | Marketing + Seller | Flash sale slots | Theo khung giờ |
| 14 | **Post-campaign analysis** (ROI, GMV vs mục tiêu, tỉ lệ hoàn trả, hiệu quả từng tool) | Marketing + BI | BI/reporting | 3–7 ngày sau chiến dịch |
| 15 | Báo cáo & điều chỉnh ngân sách cho chiến dịch kế tiếp | Marketing + Finance | Reporting, review meeting | Theo chu kỳ |

### 6.2 Gateway đề xuất (≥7)

| # | Gateway | Loại | Điều kiện rẽ nhánh |
|---|---|---|---|
| G1 | **Loại chiến dịch** | Exclusive (multi-branch) | Flash sale / Mega campaign (11.11, 12.12) / Brand day / Voucher nền / Livestream → luồng & nguồn ngân sách khác nhau |
| G2 | **Hạng mức ngân sách** | Exclusive | Dưới ngưỡng → duyệt bởi trưởng bộ phận; trên ngưỡng → CFO/CMO; ngân sách lớn → hội đồng phê duyệt |
| G3 | **Ngân sách được duyệt?** | Exclusive | Được duyệt → tiến hành; Bị điều chỉnh → thiết kế lại theo ngân sách mới; Từ chối → dừng, Rejected |
| G4 | **Creative/nội dung đạt tuân thủ?** | Exclusive | Đạt → mở cổng đăng ký; Không → chỉnh sửa (loop) |
| G5 | **Seller đủ điều kiện?** | Exclusive | Đủ (điểm ≥ ngưỡng, không vi phạm) → cho tham gia; Không → từ chối seller |
| G6 | **SKU đủ giảm giá tối thiểu?** | Exclusive | Đạt → duyệt SKU; Không đạt → yêu cầu seller điều chỉnh giá hoặc loại SKU |
| G7 | **Cần duyệt thủ công SKU nhạy cảm?** | Exclusive | Category thường → auto-approve; Nhạy cảm → duyệt thủ công |
| G8 | **Hiệu suất chiến dịch đạt KPI?** | Exclusive | Đạt → tiếp tục/scale; Không đạt → tăng voucher/ads hoặc cắt giảm sớm |
| G9 | **Sự cố nghiêm trọng?** | Exclusive | Có (hết kho ồ ạt, sai giá, hàng giả) → kích hoạt xử lý khẩn cấp (đình chỉ SKU/seller); Không → chạy bình thường |
| G10 | **Kết thúc chiến dịch: auto-renew hay dừng?** | Exclusive | Có ngân sách & KPI tốt → tự gia hạn; Hết ngân sách/không hiệu quả → dừng |

### 6.3 Điều kiện seller tham gia (điển hình)

- Điểm chất lượng shop đạt ngưỡng (thường ≥ 4.0 sao, tùy campaign).
- Tỉ lệ hủy & ship trễ dưới ngưỡng (thường < 5%).
- Shop active, không vi phạm/treo.
- Giá khuyến mãi phải thấp hơn giá gốc tối thiểu (thường giảm 5–20%).
- Tồn kho đủ để đáp ứng lượng dự kiến.
- Lý do từ chối: không đủ giảm giá, chỉ số kém, listing vi phạm, tồn kho thiếu.

### 6.4 End events

- **Launched** — chiến dịch kích hoạt, chạy đúng lịch.
- **Rejected** — ngân sách/content không được duyệt, hoặc seller không đủ điều kiện.
- **Completed** — kết thúc, báo cáo post-campaign xong.
- **Auto-renewed** — gia hạn do đạt KPI + còn ngân sách.

---

## 7. Bảng kiểm tra nhanh cho người vẽ BPMN

**Trước khi vẽ mỗi quy trình, kiểm tra:**
- [ ] Đủ **≥7 gateways** (exclusive/inclusive, có timer event cho SLA).
- [ ] Mỗi task ghi đủ **actor + tool**.
- [ ] Ghi **estimated time** trên annotation hoặc timer event.
- [ ] Mỗi pool/lane = đúng actor; message flow dùng cho notification giữa các pool.
- [ ] End events đúng danh sách ở mục 0 (không dùng "End" chung chung).
- [ ] Không có gateway "bao lô" (OR nhiều kết quả không liên quan) — mỗi gateway chỉ rẽ 1 điều kiện xác định.
- [ ] Quy trình 3 (Đơn hàng) là phức tạp nhất — vẽ riêng, cân nhắc tách sub-process "Warehouse Fulfillment" và "COD Settlement".

**Trọng tâm khi vẽ:**
1. Quy trình 3 phải thể hiện **split shipment**, **QC fail loop**, **auto-cancel timer (24–48h)**, **COD vs online settle**.
2. Quy trình 4 phải phân biệt **Full Return / Partial Refund / Only Refund** ngay gateway đầu tiên.
3. Quy trình 1 phải thể hiện **thang phạt Warning → Delist → Suspend → Deactivate → Re-register**.
4. Quy trình 2 phải có **vòng kháng cáo cấp 2** với timer.
5. Quy trình 5 phải có **vòng chatbot → agent → tier-2** và **CSAT loop**.
6. Quy trình 6 phải có **vòng duyệt ngân sách theo hạng mức** và **auto-renew**.

---

## 8. Nguồn tham khảo

- [Lazada Vietnam Seller Center](https://sellercenter.lazada.vn)
- [Lazada Help Center VN (VN  ](https://helpcenter.lazada.vn/s/faq)
- [Lazada "Sell on Lazada" — register page](https://pages.lazada.vn/wow/i/vn/sell-on-lazada/register_now/)
- [Lazada Vietnam homepage (delivery partners: LEX, GHN, Ninja Van, Best Inc, AhaMove, JT, Grab)](https://www.lazada.vn)
- [Wikipedia — Lazada Group (15-day return policy, COD, marketplace model, next-day delivery)](https://en.wikipedia.org/wiki/Lazada)
- [Lazada Seller Performance / Return Policy documentation (qua Seller Center Help Hub)](https://sellercenter.lazada.vn)

**Lưu ý cuối:** Các SLA và con số ngưỡng (48h phản hồi return, 24–48h auto-cancel, 7–15 ngày cửa sổ hoàn trả, ngưỡng 5% hủy/ship trễ, 7–15 ngày vòng thanh toán, 5–20% giảm giá tối thiểu campaign) là ước lượng dựa trên chính sách công khai và kinh nghiệm vận hành marketplace. Khi chốt BPMN cho production, hãy verify lại trên Seller Center bản hiện hành và điền con số chính xác vào các timer event.
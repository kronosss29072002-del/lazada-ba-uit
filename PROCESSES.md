# Tổng quan 10 Quy trình Nghiệp vụ Lazada Việt Nam

> **Đồ án IE203** — Hệ thống Quản trị Quy trình Nghiệp vụ
> **Công ty:** Lazada Việt Nam (Công ty TNHH Recess)
> **Mô hình:** Kiến trúc 3 lớp — Management / Core / Support

---

## Mô hình kiến trúc 3 lớp (House Diagram)

```
┌─────────────────────────────────────────────────────────────────────┐
│              KIẾN TRÚC QUY TRÌNH NGHIỆP VỤ LAZADA VN              │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌────────────── NHÓM QUẢN LÝ (Management - 3 quy trình) ────────┐ │
│  │  P1. Quản lý Nhà bán hàng (Seller Management)                  │ │
│  │  P2. Quản lý Tranh chấp & Rủi ro (Dispute & Risk Management)  │ │
│  │  P3. Quản lý Nhân sự & Đào tạo (HR & Training - Lazada Univ)  │ │
│  └────────────────────────────────────────────────────────────────┘ │
│                                                                     │
│  ┌────────────── NHÓM CỐT LÕI (Core - 4 quy trình) ────────────┐ │
│  │  P4. Xử lý Đơn hàng Online (Order Processing)  ◄── CHÍNH     │ │
│  │  P5. Thanh toán & Đối soát (Payment & Settlement)             │ │
│  │  P6. Hoàn trả & Hoàn tiền (Return & Refund)                   │ │
│  │  P7. Vận chuyển & Giao nhận (Logistics & Delivery)             │ │
│  └────────────────────────────────────────────────────────────────┘ │
│                                                                     │
│  ┌────────────── NHÓM HỖ TRỢ (Support - 3 quy trình) ──────────┐ │
│  │  P8. Chăm sóc Khách hàng (Customer Service - CSKH)            │ │
│  │  P9. Marketing & Khuyến mãi (Marketing & Campaigns)           │ │
│  │  P10. Quản lý ICT & Hạ tầng (IT Operations)                  │ │
│  └────────────────────────────────────────────────────────────────┘ │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Bảng tổng hợp 10 quy trình nghiệp vụ

| STT | Tên quy trình | Nhóm | Tác nhân chính (Actors) | Khách hàng quy trình | Kết quả có thể (Outcomes) |
|-----|--------------|------|-------------------------|---------------------|---------------------------|
| P1 | Quản lý Nhà bán hàng | Quản lý | Seller, Lazada System, Compliance, Legal | Seller | Duyệt bán hàng / Từ chối / Cảnh cáo / Khóa tài khoản |
| P2 | Quản lý Tranh chấp & Rủi ro | Quản lý | Buyer, Seller, CS Agent, Escalation, System AI | Buyer, Seller | Full refund / Bác bỏ / Split refund / Khóa tài khoản gian lận |
| P3 | Quản lý Nhân sự & Đào tạo | Quản lý | HR Team, Lazada University, Seller | Seller, Nhân viên | Đào tạo hoàn tất / Phát hiện vi phạm / Cập nhật chứng chỉ |
| P4 | Xử lý Đơn hàng Online | Cốt lõi | Buyer, System, Seller, 3PL/LEX, Payment GW | Buyer, Seller | Giao thành công / Hủy đơn / Giao thất bại hoàn về |
| P5 | Thanh toán & Đối soát | Cốt lõi | Payment GW, System, Finance, Seller, NH | Seller, Lazada | Thanh toán OK / Giải ngân Ví / Xử lý lệch dòng tiền |
| P6 | Hoàn trả & Hoàn tiền | Cốt lõi | Buyer, System, Seller, CS Agent, 3PL | Buyer | Complete refund / Reject return / Instant refund low-value |
| P7 | Vận chuyển & Giao nhận | Cốt lõi | Seller, LEX, 3PL (GHN/J&T/Grab), Shipper, Buyer | Buyer | Giao thành công 1st / Hẹn giao lại / Chuyển hoàn Seller |
| P8 | Chăm sóc Khách hàng | Hỗ trợ | Customer, Chatbot AI, Agent T1, Agent T2 | Customer | Giải đáp tức thì / Tạo ticket / Đóng ticket |
| P9 | Marketing & Khuyến mãi | Hỗ trợ | Marketing Team, Seller, Buyer, System | Buyer, Seller | Campaign launch thành công / Điều chỉnh budget / Cancel |
| P10 | Quản lý ICT & Hạ tầng | Hỗ trợ | Dev Team, QA, DevOps, Security | Internal Staff | Deploy tính năng mới / Bug fix / Rollback |

---

## Mô tả chi tiết từng quy trình

### P1. Quản lý Nhà bán hàng (Seller Management)

**Mô tả:** Quy trình onboarding, phê duyệt và giám sát nhà bán hàng trên nền tảng Lazada.

**Các bước chính:**
1. Seller đăng ký tài khoản trên Seller Centre
2. Upload giấy tờ tùy thân (CMND/CCCD) + Giấy phép kinh doanh + Chứng nhận LazMall (nếu có)
3. Hệ thống OCR + AI kiểm tra giấy tờ giả, phân loại rủi ro (Risk Scoring: Low/Medium/High)
4. Compliance review thủ công (24-48h cho Medium/High risk)
5. Phê duyệt / Từ chối tài khoản
6. Giám sát điểm đánh giá và vi phạm sau duyệt
7. Cảnh cáo → Tạm khóa (7 ngày) → Khóa vĩnh viễn (vi phạm nghiêm trọng)

**Tác nhân tham gia:**
- **Internal:** Seller, Compliance Team, Legal, Lazada System (AI)
- **External:** Không có external actors chính

**Khách hàng quy trình:** Seller (người đăng ký bán hàng)

**Kết quả có thể:**
- ✅ Gian hàng được kích hoạt (Seller bán hàng thành công)
- ❌ Hồ sơ bị từ chối vĩnh viễn (thiếu giấy tờ hợp lệ)
- ⚠️ Đã cảnh cáo (vi phạm nhẹ)
- ⚠️ Đã tạm khóa 7 ngày (vi phạm trung bình)
- 🔴 Đã khóa vĩnh viễn (vi phạm nghiêm trọng/lặp lại)

---

### P2. Quản lý Tranh chấp & Rủi ro (Dispute & Risk Management)

**Mô tả:** Giải quyết tranh chấp giữa Buyer và Seller trong khuôn khổ chương trình Bảo vệ Người mua (Lazada Buyer Protection).

**Các bước chính:**
1. Buyer tạo tranh chấp + lý do trên hệ thống
2. Bổ sung bằng chứng (ảnh/video) nếu cần
3. Hệ thống AI tự động thu thập dữ liệu đơn hàng, phân loại (Đơn giản/Phức tạp)
4. Kiểm tra lịch sử SLA của Seller
5. Seller phản hồi trong vòng 48 giờ
6. CS Agent thẩm định toàn bộ hồ sơ và đưa quyết định
7. Cases phức tạp: chuyển lên nhóm chuyên trách (Escalation)
8. Hội đồng thẩm định ra quyết định cuối cùng

**Tác nhân tham gia:**
- **Internal:** Buyer, Seller, CS Agent, Escalation Team, Lazada System (AI)
- **External:** Không có external actors chính

**Khách hàng quy trình:** Buyer (người mua bị khiếu nại), Seller (bị khiếu nại)

**Kết quả có thể:**
- ✅ Giải quyết xong (Buyer được hoàn tiền / Compromise)
- ❌ Tranh chấp bác bỏ (thiếu bằng chứng)
- ✅ AI tự giải quyết (cases đơn giản)

---

### P3. Quản lý Nhân sự & Đào tạo (HR & Lazada University)

**Mô tả:** Quản lý nhân sự nội bộ và chương trình đào tạo Seller thông qua Lazada University.

**Các bước chính:**
1. Lập kế hoạch đào tạo theo quý
2. Xây dựng nội dung khóa học (onboarding, nâng cao, compliance)
3. Publish khóa học lên Lazada University
4. Theo dõi tiến độ học tập của Seller/Staff
5. Đánh giá hiệu quả đào tạo
6. Cập nhật chứng chỉ, nhật ký vi phạm

**Tác nhân tham gia:**
- **Internal:** HR Team, Lazada University, Compliance
- **External:** Seller (tham gia đào tạo)

**Khách hàng quy trình:** Seller, Nhân viên nội bộ

**Kết quả có thể:**
- ✅ Đào tạo hoàn tất (Seller/Nhân viên đạt yêu cầu)
- ⚠️ Phát hiện vi phạm trong quá trình đào tạo
- ✅ Cập nhật chứng chỉ mới

---

### P4. Xử lý Đơn hàng Online (Order Processing) ⭐ Quy trình chính

**Mô tả:** Quy trình end-to-end từ khi Buyer đặt hàng đến khi giao thành công và giải ngân cho Seller.

**Các bước chính:**
1. Buyer xem giỏ hàng và đặt hàng
2. Thanh toán (COD / Thẻ tín dụng / Ví / Chuyển khoản)
3. Validate thông tin đơn hàng tự động
4. Khóa tồn kho + Tạo đơn
5. Kiểm tra gian lận (AI Fraud Detection)
6. Kiểm tra tồn kho
7. Seller xác nhận đơn → Đóng gói → Bàn giao cho LEX/3PL
8. LEX lấy hàng + quét barcode
9. Giao hàng (nhiều lần thử nếu thất bại)
10. Buyer xác nhận nhận hàng → Auto-confirm (7 ngày)
11. Giải ngân cho Seller
12. Hủy đơn (nếu quá hạn 48h Seller không xác nhận / giao hàng thất bại 3 lần)

**Tác nhân tham gia:**
- **Internal:** Buyer, Lazada System, Seller
- **External:** LEX (Lazada Express), 3PL đối tác (GHN, J&T, GrabExpress), Payment Gateway (VNPay, MoMo, ZaloPay)

**Khách hàng quy trình:** Buyer (người mua), Seller (người bán)

**Kết quả có thể:**
- ✅ Đơn hoàn tất (giao thành công + giải ngân)
- ❌ Đơn bị hủy (Buyer hủy / Seller quá hạn / giao hàng thất bại)
- 💰 Đã hoàn tiền (đơn bị hủy → hoàn tiền Buyer)

---

### P5. Thanh toán & Đối soát (Payment & Settlement)

**Mô tả:** Quản lý luồng tiền từ Buyer → Lazada Escrow → Seller, bao gồm COD, thanh toán online, và đối soát.

**Các步骤 chính:**
1. Buyer thanh toán (COD hoặc Online)
2. System giữ tiền tạm thời trong Escrow
3. Đơn hàng hoàn tất → Giải ngân cho Seller (L+2 ngày làm việc)
4. Đối soát COD với 3PL
5. Xử lý lệch dòng tiền
6. Quản lý Commission (1-8% tùy danh mục)
7. Rút tiền từ Ví Seller về tài khoản ngân hàng

**Tác nhân tham gia:**
- **Internal:** Payment Gateway, Lazada System, Finance, Seller
- **External:** VNPay, MoMo, ZaloPay, Ngân hàng

**Khách hàng quy trình:** Seller (nhận tiền), Lazada (thu phí)

**Kết quả có thể:**
- ✅ Thanh toán OK (giải ngân đúng hạn)
- ⚠️ Xử lý lệch dòng tiền (COD discrepancy)
- ✅ Giải ngân Ví Seller thành công

---

### P6. Hoàn trả & Hoàn tiền (Return & Refund)

**Mô tả:** Xử lý yêu cầu đổi trả và hoàn tiền từ Buyer theo chính sách Lazada Buyer Protection.

**Các bước chính:**
1. Buyer gửi yêu cầu đổi trả + lý do
2. Tải lên bằng chứng (ảnh/video)
3. AI phân loại bằng chứng khiếu nại
4. CS thẩm định hồ sơ
5. Đặt lịch pickup hàng hoàn từ LEX/3PL
6. LEX pickup hàng trả
7. Kiểm định hàng hoàn tại kho (≤12h)
8. Kích hoạt lệnh hoàn tiền

**Tác nhân tham gia:**
- **Internal:** Buyer, Lazada System, CS Agent
- **External:** LEX (Lazada Express), 3PL

**Khách hàng quy trình:** Buyer (người yêu cầu hoàn tiền)

**Kết quả có thể:**
- ✅ Hoàn tiền hoàn tất (Full refund)
- ❌ Yêu cầu bị từ chối (thiếu bằng chứng / hết hạn)
- ⚠️ Hoàn tiền instant cho đơn low-value (<200k)

---

### P7. Vận chuyển & Giao nhận (Logistics & Delivery)

**Mô tả:** Quản lý luồng hàng hóa từ kho Seller đến tay Buyer thông qua LEX và các 3PL đối tác.

**Các bước chính:**
1. Tạo vận đơn tự động
2. LEX/3PL pickup hàng từ kho Seller
3. Sort hàng tại kho trung tâm
4. Shipper giao hàng cho Buyer
5. Nếu thất bại: hẹn giao lại (tối đa 3 lần)
6. Nếu thất bại 3 lần: chuyển hoàn Seller

**Tác nhân tham gia:**
- **Internal:** Seller, Lazada System
- **External:** LEX (Lazada Express), GHN, J&T Express, GrabExpress, NINJAVAN

**Khách hàng quy trình:** Buyer (người nhận hàng)

**Kết quả có thể:**
- ✅ Giao thành công lần 1
- ⚠️ Hẹn giao lại (lần 2-3)
- ❌ Chuyển hoàn Seller (3 lần thất bại)

---

### P8. Chăm sóc Khách hàng (Customer Service)

**Mô tả:** Hỗ trợ khách hàng qua nhiều kênh (Chat, Hotline, Email) với hệ thống AI phân loại ticket.

**Các bước chính:**
1. Customer tiếp cận (Chatbot tự động trả lời)
2. AI NLP phân loại vấn đề + mức độ khẩn cấp
3. Nếu giải quyết được → Chatbot xử lý tự động
4. Nếu cần can thiệp → Chuyển CS Tier 1
5. CS Tier 1 lấy lịch sử tương tác, đề xuất giải pháp
6. Nếu phức tạp → Chuyển CS Tier 2
7. CS Tier 2 thẩm định chuyên sâu, xử lý dứt điểm
8. Khảo sát CSAT sau hỗ trợ

**Tác nhân tham gia:**
- **Internal:** Customer, Chatbot AI (Lazada Assistant), CS Tier 1, CS Tier 2
- **External:** Không có external actors chính

**Khách hàng quy trình:** Customer (người cần hỗ trợ)

**Kết quả có thể:**
- ✅ Giải đáp tức thì (qua Chatbot)
- ✅ Tạo ticket theo dõi (cần can thiệp thêm)
- ❌ Đóng ticket (quá hạn SLA / Customer không phản hồi)

---

### P9. Marketing & Khuyến mãi (Marketing & Campaigns)

**Mô tả:** Thiết kế, triển khai và đánh giá các chiến dịch marketing trên nền tảng Lazada (Mega Sale, Flash Sale, Voucher...).

**Các bước chính:**
1. Nghiên cứu thị trường + Lập bản đề xuất chiến dịch
2. Phân khúc đối tượng mục tiêu
3. Thiết kế concept + Kế hoạch chi tiết
4. Thẩm định ngân sách & ROI
5. Phê duyệt (Director-level)
6. Cấu hình chiến dịch trên hệ thống
7. Kiểm tra & giả lập áp mã voucher
8. Kích hoạt chiến dịch (ví dụ: 12.12 Siêu Hội Mua Sắm)
9. Theo dõi hiệu năng realtime
10. Lập báo cáo tổng kết & đánh giá ROI

**Tác nhân tham gia:**
- **Internal:** Marketing Team, Lazada System
- **External:** Sellers (tham gia chương trình), Buyers (người tham gia mua sắm)

**Khách hàng quy trình:** Buyer (người hưởng ưu đãi), Seller (người tham gia chương trình)

**Kết quả có thể:**
- ✅ Chiến dịch kết thúc thành công (ROI đạt target)
- ⚠️ Điều chỉnh budget (hiệu quả dưới kỳ vọng)
- ❌ Hủy chiến dịch (phát hiện vi phạm pháp lý)

---

### P10. Quản lý ICT & Hạ tầng (IT Operations)

**Mô tả:** Quản lý hệ thống công nghệ thông tin, triển khai tính năng mới, bảo trì và an ninh mạng.

**Các bước chính:**
1. Đề xuất tính năng mới (Product Owner)
2. Phát triển (Dev Team)
3. Kiểm thử (QA/Tester)
4. Triển khai (DevOps/CI-CD)
5. Theo dõi sau deploy
6. Xử lý sự cố (Incident Management)
7. Bảo trì định kỳ + Patch security

**Tác nhân tham gia:**
- **Internal:** Dev Team, QA, DevOps, Security, Product Owner
- **External:** Không có external actors chính

**Khách hàng quy trình:** Internal Staff (nhân viên nội bộ sử dụng hệ thống)

**Kết quả có thể:**
- ✅ Deploy tính năng mới thành công
- ✅ Bug fix hoàn tất
- ❌ Rollback (phát hiện lỗi nghiêm trọng sau deploy)

---

## Mối quan hệ giữa các quy trình

Các quy trình trong hệ thống quy trình nghiệp vụ của Lazada liên kết chặt chẽ:

1. **Quản lý Nhà bán hàng (P1)** → thẩm định đầu vào, cấp quyền cho Seller tham gia **Xử lý Đơn hàng (P4)** và **Marketing (P9)**.
2. **Xử lý Đơn hàng (P4)** → kích hoạt **Thanh toán & Đối soát (P5)** (Escrow) và **Vận chuyển (P7)** (tạo vận đơn).
3. Trường hợp giao hàng hỏng/trễ trong **Vận chuyển (P7)** → kích hoạt **Hoàn trả & Hoàn tiền (P6)** hoặc **CSKH (P8)**.
4. Nếu phát sinh xung đột không thể thỏa thuận ở **Hoàn trả (P6)** → chuyển sang **Quản lý Tranh chấp (P2)** để hòa giải.
5. **Marketing (P9)** kích hoạt spike đơn hàng → tải lên **ICT (P10)** cần đảm bảo uptime.

---

> **Lưu ý:** 10 quy trình trọng tâm được mô hình hóa chi tiết bằng BPMN 2.0 nằm trong thư mục `processes/` (AS-IS) và `processes-to-be/` (TO-BE). Xem `docs/analysis/` để biết phân tích VA/BVA/NVA, Fishbone, Pareto và 5-Why cho từng quy trình.

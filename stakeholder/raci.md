# Ma trận RACI — Phân công Trách nhiệm theo Quy trình (Lazada Việt Nam)

> **Mục đích:** Xác định rõ vai trò của từng bên liên quan trong các hoạt động chính của 10 quy trình nghiệp vụ. RACI giúp tránh chồng chéo, thiếu sót và đảm bảo mọi hoạt động đều có người chịu trách nhiệm.
> **Đồ án:** Hệ thống Quản trị Quy trình Nghiệp vụ (BPM) Lazada Việt Nam (IE203)
> **Ngày lập:** 2026-09-03

**Chú thích:**
- **R (Responsible):** Người thực hiện công việc (có thể nhiều người)
- **A (Accountable):** Người chịu trách nhiệm cuối cùng, phê duyệt (chỉ 1 người/hoạt động)
- **C (Consulted):** Người được tư vấn trước khi quyết định (2 chiều)
- **I (Informed):** Người được thông báo sau khi quyết định (1 chiều)
- **System (Auto):** Hệ thống tự động thực hiện (là R ở các bước tự động hóa — mục tiêu của BPM)

---

## 1. Quy trình Quản lý Nhà bán hàng (Seller Management)

| Hoạt động | Seller | Seller Ops | System (Auto) | Category Mgr | Risk/Fraud | Legal | Finance | CEO/MD | Marketing |
|-----------|--------|------------|---------------|--------------|------------|-------|---------|--------|-----------|
| Đăng ký tài khoản seller | **R** | **A** | - | - | - | C | - | - | - |
| Xác minh giấy phép kinh doanh | - | **R/A** | - | - | C | C | - | I | - |
| Duyệt sản phẩm listing đầu tiên | I | **A** | - | **R** | C | - | - | - | - |
| Setup gian hàng (banner, description) | **R** | **A** | - | - | - | - | - | - | C |
| Giới thiệu công cụ bán hàng | I | **R/A** | - | - | - | - | - | - | C |
| Theo dõi performance metrics (DSR, cancellation, late shipment) | I | **A** | **R** | - | - | - | - | I | - |
| Cảnh báo seller vi phạm policy | I | **A** | **R** | - | - | C | - | - | - |
| Tạm ngừng gian hàng (suspend) | I | **R** | - | - | C | C | - | **A** | - |
| Khôi phục gian hàng | I | **R** | - | - | - | C | - | **A** | - |
| Cập nhật policy seller | I | C | - | - | - | **R** | - | **A** | C |
| Xử lý hàng giả / counterfeit | I | **A** | - | - | **R** | C | - | I | - |
| Payout tuần cho seller | I | C | **R** | - | - | - | **A** | - | - |

**Ghi chú:** Seller Ops là trung tâm quy trình; các quyết định suspend/khôi phục/phân chính sách do CEO/MD phê duyệt. Data Team tham vấn ở bước theo dõi metrics (C); CS & IT/Eng chỉ nhận thông báo (I) ở các bước liên quan.

> **Vai trò ngoài BPMN lane:** Category Mgr tham gia duyệt listing theo ngành hàng; vai trò này không tách lane riêng trong sơ đồ BPMN (gộp vào Seller Ops lane) nhưng có trách nhiệm R/A cụ thể theo phân công nội bộ.

---

## 2. Quy trình Giải quyết Tranh chấp (Dispute Resolution)

| Hoạt động | Buyer | Seller | System (Auto) | CS Team | Seller Ops | Risk/Fraud | Legal | Finance | Operations | CEO/MD |
|-----------|-------|--------|---------------|---------|------------|------------|-------|---------|------------|--------|
| Buyer mở dispute | **R** | I | - | **A** | - | - | - | - | - | - |
| System tự động ghi nhận & phân loại | I | I | **R** | **A** | I | - | - | - | - | - |
| Thông báo seller về dispute | I | I | **R** | **A** | - | - | - | - | - | - |
| Seller phản hồi & đề xuất giải pháp | I | **R** | - | **A** | - | - | - | - | - | - |
| Buyer chấp nhận / từ chối giải pháp | **R** | I | - | **A** | - | - | - | - | - | - |
| CS phân tích bằng chứng (ảnh, video) | I | I | - | **R/A** | - | C | - | - | - | - |
| Quyết định của platform (auto/manual) | I | I | I | **R** | - | - | C | I | - | **A** |
| Áp dụng hình phạt seller (nếu có) | - | I | - | - | **R** | C | C | - | - | **A** |
| Hoàn tiền cho buyer | I | I | **R** | C | - | - | - | **A** | - | - |
| Trao đổi vận chuyển (nếu có return) | I | I | - | C | - | - | - | - | **R/A** | - |
| Cập nhật seller performance score | I | I | **R** | - | C | - | - | - | - | **A** |
| Escalation lên cấp cao hơn | I | I | - | **R** | - | - | C | - | C | **A** |

**Ghi chú:** CS Team xử lý phần lớn cases; Escalation chỉ cho 10-15% cases phức tạp (leo lên CEO/MD). Data Team là A ở bước cập nhật performance score và C ở bước phân loại tự động. LEX/3PL nằm trong phạm vi Operations ở bước trao đổi vận chuyển.

---

## 3. Quy trình Xử lý Đơn hàng Online (Order Processing)

| Hoạt động | Buyer | Seller | System (Auto) | Product Mgr | Seller Ops | Engineering | LEX/3PL | Operations | Finance | Payment GW |
|-----------|-------|--------|---------------|-------------|------------|-------------|---------|------------|---------|-------------|
| Đặt hàng (checkout) | **R** | I | - | **A** | - | C | - | - | - | - |
| Kiểm tra tồn kho | I | I | **R** | - | C | **A** | - | - | - | - |
| Xác nhận thanh toán (COD/Card/E-wallet) | I | I | **R** | - | - | - | - | **A** | I | C |
| Thông báo đơn hàng cho seller | I | I | **R** | - | C | **A** | - | - | - | - |
| Seller xác nhận đơn hàng | I | **R** | - | - | **A** | - | I | - | - | - |
| Seller đóng gói sản phẩm | I | **R** | - | - | **A** | - | I | - | - | - |
| Nhận hàng tại kho / FBL auto-pick | I | I | - | - | C | - | **R** | **A** | - | - |
| Sắp xếp tại kho sorting hub | - | - | **R** | - | - | C | - | **A** | - | - |
| Vận chuyển last-mile | I | I | - | - | - | - | **R** | **A** | - | - |
| Buyer nhận hàng & xác nhận | **R** | I | - | **A** | - | - | - | - | I | - |
| Giải phóng escrow (release payment) | I | I | **R** | - | - | - | - | C | **A** | - |
| Đánh giá sản phẩm (optional) | **R** | I | - | **A** | - | - | - | - | - | - |
| Quyết định vận chuyển lỗi (failed delivery) | I | I | I | - | - | - | - | **R/A** | I | - |

**Ghi chú:** System đóng vai trò điều phối tự động; Engineering chịu trách nhiệm kỹ thuật các bước tự động; Payment Gateway chỉ tham gia ở bước xác nhận thanh toán (C); CS Team được tư vấn ở bước nhận hàng và quyết định vận chuyển lỗi (C).

---

## 4. Quy trình Hoàn trả & Refund (Return & Refund)

| Hoạt động | Buyer | Seller | System (Auto) | CS Team | Operations | Seller Ops | Finance | Data Team |
|-----------|-------|--------|---------------|---------|------------|------------|---------|-----------|
| Buyer yêu cầu return (7-30 ngày) | **R** | I | - | **A** | - | - | - | - |
| System kiểm tra eligibility | I | I | **R** | **A** | - | - | - | - |
| Seller chấp nhận / từ chối return | I | **R** | - | **A** | - | - | - | - |
| CS phân tích & quyết định | I | I | - | **R/A** | - | - | - | - |
| Tạo lệnh trả hàng (return label) | I | I | **R** | - | **A** | - | - | - |
| Buyer gửi trả hàng | **R** | I | - | - | **A** | - | - | - |
| Seller/Kho nhận & kiểm tra hàng trả | I | **R** | - | - | **A** | - | I | - |
| Xác nhận hàng trả hợp lệ | I | I | - | C | **R/A** | - | I | - |
| Xử lý hoàn tiền (refund) | I | I | **R** | C | - | - | **A** | - |
| Cập nhật tồn kho (nếu hàng đạt điều kiện) | - | I | **R** | - | C | **A** | - | - |
| Áp dụng phí return (nếu buyer lỗi) | I | - | - | C | - | - | **R/A** | - |
| Cập nhật seller performance metrics | I | I | **R** | - | - | C | - | **A** |

**Ghi chú:** Return giá trị thấp (< 200k VND) được auto-approve, không cần kiểm tra tại kho. Risk/Fraud tham vấn (C) ở bước CS phân tích quyết định; Legal tham vấn (C) ở bước kiểm tra eligibility; QC tham vấn ở bước kiểm tra hàng trả.

---

## 5. Quy trình Chăm sóc Khách hàng (Customer Service)

| Hoạt động | Buyer | System (Auto) | CS Team | Product Mgr | Legal | Risk/Fraud | Seller Ops | Data Team | CEO/MD |
|-----------|-------|---------------|---------|-------------|-------|------------|------------|-----------|--------|
| Buyer liên hệ CS (hotline/chat/email) | **R** | - | **A** | - | - | - | - | - | - |
| Phân loại & ưu tiên tuyến đường | - | **R** | **A** | C | - | - | - | - | - |
| Trả lời vấn đề đơn giản (FAQ) | I | - | **R/A** | - | - | - | - | - | - |
| Chuyển lên đơn phức tạp | I | - | **R/A** | - | C | C | - | - | - |
| Làm việc với seller để giải quyết | I | - | **R/A** | - | - | - | C | - | - |
| Escalation lên management | I | - | **R** | - | C | - | - | - | **A** |
- Product Mgr tham gia thiết kế luồng chat/chatbot (C/R/R&A ở bước phân loại & trả lời); vai trò này không tách lane riêng trong BPMN (gộp vào System/lane CS) nhưng có trách nhiệm theo phân công nội bộ.
| Ghi nhận feedback & feedback loop | I | - | **R** | **A** | - | - | - | C | I |
| Đánh giá CSAT/NPS sau hỗ trợ | - | **R** | **A** | - | - | - | - | C | I |
| Cập nhật knowledge base | - | - | **R/A** | C | - | - | - | - | - |
| Báo cáo hàng ngày về CS metrics | - | - | **A** | - | - | - | - | **R** | I |

**Ghi chú:** CS Team là tuyến đầu xử lý; System tự động hóa phân loại và khảo sát CSAT; Operations tham vấn (C) ở bước escalation; Marketing và Seller nhận thông báo (I) ở các bước feedback/báo cáo.

---

## 6. Quy trình Marketing & Khuyến mãi (Marketing & Promotions)

| Hoạt động | Marketing | Data Team | Finance | CEO/MD | Product Mgr | Engineering | Seller Ops | Seller | PR/Media | Legal |
|-----------|-----------|-----------|---------|--------|-------------|-------------|------------|--------|----------|-------|
| Lên kế hoạch chiến dịch (9.9, 11.11, 12.12) | **R/A** | C | C | I | - | - | - | - | - | - |
| Phân tích market trends & competitor | C | **R** | - | I | C | - | - | - | - | **A** |
| Thiết kế voucher / chương trình khuyến mãi | **R/A** | - | C | - | - | - | C | I | - | - |
| Duyệt budget chiến dịch | C | - | **R** | **A** | - | - | - | - | - | - |
| Tạo landing page & creative assets | **R/A** | - | - | - | C | C | - | - | - | - |
| Chạy quảng cáo PPC (Lazada Ads) | **R/A** | C | - | - | - | - | - | I | - | - |
| Hợp tác với influencer / KOL | **R/A** | - | - | I | - | - | - | - | C | - |
| Giới thiệu chiến dịch cho seller | **A** | - | - | - | - | - | **R** | I | - | - |
| Theo dõi performance chiến dịch | **A** | **R** | I | I | - | - | - | - | - | - |
| Tổng kết campaign (post-campaign review) | **R/A** | C | C | I | - | - | - | - | - | - |
| Quản lý affiliate program | **R/A** | - | C | - | - | - | - | I | - | - |
| PR / Media relations | **A** | - | - | I | - | - | - | - | **R** | C |

**Ghi chú:** Marketing lead toàn bộ quy trình; CEO/MD chỉ phê duyệt ngân sách chiến dịch lớn; Finance tham vấn ở các bước liên quan budget; Affiliate nhận thông báo (I) ở bước quản lý affiliate program.

> **Vai trò ngoài BPMN lane:** Product Mgr & Engineering tham vấn (C) ở bước tạo landing page/creative; họ không tách lane riêng trong BPMN (gộp vào Marketing/System lane) nhưng có trách nhiệm theo phân công nội bộ.

---

## 7. Quy trình Quản lý Nhân sự & Đào tạo (HR & Training)

| Hoạt động | HR Team | Giám đốc HR | System (Auto) | Finance | L&D/Content | Seller/NV | Compliance |
|-----------|---------|-------------|---------------|---------|-------------|-----------|------------|
| Lập kế hoạch đào tạo theo quý | **R** | **A** | - | C | C | - | C |
| Phê duyệt kế hoạch đào tạo | C | **R/A** | - | C | - | - | - |
| Duyệt ngân sách đào tạo | C | C | - | **R/A** | - | - | - |
| AI phân tích khoảng cách kỹ năng (skill gap) | C | I | **R** | - | **A** | I | - |
| Xây dựng nội dung khóa học | - | - | C | - | **R/A** | - | C |
| Chuyên gia nội dung đánh giá & phê duyệt khóa học | I | - | C | - | **R/A** | - | - |
| Publish khóa học lên Lazada University (LMS) | C | - | **R** | - | **A** | I | - |
| Đăng ký & hoàn thành module học tập | I | - | C | - | C | **R/A** | - |
| Thi đánh giá kiến thức | I | - | **R** | - | **A** | **R** | - |
| Cấp & cập nhật chứng chỉ đào tạo | **R** | - | **R** | - | **A** | I | I |
| Kiểm tra tuân thủ chính sách đào tạo định kỳ | C | I | **R** | - | - | I | **A** |
| Xử lý vi phạm (cảnh cáo / đình chỉ truy cập) | **R** | C | **R** | - | - | I | **A** |
| Đánh giá hiệu quả đào tạo (ROI) | C | I | **R** | C | - | - | **A** |

**Ghi chú:** Giám đốc HR là A về chiến lược đào tạo; Phòng Tài chính là R/A duy nhất ở bước duyệt ngân sách (bottleneck 5-10 ngày — mục tiêu TO-BE là auto-approval threshold). Compliance chịu trách nhiệm giám sát tuân thủ và xử lý vi phạm theo chính sách.

---

## 8. Quy trình Thanh toán & Đối soát (Payment & Settlement)

| Hoạt động | Buyer | Seller | System (Auto) | Payment GW | Finance | Risk/Fraud | Operations | Legal |
|-----------|-------|--------|---------------|------------|---------|------------|------------|-------|
| Chọn phương thức thanh toán (COD/Online/Wallet) | **R** | I | - | - | **A** | - | - | - |
| Xác thực thanh toán (OTP/3D Secure/Biometric) | **R** | - | **R** | **A** | - | C | - | - |
| Xử lý giao dịch qua Payment Gateway | I | - | **R** | **A** | - | - | - | - |
| Giữ tiền vào Escrow & kiểm tra gian lận AI | I | I | **R** | - | **A** | C | - | - |
| Đối soát đơn với giao dịch thanh toán | I | I | **R** | - | **A** | - | - | - |
| Tính phí hoa hồng & phí platform | I | I | **R** | - | **A** | - | - | - |
| Giải phóng tiền từ Escrow cho Seller | I | I | **R** | - | **A** | - | - | - |
| Xử lý COD thu hộ & đối soát COD | I | I | **R** | - | **A** | C | C | - |
| Xử lý chênh lệch COD (discrepancy) | - | I | C | - | **R/A** | C | I | - |
| Phê duyệt giải ngân đặc biệt | - | I | C | - | **R/A** | C | - | - |
| Phát hành hóa đơn điện tử | I | I | **R** | - | **A** | - | - | C |
| Xử lý lệnh rút tiền & chuyển khoản ngân hàng | - | **R** | **R** | - | **A** | - | - | - |

**Ghi chú:** Finance là A ở mọi bước liên quan tiền (escrow, hoa hồng, giải ngân, đối soát, rút tiền) — kiểm soát dòng tiền tập trung. System (Auto) thực hiện phần lớn thao tác; Payment Gateway chỉ là A ở bước xác thực/xử lý giao dịch; Risk/Fraud tư vấn (C) ở bước kiểm tra gian lận và xử lý chênh lệch.

---

## 9. Quy trình Logistics & Giao nhận (Logistics & Delivery)

| Hoạt động | Seller | System (Auto) | LEX/3PL | Shipper | Buyer | Operations | CS Team | Finance |
|-----------|--------|---------------|---------|---------|-------|------------|---------|---------|
| Seller đóng gói & bàn giao hàng | **R** | - | - | - | - | **A** | - | - |
| Tạo vận đơn AWB & phân bổ đơn vị vận chuyển | I | **R** | - | - | - | **A** | - | - |
| LEX/3PL lấy hàng tại kho Seller | I | C | **R** | - | - | **A** | - | - |
| Quét barcode & sắp xếp tại Hub | - | **R** | **R** | - | - | **A** | - | - |
| Vận chuyển trung chuyển (line-haul) | I | C | **R** | - | I | **A** | - | - |
| Xuất kho giao hàng & tối ưu tuyến đường | - | **R** | **R** | - | - | **A** | - | - |
| Shipper liên hệ Buyer trước khi giao | - | C | **A** | **R** | I | - | - | - |
| Giao hàng lần đầu & thu COD | I | C | - | **R** | **R** | **A** | - | - |
| Buyer nhận hàng & ký nhận (POD) | I | **R** | - | **R** | **R/A** | - | - | - |
| Giao lại (retry ≤3 lần) | I | C | - | **R** | I | **A** | - | - |
| Hàng hoàn về kho trung chuyển / Seller | I | **R** | **R** | - | I | **A** | - | - |
| Xử lý tranh chấp vận chuyển | I | C | C | I | **R** | - | **R/A** | - |
| Phân tích hiệu suất logistics (BI) | - | **R** | I | - | - | C | - | **A** |

**Ghi chú:** Operations là A xuyên suốt quy trình logistics; LEX/3PL là R chính ở các hoạt động vận chuyển; Shipper là R ở giao hàng trực tiếp (bao gồm retry); System tự động hóa AWB, phân bổ, tracking và BI. CS Team là R/A khi xử lý tranh chấp vận chuyển; Finance là A cho đối soát chi phí logistics.

---

## 10. Quy trình Vận hành Nền tảng Công nghệ (IT Operations)

| Hoạt động | Product Owner | Dev Team | QA/Tester | DevOps/CI-CD | Security | System (Auto) | Marketing | CEO/MD |
|-----------|---------------|----------|-----------|--------------|----------|---------------|-----------|--------|
| Đề xuất & phân tích ưu tiên User Story | **R/A** | C | - | - | - | - | I | I |
| Thiết kế kỹ thuật (Technical Design) | - | **R** | C | **A** | C | - | - | - |
| Viết code & Unit Test | - | **R** | - | **A** | - | - | - | - |
| Code Review | - | **R/A** | I | - | C | - | - | - |
| Kiểm thử Hệ thống/Tích hợp (ST/IT) | I | C | **R/A** | - | - | **R** | - | - |
| Vòng lặp sửa lỗi (Bug Fix Loop) | C | **R** | **A** | - | - | - | - | - |
| Quét lỗ hổng bảo mật (Security Scan) | - | C | - | - | **R/A** | **R** | - | - |
| Kiểm thử Hiệu năng (Performance Test) | - | C | **R** | C | - | **A** | - | - |
| Demo & phê duyệt Release | **R/A** | C | C | - | - | - | I | - |
| Triển khai (Pre-staging → Staging → Production) | I | C | C | **R/A** | C | **R** | I | I |
| Giám sát Production & Health Check | - | C | - | **R** | C | **A** | - | - |
| Rollback khi triển khai lỗi | I | C | - | **R** | - | **A** | - | - |

**Ghi chú:** DevOps/CI-CD là R/A cho toàn bộ pipeline triển khai và giám sát; QA là A cho chất lượng kiểm thử; Security là R/A riêng cho bước quét lỗ hổng (gate bắt buộc trước release); Product Owner là A duy nhất ở bước ưu tiên backlog và phê duyệt demo; System (Auto) tự động hóa CI/CD, scanning và health check.

---

## Tổng kết & Nguyên tắc

### Số lượng R/A/C/I theo vai trò (ước lượng)

| Vai trò | R (Thực hiện) | A (Phê duyệt) | C (Tư vấn) | I (Thông báo) |
|---------|---------------|---------------|------------|----------------|
| Buyer | 13 | 1 | 0 | 43 |
| Seller | 9 | 0 | 0 | 60 |
| System (Auto) | 44 | 3 | 11 | 2 |
| Seller Ops | 6 | 11 | 9 | 1 |
| CS Team | 11 | 19 | 5 | 0 |
| Marketing | 7 | 10 | 5 | 3 |
| Finance | 5 | 17 | 7 | 7 |
| Operations | 3 | 19 | 5 | 1 |
| Legal | 1 | 1 | 13 | 0 |
| CEO/MD | 0 | 9 | 0 | 14 |
| Risk/Fraud | 1 | 0 | 11 | 0 |
| HR Team | 3 | 0 | 6 | 3 |
| Giám đốc HR | 1 | 2 | 2 | 3 |
| L&D/Content | 2 | 6 | 2 | 0 |
| Compliance | 0 | 3 | 2 | 1 |
| LEX/3PL | 7 | 1 | 1 | 3 |
| Shipper | 4 | 0 | 0 | 1 |
| Product Owner | 2 | 2 | 1 | 3 |
| Dev Team | 4 | 1 | 8 | 0 |
| QA/Tester | 2 | 2 | 3 | 1 |
| DevOps/CI-CD | 3 | 3 | 1 | 0 |
| Security | 1 | 1 | 4 | 0 |
| Category Mgr | 1 | 0 | 0 | 0 |
| Data Team | 3 | 1 | 5 | 0 |
| Engineering | 0 | 2 | 3 | 0 |
| Payment GW | 0 | 2 | 1 | 0 |
| Product Mgr | 0 | 4 | 4 | 0 |
| PR/Media | 1 | 0 | 1 | 0 |
| Seller/NV | 2 | 1 | 0 | 5 |

### Nguyên tắc áp dụng

1. **Chỉ 1 A cho mỗi hoạt động** — tránh mơ hồ về trách nhiệm cuối cùng.
2. **System (Auto) là R chính** — tự động hóa là mục tiêu của BPM, System thực hiện phần lớn công việc điều phối (kiểm tra tồn kho, phân loại dispute, refund, payout, theo dõi metrics, AWB/sorting, CI/CD pipeline).
3. **Buyer/Seller là R ở đầu quy trình** — họ khởi tạo yêu cầu (mở dispute, đặt hàng, yêu cầu return, học tập, đăng ký tham gia khóa học), nhưng I ở hầu hết các bước xử lý.
4. **Legal & Risk/Fraud là C** — tư vấn trước khi quyết định, không thực hiện trực tiếp (trừ Legal là R khi cập nhật policy seller, Risk/Fraud là R khi xử lý hàng giả).
5. **CEO/MD là A ở các quyết định chiến lược** — suspend/khôi phục gian hàng, quyết định tranh chấp lớn, duyệt budget, escalation — nhưng không tham gia vận hành.
6. **CS Team là R/A ở quy trình tranh chấp & CSKH** — tuyến đầu xử lý; escalation leo lên CEO/MD khi cần.
7. **Finance là A ở các bước tiền** — hoàn tiền, payout, escrow, phí return, duyệt ngân sách đào tạo, đối soát chi phí logistics — đảm bảo kiểm soát dòng tiền.
8. **Role chuyên môn hóa ở quy trình hỗ trợ** — Giám đốc HR là A cho chiến lược đào tạo, L&D/Content là R/A cho nội dung khóa học, Compliance là A cho giám sát tuân thủ, DevOps/CI-CD là R/A cho pipeline triển khai, QA là A cho chất lượng kiểm thử, Security là R/A riêng cho gate bảo mật.

---

> **Tài liệu liên quan:** [Ma trận Stakeholder](./matrix.md) (đánh giá Interest/Power) và [Phân công công việc](../appendix/task-assignment.md).

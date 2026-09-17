# Ma trận Phân tích Stakeholder - Dự án BPM Lazada Việt Nam

> **Đồ án:** Hệ thống Quản trị Quy trình Nghiệp vụ (BPM) Lazada Việt Nam (IE203)
> **Ngày lập:** 2026-09-03
> **Nguồn dữ liệu:** Phân tích stakeholders từ 10 quy trình khảo sát (interviews + workshop minutes + research docs); đối chiếu với [Ma trận RACI](./raci.md) và [Phân công công việc](../appendix/task-assignment.md).

---

## Bảng Phân tích Stakeholder

| # | Stakeholder | Vai trò | Mức độ Quan tâm (Interest) | Quyền lực (Power) | Chiến lược Thu hút |
|---|-------------|---------|---------------------------|-------------------|---------------------|
| 1 | **Buyer (Người mua)** | Người sử dụng cuối cùng mua hàng trên sàn; nguồn doanh thu chính (~50M+ active buyers SEA) | Cao | Cao | Quản lý chặt chẽ. Thông báo real-time qua in-app notification, email. Thu thập phản hồi qua CSAT/NPS sau mỗi tương tác. Đảm bảo trải nghiệm mua hàng mượt mà, giao nhanh, refund nhanh. |
| 2 | **Seller (Cá nhân/SME)** | Người cung cấp hàng hóa, tạo đơn hàng, xử lý khiếu nại; nguồn hàng của marketplace | Cao | Trung bình | Quản lý chặt chẽ. Cung cấp Seller Center portal, dashboard KPI, đào tạo quy trình BPM mới. Chính sách công bằng, payout định kỳ, chương trình hỗ trợ seller. |
| 3 | **Brand Seller (LazMall)** | Thương hiệu chính hãng, tạo uy tín cho platform (32,000+ brands SEA) | Cao | Cao | Quan hệ đối tác cao cấp. Dedicated account manager, bảo vệ thương hiệu qua IPP, chống hàng giả. Tham gia thiết kế workflow liên quan LazMall. |
| 4 | **Lazada System (Hệ thống kỹ thuật)** | Nền tảng công nghệ vận hành toàn bộ quy trình (mobile app, platform, API, AI/ML) | Cao | Cao | Nhóm kỹ thuật cốt lõi. Tham gia thiết kế kiến trúc, review kỹ thuật hàng tuần. Đảm bảo tích hợp API ổn định, tự động hóa các bước hệ thống. |
| 5 | **LEX (Logistics Express - Vận chuyển nội bộ)** | Đơn vị vận chuyển last-mile nội bộ của Lazada; xử lý giao hàng, hoàn hàng | Cao | Trung bình | Tích hợp API tracking. Họp đối tác định kỳ. SLA rõ ràng về thời gian giao hàng và xử lý hoàn hàng. Phối hợp với warehouse/fulfillment. |
| 6 | **3PL Đối tác (GHN, GHTK, Viettel Post, J&T)** | Đơn vị vận chuyển bên ngoài bổ sung năng lực giao nhận | Trung bình | Thấp | Giữ thông tin. Tích hợp API, dashboard SLA. Đánh giá hiệu suất định kỳ, đa dạng hóa đối tác để giảm rủi ro. |
| 7 | **CS Team (Chăm sóc khách hàng)** | Xử lý ticket, dispute, refund, hotline; tuyến đầu tương tác khách hàng | Cao | Trung bình | Quản lý chặt chẽ. Đào tạo chi tiết quy trình mới, cung cấp playbook/script, giám sát chất lượng qua QA định kỳ. Tham gia thiết kế workflow escalation. |
| 8 | **Marketing Team** | Quản lý chiến dịch (9.9, 11.11, 12.12), voucher, khuyến mãi, PR | Cao | Trung bình | Giữ hài lòng. Phối hợp khi tích hợp workflow khuyến mãi vào BPM. Thông báo trước khi thay đổi ảnh hưởng chiến dịch. Cung cấp số liệu campaign. |
| 9 | **Compliance (Tuân thủ)** | Đảm bảo quy trình tuân thủ Nghị định 52/2013, 85/2021, Luật An ninh mạng | Trung bình | Cao | Giữ hài lòng. Tham vấn ngay từ giai đoạn thiết kế. Review tất cả workflow trước khi triển khai. Báo cáo tuân thủ định kỳ. |
| 10 | **Legal (Pháp chế)** | Tư vấn pháp lý về hợp đồng, tranh chấp, bảo vệ dữ liệu, chính sách seller | Trung bình | Cao | Giữ hài lòng. Tham vấn khi có thay đổi chính sách lớn. Review điều khoản dịch vụ, policy seller. Đảm bảo tuân thủ pháp luật e-commerce. |
| 11 | **Escalation Team (Đội xử lý leo thang)** | Giải quyết khiếu nại phức tạp vượt cấp, phối hợp với CS và CEO/MD | Cao | Trung bình | Thiết kế workflow escalation rõ ràng. Đào tạo chuyên sâu. Cung cấp quyền quyết định trong giới hạn. Họp review case phức tạp hàng tuần. |
| 12 | **Payment Gateway (VNPay, MoMo)** | Xử lý giao dịch thanh toán (QR, e-wallet, Internet Banking), hoàn tiền | Cao | Trung bình | Giữ hài lòng. Tích hợp chặt chẽ qua API, giám sát tỷ lệ thành công giao dịch, đối soát tự động. Đa GW dự phòng để đảm bảo uptime. |
| 13 | **Banks (Ngân hàng liên kết)** | Xử lý thanh toán COD, payout vào tài khoản seller | Trung bình | Trung bình | Giữ hài lòng. Phối hợp đối soát, đảm bảo payout đúng hạn. |
| 14 | **Cục Thương mại điện tử & Kinh tế số (Cục TMĐT&KTĐS)** | Thanh tra, giám sát, xử phạt vi phạm TMĐT; thuộc Bộ Công Thương | Trung bình | Cao | Giữ hài lòng. Chủ động tuân thủ Nghị định 52/2013, 85/2021. Hợp tác trong thanh tra, cung cấp báo cáo định kỳ qua Legal. |
| 15 | **Ngân hàng Nhà nước (NHNN)** | Cơ quan quản lý nhà nước về thanh toán, trung gian thanh toán | Trung bình | Cao | Giữ hài lòng. Đảm bảo tuân thủ quy định về thanh toán trung gian, phối hợp với Payment team và Finance. |
| 16 | **Management/Country CEO (Ban lãnh đạo)** | Quyết định chiến lược, phê duyệt ngân sách và phạm vi; P&L owner tại VN | Cao | Cao | Báo cáo executive hàng tháng. Dashboard KPI tổng quan. Trình bày ROI và tiến độ dự án định kỳ. Họp lãnh đạo hàng tuần. |
| 17 | **Risk/Fraud Team** | Ngăn chặn gian lận, bảo vệ IP, xác minh seller | Cao | Trung bình | Quản lý chặt chẽ. Tham gia thiết kế workflow xác minh seller, giám sát fraud rate, tích hợp AI/ML fraud detection. |
| 18 | **Finance** | Quản lý tài chính, payout seller, cash flow, đối soát | Trung bình | Cao | Giữ hài lòng. Phối hợp trong quy trình payout, đối soát thanh toán, duyệt ngân sách. |
| 19 | **Operations Manager (Phụ trách vận hành)** | Điều phối vận hành kho, hub, giao nhận; kết nối 10 quy trình vận hành | Cao | Cao | Quản lý chặt chẽ. Báo cáo vận hành hàng tuần, phối hợp triển khai BPM TO-BE, giám sát SLA fulfillment. |

---

## Lưới Quyền lực - Quan tâm (Power-Interest Grid)

```
                        QUAN TÂM (INTEREST)
              Thấp              Trung bình            Cao
         +------------------+------------------+------------------+
  CAO    |   KEEP           |                  |   MANAGE         |
  (P)    |   SATISFIED      |                  |   CLOSELY        |
  QUY    |                  |  - Compliance    |  - Buyer         |
  LỰC    |                  |  - Legal         |  - Brand LazMall  |
         |                  |  - Finance       |  - Lazada System  |
         |                  |  - Cục TMĐT&KTĐS |  - Country CEO    |
         |                  |  - NHNN          |  - Ops Manager    |
         +------------------+------------------+------------------+
  TRUNG  |   MONITOR        |   MONITOR        |   KEEP           |
  BÌNH   |   (MIN EFFORT)   |                  |   INFORMED       |
  (P)    |                  |  - Banks         |  - CS Team        |
         |                  |  - 3PL (GHN,     |  - Marketing      |
         |                  |    GHTK, J&T)    |  - Escalation     |
         |                  |                  |  - LEX            |
         |                  |                  |  - Seller (SME)   |
         |                  |                  |  - Payment GW     |
         |                  |                  |  - Risk/Fraud     |
         +------------------+------------------+------------------+
  THẤP   |   MONITOR        |   MONITOR        |   KEEP           |
  (P)    |   (MIN EFFORT)   |                  |   INFORMED       |
         |                  |                  |                  |
         +------------------+------------------+------------------+
```

> **Ghi chú:** Competitors, Media, General Public là các bên ngoài (external) cần theo dõi thị trường nhưng không nằm trong 19 stakeholders chính (không đánh giá I/P trong bảng) — do đó không xếp vào grid.

### Phân loại chi tiết theo ô:

**MANAGE CLOSELY (Quản lý chặt chẽ)** - Quyền lực CAO + Quan tâm CAO:
- Buyer, Brand Seller (LazMall), Lazada System, Country CEO, Operations Manager
- Đây là nhóm stakeholder quan trọng nhất, cần tham gia tích cực và liên tục.

**KEEP SATISFIED (Giữ hài lòng)** - Quyền lực CAO + Quan tâm TRUNG BÌNH:
- Compliance, Legal, Finance, Cục TMĐT&KTĐS, NHNN
- Cần đảm bảo họ được thông báo đầy đủ và hài lòng với tiến độ.

**KEEP INFORMED (Giữ thông tin)** - Quyền lực TRUNG BÌNH + Quan tâm CAO:
- CS Team, Marketing, Escalation Team, LEX, Seller (SME), Payment Gateway, Risk/Fraud Team
- Thường xuyên cập nhật tiến trình và thay đổi quy trình.

**MONITOR (Giám sát)** - Quyền lực TRUNG BÌNH/THẤP + Quan tâm TRUNG BÌNH:
- Banks, 3PL Partners (GHN, GHTK, Viettel Post, J&T)
- Các bên liên quan ít tác động trực tiếp nhưng cần theo dõi.

---

## Ma trận Mức độ Ảnh hưởng theo Giai đoạn Dự án

| Giai đoạn | Stakeholder Chính | Stakeholder Phụ |
|-----------|-------------------|-----------------|
| Khởi tạo (Initiation) | Country CEO, Compliance, Legal, Finance | Marketing, Cục TMĐT&KTĐS |
| Thiết kế (Design) | Lazada System, Seller, CS Team, Compliance | Buyer, Brand (LazMall), Payment Gateway |
| Phát triển (Development) | Lazada System, Payment Gateway, LEX, 3PL | CS Team, Escalation Team |
| Kiểm thử (Testing) | CS Team, Buyer, Seller, Escalation Team | Compliance, Risk/Fraud |
| Triển khai (Go-live) | Toàn bộ stakeholder | Country CEO, Legal, NHNN |
| Vận hành (Operations) | CS Team, LEX, Escalation Team, Seller, Buyer, Operations Manager | Compliance, Marketing, Risk/Fraud |

---

> **Tài liệu liên quan:** [Ma trận RACI](./raci.md) (phân công trách nhiệm theo 10 quy trình) và [Phân công công việc](../appendix/task-assignment.md).

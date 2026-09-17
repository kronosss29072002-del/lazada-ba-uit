# Annotation VA/BVA/NVA — Toàn bộ Task trong 10 BPMN AS-IS

> **Mục đích:** Map từng task cụ thể trong file `.bpmn` (AS-IS) sang phân loại VA / BVA / NVA kèm lý do và đề xuất TO-BE.
> **Nguồn:** `processes/0X-*.bpmn` (tên task lấy nguyên từ file mô hình)
> **Phân loại:**
> - **VA** (Value-Added) — trực tiếp tạo giá trị cho khách hàng / tạo doanh thu
> - **BVA** (Business Value-Added) — cần thiết để vận hành, tuân thủ, kiểm soát rủi ro nhưng không trực tiếp tạo giá trị
> - **NVA** (Non-Value-Added) — không tạo giá trị, waste; mục tiêu loại bỏ / tự động hóa / giảm thiểu

> **Ghi chú:** Tỷ lệ % làm tròn đến hàng đơn vị nên tổng từng dòng có thể lệch ±1%.

---

## Tổng quan

| Process | Tổng task | VA | BVA | NVA | Tỷ lệ VA/BVA/NVA |
|---------|-----------|----|-----|-----|------------------|
| 01 Seller Management | 14 | 4 (29%) | 10 (71%) | 0 | 29% / 71% / 0% |
| 02 Dispute Management | 12 | 6 (50%) | 6 (50%) | 0 | 50% / 50% / 0% |
| 03 Order Processing | 26 | 9 (35%) | 17 (65%) | 0 | 35% / 65% / 0% |
| 04 Return & Refund | 13 | 6 (46%) | 5 (39%) | 2 (15%) | 46% / 39% / 15% |
| 05 Customer Service | 18 | 10 (56%) | 8 (44%) | 0 | 56% / 44% / 0% |
| 06 Marketing | 21 | 12 (57%) | 7 (33%) | 2 (10%) | 57% / 33% / 10% |
| 07 HR & Training | 17 | 8 (47%) | 9 (53%) | 0 | 47% / 53% / 0% |
| 08 Payment & Settlement | 22 | 14 (64%) | 6 (27%) | 2 (9%) | 64% / 27% / 9% |
| 09 Logistics & Delivery | 20 | 9 (45%) | 6 (30%) | 5 (25%) | 45% / 30% / 25% |
| 10 IT Operations | 18 | 6 (33%) | 10 (56%) | 2 (11%) | 33% / 56% / 11% |
| **TỔNG** | **181** | **84 (46%)** | **84 (46%)** | **13 (7%)** | **46% / 46% / 7%** |

> **Ghi chú chung:** Ở mức task BPMN (nguyên tử), hầu hết task có chức năng tối thiểu nên ít task bị xếp NVA tuyệt đối. NVA nằm ở **thời gian chờ (Hold)** giữa các task, **các lớp duyệt thừa (Overdo)** và **công đoạn thủ công trùng lặp (Move)**. Đây chính là nguồn cải tiến TO-BE.

---

## 01. Quản lý Nhà bán hàng (Seller Management) — 14 tasks

| # | Task (trong BPMN) | Loại | VA | BVA | NVA | Lý do | Đề xuất TO-BE |
|---|-------------------|------|----|-----|-----|-------|---------------|
| 1 | Điền thông tin định danh Seller | User | ✓ | | | Tạo hồ sơ Seller — đầu vào giá trị | Giữ nguyên; guided form |
| 2 | Upload CMND/CCCD + GPKD + Giấy chứng nhận (LazMall) | User | ✓ | | | Bắt buộc để xác minh danh tính & LazMall badge | Smart Scan OCR tự động |
| 3 | Bổ sung / sửa hồ sơ | User | | ✓ | | Cần khi hồ sơ thiếu — kiểm soát chất lượng | Auto-check trước khi submit (giảm vòng sửa) |
| 4 | Cập nhật tài khoản ngân hàng (giải ngân) | User | | ✓ | | Bắt buộc cho giải ngân — tuân thủ tài chính | Xác thực IBAN tự động |
| 5 | Compliance review thủ công (24-48h) | User | | ✓ | | Cần cho legal compliance nhưng chậm — Hold lớn | **Semi-automate:** auto-approve low-risk 3s, review chỉ high-risk |
| 6 | Gửi cảnh cáo Seller | User | | ✓ | | Quản trị vi phạm — cần thiết duy trì chất lượng sàn | Template cảnh cáo chuẩn hóa |
| 7 | Tạm khóa gian hàng (7 ngày) | User | | ✓ | | Kiểm soát rủi ro khi vi phạm nghiêm trọng | Tự động hóa theo mức risk score |
| 8 | Khóa gian hàng vĩnh viễn | User | | ✓ | | Kiểm soát rủi ro tối đa — hiếm khi dùng | Giữ nguyên; SLA phản hồi khiếu nại |
| 9 | Gửi OTP xác thực SĐT | Service | | ✓ | | Xác minh chủ sở hữu — bảo mật | Giữ nguyên (auto) |
| 10 | Validate định danh tự động | Service | | ✓ | | Lọc hồ sơ sai — prevent fraud | Nâng cấp rule engine real-time |
| 11 | Quét OCR + kiểm tra giấy tờ giả | Service | | ✓ | | Chống gian lận giấy tờ — bảo vệ sàn | Nâng cấp eKYC sinh trắc học real-time |
| 12 | Chấm điểm rủi ro (Risk scoring) | Service | | ✓ | | Phân loại mức rủi ro — nền tảng auto-decision | Kết nối auto-approve path (Low-risk 3s) |
| 13 | Thông báo kết quả duyệt Seller Centre | Service | ✓ | | | Người dùng nhận kết quả — giao tiếp giá trị | Đa kênh (push + email) tức thì |
| 14 | Giám sát điểm đánh giá & vi phạm (auto) | Service | ✓ | | | Chủ động bảo vệ sàn — giảm tỷ lệ khóa tài khoản | Cảnh báo sớm trước khi vi phạm |

**Phân tích:** 4 VA (29%) / 10 BVA (71%) / 0 NVA. Hold-time lớn nhất là Compliance review 24-48h → TO-BE tự động duyệt low-risk 3 giây (giảm từ 24-48h xuống 3s).

---

## 02. Quản lý Tranh chấp (Dispute Management) — 12 tasks

| # | Task (trong BPMN) | Loại | VA | BVA | NVA | Lý do | Đề xuất TO-BE |
|---|-------------------|------|----|-----|-----|-------|---------------|
| 1 | Tạo tranh chấp + lý do | User | ✓ | | | Nhu cầu chính đáng của KH — mở quy trình | Guided form + checklist lý do |
| 2 | Bổ sung bằng chứng (nếu có) | User | ✓ | | | Bằng chứng giúp giải quyết đúng | Upload evidence có cấu trúc (ảnh/video theo danh mục) |
| 3 | Yêu cầu bổ sung bằng chứng | User | | ✓ | | Đảm bảo đủ thông tin — fairness | Auto-check nội dung trước khi gửi |
| 4 | Seller phản hồi (≤48h) | User | ✓ | | | Phản hồi từ bên liên quan — due process | Dynamic deadline 12h/48h theo độ phức tạp |
| 5 | CS thẩm định toàn bộ hồ sơ tranh chấp | User | ✓ | | | Phán xét — giá trị cốt lõi của quy trình | AI-assisted review (summary + gợi ý) |
| 6 | CS ban hành quyết định xử lý | User | ✓ | | | Kết quả giải quyết — giá trị cốt lõi | Decision template theo category |
| 7 | Chuyển lên nhóm chuyên trách (Lazada Escalation) | User | | ✓ | | Complex cases cần chuyên môn | Clear escalation criteria tự động gợi ý |
| 8 | Hội đồng thẩm định & ra quyết định cuối | User | | ✓ | | Phán quyết cuối cho case phức tạp | Decision framework + checklist |
| 9 | Tự động thu thập dữ liệu đơn hàng | Service | | ✓ | | Cung cấp context — hỗ trợ review | Fully automate (đã auto) |
| 10 | AI phân loại tranh chấp (Đơn giản/Phức tạp) | Service | | ✓ | | Routing đúng luồng — giảm tải CS | Nâng cấp accuracy, auto-assign straight |
| 11 | Kiểm tra lịch sử SLA | Service | | ✓ | | Kiểm soát tuân thủ cam kết | Tự động penalty/compensation |
| 12 | Gửi thông báo đối soát đến hai bên | Service | ✓ | | | Minh bạch thông tin — giảm khiếu nại kép | Auto update status theo sự kiện |

**Phân tích:** 6 VA (50%) / 6 BVA (50%) / 0 NVA. Waste chính nằm **giữa** các task: chờ CS assignment 4-24h (Hold) và nhiều vòng evidence (Overdo) → TO-BE auto-assign + giới hạn 2 vòng.

---

## 03. Xử lý Đơn hàng Online (Order Processing) — 26 tasks

| # | Task (trong BPMN) | Loại | VA | BVA | NVA | Lý do | Đề xuất TO-BE |
|---|-------------------|------|----|-----|-----|-------|---------------|
| 1 | Xem lại đơn hàng | Task | ✓ | | | KH xác nhận giỏ hàng — tránh nhầm lẫn | Giữ nguyên |
| 2 | Thanh toán đơn hàng (COD / Thẻ / Ví / Chuyển khoản) | User | ✓ | | | Giao dịch trực tiếp — tạo doanh thu | Giữ nguyên; one-tap checkout |
| 3 | Nhận hàng từ shipper | Task | ✓ | | | KH nhận hàng — hoàn tất giá trị | Giữ nguyên |
| 4 | Xác nhận đã nhận hàng | User | ✓ | | | Chốt giao dịch hoàn chỉnh | Auto-confirm sau 7 ngày |
| 5 | Buyer hủy đơn | User | ✓ | | | Quyền lợi KH trước khi giao | Giữ nguyên; auto-refund |
| 6 | Validate thông tin đơn | Service | | ✓ | | Kiểm tra hợp lệ — prevent errors | Nâng cấp rule real-time |
| 7 | Khóa tồn kho + tạo đơn | Service | | ✓ | | Chống bán quá — quản trị tồn kho | Auto reservation ngay khi đặt |
| 8 | Kiểm tra gian lận (AI) | Service | | ✓ | | Chống fraud — bảo vệ hệ thống | Nâng cấp model liên tục |
| 9 | Kiểm tra tồn kho | Service | | ✓ | | Đảm bảo khả năng giao — tránh hủy đơn | Real-time sync với warehouse |
| 10 | Tạo vận đơn tự động (LEX / 3PL) | Service | ✓ | | | Đầu vào thiết yếu cho vận chuyển | Tạo nhãn vận đơn QR số hóa |
| 11 | Cập nhật định vị đơn hàng realtime | Service | ✓ | | | KH theo dõi đơn — trải nghiệm giá trị | API auto-sync tracking |
| 12 | Đếm số lần giao lại | Service | | ✓ | | Kiểm soát tối đa 3 lần — vận hành | Kết nối auto-cancel khi đạt limit |
| 13 | Auto-confirm (7 ngày) | Service | | ✓ | | Chốt đơn khi KH im lặng | Giảm xuống dưới 24h (24-72h cho Shop uy tín) |
| 14 | Hủy đơn do Seller quá hạn 48h | Service | | ✓ | | Bảo vệ KH khi Seller không phản hồi | **Giảm còn 2h** kết hợp auto-accept |
| 15 | Giải ngân cho Seller | Service | | ✓ | | Thanh toán theo escrow — vận hành tài chính | Giữ nguyên (auto) |
| 16 | Auto-cancel đơn | Service | | ✓ | | Hủy tự động khi thất bại/permissions | Giữ nguyên |
| 17 | Thông báo hủy đơn | Service | ✓ | | | KH biết trạng thái — giao tiếp minh bạch | Smart notification (Push > SMS) |
| 18 | Tự động hoàn tiền cho Buyer | Service | ✓ | | | Hoàn tiền — giá trị trực tiếp cho KH | Instant refund |
| 19 | Seller xác nhận đơn | User | | ✓ | | Bước điều phối — KHÔNG tạo giá trị trực tiếp | **Auto-accept sau 2h** (giảm Hold 2-24h) |
| 20 | Seller đóng gói | User | | ✓ | | Chuẩn bị hàng — bước chuẩn bị vận chuyển | Quy chuẩn đóng gói + ảnh xác nhận |
| 21 | Bàn giao hàng cho 3PL / LEX | User | | ✓ | | Kích hoạt vận chuyển | API auto-sync (bỏ nhập tay tracking) |
| 22 | Giao hàng (attempt) | User | | ✓ | | Hoàn tất phân phối | Pre-delivery call + time slot |
| 23 | LEX (Lazada Express) lấy hàng & quét barcode tại kho | Task | | ✓ | | Vận hành logistics nội bộ | Tự động lên lịch lấy hàng với 3PL |
| 24 | Gateway verify thanh toán | Service | | ✓ | | Xác minh giao dịch — bảo mật | Giữ nguyên |
| 25 | Giữ tiền tạm thời (COD) | Service | | ✓ | | Escrow chống rủi ro | Giữ nguyên |
| 26 | Cổng thanh toán xử lý hoàn tiền | Service | | ✓ | | Xử lý hoàn tiền qua gateway | Giữ nguyên |

**Phân tích:** 9 VA (35%) / 17 BVA (65%) / 0 NVA. Waste chủ yếu là Hold-time giữa các task: Seller confirm 2-24h, LEX pickup 4-12h, giao lại +1-2 ngày. **Overdo:** nhiều lớp notification đồng thời → TO-BE smart routing.

---

## 04. Hoàn trả & Refund (Return & Refund) — 13 tasks

| # | Task (trong BPMN) | Loại | VA | BVA | NVA | Lý do | Đề xuất TO-BE |
|---|-------------------|------|----|-----|-----|-------|---------------|
| 1 | Gửi yêu cầu đổi trả và lý do | User | ✓ | | | Nhu cầu chính đáng của KH | Guided form + lý do chuẩn hóa |
| 2 | Tải lên bằng chứng ảnh và video | User | ✓ | | | Bằng chứng cần thiết cho quyết định | Checklist guided + AI quality check |
| 3 | Xử lý yêu cầu trễ hạn | User | | ✓ | | Xử lý ngoại lệ khi KH bỏ lỡ deadline | Auto-extend 1 lần, nhắc reminder |
| 4 | Bàn giao hàng trả cho LEX / 3PL | User | ✓ | | | Bắt đầu logistics ngược | Drop-off point + QR code |
| 5 | CS thẩm định hồ sơ khiếu nại | User | | ✓ | | Cần cho fair decision — Hold lớn | **AI triage evidence** + CS chỉ review ngoại lệ |
| 6 | Kiểm định hàng hoàn tại kho (≤12h) | User | | | **NVA** | Inspection thủ công tại kho — waste (bỏ qua khi return-less <200k) | **Return-less refund** low-risk + AI image analysis |
| 7 | Kiểm tra tính hợp lệ tự động | Service | | ✓ | | Lọc yêu cầu không hợp lệ — chống lạm dụng | Auto instant; mở rộng luật |
| 8 | AI phân loại bằng chứng khiếu nại | Service | | ✓ | | Phân loại nhanh — rút ngắn thời gian xử lý | Mở rộng auto-approve path |
| 9 | Gửi thông báo cập nhật tiến độ tự động | Service | ✓ | | | KH theo dõi trạng thái — minh bạch | Giữ nguyên (auto) |
| 10 | Đặt lịch hẹn Shipper đến lấy hàng hoàn | Service | ✓ | | | Lên lịch pickup — giảm Hold | Smart scheduling + drop-off point |
| 11 | Đặt lại lịch pickup | Service | | ✓ | | Xử lý ngoại lệ (KH bận) | Tự động đề xuất 3 slot kế tiếp |
| 12 | Kích hoạt lệnh hoàn tiền | Service | | | **NVA** | Hoàn tiền thủ công sau khi đã duyệt — waste (nhiều bước click) | Auto-execute refund qua payment gateway |
| 13 | LEX / 3PL pickup hàng trả | Task | ✓ | | | Vận chuyển hàng trả — logistics ngược | Scheduled pickup slot (giảm Hold 4-24h) |

**Phân tích:** 6 VA (46%) / 5 BVA (39%) / **2 NVA (15%)** — Inspect hàng hoàn tại kho (NVA khi return-less <200k) + kích hoạt hoàn tiền thủ công (NVA waste). Chờ kiểm định Return Center 3-7 ngày giữa các task là Hold nặng nhất → TO-BE tiered refund + SLA ≤12h + auto-notify + instant refund.

---

## 05. Chăm sóc Khách hàng (Customer Service) — 18 tasks

| # | Task (trong BPMN) | Loại | VA | BVA | NVA | Lý do | Đề xuất TO-BE |
|---|-------------------|------|----|-----|-----|-------|---------------|
| 1 | Mô tả chi tiết vấn đề cần hỗ trợ | User | ✓ | | | KH trình bày nhu cầu — đầu vào | Guided category menu |
| 2 | Cung cấp thêm thông tin chứng từ | User | ✓ | | | Đủ context để giải quyết | Auto-fill từ order/user context |
| 3 | Khách hàng bấm xác nhận hoàn tất hỗ trợ | User | ✓ | | | Verify hài lòng — chốt ticket | One-tap confirm |
| 4 | Khách hàng chấm điểm khảo sát CSAT | User | ✓ | | | Đo lường trải nghiệm — đầu vào cải tiến | 2-question CSAT/CES |
| 5 | Chờ phản hồi từ tư vấn viên | User | | ✓ | | Chờ agent (cần thiết nhưng Hold 5-30 phút) | **Predictive staffing** giảm queue |
| 6 | Xác minh danh tính khách hàng | User | | ✓ | | Bảo mật — chống mạo danh | SSO/OTP nhanh |
| 7 | Tư vấn viên Tier 1 tiếp nhận & hỗ trợ | User | ✓ | | | Core service — giải quyết trực tiếp | Copilot gợi ý + auto-context |
| 8 | Tư vấn viên Tier 1 đưa giải pháp xử lý | User | ✓ | | | Kết quả giải quyết trực tiếp | Solution KB integration |
| 9 | Chuyên viên Tier 2 thẩm định chuyên sâu | User | ✓ | | | Case phức tạp cần chuyên môn | Clear handoff summary |
| 10 | Chuyên viên Tier 2 xử lý dứt điểm | User | ✓ | | | Phán quyết chuyên sâu | Checklist + SLA |
| 11 | Khảo sát đánh giá chất lượng (QA Follow-up) | User | | ✓ | | Đo chất lượng — kiểm soát | Auto-survey thay call thủ công |
| 12 | AI NLP phân loại ý định & mức độ khẩn cấp | Service | | ✓ | | Routing đúng luồng — hỗ trợ chatbot | Nâng cấp NLP accuracy |
| 13 | Chatbot (Lazada Assistant) tự động giải đáp | Service | ✓ | | | Giải quyết tức thì — giá trị cốt lõi hiện đại | Mở rộng knowledge base (tăng 40-50% auto-resolve) |
| 14 | Hệ thống kiểm tra SLA xử lý ticket | Service | | ✓ | | Kiểm soát cam kết thời gian | Auto-escalate khi sắp quá hạn |
| 15 | Lấy lịch sử tương tác (auto) | Service | | ✓ | | Context cho agent — giảm lặp | Auto-attach (đã auto) |
| 16 | Hệ thống trích xuất thông tin đơn & tài khoản | Service | | ✓ | | Tự động lấy context → bỏ hỏi lại KH | Auto-context fetch (chống waste Move) |
| 17 | Ghi nhận nhật ký phiên & điểm CSAT | Service | | ✓ | | Ghi nhận phục vụ phân tích | Giữ nguyên (auto) |
| 18 | Gửi nhắc nhở phản hồi cho khách hàng | Service | ✓ | | | Nhắc KH theo dõi — giảm ticket kép | Auto-reminder, tránh spam |

**Phân tích:** 10 VA (56%) / 8 BVA (44%) / 0 NVA. Pain chính là Hold queue 5-30 phút (Tier 1) và waste Move (khách mô tả lại vấn đề, agent đọc transcript dài) → TO-BE auto-context + auto-summary + predictive staffing.

---

## 06. Marketing & Khuyến mãi (Marketing) — 21 tasks

| # | Task (trong BPMN) | Loại | VA | BVA | NVA | Lý do | Đề xuất TO-BE |
|---|-------------------|------|----|-----|-----|-------|---------------|
| 1 | Nghiên cứu thị trường & lập bản đề xuất | User | ✓ | | | Tạo insight — nền tảng campaign | Data-driven research + AI phân bổ ngân sách |
| 2 | Phân khúc lại nhóm đối tượng mục tiêu | User | ✓ | | | Chọn đúng đối tượng — tăng hiệu quả ngân sách | Auto-segment từ dữ liệu |
| 3 | Thiết kế concept & lập kế hoạch chi tiết | User | ✓ | | | Sáng tạo cốt lõi | A/B test concept |
| 4 | Theo dõi hiệu năng hệ thống & doanh số realtime | User | | ✓ | | Giám sát — kiểm soát mid-flight | Real-time ROAS dashboard |
| 5 | Lập báo cáo tổng kết & đánh giá ROI | User | | ✓ | | Đo lường hiệu quả — kiểm soát post-campaign | Template chuẩn hóa + ML insight |
| 6 | Kiểm tra tính tuân thủ pháp lý khuyến mãi (Nghị định 81) | User | | ✓ | | Tuân thủ pháp lý — tránh sai sót pháp lý | Auto-compliance check |
| 7 | Thẩm định ngân sách & tỷ suất ROI | User | | ✓ | | Kiểm soát chi tiêu — governance | Budget real-time dashboard |
| 8 | Giám đốc Khối phê duyệt ngân sách lớn | User | | ✓ | | Governance — kiểm soát ngân sách | Risk-tiering: duyệt 1 cấp cho budget nhỏ |
| 9 | Seller xem xét thư mời chiến dịch | User | ✓ | | | Seller tự xem — tăng coverage | Self-serve portal |
| 10 | Seller xác nhận tham gia trên Seller Centre | User | ✓ | | | Xác nhận cam kết seller | Auto-confirm + template |
| 11 | Seller chuẩn bị tồn kho & cài đặt giá sốc | User | ✓ | | | Chuẩn bị đầu vào bán hàng | Checklist + reminder |
| 12 | Buyer truy cập săn deal 12.12 Siêu Sale | User | ✓ | | | KH xem promotion — tiếp cận | Personalization engine |
| 13 | Buyer thanh toán áp mã FreeShip & Lazada Voucher | User | ✓ | | | Doanh thu — giá trị cuối cùng | One-tap checkout + voucher auto-apply |
| 14 | Hệ thống gửi lời mời tham gia đến Sellers | Service | ✓ | | | Tự động mời — thay manual outreach | Cá nhân hóa lời mời seller |
| 15 | Cấu hình chiến dịch trên hệ thống | Service | | | **NVA** | Config copy-paste thủ công — waste (lỗi ~9%) | Config campaign tự động từ template |
| 16 | Tự động phân tách & giải quyết xung đột mã | Service | ✓ | | | Chống chồng voucher — bảo vệ lợi nhuận | Auto-stack rules theo policy |
| 17 | Hệ thống kiểm tra & giả lập áp mã voucher | Service | | ✓ | | QA kỹ thuật — tránh lỗi tại launch | Auto-QA checklist |
| 18 | Kiểm toán QA toàn diện trước giờ G | Service | | ✓ | | Prevent errors | Automated QA suite |
| 19 | Kích hoạt Chiến dịch 12.12 Siêu Hội Mua Sắm | Service | ✓ | | | Thực thi campaign | Realtime launch monitor |
| 20 | Hệ thống tự động xuất báo cáo sơ bộ | Service | ✓ | | | Tự động báo cáo — thay báo cáo tay | Auto-report + ML insight |
| 21 | Thu thập bổ sung số liệu đối soát | Service | | | **NVA** | Thu thập data thủ công sau campaign — waste | Auto-extend từ data warehouse |

**Phân tích:** 12 VA (57%) / 7 BVA (33%) / **2 NVA (10%)** — Cấu hình campaign copy-paste thủ công (NVA waste, lỗi config ~9%) và thu thập số liệu đối soát thủ công (NVA waste) → TO-BE template library + auto-config + auto-extend data. Hold-time chính: budget approval multi-layer 2-5 ngày → TO-BE risk-tiering + digital workflow.

---

## 07. Quản lý Nhân sự & Đào tạo (HR & Training) — 17 tasks

| # | Task (trong BPMN) | Loại | VA | BVA | NVA | Lý do | Đề xuất TO-BE |
|---|-------------------|------|----|-----|-----|-------|---------------|
| 1 | Lập kế hoạch đào tạo theo quý | User | ✓ | | | Nền tảng định hướng toàn bộ hoạt động đào tạo | AI skill-gap analysis tự động |
| 2 | Giám đốc HR phê duyệt kế hoạch đào tạo | User | | ✓ | | Kiểm soát chiến lược & ngân sách — cần thiết | Phân quyền theo hạn mức ngân sách |
| 3 | Phòng Tài chính duyệt ngân sách đào tạo | User | | ✓ | | Kiểm soát tài chính bắt buộc — Hold 5-10 ngày | Auto-approval threshold + dashboard |
| 4 | Kiểm tra chứng chỉ hiện tại còn hiệu lực? | User | | ✓ | | Check điều kiện tiên quyết | Tự động check + nhắc hạn |
| 5 | Xây dựng nội dung khóa học (onboarding, nâng cao, compliance) | User | ✓ | | | Tạo giá trị cốt lõi cho người học — Hold 2-4 tuần | AI-generated content + template chuẩn |
| 6 | Chuyên gia nội dung đánh giá & phê duyệt khóa học | User | | ✓ | | Đảm bảo chất lượng nội dung | AI review + expert xác nhận cuối |
| 7 | Publish khóa học lên Lazada University | Service | ✓ | | | Đưa khóa học đến người học — hệ thống tự động | Giữ nguyên (auto) |
| 8 | Seller/Nhân viên đăng ký tham gia khóa học | User | ✓ | | | Người học chủ động tham gia | AI tự động gợi ý + đăng ký |
| 9 | Hoàn thành các module học tập trên hệ thống | User | ✓ | | | Học viên tiếp thu kiến thức — giá trị cốt lõi | Giữ nguyên |
| 10 | Thi đánh giá kiến thức sau khóa học | User | ✓ | | | Đánh giá năng lực thực tế — pass lần đầu 70% | Auto-proctoring + AI tạo đề |
| 11 | Cấp chứng chỉ hoàn thành khóa học | User | ✓ | | | Xác nhận kết quả đào tạo | Tự động hóa |
| 12 | Cập nhật chứng chỉ đào tạo cho nhân viên/Seller | User | | ✓ | | Quản lý hồ sơ bắt buộc | Tự động sync HRIS |
| 13 | Đánh giá hiệu quả đào tạo sau khóa học | User | ✓ | | | Đo lường ROI đào tạo | Dashboard real-time + AI phân tích |
| 14 | Kiểm tra tuân thủ chính sách đào tạo định kỳ | Service | | ✓ | | Tuân thủ bắt buộc — audit thủ công hàng tuần | Real-time compliance monitoring |
| 15 | Ghi nhận nhật ký vi phạm chính sách đào tạo | User | | ✓ | | Lưu trữ bằng chứng xử lý | Auto-log + cảnh báo |
| 16 | Áp dụng biện pháp xử lý cảnh cáo | User | | ✓ | | Xử lý vi phạm mức nhẹ — 2-3 ngày | Workflow tự động hóa |
| 17 | Đình chỉ quyền truy cập Seller vi phạm nghiêm trọng | User | | ✓ | | Xử lý vi phạm mức nặng — 3-7 ngày | Auto-lock + escalation policy |

**Phân tích:** 8 VA (47%) / 9 BVA (53%) / 0 NVA. **Hold-time lớn nhất:** Finance approval 5-10 ngày + content creation 2-4 tuần → TO-BE AI content + auto-approval threshold (giảm 65% approval time, cycle 54 → 15-20 ngày).

---

## 08. Thanh toán & Đối soát (Payment & Settlement) — 22 tasks

| # | Task (trong BPMN) | Loại | VA | BVA | NVA | Lý do | Đề xuất TO-BE |
|---|-------------------|------|----|-----|-----|-------|---------------|
| 1 | Chọn phương thức thanh toán (COD/Online/Ví) | User | ✓ | | | Buyer quyết định cách trả — core choice | Gợi ý phương thức ưu đãi |
| 2 | Thanh toán COD khi nhận hàng | User | ✓ | | | COD = ~40-45% giao dịch — thu hộ critical flow | Digital POD + xác thực cash |
| 3 | Xác nhận thanh toán online qua cổng | User | | ✓ | | Xác thực bảo mật bắt buộc | Nâng facial recognition + SCA |
| 4 | Buyer nhận hàng & hoàn tất đơn | User | ✓ | | | Hoàn tất chuỗi mua — giá trị | Giữ nguyên |
| 5 | Buyer nhận hoàn tiền khi hủy/hoàn trả | User | ✓ | | | Hoàn tiền đúng hạn cho Buyer | Instant refund qua wallet |
| 6 | Cổng thanh toán xử lý giao dịch | Service | ✓ | | | Heartbeat — tiền thực sự được xử lý | Multi-gateway fallback |
| 7 | Xác minh chữ ký & tính hợp lệ giao dịch | Service | | ✓ | | Bảo mật bắt buộc | Giữ nguyên |
| 8 | Gửi kết quả thanh toán về hệ thống | Service | ✓ | | | Cập nhật trạng thái đơn | Giữ nguyên |
| 9 | Kiểm tra IPN/Webhook đối soát giao dịch | Service | | ✓ | | Đối soát tự động — kiểm soát | Auto-reconcile real-time |
| 10 | Hệ thống giữ tiền tạm thời trong Escrow | Service | | ✓ | | Ký quỹ bảo vệ 2 bên | Blockchain escrow minh bạch |
| 11 | Đối chiếu giao dịch với mã đơn hàng | Service | ✓ | | | Core reconciliation — tiền khớp đơn | Auto-reconciliation ML |
| 12 | Giải ngân tiền cho Seller (L+2 ngày) | Service | ✓ | | | Seller nhận tiền — giá trị cuối cùng | Instant settlement cho trusted |
| 13 | Đối soát COD với 3PL thu hộ | Service | | ✓ | | Matching cash từ shipper — 97-98% accuracy | ML auto-matching |
| 14 | Tổng hợp đối soát dòng tiền cuối ngày | Service | ✓ | | | Báo cáo dòng tiền chính xác | Auto tổng hợp real-time |
| 15 | Tính hoa hồng Lazada (1-8% theo danh mục) | Service | ✓ | | | Doanh thu cốt lõi của sàn | Dynamic commission model |
| 16 | Cập nhật số dư Ví Seller | Service | ✓ | | | Seller thấy tiền chính xác | Real-time wallet sync |
| 17 | Phòng Tài chính xử lý lệch dòng tiền | User | | | ✓ | NVA — xử lý chênh lệch thủ công từng case | Auto-triage + AI detect root cause |
| 18 | Xác nhận bảng đối soát cuối kỳ | User | ✓ | | | Kiểm soát tài chính cuối kỳ — minh bạch | Dashboard số liệu thống nhất |
| 19 | Điều chỉnh số liệu sai lệch trên bảng kê | User | | | ✓ | NVA — sửa sai thủ công | Auto-adjust + audit trail |
| 20 | Xuất hóa đơn & báo cáo tài chính | User | | ✓ | | Bắt buộc theo quy định pháp luật | Auto-e-invoice integration |
| 21 | Seller kiểm tra số dư Ví trên Seller Centre | User | ✓ | | | Minh bạch dòng tiền cho Seller | Real-time dashboard |
| 22 | Seller yêu cầu rút tiền về tài khoản ngân hàng | User | ✓ | | | Seller cần nhận tiền | Ví Lazada instant + bank API |

**Phân tích:** 14 VA (64%) / 6 BVA (27%) / **2 NVA (9%)** — xử lý lệch dòng tiền & điều chỉnh sai lệch thủ công (từ 2-3% chênh lệch COD ~90-135 tỷ VND/tháng). **Waste chính là Hold:** settlement L+2/L+3 và bank transfer 24-48h → TO-BE instant settlement + auto-reconciliation.

---

## 09. Logistics & Giao nhận (Logistics & Delivery) — 20 tasks

| # | Task (trong BPMN) | Loại | VA | BVA | NVA | Lý do | Đề xuất TO-BE |
|---|-------------------|------|----|-----|-----|-------|---------------|
| 1 | Seller chuẩn bị hàng hóa đóng gói | User | ✓ | | | Chuẩn bị hàng vận chuyển — bắt buộc | Hướng dẫn đóng gói chuẩn LEX |
| 2 | Đóng gói hàng hóa & gắn nhãn vận chuyển | User | ✓ | | | Hàng sẵn sàng cho AWB | Auto-print label |
| 3 | Đặt lịch hẹn lấy hàng từ 3PL | User | ✓ | | | Chủ động schedule pickup | Auto-schedule theo vị trí Seller |
| 4 | Gửi mã theo dõi vận chuyển cho Buyer | User | | ✓ | | Buyercần biết tracking | Auto-send qua app/SMS |
| 5 | Tạo vận đơn tự động (AWB) | Service | | ✓ | | Bắt buộc cho tracking — không trực tiếp tạo giá trị | Giữ nguyên |
| 6 | Phân công 3PL phù hợp (LEX/GHN/J&T) | Service | | ✓ | | Phân bổ hợp lý — tối ưu chi phí | AI phân bổ theo tuyến + chi phí |
| 7 | Tạo lô hàng vận chuyển trên hệ thống | Service | | ✓ | | Gom lô cho line-haul | Giữ nguyên |
| 8 | 3PL nhận hàng từ kho Seller | User | ✓ | | | Hàng bắt đầu di chuyển trong mạng | Auto-confirm pickup |
| 9 | Phân loại hàng tại kho trung tâm 3PL | Service | | ✓ | | Sort bắt buộc — Hold 2-6h, capacity 75% | AI sorting + automated Hub |
| 10 | Vận chuyển hàng qua các trung tâm phân loại | Service | ✓ | | | Di chuyển hàng giữa Hub — core | Giữ nguyên |
| 11 | Hàng xuất kho — shipper nhận giao | Service | ✓ | | | Out for delivery | Giữ nguyên |
| 12 | Shipper giao hàng cho Buyer tại địa chỉ | User | ✓ | | | Giao hàng cốt lõi — first attempt 85% | Slot hẹn giờ + gọi trước 15 phút |
| 13 | Hẹn giao lại lần tiếp theo | User | | | ✓ | NVA — giao lại lần 1 (15% đơn) | Giảm tối đa 2 lần + address verify |
| 14 | Buyer nhận hàng & kiểm tra tại chỗ | User | ✓ | | | Buyer verify chất lượng — giá trị | Giữ nguyên |
| 15 | Buyer xác nhận đã nhận hàng | User | ✓ | | | POD xác nhận giao thành công | Digital POD + chữ ký |
| 16 | Buyer từ chối nhận hàng (lý do) | User | | | ✓ | NVA — từ chối → reverse logistics | Ghi nhận lý do + giảm retry |
| 17 | Seller đóng gói lại hàng hóa theo yêu cầu | User | | | ✓ | NVA — repack sau hoàn về | Giảm return rate (8-12% → 4-7%) |
| 18 | Nhận hàng hoàn về từ 3PL (giao thất bại 3 lần) | Service | | | ✓ | NVA — reverse logistics tốn kém | Giảm retry xuống 2 lần |
| 19 | Cập nhật trạng thái COD trên hệ thống | Service | | ✓ | | COD tracking cho đối soát | Auto-update realtime |
| 20 | Chuyển hoàn hàng về kho Seller | User | | | ✓ | NVA — hoàn về gốc, chi phí cao nhất | Đánh giá trước khi hoàn |

**Phân tích:** 9 VA (45%) / 6 BVA (30%) / **5 NVA (25%)** — **tỷ trọng NVA cao nhất trong 10 quy trình** (giao lại, từ chối nhận, repack, hoàn về): chi phí retry ~85 tỷ (24.0%) + return ~90 tỷ (25.4%) VND/tháng → TO-BE slot hẹn giờ + predictive ETA + AI route optimization (giảm ~40% return rate).

---

## 10. Vận hành Nền tảng Công nghệ (IT Operations) — 18 tasks

| # | Task (trong BPMN) | Loại | VA | BVA | NVA | Lý do | Đề xuất TO-BE |
|---|-------------------|------|----|-----|-----|-------|---------------|
| 1 | Tạo User Story & acceptance criteria | User | ✓ | | | Nền tảng cho mọi phát triển | AI-assisted story estimation |
| 2 | Ưu tiên backlog & sprint planning | User | ✓ | | | Chọn đúng việc làm — giá trị trực tiếp | Data-driven prioritization |
| 3 | Demo tính năng cho Stakeholder | User | ✓ | | | Stakeholder sign-off | Automated demo dashboard |
| 4 | Thiết kế kiến trúc & API cho tính năng | User | ✓ | | | Đảm bảo giải pháp đúng trước khi code | Auto-generate design từ spec |
| 5 | Viết code theo User Story & unit test | User | ✓ | | | Tính năng cốt lõi — giá trị trực tiếp | AI-assisted coding (Copilot) |
| 6 | Chạy unit test & code review | User | | ✓ | | Đảm bảo chất lượng code, bắt lỗi sớm | AI code review + auto-assign reviewer |
| 7 | Thực hiện System Test & Integration Test | User | | ✓ | | Đảm bảo tích hợp đúng | AI-driven test generation |
| 8 | Sửa lỗi QA phát hiện & regression test | User | | | ✓ | NVA — rework do bug (2-5 ngày/release) | Shift-left testing giảm 60% bugs |
| 9 | Performance test & load test | User | | ✓ | | Đảm bảo SLA trước khi release | Continuous performance testing |
| 10 | Triển khai lên môi trường Pre-Staging | Service | | ✓ | | Verify trên môi trường gần prod | IaC auto-provisioning |
| 11 | Triển khai lên môi trường Staging (UAT) | Service | | ✓ | | Validate toàn diện trước prod | Canary deployment tự động |
| 12 | Triển khai lên Production (Blue-Green Deploy) | Service | ✓ | | | Tính năng đến tay người dùng — giá trị | Blue-green / Canary |
| 13 | Giám sát metrics sau deploy 30 phút | Service | | ✓ | | Đảm bảo ổn định sau release | AIOps predictive monitoring |
| 14 | Rollback về version trước — tạo Incident | User | | | ✓ | NVA — deploy thất bại 15% | Self-healing pods, auto-rollback |
| 15 | Xử lý sự cố infrastructure & incident | User | | ✓ | | Khắc phục sự cố — MTTR 2-4h | Runbook + AIOps |
| 16 | Quét lỗ hổng bảo mật (SAST/DAST) | Service | | ✓ | | Bắt buộc cho compliance | Shift-left SAST/SCA trong CI |
| 17 | Áp dụng bản vá bảo mật khẩn cấp | User | | ✓ | | Khắc phục lỗ hổng — 7-14 ngày response | Auto-patch workflow |
| 18 | Triển khai bản vá & regression test | User | | ✓ | | Xác nhận bản vá an toàn | Tự động hóa |

**Phân tích:** 6 VA (33%) / 10 BVA (56%) / **2 NVA (11%)** — bug fix loop (30% chi phí lãng phí), rollback (15% deploy fail): tổng ~3.9 tỷ VND/tháng → TO-BE shift-left testing + canary + AI code review (giảm 77% chi phí lãng phí).

---

## Tổng hợp đề xuất TO-BE ưu tiên

| # | NVA/Waste | Process | Giải pháp | Nhóm cải tiến |
|---|-----------|---------|-----------|---------------|
| 1 | Chờ Seller confirm 2-24h (Hold) | 03 Order | Auto-accept sau 2h | Ngắn hạn |
| 2 | Chờ LEX/3PL pickup 4-12h (Hold) | 03, 04 | Scheduled pickup slot | Ngắn hạn |
| 3 | Chờ compliance review 24-48h (Hold) | 01 Seller | Auto-approve low-risk 3s | Ngắn hạn |
| 4 | Budget approval 2-5 ngày (Hold) | 06 Marketing | Risk-tiering + digital workflow | Trung hạn |
| 5 | Chờ kiểm định Return Center 3-7 ngày (Hold) | 04 Refund | Return-less <200k + AI image inspection | Ngắn hạn |
| 6 | Chờ CS queue 5-30' (Hold) | 05 CS | Predictive staffing + AI intent routing | Trung hạn |
| 7 | Mô tả lại vấn đề / transcript dài (Move) | 05 CS | Auto-context + auto-summary | Ngắn hạn |
| 8 | Nhập tay tracking number (Move) | 03 Order | API auto-sync với 3PL | Ngắn hạn |
| 9 | Vòng evidence lặp (Overdo) | 02 Dispute | Giới hạn 2 vòng + structured form | Trung hạn |
| 10 | Inspect hàng hoàn thủ công tại kho (NVA) | 04 Refund | Return-less refund + AI inspection | Ngắn hạn |
| 11 | Kích hoạt hoàn tiền thủ công (NVA) | 04 Refund | Auto-execute refund qua gateway | Ngắn hạn |
| 12 | Cấu hình campaign copy-paste (NVA) | 06 Marketing | Template library + auto-config | Ngắn hạn |
| 13 | Thu thập số liệu đối soát thủ công (NVA) | 06 Marketing | Auto-extend từ data warehouse | Trung hạn |
| 14 | Chờ Finance approval 5-10 ngày (Hold) | 07 HR | Auto-approval threshold + parallel workflow | Trung hạn |
| 15 | Content creation thủ công 2-4 tuần (Hold) | 07 HR | AI-generated content + template chuẩn | Trung hạn |
| 16 | Chênh lệch COD 2-3% → xử lý thủ công (NVA) | 08 Payment | ML auto-reconciliation + COD digital verification | Ngắn hạn |
| 17 | Settlement L+2/L+3 chậm (Hold) | 08 Payment | Instant settlement cho trusted seller | Trung hạn |
| 18 | Giao lại nhiều lần 15% đơn (NVA) | 09 Logistics | Slot hẹn giờ + predictive ETA + gọi trước 15 phút | Ngắn hạn |
| 19 | Hàng hoàn về 8-12% (NVA) | 09 Logistics | Address validation realtime + giảm retry ≤2 lần | Ngắn hạn |
| 20 | Sort Hub 2-6h (Hold) | 09 Logistics | AI sorting + automated Hub | Trung hạn |
| 21 | Bug fix loop 2-5 ngày/release (NVA) | 10 IT Ops | Shift-left testing + AI code review | Ngắn hạn |
| 22 | Deploy thất bại 15% → rollback (NVA) | 10 IT Ops | Canary deploy + quality gates + IaC | Trung hạn |

---

> **Liên kết:** [issue-register.md](issue-register.md) (65 issues) — [fishbone-diagrams.md](fishbone-diagrams.md) (3 fishbone diagrams)

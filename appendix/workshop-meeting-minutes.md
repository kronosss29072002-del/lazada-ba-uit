# PHỤ LỤC: BIÊN BẢN CUỘC HỌP WORKSHOP — LAZADA VIỆT NAM

---

## I. BIÊN BẢN CUỘC HỌP WORKSHOP KHẢO SÁT 6 QUY TRÌNH (MEETING MINUTES)

**Dự án:** Phân tích & Cải tiến 10 Quy trình Nghiệp vụ Lazada Việt Nam (Seller Management, Dispute Management, Order Processing, Return & Refund, Customer Service, Marketing, HR & Training, Payment & Settlement, Logistics & Delivery, IT Operations) — Đồ án BA
**Thời gian:** 09:00 – 12:00, Ngày 20 tháng 08 năm 2026 (3 giờ)
**Địa điểm:** Văn phòng Lazada Việt Nam, Tòa nhà Flemington, 182 Lê Đại Hành, Quận 11, TP.HCM + Trực tuyến qua Microsoft Teams
**Hình thức:** Hybrid (Trực tiếp + Online)

### 1. Thành phần tham dự

**Đại diện Nhóm BA (Thực hiện khảo sát):**
- Nguyễn Văn A – Lead Business Analyst (Chủ trì / Facilitator)
- Trần Thị B – Process Analyst & Note Taker (Thư ký)
- Lê Văn C – Quantitative Data Analyst

**Đại diện Lazada (Các bên liên quan — Stakeholders):**
- Phùng Văn D – Manager, Seller Operations (phụ trách Quy trình 1: Quản lý Nhà bán hàng)
- Nguyễn Thị E – Team Lead, Customer Service & Dispute Resolution (phụ trách Quy trình 2 & 5)
- Hoàng Văn F – Head of Fulfillment Operations, LEX Logistics (phụ trách Quy trình 3 & 4)
- Đỗ Thu Hà – Seller Operations Partner Lead (Quy trình 1)
- Trần Minh Đức – Senior Dispute Resolution Specialist (Quy trình 2)
- Lê Hoàng Nam – Head of Fulfillment Operations, LEX (Quy trình 3)
- Nguyễn Thị Mai – Trưởng bộ phận Return & Refund (Quy trình 4)
- Phạm Thị Lan – Senior Customer Service Manager (Quy trình 5)
- Vũ Quốc Bảo – Senior Campaign Manager (Quy trình 6)
- 5 Đại diện Người bán (Seller tầm trung + LazMall: ngành Hàng Tiêu Dùng, Điện Tử, Thời Trang)
- 5 Đại diện Người mua (Buyers tần suất mua cao — Phân hạng VIP/Kim Cương)

**Tổng cộng:** 22 người tham dự (03 thành viên nhóm BA + 09 đại diện Lazada + 05 đại diện Người bán + 05 đại diện Người mua)

---

### 2. Chương trình cuộc họp (Agenda)

| Giờ | Nội dung | Người phụ trách |
|-----|----------|-----------------|
| 09:00 – 09:20 | Tuyên bố mục đích workshop; giới thiệu phương pháp phân tích quy trình BPMN 2.0; phổ biến bộ câu hỏi phỏng vấn chuẩn (Appendix: interview-questions.md — 20 câu: 10 định tính + 10 định lượng) | Nguyễn Văn A |
| 09:20 – 09:50 | Trình bày sơ đồ quy trình AS-IS của 10 quy trình nhóm đã xây dựng và kiểm chứng thực tế (gateways, timer SLA, pools/lanes, end events) | Trần Thị B |
| 09:50 – 11:00 | Thảo luận nhóm (Breakout) theo từng quy trình về lãng phí (Waste – VA/NVA/BVA) và điểm nghẽn (Bottlenecks) | Nhóm BA + 9 chuyên gia vận hành |
| 11:00 – 11:40 | Thu thập đóng góp cho mô hình cải tiến (TO-BE); bình chọn giải pháp ưu tiên (dot-voting) | Lê Văn C + toàn thể |
| 11:40 – 12:00 | Tổng kết, thống nhất SLA & KPI mục tiêu, ký biên bản | Nguyễn Văn A |

---

### 3. Nội dung thảo luận & Điểm thống nhất

#### A. Xác nhận quy trình AS-IS (10 quy trình)

1. **Quản lý Nhà bán hàng (Q1):** Đại diện Seller Ops xác nhận luồng Đăng ký → KYC → Phê duyệt → Onboarding → Kinh doanh → Giám sát → Xử lý vi phạm phản ánh ~90% thực tế. Thang phạt Warning → Delist → Suspend → Deactivate → Re-register được xác nhận đúng. Ngưỡng Cancellation Rate & Late Shipment Rate ~5% là sát thực tế.
2. **Quản lý Tranh chấp (Q2):** Đại diện Dispute xác nhận luồng khiếu nại → AI categorize → điều tra → quyết định → kháng cáo cấp 2 (7 ngày). SLA seller phản hồi 48h được xác nhận; hết hạn im lặng → auto nghiêng về buyer.
3. **Xử lý Đơn hàng Online (Q3):** Head of Fulfillment xác nhận luồng phức tạp nhất: seller accept (24–48h) → pickup LEX → QC inspection (5–15 phút/kiện) → packing → handoff → in-transit → out-for-delivery → delivery attempt → COD settle. Split shipment + QC fail loop + auto-cancel timer được xác nhận là có thật.
4. **Hoàn trả & Hoàn tiền (Q4):** Trưởng Return & Refund xác nhận 3 loại yêu cầu (Full Return / Partial Refund / Only Refund) ngay gateway đầu; cửa sổ hoàn trả 7–15 ngày; refund qua Lazada Wallet nhanh, thẻ/bank 5–15 ngày, COD không hoàn tiền mặt.
5. **Chăm sóc Khách hàng (Q5):** CS Manager xác nhận vòng chatbot → agent → Tier-2 và vòng CSAT; thẩm quyền agent hiện tại thấp (refund ≤50,000 VND).
6. **Marketing & Khuyến mãi (Q6):** Campaign Manager xác nhận luồng planning → duyệt ngân sách theo hạng mức (CFO/CMO/hội đồng) → creative + compliance → mở cổng seller (7–14 ngày) → eligibility + price validation → launch → giám sát → post-campaign → auto-renew.

#### B. Xác định lãng phí & Pain points chính (Root Causes)

1. **Hold Time (Chờ đợi):**
   - *Seller accept:* Nhiều seller để đơn quá lâu; auto-cancel 24–48h gây gánh nặng chỉ số cho seller nhỏ mới (khớp phỏng vấn Q1). Xác nhận waste hold time.
   - *Approval ngân sách:* 70% budget campaign dưới ngưỡng vẫn vào queue thủ công 3–7 ngày (khớp phỏng vấn Q6 — Marketing).
2. **Defects (Lỗi giao hàng):**
   - *Giao thất bại lần đầu 20–25%:* địa chỉ sai, khách không nghe máy, thiếu pre-delivery contact (khớp phỏng vấn Q3 — Order; LEX ước ~15% theo góc nhìn kho, phạm vi e-commerce toàn chuỗi 20–25%).
   - *QC fail 3–5%:* barcode in nhòe, sai SKU/hết hạn (warehouse view).
3. **Over-do & Manual Handling:**
   - *Refund ≤50k–200k phải escalate Tier-2* chờ 1–5 ngày (Q5).
   - *COD settlement reconciliation thủ công:* 1.5 ngày/tuần (Q3).
   - *Price validation + check scam seller giả giá gốc:* thủ công (Q6).
   - *Inspection hoàn trả 3–7 ngày* thiếu ảnh baseline lúc pack (Q4).
4. **Notification & Self-service:**
   - Seller bỏ sót notification phản hồi 48h → auto-approve mất tiền oan (Q1, Q4).
   - Chatbot triage sai intent → chuyển agent, delay (Q5).

#### C. Thống nhất định hướng cải tiến (TO-BE Solutions) — kết quả dot-voting (top 5)

| Hạng | Giải pháp TO-BE | Số phiếu | Quy trình liên quan |
|------|-----------------|----------|---------------------|
| 1 | **Instant refund tự động** (Only Refund không cần inspection) cho đơn <100,000 VND từ shop uy tín (điểm ≥4.5 sao, return rate <2%) | 14/24 | Q4, Q2 |
| 2 | **Tier-based QC inspection** (shop uy tín skip QC chỉ random sampling; shop mới/vi phạm QC 100%) | 12/24 | Q3, Q1 |
| 3 | **Tăng thẩm quyền CS Agent** refund lên 200,000 VND cho agent kinh nghiệm >1 năm + QA score ≥85% | 11/24 | Q5 |
| 4 | **Unified CRM single-pane view** (order + tracking LEX + payment + chat log trên 1 màn hình); tracking auto-sync realtime WMS ↔ Seller Center | 10/24 | Q5, Q3 |
| 5 | **Rule engine duyệt ngân sách theo hạng mức** + pre-approved quarterly buffer; chia sẻ predicted volume forecast cho Ops/Warehouse | 9/24 | Q6, Q3 |

**Các đề xuất bổ sung được ghi nhận:** Escrow hold cho tranh chấp giá trị >500k (Q2); auto-flag SKU lịch sử khiếu nại cao (Q2); hướng dẫn upload bằng chứng theo category (Q2/Q4); cảnh báo proactive trước deadline 48h + cảnh báo ngưỡng 5% cho seller (Q1); pre-delivery contact + khung giờ giao (Q3); nudge buyer chọn đúng loại yêu cầu hoàn trả (Q4).

---

### 4. Kết luận & Hành động tiếp theo (Action Items)

| STT | Nội dung công việc | Người chịu trách nhiệm | Hạn hoàn thành |
|-----|--------------------|------------------------|----------------|
| 1 | Cập nhật sơ đồ BPMN AS-IS theo góp ý (bổ sung annotation & timer) | Nhóm BA (Trần Thị B) | 25/08/2026 |
| 2 | Xây dựng sơ đồ TO-BE phiên bản 1 cho 10 quy trình theo 5 giải pháp đã chọn | Nhóm BA (Nguyễn Văn A) | 28/08/2026 |
| 3 | Tính toán lại Cycle Time & Cost Saving cho Instant Refund (<100k) và Tier-based QC | Nhóm BA (Lê Văn C) | 29/08/2026 |
| 4 | Phê duyệt mô hình TO-BE và đưa vào Báo cáo Đồ án | Lãnh đạo các bộ phận Lazada | 02/09/2026 |

**Thư ký cuộc họp:** *(Đã ký)* Trần Thị B
**Trưởng Nhóm BA:** *(Đã ký)* Nguyễn Văn A

---

## II. KỊCH BẢN WORKSHOP PHỎNG VẤN & THẢO LUẬN TƯƠNG TÁC (WORKSHOP SCRIPT)

### 1. Thông tin chung
- **Mục tiêu:** Thu thập dữ liệu định tính + định lượng trực tiếp từ bộ 20 câu hỏi chuẩn (interview-questions.md — 10 định tính: 5 Likert + 5 mở; 10 định lượng: 5 trắc nghiệm + 5 nhập số) cho 10 quy trình.
- **Thời lượng:** 75 phút / phiên.
- **Người tham gia/phiên:** 1 chuyên gia vận hành (domain expert) + 1 giám sát mobile từ phía BA + 1 người thu thập sẽ không lộ danh tính.

### 2. Kịch bản chi tiết (Step-by-Step Script)

#### Bước 1: Mở đầu & Khởi động (Warm-up) – 5 phút
- **Facilitator:** *"Xin chào quý anh/chị. Cảm ơn đã tham dự phiên phỏng vấn khảo sát quy trình Lazada. Mục tiêu của chúng tôi là làm rõ các điểm nghẽn thực tế và cùng xây dựng giải pháp tối ưu cho 10 quy trình: quản lý seller, tranh chấp, xử lý đơn, hoàn trả hoàn tiền, CSKH, marketing, HR & Training, Payment & Settlement, Logistics & Delivery, IT Operations."*
- **Hoạt động:** Giới thiệu mục đích học thuật, cam kết ẩn danh, kiểm tra quyền ghi âm, phát bộ câu hỏi.

#### Bước 2: Phỏng vấn Định tính (Q1 – Q10) – 25 phút
- Lần lượt đi qua 5 câu Likert 1–5 (Q1–Q5) và 5 câu mở (Q6–Q10).
- **Câu hỏi gợi mở:**
  - *"Q6: Anh/chị mô tả bước nào làm mất nhiều thời gian nhất từ lúc nhận đơn Lazada đến khi LEX lấy hàng?"*
  - *"Q8: Nếu được cắt bỏ/tự động hóa 1 bước trong quy trình Lazada hiện tại, anh/chị chọn bước nào? Tại sao?"*
- **Thư ký:** Ghi chép câu trả lời vào bảng phân loại VA / BVA / NVA / Waste theo 10 quy trình.

#### Bước 3: Thu thập số liệu Định lượng & KPI (Q11 – Q20) – 20 phút
- Hướng dẫn điền 5 câu trắc nghiệm (Q11–Q15) + 5 câu nhập số (Q16–Q20).
- **Tập trung vào:**
  - Thời gian accept → LEX pickup; tỷ lệ giao thất bại lần đầu.
  - Chi phí đóng gói, chi phí vận hành biên/đơn.
  - Thời gian hoàn tất hoàn trả/refund; CSAT; chi phí marketing/đơn.

#### Bước 4: Deep-dive vào Waste & Bottleneck – 15 phút
- Follow-up vào những điểm bất thường phát hiện từ câu trả lời (ví dụ: split shipment không thông báo, auto-approve do seller im lặng, approval ngân sách thủ công).
- **Facilitator:** Ghi các waste lên bảng Miro/Jamboard theo 6 luồng.

#### Bước 5: Tổng kết & Cảm ơn – 5 phút
- Tóm tắt các điểm chính; xin phép follow-up qua email nếu cần; gửi voucher cảm ơn (Lazada 100k).

---

## III. GHI CHÚ SỬ DỤNG DỮ LIỆU

1. Biên bản workshop này tổng hợp kết quả thảo luận của cuộc họp ngày 20/08/2026, có đối chiếu với 10 bộ phỏng vấn riêng trong thư mục `interviews/` (file 01 → 10, mỗi file một quy trình tương ứng).
2. Các con số trong biên bản là số liệu giả định phục vụ mục đích học thuật (mock data), dựa trên ước tính từ chính sách công khai của Lazada và dữ liệu huấn luyện (như ghi chú tại `lazada_04_6_quytrinh_bpmn_ready.md`).
3. Toàn bộ dữ liệu phỏng vấn dùng để kiểm chứng sơ đồ AS-IS và xây dựng TO-BE trong:
   - `docs/analysis/` (6 phân tích quy trình)
   - `docs/analysis/comparison/` (so sánh các quy trình)
   - `docs/analysis/issue-register.md` (đăng ký vấn đề/issues)

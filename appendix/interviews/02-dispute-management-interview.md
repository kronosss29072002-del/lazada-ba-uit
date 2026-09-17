# Bộ Phỏng vấn riêng — Quy trình 02: Quản lý Tranh chấp (Dispute Resolution)

## A. Mục đích phỏng vấn & Đối tượng

### Mục đích
Thu thập dữ liệu về **quy trình khiếu nại trên Lazada VN** — từ lúc buyer gửi khiếu nại qua Resolution Center, auto-categorize (hàng hư/sai mô tả/thiếu hàng/hàng giả/giao trễ), seller phản hồi trong 48h, điều tra CS Agent/Dispute Team, đưa ra quyết định sơ bộ, vòng kháng cáo cấp 2 (7 ngày), đến thực thi hoàn tiền/hoàn hàng.

### Thông tin người phỏng vấn
- **Họ tên (giả định):** Anh Trần Minh Đức
- **Vai trò:** Senior Dispute Resolution Specialist — xử lý tranh chấp phức tạp giá trị cao (trên 500,000 VND), phụ trách mảng Hàng điện tử & Thực phẩm trên Lazada Việt Nam
- **Thâm niên:** 4 năm làm dispute resolution marketplace (2 năm Tiki, 2 năm Lazada)
- **Kinh nghiệm liên quan:** Xử lý 200–300 tranh chấp/tháng; am hiểu luồng kháng cáo cấp 2; từng tham gia pilot features Resolver Team với AI auto-decision
- **Hình thức phỏng vấn:** Trực tuyến (Google Meet), 55 phút, 14:00 ngày 07/08/2026

---

## B. 10 Câu hỏi ĐỊNH TÍNH

### B1. 5 câu CẤU TRÚC (Thang đo Likert 1-5)

| # | Câu hỏi | 1 | 2 | 3 | 4 | 5 |
|---|---------|---|---|---|---|---|
| Q1 | Mức độ hài lòng với quy trình xử lý đơn hàng trên Lazada hiện tại? | | | ✓ (3) | | |
| Q2 | Quy trình đóng gói & bàn giao cho LEX/shipper có dễ thực hiện? | | | | ✓ (4) | |
| Q3 | Hệ thống notification của Lazada có hữu ích (đúng lúc, không spam)? | | | ✓ (3) | | |
| Q4 | Thời gian xử lý đơn (auto-cancel, SLA giao LEX) có hợp lý? | | | | ✓ (4) | |
| Q5 | Quy trình hoàn trả & hoàn tiền trên Lazada có minh bạch & công bằng? | | | | ✓ (4) | |

### B2. 5 câu KHÔNG CẤU TRÚC (Câu hỏi mở)

**Q6. Anh/chị mô tả chi tiết các bước xử lý 1 đơn hàng Lazada kể từ lúc nhận thông báo đến khi bàn giao kiện cho LEX? Bước nào mất thời gian nhất?**

> "Là Dispute Team nên tôi chủ yếu can thiệp khi đơn đã phát sinh vấn đề, nhưng tôi hiểu luồng căn bản: buyer nhận hàng → mở Resolution Center → chọn lý do → upload bằng chứng → AI auto-categorize → gán CS Agent hoặc Dispute Team tùy giá trị/độ phức tạp → seller phản hồi 48h → điều tra → quyết định sơ bộ. Bước **mất thời gian nhất là điều tra** — phải đối chiếu tracking, chat log, ảnh QC, chính sách bảo hành; với hàng điện tử mất 3–5 ngày vì cần xác minh tính năng lỗi."

**Q7. Những khó khăn/lỗi thường gặp nhất khi thao tác trên Lazada là gì? (top 3)**

> "Top 3: (1) **Seller không phản hồi đúng hạn 48h** — bằng chứng thiếu khiến quyết định nghiêng hoàn toàn về buyer, gây bất công; (2) **Bằng chứng buyer upload không rõ ràng** — ảnh mờ, không chụp lỗi cụ thể, phải yêu cầu bổ sung, kéo dài điều tra 2–3 ngày; (3) **Hàng giả/hàng nhái khó xác minh** — cần phối hợp Compliance + thương hiệu gốc xác nhận, quy trình thường mất 5–7 ngày thay vì 2–5 ngày bình thường."

**Q8. Nếu được thay đổi 1 điều trong quy trình Lazada hiện tại, anh/chị sẽ thay đổi gì? Tại sao?**

> "Tôi muốn **thêm cơ chế 'giữ tiền tạm' (escrow hold) tự động khi buyer mở tranh chấp giá trị lớn** (>500k). Hiện tại, tiền đã về seller ngay sau giao hàng, khi tranh chấp xong phải trừ vào số dư gây khó khăn cho seller tư bản nhỏ. Escrow hold sẽ bảo vệ buyer mà không gây shock tài chính cho seller."

**Q9. Lazada có những hạn chế nào ảnh hưởng trực tiếp đến hiệu suất làm việc của anh/chị?**

> "Hệ thống không có **auto-flag SKU có lịch sử khiếu nại cao** — tôi phải tự search từng case. Ngoài ra, luồng kháng cáo cấp 2 (3–7 ngày) xử lý thủ công rất chậm vì thiếu công cụ auto-compare bằng chứng lần 1 và lần 2. Chat log giữa buyer–seller phân tán, phải mở nhiều tab."

**Q10. Anh/chị xử lý thế nào khi có đơn Lazada bị hoàn trả, tranh chấp hoặc khiếu nại CSKH? Mô tả workflow thực tế.**

> "Khi nhận tranh chấp phức tạp: (1) Xem timeline đơn + bằng chứng AI categorize; (2) Liên hệ seller yêu cầu bằng chứng bổ sung trong 48h; (3) Đọc chat log buyer–seller; (4) Check tracking LEX; (5) Nếu hàng điện tử, tham khảo chính sách bảo hành; (6) Đưa quyết định sơ bộ (buyer/seller thắng); (7) Gửi cả 2 bên → bên thua kháng cáo trong 7 ngày; (8) Dispute Team cấp cao xử lý kháng cáo (3–7 ngày) → quyết định cuối cùng; (9) Finance thực thi refund/hold; (10) Cập nhật dispute rate seller."

---

## C. 10 Câu hỏi ĐỊNH LƯỢNG

### C1. 5 câu CẤU TRÚC (Multiple Choice)

**Q11.** Trung bình các seller trong phạm vi phụ trách xử lý bao nhiêu đơn/ngày?
- [ ] < 10 đơn
- [ ] 10-50 đơn
- [x] 50-100 đơn *(phần lớn seller tầm trung Luzmall/DN)*
- [ ] 100-500 đơn
- [ ] > 500 đơn

**Q12.** Thời gian trung bình đóng gói + dán waybill 1 đơn (seller-arranged)?
- [ ] < 5 phút
- [x] 5-15 phút *(seller chuyên nghiệp)*
- [ ] 15-30 phút
- [ ] 30-60 phút
- [ ] > 60 phút

**Q13.** Tỷ lệ đơn bị khiếu nại/tranh chấp/hoàn trả trung bình trên Lazada (trong mẫu bạn xử lý)?
- [ ] < 2%
- [ ] 2-5%
- [x] 5-10% *(hàng điện tử + thực phẩm có tỷ lệ cao hơn)*
- [ ] 10-20%
- [ ] > 20%

**Q14.** Số lần LEX/shipper pickup tại kho/seller trung bình/tuần?
- [ ] 1-2 lần
- [ ] 3-5 lần
- [x] 6-10 lần *(seller lớn có LEX pickup hàng ngày)*
- [ ] Hàng ngày
- [ ] Nhiều hơn 1 lần/ngày

**Q15.** Chi phí đóng gói trung bình/đơn (bao bì + băng keo + xốp)?
- [ ] < 3,000 VND
- [ ] 3,000-5,000 VND
- [x] 5,000-10,000 VND *(hàng điện tử cần bọc chống sốc, thùng cứng)*
- [ ] 10,000-20,000 VND
- [ ] > 20,000 VND

### C2. 5 câu KHÔNG CẤU TRÚC (Numeric Open)

**Q16.** Thời gian trung bình từ lúc nhận đơn đến khi LEX pickup? → **~12 giờ** (seller accept trong 2–4h + chờ pickup 8–12h)

**Q17.** Tỷ lệ % đơn giao thành công ngay lần đầu tiên? → **~87%** (13% thất bại — cao hơn trung bình do hàng điện tử phải hẹn giờ chính xác)

**Q18.** Chi phí vận hành biên/đơn (nhân công + bao bì + điện nước)? → **~8,000 VND** (hàng điện tử cần đóng gói kỹ hơn)

**Q19.** Lượng đơn trong campaign 9.9/11.11/12.12 tăng gấp bao nhiêu lần? → **~5 lần** (mùa sale khiếu nại cũng tăng theo tỷ lệ ~30% so với ngày thường)

**Q20.** Thời gian trung bình hoàn tất 1 tranh chấp/hoàn tiền (buyer mở → nhận refund)? → **~8 ngày** (điều tra 2–5 ngày + kháng cáo 3–5 ngày nếu có)

---

## D. Bảng ghi chép kết quả giả định (Mock Results — 6 người trả lời)

### D1. Tóm tắt định tính

| ID | Vai trò | Q1 | Q2 | Q3 | Q4 | Q5 | Điểm nổi bật định tính |
|----|---------|----|----|----|----|----|------------------------|
| SL-01 | Seller nhỏ | 3 | 4 | 2 | 3 | 3 | "Bị khiếu nại sai, mất 7 ngày mới giải quyết xong" |
| SL-02 | Seller DN vừa | 4 | 4 | 4 | 4 | 3 | "Tiền bị trừ shock khi tranh chấp xong, không có escrow hold" |
| BY-01 | Buyer thường xuyên | 3 | — | 3 | 3 | 4 | "Gửi bằng chứng nhiều lần, chờ 5–7 ngày mới nhận refund" |
| BY-02 | Buyer VIP | 3 | — | 2 | 4 | 3 | "Chatbot không giải quyết được vấn đề, phải chờ agent 30 phút" |
| DS-01 | Dispute Specialist (người phỏng vấn) | 3 | 4 | 3 | 4 | 4 | "Thiếu auto-flag SKU lịch sử khiếu nại cao, xử lý thủ công" |
| QA-01 | CS Quality Assurance | 4 | — | 3 | — | 4 | "CSAT scores improve after instant refund pilot cho đơn nhỏ <200k" |

### D2. Tóm tắt định lượng

| ID | Q11 (đơn) | Q12 (phút) | Q13 (%) | Q14 (lần) | Q15 (VND) | Q16 (h) | Q17 (%) | Q18 (VND) | Q19 (lần) | Q20 (ngày) |
|----|-----------|-----------|---------|-----------|-----------|---------|---------|-----------|-----------|-----------|
| SL-01 | 10-50 | 15-30 | 10-20% | 3-5 | 5-10K | 22 | 85 | 8,000 | 3 | 9 |
| SL-02 | 50-100 | 5-15 | 5-10% | 6-10 | 5-10K | 10 | 91 | 7,500 | 5 | 7 |
| BY-01 | — | — | — | — | — | — | — | — | — | 10 |
| BY-02 | — | — | — | — | — | — | — | — | — | 6 |
| DS-01 | 100-500 | 5-15 | 5-10% | 6-10 | 5-10K | 12 | 87 | 8,000 | 5 | 8 |
| QA-01 | — | — | — | — | — | — | — | — | — | 5*(auto-refund)* |

### D3. Số liệu tổng hợp

| Metric | Giá trị trung bình (mock) | Ghi chú |
|--------|---------------------------|---------|
| Dispute resolution time | ~8 ngày (kháng cáo 3–5 ngày) | Khớp doc: 2–5 ngày điều tra + 3–7 ngày kháng cáo |
| Tỷ lệ khiếu nại | ~8% (hàng điện tử + thực phẩm) | Cao hơn marketplace trung bình (~5%) |
| Chi phí vận hành biên/đơn | ~8,000 VND | Đóng gói kỹ hơn (hàng điện tử) |
| Tỷ lệ kháng cáo seller | ~35% seller kháng cáo sau quyết định sơ bộ | Thiếu escrow hold → seller kháng cáo để bảo vệ tiền |
| CSAT sau instant refund | 4.2/5 *(pilot đơn <200k)* | Cải thiện 0.8 điểm so với quy trình truyền thống |

---

## E. Nhận xét rút ra từ câu trả lời

1. **Điều tra tranh chấp là bước tốn thời gian nhất** — DS-01: 3–5 ngày cho hàng điện tử do cần xác minh tính năng lỗi + chat log phân tán. Giải pháp: tích hợp chat log + tracking + ảnh QC vào 1 màn hình duy nhất (single-pane resolution tool).
2. **Thiếu escrow hold gây shock tài chính cho seller** — SL-02, DS-01: tiền đã về seller nên khi tranh chấp xong phải trừ trực tiếp → seller kháng cáo nhiều hơn (~35%). Giải pháp: auto-escrow hold cho đơn giá trị >500k khi buyer mở tranh chấp.
3. **Bằng chứng upload không rõ ràng kéo dài điều tra** — BY-01: phải upload lại nhiều lần; DS-01: yêu cầu bổ sung 2–3 ngày. Giải pháp: hướng dẫn upload cụ thể (theo category: ảnh lỗi, video test, screenshot).
4. **Auto-flag SKU lịch sử khiếu nại cao giúp phòng ngừa** — DS-01: thiếu tool này khiến phải search thủ công. Giải pháp: SKU Risk Dashboard tích hợp vào Dispute Team workspace.
5. **Instant refund cho đơn nhỏ có hiệu quả CSAT rõ rệt** — QA-01: pilot tự động hoàn tiền không cần inspection cho đơn <200k từ shop uy tín → CSAT tăng 0.8 điểm, thời gian giải quyết giảm còn 1–2 ngày. Đây là giải pháp TO-BE tiềm năng.

**Dữ liệu này được sử dụng trong:**
- `docs/analysis/02-dispute-management.md`
- `docs/analysis/comparison/02-dispute-management.md`
- `docs/analysis/issue-register.md` (issues DM-01 đến DM-05)

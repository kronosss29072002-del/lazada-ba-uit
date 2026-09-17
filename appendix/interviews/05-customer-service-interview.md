# Bộ Phỏng vấn riêng — Quy trình 05: Chăm sóc Khách hàng (Customer Service)

## A. Mục đích phỏng vấn & Đối tượng

### Mục đích
Thu thập dữ liệu về **quy trình CSKH Lazada VN** — từ lúc khách báo vấn đề qua Chat/Hotline/Email/Fanpage, chatbot triage (NLP intent classifier + FAQ KB), tự phục vụ, tạo ticket CRM, phân hạng ưu tiên & gán CS Agent, điều tra (tracking + payment + chat log + KB), escalation lên Tier-2 (Dispute/Tech/Finance/Compliance 1–5 ngày), giải pháp (refund/reship/coupon), CSAT survey 1–5 sao, đến QC chất lượng tương tác.

### Thông tin người phỏng vấn
- **Họ tên (giả định):** Chị Phạm Thị Lan
- **Vai trò:** Senior Customer Service Manager — phụ trách kênh Chat & Hotline Lazada VN, quản lý 60+ CS Agents, theo dõi CSAT score và QA scorecard
- **Thâm niên:** 5 năm CS marketplace (2 năm Tiki, 3 năm Lazada)
- **Kinh nghiệm liên quan:** Piloting chatbot triage + intent classifier; xây dựng escalation rules theo tier giá trị đơn & khách VIP; quản lý CSAT benchmark; directly handle Tier-2 escalations cho mảng Housing & FMCG
- **Hình thức phỏng vấn:** Trực tuyến (Zoom), 55 phút, 14:00 ngày 14/08/2026

---

## B. 10 Câu hỏi ĐỊNH TÍNH

### B1. 5 câu CẤU TRÚC (Thang đo Likert 1-5)

| # | Câu hỏi | 1 | 2 | 3 | 4 | 5 |
|---|---------|---|---|---|---|---|
| Q1 | Mức độ hài lòng với quy trình xử lý đơn hàng trên Lazada hiện tại? | | | ✓ (3) | | |
| Q2 | Quy trình đóng gói & bàn giao cho LEX/shipper có dễ thực hiện? | | | | ✓ (4) | |
| Q3 | Hệ thống notification của Lazada có hữu ích (đúng lúc, không spam)? | | | | ✓ (4) | |
| Q4 | Thời gian xử lý đơn (auto-cancel 24–48h, SLA giao LEX) có hợp lý? | | | | ✓ (4) | |
| Q5 | Quy trình hoàn trả & hoàn tiền trên Lazada có minh bạch & công bằng? | | | | ✓ (4) | |

### B2. 5 câu KHÔNG CẤU TRÚC (Câu hỏi mở)

**Q6. Anh/chị mô tả chi tiết các bước xử lý 1 đơn hàng Lazada kể từ lúc nhận thông báo trên Seller Center đến khi bàn giao kiện cho LEX? Bước nào mất thời gian nhất?**

> "Vì tôi làm CS nên góc nhìn khác — khách hàng liên hệ qua Chat/Hotline, tôi truy cập CRM theo dõi order: (1) Khách mô tả vấn đề (đơn chưa nhận, sai hàng, hoàn tiền...); (2) Agent tra cứu order trên CRM — check status đơn, tracking LEX, payment record, chat log seller; (3) Đọc KB (Knowledge Base) xem chính sách; (4) Giải quyết: refund, reship, coupon bù; (5) Đóng ticket + CSAT survey. Bước **mất thời gian nhất là tra cứu thông tin** — phải mở 3–4 tab (CRM + Tracking LEX + Payment Gateway + Chat log) để xác minh vấn đề, mất 10–20 phút chỉ để gather info."

**Q7. Những khó khăn/lỗi thường gặp nhất khi thao tác trên Lazada là gì? (top 3)**

> "Top 3: (1) **Chatbot triage sai intent** — khách hỏi về 'hoàn tiền COD' nhưng chatbot phân vào FAQ giao hàng, phải transfer agent; (2) **Tracking LEX không realtime** — khách hỏi 'đơn đang ở đâu' mà agent phải tra LEX CMS riêng, không tích hợp vào CRM; (3) **Thẩm quyền agent quá hẹp** — refund trên 50,000 VND phải escalate Tier-2, chờ 1–5 ngày, khách bức xúc. Agent muốn tự xử lý nhưng bị giới hạn ngưỡng."

**Q8. Nếu được thay đổi 1 điều trong quy trình Lazada hiện tại, anh/chị sẽ thay đổi gì? Tại sao?**

> "Tôi sẽ **mở rộng thẩm quyền CS Agent lên refund 200,000 VND** (từ ngưỡng hiện tại 50,000 VND) với điều kiện agent có kinh nghiệm >1 năm + QA score ≥85%. Lý do: 80% ticket Tier-2 là refund 50k–200k, chờ 1–5 ngày, trong khi agent đủ khả năng xử lý tại chỗ → giảm wait time cho khách, giảm workload Tier-2, tăng CSAT. Pilot thử nội bộ 3 tháng."

**Q9. Lazada có những hạn chế nào ảnh hưởng trực tiếp đến hiệu suất làm việc của anh/chị?**

> "Ba hạn chế lớn: (1) **CRM không tích hợp unified view** — agent phải mở 3–4 tab (CRM + tracking LEX + payment + chat log), tốn 10–20 phút gather info; (2) **Escalation rules cứng nhắc** — agent không có quyền refund >50k dù biết rõ vấn đề; (3) **CSAT survey gửi quá muộn** — thường 24h sau đóng ticket, khách không nhớ chi tiết → điểm CSAT không phản ánh đúng; nên gửi ngay sau resolved."

**Q10. Anh/chị xử lý thế nào khi có đơn Lazada bị hoàn trả, tranh chấp hoặc khiếu nại CSKH? Mô tả workflow thực tế.**

> "Khi receive ticket từ buyer: (1) Chatbot tạo ticket CRM; (2) ACD routing gán agent theo skill (issue type + giá trị đơn + khách VIP); (3) Agent xác minh danh tính + order; (4) Điều tra: check tracking LEX + payment record + chat log + policy KB; (5) Quyết định trong thẩm quyền: refund ≤50k, reship, coupon; (6) Nếu vượt thẩm quyền → escalate Tier-2 (Dispute/Tech/Finance) với case brief; (7) Agent đóng ticket + CSAT survey; (8) QA review CSAT thấp (<3 sao) → follow-up call. Agent xử lý trung bình 50–80 ticket/ngày, thời gian average handle time 8–12 phút/ticket."

---

## C. 10 Câu hỏi ĐỊNH LƯỢNG

### C1. 5 câu CẤU TRÚC (Multiple Choice)

**Q11.** Agent CS trung bình xử lý bao nhiêu ticket/ngày?
- [ ] < 20 ticket
- [ ] 20-50 ticket
- [x] 50-80 ticket *(CS Agent Lazada — hỗ trợ multichannel: chat + hotline + email)*
- [ ] 80-150 ticket
- [ ] > 150 ticket

**Q12.** Thời gian average handle time (AHT) trên 1 ticket CS?
- [ ] < 5 phút
- [ ] 5-10 phút
- [x] 8-15 phút *(bao gồm gather info + xử lý + đóng ticket)*
- [ ] 15-30 phút
- [ ] > 30 phút

**Q13.** Tỷ lệ ticket CS trên tổng số đơn hàng trên Lazada (CS ticket rate)?
- [ ] < 3%
- [ ] 3-5%
- [x] 5-10%
- [ ] 10-15%
- [ ] > 15%

**Q14.** CSAT score trung bình hiện tại (thang điểm 1–5)?
- [ ] < 3.0
- [ ] 3.0-3.5
- [x] 3.5-4.0 *(mục tiêu Lazada >3.8; AS-IS chốt đồ án 3,2/5 — xem doc 05 & Bảng 3.9)*
- [ ] 4.0-4.5
- [ ] > 4.5

**Q15.** Chi phí vận hành CS cho 1 ticket (nhân công + tool + overhead)?
- [ ] < 10,000 VND
- [ ] 10,000-20,000 VND
- [x] 15,000-25,000 VND *(bao gồm CS Agent labor + CRM + chatbot hosting)*
- [ ] 25,000-50,000 VND
- [ ] > 50,000 VND

### C2. 5 câu KHÔNG CẤU_TRÚC (Numeric Open)

**Q16.** Thời gian trung bình từ lúc buyer gửi ticket đến khi CS Agent nhận và bắt đầu xử lý (wait time)? → **~8 phút** (chat: 2–3 phút; hotline: 5–10 phút chờ IVR + queue; email: 2–4 giờ)

**Q17.** Tỷ lệ % ticket Tier-2 escalations (vượt thẩm quyền agent) trên tổng ticket? → **~20%** (chủ yếu refund 50k–200k + khiếu nại phức tạp)

**Q18.** Chi phí vận hành CS/trung bình cho 1 ticket (agent labor + tool + overhead)? → **~18,000 VND** (agent 12k + tool 3k + overhead 3k — chi phí trực tiếp theo người phỏng vấn; chi phí toàn phần/contact theo doc 05 là ~52,600 VND)

**Q19.** Lượng ticket CS tăng gấp bao nhiêu lần trong campaign 9.9/11.11/12.12? → **~3.5 lần** (ticket after-sale + khiếu nại giá + giao trễ tăng mạnh)

**Q20.** Tỷ lệ khách hàng trả lời CSAT survey sau khi đóng ticket? → **~30%** (chủ yếu qua app push notification; email rate thấp hơn ~15%)

---

## D. Bảng ghi chép kết quả giả định (Mock Results — 6 người trả lời)

### D1. Tóm tắt định tính

| ID | Vai trò | Q1 | Q2 | Q3 | Q4 | Q5 | Điểm nổi bật định tính |
|----|---------|----|----|----|----|----|------------------------|
| AG-01 | CS Agent (Chat) | 3 | 4 | 4 | 4 | 4 | "Mở 3–4 tab gather info, tốn 10–20 phút chỉ để tra cứu" |
| AG-02 | CS Agent (Hotline) | 3 | 4 | 3 | 4 | 4 | "Agent bị giới hạn 50k refund, 80% ticket Tier-2 là 50–200k" |
| CS-01 | CS Manager (người phỏng vấn) | 3 | 4 | 4 | 4 | 4 | "Mở rộng thẩm quyền agent lên 200k → giảm Tier-2 50%" |
| BY-01 | Buyer (chat support) | 3 | — | 3 | 3 | 4 | "Chatbot trả lời sai intent, phải chờ agent 5–10 phút" |
| BY-02 | Buyer (hotline) | 2 | — | 2 | 3 | 3 | "Giữ máy hotline 15 phút mới có agent nghe" |
| QA-01 | CS Quality Assurance | 4 | — | 3 | — | 4 | "CSAT survey gửi 24h sau → khách không nhớ, điểm không chính xác" |

### D2. Tóm tắt định lượng

| ID | Q11 (ticket/ngày) | Q12 (phút) | Q13 (%) | Q14 (CSAT) | Q15 (VND) | Q16 (phút) | Q17 (%) | Q18 (VND) | Q19 (lần) | Q20 (%) |
|----|-------------------|-----------|---------|-----------|-----------|-----------|---------|-----------|-----------|---------|
| AG-01 | 50-80 | 8-15 | 5-10% | 3.8 | 15-25K | 8 | 20 | 18,000 | 3.5 | 30 |
| AG-02 | 50-80 | 8-15 | 5-10% | 3.7 | 15-25K | 10 | 20 | 18,000 | 3.5 | 30 |
| CS-01 | 50-80 | 8-15 | 5-10% | 3.8 | 15-25K | 8 | 20 | 18,000 | 3.5 | 30 |
| BY-01 | — | — | — | — | — | 5-10 | — | — | — | — |
| BY-02 | — | — | — | — | — | 15+ | — | — | — | — |
| QA-01 | — | — | — | 3.8 | — | — | 20 | — | — | 30 |

### D3. Số liệu tổng hợp

| Metric | Giá trị trung bình (mock) | Ghi chú |
|--------|---------------------------|---------|
| CS ticket rate | ~7% (ticket / tổng đơn) | Khớp doc CS~5–10% |
| AHT (handle time) | ~11 phút/ticket | Bao gồm gather info + xử lý + đóng |
| Wait time (chat) | ~8 phút | Hotline 15 phút; email 2–4 giờ |
| Tier-2 escalation rate | ~20% | 80% là refund 50k–200k — giải pháp mở thẩm quyền |
| CSAT score | **3,2/5 (AS-IS chốt đồ án)** | Người phỏng vấn ước lượng 3.8; mục tiêu >3.8; peak campaign 9.9/11.11 giảm ~0.3 — khớp doc 05 & Bảng 3.9 |
| Cost per ticket | **~52,600 VND/contact (chi phí toàn phần)** | Người phỏng vấn ước tính chi phí trực tiếp ~18,000 (agent labor + tool + chatbot); chi phí toàn phần gồm overhead + escalation theo doc 05 |

---

## E. Nhận xét rút ra từ câu trả lời

1. **CRM thiếu unified view gây lãng phí thời gian gather info** — AG-01: mở 3–4 tab, 10–20 phút gather info/ticket. Giải pháp TO-BE: tích hợp CRM single-pane (order + tracking LEX + payment + chat log trên 1 màn hình); fraction gather time xuống 2–3 phút.
2. **Thẩm quyền agent 50k quá thấp gây ùn tắc Tier-2** — AG-02, CS-01: 80% Tier-2 là refund 50k–200k, chờ 1–5 ngày. Giải pháp: mở thẩm quyền lên 200k cho agent có kinh nghiệm + QA score ≥85%, giảm Tier-2 load 50%.
3. **CSAT survey gửi quá muộn (24h sau) gây mất chính xác** — QA-01: khách không nhớ chi tiết → CSAT không phản ánh đúng. Giải pháp: gửi survey ngay sau resolved + thông báo "phản hồi trong 2 giờ".
4. **Chatbot triage sai intent gây delay** — BY-01: chatbot trả lời sai, phải transfer agent, chờ thêm 5–10 phút. Giải pháp: cải thiện NLP intent classifier + human-in-the-loop cho edge cases.
5. **Ticket CS tăng 3.5x mùa sale nhưng nhân sự không tăng tương ứng** — CS-01: peak ticket 9.9/11.11 kèm CSAT giảm 0.3. Giải pháp: pre-hire seasonal agents + chatbot deflect rate mục tiêu 40% giảm workload agent.

**Dữ liệu này được sử dụng trong:**
- `docs/analysis/05-customer-service.md`
- `docs/analysis/comparison/05-customer-service.md`
- `docs/analysis/issue-register.md` (issues CS-01 đến CS-06)

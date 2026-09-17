# Bộ Phỏng vấn riêng — Quy trình 06: Marketing & Khuyến mãi (Campaign & Promotion)

## A. Mục đích phỏng vấn & Đối tượng

### Mục đích
Thu thập dữ liệu về **quy trình vận hành campaign & khuyến mãi Lazada VN** — từ lúc lập kế hoạch chiến dịch (9.9, 10.10, 11.11, 12.12, sinh nhật, brand day), duyệt ngân sách theo hạng mức (Dưới ngưỡng → CMO; trên ngưỡng → CFO; lớn → hội đồng), thiết kế creative + duyệt tuân thủ Legal, mở cổng seller đăng ký (7–14 ngày), kiểm tra điều kiện seller (điểm ≥4.0 sao, tỉ lệ hủy/ship trễ <5%), kiểm tra giá khuyến mãi tối thiểu (5–20%), giám sát realtime, xử lý sự cố (hết kho, sai giá, scam seller), post-campaign analysis (ROI, GMV vs mục tiêu), auto-renew.

### Thông tin người phỏng vấn
- **Họ tên (giả định):** Anh Vũ Quốc Bảo
- **Vai trò:** Senior Campaign Manager — phụ trách planning & operation cho Mega Campaigns (9.9, 11.11, 12.12) và Brand Days tại Lazada Việt Nam
- **Thâm niên:** 6 năm e-commerce marketing ops (2 năm Lazada Regional, 4 năm Lazada)
- **Kinh nghiệm liên quan:** Quản lý ngân sách campaign 100+ tỷ VND/năm; dựng công cụ eligibility check + price validation cho sellers; điều hành War Room xử lý sự cố mùa 11.11; xây dựng post-campaign ROI framework
- **Hình thức phỏng vấn:** Trực tuyến (Microsoft Teams), 60 phút, 10:00 ngày 16/08/2026

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

> "Tôi quản lý campaign nên quy trình của tôi khác — nhưng liên hệ với đơn hàng ở chỗ seller phải commit năng lực: (1) Marketing plan campaign + calendar; (2) Dự toán ngân sách (voucher, flash sale subsidy, ads, logistics subsidy); (3) Duyệt ngân sách theo hạng mức; (4) Creative + duyệt tuân thủ Legal; (5) Mở cổng seller đăng ký trên Campaign Hub (7–14 ngày); (6) Eligibility check: điểm ≥4.0 sao + tỉ lệ hủy/ship trễ <5%; (7) Price validation: giảm 5–20% tối thiểu, không cao hơn giá gốc; (8) Duyệt SKU (auto hoặc manual cho category nhạy cảm); (9) Launch đúng giờ; (10) Giám sát realtime GMV/volume + War Room xử lý sự cố; (11) Post-campaign analysis ROI; (12) Auto-renew. **Bước mất thời gian nhất là duyệt ngân sách** — trên ngưỡng phải trình CFO/CMO 3–7 ngày, campaign deadline chặt nhưng approval queue thủ công."

**Q7. Những khó khăn/lỗi thường gặp nhất khi thao tác trên Lazada là gì? (top 3)**

> "Top 3: (1) **Seller đăng ký SKU nhưng không duy trì tồn kho đủ** — bán cháy hàng giữa campaign, phải dừng SKU gây bức xúc buyer và giảm GMV; (2) **Price validation fail** — seller set giá khuyến mãi chỉ giảm 3% trong khi yêu cầu tối thiểu 5%, phải yêu cầu sửa, tạo loop; (3) **Scam seller khai báo giá gốc khống** — set giá gốc rồi giảm 50% để vào flash sale, phải kiểm tra lịch sử giá (price history) thủ công; chưa có tool auto-detect."

**Q8. Nếu được thay đổi 1 điều trong quy trình Lazada hiện tại, anh/chị sẽ thay đổi gì? Tại sao?**

> "Tôi sẽ **tự động hóa hoàn toàn approval budget theo hạng mức** bằng rule engine: dưới ngưỡng auto-approve + notify, trên ngưỡng mới trình CFO; tốt hơn nữa là kết nối với lịch campaign để pre-approve ngân sách chu kỳ (quarterly buffer). Lý do: hiện tại 70% budget approval là campaign thường dưới ngưỡng nhưng vẫn vào queue thủ công 3–7 ngày, làm trì hoãn toàn bộ timeline."

**Q9. Lazada có những hạn chế nào ảnh hưởng trực tiếp đến hiệu suất làm việc của anh/chị?**

> "Ba hạn chế lớn: (1) **Thiếu price history tool** — không auto-detect scam seller giả giá gốc, phải check thủ công → chậm 1–3 ngày duyệt SKU; (2) **Thiếu predicted volume/dữ liệu định lượng số** cho logistics team — marketing không được chia sẻ dự báo volume nên warehouse không chuẩn bị kịp, khớp với feedback của Ops; (3) **Thiếu integration giữa Campaign Hub và Seller Center** — seller đăng ký ở 1 nơi like flash sale slot, nhưng inventory sync không realtime, xảy ra over-subscription."

**Q10. Anh/chị xử lý thế nào khi có đơn Lazada bị hoàn trả, tranh chấp hoặc khiếu nại CSKH? Mô tả workflow thực tế.**

> "Trong campaign, khiếu nại xuất hiện ở 2 form: (1) **Buyer khiếu nại giá** — vào Bio đúng giờ nhưng giá không đúng như banner → CS gửi War Room review, truy tìm transaction log; (2) **Buyer khiếu nại shipping delay** — campaign volume quá tải LEX → limit Seller Center notification, gửi apology voucher 50–100k. Post-campaign, marketing phối hợp BI analyze return rate & dispute rate của từng SKU campaign để đánh giá quality của seller tham gia campaign kỳ sau."

---

## C. 10 Câu hỏi ĐỊNH LƯỢNG

### C1. 5 câu CẤU TRÚC (Multiple Choice)

**Q11.** Số lượng campaign marketing Lazada VN vận hành trung bình/tháng?
- [ ] 1-5 campaign
- [x] 5-10 campaign *(bao gồm flash sale hàng ngày + brand day + mega campaign)*
- [ ] 10-20 campaign
- [ ] 20-50 campaign
- [ ] > 50 campaign

**Q12.** Thời gian planning → launch trung bình cho 1 mega campaign (11.11)?
- [ ] < 2 tuần
- [ ] 2-4 tuần
- [ ] 4-6 tuần
- [x] 6-8 tuần *(11.11 planning bắt đầu từ giữa Q3)*
- [ ] > 8 tuần/Q4

**Q13.** Tỷ lệ seller bị từ chối đăng ký campaign (không đủ điều kiện) / tổng đăng ký?
- [ ] < 5%
- [ ] 5-10%
- [x] 10-20% *(thiếu điểm, tỉ lệ hủy/ship trễ >5%, sai giá)*
- [ ] 20-30%
- [ ] > 30%

**Q14.** Mức tăng GMV trung bình của campaign 11.11 so với ngày thường (số lần)?
- [ ] < 2 lần
- [ ] 2-3 lần
- [x] 3-5 lần *(11.11 Lazada GMV tăng trung bình 4–5x ngày thường)*
- [ ] 5-10 lần
- [ ] > 10 lần

**Q15.** Chi phí marketing trung bình/đơn hàng thu về được trong campaign (CAC — Customer Acquisition Cost)?
- [ ] < 10,000 VND
- [ ] 10,000-20,000 VND
- [x] 15,000-30,000 VND *(voucher + ads + flash sale subsidy chia tổng GMV)*
- [ ] 30,000-50,000 VND
- [ ] > 50,000 VND

### C2. 5 câu KHÔNG CẤU TRÚC (Numeric Open)

**Q16.** Thời gian trung bình từ lúc duyệt ngân sách → mở cổng seller đăng ký campaign? → **~7 ngày** (duyệt ngân sách 3–7 ngày + thiết kế creative + đảo nội dung tuân thủ 1–2 ngày song song)

**Q17.** Tỷ lệ % GMV từ campaign mỗi năm so với tổng GMV Lazada VN? → **~35%** (6 mega campaigns + flash sale hàng ngày đóng góp)

**Q18.** Chi phí marketing trung bình/đơn hàng campaign (subsidy + ads + voucher)? → **~22,000 VND/đơn** (hỗ trợ ước tính ROAS net)

**Q19.** Lượng đơn hàng trong 11.11 tăng gấp bao nhiêu lần so với ngày thường? → **~6 lần** (volume đơn trong ngày event so với ngày thường — ước lượng Marketing; warehouse LEX ghi nhận peak 10.000+ kiện/ngày vs 2.000 ngày thường, tương đương 5x — xem file 03)

**Q20.** Tỷ lệ phần trăm SKU tham gia campaign bị hết kho giữa chừng (out-of-stock)? → **~12%** (8–15% tùy category; FMCG + voucher hấp dẫn hết nhanh hơn)

---

## D. Bảng ghi chép kết quả giả định (Mock Results — 6 người trả lời)

### D1. Tóm tắt định tính

| ID | Vai trò | Q1 | Q2 | Q3 | Q4 | Q5 | Điểm nổi bật định tính |
|----|---------|----|----|----|----|----|------------------------|
| MK-01 | Campaign Manager (người phỏng vấn) | 3 | 4 | 4 | 4 | 4 | "70% budget approval dưới ngưỡng vẫn thủ công 3–7 ngày" |
| FN-01 | Finance Controller | 3 | — | 3 | — | 4 | "Approval queue thủ công vì thiếu rule engine theo hạng mức" |
| SL-01 | Seller (FMCG) | 4 | 4 | 4 | 4 | 3 | "Đăng ký SKU nhưng hết kho giữa campaign, bị dừng SKU" |
| SL-02 | Seller (Thời trang) | 3 | 4 | 3 | 4 | 3 | "Price validation fail loop: chỉ giảm 3% trong khi yêu cầu 5%" |
| CR-01 | Creative Team Lead | 3 | — | 3 | — | 3 | "Legal duyệt content thủ công 1–2 ngày, campaign gấp phải chờ" |
| OPS-01 | Warehouse Ops (như Q03) | 3 | 4 | 3 | 3 | 3 | "Không được chia sẻ predicted volume → chuẩn bị không kịp" |

### D2. Tóm tắt định lượng

| ID | Q11 (campaign/tháng) | Q12 (tuần) | Q13 (%) | Q14 (GMV lần) | Q15 (VND) | Q16 (ngày) | Q17 (%) | Q18 (VND) | Q19 (đơn lần) | Q20 (%) |
|----|----------------------|-----------|---------|---------------|-----------|-----------|---------|-----------|---------------|---------|
| MK-01 | 5-10 | 6-8 tuần | 10-20% | 3-5 | 15-30K | 7 | 35 | 22,000 | 6 | 12 |
| FN-01 | 5-10 | 6-8 | 10-20% | 3-5 | 15-30K | 7 | 35 | 22,000 | 6 | 12 |
| SL-01 | — | — | 5-10%*(rejected)* | — | — | — | — | — | — | — |
| SL-02 | — | — | 10-20% | — | — | — | — | — | — | — |
| CR-01 | 5-10 | 6-8 | 10-20% | 3-5 | 15-30K | 7 | 35 | 22,000 | 6 | 12 |
| OPS-01 | — | — | — | — | — | — | — | — | 6 | 15*(warehouse out-of-stock view)* |

### D3. Số liệu tổng hợp

| Metric | Giá trị trung bình (mock) | Ghi chú |
|--------|---------------------------|---------|
| Planning → launch (mega campaign) | ~7 tuần | 11.11 bắt đầu Q3; approval chiếm 3–7 ngày |
| Tỷ lệ seller bị từ chối | ~15% | Thiếu điểm / hủy ship trễ >5% / giá sai |
| GMV tăng campaign 11.11 | ~4x ngày thường | Khớp doc GMV surge post-sale |
| Volume đơn 11.11 | ~6x ngày thường *(ước lượng Marketing)* | OPS: warehouse peak 10.000+ kiện/ngày (≈ 5x so với 2.000 ngày thường) |
| Out-of-stock giữa campaign | ~12% | Hết kho → dừng SKU → mất GMV |
| CAC campaign | ~22,000 VND/đơn | Voucher + ads + subsidy |

---

## E. Nhận xét rút ra từ câu trả lời

1. **Approval ngân sách thủ công là bottleneck chính** — MK-01, FN-01: 70% budget dưới ngưỡng vẫn vào queue thủ công 3–7 ngày. Giải pháp TO-BE: rule engine auto-approve theo hạng mức + pre-approved quarterly buffer kết nối calendar.
2. **Thiếu predicted volume chia sẻ → warehouse không chuẩn bị kịp** — OPS-01: marketing không share volume forecast nên warehouse bị surprise (khớp feedback quy trình 03). Giải pháp: marketing → OPS forecast dashboard realtime, điều phối nhân sự & LEX capacity.
3. **Out-of-stock 12% giữa campaign gây mất GMV** — SL-01: seller bán cháy hàng, bị dừng SKU, buyer bức xúc. Giải pháp: yêu cầu seller commit inventory buffer trước launch + auto-flag SKU sắp hết kho để kích hoạt cảnh báo restock kịp thời.
4. **Price validation loop + scam seller giả giá gốc** — SL-02, MK-01: seller giảm 3% không đạt 5%, scam seller khai giá khống. Giải pháp: auto-validate realtime + price history check (AI detect fake base price trước khi duyệt SKU).
5. **Campaign marketing phải liên thông với 5 quy trình còn lại** — CS (khiếu nại giá/ship trễ), Warehouse (volume forecast), Dispute (SKU campaign dispute rate), Seller Management (eligibility), Order (GMV surge → SLA). Marketing không chỉ là quy trình đơn lẻ mà là catalyst của toàn bộ system load.

**Dữ liệu này được sử dụng trong:**
- `docs/analysis/06-marketing.md`
- `docs/analysis/comparison/06-marketing.md`
- `docs/analysis/issue-register.md` (issues MK-01 đến MK-06)

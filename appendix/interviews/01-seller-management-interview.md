# Bộ Phỏng vấn riêng — Quy trình 01: Quản lý Nhà bán hàng (Seller Onboarding & Lifecycle)

## A. Mục đích phỏng vấn & Đối tượng

### Mục đích
Thu thập dữ liệu về **toàn bộ vòng đời seller trên Lazada VN** — từ đăng ký KYC (cá nhân/doanh nghiệp/LazMall), auto-check hồ sơ, onboard education (Lazada University), phê duyệt listing, đến giám sát performance (Cancellation Rate ~5%, Late Shipment Rate ~5%), xử lý vi phạm (Warning → Delist → Suspend → Deactivate) và kháng cáo (3–7 ngày). *(Ghi chú số liệu: con số "thất bại lần đầu ~12%" trong bảng Q&A là ƯỚC LƯỢNG của seller theo góc nhìn đơn lẻ; con số chốt của đồ án là 20–25% theo phân tích toàn chuỗi — xem doc 09.)*

### Thông tin người phỏng vấn
- **Họ tên (giả định):** Chị Đỗ Thu Hà
- **Vai trò:** Trưởng nhóm Vận hành đối tác (Seller Operations Partner Lead) — chuyên gia vận hành phụ trách 400+ seller tầm trung & LazMall trên miền Bắc, Lazada Việt Nam
- **Thâm niên:** 6 năm làm marketplace operations (2 năm tại Sendo, 4 năm tại Lazada)
- **Kinh nghiệm liên quan:** Trực tiếp vận hành luồng KYC, giải quyết kháng cáo vi phạm, tư vấn seller nâng điểm chất lượng shop; tham gia xây dựng chính sách thang phạt Warning → Delist → Suspend
- **Hình thức phỏng vấn:** Trực tuyến (Microsoft Teams), 60 phút, 10:00 ngày 05/08/2026

---

## B. 10 Câu hỏi ĐỊNH TÍNH

### B1. 5 câu CẤU TRÚC (Thang đo Likert 1-5)

| # | Câu hỏi | 1 | 2 | 3 | 4 | 5 |
|---|---------|---|---|---|---|---|
| Q1 | Mức độ hài lòng với quy trình xử lý đơn hàng trên Lazada hiện tại? | | | | ✓ (4) | |
| Q2 | Quy trình đóng gói & bàn giao cho LEX/shipper có dễ thực hiện? | | | | ✓ (4) | |
| Q3 | Hệ thống notification của Lazada (đơn mới, deadline phản hồi) có hữu ích? | | | ✓ (3) | | |
| Q4 | Thời gian xử lý đơn (auto-cancel 24–48h, SLA LEX 2–5 ngày) có hợp lý? | | | | ✓ (4) | |
| Q5 | Quy trình hoàn trả & hoàn tiền trên Lazada có minh bạch & công bằng? | | | ✓ (3) | | |

### B2. 5 câu KHÔNG CẤU TRÚC (Câu hỏi mở)

**Q6. Anh/chị mô tả chi tiết các bước xử lý 1 đơn hàng Lazada kể từ lúc nhận thông báo trên Seller Center đến khi bàn giao kiện cho LEX? Bước nào mất thời gian nhất?**

> "Với seller bình thường (LGS — Logistics by Seller), luồng là: nhận thông báo đơn mới trên Seller Center → seller bấm 'Chuẩn bị hàng' (accept) trong SLA 24–48h → đóng gói + in waybill từ Seller Center → chọn lịch pickup trên LEX CMS hoặc chờ LEX đến điểm gom → LEX quét mã nhận hàng → kiện đi sorting center. Bước mất thời gian nhất là **chờ pickup của LEX** — cắt giờ lấy hàng (cut-off) cố định, seller ở tỉnh phải chờ tới chiều hoặc hôm sau, trong khi đơn đã sẵn sàng từ sáng."

**Q7. Những khó khăn/lỗi thường gặp nhất khi thao tác trên Lazada là gì? (top 3)**

> "Top 3 tôi gặp nhiều nhất: (1) **Seller không bấm accept đúng hạn** → đơn bị auto-cancel khi hết 24–48h, ghi nhận vào Cancellation Rate và làm hỏng điểm chất lượng shop; (2) **Khai báo thông tin KYC sai lệch** — seller cá nhân nhập sai MST hoặc upload CCCD mờ, bị OCR fail phải bổ sung hồ sơ nhiều lần, làm kéo dài 1–3 ngày review; (3) **Bỏ sót notification phản hồi hoàn trả 48h** — seller để quá hạn nên hệ thống auto-approve, mất tiền oan."

**Q8. Nếu được thay đổi 1 điều trong quy trình Lazada hiện tại, anh/chị sẽ thay đổi gì? Tại sao?**

> "Tôi sẽ thay đổi **cơ chế auto-cancel 24–48h** thành cơ chế linh hoạt theo lịch sử seller: seller chuyên nghiệp có tỷ lệ accept cao được gia hạn dài hơn hoặc ưu tiên pickup sớm; seller mới bị siết hơn. Lý do: hiện tại auto-cancel là gánh nặng lớn nhất với chỉ số Cancellation Rate của seller nhỏ, họ vừa chưa quen vận hành vừa bị trừ điểm, tạo vòng xoáy khó thoát."

**Q9. Lazada có những hạn chế nào ảnh hưởng trực tiếp đến hiệu suất làm việc của anh/chị?**

> "Hạn chế rõ nhất là **màn hình Performance Dashboard tách rời** — seller phải tự theo dõi nhiều chỉ số (Cancellation Rate, Late Shipment Rate, Order Defect Rate) trên nhiều trang, không có cảnh báo tổng hợp 'bạn sắp chạm ngưỡng 5%'. Khi seller vi phạm, chúng tôi phải tư vấn thủ công từng shop. Ngoài ra, luồng kháng cáo 3–7 ngày làm việc khá lâu với seller bị treo — họ rất sốt ruột."

**Q10. Anh/chị xử lý thế nào khi có đơn Lazada bị hoàn trả, tranh chấp hoặc khiếu nại CSKH? Mô tả workflow thực tế.**

> "Khi seller bị khiếu nại, hệ thống gửi notification + email yêu cầu phản hồi trong 48h kèm bằng chứng. Nếu seller không phản hồi, hệ thống auto-approve nghiêng về buyer. Với vi phạm performance (hủy đơn quá 5%, ship trễ), Compliance xử lý theo thang Warning → Delist → Suspend; seller có thể kháng cáo trong 7 ngày qua Seller Center Appeal. Với shop bị treo nặng, seller phải đăng ký lại (re-register) — luồng KYC mới hoàn toàn."

---

## C. 10 Câu hỏi ĐỊNH LƯỢNG

### C1. 5 câu CẤU TRỤC (Multiple Choice)

**Q11.** Trung bình các seller trong phạm vi phụ trách xử lý bao nhiêu đơn Lazada/ngày?
- [ ] < 10 đơn
- [ ] 10-50 đơn
- [x] 50-100 đơn *(đa số seller tầm trung)*
- [ ] 100-500 đơn
- [ ] > 500 đơn

**Q12.** Thời gian trung bình để đóng gói + dán waybill 1 đơn (seller-arranged)?
- [ ] < 5 phút
- [x] 5-15 phút
- [ ] 15-30 phút
- [ ] 30-60 phút
- [ ] > 60 phút

**Q13.** Tỷ lệ đơn giao thất bại lần đầu/hoàn trả trung bình của seller trong phạm vi?
- [ ] < 2%
- [ ] 2-5%
- [x] 5-10%
- [ ] 10-20%
- [ ] > 20%

**Q14.** Số lần LEX/shipper pickup trung bình/tuần tại các seller LGS?
- [ ] 1-2 lần
- [x] 3-5 lần *(thành phố lớn có thể mỗi ngày)*
- [ ] 6-10 lần
- [ ] Hàng ngày
- [ ] Nhiều hơn 1 lần/ngày

**Q15.** Chi phí đóng gói trung bình/đơn (bao bì + băng keo + xốp + in waybill)?
- [ ] < 3,000 VND
- [x] 3,000-5,000 VND
- [ ] 5,000-10,000 VND
- [ ] 10,000-20,000 VND
- [ ] > 20,000 VND

### C2. 5 câu KHÔNG CẤU TRÚC (Numeric Open)

**Q16.** Thời gian trung bình từ lúc Lazada báo đơn mới đến khi LEX quét mã nhận hàng (pickup xong)? → **~14 giờ** (seller accept trung bình 4h + chờ pickup 8–12h tùy tuyến)

**Q17.** Tỷ lệ % đơn giao thành công ngay lần giao đầu tiên của các seller? → **~88%** (thất bại lần đầu ~12% — ước lượng seller; con số chốt đồ án 20–25% toàn chuỗi)

**Q18.** Chi phí vận hành biên/đơn mà seller phải chịu? → **~6,500 VND** (đóng gói 4k + nhân công 2k + điện nước/hao hụt 0.5k)

**Q19.** Lượng đơn xử lý trong tháng cao điểm campaign (9.9, 11.11, 12.12) tăng gấp bao nhiêu lần? → **~4 lần** (seller tầm trung; LazMall có thể 6–8 lần)

**Q20.** Thời gian trung bình hoàn tất 1 yêu cầu hoàn trả/hoàn tiền? → **~7 ngày** (auto-approve nhanh 1–2 ngày với đơn giá trị thấp; có inspection thì 5–7 ngày)

---

## D. Bảng ghi chép kết quả giả định (Mock Results — 6 người trả lời)

### D1. Tóm tắt định tính

| ID | Vai trò | Q1 | Q2 | Q3 | Q4 | Q5 | Điểm nổi bật định tính |
|----|---------|----|----|----|----|----|------------------------|
| SL-01 | Seller cá nhân nhỏ | 3 | 4 | 2 | 3 | 3 | "Toàn quên bấm accept, đơn auto-cancel, điểm shop tụt" |
| SL-02 | Seller doanh nghiệp vừa | 4 | 4 | 4 | 4 | 3 | "KYC doanh nghiệp phải bổ sung hồ sơ 2 lần vì OCR fail" |
| SL-03 | Seller LazMall | 4 | 4 | 3 | 4 | 4 | "Kháng cáo treo shop 7 ngày quá lâu, thiệt hại doanh thu" |
| SL-04 | Seller cá nhân (mới) | 2 | 3 | 3 | 2 | 3 | "Không biết ngưỡng 5% hủy đơn, không có cảnh báo trước" |
| OP-01 | Seller Ops Partner (người được phỏng vấn) | 4 | 4 | 3 | 4 | 3 | "Dashboard chỉ số rời rạc, tư vấn thủ công từng shop" |
| CP-01 | Compliance Staff | 3 | — | 3 | — | — | "60% kháng cáo thiếu bằng chứng, phải yêu cầu bổ sung" |

### D2. Tóm tắt định lượng

| ID | Q11 (đơn) | Q12 (phút) | Q13 (%) | Q14 (lần/tuần) | Q15 (VND) | Q16 (h) | Q17 (%) | Q18 (VND) | Q19 (lần) | Q20 (ngày) |
|----|-----------|-----------|---------|----------------|-----------|---------|---------|-----------|-----------|-----------|
| SL-01 | 10-50 | 15-30 | 10-20% | 3-5 | 3-5K | 20 | 85 | 6,000 | 3 | 8 |
| SL-02 | 50-100 | 5-15 | 5-10% | 3-5 | 3-5K | 12 | 90 | 5,500 | 4 | 6 |
| SL-03 | 100-500 | 5-15 | 2-5% | 6-10 | 3-5K | 8 | 93 | 5,000 | 6 | 5 |
| SL-04 | 10-50 | 15-30 | 10-20% | 1-2 | 3-5K | 26 | 82 | 7,000 | 3 | 9 |
| OP-01 | 50-100 | 5-15 | 5-10% | 3-5 | 3-5K | 14 | 88 | 6,500 | 4 | 7 |
| CP-01 | — | — | — | — | — | — | — | — | — | — |

### D3. Số liệu tổng hợp

| Metric | Giá trị trung bình (mock) | Ghi chú |
|--------|---------------------------|---------|
| Seller accept → LEX pickup | ~14 giờ | Khớp doc: accept trong 24–48h + pickup theo cut-off |
| Tỷ lệ giao thất bại lần đầu | ~12% | Ước lượng seller; đồ án chốt 20–25% toàn chuỗi (doc 09) |
| Chi phí đóng gói | 3,000–5,000 VND | Khớp doc 03 (Xử lý Đơn hàng Online): 5.000 VND/đơn (Đóng gói — Seller chịu); bảng chi phí biên Bảng 3.5 |
| Chi phí vận hành biên/đơn | ~6,000 VND | Chưa tính phí ship, hoa hồng |
| Thời gian hoàn tất hoàn trả | ~7 ngày | Khớp doc 1–15 ngày tùy phương thức refund |

---

## E. Nhận xét rút ra từ câu trả lời

1. **Auto-cancel 24–48h là điểm đau lớn nhất với seller nhỏ** — SL-01, SL-04 để quên accept → đơn auto-cancel → Cancellation Rate chạm ngưỡng ~5% → bị phạt. Xác nhận waste hold time + cần cảnh báo proactive (nudge trước deadline) và chính sách accept linh hoạt theo lịch sử seller.
2. **KYC bổ sung hồ sơ nhiều vòng do OCR fail** — SL-02 phải bổ sung 2 lần (giấy tờ mờ, MST sai). Xác nhận waste loop ở gateway G2/G3; giải pháp: hướng dẫn chụp hồ sơ chuẩn ngay tại form + auto-check theo real-time.
3. **Performance Dashboard rời rạc, thiếu cảnh báo ngưỡng** — OP-01 xác nhận seller không nhận biết sớm nguy cơ chạm 5%; giải pháp: alert tổng hợp + cảnh báo đỏ trước ngưỡng.
4. **Kháng cáo 7 ngày gây thiệt hại doanh thu** — SL-03: shop bị treo 7 ngày mất doanh thu; giải pháp: ưu tiên queue kháng cáo shop đang hoạt động, xử lý trong 2–3 ngày.
5. **Notification kém hiệu quả với seller mới** — SL-04 không biết ngưỡng phạt; giải pháp: onboarding interactive + checklist bắt buộc trước khi listing (liên kết với Lazada University).

**Dữ liệu này được sử dụng trong:**
- `docs/analysis/01-seller-management.md`
- `docs/analysis/comparison/01-seller-management.md`
- `docs/analysis/issue-register.md` (issues SM-01 đến SM-05)

# Bộ Phỏng vấn riêng — Quy trình 09: Logistics & Delivery (Chuỗi cung ứng Last-mile)

## A. Mục đích phỏng vấn & Đối tượng

### Mục đích
Thu thập dữ liệu về **toàn bộ chuỗi logistics & delivery trên Lazada VN** — từ lúc seller đóng gói & bàn giao kiện, qua scheduling pickup, hub sorting tại trung tâm phân loại, quá trình transit liên tỉnh, giao hàng lần cuối (last-mile delivery) đến proof of delivery (POD). Phỏng vấn tập trung xác định điểm nghẽn gây ra thời gian giao 3–5 ngày (nội đô) / 5–7 ngày (tỉnh), tỷ lệ giao thành công lần đầu ~85% (theo LEX; đồ án chốt 75–80% toàn chuỗi — xem doc 09 & Bảng 3.13), tỷ lệ hoàn trả 8–12%, quy trình sorting hub còn thủ công và thiếu GPS tracking real-time.

### Thông tin người được phỏng vấn
- **Họ tên (giả định):** Anh Phạm Quốc Huy
- **Vai trò:** Trưởng phòng Vận hành Logistics (Logistics Operations Manager) — quản lý mạng lưới hub sorting + đội ngũ last-mile delivery tại miền Nam, Lazada Express (LEX)
- **Thâm niên:** 7 năm trong ngành logistics e-commerce (2 năm tại GHN Express, 1 năm tại Viettel Post, 4 năm tại Lazada/LEX)
- **Kinh nghiệm liên quan:** Trực tiếp vận hành 12 hub sorting tại TP.HCM & Bình Dương, quản lý đội ngũ 200+ shipper last-mile; tham gia triển khai chương trình pilot drone delivery tại Quận 7; xây dựng KPI SLA cho đội ngũ giao hàng
- **Hình thức phỏng vấn:** Trực tiếp (Lazada Office, Q.7 TP.HCM), 75 phút, 09:00 ngày 08/08/2026

---

## B. 10 Câu hỏi ĐỊNH TÍNH

### B1. 5 câu CẤU TRÚC (Thang đo Likert 1-5)

| # | Câu hỏi | 1 | 2 | 3 | 4 | 5 |
|---|---------|---|---|---|---|---|
| Q1 | Mức độ hài lòng với hiệu suất giao hàng last-mile hiện tại của LEX? | | | ✓ (3) | | |
| Q2 | Quy trình pickup scheduling & dispatch đơn hàng có hiệu quả? | | | ✓ (3) | | |
| Q3 | Hệ thống tracking & quản lý đơn hàng có đủ thông tin real-time? | | | | ✓ (4) | |
| Q4 | Tỷ lệ giao thành công lần đầu (~85%) có đạt yêu cầu? | | | | ✓ (4) | |
| Q5 | Quy trình proof of delivery (POD) có minh bạch & chính xác? | | | | | ✓ (5) |

### B2. 5 câu KHÔNG CẤU TRÚC (Câu hỏi mở)

**Q6. Anh mô tả chi tiết quy trình từ lúc kiện hàng được nhận tại hub sorting LEX cho đến khi shipper last-mile giao tận tay khách hàng. Giai đoạn nào gây ùn tắc nhất?**

> "Luồng thực tế tại hub TP.HCM: kiện đến hub từ warehouse/seller drop-off → nhân viên quét barcode phân loại (sorting) theo tuyến quận/huyện → xếp lên pallet theo tuyến → loader lên xe trung chuyển (linehaul) hoặc chuyển thẳng cho shipper last-mile tùy theo khoảng cách → shipper quét nhận kiện (out-for-delivery) → shipper giao theo route được assign trên app LEX → giao thành công thì quét POD (ảnh + chữ ký số) hoặc giao thất bại thì ghi lý do (khách không nhận, sai địa chỉ, v.v.). **Giai đoạn ùn tắc nhất là hub sorting** — cao điểm 9.9/11.11, throughput hub đạt 150% capacity, nhân viên phải overtime 2–3 giờ mỗi ngày, tỷ lệ sorting nhầm (mis-sort) tăng từ ~2% lên ~5%, kiện giao sai tuyến phải quay đầu hub → mất thêm 1–2 ngày."

**Q7. Những khó khăn/lỗi thường gặp nhất trong vận hành logistics hàng ngày? (top 3)**

> "Top 3: (1) **Mis-sort tại hub** — nhân viên xếp kiện sai tuyến do barcode scan lỗi hoặc human error, kiện giao nhầm quận rồi phải reverse logistics quay về hub → mất thêm 1–2 ngày & tăng chi phí; (2) **Địa chỉ khách hàng sai hoặc không rõ** — đặc biệt ở vùng ven ngoại thành, shipper mất 15–30 phút mỗi đơn để tìm đường, gọi điện xác nhận, tỷ lệ giao thất bại lần đầu khoảng 12–15% phần lớn do lý do này; (3) **Thiếu GPS real-time trên shipper** — hiện tại chỉ cập nhật vị trí khi shipper quét barcode (scan-in/out), không track được shipper đang ở đâu giữa các lần quét → customer service không trả lời chính xác 'shipper đang ở đâu' cho khách."

**Q8. Nếu được thay đổi 1 điều trong quy trình logistics hiện tại, anh sẽ thay đổi gì? Tại sao?**

> "Tôi sẽ triển khai **hệ thống GPS real-time tracking trên toàn bộ đội ngũ shipper** kết hợp với **AI route optimization**. Hiện tại mỗi shipper nhận 40–60 kiện/ngày, tự quyết định thứ tự giao dựa trên kinh nghiệm cá nhân → quãng đường giao hàng thường dài hơn 20–30% so với optimal route. Nếu có AI tối ưu route + GPS real-time, tôi ước tính có thể giảm thời gian giao trung bình 1.5–2 giờ/ngày, tăng số đơn giao được 15–20%, đồng thời customer service có thể track shipper real-time để trả lời khách."

**Q9. LEX có những hạn chế nào ảnh hưởng trực tiếp đến hiệu suất giao hàng & trải nghiệm khách hàng?**

> "Hạn chế lớn nhất là **quy trình sorting hub còn thủ công** — nhân viên scan barcode từng kiện một, phân loại thủ công theo tuyến, không có conveyor belt tự động hay sorting system hỗ trợ. Hubs mới ở ngoại thành còn thiếu cơ sở hạ tầng. Hạn chế thứ hai là **thời gian transit liên tỉnh chậm** — kiện từ TP.HCM ra Hà Nội mất 2–3 ngày do tuyến đường bộ, không có air freight option cho đơn thường. Hạn chế thứ ba là **không có predictive ETA cho khách** — khách chỉ thấy 'đang giao' hoặc 'giao trong ngày' chứ không có ETA chính xác đến giờ."

**Q10. Anh mô tả workflow xử lý khi kiện hàng bị hư hỏng, mất hoặc khách từ chối nhận (delivery failure)?**

> "Khi shipper giao thất bại: shipper quét 'delivery failed' trên app kèm lý do (khách từ chối, hàng hư, sai địa chỉ, v.p.) + ảnh hiện trường. Hệ thống tự động chuyển trạng thái đơn → tạo ticket CSKH notify seller & buyer trong 24h. Nếu khách từ chối, seller có 48h để xác nhận hoàn hàng hoặc đồng ý hoàn tiền. Hàng hoàn quay về hub bằng shipper last-mile → hub nhận + scan reverse → chuyển về seller hoặc warehouse tùy theo chính sách. Với case mất hàng/hư hỏng, quy trình khiếu nại qua dashboard seller, kết quả trong 5–7 ngày. **Vấn đề lớn nhất là thiếu khả năng theo dõi real-time** — seller không biết kiện đang ở giai đoạn nào, phải gọi hotline LEX hỏi thủ công."

---

## C. 10 Câu hỏi ĐỊNH LƯỢNG

### C1. 5 câu CẤU TRỤC (Multiple Choice)

**Q11.** Thời gian trung bình từ lúc kiện nhập hub đến khi shipper last-mile nhận để giao?
- [ ] < 2 giờ
- [ ] 2-4 giờ
- [x] 4-8 giờ *(sorting hub mất 2–3 giờ, dispatch theo ca)*
- [ ] 8-12 giờ
- [ ] > 12 giờ

**Q12.** Tỷ lệ mis-sort (kiện giao sai tuyến) tại hub trung bình hàng tháng?
- [ ] < 1%
- [x] 1-3% *(ngày thường); 3-5% (cao điểm)*
- [ ] 3-5%
- [ ] 5-8%
- [ ] > 8%

**Q13.** Số lượng kiện average xử lý/ngày/hub TP.HCM?
- [ ] < 1,000 kiện
- [ ] 1,000-3,000 kiện
- [x] 3,000-5,000 kiện *(hub lớn tại Q7 Bình Thạnh)*
- [ ] 5,000-10,000 kiện
- [ ] > 10,000 kiện

**Q14.** Lý do phổ biến nhất gây ra giao hàng thất bại lần đầu?
- [ ] Khách không nghe điện thoại
- [x] Địa chỉ sai/không rõ (40%)
- [ ] Hàng hư/hỏng (20%)
- [ ] Khách không muốn nhận (25%)
- [ ] Lý do khác (15%)

**Q15.** Chi phí logistics trung bình/đơn (bao gồm hub sorting + linehaul + last-mile)?
- [ ] < 10,000 VND
- [ ] 10,000-15,000 VND
- [x] 15,000-25,000 VND *(metro); 25,000-40,000 VND (tỉnh)*
- [ ] 25,000-40,000 VND
- [ ] > 40,000 VND

### C2. 5 câu KHÔNG CẤU TRÚC (Numeric Open)

**Q16.** Tỷ lệ giao thành công lần đầu (first-attempt delivery success rate) trung bình toàn mạng LEX? → **~85%** (15% giao thất bại lần đầu — góc nhìn LEX; con số chốt đồ án 20–25% thất bại / 75–80% thành công toàn chuỗi)

**Q17.** Số kiện sorting trung bình/giờ/nhân viên hub? → **~120 kiện/giờ** (bằng tay với barcode scanner; conveyor belt có thể đạt 300+ kiện/giờ)

**Q18.** Thời gian transit trung bình từ TP.HCM → Hà Nội cho đơn standard? → **2–3 ngày** (đường bộ; express 1–2 ngày nhưng phí gấp 2–3 lần)

**Q19.** Số lượng shipper last-mile trung bình quản lý bởi 1 team leader? → **25–30 shipper** (tỷ lệ team leader:shipper ~ 1:28)

**Q20.** Tỷ lệ hoàn trả (return rate) đối với đơn logistics LEX trung bình? → **8–12%** (phần lớn do giao sai/sai mô tả sản phẩm; khớp data BPMN 8–12%)

---

## D. Bảng ghi chép kết quả giả định (Mock Results — 6 người trả lời)

### D1. Tóm tắt định tính

| ID | Vai trò | Q1 | Q2 | Q3 | Q4 | Q5 | Điểm nổi bật định tính |
|----|---------|----|----|----|----|----|------------------------|
| LG-01 | Hub Manager Q7 | 3 | 3 | 4 | 3 | 5 | "Sorting hub thủ công, cao điểm nhân viên overtime 3h/ngày, mis-sort tăng 2.5x" |
| LG-02 | Shipper Last-mile | 3 | 3 | 2 | 4 | 4 | "Không có GPS real-time, tự chọn route, mất 30 phút/đơn tìm nhà khách ngoại thành" |
| LG-03 | CSKH Logistics | 4 | 3 | 4 | 3 | 5 | "Khách gọi hỏi 'shipper đang đâu' mà không trả lời được, chỉ biết 'đang giao'" |
| LG-04 | Warehouse Lead | 3 | 4 | 3 | 3 | 4 | "Kiện transit liên tỉnh mất 2–3 ngày, không có air freight option cho đơn thường" |
| LD-01 | Logistics Ops Manager (được phỏng vấn) | 3 | 3 | 4 | 4 | 5 | "AI route optimization + GPS real-time sẽ giảm 20–30% quãng đường giao" |
| CS-01 | Customer Service Lead | 3 | 2 | 3 | 3 | 4 | "40% khiếu nại là 'không biết kiện ở đâu' + 'giao sai địa chỉ'" |

### D2. Tóm tắt định lượng

| ID | Q11 (giờ) | Q12 (%) | Q13 (kiện) | Q14 (%) | Q15 (VND) | Q16 (%) | Q17 (kiện/h) | Q18 (ngày) | Q19 (shipper) | Q20 (%) |
|----|-----------|---------|------------|---------|-----------|---------|-------------|------------|--------------|---------|
| LG-01 | 4-8 | 3-5% | 3,000-5,000 | 40% | 15-25K | 84 | 100 | 2.5 | 28 | 10 |
| LG-02 | 4-8 | 1-3% | — | 45% | 15-25K | 83 | — | — | — | 12 |
| LG-03 | — | — | — | 40% | — | 86 | — | — | — | 9 |
| LG-04 | 4-8 | 2-3% | 3,000-5,000 | 35% | 25-40K | 87 | 130 | 3 | 25 | 8 |
| LD-01 | 4-8 | 2% | 5,000+ | 40% | 15-25K | 85 | 120 | 2 | 30 | 10 |
| CS-01 | — | — | — | 42% | — | 85 | — | — | — | 11 |

### D3. Số liệu tổng hợp

| Metric | Giá trị trung bình (mock) | Ghi chú |
|--------|---------------------------|---------|
| First-attempt delivery success | ~85% | 15% giao thất bại lần đầu (góc nhìn LEX; đồ án chốt 75–80% toàn chuỗi) |
| Tỷ lệ mis-sort hub | 2–3% (ngày thường), 3–5% (cao điểm) | Gây reverse logistics, mất 1–2 ngày |
| Thời gian transit HCM → HN | 2–3 ngày | Không air freight cho đơn standard |
| Chi phí logistics/đơn (metro) | 15,000–25,000 VND | Province: 25,000–40,000 VND |
| Tỷ lệ hoàn trả | 8–12% | Khớp data BPMN |
| Sorting throughput (tay) | ~120 kiện/giờ/người | Conveyor belt: 300+ kiện/giờ |
| Lý do giao thất bại #1 | Địa chỉ sai/không rõ (40%) | Tỷ lệ shipper dành 30 phút/đơn tìm nhà |

---

## E. Nhận xét rút ra từ câu trả lời

1. **Hub sorting thủ công là bottleneck lớn nhất gây ùn tắc** — LG-01 xác nhận cao điểm throughput hub đạt 150% capacity, mis-sort tăng 2.5x (từ 2% lên 5%). Xác nhận waste processing time + cần đầu tư conveyor belt + automated sorting system để tăng throughput gấp 2–3 lần và giảm mis-sort xuống < 1%.

2. **Thiếu GPS real-time tracking gây mất trải nghiệm khách hàng** — LG-02, LG-03, CS-01 đều xác nhận: shipper không được track vị trí real-time, CSKH không trả lời được "shipper đang ở đâu". 40% khiếu nại CSKH liên quan đến "không biết kiện ở đâu". Giải pháp: GPS tracking trên app shipper + tích hợp vào customer-facing tracking page.

3. **AI route optimization có tiềm năng giảm 20–30% quãng đường giao** — LD-01 ước tính shipper tự chọn route hiện nay dài hơn optimal 20–30%, mỗi shipper mất 1.5–2 giờ/ngày cho quãng đường thừa. Giải pháp: AI route optimization gợi ý route optimal theo real-time traffic, giảm time-per-delivery 15–20%.

4. **Địa chỉ sai là nguyên nhân #1 gây giao thất bại (40%)** — LG-02, LD-01, CS-01 đồng nhất: 40% giao thất bại do địa chỉ sai/không rõ. Giải pháp: address validation real-time tại checkout + chuyển sang smart pin (pin GPS location) + verify địa chỉ bằng AI trước khi dispatch.

5. **Thời gian transit liên tỉnh 2–3 ngày cần cải thiện** — LG-04 xác nhận không có air freight option cho đơn standard, gây chậm so với đối thủ. Giải pháp: piloting drone delivery cho short-distance + partnership với airlines cho express tier + predictive ETA ML để khách biết chính xác khi nào nhận hàng.

**Dữ liệu này được sử dụng trong:**
- `docs/analysis/09-logistics-delivery.md`
- `docs/analysis/comparison/09-logistics-delivery.md`
- `docs/analysis/issue-register.md` (issues LG-01 đến LG-07)

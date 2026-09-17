# Bộ Phỏng vấn riêng — Quy trình 03: Xử lý Đơn hàng Online (Order Processing)

## A. Mục đích phỏng vấn & Đối tượng

### Mục đích
Thu thập dữ liệu về quy trình **xử lý đơn hàng Lazada từ lúc buyer đặt hàng đến khi LEX giao thành công và COD settle** — tập trung vào thời gian accept/reject đơn của seller (SLA 24–48h), quy trình đóng gói/waybill, pickup scheduling của LEX/3PL, tỷ lệ giao thất bại lần đầu (~15% theo LEX, ~20–25% chốt toàn chuỗi), split shipment, QC inspection tại warehouse, COD settlement (thu ngay + đối soát tuần), và chi phí vận hành biên.

### Thông tin người phỏng vấn
- **Họ tên (giả định):** Anh Lê Hoàng Nam
- **Vai trò:** Head of Fulfillment Operations — phụ trách vận hành kho LEX Hà Nội & TP.HCM, quản lý 150+ nhân sự warehouse + QC + logistics coordination cho Lazada VN
- **Thâm niên:** 5 năm logistics marketplace (2 năm Lazada Warehouse, 3 năm Lazada LEX)
- **Kinh nghiệm liên quan:** Trực tiếp quản lý WMS, QC inspection, packing station, LEX pickup scheduling, COD settlement reconciliation; từng pilot FBL (Fulfillment by Lazada) với 50 seller Hà Nội
- **Hình thức phỏng vấn:** Trực tiếp tại Warehouse LEX Hà Nội, 65 phút, 09:00 ngày 10/08/2026

---

## B. 10 Câu hỏi ĐỊNH TÍNH

### B1. 5 câu CẤU TRÚC (Thang đo Likert 1-5)

| # | Câu hỏi | 1 | 2 | 3 | 4 | 5 |
|---|---------|---|---|---|---|---|
| Q1 | Mức độ hài lòng với quy trình xử lý đơn hàng trên Lazada hiện tại? | | | | ✓ (4) | |
| Q2 | Quy trình đóng gói & bàn giao cho LEX/shipper có dễ thực hiện? | | | ✓ (3) | | |
| Q3 | Hệ thống notification của Lazada có hữu ích (đúng lúc, không spam)? | | | ✓ (3) | | |
| Q4 | Thời gian xử lý đơn (auto-cancel 24–48h, SLA giao LEX 2–5 ngày) có hợp lý? | | | ✓ (3) | | |
| Q5 | Quy trình hoàn trả & hoàn tiền trên Lazada có minh bạch & công bằng? | | | ✓ (3) | | |

### B2. 5 câu KHÔNG CẤU TRÚC (Câu hỏi mở)

**Q6. Anh/chị mô tả chi tiết các bước xử lý 1 đơn hàng Lazada kể từ lúc nhận thông báo trên Seller Center đến khi bàn giao kiện cho LEX? Bước nào mất thời gian nhất?**

> "Luồng từ warehouse perspective: (1) Seller bấm accept đơn → (2) Tạo pickup request trên LEX CMS → (3) Warehouse nhận kiện pickup tại điểm gom hoặc FBL → (4) QC inspection — scan barcode, đối chiếu SKU/số lượng/tình trạng/hạn dùng với order details trên WMS → (5) Packing station — đóng gói đúng chuẩn (thùng cứng, xốp chống vỡ) → (6) Label — in nhãn vận đơn barcode từ WMS → (7) Handoff cho LEX/3PL — quét mã chuyển trạng thái. Bước **mất thời gian nhất là QC inspection** — 5–15 phút/kiện, đặc biệt hàng điện tử cần check tính năng + phụ kiện đầy đủ; mùa sale volume gấp 4–5 lần nên queue chờ QC tắc nghẽn."

**Q7. Những khó khăn/lỗi thường gặp nhất khi thao tác trên Lazada là gì? (top 3)**

> "Top 3: (1) **Không có tracking auto-sync giữa LEX CMS và Seller Center** — warehouse quét mã nhưng seller không thấy cập nhật realtime, buyer hỏi seller không trả lời được; (2) **Waybill in tay có barcode lỗi hoặc in nhòe** — QC scan fail phải in lại, tắc nghẽn packing station; (3) **Split shipment tự động không thông báo seller rõ ràng** — đơn 3 item bị tách thành 2 kiện giao riêng, seller không biết để chuẩn bị hàng, kiện thứ 2 bị delay."

**Q8. Nếu được thay đổi 1 điều trong quy trình Lazada hiện tại, anh/chị sẽ thay đổi gì? Tại sao?**

> "Tôi sẽ **tự động hóa QC inspection theo tier** — hàng shop có điểm chất lượng cao (>4.5 sao, tỷ lệ return <2%) thì skip QC, chỉ random sampling; chỉ shop mới/vi phạm mới QC 100%. Hiện tại QC 100% tất cả đơn gây tắc nghẽn nghiêm trọng mùa sale. Pilot nhỏ tại warehouse Hà Nội cho thấy skip QC với shop uy tín giảm throughput time 30% mà tỷ lệ lỗi không tăng."

**Q9. Lazada có những hạn chế nào ảnh hưởng trực tiếp đến hiệu suất làm việc của anh/chị?**

> "Ba hạn chế lớn: (1) **WMS không tích hợp realtime với LEX CMS** — phải đồng bộ batch mỗi 30 phút, gây delay tracking; (2) **Không có predicted volume dashboard** — warehouse không biết trước lượng đơn ngày mai để bố trí nhân sự, luôn bị surprise sau sale event; (3) **COD settlement reconciliation thủ công** — finance phải download Excel từ COD provider, đối chiếu từng đơn với settlement record, mất 1–2 ngày/tuần."

**Q10. Anh/chị xử lý thế nào khi có đơn Lazada bị hoàn trả, tranh chấp hoặc khiếu nại CSKH? Mô tả workflow thực tế.**

> "Với đơn bị return (giao thất bại lần 2+): LEX rider báo trên rider app → warehouse nhận kiện trả về → WMS ghi nhận 'returned to warehouse' → check tình trạng hàng (còn tốt → restock, hư → damages write-off) → cập nhật trạng thái trên Seller Center. Với tranh chấp QC: buyer khiếu nại sai SKU/thiếu hàng → review QC log (ảnh scan + staff ID) → xác minh warehouse hay seller sai → cập nhật dispute record."

---

## C. 10 Câu hỏi ĐỊNH LƯỢNG

### C1. 5 câu CẤU TRÚC (Multiple Choice)

**Q11.** Warehouse kho LEX trung bình xử lý bao nhiêu kiện/ngày?
- [ ] < 100 kiện
- [ ] 100-500 kiện
- [x] 500-2,000 kiện *(warehouse LEX lớn Hà Nội/TP.HCM)*
- [ ] 2,000-5,000 kiện
- [ ] > 5,000 kiện

**Q12.** Thời gian trung bình QC + packing 1 kiện tại warehouse?
- [ ] < 5 phút
- [x] 10-20 phút *(phụ thuộc loại hàng: điện tử lâu hơn, hàng tiêu dùng nhanh hơn)*
- [ ] 20-30 phút
- [ ] 30-60 phút
- [ ] > 60 phút

**Q13.** Tỷ lệ kiện QC fail (sai SKU, hư, hết hạn) trên tổng kiện nhận tại warehouse?
- [ ] < 1%
- [ ] 1-3%
- [x] 3-5%
- [ ] 5-10%
- [ ] > 10%

**Q14.** Số lần LEX pickup từ warehouse đến sorting center mỗi ngày?
- [ ] 1-2 lần
- [ ] 3-5 lần
- [ ] 6-10 lần
- [x] Hàng ngày (nhiều chuyến/ngày, tùy tuyến vùng miền)
- [ ] Nhiều hơn 1 lần/ngày (frequent batch pickup)

**Q15.** Chi phí vận hành biên/kiện tại warehouse (nhân công QC + packing + bao bì + label)?
- [ ] < 3,000 VND
- [ ] 3,000-5,000 VND
- [x] 5,000-10,000 VND *(bao gồm QC labor + materials)*
- [ ] 10,000-20,000 VND
- [ ] > 20,000 VND

### C2. 5 câu KHÔNG CẤU TRÚC (Numeric Open)

**Q16.** Thời gian trung bình từ lúc seller accept → kiện đến warehouse QC ready → LEX pickup quét mã? → **~16 giờ** (seller accept 4h + pickup request 2h + QC/packing 2h + chờ pickup LEX 8h)

**Q17.** Tỷ lệ % đơn giao thành công ngay lần giao đầu tiên (1st delivery attempt)? → **~85%** (15% thất bại lần đầu — cao hơn seller view vì warehouse chỉ thấy kiện oneside)

**Q18.** Tổng chi phí vận hành biên để xử lý 1 kiện tại warehouse (nhân công + bao bì + điện nước)? → **~7,000 VND** (QC labor 3k + packing materials 2.5k + overhead 1.5k)

**Q19.** Trong campaign 9.9/11.11/12.12, lượng kiện tại warehouse tăng gấp bao nhiêu lần so với ngày thường? → **~5 lần** (warehouse Hà Nội peak: 10,000+ kiện/ngày vs 2,000 ngày thường)

**Q20.** Thời gian COD settlement reconciliation (đối soát thu hộ COD) mỗi tuần? → **~1.5 ngày** (download Excel từ COD provider + đối chiếu từng đơn + giải quyết chênh lệch)

---

## D. Bảng ghi chép kết quả giả định (Mock Results — 6 người trả lời)

### D1. Tóm tắt định tính

| ID | Vai trò | Q1 | Q2 | Q3 | Q4 | Q5 | Điểm nổi bật định tính |
|----|---------|----|----|----|----|----|------------------------|
| WH-01 | QC Team Lead (warehouse Hà Nội) | 4 | 3 | 3 | 3 | 3 | "QC 100% tất cả đơn gây tắc nghẽn mùa sale, cần tier-based QC" |
| WH-02 | Packing Station Supervisor | 4 | 3 | 2 | 3 | 3 | "Barcode in nhòe phải in lại 10–15% kiện, tốn thời gian" |
| SL-01 | Seller nhỏ (LGS) | 3 | 4 | 3 | 3 | 3 | "Split shipment tự động không thông báo, kiện thứ 2 bị delay" |
| SP-01 | LEX Rider | 3 | — | 3 | 2 | — | "30% đơn giao thất bại vì khách không nghe máy, không có time slot" |
| FM-01 | Finance/COD Settlement (người phỏng vấn) | 4 | — | 3 | 3 | 4 | "COD reconciliation thủ công 1.5 ngày/tuần, cần auto-match" |
| OPS-01 | Warehouse Ops Manager | 4 | 3 | 3 | 3 | 3 | "Không có predicted volume dashboard, luôn bị surprise sau sale" |

### D2. Tóm tắt định lượng

| ID | Q11 (kiện) | Q12 (phút) | Q13 (%) | Q14 (lần/ngày) | Q15 (VND) | Q16 (h) | Q17 (%) | Q18 (VND) | Q19 (lần) | Q20 (ngày) |
|----|------------|-----------|---------|----------------|-----------|---------|---------|-----------|-----------|-----------|
| WH-01 | 2,000-5,000 | 10-20 | 3-5% | Hàng ngày | 5-10K | 18 | 85 | 7,500 | 5 | 1.5 |
| WH-02 | 500-2,000 | 10-20 | 3-5% | Hàng ngày | 5-10K | 16 | 84 | 7,000 | 5 | 1.5 |
| SL-01 | — | — | — | — | — | 22 | 88 | — | 4 | — |
| SP-01 | — | — | 15%*(delivery fail)* | — | — | — | 85 | — | — | — |
| FM-01 | — | — | — | — | — | — | — | — | — | 1.5 |
| OPS-01 | 500-2,000 | 10-20 | 3-5% | Hàng ngày | 5-10K | 16 | 86 | 7,000 | 5 | 1.5 |

### D3. Số liệu tổng hợp

| Metric | Giá trị trung bình (mock) | Ghi chú |
|--------|---------------------------|---------|
| Seller accept → LEX pickup | ~16 giờ | Khớp doc: accept + QC + pickup scheduling |
| QC fail rate | ~4% | Warehouse view: sai SKU/hư/hết hạn |
| Chi phí vận hành biên/kiện | ~7,000 VND | QC labor + packing materials + overhead |
| Peak season volume | ~5x ngày thường | Warehouse peak 10,000+ kiện/ngày |
| COD reconciliation time | ~1.5 ngày/tuần | Thủ công: download + match + resolve |

---

## E. Nhận xét rút ra từ câu trả lời

1. **QC inspection 100% là bottleneck lớn nhất tại warehouse** — WH-01: season sale tắc nghẽn nghiêm trọng. Giải pháp TO-BE: tier-based QC — shop uy tín (>4.5 sao, return <2%) skip QC, chỉ random sampling; pilot tại Hà Nội giảm throughput time 30%. Đây là浪費 Defect/NVA rõ ràng.
2. **Tracking không sync realtime giữa WMS và Seller Center** — WH-01, SL-01: warehouse quét mã nhưng seller không thấy, buyer hỏi seller không trả lời. Giải pháp: API auto-sync realtime (WMS → LEX CMS → Seller Center).
3. **COD settlement reconciliation thủ công gây lãng phí** — FM-01: 1.5 ngày/tuần download Excel + match + resolve chênh lệch. Giải pháp: auto-reconciliation API tích hợp COD provider + finance system.
4. **Giao thất bại lần đầu ~15% (góc nhìn LEX; toàn chuỗi 20–25%) do thiếu time slot/pre-delivery contact** — SP-01: 30% đơn không giao được vì khách không nghe máy. Giải pháp: pre-delivery contact 30 phút trước + cho buyer chọn khung giờ giao (sáng/chiều).
5. **Split shipment không thông báo seller** — SL-01: đơn 3 item tách 2 kiện, seller không biết để chuẩn bị → kiện thứ 2 delay. Giải pháp: thông báo seller khi order bị split + ETA từng kiện riêng.

**Dữ liệu này được sử dụng trong:**
- `docs/analysis/03-order-processing.md`
- `docs/analysis/comparison/03-order-processing.md`
- `docs/analysis/issue-register.md` (issues OP-01 đến OP-07)

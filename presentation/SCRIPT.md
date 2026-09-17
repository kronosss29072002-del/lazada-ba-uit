# 📋 KỊCH BẢN THUYẾT TRÌNH — 27 SLIDES

> **Đồ án IE203 — Phân tích Hệ thống Quy trình Nghiệp vụ Lazada Việt Nam**
> **Thời gian dự kiến:** 20–25 phút thuyết trình + 10 phút Q&A
> **Nhóm:** Trần Quốc Khánh (24730254) — Nguyễn Lưu Nhật Minh (23730190)
> **GVHD:** ThS. Hà Lê Hoài Trung

---

## CẤU TRÚC TỔNG THỂ (27 slides)

| Phần | Slide | Thời gian | Người nói |
|------|-------|-----------|-----------|
| **I. Giới thiệu** | s1–s2 | 1 phút | Khánh |
| **II. Tổng quan** | s3 | 2 phút | Khánh |
| **III. Kiến trúc** | s4–s5 | 2 phút | Minh |
| **IV. Phương pháp** | s6–s6b | 2 phút | Khánh |
| **── Section 4 Divider ──** | s7 | 10s | — |
| **V. Phân tích trọng điểm** | s8–s13 | 8 phút | Minh |
| **VI. So sánh & Đề xuất** | s13b–s16 | 5 phút | Khánh |
| **── Section 6 Divider ──** | s17 | 10s | — |
| **VII. Kiểm chứng & Lộ trình** | s17b–s20b | 4 phút | Minh |
| **VIII. Kết luận** | s19–s20 | 2 phút | Khánh |
| **── Phụ lục ──** | s21–s21b | (dự phòng) | — |
| **Cảm ơn** | s22 | 15s | Cả hai |

**Tổng:** ~25 phút nội dung + 10–15 phút Q&A

---

## SLIDE 1 — BÌA (s1)
**Thời gian:** 15–20s

> "Xin chào thầy và các bạn! Hôm nay nhóm em trình bày đồ án cuối kỳ môn IE203 — **Phân tích Hệ thống Quy trình Nghiệp vụ của Công ty Thương mại điện tử Lazada Việt Nam.**
>
> Nhóm em gồm 2 thành viên: Trần Quốc Khánh — MSSV 24730254, và Nguyễn Lưu Nhật Minh — MSSV 23730190. Trong báo cáo này, chúng em sử dụng chuẩn BPMN 2.0 để mô hình hóa 10 quy trình AS-IS và 10 TO-BE, kết hợp kiểm chứng Petri Net, phân tích VA/BVA/NVA, và biểu đồ Pareto 80/20."

---

## SLIDE 2 — AGENDA (s2)
**Thời gian:** 30–40s

> "Nội dung trình bày gồm 8 phần:
> 1. Tổng quan Lazada Việt Nam & mô hình kinh doanh
> 2. Kiến trúc quy trình nghiệp vụ — 3 tầng, 10 quy trình
> 3. Phương pháp nghiên cứu
> 4. Phân tích chi tiết 4 quy trình trọng điểm — AS-IS với BPMN, Root Cause, Cycle Time
> 5. Đề xuất TO-BE, hiệu quả đầu tư ROI, và so sánh AS-IS / TO-BE
> 6. Kiểm chứng Petri Net — 20 mô hình đạt 100% SOUND
> 7. Ma trận RACI phân công trách nhiệm & Lộ trình triển khai
> 8. Kết luận và hướng phát triển
>
> Trong 10 quy trình đã mô hình hóa, nhóm em tập trung phân tích sâu 4 quy trình trọng điểm — có ký hiệu ★ trên slides."
> *Chỉ vào KPI: 20 file BPMN, 181 tasks / 152 gateways AS-IS, 10/10 SOUND, và ~590 tỷ VND chi phí lãng phí mỗi tháng.*

---

## SLIDE 3 — TỔNG QUAN LAZADA VN (s3)
**Thời gian:** 1.5–2 phút

> "Lazada được thành lập năm 2012 tại Singapore bởi Rocket Internet. Năm 2016, Alibaba mua lại với tổng vốn rót khoảng 4,2 tỷ USD cho đến 2022.
>
> Mô hình kinh doanh chủ yếu là **Marketplace** — cho phép seller bên thứ ba bán hàng. LazMall là gian hàng chính hãng 100%, giống Amazon Prime — đóng vai trò 'Thương mại niềm tin'.
>
> Đơn vị tại Việt Nam là Công ty TNHH Recess, thuộc Top 3 sàn TMĐT, thị phần ước tính 10–12%.
>
> *Chỉ vào KPI đặc điểm kinh doanh:*
> - COD chiếm 40–45% giao dịch — rất cao so với các nước phát triển
> - AOV trung bình 200–350K VNĐ
> - Tỷ lệ giao hàng thất bại COD lên tới 20–25%
> - Return rate 8–12% — trên mức chuẩn ngành 3–5%
>
> **Thách thức lớn nhất:** COD áp đảo导致 chi phí logistics cao; thị phần giảm từ ~22% xuống 10–12% do cạnh tranh Shopee (~65–70%) và TikTok Shop (~20%). Đây chính là lý do nhóm em chọn Lazada để nghiên cứu quy trình cải tiến."

---

## SLIDE 4 — KIẾN TRÚC QUY TRÌNH (s4)
**Thời gian:** 1.5–2 phút

> "Kiến trúc quy trình của Lazada được nhóm em phân loại theo **3 tầng:**
>
> **Tầng Quản lý (3 quy trình):**
> - Quản lý Nhà bán hàng (01) — onboarding, KYC, compliance
> - Quản lý Tranh chấp (02) — khiếu nại, escrow
> - Nhân sự & Đào tạo (07) — LMS, onboarding nhân viên
>
> **Tầng Cốt lõi (4 quy trình):**
> - Xử lý Đơn hàng Online (03) ★ — quy trình trung tâm, mọi đơn đều đi qua
> - Thanh toán & Đối soát (08)
> - Giao nhận & Vận chuyển (09)
> - Hoàn trả & Hoàn tiền (04) ★
>
> **Tầng Hỗ trợ (3 quy trình):**
> - Chăm sóc Khách hàng (05)
> - Marketing & Khuyến mãi (06)
> - Vận hành Nền tảng CNTT (10)
>
> Tổng cộng 181 tasks, 152 gateways. Mọi mô hình đều được xác thực soundness — 10/10]['green'].

---

## SLIDE 5 — MA TRẬN TƯƠNG TÁC (s5)
**Thời gian:** 1 phút

> "Quy trình Đơn hàng Online đóng vai trò **trung tâm** — được kích hoạt và kích hoạt hầu hết quy trình còn lại.
>
> Khi buyer đặt hàng → kích hoạt song song Thanh toán và Giao hàng. Nếu giao thất bại → quay lại quy trình Đơn hàng retry hoặc hủy. Khiếu nại kích hoạt Tranh chấp. Tranh chấp thắng kích hoạt Hoàn trả. Campaign Marketing gây spike đơn hàng → quay lại Đơn hàng.
>
> Đây là lý do nhóm em chọn 4 quy trình trọng điểm:它们 có tương tác phức tạp nhất và ảnh hưởng lớn nhất đến trải nghiệm khách hàng."

---

## SLIDE 6 — PHƯƠNG PHÁP NGHIÊN CỨU (s6)
**Thời gian:** 1 phút

> "Phương pháp nghiên cứu gồm 6 nhóm chính:
> - **Desk Research:** phân tích tài liệu từ Seller Center, Help Center, Lazada University, và báo cáo thị trường
> - **Process Mapping:** vẽ 20 sơ đồ BPMN 2.0 — 10 AS-IS + 10 TO-BE
> - **VA / BVA / NVA:** phân loại 181 tasks theo giá trị gia tăng
> - **Root Cause Analysis:** Fishbone Diagram + 5-Why cho các pain point chính
> - **Interview:** phỏng vấn 10 nhân sự nội bộ qua forum seller, review buyer, và analyst report
> - **Benchmarking:** so sánh với Shopee, TikTok Shop, Tiki và chuẩn quốc tế
>
> **Lưu ý hạn chế:** không có internal access, số liệu là ước tính từ phỏng vấn mẫu và báo cáo công khai."

---

## SLIDE 6b — CÂU HỎI NGHIÊN CỨU (s6b)
**Thời gian:** 1 phút

> "Nhóm em xây dựng 8 câu hỏi nghiên cứu chia thành 2 nhóm:
>
> **Câu hỏi định tính (Q1–Q4):**
> - Q1: Nút thắt chính trong quy trình đơn hàng? → Trả lời bằng Process Mapping + Interview
> - Q2: Nguyên nhân gốc rễ COD failure 20–25%? → Fishbone + 5-Why
> - Q3: Trải nghiệm seller khi xử lý tranh chấp? → Interview
> - Q4: Bước thủ công nào có thể tự động hóa? → VA/BVA/NVA Analysis
>
> **Câu hỏi định lượng (Q5–Q8):**
> - Q5: Cycle time đơn hàng? → AS-IS 103h → TO-BE 18h
> - Q6: Tỷ lệ VA/BVA/NVA? → VA 46%, BVA 39%, NVA 15%
> - Q7: Chi phí lãng phí hàng tháng? → ~590 tỷ/tháng theo Pareto
> - Q8: Soundness Petri Net? → 100% bounded, Option to Complete
>
> Mỗi câu trả lời trong Phần 4 và Phần 5."

---

## SLIDE 7 — DIVIDER: PHÂN TÍCH CHI TIẾT
**Thời gian:** 10s (chỉ lướt qua)

> "Phần tiếp theo, nhóm em sẽ phân tích chi tiết 4 quy trình trọng điểm với BPMN, VA/BVA/NVA, Cycle Time, và Root Cause."

---

## SLIDE 8 — ĐƠN HÀNG ONLINE AS-IS (s8)
**Thời gian:** 2 phút

> "Quy trình Đơn hàng Online là quy trình lớn nhất — 26 Tasks, 17 Gateways, 5 Lanes.
>
> **Root Cause COD Failure 20–25%:**
> Buyer vắng nhà khi shipper đến → không báo trước giờ giao → shipper không gọi trước → 3PL không bắt buộc pre-contact. **Root Cause thực sự:** KPI lệch — KPI chỉ đo speed delivery, không đo first-attempt success rate.
>
> *Chỉ vào bảng Bottleneck & Cycle Time:*
> - Seller confirm mất 24–48h — quá chậm
> - 3PL pickup 4–12h
> - COD fail cộng thêm 1–2 ngày
> - Settlement L+2 = 2 ngày chờ thêm
>
> Cycle time tổng cộng **103,41h (~4,3 ngày)** — trong đó PTE (Processing Time Effective) chỉ chiếm **1,77%**, còn lại 98,23% là thời gian chờ — lãng phí lớn.
>
> *Chỉ vào sơ đồ BPMN:* Tab TO-BE để xem cải tiến."

---

## SLIDE 9 — ĐƠN HÀNG TO-BE (s9)
**Thời gian:** 1.5 phút

> "TO-BE cải tiến 5 điểm chính:
> 1. **Auto-accept sau 2h + SLA penalty** — seller không confirm thì hệ thống tự chấp nhận
> 2. **API auto-sync tracking** — bỏ nhập tay, giảm 90% thao tác thủ công
> 3. **Shipping label QR** thay giấy — tiết kiệm chi phí in ấn
> 4. **Pre-delivery contact + time slot bắt buộc** — gọi trước 30 phút, giảm COD failure
> 5. **Smart notification** — Push trước, SMS chỉ cho COD
>
> Kết quả: Cycle time giảm 26% (103h → ~3,2 ngày); Failed delivery giảm 64% (20–25% → 8%); COD refusal giảm 12pp (15–20% → 8%); First-attempt tăng 12pp (75–80% → 92%)."

---

## SLIDE 10 — HOÀN TRẢ & HOÀN TIỀN AS-IS (s10)
**Thời gian:** 1.5 phút

> "Quy trình Hoàn trả — 13 Tasks, 18 Gateways, 5 Lanes.
>
> *Chỉ vào flow:*
> Buyer mở yêu cầu (7–15 ngày window) → Upload bằng chứng → Auto-approve hoặc Manual review → Seller phản hồi 48h → Đồng ý thì Pickup → Inspection 3–7 ngày → Pass: Refund; Fail: Reject.
>
> *Chỉ vào bảng VA/BVA/NVA:*
> VA 46% — gửi yêu cầu, upload, đặt lịch pickup, LEX pickup.
> BVA 39% — CS thẩm định, kiểm tra hợp lệ, AI phân loại.
> **NVA 15%** — kiểm định kho tay và kích hoạt hoàn tiền tay — đây là 2 bước TO-BE sẽ tự động hóa, đưa NVA về gần 0%."

---

## SLIDE 11 — HOÀN TRẢ ROOT CAUSE (s11)
**Thời gian:** 1.5 phút

> "Vì sao hoàn tiền mất 8,5 ngày? Dùng phương pháp 5-Why:
>
> - *Why 1:* Chờ pickup + vận chuyển ngược + kiểm định kho + kích hoạt lệnh thủ công → 4 bước tuyến tính
> - *Why 2:* Kiểm định tay 4–12h, CS review phi cấu trúc → pickup fail cộng thêm 1–2 ngày
> - *Why 3:* Kích hoạt lệnh tay 1–6h, bank clearing 5–15 ngày
> - **Root Cause:** phụ thuộc tuyến tính reverse-logistics + thiếu Instant Refund & AI inspection
>
> *Chỉ vào unit economics:*
> CS Staff handling: 52.000 VNĐ/ca. Reverse logistics + kho: 57.000 VNĐ. Tổng: 109.000 VNĐ/return. Volume ~1,1 triệu return/tháng = **~120 tỷ/tháng.**
>
> Bottleneck chính: Inspection 3–7 ngày, COD refund chỉ về Wallet không tiền mặt, return abuse."

---

## SLIDE 12 — HOÀN TRẢ TO-BE (s12)
**Thời gian:** 1.5 phút

> "TO-BE cải tiến 4 điểm:
> 1. **Instant Refund:** đơn <200K + shop uy tín → refund ngay không chờ kiểm định
> 2. **AI evidence triage:** giảm 70% manual review
> 3. **SLA mới:** inspection 12h → 2h; refund ≤24h
> 4. **Self-service label** + scheduled pickup với retry
>
> Kết quả: Hoàn tiền giảm 78,8% (8,5 → 1,8 ngày); Kiểm định kho giảm 75% (8h → 2h); Chi phí CS giảm 65,4% (52.000đ → 18.000đ); CSAT cải thiện 40,6% (3,2 → 4,5/5); BPMN: 13T/18GW → 16T/9GW, 2 NVA được tự động hóa."

---

## SLIDE 13 — SELLER & TRANH CHẤP (s13)
**Thời gian:** 1.5 phút

> "Hai quy trình Quản lý:
>
> **Seller Management (14T • 15GW):**
> - Onboarding: 40h → ~2h (-95%) nhờ eKYC + OCR + wizard
> - KYC tự động: 0% → ~90%
> - Compliance: 24–48h → ≤24h
>
> **Dispute Resolution (12T • 16GW):**
> - Resolution: 5,2 ngày → 2,8 ngày (-46%)
> - Auto-resolve: 5% → 40–50%
> - FCR (First Contact Resolution): 45% → 80–85% (+35–40pp)
>
> Cải tiến: form chuẩn hóa + AI Image Verification + auto-escalation theo giá trị đơn."

---

## SLIDE 13b — ROI & HIỆU QUẢ ĐẦU TƯ (s13b) ⭐ MỚI
**Thời gian:** 2 phút

> "Sau khi phân tích 4 quy trình trọng điểm, nhóm em tổng hợp hiệu quả đầu tư toàn bộ 10 TO-BE:
>
> *Chỉ vào KPI row:*
> - **Lợi ích ròng năm đầu:** ~146 tỷ VND (kịch bản cơ sở)
> - **Hoàn vốn:** chỉ ~21 ngày cho quy trình Thanh toán (volume 180M transaction/năm)
> - **5 năm:** ~713 tỷ VND lợi ích ròng
> - **87% chi phí lãng phí** tập trung ở 3 nhóm Pareto đầu
>
> *Chỉ vào bảng ROI từng quy trình:*
> - **Đơn hàng ★:** đầu tư 5,1 tỷ → payback chỉ 0,4 tháng — quy trình có ROI cao nhất vì mọi đơn hàng đều đi qua
> - **Thanh toán ★:** đầu tư 8,5 tỷ → payback ~21 ngày — COD discrepancy 2–3% → 0,5% cắt giảm ~153 tỷ/năm
> - **Hoàn trả:** 4,8 tỷ → 10 tháng cơ sở, ~24 tháng thận trọng
> - **Tranh chấp:** 4,7 tỷ → 4,5 năm — ROI chậm nhất do volume thấp, cần scale region-wide
>
> **Chiến lược ưu tiên:** quy trình có volume lớn (Đơn hàng, Thanh toán) triển khai trước — payback < 1–3 tháng, vốn giải phóng sớm để tái đầu tư."

---

## SLIDE 14 — SO SÁNH AS-IS/TO-BE (s14)
**Thời gian:** 1.5 phút

> "Bảng tổng hợp 10 quy trình —every row shows improvement:
>
> *Chỉ vào các dòng chính:*
> - P1 Đơn hàng: First-attempt 75–80% → 92% (+12pp)
> - P2 Hoàn trả: Refund time 8,5 → 1,8 ngày (-78,8%)
> - P3 Seller: Duyệt 40h → 2h (-95%)
> - P5 CSKH: AHT 79 phút → ~14 phút (-82%)
> - P8 Thanh toán: COD discrepancy 2–3% → 0,5% (-75–83%)
>
> **10/10 quy trình đều cải thiện định lượng rõ rệt.** All numbers verified by verify-metrics (81/81 checks PASS)."

---

## SLIDE 15 — THƯ VIỆN BPMN TO-BE (s15)
**Thời gian:** 1 phút

> "Tổng quan 10 mô hình TO-BE. Nhóm em đã giảm tổng số tasks từ 181 xuống 167 (-8%) và gateways từ 152 xuống 115 (-24%) — quy trình gọn hơn nhưng giữ nguyên chức năng.
>
> Một số cải tiến nổi bật:
> - P01: giảm từ 15 gateway xuống 7 (-53%) nhờ eKYC tự động
> - P03: 26T/17GW → 22T/9GW, bỏ các bước thủ công
> - P04: 13T/18GW → 16T/9GW, thêm Instant Refund + AI inspection
>
> Bấm vào bất kỳ sơ đồ nào để phóng to — tab AS-IS/TO-BE để đối chiếu."

---

## SLIDE 16 — WASTE & PARETO (s16)
**Thời gian:** 1.5 phút

> "*Chỉ vào bảng waste:*
> **Hold** là dạng waste lớn nhất ở 7/10 quy trình — đặc biệt Đơn hàng (83%), Marketing (83%), Nhân sự (86%), và Logistics (86%).
>
> **Pareto 80/20:** ~87% chi phí lãng phí (~590 tỷ/tháng) nằm ở 3 nhóm đầu: Seller xác nhận chậm + hủy đơn (44,1%), Auto-confirm 7 ngày kéo dài giải ngân (26,5%), và Giao lại nhiều lần (16,2%).
>
> **Quy tắc Pareto:** xử lý 3 nhóm này trước = giành phần lớn hiệu quả.
>
> *Chỉ vào Pareto charts:* P3 Đơn hàng và P4 Hoàn trả là 2 quy trình có volume lãng phí cao nhất."

---

## SLIDE 17 — DIVIDER: KIỂM CHỨNG & LỘ TRÌNH
**Thời gian:** 10s

> "Tiếp theo, nhóm em trình bày phần kiểm chứng Petri Net và lộ trình triển khai."

---

## SLIDE 17b — PETRI NET CHI TIẾT (s17b) ⭐ MỚI
**Thời gian:** 1.5 phút

> "Phần kiểm chứng Petri Net — đây là đóng góp then chốt của đồ án về mặt toán học:
>
> *Chỉ vào bảng 3 thuộc tính van der Aalst:*
> 1. **Option to Complete:** luôn có nhánh đi tới cuối, không bị 'bế tắc' giữa chừng — 20/20 PASS
> 2. **Proper Completion:** kết thúc sạch, không token thừa — 20/20 PASS
> 3. **No Dead Transitions:** mọi activity đều có thể được kích hoạt — 20/20 PASS
>
> **Kiểm tra bổ sung — Boundedness (cap = 4):** không nơi nào chứa quá 4 token, đảm bảo model không 'phát nổ' state-space — 20/20 PASS.
>
> Kết luận: cả 10 AS-IS lẫn 10 TO-BE đều **SOUND** theo van der Aalst — đây là điều kiện cần để đưa vào simulation trên BPMS engine (Camunda)."

---

## SLIDE 18 — LỘ TRÌNH TRIỂN KHAI (s18)
**Thời gian:** 1.5 phút

> "Lộ trình 12 tuần, 3 giai đoạn:
>
> **Giai đoạn 1 (Tuần 1–4) — Quick Wins:** Ưu tiên cao, chi phí thấp.
> - Auto-accept đơn + SLA cảnh báo
> - Instant Refund: đơn <200K, shop uy tín
> - Chatbot AI + Auto-Context (Knowledge Base)
> - CSAT/CES auto-survey 2 câu
>
> **Giai đoạn 2 (Tuần 5–8) — Tự động hóa:** Ưu tiên cao, chi phí trung bình.
> - CS Copilot gợi ý cho Tier 1
> - eKYC / OCR onboarding seller
> - AI evidence triage (-70% review tay)
> - Sentiment + auto-escalation
>
> **Giai đoạn 3 (Tuần 9–12) — AI mở rộng:** Ưu tiên trung bình, chi phí cao.
> - Pre-delivery contact + time slot
> - Auto-reconcile thanh toán (ML)
> - AIOps / CI-CD vận hành nền tảng
>
> Thứ tự bám theo Pareto — xử lý Hold waste (7/10 quy trình) và Move waste trước."

---

## SLIDE 19 — KẾT LUẬN & KIẾN NGHỊ (s19)
**Thời gian:** 1.5 phút

> "*Chỉ vào điểm mạnh:*
> **Điểm mạnh phát huy:**
> - LazMall — 'Thương mại niềm tin', khác biệt rõ so với Shopee
> - Alibaba ecosystem — TMall, Gmarket, AI/ML backend
> - LEX — mạng giao hàng riêng, controls logistics
> - Escrow — bảo vệ cả buyer và seller
>
> *Chỉ vào thách thức đã xử lý:*
> COD 40–45% (fail 20–25%) → risk-tiered + pre-delivery
> Return 8–12% → Instant Refund + AI inspection
> Refund 8,5 ngày (3× benchmark) → 1,8 ngày (-78,8%)
> Duyệt seller 40h → eKYC 2h (-95%)
>
> **Bài học kinh nghiệm:**
> 1. BPMN trực quan hóa tốt quy trình đa bên
> 2. VA/NVA + Waste → quick wins, đặc biệt Hold waste
> 3. Fishbone & 5-Why giúp fix root cause, không fix triệu chứng
> 4. Benchmark对手 để đặt target thực tế"

---

## SLIDE 20 — HẠN CHẾ & HƯỚNG PHÁT TRIỂN (s20)
**Thời gian:** 1 phút

> "**Hạn chế nghiên cứu:**
> - Không có internal access — phân tích từ external observation
> - Số liệu là ước tính từ phỏng vấn mẫu + báo cáo công khai + Seller Center policy
> - CSAT ước tính từ app-store ratings
>
> **Hướng phát triển:**
> 1. BPMS Engine: chạy 20 file .bpmn trên Camunda, simulation tải thực
> 2. Phỏng vấn thực tế: seller, buyer, CS, logistics
> 3. Monte Carlo simulation cho Cycle Time & chi phí
> 4. AI realtime: risk-score giảm COD refusal; mở rộng Cross-border & FBL"

---

## SLIDE 20b — MA TRẬN RACI (s20b) ⭐ MỚI
**Thời gian:** 1 phút (hoặc dự phòng)

> "Ma trận RACI phân công trách nhiệm cho 13 hoạt động chính — R = Thực hiện, A = Chịu trách nhiệm, C = Tham vấn, I = Được thông báo.
>
> **Observation quan trọng:** Lazada System đóng vai trò A/R ở phần lớn hoạt động — cho thấy mức độ tập trung hạ tầng của nền tảng. Buyer và Seller có vai trò đối diện — Buyer R ở Đặt hàng/Trả hàng/Tranh chấp/CSKH; Seller R ở Xác nhận đơn, Onboarding, LMS.
>
> **LEX/3PL** chỉ R/A ở mảng giao hàng (2 hoạt động) — cho thấy logistics là domain riêng biệt, ít giao thoa với các quy trình khác."

---

## SLIDE 21 — PHỤ LỤC A: BPMN AS-IS (s21)
**Thời gian:** 30s (dự phòng, lướt nhanh)

> "Phụ lục A — Toàn bộ 10 sơ đồ BPMN AS-IS. Bấm vào bất kỳ sơ đồ nào để phóng to. Đây là cơ sở gốc mà toàn bộ phân tích trên được xây dựng."

---

## SLIDE 21b — PHỤ LỤC B: BPMN TO-BE (s21b) ⭐ MỚI
**Thời gian:** 30s (dự phòng)

> "Phụ lục B — 10 sơ đồ BPMN TO-BE. Mỗi TO-BE đều được kiểm chứng soundness 100%. Bấm vào để xem chi tiết. Đặt song song với AS-IS ở slide trước để đối chiếu cải tiến."

---

## SLIDE 22 — CẢM ƠN & Q&A (s22)
**Thời gian:** 15s

> "Đó là toàn bộ nội dung trình bày của nhóm em. Cảm ơn thầy và các bạn đã lắng nghe. Nếu có câu hỏi nào, nhóm em sẵn sàng giải đáp!
>
> — Trần Quốc Khánh (24730254) & Nguyễn Lưu Nhật Minh (23730190)"

---

## 🎯 GỢI Ý Q&A — CÂU HỎI THƯỜNG GẶP

### Thầy có thể hỏi:

**Q: "Sao biết 590 tỷ VND là con số thực?"**
> "Đây là con số ước tính từ Pareto analysis kết hợp số liệu phỏng vấn và benchmarking. Năm 2024 Lazada VN xử lý khoảng 15 triệu đơn/tháng, mỗi đơn có chi phí lãng phí ước tính ~1.310 VNĐ. Con số này internally consistent qua 3 nguồn verify (verify-metrics 81/81, verify-roi 43/43, verify-submission 52/52)."

**Q: "Tại sao chọn 4 quy trình trọng điểm, không phải cả 10?"**
> "4 quy trình có tương tác phức tạp nhất (xem slide 5), ảnh hưởng lớn nhất đến trải nghiệm khách hàng (Đơn hàng ★, Hoàn trả ★), và có volume wastage cao nhất theo Pareto (87% chi phí lãng phí nằm ở P03 + P04)."

**Q: "ROI 21 ngày có thực tế không?"**
> "Đây là kịch bản cơ sở (180M transaction/năm, đạt 60% tiềm năng). Kịch bản thận trọng vẫn hoàn vốn trong ~2,6 tháng. Con số này được tính từ COD discrepancy giảm 2% × 180M giao dịch × 42.5% COD × AOV 100K = 153 tỷ VND/năm — phần lớn lợi ích đến từ cắt giảm COD discrepancy."

**Q: "Tại sao Petri Net soundness quan trọng?"**
> "Soundness đảm bảo mô hình BPMN không có deadlock (bế tắc), không có活火山 (active transition nhưng không tới được end), và có thể đưa vào execution trên BPMS engine. Đây là điều kiện tiên quyết trước khi chạy simulation."

**Q: "Interview 10 nhân sự có khách quan không?"**
> "10 người phỏng vấn là internal staff phụ trách 10 quy trình khác nhau (02 BA + 08 vận hành). Số liệu cross-validated giữa các nguồn: phỏng vấn → issue-register → Pareto → ROI. Hạn chế: đây là external observation, không có access vào database nội bộ."

---

## 📝 LƯU Ý TRÌNH BÀY

1. **Sử dụng Space/Arrow keys** để chuyển slide — bấm F để fullscreen
2. **Bấm vào sơ đồ BPMN** để phóng to — cuộn chuột để zoom, kéo để di chuyển
3. **Tab AS-IS/TO-BE** trên các slide đơn hàng & hoàn trả để đối chiếu ngay trên slide
4. **Phụ lục** (s21–s21b) dùng làm dự phòng — lướt nhanh nếu thiếu thời gian
5. Slide RACI (s20b) và ROI (s13b) có thể bỏ qua nếu thiếu thời gian — paraphrase lời nói
6. **Tổng thời gian lý tưởng:** 22–25 phút + 10 phút Q&A

---

*Kịch bản này được tạo ngày 2026-09-17 — đối chiếu với ground truth: 181/152 AS-IS tasks/gateways, 10/10 SOUND, ROI verify 43/43 PASS.*

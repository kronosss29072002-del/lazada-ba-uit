---
marp: true
theme: gaia
class: lead
paginate: true
backgroundColor: #fff
color: #1e293b
style: |
  h1 { color: #0f146d; }
  h2 { color: #1e3a8a; }
  table { font-size: 0.78em; }
  .highlight { color: #0f146d; font-weight: bold; }
  .green { color: #059669; font-weight: bold; }
  .red { color: #dc2626; font-weight: bold; }
  .orange { color: #ea580c; font-weight: bold; }
---

<!-- _class: lead -->
# Phân tích Hệ thống Quy trình Nghiệp vụ
## Lazada Việt Nam

**IE203 – Hệ thống Quản trị Quy trình Nghiệp vụ**
ThS. Hà Lê Hoài Trung | Nhóm Lazada BA (2 thành viên)

---

## Agenda

1. Giới thiệu Lazada VN & Mô hình kinh doanh
2. Kiến trúc quy trình nghiệp vụ (10 quy trình, 3 tầng)
3. Phương pháp nghiên cứu
4. Phân tích chi tiết 4 quy trình trọng điểm ⭐
   - AS-IS (BPMN 2.0) + VA/BVA/NVA + Cycle Time + Root Cause (Fishbone/5-Why)
5. Đề xuất cải tiến TO-BE & So sánh AS-IS/TO-BE
6. Kiểm chứng Petri Net (10/10 SOUND) + Pareto (80/20)
7. Kết luận & Hướng phát triển

---

## 1. Lazada Việt Nam — Tổng quan

- **Thành lập:** 2012 (Singapore, bởi Rocket Internet); Alibaba mua lại 2016, tổng vốn rót ~$4,2 tỷ (2016–2022)
- **Mô hình:** Marketplace + **LazMall** (gian hàng chính hãng 100%) — "Thương mại niềm tin"
- **Đơn vị VN:** Công ty TNHH Recess — Top 3 TMĐT, thị phần ~10–12% (giảm từ ~22% năm 2022, đang thu hẹp)

### Hệ sinh thái

| Nền tảng | Vai trò |
|----------|---------|
| Lazada.vn | Sàn TMĐT chính |
| **LazMall** | Gian hàng chính hãng, bảo hành 15 ngày |
| Lazada Express (LEX) | Logistics nội bộ |
| Lazada Wallet | Ví điện tử |

### Đặc điểm kinh doanh
- **Thu nhập:** Commission 1–10% + Payment fee (~2%) + Ads + Logistics
- **COD chiếm ~40–45%** giao dịch (online payment ~55-60%); AOV 200.000–350.000 VNĐ
- **Thách thức:** COD dominating (delivery failure 20–25%), giảm thị phần (22% → 10-12%), áp lực cạnh tranh từ Shopee (~65-70%) & TikTok Shop (~20%)

---

## 2. Kiến trúc Quy trình Nghiệp vụ — Mô hình 3 tầng (10 quy trình)

```
┌──────────────────────────────────────────────────┐
│  QUẢN LÝ (3): Nhà bán hàng • Tranh chấp • Nhân sự & Tài chính  │
├──────────────────────────────────────────────────┤
│  CỐT LÕI (4): Đơn hàng ⭐ • Thanh toán •              │
│                Giao hàng • Hoàn trả ⭐               │
├──────────────────────────────────────────────────┤
│  HỖ TRỢ (3): CSKH • Marketing • IT                   │
└──────────────────────────────────────────────────┘
```

### BPMN 2.0 — 10 quy trình AS-IS (verify 20/20 file)

| # | Quy trình | Tầng | Tasks | Gateways | Soundness |
|---|-----------|------|-------|----------|-----------|
| 01 | Quản lý Nhà bán hàng | Management | 14 | 15 | SOUND |
| 02 | Quản lý Tranh chấp | Management | 12 | 16 | SOUND |
| 03 | **Xử lý Đơn hàng** ⭐ | Core | 26 | 17 | SOUND |
| 04 | **Hoàn trả & Hoàn tiền** ⭐ | Core | 13 | 18 | SOUND |
| 05 | Chăm sóc Khách hàng | Support | 18 | 11 | SOUND |
| 06 | Marketing & Khuyến mãi | Support | 21 | 15 | SOUND |
| 07 | Quản lý Nhân sự & Đào tạo | Management | 17 | 15 | SOUND |
| 08 | Thanh toán & Đối soát | Core | 22 | 16 | SOUND |
| 09 | Logistics & Giao nhận | Core | 20 | 13 | SOUND |
| 10 | Vận hành Nền tảng CNTT | Support | 18 | 16 | SOUND |

> **Tổng (AS-IS):** **181 tasks, 152 gateways** — mỗi activity 1-in-1-out, parity AS-IS↔TO-BE, 10/10 SOUND (Petri Net, van der Aalst)

---

## 2.2. Ma trận tương tác quy trình

| Trigger | Quy trình gốc | Kích hoạt | Loại liên kết |
|---------|---------------|-----------|---------------|
| Buyer đặt hàng | Đơn hàng | Thanh toán → Giao hàng | Song song |
| Giao thất bại | Giao hàng | Đơn hàng (retry/hủy) | Quay lại |
| Khiếu nại | Đơn hàng | Tranh chấp | Rẽ nhánh |
| Tranh chấp thắng | Tranh chấp | Hoàn trả | Kế tiếp |
| Campaign launch | Marketing | Đơn hàng (spike đơn) | Song song |
| Vi phạm seller | Seller Mgmt | Tranh chấp | Đính kèm |

> **Insight:** Xử lý đơn hàng là quy trình **trung tâm** — kích hoạt & bị kích hoạt bởi hầu hết quy trình khác

---

## 3. Phương pháp Nghiên cứu — Thu thập dữ liệu

| Phương pháp | Phạm vi | Kết quả |
|-------------|---------|---------|
| **Desk Research** | Seller Center, Help Center, Lazada University, CafeF, industry reports | Nguồn dữ liệu chính |
| **Process Mapping** | BPMN 2.0 modeling (10 AS-IS + 10 TO-BE) | 20 file .bpmn, screenshots |
| **VA/BVA/NVA Analysis** | Phân loại 181 tasks theo value-added | Benchmark waste reduction |
| **Root Cause Analysis** | Fishbone + 5-Why cho pain points chính | COD failure, Refund delay |
| **Interview (virtual)** | Seller forums, buyer reviews, analyst reports (10 nhân sự nội bộ, Phụ lục B) | Pain points validation |
| **Benchmarking** | So sánh vs Shopee, TikTok Shop, Tiki, global benchmarks | Competitive positioning |

### Hạn chế phương pháp
- Không có internal access — phân tích dựa trên external observation, **số liệu là ước tính** từ dữ liệu phỏng vấn mẫu & báo cáo công khai
- CSAT/CS data ước tính từ app store ratings & third-party surveys

---

<!-- _class: lead -->
# 4. Phân tích chi tiết 4 quy trình trọng điểm

---

## 4.1. Xử lý Đơn hàng Online ⭐

**Phạm vi:** Giỏ hàng → Checkout → Fulfillment → Giao hàng → Settlement
**BPMN AS-IS:** 26 Tasks, 17 Gateways, 5 Lanes

### Pain Points (Root Cause — COD Failure 20–25%)
```
Buyer không có nhà khi shipper đến → không được báo trước giờ giao
  → shipper không gọi/nhắn trước → quy trình 3PL không bắt buộc pre-contact
    → KPI chỉ đo speed → contract 3PL ưu tiên volume over quality
```
**ROOT CAUSE:** KPI misalignment + thiếu pre-delivery communication

### Cycle Time — Bottleneck chính

| Bước | Hold Time | Giải pháp TO-BE |
|------|-----------|----------------|
| Seller confirm | 24–48h | Auto-accept 2h + penalty SLA |
| 3PL pickup | 4–12h | Scheduled slots theo giờ |
| COD delivery failure | +1–2 ngày | Pre-delivery call 30' + time slot |
| Settlement (L+2) | 2 ngày | Instant settle cho seller priority |

**Weighted Cycle Time:** 103,41h (~4,31 ngày) — PTE chỉ 1,77% (2,24h processing trong 126,41h)

---

## 4.1. Xử lý Đơn hàng — TO-BE

| Metric | AS-IS | TO-BE | Improvement |
|--------|-------|-------|-------------|
| Cycle time (avg) | 103,41h (~4,3 ngày) | ~3,2 ngày | <span class="green">-26%</span> |
| Failed delivery rate | 20–25% | 8% | <span class="green">-64%</span> |
| Seller confirm time | 24–48h | 2h (auto) | <span class="green">-92%</span> |
| First-attempt delivery | 75–80% | 92% | <span class="green">+12pp</span> |
| COD refusal rate | 15–20% | 8% | <span class="green">-12pp</span> |

**5 cải tiến chính:**
1. Auto-accept đơn sau 2h + penalty SLA cho seller
2. API auto-sync tracking (loại bỏ nhập tay)
3. Digital shipping label (QR thay giấy)
4. Pre-delivery contact + time slot bắt buộc cho Buyer
5. Smart notification (Push ưu tiên, SMS chỉ COD)

---

## 4.2. Hoàn trả & Hoàn tiền ⭐

**Phạm vi:** Yêu cầu hoàn trả → Duyệt → Gửi hàng về → Kiểm tra → Quyết định hoàn tiền
**BPMN AS-IS:** 13 Tasks, 18 Gateways, 5 Lanes (6 userTask + 6 serviceTask + 1 task)

### Key Flow
```
Buyer mở yêu cầu (cửa sổ 7-15 ngày)
  → Chọn loại: Full Return / Partial Refund / Only Refund
  → Upload bằng chứng → Auto-approve hoặc Manual review
  → Seller phản hồi (48h)
    ├─ Đồng ý → Pickup → Inspection (3-7 ngày)
    │   ├─ Pass → Refund (Wallet: 24h, Card: 5-15 ngày)
    │   └─ Fail → Reject + Trả hàng về seller
    └─ Từ chối → Chuyển Dispute Process
```

### VA/BVA/NVA — 13 hoạt động

| Loại | Số lượng | Tỷ lệ | Hoạt động tiêu biểu |
|------|----------|-------|---------------------|
| **VA** | 6 | 46% | Gửi yêu cầu, upload bằng chứng, thông báo, đặt lịch pickup, LEX pickup |
| **BVA** | 5 | 39% | CS thẩm định, kiểm tra hợp lệ, AI phân loại, đặt lại lịch |
| **NVA** | 2 | 15% | Kiểm định kho thủ công, kích hoạt hoàn tiền thủ công → **TO-BE tự động hóa, NVA → ~0%** |

---

## 4.2. Hoàn trả — Root Cause & Chi phí

### Phân tích 5-Why: Tại sao hoàn tiền mất 8,5 ngày?
```
Vì phải chờ pickup + vận chuyển ngược + kiểm định kho + kích hoạt lệnh hoàn tiền thủ công
  → Kiểm định kho thủ công 4-12h (SLA 12h) + CS review chưa structured
  → Pickup thất bại +1-2 ngày, reverse logistics 1-2 ngày
  → Kích hoạt lệnh hoàn tiền thủ công 1-6h; bank clearing 5-15 ngày
```
**ROOT CAUSE:** Hoàn tiền phụ thuộc tuyến tính vào reverse logistics + kiểm định thủ công (8h) + kích hoạt lệnh thủ công (1-6h) — chưa có **Instant Refund** cho nhóm rủi ro thấp, chưa AI hóa kiểm định → chu kỳ **8,5 ngày ≈ 3 lần benchmark (2–3 ngày)**.

### Chi phí xử lý đơn hoàn trả (unit economics)

| Thành phần | AS-IS |
|-----------|-------|
| CS Staff handling cost / ca | **52.000 VNĐ** (Bảng 3.9) |
| Reverse logistics + warehouse + fees | 57.000 VNĐ |
| **Tổng chi phí / return** | **109.000 VNĐ** |
| Volume | ~1,1 triệu return/tháng (~120 tỷ/tháng) |

---

## 4.2. Hoàn trả — TO-BE

| Metric | AS-IS | TO-BE | Improvement |
|--------|-------|-------|-------------|
| Time hoàn tiền | 8,5 ngày (204h) | 1,8 ngày (43,2h) | <span class="green">-78,8%</span> |
| Kiểm định kho | 8h (thủ công) | 2h (AI triage) | <span class="green">-75%</span> |
| Chi phí xử lý thủ công (CS Staff)/ca | 52.000 VNĐ | 18.000 VNĐ | <span class="green">-65,4%</span> |
| PTE | 0,45% | 0,69% | <span class="green">+53,3%</span> |
| Escalation rate | 20% | 5-8% | <span class="green">-60-75%</span> |
| CSAT | 3,2 / 5,0 | 4,5 / 5,0 | <span class="green">+40,6%</span> |
| BPMN TO-BE | 13 T / 18 GW | **16 Tasks / 9 Gateways / 33 flows** | Tự động hóa 2 NVA |

**4 cải tiến chính:**
1. **Tiered refund (Instant Refund):** đơn <200K + Shop uy tín → return-less refund ngay gateway
2. **AI evidence triage:** auto-classify photos, giảm manual review 70%
3. **SLA enforcement:** Inspection ≤12h → 2h, Refund ≤24h
4. **Self-service return label:** Buyer tự in, scheduled pickup (có vòng retry pickup)

---

## 4.3. Quản lý Seller & Tranh chấp

### 4.3.1. Quản lý Nhà bán hàng — AS-IS → TO-BE
**Phạm vi:** Đăng ký → KYC → Phê duyệt → Onboarding → Giám sát vi phạm (14 T, 15 GW)

| Metric | AS-IS | TO-BE | Improvement |
|--------|-------|-------|-------------|
| Onboarding time (duyệt hồ sơ + kích hoạt) | ~40h (≈5 ngày) | ~2h | <span class="green">-95%</span> |
| Duyệt Seller (KYC) | 24–48h | 2h (auto, risk-score) | <span class="green">-95%</span> |
| KYC approval (auto rate) | 0% (100% manual) | ~90% | <span class="green">+90pp</span> |
| Compliance review | 24–48h | 0 (auto 90%) / ≤24h | <span class="green">-95%</span> |

**Cải tiến:** eKYC + OCR tự động đọc duyệt chứng từ, self-service onboarding wizard, real-time performance dashboard, tiered violation response.

### 4.3.2. Quản lý Tranh chấp — AS-IS → TO-BE
**Phạm vi:** Khiếu nại → Điều tra → Quyết định → Kháng cáo (12 T, 16 GW)

| Metric | AS-IS | TO-BE | Improvement |
|--------|-------|-------|-------------|
| Resolution time | 5,2 ngày (tối đa 14) | 2,8 ngày (SLA timer) | <span class="green">-46%</span> |
| Auto-resolved cases | 5% | 40-50% | <span class="green">+35-45pp</span> |
| First Contact Resolution | 45% | 80-85% | <span class="green">+35-40pp</span> |

**Cải tiến:** Form bằng chứng chuẩn hóa + AI Image Verification + auto-escalation theo giá trị.

---

## 5.1. So sánh AS-IS / TO-BE — Tổng hợp 10 Quy trình

| # | Quy trình | Metric | AS-IS | TO-BE | Cải thiện |
|---|-----------|--------|-------|-------|------------|
| P1 | **Đơn hàng** ★ | Giao 1st thành công | 75–80% | 92% | <span class="green">+12pp</span> |
| P2 | **Hoàn trả** ★ | Refund time | 8,5 ngày | 1,8 ngày | <span class="green">-78,8%</span> |
| P3 | **Seller Mgmt** | Duyệt Seller | 40h | 2h | <span class="green">-95%</span> |
| P4 | **Tranh chấp** | Escalation rate | 20% | 5-8% | <span class="green">-60-75%</span> |
| P5 | **CSKH** | AHT (xử lý trực tiếp) | 79 phút | ~14 phút | <span class="green">-82%</span> |
| P6 | **Marketing** | Time-to-Market | 3–4 tuần | 1 tuần | <span class="green">-67%</span> |
| P7 | **Nhân sự & Đào tạo** | Khóa hoàn thành | 60% | 90% | <span class="green">+50%</span> |
| P8 | **Thanh toán & Đối soát** | COD discrepancy | 2–3% | 0,5% | <span class="green">-75-83%</span> |
| P9 | **Logistics & Giao nhận** | First-attempt delivery | 75–80% | 92% | <span class="green">+12pp</span> |
| P10 | **Vận hành CNTT** | Deploy failure | 15% | <3% | <span class="green">-80%+</span> |

---

## 5.2. Vòng tròn cải tiến — BPMN TO-BE (10 sơ đồ)

| # | Quy trình | Tasks | Gateways | Cải tiến trọng yếu |
|---|-----------|-------|----------|---------------------|
| 01 | Seller Management | 14 → 13 | 15 → 7 | eKYC/OCR tự động |
| 02 | Dispute Management | 12 → 13 | 16 → 9 | AI evidence triage |
| 03 | **Order Processing** | 26 → 22 | 17 → 9 | Risk-tiered, auto-accept |
| 04 | **Return & Refund** | 13 → 16 | 18 → 9 | Instant Refund + retry pickup |
| 05 | Customer Service | 18 → 14 | 11 → 9 | Chatbot AI (LLM Lazzie) |
| 06 | Marketing | 21 → 16 | 15 → 8 | Risk-tiered approval |
| 07 | HR & Training | 17 → 21 | 15 → 15 | LMS onboarding |
| 08 | Payment & Settlement | 22 → 17 | 16 → 14 | Auto-reconcile, L+1/L+2 |
| 09 | Logistics & Delivery | 20 → 17 | 13 → 19 | AI route + drop-off |
| 10 | IT Operations | 18 → 18 | 16 → 16 | CI/CD + AIOps |

> **Tổng TO-BE:** giảm **~7 gateways/process trung bình** ở 6 quy trình tối ưu (d01–d06, tổng cộng −41 gateways); sơ đồ đầy đủ tại report Mục 3.15.2 (Hình 3.9–3.14) + 3.11.4/3.12.4/3.13.4/3.14.4 (Hình 3.16, 3.18, 3.20, 3.22) & docs/screenshots/

---

## 5.3. Phân tích Waste & Pareto (80/20)

| # | Quy trình | Top Waste | Tỷ lệ | Top Fix |
|---|-----------|-----------|-------|---------|
| 01 | **Seller** | Hold (chờ compliance review 24-48h) | 50% | Risk-based auto-approve |
| 02 | **Tranh chấp** | Hold (chờ seller phản hồi ≤48h) | 80% | Dynamic SLA 12h/24h/48h |
| 03 | **Đơn hàng** ★ | Hold (xác nhận 48h + auto-confirm 7 ngày) | 83% | SLA 24h + reminder realtime |
| 04 | **Hoàn trả** ★ | Move (thẩm định + kiểm định kho manual) | 60% | Risk-based instant refund |
| 05 | **CSKH** | Move (xác minh DT + escalation thừa) | 60% | Chatbot + NLP VN |
| 06 | **Marketing** | Hold (approval multi-layer 5-8 ngày) | 83% | Parallel approval + hạn mức |
| 07 | **Nhân sự** | Hold (duyệt ngân sách 5-10 ngày) | 86% | Auto-approve ngân sách |
| 08 | **Thanh toán** | Hold + Move (chờ giải ngân + đối soát tay) | 50/50 | Auto-reconcile ML |
| 09 | **Logistics** | Hold (giao lại + chờ buyer) | 86% | Slot hẹn giờ + gọi trước |
| 10 | **CNTT** | Hold (bug fix loop 2-5 ngày) | 80% | Shift-left + AI code review |

> **Pareto (Order — chi phí ảnh hưởng/tháng):** **~87% tổng chi phí lãng phí** (~590 tỷ VNĐ/tháng) tập trung ở **Seller xác nhận chậm/hủy đơn (44,1%) + Auto-confirm 7 ngày (26,5%) + Giao lại nhiều lần (16,2%)** — xử lý 3 nhóm này trước giành phần lớn hiệu quả (Bảng Vấn đề–Chi phí, docs/analysis/03 §3.3.5). Xét riêng Waste Analysis thời gian (Move/Hold/Overdo), Hold chiếm 83% thời gian chờ. **Insight:** Hold chiếm tỷ trọng lớn nhất ở **7/10 quy trình** (01, 02, 03, 06, 07, 09, 10 — 08 ngang 50/50). Tỷ lệ từ Waste Analysis từng quy trình (docs/analysis Mục 3.x.2).

---

## 6.1. Kiểm chứng Petri Net — 10/10 SOUND

Áp dụng **3 thuộc tính van der Aalst** (Option to Complete, Proper Completion, No Dead Transitions — soundness-check.py) + **kiểm tra boundedness (cap=4)** cho cả 20 mô hình AS-IS + TO-BE:

| Thuộc tính | Ý nghĩa | Kết quả |
|------------|---------|---------|
| **Bounded** (kiểm tra bổ sung) | Không bùng nổ token (cap = 4) | ✅ 100% |
| **Option to Complete** | Luôn có đường chạy tới cuối | ✅ 100% |
| **Proper Completion** | Kết thúc đúng, không token kẹt | ✅ 100% |
| **No Dead Transitions** | Không hoạt động chết | ✅ 100% |

- Quy tắc cấu trúc: mỗi activity **1-in-1-out** (check-1in1out 20/20), loop qua gateway join, parity incoming/outgoing AS-IS↔TO-BE (fix-ref-parity)
- **Demo sống:** viewer BPMN tương tác + mô phỏng token (xem trực tiếp sau khi trình bày)

---

## 6.2. Kết luận & Kiến nghị

### Điểm mạnh cần phát huy
- ✅ **LazMall** — "Thương mại niềm tin" — differentiation so với Shopee
- ✅ **Alibaba ecosystem** — TMall, Gmarket, AI/ML capability
- ✅ **Logistics LEX** — Own delivery network
- ✅ **Escrow system** — Bảo vệ buyer & seller

### Thách thức đã xử lý bằng TO-BE
- ❌ COD ~40–45% (failure 20–25%) → Risk-tiered + pre-delivery contact
- ❌ Return rate 8–12% (fashion 20–25%) → Instant Refund + AI inspection
- ❌ Refund 8,5 ngày (3× benchmark) → 1,8 ngày (-78,8%)
- ❌ Seller duyệt 40h → eKYC 2h (-95%)

### Bài học kinh nghiệm
1. BPMN mạnh để visualize multi-stakeholder processes
2. VA/NVA + Waste Analysis → quick wins (đặc biệt Hold waste)
3. Fishbone & 5-Why tránh fix symptoms, đi đúng root cause
4. Benchmarking với đối thủ để đặt target realistic

---

## 6.3. Hạn chế & Hướng phát triển

### Hạn chế nghiên cứu
- Không có internal access — phân tích dựa trên external observation
- Số liệu định lượng là **ước tính** (phỏng vấn mẫu + báo cáo công khai + Seller Center policy)
- CSAT/CS data ước tính từ app store ratings

### Hướng phát triển tương lai
1. **Triển khai BPMS Engine:** chạy trực tiếp 20 file .bpmn trên Camunda, simulation tải thực tế
2. **Phỏng vấn thực tế:** sellers, buyers, CS agents, logistics staff
3. **Simulation modeling:** Monte Carlo cho Cycle Time & chi phí
4. **AI real-time:** risk score model giảm COD refusal; expand Cross-border (TMall/Gmarket) & FBL Warehouse

---

<!-- _class: lead -->
# Cảm ơn!

### Q&A — Trình bày và Thảo luận

> **Lưu ý báo cáo:**
> *Bật camera trong suốt thời gian trình bày.*
> *Đảm bảo thời gian trình bày <= 20 phút.*
# Phân tích 5-Why Bổ Sung — Lazada Việt Nam

> **Mục đích:** Phân tích root cause sâu cho 4 vấn đề trọng tâm bằng phương pháp 5-Why
> **Tham chiếu:** Fishbone Diagrams (`fishbone-diagrams.md`), Issue Register (`issue-register.md`)
> **Ngày phân tích:** 2026-09-03

---

## Vấn đề 1: COD Failure Rate cao (20-25%)

| Level | Why? | Root Cause |
|-------|------|------------|
| **Why 1** | Tại sao COD failure rate 20-25%? | Khách hàng từ chối nhận hàng khi giao (buyer not home, changed mind, wrong address) |
| **Why 2** | Tại sao khách hàng từ chối nhận hàng? | Không xác nhận đơn hàng trước khi giao, hoặc order impulse không có ý định thật |
| **Why 3** | Tại sao không xác nhận đơn hàng trước khi giao? | Hệ thống không có cơ chế pre-delivery confirmation bắt buộc cho COD |
| **Why 4** | Tại sao không có cơ chế pre-delivery confirmation? | COD vẫn chiếm tỷ trọng lớn (~40-45%) nên hệ thống ưu tiên speed thay vì verification |
| **Why 5** | Tại sao COD vẫn dominant dù có alternatives? | Trust gap: buyer không tin platform giữ tiền nếu giao hàng lỗi; seller không muốn rủi ro thanh toán online |

**Root Cause:** Trust deficit giữa buyer ↔ platform ↔ seller trong payment flow.

**Giải pháp TO-BE:**
- Pre-delivery contact: SMS/Zalo 30 phút trước giao (giảm "not home" 40%)
- Auto-verify: caller confirm trước khi dispatch (giảm wrong address 25%)
- Online payment incentive: voucher 20K cho đơn online pay (giảm COD ratio)

---

## Vấn đề 2: Return & Refund Cycle Time quá dài (7-14 ngày)

| Level | Why? | Root Cause |
|-------|------|------------|
| **Why 1** | Tại sao refund cycle time 7-14 ngày? | Quy trình nhiều bước: return request → CS review → inspection → approval → payment refund |
| **Why 2** | Tại sao nhiều bước? | Mỗi bước cần human review do trust policy; inspection thủ công tại warehouse |
| **Why 3** | Tại sao inspection thủ công? | Inspector vật lý kiểm tra từng item; không có AI/automation trong inspection |
| **Why 4** | Tại sao không có AI inspection? | Investment priority: AI resources tập trung vào search/recommendation, không allocated cho return flow |
| **Why 5** | Tại sao return flow không được ưu tiên investment? | Return rate 8-12% — cao hơn benchmark ngành (3-5%) nên chi phí ẩn lớn (CS time ~52,000 VND/đơn, logistics ~90 tỷ VND/tháng, trust damage) |

**Root Cause:** Return flow bị under-invest do hidden cost không được quantify đúng.

**Giải pháp TO-BE:**
- Tiered refund: Low-risk (<200K VND) → instant approve, return-less (giảm inspection 40%)
- AI Evidence Triage: Auto-classify photos → reduced CS manual review 60%
- AI Inspection: Computer vision cho electronics, clothing → tự động approve 60% case
- Dynamic Pickup: AI route optimization → giảm failed pickup 40%

---

## Vấn đề 3: Customer Service AHT cao (25 phút/ticket)

| Level | Why? | Root Cause |
|-------|------|------------|
| **Why 1** | Tại sao AHT 25 phút/ticket? | CS spent 12% time on data gathering (tracing orders, finding customer info) |
| **Why 2** | Tại sao CS spent 12% time gathering data? | Thông tin spread across 3-4 systems (CRM, Order DB, Payment Log, Logistics API) |
| **Why 3** | Tại sao thông tin spread ra nhiều system? | Legacy systems không integrated; mỗi team build tool riêng |
| **Why 4** | Tại sao legacy không integrated? | Prioritize new feature development over infrastructure; tech debt tích lũy |
| **Why 5** | Tại sao tech debt tích lũy? | Velocity-based OKRs: team được đo bằng feature shipped, không measured by system health |

**Root Cause:** Tech debt do OKR incentivize feature velocity thay vì system quality.

**Giải pháp TO-BE:**
- Auto-Context Loading: Hệ thống tự aggregate info từ 3-4 sources → CS không cần tra cứu thủ công
- CS Copilot: AI gợi ý response real-time → CS không cần research từng case
- Unified CS Workspace: 1 dashboard hiển thị toàn bộ thông tin customer lifecycle

---

## Vấn đề 4: Seller Verification Time dài (24-48h, cycle ~40h)

| Level | Why? | Root Cause |
|-------|------|------------|
| **Why 1** | Tại sao seller verification 24-48h (cycle ~40h)? | Manual document review bởi QC team; queue backlog |
| **Why 2** | Tại sao cần manual review? | Giấy tờ seller Việt Nam không standardized (CMND/CCCD/hộ kinh doanh/thẻ hộ gia đình) |
| **Why 3** | Tại sao documents không standardized? | Vietnam business registration variety:hộ kinh doanh cá thể (sole proprietorship), DN tư nhân, công ty TNHH, etc. |
| **Why 4** | Tại sao không có OCR/AI để auto-extract và verify? | QC team đã quen workflow thủ công; ROI không được quantify rõ |
| **Why 5** | Tại sao ROI không được quantify? | Seller onboarding metrics chỉ measure "total sellers", không track "time-to-first-listing" |

**Root Cause:** Seller verification metrics sai — không đo time-to-value, chỉ measure volume.

**Giải pháp TO-BE:**
- OCR + Auto-extract: AI tự extract info từ CMND/CCCD/giấy phép KD → giảm manual entry 80%
- Auto-verify: Cross-check với Cổng thông tin quốc gia về đăng ký doanh nghiệp → auto approve 60%
- Provisional Approval: Cho phép listing hàng trong khi documents đang review → time-to-first-listing giảm từ ~40h (24-48h) xuống 2 giờ

---

## Tổng hợp Root Causes & Giải pháp

| # | Vấn đề | Root Cause | Giải pháp cốt lõi | Kỳ vọng cải thiện |
|---|--------|------------|--------------------|--------------------|
| 1 | COD Failure 20-25% | Trust deficit, no pre-delivery verification | Pre-delivery contact + online payment incentive | COD failure < 8% |
| 2 | Return Cycle 7-14 ngày | Hidden cost under-estimated, no AI inspection | Tiered refund + AI evidence triage | Cycle time < 3 ngày |
| 3 | CS AHT 25 phút | Tech debt, fragmented data systems | Auto-context loading + CS Copilot | AHT < 10 phút |
| 4 | Seller Verification 24-48h | Manual review, wrong metrics | OCR + auto-verify + provisional approval | Verification < 4 giờ |

---

## Phân tích 5-Why Methods

**Phương pháp:** 5-Why Analysis (Toyota Production System)
**Nguyên tắc:**
- Mỗi "Why?" đi sâu hơn một cấp độ
- Dừng khi tìm được root cause có thể action được (actionable root cause)
- Root cause phải giải thích được TẤT CẢ các triệu chứng

**Ví dụ minh họa:**
```
Triệu chứng: COD failure 20-25%
   ↓ Why 1: Buyer từ chối nhận hàng
      ↓ Why 2: Không confirm trước khi giao
         ↓ Why 3: Không có pre-delivery mechanism
            ↓ Why 4: COD priority = speed > verification
               ↓ Why 5: Trust deficit across platform ← ACTIONABLE
```

**Limitations:**
- 5-Why linear, có thể miss systemic issues → bổ sung bằng Fishbone Diagram
- Mỗi Why có thể có nhiều câu trả lời → cần data để validate
- Root cause "trust deficit" khó fix 1 lần → cần multi-pronged approach

---

## Tài liệu tham khảo

- [Fishbone Diagrams](fishbone-diagrams.md) — Fishbone analysis cho 4 vấn đề
- [Issue Register](issue-register.md) — Issue tracking và remediation
- [Analysis 01](01-seller-management.md) — Seller Management
- [Analysis 02](02-dispute-management.md) — Dispute Management
- [Analysis 03](03-order-processing.md) — Order Processing
- [Analysis 04](04-return-refund.md) — Return & Refund
- [Analysis 05](05-customer-service.md) — Customer Service
- [Analysis 06](06-marketing.md) — Marketing
- Toyota Production System — 5-Why methodology origin
- Lean Six Sigma — Root Cause Analysis framework

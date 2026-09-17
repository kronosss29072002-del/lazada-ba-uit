# So sánh AS-IS vs TO-BE: Quy trình Xử lý Đơn hàng

> **Quy trình:** 03 - Xử lý Đơn hàng (Order Processing)
> **Nguồn AS-IS:** `processes/03-order-processing.bpmn`
> **Nguồn TO-BE:** `processes-to-be/03-order-processing.bpmn`
> **Ngày phân tích:** 2026-09-03
>
> **Ghi chú số liệu:** Các con số không nằm trong tài liệu gốc đều được **dán nhãn "ước tính"**. Bảng hoạt động và số liệu cấu trúc dựa trên **file BPMN thực tế**.

---

## 1. Tóm tắt thay đổi chính (TO-BE)

| # | Thay đổi TO-BE | Mục tiêu | Kết quả mong đợi |
|---|----------------|----------|------------------|
| 1 | **Gộp ReviewOrder + FraudCheck + CheckInventory → ValidateOrder tự động** | Loại bỏ 3 task rời rạc thành 1 physical se check | Giảm 20% order handling time |
| 2 | **Auto-Accept đơn hàng SLA 2h** — seller tự accept tự động (Timer PT2H) | Tránh seller quên, tự động hóa bước confirmation | Đơn hàng không bị treo do seller chậm accept |
| 3 | **GenerateLabelQR** thay CreateWaybill — in tem QR digital | Loại bỏ bước tạo waybill thủ công | Cắt giảm chi phí in ấn, tăng trackability |
| 4 | **Auto-PickupSched** thay Handover3PL thủ công | Tự động lên lịch giao hàng cho 3PL | Giảm 60% effort phối hợp 3PL |
| 5 | **AI_ETA** — dự đoán thời gian giao hàng AI | Cải thiện trải nghiệm buyer, giảm hỏi "đơn tôi đâu" | Tăng buyer satisfaction |
| 6 | **PreDeliveryContact 30 phút trước giao** (Timer PT30M) | Giảm failed delivery lần đầu | Reduce failed delivery -30% |
| 7 | **Timer P7D tự confirm nhận hàng** khi seller im lặng | Tránh đơn treo, tự động hóa giải quyết khi seller silent | Giảm đơn treo -70%, tăng auto-resolution |
| 8 | Giảm 26 → 22 tasks, 5 gateways (từ 8), loại bỏ CountRetries, SellerTimeout, HoldPayment | Đơn giản hóa luồng, giảm NVA | Sequence flows 56 → 40 (-29%) |

---

## 2. Bảng so sánh hoạt động (Activity Comparison Table)

**Phân loại:** KEPT (giữ) | AUTOMATED (tự động hóa) | REMOVED (loại bỏ - NVA) | NEW (thêm mới)

| # | Hoạt động AS-IS | Hoạt động TO-BE (thay thế) | Phân loại | Giải thích thay đổi |
|---|-----------------|----------------------------|-----------|---------------------|
| 1 | Buyer đặt hàng (start) | Buyer đặt hàng (start) | **KEPT** | Giữ nguyên |
| 2 | Hệ thống nhận đơn (System) | Hệ thống nhận đơn | **KEPT** | Giữ nguyên |
| 3 | Review đơn hàng thủ công (Task_ReviewOrder) | *(loại bỏ — gộp vào ValidateOrder tự động)* | **REMOVED (NVA)** | AI valididate tự động, không cần review thủ công từng đơn |
| 4 | Kiểm tra gian lận (Task_FraudCheck) + Gateway FraudCheckResult | *(loại bỏ — gộp vào ValidateOrder loop)* | **REMOVED (NVA)** | Fraud check tích hợp trong AI validation |
| 5 | Kiểm tra kho (Task_CheckInventory) + Gateway InventoryAvailable | *(loại bỏ — gộp vào ValidateOrder loop)* | **REMOVED (NVA)** | Inventory check trong auto validation, giảm round-trip |
| 6 | *(không có)* | ValidateOrder tự động (Task_ValidateOrder) | **NEW** | Gộp review + fraud check + inventory thành 1 service task tự động |
| 7 | Seller xác nhận đơn (Task SellerConfirm) + Gateway SellerConfirmed | Seller auto-accept đơn (Timer PT2H + AutoAccept) | **AUTOMATED** | SLA timer 2h, seller không cần confirm thủ công, timeout tự xử lý |
| 8 | Tạo waybill (Task_CreateWaybill) | GenerateLabelQR — tem QR digital (Task_GenerateLabelQR) | **AUTOMATED** | Tem QR digital kèm QR code thay waybill giấy |
| 9 | Đếm retry seller (Task_CountRetries) | *(loại bỏ — SLA timer thay thế)* | **REMOVED (NVA)** | Timer PT2H thay logic đếm retry manual |
| 10 | Seller timeout xử lý (Task_SellerTimeout) | *(loại bỏ — auto-accept trước, timer PT2H)* | **REMOVED (NVA)** | Auto-accept 2h, không cần flow timeout riêng |
| 11 | Giữ tiền (Task_HoldPayment) | *(loại bỏ — giữ tiền tích hợp)* | **REMOVED (NVA)** | Payment hold logic nhúng trong ValidateOrder |
| 12 | Bàn giao 3PL (Task_Handover3PL) | Tự động lên lịch 3PL (Task_AutoPickupSched) | **AUTOMATED** | Tự động sắp lịch pickup, không cần bàn giao thủ công |
| 13 | Tạo mã vận đơn + gửi buyer (shipping label + notify) | Tạo tem QR + gửi AI_ETA cho buyer | **AUTOMATED** | AI tính ETA theo tuyến, buyer nhận tự động |
| 14 | *(không có)* | AI dự đoán thời gian giao (Task_AI_ETA) | **NEW** | Tính ETA realtime theo route conditions |
| 15 | *(không có)* | Pre-Delivery Contact — 30 phút trước giao (Task_PreDeliveryContact) | **NEW** | Nhắc buyer qua SMS/app trước khi giao |
| 16 | 3PL giao hàng (Deliver + ConfirmDelivery) | 3PL giao hàng (Task_DeliverOrder) | **KEPT** | Giữ nguyên |
| 17 | Xác nhận nhận hàng (Buyer/Confirmed) + Timer tự confirm nếu seller im lặng | Xác nhận nhận hàng (ConfirmDelivery) + Timer P7D auto-confirm | **KEPT (+ Timer)** | Timer P7D: seller silence → auto-confirm nhận hàng |
| 18 | *(không có)* | Timer P7D — tự xác nhận đã nhận (Timer_7d) | **NEW** | Giải quyết trường hợp seller không phản hồi |

### Tổng hợp phân loại

| Phân loại | Số lượng | Danh sách |
|-----------|----------|-----------|
| **KEPT** | 5 | #1, 2, 16, 17 (partial), #18 |
| **AUTOMATED** | 4 | #7 (AutoAccept + Timer), #8 (QR label), #12 (AutoPickupSched), #13 (AI_ETA + notify) |
| **NEW** | 3 | #6 (ValidateOrder), #14 (AI_ETA), #15 (PreDeliveryContact), #18 (Timer 7d) |
| **REMOVED (NVA)** | 7 | #3 (ReviewOrder), #4 (FraudCheck), #5 (CheckInventory), #9 (CountRetries), #10 (SellerTimeout), #11 (HoldPayment), #12 (Handover3PL) |

---

## 3. So sánh cấu trúc mô hình (Structure Comparison)

| Tiêu chí | AS-IS (file BPMN) | TO-BE (file BPMN) | Thay đổi |
|----------|-------------------|-------------------|----------|
| Số lanes | 5 (Buyer, System, Seller, 3PL, Picker) | 5 (Buyer, System, Seller, 3PL, Picker) | 0 |
| Số activities (tasks) | 26 (user: 7, service: 19) | 22 (user: 5, service: 17) | **-4** (loại bỏ 7 NVA, thêm 3 mới) |
| Số named gateways (decision) | 8 | 5 | **-3** |
| Số all gateways (incl join/split) | 17 | 9 | **-8** |
| Số timer events (SLA) | 0 | 3 (PT2H, PT30M pre-delivery, P7D) | **+3** (mới) |
| Số start events | 1 | 1 | 0 |
| Số end events | 4 | 2 | **-2** (gộp end states) |
| Số sequence flows | 56 | 40 | **-16 (-29%)** |

**Phân bố task theo lane:**

| Lane | AS-IS | TO-BE | Thay đổi |
|------|-------|-------|----------|
| Buyer | 2 | 1 | -1 (gộp confirm) |
| System | 12 | 12 | 0 (thay nhiều task NVA bằng validate/QR) |
| Seller | 4 (Confirm, CountRetries, SellerTimeout, HoldPayment) | 2 (AutoAccept + Timer 2h) | **-2** |
| 3PL | 4 | 5 (thêm PreDeliveryContact + AI_ETA) | +1 |
| Picker | 4 | 2 | -2 |

---

## 4. Bảng so sánh Metrics (Định lượng)

| Metric | AS-IS (ước tính) | TO-BE (expected) | Cải thiện |
|--------|------------------|------------------|-----------|
| **Order acceptance cycle time** | **4 giờ** | **2 giờ (SLA)** | **-50%** |
| **Time label to 3PL pickup** | **6 giờ** | **3 giờ** | **-50%** |
| **Failed delivery first attempt** | **20-25%** | **8%** (PreDeliveryContact) | **-60-67%** |
| **Seller silent orders auto-resolved** | **0%** | **70%** (Timer P7D) | **+70%** |
| **Order processing cost** | **38,900 VND** | **19,000 VND** | **-51%** |
| **Late order rate** | **18%** | **8%** | **-56%** |
| **Buyer satisfaction (CSAT related to order)** | **70%** | **88%** | **+18%** |
| **Named gateways** | **17** | **9** | **-47%** |
| **Sequence flows** | **56** | **40** | **-29%** |

### 4.1. Chi tiết chi phí (ước tính, per order)

| Thành phần chi phí | AS-IS | TO-BE | Thay đổi |
|--------------------|-------|-------|----------|
| Payment gateway fee | 4,000 VND | 4,000 VND | 0 |
| Logistics cost (chặng đầu + sort + last-mile) | 23,300 VND | 10,000 VND | **-13,300** (AI_ETA + route optimization) |
| IT infrastructure & bandwidth | 900 VND | 900 VND | 0 |
| Đóng gói (Seller chịu) | 5,000 VND | 4,000 VND | **-1,000** (tối ưu đóng gói) |
| Dự phòng giao hỏng / COD refusal | 3,500 VND | 500 VND | **-3,000** (PreDeliveryContact + failed delivery 8%) |
| CSKH / Khiếu nại phân bổ | 2,200 VND | 600 VND | **-1,600** (giảm khiếu nại) |
| **TỔNG CHI PHÍ** | **38,900 VND** | **19,000 VND** | **-19,900 (-51%)** |

### 4.2. Cycle time chi tiết (ước tính)

| Giai đoạn | AS-IS | TO-BE (ước tính) | Ghi chú |
|-----------|-------|------------------|---------|
| Buy → Order validation | 30 phút | 5 phút (auto) | Gộp 3 task thành 1 |
| Seller acceptance | 4 giờ | 2 giờ (SLA timer) | Auto-accept |
| Label + handover 3PL | 6 giờ | 3 giờ | QR digital + auto sched |
| Delivery | 2-4 ngày | 2-3 ngày | AI_ETA + pre-delivery contact |
| Confirmation/payment | 48 giờ (nếu seller chậm) | 5 ngày (Timer auto-confirm) | Timer 7d |
| **Tổng trung bình** | **~6 giờ (manual steps)** | **~3 giờ (tự động)** | **-50%** |

---

## 5. ROI — Ước tính đầu tư và thời gian hoàn vốn

> Toàn bộ số liệu mục này là **ước tính** cho mục đích trình bày BA (business case).

### 5.1. Đầu tư ban đầu (one-time, ước tính)

| Hạng mục | Chi phí (tỷ VND) | Ghi chú |
|----------|------------------|---------|
| ValidateOrder Engine (gộp 3 check vào 1) | 1.0 | Rule engine + API integration |
| AutoAccept SLA (Timer 2h) | 0.5 | Timer orchestration |
| GenerateLabelQR (digital label) | 0.6 | Label generation + QR integration |
| AutoPickupSched (3PL API) | 0.7 | Integration với logistic partners |
| AI_ETA Model | 1.2 | Route prediction model |
| PreDeliveryContact (SMS/App notification) | 0.4 | Notification service |
| Timer P7D (auto-confirm) | 0.3 | Timer + settlement logic |
| Testing, QA, rollout | 0.4 | UAT + phased rollout |
| **TỔNG ĐẦU TƯ BAN ĐẦU** | **5.1 tỷ VND** (~212K USD) | |

**Chi phí vận hành hằng năm:** ~1.5 tỷ VND/năm (AI_ETA inference, QR generation, notify/sms, 3PL API).

### 5.2. Lợi ích hàng năm (ước tính)

**Giả định:** ~12 triệu đơn hàng/năm trên Lazada VN.

| Nguồn lợi ích | Công thức | Giá trị (tỷ VND/năm) |
|---------------|-----------|----------------------|
| Tiết kiệm chi phí xử lý đơn | 19,900 VND x 12M orders | 238.8 |
| Giảm failed delivery | 15% x 12M x 10,000 VND/đơn thất bại | 18.0 |
| Giảm late orders (re-ship) | 10% x 12M x 5,000 VND | 6.0 |
| Tăng repeat purchase (better delivery) | 2% revenue uplift x 1,800 tỷ GMV | 36.0 |
| Giảm CS tickets hỏi "đơn tôi đâu" | 5% x 12M x 2,000 VND | 1.2 |
| **Tổng lợi ích tiềm năng** | | **300.0** |
| Lợi ích năm đầu thực thu (50%) | 300.0 x 50% | **150.0** |
| Trừ chi phí vận hành hằng năm | | -1.5 |
| **Lợi ích ròng năm đầu** | | **~148.5 tỷ VND/năm** |

> **Ghi chú số liệu:** Giả định 12 triệu đơn/năm là **thận trọng** so với analysis doc (20 triệu đơn/tháng ≈ 240 triệu/năm) — ước tính lợi ích theo hướng thấp hơn thực tế.

### 5.3. Thời gian hoàn vốn (Payback)

| Kịch bản | Giả định | Payback |
|----------|----------|---------|
| **Cơ sở (Base)** | 12M orders/năm | 5.1 / 148.5 ≈ **~0,41 tháng (~12 ngày)** |
| **Thận trọng (Conservative)** | 4M orders, 50% cost saving | 5.1 / (50.0 - 0.5) ≈ **~1,2 tháng** |

- **Kết luận ROI:** Đây là quy trình có ROI cao nhất trong 10 quy trình — do volume cực lớn (mọi đơn hàng đều đi qua). Đầu tư 5.1 tỷ VND hoàn vốn trong vòng **chưa đầy 2 tháng** ngay cả ở kịch bản thận trọng. Ưu tiên triển khai sớm.

---

## 6. Rủi ro của TO-BE và giải pháp giảm thiểu

| # | Rủi ro | Mức độ | Giải pháp giảm thiểu (Mitigation) |
|---|--------|--------|------------------------------------|
| 1 | **AI_ETA sai lệch — buyer nhận ETA không đúng** | Cao | (a) Dùng historical data + realtime traffic; (b) ETA confidence threshold; (c) Fallback về ETA tĩnh khi AI không chắc | 
| 2 | **Auto-accept làm seller bị charged sai** | Trung bình | (a) Notification seller ngay khi auto-accept; (b) Seller có thể từ chối trong 2h; (c) Dispute window cho seller |
| 3 | **Flood của 3PL integration breaks** | Trung bình | (a) Circuit breaker fallback manual; (b) Multi-provider failover; (c) SLA uptime monitoring |
| 4 | **Buyer không nhận SMS PreDeliveryContact** | Thấp-Trung bình | (a) Đa kênh: SMS + App push + in-app; (b) Fallback 3PL tự gọi; (c) Buyer có thể edit delivery window |
| 5 | **Timer P7D gây tranh chấp với seller** | Trung bình | (a) Quy định rõ ràng SLA trong hợp đồng seller; (b) Audit trail đầy đủ; (c) Escalation cho seller dispute |

---

## 7. Kết luận

1. **TO-BE loại bỏ 7 hoạt động NVA** (ReviewOrder, FraudCheck, CheckInventory, CountRetries, SellerTimeout, HoldPayment, Handover3PL thủ công), **tự động hóa 4 hoạt động** (SellerAccept, LabelQR, PickupSched, Notify+ETA), **thêm 4 hoạt động mới** (ValidateOrder, AI_ETA, PreDeliveryContact, Timer 7d). Đây là sự chuyển dịch rõ nét từ "xử lý đơn thủ công" sang "xử lý đơn tự động hóa cao".
2. **Metrics:** Order acceptance -50% (4h → 2h SLA), failed delivery -60-67% (20-25% → 8%), seller silent auto-resolved +70%, chi phí xử lý đơn -51% (38,900 → 19,000 VND). Sequence flows 56 → 40 (-29%).
3. **ROI:** Đầu tư 5.1 tỷ VND, payback cực nhanh: ~0,4 tháng (cơ sở) / ~1,2 tháng (thận trọng) — quy trình có ROI triển khai nhanh nhất. Năm đầu mang lại ~148,5 tỷ VND lợi ích ròng.
4. **Hành động tiếp theo:** (a) Phê duyệt rollout Phase 1 (AutoAccept + LabelQR + AutoPickupSched ~2.2 tỷ); (b) Thử nghiệm AI_ETA trên 3 thành phố lớn (HCM, HN, ĐN); (c) Xác thực chi phí với team 3PL & logistics; (d) Sync SLA policy mới với Seller Operations.

---

## 8. Tham chiếu

- AS-IS BPMN: `processes/03-order-processing.bpmn`
- TO-BE BPMN: `processes-to-be/03-order-processing.bpmn`

# So sánh AS-IS vs TO-BE: Quy trình Logistics & Giao nhận

> **Quy trình:** 09 - Logistics & Giao nhận (Logistics & Delivery)
> **Nguồn AS-IS:** `processes/09-logistics-delivery.bpmn`
> **Nguồn TO-BE:** `processes-to-be/09-logistics-delivery.bpmn`
> **Ngày phân tích:** 2026-09-03
>
> **Ghi chú số liệu:** Các con số không nằm trong tài liệu gốc đều được **dán nhãn "ước tính"**. Bảng hoạt động và số liệu cấu trúc dựa trên **file BPMN thực tế**.

---

## 1. Tóm tắt thay đổi chính (TO-BE)

| # | Thay đổi TO-BE | Mục tiêu | Kết quả mong đợi |
|---|----------------|----------|------------------|
| 1 | **AI Route Optimization** — Tối ưu tuyến đường shipper real-time dựa trên traffic, khoảng cách, ưu tiên giao | Giảm thời gian last-mile, tăng first-attempt success | First-attempt success 75-80% → 92%; Chi phí last-mile giảm 15% |
| 2 | **Predictive ETA using ML** — Machine learning dự đoán thời gian giao hàng chính xác (traffic + weather + historical data) | Buyer biết chính xác giờ giao, giảm vắng nhà | ETA accuracy: ±1 ngày → ±3 giờ; Giảm giao lại 50% |
| 3 | **Real-time GPS Tracking** — Tích hợp GPS API realtime cho tất cả LEX/3PL, hiển thị vị trí cho Buyer | Tăng tracking accuracy, giảm CS queries | Tracking accuracy 90% → 98%; Giảm CS queries 40% |
| 4 | **Smart Hub Sorting** — Automated sorting tại Hub + AI phân loại theo tuyến giao | Giảm thời gian sort Hub, tăng capacity | Sort time 2-6 giờ → 1-2 giờ; Capacity 75% → 90% |
| 5 | **Automated Pickup Scheduling** — Tự động lịch pickup theo vị trí Seller + capacity LEX/3PL | Giảm thời gian chờ pickup | Pickup time giảm 50%; Seller không cần đặt lịch thủ công |
| 6 | **Drone Delivery Pilot** — Thử nghiệm giao hàng bằng drone cho remote area / province xa | Giảm thời gian giao vùng sâu, giảm chi phí province | Province delivery 5-7 ngày → 1-2 ngày (khu vực drone-eligible) |
| 7 | **Shipper gọi trước 15 phút + SMS** (Predictive ETA) — Gọi/SMS nhắc Buyer trước khi giao | Giảm vắng nhà, tăng first-attempt success | Buyer chuẩn bị nhận hàng, giảm failed delivery -30% |
| 8 | Giảm 20 → 17 tasks, thay thế lane "Shipper" bằng lane "AI Route & Fleet System" | Đơn giản hóa luồng, thêm layer AI | Sequence flows tăng 42 → 49 (thêm nhánh drone + re-route + routing splits) |

---

## 2. Bảng so sánh hoạt động (Activity Comparison Table)

**Phân loại:** KEPT (giữ) | AUTOMATED (tự động hóa) | REMOVED (loại bỏ - NVA) | NEW (thêm mới)

| # | Hoạt động AS-IS | Hoạt động TO-BE (thay thế) | Phân loại | Giải thích thay đổi |
|---|-----------------|----------------------------|-----------|---------------------|
| 1 | Seller đóng gói hàng | Dong goi hang hoa dat chuan (Task_PackGoods) | **KEPT** | Giữ nguyên, chuẩn bị hàng đóng gói đạt chuẩn |
| 2 | Bàn giao hàng cho LEX/3PL | *(loại bỏ — tự động scheduling)* | **REMOVED (NVA)** | Bước bàn giao thủ công bị loại, thay bằng auto-scheduling |
| 3 | LEX lấy hàng tại kho Seller | Yeu cau auto-scheduling lay hang (Task_SchedulePickup) | **AUTOMATED** | Tự động sắp lịch pickup theo vị trí Seller + capacity 3PL |
| 4 | Tạo vận đơn AWB tự động (Task_GenerateAWB) | Tao AWB tu dong + Push tracking info (Task_GenerateAWB) | **KEPT (cải tiến)** | AWB kết hợp push tracking info realtime, gộp 2 bước thành 1 |
| 5 | Phân bổ đơn vị vận chuyển (LEX/3PL) (Task_Assign3PL) | *(loại bỏ — tích hợp trong AI Route Optimization)* | **REMOVED (NVA)** | AI tự phân bổ 3PL theo tuyến + chi phí, không cần task riêng |
| 6 | Tạo lô hàng vận chuyển trên hệ thống (Task_CreateShipment) | *(loại bỏ — tích hợp trong AWB + tracking)* | **REMOVED (NVA)** | Bước tạo shipment gộp vào AWB generation + push tracking |
| 7 | Cập nhật tracking realtime cho Buyer (Task_SendTracking) | Cap nhat vi tri real-time GPS cho Buyer (Task_RealTimeTracking) | **AUTOMATED** | Nâng cấp từ push mã tracking sang GPS real-time live location |
| 8 | Quét barcode & xác nhận tại Hub | *(loại bỏ — Smart Hub Sorting tự xử lý)* | **REMOVED (NVA)** | Smart Hub Sorting tự phân loại bằng AI, không cần scan thủ công |
| 9 | Sắp xếp hàng tại Hub/Trung tâm phân loại (Task_SortWarehouse) | Phan loai hang tai Hub trung chuyen (Task_SortHub) | **AUTOMATED** | AI sorting theo tuyến giao, capacity tăng 75% → 90% |
| 10 | Tối ưu tuyến đường (route optimization) | AI toi uu lo trinh giao hang real-time (Task_RouteOptimize) | **AUTOMATED** | Nâng cấp semi-AI sang AI real-time optimization |
| 11 | Vận chuyển trung chuyển (line-haul) (Task_TransitHub) | Van chuyen lien tinh / duong hang khong (Task_Transit) | **KEPT** | Giữ nguyên, thêm option đường hàng không cho distance xa |
| 12 | Xuất kho giao hàng (out for delivery) (Task_OutForDelivery) | Shipper nhan kien hang -- di giao (Task_OutForDelivery) | **KEPT** | Giữ nguyên |
| 13 | Shipper liên hệ Buyer | Push thong bao lich giao + SMS/In-app alert (Task_NotifyBuyer) | **AUTOMATED** | Thay gọi điện thủ công bằng push notification + SMS tự động 15 phút trước |
| 14 | Giao hàng lần đầu (first attempt) (Task_DeliverToBuyer) | *(giải quyết bởi Gate_DeliveryAttempt + nhánh drone/standard)* | **KEPT** | Giữ logic giao, thêm nhánh drone cho eligible zones |
| 15 | Buyer nhận hàng & ký nhận (POD) (Task_ReceiveGoods) | Nhan hang & kiem tra truc tiep (Task_ReceiveDelivery) | **KEPT** | Giữ nguyên |
| 16 | Thu COD từ Buyer | *(loại bỏ — tích hợp trong ConfirmAccept)* | **REMOVED (NVA)** | COD collection tích hợp trong xác nhận nhận hàng |
| 17 | Cập nhật trạng thái giao thành công (Task_UpdateCOD) | Xac nhan da nhan hang tren App (Task_ConfirmAccept) | **KEPT** | Buyer xác nhận trên App, system tự update |
| 18 | Giao lại do vắng nhà/sai địa chỉ (Task_RetryDelivery) | Hen giao lai — Slot hẹn giờ (qua Gate_RetryLimit) | **KEPT (cải tiến)** | Thêm slot hẹn giờ + predictive ETA giảm likelihood retry |
| 19 | Giao lại lần 2 | *(loại bỏ — giảm tối đa retry xuống 2 lần thay vì 3)* | **REMOVED (NVA)** | Giảm retry limit, giảm chi phí giao lại |
| 20 | Giao lại lần 3 (lần cuối) | *(loại bỏ —gộp vào RetryLimit gateway)* | **REMOVED (NVA)** | Gateway RetryLimit xử lý max 2 lần retry, sau đó hoàn về |
| 21 | Hàng hoàn về kho trung chuyển (Task_ReceiveReturn) | Hang hoan ve kho -- cap nhat he thong (Task_ReturnToSeller) | **KEPT** | Giữ nguyên |
| 22 | Hàng hoàn về Seller | *(gộp vào Task_ReturnToSeller)* | **KEPT** |gộp vào cùng task hoàn hàng |
| 23 | Seller đóng gói lại theo yêu cầu (Task_ReworkParcel) | Dong goi lai / dinh chinh thong tin (Task_ReworkPackage) | **KEPT** | Giữ nguyên |
| 24 | Xử lý tranh chấp vận chuyển | *(loại bỏ — tích hợp trong Task_ReportIssue)* | **REMOVED (NVA)** | Buyer report issue qua App, system tự xử lý |

### Tổng hợp phân loại

| Phân loại | Số lượng | Danh sách |
|-----------|----------|-----------|
| **KEPT** | 11 | #1, 4, 11, 12, 14, 15, 17, 18, 21, 22, 23 |
| **AUTOMATED** | 5 | #3 (AutoPickupSched), #7 (GPS RealTime), #9 (Smart Hub Sort), #10 (AI Route Optimize), #13 (NotifyBuyer SMS) |
| **NEW** | 3 | #25 (Drone Delivery — Task_DroneDelivery), #26 (Standard Routing fallback — Task_StandardRouting), #27 (Hub Re-route — Gate_ReRoute); các task mới thể hiện trong cột TO-BE của bảng trên |
| **REMOVED (NVA)** | 8 | #2 (Bàn giao thủ công), #5 (Assign3PL), #6 (CreateShipment), #8 (Quét barcode Hub), #16 (COD thu thủ công), #19 (Retry lần 2), #20 (Retry lần 3), #24 (Xử lý tranh chấp vận chuyển) |

**Nhận xét:** Quy trình TO-BE giảm mạnh số bước thủ công — từ 12 userTask xuống 7 userTask (-42%), đồng thời tăng serviceTask từ 8 lên 10 (+25%) nhờ AI Route & Fleet System. Lane "Shipper" bị thay thế hoàn toàn bằng "AI Route & Fleet System", thể hiện chuyển đổi từ vận hành thủ công sang vận hành AI-driven. Bổ sung nhánh Drone Delivery cho remote area. Tỷ lệ VA/BVA/NVA: AS-IS **38% / 32% / 30%** (theo báo cáo tổng hợp, tỷ trọng thời gian), TO-BE ước tính **~50% / ~35% / ~15%**.

---

## 3. So sánh cấu trúc mô hình (Structure Comparison)

| Tiêu chí | AS-IS (file BPMN) | TO-BE (file BPMN) | Thay đổi |
|----------|-------------------|-------------------|----------|
| Số lanes | 5 (Seller, Lazada System, LEX/3PL, Shipper, Buyer) | 5 (Seller, AI Route & Fleet System, LEX/3PL Partner, Buyer, Lazada System) | 0 (giữ nguyên, lane "Shipper" → "AI Route & Fleet System") |
| Số activities (tasks) | 20 (user: 12, service: 8) | 17 (user: 7, service: 10) | **-3** (giảm 5 userTask, tăng 2 serviceTask) |
| Số named gateways (decision) | 13 | 19 | **+6** (thêm routing gateways, drone gateways) |
| Số all gateways (incl join/split) | 13 | 19 | **+6** |
| Số timer events (SLA) | 0 | 0 | 0 |
| Số start events | 1 | 1 | 0 |
| Số end events | 2 (Giao thành công, Hàng hoàn về Seller) | 2 (Giao thành công, Hàng hoàn về Seller) | 0 |
| Số sequence flows | 42 | 49 | **+7 (+17%)** (thêm nhánh drone + re-route Hub + routing splits) |
| Độ phức tạp | Trung bình (13 gateways, retry loop 3 lần) | Cao hơn (19 gateways, drone path + re-route + dynamic routing) | Tăng routing complexity, giảm retry complexity |

**Phân bố task theo lane:**

| Lane | AS-IS | TO-BE | Thay đổi |
|------|-------|-------|----------|
| Seller | 4 (PrepareParcel, PackageGoods, SchedulePickup, ReworkParcel) | 3 (PackGoods, SchedulePickup, ReworkPackage) | **-1** (gộp PrepareParcel + PackageGoods) |
| Lazada System | 6 (GenerateAWB, Assign3PL, CreateShipment, SendTracking, ReceiveReturn, UpdateCOD) | 4 (GenerateAWB, RealTimeTracking, NotifyBuyer, ReturnToSeller) | **-2** (loại bỏ Assign3PL, CreateShipment; cải tiến SendTracking → RealTimeTracking) |
| AI Route & Fleet System | 0 | 4 (RouteOptimize, PredictDelivery, DroneDelivery, StandardRouting) | **+4** (lane mới — thay thế Shipper) |
| LEX/3PL | 4 (PickupParcel, SortWarehouse, TransitHub, OutForDelivery) | 3 (SortHub, Transit, OutForDelivery) | **-1** (loại bỏ PickupParcel — dùng auto-scheduling) |
| Shipper | 3 (DeliverToBuyer, RetryDelivery, RescheduleDelivery) | 0 (bị loại — lane Shipper không còn) | **-3** (chuyển sang AI Route & Fleet System) |
| Buyer | 3 (ReceiveGoods, ConfirmReceive, RejectGoods) | 3 (ReceiveDelivery, ConfirmAccept, ReportIssue) | 0 (giữ tương đương, đổi tên) |
| **Tổng** | **20** | **17** | **-3** |

> **Ghi chú:** Số liệu dựa trên **file BPMN live** (processes/09-logistics-delivery.bpmn và processes-to-be/09-logistics-delivery.bpmn), không phải file .bak. File .bak cũ có 36/38 flows và 21/17 tasks nhưng không phản ánh bản gửi bài. AS-IS live: 12 userTask + 8 serviceTask (all unique IDs). TO-BE live: 7 userTask + 10 serviceTask.

---

## 4. Bảng so sánh Metrics (Định lượng)

> Giá trị TO-BE là **ước tính** dựa trên hiệu quả từ AI Route Optimization, GPS real-time, Smart Hub Sorting và Drone pilot.

| Metric | AS-IS (ước tính) | TO-BE (expected) | Cải thiện |
|--------|------------------|------------------|-----------|
| **Cycle time trung bình** | **4,0 ngày** | **1,5 ngày** | **-62,5%** |
| **First-attempt delivery success** | **75-80%** | **92%** | **+12-17 điểm %** |
| **Delivery time trung bình (metro)** | **3-5 ngày** | **1-2 ngày** | **-50%** |
| **Delivery time trung bình (province)** | **5-7 ngày** | **3-5 ngày** (2-3 ngày drone-eligible) | **-30%** |
| **Return/re-delivery rate** | **8-12%** | **4-7%** | **-40%** |
| **Hub sort time** | **2-6 giờ** | **1-2 giờ** | **-67%** |
| **Hub capacity utilization** | **75%** | **90%** | **+15%** |
| **Tracking accuracy (realtime)** | **~90%** | **98%** | **+8%** |
| **Chi phí per parcel (metro)** | **~23,450 VND** | **~18,000 VND** | **-23%** |
| **Chi phí per parcel (province)** | **~40,000 VND** | **~30,000 VND** | **-25%** |
| **Monthly logistics cost** | **~354 tỷ VND** | **~246 tỷ VND** | **-108 tỷ VND (-31%)** |
| **UserTask (thủ công)** | **12** | **7** | **-42%** |
| **Gateways (all)** | **13** | **19** | **+6** (+46%) |
| **Sequence flows** | **42** | **49** | **+7 (+17%)** |

### 4.1. Chi tiết chi phí TO-BE (ước tính, per parcel — metro)

| Thành phần chi phí | AS-IS (VND) | TO-BE (VND) | Thay đổi |
|--------------------|-------------|-------------|----------|
| Lấy hàng (pickup) | 3,000 | 2,000 | **-1,000** (auto-scheduling tối ưu) |
| Sort Hub / Phân loại | 2,000 | 1,000 | **-1,000** (AI sorting) |
| Vận chuyển trung chuyển (line-haul) | 5,000 | 4,000 | **-1,000** (AI route optimization) |
| Giao hàng cuối (last-mile) | 8,000 | 6,000 | **-2,000** (route optimization + reduced retry) |
| COD thu hộ | 1,500 | 1,000 | **-500** (digital POD + e-wallet) |
| Chi phí giao lại (retry) | 3,000 | 1,500 | **-1,500** (first-attempt 75-80%→92%, retry giảm ~50%) |
| Chi phí hàng hoàn (return) | 450 | 200 | **-250** (giảm return rate) |
| Insurance / Bảo hiểm kiện hàng | 500 | 500 | 0 |
| AI Route + GPS tracking (phân bổ) | 0 | 1,000 | **+1,000** (mới — AI infrastructure) |
| Drone infrastructure (phân bổ) | 0 | 800 | **+800** (mới — pilot zones) |
| **TỔNG (Metro)** | **~23,450 VND** | **~18,000 VND** | **-5,450 VND (-23%)** |
| **TỔNG (Province)** | **~40,000 VND** | **~30,000 VND** | **-10,000 VND (-25%)** |

### 4.2. Cycle time chi tiết (ước tính — metro, success path)

| Giai đoạn | AS-IS | TO-BE (ước tính) | Ghi chú |
|-----------|-------|------------------|---------|
| Seller đóng gói + chuẩn bị | 30 phút | 25 phút | Giữ, đóng gói chuẩn LEX |
| Auto-scheduling pickup | 30 phút (đặt lịch) | 10 phút (auto) | Tự động theo vị trí + capacity |
| 3PL lấy hàng tại kho Seller | 20 phút | 15 phút | Pickup tối ưu hơn |
| Tạo AWB + Push tracking | 3 phút | 2 phút | Gộp AWB + tracking push |
| AI Route Optimization | 10 phút | 3 phút | Real-time AI |
| Sort Hub | 4 giờ (2-6h) | 1.5 giờ (1-2h) | AI sorting |
| Vận chuyển trung chuyển | 18 giờ (metro avg) | 12 giờ | Route optimization |
| Out for delivery + NotifyBuyer | 1 giờ + 5 phút | 30 phút + instant | Auto notify 15 phút trước |
| Giao hàng lần đầu | 10 phút | 8 phút | Route planning tốt hơn |
| Buyer nhận + Confirm POD | 5 phút | 3 phút | Digital POD |
| **Tổng success path (metro)** | **~25 giờ ≈ 1.0 ngày** | **~16 giờ ≈ 0.7 ngày** | **-36%** |

---

## 5. ROI — Ước tính đầu tư và thời gian hoàn vốn

> Toàn bộ số liệu mục này là **ước tính** cho mục đích trình bày BA (business case).

### 5.1. Đầu tư ban đầu (one-time, ước tính)

| Hạng mục | Chi phí (tỷ VND) | Ghi chú |
|----------|------------------|---------|
| AI Route Optimization (ML model + traffic API) | 2.5 | Real-time route planning, traffic/weather integration |
| Predictive ETA ML Model | 1.5 | Historical data training + real-time inference |
| Real-time GPS Tracking (tích hợp LEX/3PL) | 2.0 | Standardized GPS API contract cho 3PL, realtime dashboard |
| Smart Hub Sorting (automated + AI) | 3.0 | Automated sorting system + AI classification |
| Automated Pickup Scheduling Engine | 1.0 | Tự động lịch pickup theo vị trí + capacity |
| Drone Delivery Pilot (regulatory + infra) | 4.0 | Regulatory approval, drone fleet pilot, remote zone mapping |
| NotifyBuyer (SMS/App push infrastructure) | 0.5 | Multi-channel notification service |
| Hub Re-route logic + system integration | 0.8 | Gateway logic + Hub capacity API |
| Testing, QA, rollout | 0.7 | UAT, phased rollout, pilot zones |
| **TỔNG ĐẦU TƯ BAN ĐẦU** | **16.0 tỷ VND** (~667K USD, ước tính) | |

**Chi phí vận hành hằng năm:** ~4.0 tỷ VND/năm (AI inference, GPS API, drone lease, Hub automation maintenance).

### 5.2. Lợi ích hàng năm (ước tính)

**Giả định:** ~400,000 kiện hàng/ngày = ~146 triệu kiện/năm trên Lazada VN (theo analysis doc, ~60% đơn hàng Lazada VN qua logistics LEX/3PL).

| Nguồn lợi ích | Công thức | Giá trị (tỷ VND/năm) |
|---------------|-----------|----------------------|
| Tiết kiệm chi phí per parcel (metro) | 5,450 VND x 94.9M metro parcels (65%) | 517.2 |
| Tiết kiệm chi phí per parcel (province) | 10,000 VND x 51.1M province parcels (35%) | 511.0 |
| Giảm retry + return cost (22,5%→8% = 14,5% reduction) | 14,5% x 146M x 15,000 VND | 317.6 |
| Giảm CS queries (tracking accuracy 90%→98%) | 8% x 146M x 2,000 VND | 23.4 |
| Tăng buyer satisfaction → repeat purchase | 2% revenue uplift x 1,800 tỷ GMV | 36.0 |
| **Tổng lợi ích tiềm năng** | | **1,405.2** |
| Lợi ích năm đầu thực thu (40%) | 1,405.2 x 40% | **562.1** |
| Trừ chi phí vận hành hằng năm | | -4.0 |
| **Lợi ích ròng năm đầu** | | **~558.1 tỷ VND/năm** |

### 5.3. Thời gian hoàn vốn (Payback)

| Kịch bản | Giả định | Payback |
|----------|----------|---------|
| **Cơ sở (Base)** | 146M kiện/năm, đạt 40% tiềm năng | 16,0 / 558,1 ≈ **~0,35 tháng (~11 ngày)** |
| **Thận trọng (Conservative)** | 50M kiện/năm, đạt 20% tiết kiệm chi phí | 16,0 / (100,0 - 4,0) ≈ **~2 tháng** |

- **Kết luận ROI:** Quy trình Logistics là quy trình có **volume cao nhất** (~146M kiện/năm) nên ROI cực lớn ngay cả khi phần trăm cải thiện khiêm tốn. Đầu tư 16 tỷ VND hoàn vốn trong vòng **~11 ngày** ở kịch bản cơ sở. Lợi ích ròng 5 năm (cơ sở): (558,1 x 5) - 16,0 - (4,0 x 5) ≈ **~2,754 tỷ VND**.

---

## 6. Rủi ro của TO-BE và giải pháp giảm thiểu

| # | Rủi ro | Mức độ | Giải pháp giảm thiểu (Mitigation) |
|---|--------|--------|------------------------------------|
| 1 | **AI Route Optimization tuyến sai — shipper chạy lộn đường** | Cao | (a) Shadow mode 3 tháng đầu (so sánh AI vs thủ công); (b) Driver feedback loop để retrain model; (c) Fallback về GPS navigation cơ bản khi AI không chắc |
| 2 | **Drone Delivery bị từ chối cấp phép (regulatory)** | Cao | (a) Pilot zone chọn khu vực đã có approval sơ bộ; (b) Hợp tác với đối tượng drone nội địa; (c) Fallback 3PL standard cho vùng chưa được phép |
| 3 | **GPS Tracking realtime gián đoạn (3PL chưa tích hợp)** | Trung bình | (a) Standardized GPS API contract bắt buộc cho 3PL; (b) Fallback polling mechanism khi GPS drop; (c) SLA penalty cho 3PL không đáp ứng |
| 4 | **Smart Hub Sorting sai phân loại Hub** | Trung bình | (a) Gate_HubSortOK + Gate_ReRoute xử lý sai Hub tự động; (b) Confidence threshold 95% cho auto-sort; (c) Manual fallback cho complex packages |
| 5 | **Predictive ETA sai lệch — Buyer nhận ETA không chính xác** | Trung bình | (a) Dùng historical data + realtime traffic + weather; (b) Hiển thị khoảng thời gian (±1 giờ) thay vì giờ chính xác; (c) Auto-update ETA khi có thay đổi route |
| 6 | **Automated Pickup Scheduling thất bại — Seller không nhận lịch** | Thấp-Trung bình | (a) Notification seller qua App + SMS khi lịch được tạo; (b) Seller có thể reject và đề xuất lịch khác; (c) Fallback pickup on-demand |
| 7 | **Volume drone vượt capacity** | Thấp | (a) Pilot zone giới hạn 5-10% đơn province; (b) Capacity monitoring real-time; (c) Auto-redirect về 3PL standard khi drone overload |

---

## 7. Kết luận

1. **TO-BE giảm 3 activities** (từ 20 xuống 17), giảm mạnh **userTask từ 12 xuống 7 (-42%)** — thể hiện chuyển đổi rõ nét từ vận hành thủ công sang AI-driven. Đồng thời tăng serviceTask từ 8 lên 10 (+25%) nhờ layer AI Route & Fleet System. Bổ sung nhánh Drone Delivery cho remote area — một innovation lớn trong logistics.
2. **Metrics:** Cycle time giảm 62,5% (4,0 ngày → 1,5 ngày), first-attempt delivery success tăng 75-80% → 92% (+12-17 điểm %), delivery time metro giảm 50% (3-5 ngày → 1-2 ngày), return rate giảm 40% (8-12% → 4-7%), chi phí per parcel metro giảm 23% (23,450 → 18,000 VND), province giảm 25% (40,000 → 30,000 VND). Hub sort time giảm 67% (2-6 giờ → 1-2 giờ). Tracking accuracy tăng 90% → 98%. Gateways 13→19 (+46%), flows 42→49 (+17%) — routing complexity tăng nhưng retry loop giảm.
3. **ROI:** Đầu tư ban đầu ~16 tỷ VND (ước tính), payback cực nhanh: **~11 ngày** (cơ sở) / **~2 tháng** (thận trọng) — do volume ~146M kiện/năm tạo leverage rất lớn. Lợi ích ròng 5 năm ~2,754 tỷ VND (ước tính). Đây là quy trình **ROI cao nhất** trong tất cả các quy trình do sheer volume.
4. **Hành động tiếp theo:** (a) Phê duyệt Phase 1 (AI Route + GPS Tracking + AutoPickupSched ~5.5 tỷ); (b) Khởi động pilot drone delivery tại 1-2 tỉnh đã có regulatory approval; (c) Đàm phán standardized GPS API contract với LEX/3PL partners; (d) Thu thập historical delivery data cho ETA ML training; (e) Xác nhận chi phí với đội Logistics Operations & 3PL.

---

## 8. Tham chiếu

- AS-IS BPMN: `processes/09-logistics-delivery.bpmn`
- TO-BE BPMN: `processes-to-be/09-logistics-delivery.bpmn`

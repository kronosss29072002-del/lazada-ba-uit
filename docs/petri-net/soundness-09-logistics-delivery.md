# Kiểm chứng Soundness — Logistics & Giao nhận

**File:** `processes-to-be/09-logistics-delivery.bpmn`
**Phương pháp:** BPMN → WF-net (van der Aalst, 1998), phân tích reachability graph.

## Thống kê mô hình

| Chỉ số | Giá trị |
|--------|---------|
| Places (sequence flows) | 37 |
| Transitions (tasks + gateways) | 31 |
| Final places | 3 |
| Reachable markings (cap=4) | 42 |
| Max tokens trong 1 marking | 1 |
| Final places | Flow_Confirm_End, Flow_Report_End, Flow_Return_End |

## Kết quả soundness

| Thuộc tính | Kết quả | Bằng chứng |
|------------|---------|-----------|
| Option to Complete | ✅ PASS | 42/42 markings reachable có thể tới completion |
| Proper Completion | ✅ PASS | terminal markings không hợp lệ: 0 |
| No Dead Transitions | ✅ PASS | dead transitions: không có |

**Overall:** ✅ SOUND

> **Ghi chú:** Các vòng lặp có điều kiện dữ liệu (data-based loop) được phân tích trong không gian giới hạn với mỗi place giữ tối đa 1 token và mỗi lần lặp ≤ cap (cap=4). Hai vòng lặp chính — (1) `Gate_PickupResult` → `Task_ReworkPackage` → `Task_PackGoods` (lặp lại khi đóng gói chưa đạt chuẩn, tối đa 3 lần), và (2) `Gate_ReRoute` → `Task_SortHub` (phân loại lại khi sai Hub, tối đa 3 lần) — tương ứng với bộ đếm đã khai báo trong mô hình TO-BE.

## Bảng minh họa vài marking

WF-net này là **1-bounded** (mọi trạng thái reachable có đúng 1 token). Dưới đây là các marking đại diện dọc theo các nhánh chính:

| # | Marking (place mang token) | Ý nghĩa |
|---|----------------------------|---------|
| $M_0$ | `{Flow_S1_Pack}` | Khởi tạo: đơn hàng được xác nhận, bắt đầu đóng gói |
| $M_1$ | `{Flow_Schedule_PickupGate}` | Sau `Task_SchedulePickup`, chờ kết quả lấy hàng tại `Gate_PickupResult` |
| $M_2$ | `{Flow_Predict_GateDrone}` | Sau `Task_PredictDelivery`, chờ AI quyết định phương thức giao tại `Gate_DroneEligible` |
| $M_3$ | `{Flow_DroneYes_Drone}` | Nhánh Drone Express: `Gate_DroneEligible` chọn drone |
| $M_4$ | `{Flow_Sort_GateOK}` | Sau `Task_SortHub`, chờ kiểm tra phân loại tại `Gate_HubSortOK` |
| $M_5$ | `{Flow_Out_DeliverGate}` | Sau `Task_OutForDelivery`, chờ kết quả giao hàng tại `Gate_DeliveryAttempt` |
| $M_6$ | `{Flow_AcceptYes_Confirm}` | Buyer chấp nhận hàng → `Task_ConfirmAccept` |
| $M_7$ | `{Flow_AcceptNo_Report}` | Buyer từ chối hàng → `Task_ReportIssue` (đổi trả) |
| $M_8$ | `{Flow_RetryNo_Reschedule}` | Chưa đủ 3 lần giao → hẹn lại lịch lấy hàng (`Task_SchedulePickup`) |
| $M_9$ | `{Flow_RetryYes_Return}` | Đã thử giao ≥ 3 lần → hàng hoàn về kho `Task_ReturnToSeller` |

Mọi $M_i$ đều có đường đi tới một marking cuối (một trong 3 final places — `Flow_Confirm_End`, `Flow_Report_End`, hoặc `Flow_Return_End`); không có marking cuối "kẹt" nào chứa token leftover.

## Bảng mapping BPMN → WF-net

| # | BPMN element | Transition | Kind |
|---|--------------|------------|------|
| T1 | `Task_PackGoods` | $t_1$ | task |
| T2 | `Task_SchedulePickup` | $t_2$ | task |
| T3 | `Task_ReworkPackage` | $t_3$ | task |
| T4 | `Task_RouteOptimize` | $t_4$ | task |
| T5 | `Task_PredictDelivery` | $t_5$ | task |
| T6 | `Task_DroneDelivery` | $t_6$ | task |
| T7 | `Task_StandardRouting` | $t_7$ | task |
| T8 | `Task_SortHub` | $t_8$ | task |
| T9 | `Task_Transit` | $t_9$ | task |
| T10 | `Task_OutForDelivery` | $t_{10}$ | task |
| T11 | `Task_ReceiveDelivery` | $t_{11}$ | task |
| T12 | `Task_ConfirmAccept` | $t_{12}$ | task |
| T13 | `Task_ReportIssue` | $t_{13}$ | task |
| T14 | `Task_GenerateAWB` | $t_{14}$ | task |
| T15 | `Task_RealTimeTracking` | $t_{15}$ | task |
| T16 | `Task_NotifyBuyer` | $t_{16}$ | task |
| T17 | `Task_ReturnToSeller` | $t_{17}$ | task |
| T18 | `Gate_PickupResult` | $t_{18}$ | XOR |
| T19 | `Gate_DroneEligible` | $t_{19}$ | XOR |
| T20 | `Gate_HubSortOK` | $t_{20}$ | XOR |
| T21 | `Gate_ReRoute` | $t_{21}$ | XOR |
| T22 | `Gate_DeliveryAttempt` | $t_{22}$ | XOR |
| T23 | `Gate_AcceptGoods` | $t_{23}$ | XOR |
| T24 | `Gate_RetryLimit` | $t_{24}$ | XOR |
| T25 | `Join_Task_SortHub_1` | $t_{25}$ | XOR |
| T26 | `Join_Task_Transit_2` | $t_{26}$ | XOR |
| T27 | `Join_Task_RealTimeTracking_3` | $t_{27}$ | XOR |
| T28 | `Join_Task_NotifyBuyer_4` | $t_{28}$ | XOR |
| T29 | `Join_Task_PackGoods_5` | $t_{29}$ | XOR |
| T30 | `Split_Task_GenerateAWB_1` | $t_{30}$ | XOR |
| T31 | `Split_Gate_PickupResult_2` | $t_{31}$ | XOR |

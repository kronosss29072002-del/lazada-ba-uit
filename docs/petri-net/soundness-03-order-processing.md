# Kiểm chứng Soundness — Xử lý Đơn hàng Online Lazada

**File:** `processes/03-order-processing.bpmn`
**Phương pháp:** BPMN → WF-net (van der Aalst, 1998), phân tích reachability graph.

## Thống kê mô hình

| Chỉ số | Giá trị |
|--------|---------|
| Places (sequence flows) | 56 |
| Transitions (tasks + gateways) | 43 |
| Final places | 3 |
| Reachable markings (cap=4) | 56 |
| Max tokens trong 1 marking | 1 |
| Final places | Flow_Cancel_End, Flow_Refund_End, Flow_Release_End |

## Kết quả soundness

| Thuộc tính | Kết quả | Bằng chứng |
|------------|---------|-----------|
| Option to Complete | ✅ PASS | 56/56 markings reachable có thể tới completion |
| Proper Completion | ✅ PASS | terminal markings không hợp lệ: 0 |
| No Dead Transitions | ✅ PASS | dead transitions: không có |

**Overall:** ✅ SOUND

> **Ghi chú:** Các vòng lặp có điều kiện dữ liệu (data-based loop) được phân tích trong không gian giới hạn với mỗi place giữ tối đa 1 token và mỗi lần lặp ≤ cap (cap=4). Điều này tương ứng với việc vòng lặp được chặn bởi bộ đếm (ví dụ `resubmitCount ≤ 3`) như đã khai báo trong mô hình TO-BE.

## Bảng minh họa vài marking

WF-net này là **1-bounded** (mọi trạng thái reachable có đúng 1 token). Dưới đây là các marking đại diện dọc theo các nhánh chính:

| # | Marking (place mang token) | Ý nghĩa |
|---|----------------------------|---------|
| $M_0$ | `{Flow_Checkout_Validate}` | Khởi tạo: Buyer đặt hàng |
| $M_1$ | `{Flow_Review_Pay}` | Sau `Task_ReviewOrder`, chờ thanh toán |
| $M_2$ | `{Flow_Pay_Gate}` | Tại `Gate_PaymentMethod` (COD / online) |
| $M_3$ | `{Flow_Fraud_Gate}` | Tại `Gate_FraudCheck` (kiểm tra gian lận AI) |
| $M_4$ | `{Flow_Pickup_CancelGate}` | Tại `Gate_CancelRequest` sau pickup (Buyer có hủy không) |
| $M_5$ | `{Flow_Retry_Count}` | Vòng lặp giao lại: tại `Gate_RetryLimit` (chặn ≤ 3 lần) |
| $M_6$ | `{Flow_Confirm_Gate}` | Tại `Gate_BuyerConfirm` (nhận hàng / auto-confirm 7 ngày) |
| $M_7$ | `{Flow_Release_End}` | **Marking cuối hợp lệ** → `End_Delivered` (giải ngân Seller) |
| $M_8$ | `{Flow_Refund_End}` | **Marking cuối hợp lệ** → `End_Refunded` |

Mọi $M_i$ đều có đường đi tới một marking cuối (một trong 3 final places); không có marking cuối "kẹt" nào chứa token leftover.

## Bảng mapping BPMN → WF-net

| # | BPMN element | Transition | Kind |
|---|--------------|------------|------|
| T1 | `Task_ReviewOrder` | $t_1$ | task |
| T2 | `Task_Pay` | $t_2$ | task |
| T3 | `Task_ReceiveGoods` | $t_3$ | task |
| T4 | `Task_ConfirmReceipt` | $t_4$ | task |
| T5 | `Task_CancelOrder` | $t_5$ | task |
| T6 | `Task_ValidateOrder` | $t_6$ | task |
| T7 | `Task_LockInventory` | $t_7$ | task |
| T8 | `Task_FraudCheck` | $t_8$ | task |
| T9 | `Task_CheckInventory` | $t_9$ | task |
| T10 | `Task_CreateWaybill` | $t_10$ | task |
| T11 | `Task_TrackDelivery` | $t_11$ | task |
| T12 | `Task_CountRetries` | $t_12$ | task |
| T13 | `Task_AutoConfirm` | $t_13$ | task |
| T14 | `Task_SellerTimeout` | $t_14$ | task |
| T15 | `Task_ReleasePayment` | $t_15$ | task |
| T16 | `Task_AutoCancel` | $t_16$ | task |
| T17 | `Task_Notify` | $t_17$ | task |
| T18 | `Task_AutoRefund` | $t_18$ | task |
| T19 | `Task_ConfirmOrder` | $t_19$ | task |
| T20 | `Task_PackageGoods` | $t_20$ | task |
| T21 | `Task_Handover3PL` | $t_21$ | task |
| T22 | `Task_Pickup` | $t_22$ | task |
| T23 | `Task_DeliverAttempt` | $t_23$ | task |
| T24 | `Task_VerifyPayment` | $t_24$ | task |
| T25 | `Task_HoldPayment` | $t_25$ | task |
| T26 | `Task_ExecuteRefund` | $t_26$ | task |
| T27 | `Gate_PaymentMethod` | $t_27$ | XOR |
| T28 | `Gate_FraudCheck` | $t_28$ | XOR |
| T29 | `Gate_InventoryCheck` | $t_29$ | XOR |
| T30 | `Gate_SellerConfirm` | $t_30$ | XOR |
| T31 | `Gate_CancelRequest` | $t_31$ | XOR |
| T32 | `Gate_RetryLimit` | $t_32$ | XOR |
| T33 | `Gate_BuyerConfirm` | $t_33$ | XOR |
| T34 | `Gate_CancelSplit` | $t_34$ | XOR |
| T35 | `Join_Task_LockInventory_1` | $t_35$ | XOR |
| T36 | `Join_Task_TrackDelivery_2` | $t_36$ | XOR |
| T37 | `Join_Task_ReleasePayment_3` | $t_37$ | XOR |
| T38 | `Join_Task_AutoCancel_4` | $t_38$ | XOR |
| T39 | `Join_Task_Notify_5` | $t_39$ | XOR |
| T40 | `Join_Task_DeliverAttempt_6` | $t_40$ | XOR |
| T41 | `Split_Task_CreateWaybill_1` | $t_41$ | XOR |
| T42 | `Split_Task_ConfirmOrder_2` | $t_42$ | XOR |
| T43 | `Split_Task_DeliverAttempt_3` | $t_43$ | XOR |

# Kiểm chứng Soundness — Thanh toán & Đối soát

**File:** `processes-to-be/08-payment-settlement.bpmn`
**Phương pháp:** BPMN → WF-net (van der Aalst, 1998), phân tích reachability graph.

## Thống kê mô hình

| Chỉ số | Giá trị |
|--------|---------|
| Places (sequence flows) | 34 |
| Transitions (tasks + gateways) | 24 |
| Final places | 4 |
| Reachable markings (cap=4) | 38 |
| Max tokens trong 1 marking | 1 |
| Final places | Flow_Statement_End, Flow_Refund_End, Flow_BankYes_End, Flow_BankNo_Retry (loop back) |

## Kết quả soundness

| Thuộc tính | Kết quả | Bằng chứng |
|------------|---------|-----------|
| Option to Complete | ✅ PASS | 38/38 markings reachable có thể tới completion |
| Proper Completion | ✅ PASS | terminal markings không hợp lệ: 0 |
| No Dead Transitions | ✅ PASS | dead transitions: không có |

**Overall:** ✅ SOUND

> **Ghi chú:** WF-net có 2 end events (`EndEvent_Settled` và `EndEvent_Refunded`). Parallel split tại `Task_UpdateWallet` (2 outgoing flows: `Flow_Wallet_Statement` + `Flow_Wallet_Check`) tạo 2 nhánh song song đều hội tụ về `EndEvent_Settled` dưới dạng AND-join. Vòng lặp retry tại `Gate_BankOK` (`Flow_BankNo_Retry` quay lại `Task_Withdraw`) bị chặn bởi điều kiện dữ liệu (số lần retry tối đa trong hệ thống, `retryCount ≤ 3`).

## Bảng minh họa vài marking

WF-net này là **1-bounded** (mọi trạng thái reachable có tối đa 1 token tại mỗi place). Dưới đây là các marking đại diện dọc theo các nhánh chính:

| # | Marking (place mang token) | Ý nghĩa |
|---|----------------------------|---------|
| $M_0$ | `{Flow_S1_Select}` | Khởi tạo: Buyer bắt đầu quá trình thanh toán đơn hàng |
| $M_1$ | `{Flow_Select_GateType}` | Sau `Task_SelectPayment`, chờ rẽ nhánh tại `Gate_PaymentType` (COD / Online) |
| $M_2$ | `{Flow_TypeOnline_Pay}` | Nhánh Online: chờ `Task_PayOnline` xử lý qua cổng thanh toán |
| $M_3$ | `{Flow_Risk_GateRisk}` | Sau `Task_RiskScore`, chờ AI đánh giá rủi ro tại `Gate_HighRisk` |
| $M_4$ | `{Flow_Approve_Hold}` | Nhánh an toàn: AI phê duyệt tự động, tiến hành giữ tiền trong Escrow |
| $M_5$ | `{Flow_Hold_GateTrust}` | Tiền đã vào Escrow, chờ kiểm tra mức độ tin cậy Seller (`Gate_SellerTrust`) |
| $M_6$ | `{Flow_OK_Commission}` | Đối soát khớp 100%, chờ tính hoa hồng & phí tại `Task_CalcCommission` |
| $M_7$ | `{Flow_Wallet_Statement}` | Đã cập nhật Ví, chờ gửi bảng đối soát điện tử tự động hàng tháng |
| $M_8$ | `{Flow_Statement_End}` | **Marking cuối hợp lệ** → `EndEvent_Settled` (tiền về Ví Seller, đối soát hoàn tất) |
| $M_9$ | `{Flow_Refund_End}` | **Marking cuối hợp lệ** → `EndEvent_Refunded` (hoàn tiền tự động về Buyer) |

Mọi $M_i$ đều có đường đi tới một marking cuối (một trong 4 final places); không có marking cuối "kẹt" nào chứa token leftover.

## Bảng mapping BPMN → WF-net

| # | BPMN element | Transition | Kind |
|---|--------------|------------|------|
| T1 | `Task_SelectPayment` | $t_1$ | task |
| T2 | `Task_PayCOD` | $t_2$ | task |
| T3 | `Task_PayOnline` | $t_3$ | task |
| T4 | `Task_ReceiveGoods` | $t_4$ | task |
| T5 | `Task_ReceiveRefund` | $t_5$ | task |
| T6 | `Task_RiskScore` | $t_6$ | task |
| T7 | `Task_BlockTransaction` | $t_7$ | task |
| T8 | `Task_ApproveAuto` | $t_8$ | task |
| T9 | `Task_FraudAlert` | $t_9$ | task |
| T10 | `Task_HoldEscrow` | $t_{10}$ | task |
| T11 | `Task_InstantSettle` | $t_{11}$ | task |
| T12 | `Task_AutoReconcile` | $t_{12}$ | task |
| T13 | `Task_CalcCommission` | $t_{13}$ | task |
| T14 | `Task_UpdateWallet` | $t_{14}$ | task |
| T15 | `Task_SendStatement` | $t_{15}$ | task |
| T16 | `Task_CheckWallet` | $t_{16}$ | task |
| T17 | `Task_Withdraw` | $t_{17}$ | task |
| T18 | `Gate_PaymentType` | $t_{18}$ | XOR |
| T19 | `Gate_CODVerify` | $t_{19}$ | XOR |
| T20 | `Gate_HighRisk` | $t_{20}$ | XOR |
| T21 | `Gate_SellerTrust` | $t_{21}$ | XOR |
| T22 | `Gate_ReconcileOK` | $t_{22}$ | XOR |
| T23 | `Gate_RefundOK` | $t_{23}$ | XOR |
| T24 | `Gate_BankOK` | $t_{24}$ | XOR |

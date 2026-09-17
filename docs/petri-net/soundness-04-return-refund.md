# Kiểm chứng Soundness — Hoàn trả & Refund

**File:** `processes/04-return-refund.bpmn`
**Phương pháp:** BPMN → WF-net (van der Aalst, 1998), phân tích reachability graph.

## Thống kê mô hình

| Chỉ số | Giá trị |
|--------|---------|
| Places (sequence flows) | 42 |
| Transitions (tasks + gateways) | 30 |
| Final places | 4 |
| Reachable markings (cap=4) | 42 |
| Max tokens trong 1 marking | 1 |
| Final places | Flow_Eligible_Reject, Flow_Inspect_Reject, Flow_Notify_End, Flow_Reject_Notify |

## Kết quả soundness

| Thuộc tính | Kết quả | Bằng chứng |
|------------|---------|-----------|
| Option to Complete | ✅ PASS | 42/42 markings reachable có thể tới completion |
| Proper Completion | ✅ PASS | terminal markings không hợp lệ: 0 |
| No Dead Transitions | ✅ PASS | dead transitions: không có |

**Overall:** ✅ SOUND

> **Ghi chú:** Các vòng lặp có điều kiện dữ liệu (data-based loop) được phân tích trong không gian giới hạn với mỗi place giữ tối đa 1 token và mỗi lần lặp ≤ cap (cap=4). Điều này tương ứng với việc vòng lặp được chặn bởi bộ đếm (ví dụ `resubmitCount ≤ 3`) như đã khai báo trong mô hình TO-BE.

## Bảng minh họa vài marking

WF-net này là **1-bounded** (mọi trạng thái reachable có đúng 1 token). Dưới đây là các marking đại diện dọc theo các nhánh chính:

| # | Marking (place mang token) | Ý nghĩa |
|---|----------------------------|---------|
| $M_0$ | `{Flow_Start_Submit}` | Khởi tạo: Buyer gửi yêu cầu đổi trả |
| $M_1$ | `{Flow_Submit_Window}` | Tại `Gate_ReturnWindow` (còn hạn hoàn trả?) |
| $M_2$ | `{Flow_Eligibility_Gate}` | Sau `Task_CheckEligibility`, tại `Gate_Eligible` |
| $M_3$ | `{Flow_Triage_Quality}` | Tại `Gate_EvidenceQuality` trong vòng lặp bằng chứng |
| $M_4$ | `{Flow_Approve_Gate}` | Tại `Gate_Approve` (CS phê duyệt) |
| $M_5$ | `{Flow_Pickup_Gate}` | Vòng lặp pickup: tại `Gate_PickupRetry` |
| $M_6$ | `{Flow_Inspect_Gate}` | Tại `Gate_InspectionPass` (kiểm định hàng hoàn) |
| $M_7$ | `{Flow_Notify_End}` | **Marking cuối hợp lệ** → `End_Refunded` (hoàn tiền hoàn tất) |
| $M_8$ | `{Flow_Eligible_Reject}` | **Marking cuối hợp lệ** → `End_Rejected` |

Mọi $M_i$ đều có đường đi tới một marking cuối (một trong 4 final places); không có marking cuối "kẹt" nào chứa token leftover.

## Bảng mapping BPMN → WF-net

| # | BPMN element | Transition | Kind |
|---|--------------|------------|------|
| T1 | `Task_SubmitRequest` | $t_1$ | task |
| T2 | `Gate_ReturnWindow` | $t_2$ | XOR |
| T3 | `Task_HandleLateRequest` | $t_3$ | task |
| T4 | `Task_UploadEvidence` | $t_4$ | task |
| T5 | `Task_HandoverReturn` | $t_5$ | task |
| T6 | `Task_CheckEligibility` | $t_6$ | task |
| T7 | `Task_TriageEvidence` | $t_7$ | task |
| T8 | `Task_NotifyStatus` | $t_8$ | task |
| T9 | `Task_ReviewEvidence` | $t_9$ | task |
| T10 | `Task_SchedulePickup` | $t_10$ | task |
| T11 | `Task_PickupReturn` | $t_11$ | task |
| T12 | `Gate_PickupRetry` | $t_12$ | XOR |
| T13 | `Task_ReschedulePickup` | $t_13$ | task |
| T14 | `Task_InspectItem` | $t_14$ | task |
| T15 | `Task_ProcessRefund` | $t_15$ | task |
| T16 | `Gate_Eligible` | $t_16$ | XOR |
| T17 | `Gate_LowRisk` | $t_17$ | XOR |
| T18 | `Gate_EvidenceQuality` | $t_18$ | XOR |
| T19 | `Gate_RefundMethod` | $t_19$ | XOR |
| T20 | `Gate_InspectionPass` | $t_20$ | XOR |
| T21 | `Gate_Approve` | $t_21$ | XOR |
| T22 | `Join_Task_UploadEvidence_1` | $t_22$ | XOR |
| T23 | `Join_Task_HandoverReturn_2` | $t_23$ | XOR |
| T24 | `Join_Task_CheckEligibility_3` | $t_24$ | XOR |
| T25 | `Join_Task_NotifyStatus_4` | $t_25$ | XOR |
| T26 | `Join_Task_ReviewEvidence_5` | $t_26$ | XOR |
| T27 | `Join_Task_PickupReturn_6` | $t_27$ | XOR |
| T28 | `Join_Task_ProcessRefund_7` | $t_28$ | XOR |
| T29 | `Split_Task_TriageEvidence_1` | $t_29$ | XOR |
| T30 | `Split_Task_ReviewEvidence_2` | $t_30$ | XOR |

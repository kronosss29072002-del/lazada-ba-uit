# Kiểm chứng Soundness — Quản lý Tranh chấp

**File:** `processes/02-dispute-management.bpmn`
**Phương pháp:** BPMN → WF-net (van der Aalst, 1998), phân tích reachability graph.

## Thống kê mô hình

| Chỉ số | Giá trị |
|--------|---------|
| Places (sequence flows) | 37 |
| Transitions (tasks + gateways) | 27 |
| Final places | 6 |
| Reachable markings (cap=4) | 37 |
| Max tokens trong 1 marking | 1 |
| Final places | Flow_Compromise_Settle, Flow_SLA_No, Flow_Senior_Settle, Flow_Simple_Auto, Flow_Wins_Not, Flow_Wins_Settle |

## Kết quả soundness

| Thuộc tính | Kết quả | Bằng chứng |
|------------|---------|-----------|
| Option to Complete | ✅ PASS | 37/37 markings reachable có thể tới completion |
| Proper Completion | ✅ PASS | terminal markings không hợp lệ: 0 |
| No Dead Transitions | ✅ PASS | dead transitions: không có |

**Overall:** ✅ SOUND

> **Ghi chú:** Các vòng lặp có điều kiện dữ liệu (data-based loop) được phân tích trong không gian giới hạn với mỗi place giữ tối đa 1 token và mỗi lần lặp ≤ cap (cap=4). Điều này tương ứng với việc vòng lặp được chặn bởi bộ đếm (ví dụ `resubmitCount ≤ 3`) như đã khai báo trong mô hình TO-BE.

## Bảng minh họa vài marking

WF-net này là **1-bounded** (mọi trạng thái reachable có đúng 1 token). Dưới đây là các marking đại diện dọc theo các nhánh chính:

| # | Marking (place mang token) | Ý nghĩa |
|---|----------------------------|---------|
| $M_0$ | `{Flow_Start_Create}` | Khởi tạo: tranh chấp được tạo ra |
| $M_1$ | `{Flow_Collect_Triage}` | Sau `Task_CollectData`, chờ AI phân loại (`Task_AuthTriage`) |
| $M_2$ | `{Flow_Triage_History}` | Nhánh phức tạp: tại `Gate_SellerHistory` |
| $M_3$ | `{Flow_Notify_SLA}` | Sau `Task_NotifyParties`, chờ `Gate_SLA` (Seller phản hồi 48h) |
| $M_4$ | `{Flow_Evidence_Solid}` | Tại `Gate_EvidenceSolid` trong vòng lặp bổ sung bằng chứng |
| $M_5$ | `{Flow_Decide_Wins}` | Nhánh quyết định: tại `Gate_BuyerWins` |
| $M_6$ | `{Flow_Wins_Settle}` | **Marking cuối hợp lệ** → `End_Settled` (Buyer thắng) |
| $M_7$ | `{Flow_Wins_Not}` | **Marking cuối hợp lệ** → `End_Rejected` (bác bỏ) |

Mọi $M_i$ đều có đường đi tới một marking cuối (một trong 6 final places); không có marking cuối "kẹt" nào chứa token leftover.

## Bảng mapping BPMN → WF-net

| # | BPMN element | Transition | Kind |
|---|--------------|------------|------|
| T1 | `Task_CreateDispute` | $t_1$ | task |
| T2 | `Task_ReplyEvidence` | $t_2$ | task |
| T3 | `Gate_EvidenceSolid` | $t_3$ | XOR |
| T4 | `Task_RequestMoreEvidence` | $t_4$ | task |
| T5 | `Task_CollectData` | $t_5$ | task |
| T6 | `Task_AuthTriage` | $t_6$ | task |
| T7 | `Gate_SellerHistory` | $t_7$ | XOR |
| T8 | `Task_CheckSLAHistory` | $t_8$ | task |
| T9 | `Task_NotifyParties` | $t_9$ | task |
| T10 | `Task_SellerReply` | $t_10$ | task |
| T11 | `Task_ReviewCase` | $t_11$ | task |
| T12 | `Task_Decide` | $t_12$ | task |
| T13 | `Task_Escalate` | $t_13$ | task |
| T14 | `Task_SeniorReview` | $t_14$ | task |
| T15 | `Gate_SLA` | $t_15$ | XOR |
| T16 | `Gate_EvidenceComplete` | $t_16$ | XOR |
| T17 | `Gate_SimpleCase` | $t_17$ | XOR |
| T18 | `Gate_BuyerWins` | $t_18$ | XOR |
| T19 | `Gate_Compromise` | $t_19$ | XOR |
| T20 | `Gate_SeniorDecision` | $t_20$ | XOR |
| T21 | `Join_Task_ReplyEvidence_1` | $t_21$ | XOR |
| T22 | `Join_Task_RequestMoreEvidence_2` | $t_22$ | XOR |
| T23 | `Join_Task_NotifyParties_3` | $t_23$ | XOR |
| T24 | `Join_Task_ReviewCase_4` | $t_24$ | XOR |
| T25 | `Split_Task_AuthTriage_1` | $t_25$ | XOR |
| T26 | `Split_Task_SellerReply_2` | $t_26$ | XOR |
| T27 | `Split_Task_Decide_3` | $t_27$ | XOR |

# Kiểm chứng Soundness — Quy trình Chăm sóc Khách hàng

**File:** `processes/05-customer-service.bpmn`
**Phương pháp:** BPMN → WF-net (van der Aalst, 1998), phân tích reachability graph.

## Thống kê mô hình

| Chỉ số | Giá trị |
|--------|---------|
| Places (sequence flows) | 39 |
| Transitions (tasks + gateways) | 29 |
| Final places | 3 |
| Reachable markings (cap=4) | 39 |
| Max tokens trong 1 marking | 1 |
| Final places | Flow_Log_End, Flow_SLA_Expired, Flow_Verify_Fail |

## Kết quả soundness

| Thuộc tính | Kết quả | Bằng chứng |
|------------|---------|-----------|
| Option to Complete | ✅ PASS | 39/39 markings reachable có thể tới completion |
| Proper Completion | ✅ PASS | terminal markings không hợp lệ: 0 |
| No Dead Transitions | ✅ PASS | dead transitions: không có |

**Overall:** ✅ SOUND

> **Ghi chú:** Các vòng lặp có điều kiện dữ liệu (data-based loop) được phân tích trong không gian giới hạn với mỗi place giữ tối đa 1 token và mỗi lần lặp ≤ cap (cap=4). Điều này tương ứng với việc vòng lặp được chặn bởi bộ đếm (ví dụ `resubmitCount ≤ 3`) như đã khai báo trong mô hình TO-BE.

## Bảng minh họa vài marking

WF-net này là **1-bounded** (mọi trạng thái reachable có đúng 1 token). Dưới đây là các marking đại diện dọc theo các nhánh chính:

| # | Marking (place mang token) | Ý nghĩa |
|---|----------------------------|---------|
| $M_0$ | `{Flow_Start_Describe}` | Khởi tạo: khách hàng liên hệ |
| $M_1$ | `{Flow_SLA_Gate}` | Tại `Gate_SLAValid` (SLA còn hạn?) |
| $M_2$ | `{Flow_Fetch_Gate}` | Tại `Gate_BotCanHandle` (chatbot có xử lý được?) |
| $M_3$ | `{Flow_BotResolve_Gate}` | Tại `Gate_BotSuccess` (chatbot thành công?) |
| $M_4$ | `{Flow_Verify_Gate}` | Tại `Gate_VerifyOK` (xác minh danh tính) |
| $M_5$ | `{Flow_T1_Resolve_Gate}` | Tại `Gate_T1Resolved` (Tier 1 giải quyết được?) |
| $M_6$ | `{Flow_Wait_Timeout}` | Vòng lặp chờ phản hồi: tại `Gate_Timeout` |
| $M_7$ | `{Flow_Log_End}` | **Marking cuối hợp lệ** → `End_Resolved` (ghép CSAT + log) |
| $M_8$ | `{Flow_SLA_Expired}` | **Marking cuối hợp lệ** → `End_SLAExpired` |

Mọi $M_i$ đều có đường đi tới một marking cuối (một trong 3 final places); không có marking cuối "kẹt" nào chứa token leftover.

## Bảng mapping BPMN → WF-net

| # | BPMN element | Transition | Kind |
|---|--------------|------------|------|
| T1 | `Task_DescribeIssue` | $t_1$ | task |
| T2 | `Task_ProvideInfo` | $t_2$ | task |
| T3 | `Task_ConfirmResolved` | $t_3$ | task |
| T4 | `Task_Feedback` | $t_4$ | task |
| T5 | `Task_WaitResponse` | $t_5$ | task |
| T6 | `Task_ClassifyIntent` | $t_6$ | task |
| T7 | `Task_AutoResolve` | $t_7$ | task |
| T8 | `Task_CheckSLA` | $t_8$ | task |
| T9 | `Task_T1VerifyIdentity` | $t_9$ | task |
| T10 | `Task_T1Review` | $t_10$ | task |
| T11 | `Gate_RepeatContact` | $t_11$ | XOR |
| T12 | `Task_CheckContextHistory` | $t_12$ | task |
| T13 | `Task_T1Resolve` | $t_13$ | task |
| T14 | `Task_T2Review` | $t_14$ | task |
| T15 | `Task_T2Resolve` | $t_15$ | task |
| T16 | `Task_FetchContext` | $t_16$ | task |
| T17 | `Task_LogSession` | $t_17$ | task |
| T18 | `Task_SendReminder` | $t_18$ | task |
| T19 | `Gate_BotSuccess` | $t_19$ | XOR |
| T20 | `Gate_SLAValid` | $t_20$ | XOR |
| T21 | `Gate_VerifyOK` | $t_21$ | XOR |
| T22 | `Gate_BotCanHandle` | $t_22$ | XOR |
| T23 | `Gate_T1Resolved` | $t_23$ | XOR |
| T24 | `Gate_Timeout` | $t_24$ | XOR |
| T25 | `Gate_CSAT` | $t_25$ | XOR |
| T26 | `Task_QualityFollowUp` | $t_26$ | task |
| T27 | `Join_Task_ConfirmResolved_1` | $t_27$ | XOR |
| T28 | `Join_Task_T1Review_2` | $t_28$ | XOR |
| T29 | `Join_Task_LogSession_3` | $t_29$ | XOR |

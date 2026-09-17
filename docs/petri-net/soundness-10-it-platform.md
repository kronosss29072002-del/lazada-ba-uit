# Kiểm chứng Soundness — Vận hành Nền tảng Công nghệ (IT Platform)

**File:** `processes-to-be/10-it-platform.bpmn`
**Phương pháp:** BPMN → WF-net (van der Aalst, 1998), phân tích reachability graph.

## Thống kê mô hình

| Chỉ số | Giá trị |
|--------|---------|
| Places (sequence flows) | 39 |
| Transitions (tasks + gateways) | 28 |
| Final places | 3 |
| Reachable markings (cap=4) | 39 |
| Max tokens trong 1 marking | 1 |
| Final places | Flow_IncidentNo_End, Flow_RecoverOK_End, Flow_Rollback_End |

## Kết quả soundness

| Thuộc tính | Kết quả | Bằng chứng |
|------------|---------|-----------|
| Option to Complete | ✅ PASS | 39/39 markings reachable có thể tới completion |
| Proper Completion | ✅ PASS | terminal markings không hợp lệ: 0 |
| No Dead Transitions | ✅ PASS | dead transitions: không có |

**Overall:** ✅ SOUND

> **Ghi chú:** Các vòng lặp có điều kiện dữ liệu (data-based loop) được phân tích trong không gian giới hạn với mỗi place giữ tối đa 1 token và mỗi lần lặp ≤ cap (cap=4). Điều này tương ứng với việc vòng lặp được chặn bởi bộ đếm (ví dụ `retryCount ≤ 3` cho sinh lại code, `resubmitCount ≤ 3` cho UAT lại) như đã khai báo trong mô hình TO-BE. Toàn bộ 7 vòng lặp dữ liệu (backlog, sửa thiết kế, AI sinh lại code, unit test fail, QA fail, UAT fail, demo lại) đều quay về các task đã qua và không tạo token leftover.

## Bảng minh họa vài marking

WF-net này là **1-bounded** (mọi trạng thái reachable có đúng 1 token — đồ thị state machine thuần XOR, không có AND-split). Dưới đây là các marking đại diện dọc theo nhánh chính (hành trình happy path + nhánh cuối):

| # | Marking (place mang token) | Ý nghĩa |
|---|----------------------------|---------|
| $M_0$ | `{Flow_S1_Collect}` | Khởi tạo: PO nhận yêu cầu tính năng / cải tiến |
| $M_1$ | `{Flow_Story_GatePriority}` | Sau `Task_UserStory`, chờ đánh giá ưu tiên (`Gate_PrioritizeOK`) |
| $M_2$ | `{Flow_AI_DesignReview}` | Sau `Task_AISuggestDesign`, chờ Dev xác nhận thiết kế |
| $M_3$ | `{Flow_DesignOK_AIGen}` | Sau `Gate_DesignReview` (duyệt), bắt đầu AI sinh code |
| $M_4$ | `{Flow_AICodeRev_GateFix}` | Sau `Task_AICodeReview`, chờ `Gate_AIFixOK` (nhánh fail quay lại sinh lại code) |
| $M_5$ | `{Flow_AITest_Unit}` | Sau `Task_AITestGen`, chờ chạy unit test tự động |
| $M_6$ | `{Flow_Integrate_SIT}` | Sau `Task_Integrate` (build OK), vào kiểm thử SIT |
| $M_7$ | `{Flow_UAT_GatePass}` | Sau `Task_UAT`, chờ `Gate_UATPass` |
| $M_8$ | `{Flow_Canary_GateHealth}` | Sau `Task_CanaryDeploy`, chờ health check (`Gate_HealthOK`) |
| $M_9$ | `{Flow_IncidentNo_End}` | **Marking cuối hợp lệ** → `EndEvent_Deployed` (không phát hiện sự cố) |

Mọi $M_i$ đều có đường đi tới một marking cuối (một trong 3 final places); không có marking cuối "kẹt" nào chứa token leftover. Các marking trong vòng lặp (`Flow_PrioNo_Backlog`, `Flow_DesignNo_AISuggest`, `Flow_AIFixNo_Regen`, `Flow_QAFail_AIGen`, `Flow_UATFail_AIGen`, `Flow_DemoNo_UAT`, `Flow_HealthFail_Rollback`, `Flow_RecoverFail_Rollback`) cũng đều reachable và dẫn tới completion khi bộ đếm đạt giới hạn.

## Bảng mapping BPMN → WF-net

| # | BPMN element | Transition | Kind |
|---|--------------|------------|------|
| T1 | `Task_CollectReq` | $t_1$ | task |
| T2 | `Task_UserStory` | $t_2$ | task |
| T3 | `Gate_PrioritizeOK` | $t_3$ | XOR |
| T4 | `Task_AISuggestDesign` | $t_4$ | task |
| T5 | `Task_DesignReview` | $t_5$ | task |
| T6 | `Gate_DesignReview` | $t_6$ | XOR |
| T7 | `Task_AICodeGen` | $t_7$ | task |
| T8 | `Task_AICodeReview` | $t_8$ | task |
| T9 | `Gate_AIFixOK` | $t_9$ | XOR |
| T10 | `Task_AITestGen` | $t_10$ | task |
| T11 | `Task_UnitTest` | $t_11$ | task |
| T12 | `Gate_UnitTestPass` | $t_12$ | XOR |
| T13 | `Task_Integrate` | $t_13$ | task |
| T14 | `Task_SIT` | $t_14$ | task |
| T15 | `Gate_QAPass` | $t_15$ | XOR |
| T16 | `Task_UAT` | $t_16$ | task |
| T17 | `Gate_UATPass` | $t_17$ | XOR |
| T18 | `Task_Demo` | $t_18$ | task |
| T19 | `Gate_DemoOK` | $t_19$ | XOR |
| T20 | `Task_CICDAuto` | $t_20$ | task |
| T21 | `Task_CanaryDeploy` | $t_21$ | task |
| T22 | `Gate_HealthOK` | $t_22$ | XOR |
| T23 | `Task_Autoscale` | $t_23$ | task |
| T24 | `Task_PredictIncident` | $t_24$ | task |
| T25 | `Gate_IncidentFound` | $t_25$ | XOR |
| T26 | `Task_SelfHeal` | $t_26$ | task |
| T27 | `Gate_RecoverOK` | $t_27$ | XOR |
| T28 | `Task_Rollback` | $t_28$ | task |
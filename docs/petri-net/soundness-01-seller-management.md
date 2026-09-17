# Kiểm chứng Soundness — Quản lý Nhà bán hàng

**File:** `processes/01-seller-management.bpmn`
**Phương pháp:** BPMN → WF-net (van der Aalst, 1998), phân tích reachability graph.

## Thống kê mô hình

| Chỉ số | Giá trị |
|--------|---------|
| Places (sequence flows) | 42 |
| Transitions (tasks + gateways) | 29 |
| Final places | 5 |
| Reachable markings (cap=4) | 42 |
| Max tokens trong 1 marking | 1 |
| Final places | Flow_Ban_End, Flow_Notify_End, Flow_Resubmit_End, Flow_Suspend_End, Flow_Warn_End |

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
| $M_0$ | `{Flow_Register_Submit}` | Khởi tạo: Seller bắt đầu đăng ký gian hàng |
| $M_1$ | `{Flow_Register_Phone}` | Sau `Task_Register`, chờ rẽ nhánh tại `Gate_PhoneVerif` |
| $M_2$ | `{Flow_Validate_Bank}` | Sau `Task_ValidateIdentity`, chờ kiểm tra tài khoản NH (`Gate_BankValid`) |
| $M_3$ | `{Flow_Risk_Doubt}` | Sau `Task_ScoreRisk`, chờ đánh giá rủi ro (`Gate_RiskDoubt`) |
| $M_4$ | `{Flow_Fix_Gate}` | Vòng lặp sửa hồ sơ: tại `Gate_ResubmitLimit` (lặp bị chặn bởi bộ đếm) |
| $M_5$ | `{Flow_Monitor_Gate}` | Nhánh giám sát hậu duyệt: tại `Gate_ViolationSeverity` |
| $M_6$ | `{Flow_Notify_End}` | **Marking cuối hợp lệ** → `End_Approved` (kích hoạt gian hàng) |
| $M_7$ | `{Flow_Warn_End}` | **Marking cuối hợp lệ** → `End_Warned` |

Mọi $M_i$ đều có đường đi tới một marking cuối (một trong 5 final places); không có marking cuối "kẹt" nào chứa token leftover.

## Bảng mapping BPMN → WF-net

| # | BPMN element | Transition | Kind |
|---|--------------|------------|------|
| T1 | `Task_Register` | $t_1$ | task |
| T2 | `Gate_PhoneVerif` | $t_2$ | XOR |
| T3 | `Task_VerifyPhone` | $t_3$ | task |
| T4 | `Task_UploadDocs` | $t_4$ | task |
| T5 | `Task_ValidateIdentity` | $t_5$ | task |
| T6 | `Gate_BankValid` | $t_6$ | XOR |
| T7 | `Task_FixBankInfo` | $t_7$ | task |
| T8 | `Task_OCRCheck` | $t_8$ | task |
| T9 | `Gate_DocValid` | $t_9$ | XOR |
| T10 | `Task_FixRejection` | $t_10$ | task |
| T11 | `Gate_ResubmitLimit` | $t_11$ | XOR |
| T12 | `Task_ScoreRisk` | $t_12$ | task |
| T13 | `Gate_RiskDoubt` | $t_13$ | XOR |
| T14 | `Gate_AutoApprove` | $t_14$ | XOR |
| T15 | `Task_ManualReview` | $t_15$ | task |
| T16 | `Gate_Approve` | $t_16$ | XOR |
| T17 | `Task_NotifyResult` | $t_17$ | task |
| T18 | `Task_MonitorViolations` | $t_18$ | task |
| T19 | `Gate_ViolationSeverity` | $t_19$ | XOR |
| T20 | `Task_Warn` | $t_20$ | task |
| T21 | `Task_Suspend` | $t_21$ | task |
| T22 | `Task_Ban` | $t_22$ | task |
| T23 | `Join_Task_UploadDocs_1` | $t_23$ | XOR |
| T24 | `Join_Task_ValidateIdentity_2` | $t_24$ | XOR |
| T25 | `Join_Task_OCRCheck_3` | $t_25$ | XOR |
| T26 | `Join_Task_FixRejection_4` | $t_26$ | XOR |
| T27 | `Join_Task_ManualReview_5` | $t_27$ | XOR |
| T28 | `Join_Task_NotifyResult_6` | $t_28$ | XOR |
| T29 | `Split_Task_NotifyResult_1` | $t_29$ | XOR |

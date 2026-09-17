# Kiểm chứng Soundness — Nhân sự & Đào tạo (HR & Training)

**File:** `processes/07-hr-training.bpmn`
**Phương pháp:** BPMN → WF-net (van der Aalst, 1998), phân tích reachability graph.

## Thống kê mô hình

| Chỉ số | Giá trị |
|--------|---------|
| Places (sequence flows) | 40 |
| Transitions (tasks + gateways) | 36 |
| Final places | 2 |
| Reachable markings (cap=4) | 40 |
| Max tokens trong 1 marking | 1 |
| Final places | Flow_Eval_End, Flow_Log_EndViolation |

## Kết quả soundness

| Thuộc tính | Kết quả | Bằng chứng |
|------------|---------|-----------|
| Option to Complete | ✅ PASS | 40/40 markings reachable có thể tới completion |
| Proper Completion | ✅ PASS | terminal markings không hợp lệ: 0 |
| No Dead Transitions | ✅ PASS | dead transitions: không có |

**Overall:** ✅ SOUND

> **Ghi chú:** Các vòng lặp có điều kiện dữ liệu (data-based loop) được phân tích trong không gian giới hạn với mỗi place giữ tối đa 1 token và mỗi lần lặp ≤ cap (cap=4). Điều này tương ứng với việc vòng lặp được chặn bởi bộ đếm (ví dụ `planReviseCount ≤ 3`, `examRetakeCount ≤ 3`, `contentReviseCount ≤ 3`) như đã khai báo trong mô hình TO-BE.

## Bảng minh họa vài marking

WF-net này là **1-bounded** (mọi trạng thái reachable có đúng 1 token). Dưới đây là các marking đại diện dọc theo các nhánh chính:

| # | Marking (place mang token) | Ý nghĩa |
|---|----------------------------|---------|
| $M_0$ | `{Flow_Start_SkillAnalysis}` | Khởi tạo: quý mới bắt đầu, nhu cầu đào tạo phát sinh |
| $M_1$ | `{Flow_PlanYes_Finance}` | Tại `Gate_PlanApproved`, kế hoạch đào tạo được duyệt → chuyển Finance |
| $M_2$ | `{Flow_BudgetYes_Check}` | Sau `Task_FinanceReview`, ngân sách được duyệt → kiểm tra chứng chỉ |
| $M_3$ | `{Flow_CertNo_Build}` | Tại `Gate_CertValid`, chứng chỉ hết hạn → xây dựng nội dung khóa học mới |
| $M_4$ | `{Flow_ContentYes_Publish}` | Sau `Gate_ContentApproved`, nội dung đạt chuẩn → publish lên Lazada University |
| $M_5$ | `{Flow_ComplianceYes_Enroll}` | Tại `Gate_ComplianceOK`, tuân thủ chính sách → chuyển đăng ký tham gia |
| $M_6$ | `{Flow_PrereqYes_Reg}` | Tại `Gate_PrereqMet`, đủ điều kiện tiên quyết → đăng ký khóa học |
| $M_7$ | `{Flow_ExamYes_Cert}` | Tại `Gate_ExamPass`, đạt điểm yêu cầu (≥70%) → cấp chứng chỉ |
| $M_8$ | `{Flow_Eval_End}` | **Marking cuối hợp lệ** → `EndEvent_Complete` (đào tạo hoàn tất, đánh giá hiệu quả) |
| $M_9$ | `{Flow_Log_EndViolation}` | **Marking cuối hợp lệ** → `EndEvent_Violation` (phát hiện vi phạm, xử lý kỷ luật) |

Mọi $M_i$ đều có đường đi tới một marking cuối (một trong 2 final places); không có marking cuối "kẹt" nào chứa token leftover.

## Bảng mapping BPMN → WF-net

| # | BPMN element | Transition | Kind |
|---|--------------|------------|------|
| T1 | `Task_SkillAnalysis` | $t_1$ | task |
| T2 | `Task_PlanTraining` | $t_2$ | task |
| T3 | `Task_ReviewPlan` | $t_3$ | task |
| T4 | `Task_FinanceReview` | $t_4$ | task |
| T5 | `Task_CheckCertValidity` | $t_5$ | task |
| T6 | `Task_BuildContent` | $t_6$ | task |
| T7 | `Task_AISuggestCourse` | $t_7$ | task |
| T8 | `Task_ReviewContent` | $t_8$ | task |
| T9 | `Task_PublishCourse` | $t_9$ | task |
| T10 | `Task_MonitorCompliance` | $t_{10}$ | task |
| T11 | `Task_ViolationDetected` | $t_{11}$ | task |
| T12 | `Task_EnforceAction` | $t_{12}$ | task |
| T13 | `Task_SuspendSeller` | $t_{13}$ | task |
| T14 | `Task_LogViolation` | $t_{14}$ | task |
| T15 | `Task_Register` | $t_{15}$ | task |
| T16 | `Task_Study` | $t_{16}$ | task |
| T17 | `Task_Exam` | $t_{17}$ | task |
| T18 | `Task_IssueCert` | $t_{18}$ | task |
| T19 | `Task_Gamification` | $t_{19}$ | task |
| T20 | `Task_UpdateCert` | $t_{20}$ | task |
| T21 | `Task_Evaluate` | $t_{21}$ | task |
| T22 | `Gate_PlanApproved` | $t_{22}$ | XOR |
| T23 | `Gate_BudgetOK` | $t_{23}$ | XOR |
| T24 | `Gate_CertValid` | $t_{24}$ | XOR |
| T25 | `Gate_ContentApproved` | $t_{25}$ | XOR |
| T26 | `Gate_ComplianceOK` | $t_{26}$ | XOR |
| T27 | `Gate_SeverityHigh` | $t_{27}$ | XOR |
| T28 | `Gate_EnrollmentOK` | $t_{28}$ | XOR |
| T29 | `Gate_PrereqMet` | $t_{29}$ | XOR |
| T30 | `Gate_ExamPass` | $t_{30}$ | XOR |
| T31 | `Join_Task_PlanTraining_1` | $t_{31}$ | XOR |
| T32 | `Join_Task_BuildContent_2` | $t_{32}$ | XOR |
| T33 | `Join_Task_PublishCourse_3` | $t_{33}$ | XOR |
| T34 | `Join_Task_Study_4` | $t_{34}$ | XOR |
| T35 | `Join_Task_LogViolation_5` | $t_{35}$ | XOR |
| T36 | `Join_Task_UpdateCert_6` | $t_{36}$ | XOR |
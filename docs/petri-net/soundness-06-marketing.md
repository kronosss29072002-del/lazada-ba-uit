# Kiểm chứng Soundness — Quy trình Marketing và Khuyến mãi

**File:** `processes/06-marketing.bpmn`
**Phương pháp:** BPMN → WF-net (van der Aalst, 1998), phân tích reachability graph.

## Thống kê mô hình

| Chỉ số | Giá trị |
|--------|---------|
| Places (sequence flows) | 46 |
| Transitions (tasks + gateways) | 35 |
| Final places | 4 |
| Reachable markings (cap=4) | 46 |
| Max tokens trong 1 marking | 1 |
| Final places | Flow_Confirm_No, Flow_Prepare_End, Flow_Purchase_End, Flow_Report_End |

## Kết quả soundness

| Thuộc tính | Kết quả | Bằng chứng |
|------------|---------|-----------|
| Option to Complete | ✅ PASS | 46/46 markings reachable có thể tới completion |
| Proper Completion | ✅ PASS | terminal markings không hợp lệ: 0 |
| No Dead Transitions | ✅ PASS | dead transitions: không có |

**Overall:** ✅ SOUND

> **Ghi chú:** Các vòng lặp có điều kiện dữ liệu (data-based loop) được phân tích trong không gian giới hạn với mỗi place giữ tối đa 1 token và mỗi lần lặp ≤ cap (cap=4). Điều này tương ứng với việc vòng lặp được chặn bởi bộ đếm (ví dụ `resubmitCount ≤ 3`) như đã khai báo trong mô hình TO-BE.

## Bảng minh họa vài marking

WF-net này là **1-bounded** (mọi trạng thái reachable có đúng 1 token). Dưới đây là các marking đại diện dọc theo các nhánh chính:

| # | Marking (place mang token) | Ý nghĩa |
|---|----------------------------|---------|
| $M_0$ | `{Flow_Idea_Research}` | Khởi tạo: ý tưởng chiến dịch được đề xuất |
| $M_1$ | `{Flow_Research_Audience}` | Tại `Gate_AudienceFit` (phân khúc lại?) |
| $M_2$ | `{Flow_Compliance_Gate}` | Tại `Gate_Compliance` (đạt chuẩn Nghị định 81?) |
| $M_3$ | `{Flow_Budget_Gate}` | Tại `Gate_BudgetTier` (vượt hạn mức → DirectorApprove) |
| $M_4$ | `{Flow_Config_Gate}` | Tại `Gate_PromoStack` (trùng mã voucher?) |
| $M_5$ | `{Flow_Test_Gate}` | Tại `Gate_VoucherTest` trong vòng lặp kiểm thử |
| $M_6$ | `{Flow_QA_Gate}` | Tại `Gate_QAPass` (đạt kiểm toán QA?) |
| $M_7$ | `{Flow_Report_Retry}` | Vòng lặp thu thập số liệu: tại `Gate_ReportReady` (lặp bị chặn bởi bộ đếm) |
| $M_8$ | `{Flow_Purchase_End}` | **Marking cuối hợp lệ** → `End_CampaignDone` |

Mọi $M_i$ đều có đường đi tới một marking cuối (một trong 4 final places); không có marking cuối "kẹt" nào chứa token leftover.

## Bảng mapping BPMN → WF-net

| # | BPMN element | Transition | Kind |
|---|--------------|------------|------|
| T1 | `Task_Research` | $t_1$ | task |
| T2 | `Gate_AudienceFit` | $t_2$ | XOR |
| T3 | `Task_ReSegment` | $t_3$ | task |
| T4 | `Task_DesignConcept` | $t_4$ | task |
| T5 | `Task_MonitorLive` | $t_5$ | task |
| T6 | `Task_PostReport` | $t_6$ | task |
| T7 | `Task_ComplianceCheck` | $t_7$ | task |
| T8 | `Task_BudgetReview` | $t_8$ | task |
| T9 | `Task_DirectorApprove` | $t_9$ | task |
| T10 | `Task_AutoInviteSellers` | $t_10$ | task |
| T11 | `Task_ConfigCampaign` | $t_11$ | task |
| T12 | `Gate_PromoStack` | $t_12$ | XOR |
| T13 | `Task_ResolveConflict` | $t_13$ | task |
| T14 | `Task_AutoTestVoucher` | $t_14$ | task |
| T15 | `Task_QACampaign` | $t_15$ | task |
| T16 | `Task_LaunchCampaign` | $t_16$ | task |
| T17 | `Task_AutoReport` | $t_17$ | task |
| T18 | `Task_ExtendData` | $t_18$ | task |
| T19 | `Gate_ReportReady` | $t_19$ | XOR |
| T20 | `Task_SellerConfirm` | $t_20$ | task |
| T21 | `Task_SellerRegister` | $t_21$ | task |
| T22 | `Task_SellerPrepare` | $t_22$ | task |
| T23 | `Task_BuyerBrowse` | $t_23$ | task |
| T24 | `Task_BuyerPurchase` | $t_24$ | task |
| T25 | `Gate_Compliance` | $t_25$ | XOR |
| T26 | `Gate_BudgetTier` | $t_26$ | XOR |
| T27 | `Gate_VoucherTest` | $t_27$ | XOR |
| T28 | `Gate_QAPass` | $t_28$ | XOR |
| T29 | `Gate_SellerConfirm` | $t_29$ | XOR |
| T30 | `Join_Task_DesignConcept_1` | $t_30$ | XOR |
| T31 | `Join_Task_AutoInviteSellers_2` | $t_31$ | XOR |
| T32 | `Join_Task_ConfigCampaign_3` | $t_32$ | XOR |
| T33 | `Join_Task_AutoTestVoucher_4` | $t_33$ | XOR |
| T34 | `Split_Task_AutoInviteSellers_1` | $t_34$ | XOR |
| T35 | `Split_Task_LaunchCampaign_2` | $t_35$ | XOR |

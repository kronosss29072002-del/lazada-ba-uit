# So sánh AS-IS vs TO-BE: Quy trình Marketing & Khuyến mãi

> **Quy trình:** 06 - Marketing & Khuyến mãi (Marketing & Promotions)
> **Nguồn AS-IS:** `processes/06-marketing.bpmn`
> **Nguồn TO-BE:** `processes-to-be/06-marketing.bpmn`
> **Ngày phân tích:** 2026-09-03
>
> **Ghi chú số liệu:** Các con số không nằm trong tài liệu gốc đều được **dán nhãn "ước tính"**. Bảng hoạt động và số liệu cấu trúc dựa trên **file BPMN thực tế**.

---

## 1. Tóm tắt thay đổi chính (TO-BE)

| # | Thay đổi TO-BE | Mục tiêu | Kết quả mong đợi |
|---|----------------|----------|------------------|
| 1 | **AI Budget Allocation** — phân bổ ngân sách tự động bằng ML, thay thẩm định thủ công | Rút ngắn time-to-market, tối ưu ROAS | ROAS +25%, time-to-market từ 3-4 tuần xuống ~1 tuần |
| 2 | **Real-time ROAS Dashboard** — giám sát hiệu năng realtime thay batch report cuối kỳ | Phát hiện campaign underperform sớm | Time-to-action giảm từ 3 ngày xuống realtime |
| 3 | **ML Insight Engine** — ML phân tích xu hướng & gợi ý tối ưu campaign | Thay tổng hợp báo cáo thủ công cuối kỳ | Actionable insight tự động, không cần analyst |
| 4 | **Template-based Campaign Config** — cấu hình campaign từ template chuẩn | Giảm cấu hình thủ công, giảm sai sót | Config time -70%, error rate -80% |
| 5 | **Auto-QA Checklist** — kiểm toán tự động trước giờ G thay kiểm tra thủ công | Giảm 50% thời gian kiểm toán | Pre-launch QA trong 30 phút thay 4 giờ |
| 6 | **Personalized Seller Invitation** — AI gửi lời mời seller personalized | Tăng tỷ lệ seller tham gia từ 60% lên 80% | Seller participation **+20pp** |
| 7 | **Auto-report + ML Insight sau chiến dịch** — báo cáo tự động + gợi ý cải tiến | Loại bỏ tổng hợp báo cáo sơ bộ thủ công | Post-campaign analysis trong 1 giờ thay 2 ngày |

---

## 2. Bảng so sánh hoạt động (Activity Comparison Table)

**Phân loại:** KEPT (giữ) | AUTOMATED (tự động hóa) | REMOVED (loại bỏ - NVA) | NEW (thêm mới)

| # | Hoạt động AS-IS | Hoạt động TO-BE (thay thế) | Phân loại | Giải thích thay đổi |
|---|-----------------|----------------------------|-----------|---------------------|
| 1 | Ý tưởng chiến dịch được đề xuất (start) | Ý tưởng chiến dịch (start) | **KEPT** | Giữ nguyên |
| 2 | Nghiên cứu thị trường & lập bản đề xuất (Task_NghienCuu) | Nghiên cứu thị trường + brief (Task_NghienCuu) | **KEPT** | Giữ nguyên |
| 3 | Thẩm định ngân sách & tỷ suất ROI (Task_ThamDinh) | AI phân bổ ngân sách (Task_AIBudget) | **AUTOMATED** | ML tính optimal budget allocation |
| 4 | Giám đốc Khối phê duyệt ngân sách lớn (Task_PheDuyet) | Giám đốc phê duyệt (ngân sách lớn) (Task_PheDuyet) | **KEPT** | Vẫn cần human approve cho budget lớn |
| 5 | Kiểm tra tính tuân thủ pháp lý khuyến mãi (Task_TuanThu) | *(gộp vào Auto-QA Checklist)* | **REMOVED (NVA)** | Tuân thủ pháp lý tích hợp vào Auto-QA |
| 6 | Thiết kế concept & lập kế hoạch chi tiết (Task_ThietKe) | Thiết kế concept + kế hoạch (Task_ThietKe) | **KEPT** | Giữ nguyên |
| 7 | Hệ thống gửi lời mời tham gia đến Sellers (Task_GuiLoiMoi) | Cá nhân hóa lời mời seller (Task_PersonalInvite) | **AUTOMATED** | AI personalized invitation |
| 8 | Cấu hình chiến dịch trên hệ thống (Task_CauHinh) | Config campaign tự động từ template (Task_AutoConfig) | **AUTOMATED** | Template thay config thủ công |
| 9 | Kiểm tra & giả lập áp mã voucher (Task_VoucherTest) | *(gộp vào Auto-QA Checklist)* | **REMOVED (NVA)** | Auto-QA tự test voucher logic |
| 10 | Kiểm toán QA toàn diện trước giờ G (Task_KiemToan) | Auto-QA checklist (Task_AutoQA) | **AUTOMATED** | AI QA checklist 30 phút thay 4 giờ |
| 11 | Kích hoạt Chiến dịch 12.12 (Task_KichHoat) | Kích hoạt Chiến dịch 12.12 (Task_KichHoat) | **KEPT** | Giữ nguyên |
| 12 | Theo dõi hiệu năng hệ thống & doanh số realtime (Task_TheoDoi) | Giám sát ROAS dashboard real-time (Task_ROASDashboard) | **AUTOMATED** | Dashboard realtime thay manual tracking |
| 13 | Tự động phân tách & giải quyết xung đột mã (Task_XungDot) | *(gộp vào Auto-QA — auto-detect conflict trước launch)* | **REMOVED (NVA)** | Auto-QA detect conflict trước khi launch |
| 14 | Hệ thống tự động xuất báo cáo sơ bộ (Task_BaoCaoSoBo) | Auto-report + ML insight sau chiến dịch (Task_AutoReportML) | **AUTOMATED** | ML insight thay batch report |
| 15 | Thu thập bổ sung số liệu đối soát (Task_ThuThapSoLieu) | *(gộp vào Auto-report — tự thu thập)* | **REMOVED (NVA)** | Auto-report tự aggregate data |
| 16 | Lập báo cáo tổng kết & đánh giá ROI (Task_DanhGiaROI) | *(gộp vào #14 — ML tự tính ROI)* | **REMOVED (NVA)** | ML tự tính + gợi ý cải tiến |
| 17 | Seller xem xét thư mời chiến dịch (Task_SellerXem) | Seller đăng ký tham gia (Task_SellerDangKy) | **KEPT** | Giữ nguyên |
| 18 | Seller xác nhận tham gia trên Seller Centre (Task_SellerXacNhan) | *(gộp vào #17 — 1-step registration)* | **KEPT (gộp)** | Gộp xem + xác nhận thành 1 step |
| 19 | Seller chuẩn bị tồn kho & cài đặt giá sốc (Task_SellerChuanBi) | Seller chuẩn bị sản phẩm + voucher (Task_SellerChuanBi) | **KEPT** | Giữ nguyên |
| 20 | Buyer truy cập săn deal 12.12 (Task_BuyerTruyCap) | Buyer xem khuyến mãi (Task_BuyerXem) | **KEPT** | Giữ nguyên |
| 21 | Buyer thanh toán áp mã FreeShip & Voucher (Task_BuyerThanhToan) | Buyer mua hàng (Task_BuyerMuaHang) | **KEPT** | Giữ nguyên |
| 22 | *(không có)* | Sinh insight ML từ dữ liệu (Task_MLInsight) | **NEW** | ML phân tích xu hướng cross-campaign |
| 23 | *(không có)* | Đo lường mức độ hài lòng của seller (Task_SellerSentiment) | **NEW** | Theo dõi trải nghiệm seller |

### Tổng hợp phân loại

| Phân loại | Số lượng | Danh sách |
|-----------|----------|-----------|
| **KEPT** | 10 | #1, 2, 4, 6, 11, 17, 18 (gộp), 19, 20, 21 |
| **AUTOMATED** | 6 | #3 (AIBudget), #7 (PersonalInvite), #8 (AutoConfig), #10 (AutoQA), #12 (ROASDashboard), #14 (AutoReportML) |
| **NEW** | 2 | #22 (MLInsight), #23 (SellerSentiment) |
| **REMOVED (NVA)** | 5 | #5 (TuanThu), #9 (VoucherTest), #13 (XungDot), #15 (ThuThapSoLieu), #16 (DanhGiaROI) |

---

## 3. So sánh cấu trúc mô hình (Structure Comparison)

| Tiêu chí | AS-IS (file BPMN) | TO-BE (file BPMN) | Thay đổi |
|----------|-------------------|-------------------|----------|
| Số lanes | 5 (Marketing Team, Approval, Lazada System, Sellers, Buyers) | 6 (Marketing Team, AI Engine, Approval, Lazada System, Sellers, Buyers) | **+1** (thêm AI Engine lane) |
| Số activities (tasks) | 21 | 16 | **-5** (gộp/remove NVA) |
| Số named gateways (decision) | 8 | 4 | **-4** (giảm decision paths nhờ auto) |
| Số all gateways (incl join/split) | 15 | 8 | **-7** |
| Số start events | 1 | 1 | 0 |
| Số end events | 1 | 1 | 0 |
| Số sequence flows | 47 | 31 | **-16 (-34%)** |

**Phân bố task theo lane:**

| Lane | AS-IS | TO-BE | Thay đổi |
|------|-------|-------|----------|
| Marketing Team | 4 (Research, DesignConcept, MonitorLive, PostReport) | 3 (Research, DesignConcept, MonitorLive) | **-1** (PostReport loại bỏ) |
| AI Engine | 0 (không có) | 3 (AIBudgetAlloc, AIPersonalInvite, MLInsights) | **+3** (lane mới) |
| Approval | 3 (ComplianceCheck, BudgetReview, DirectorApprove) | 1 (DirectorApprove) | **-2** (AI thay thẩm định) |
| System/AI | 7 (AutoInviteSellers, ConfigCampaign, AutoTestVoucher, QACampaign, LaunchCampaign, AutoReport, ExtendData) | 5 (ConfigTemplate, AutoQA, Launch, ROASDashboard, AutoReport) | **-2** (gộp NVA) |
| Seller | 3 (SellerConfirm, SellerRegister, SellerPrepare) | 2 (SellerRegister, SellerPrepare) | **-1** (gộp) |
| Buyer | 2 (BuyerBrowse, BuyerPurchase) | 2 (BuyerBrowse, BuyerPurchase) | 0 |

---

## 4. Phân tích PSI (People - System - Information)

### Peoples/Service Impacts

| Nhân vật | AS-IS | TO-BE | Thay đổi |
|----------|-------|-------|----------|
| **Marketing Team** | Phân bổ ngân sách thủ công, kiểm tra tuân thủ, test voucher, theo dõi realtime thủ công, tổng hợp báo cáo | AI phân bổ ngân sách, Auto-QA, dashboard realtime, auto-report | **Giảm workload -50%** |
| **Legal/Compliance** | Kiểm tra tuân thủ pháp lý (Nghị định 81) thủ công | Auto-QA tích hợp kiểm tra tuân thủ | **Giảm 100% manual effort** |
| **Seller** | Nhận thư mời chung, phải xác nhận 2 bước | Nhận lời mời personalized, 1-step registration | **Giảm friction +30% participation** |
| **Buyer** | Truy cập deal, thanh toán | Giữ nguyên | 0 thay đổi |

### Process Impacts

| Tiêu chí | AS-IS | TO-BE | Cải thiện |
|----------|-------|-------|-----------|
| Time-to-market (cycle time campaign) | 3-4 tuần (21-28 ngày; cycle kỳ vọng 21,1 ngày) | ~1 tuần (7,0 ngày) | **-67%** |
| Approval cycle | 5-8 ngày (multi-layer) | 2 ngày | **-65%** |
| Pre-launch QA Time | 4 giờ | 30 phút | **-87.5%** |
| Config Time | 3 giờ/campaign | 45 phút/campaign | **-75%** |
| Seller Participation Rate | 60% | 80% | **+20pp** |
| Post-campaign Report Time | 7 ngày | 3 ngày | **-57%** |
| ROAS Improvement | baseline | +25% | **+25%** |
| Error Rate (voucher conflict) | 8% | 3,8% | **-4,2pp (-52,5%)** |

### System Impacts

| Hệ thống | Thay đổi |
|----------|----------|
| Budget Allocator | Mới — ML-based budget optimization |
| ROAS Dashboard | Mới — realtime monitoring thay batch tracking |
| ML Insight Engine | Mới — cross-campaign analytics + recommendation |
| Auto-Config | Mới — template-based campaign setup |
| Auto-QA | Mới — 1-click pre-launch checklist |
| Personalized Invite | Mới — AI generate personalized seller invitation |

---

## 5. Phân tích Rủi ro (Risk Assessment)

| # | Rủi ro | Mức | Xác suất | Giải pháp |
|---|--------|-----|----------|-----------|
| 1 | AI phân bổ ngân sách sai, gây lãng phí | Cao | Trung bình | human approve cho mọi phân bổ, AI gợi ý thay vì quyết định |
| 2 | Auto-QA bỏ sót vi phạm pháp lý | Cao | Thấp | legal review manual cho campaign > 5 tỷ VND |
| 3 | Template config không phù hợp campaign đặc biệt | Trung bình | Trung bình | cho phép custom config override template |
| 4 | ROAS dashboard dữ liệu sai do integration bug | Trung bình | Thấp | daily data reconciliation check |
| 5 | Seller personalized invite bị coi là spam | Thấp | Trung bình | frequency cap + opt-out available |

---

## 6. ROI / Cost-Benefit Analysis

| Hạng mục | Chi phí ước tính | Ghi chú |
|----------|-----------------|---------|
| **AS-IS: Chi phí vận hành/campaign** | **62,000,000 VND** | Labor + system/ops, chưa gồm ngân sách khuyến mãi/voucher |
| **TO-BE: Chi phí vận hành/campaign** | **30,000,000 VND** | Giảm 52% nhờ automation + parallel approval |
| **Tiết kiệm/campaign** | **32,000,000 VND (-52%)** | |
| **Tool/AI monthly cost** | **63,000,000/tháng** (AI 35M + QA 15M + Dashboard 8M + Invite 5M) | Chi phí hệ thống mới |
| **Volume: Mega Campaigns/năm** | **~4 campaigns** | 9.9, 11.11, 12.12, Flash Sale mega |
| **Tiết kiệm labor hàng năm** | 32M x 4 = **128,000,000 VND/năm** | Only direct campaign cost savings |
| **Tổng đầu tư ban đầu (setup)** | **~120,000,000 VND** | AI + Dashboard + Auto-QA + Invite system |
| **Chi phí tool hàng năm** | 63M x 12 = **756,000,000 VND/năm** | |
| **Net benefit năm 1** | 128M - 756M = **-628,000,000 VND** (tool cost offset savings) | Tuy nhiên ROAS +25% → revenue tăng ước tính ~50M/tháng = 600M/năm |
| **Net benefit với revenue uplift** | -628M + 600M = **-28,000,000 VND/năm** | Gần break-even; ROAS improvement là driver chính |
| **Payback period** | **>1 năm** (chỉ dựa vào revenue uplift từ ROAS +25%) | Cần 3-4 năm đạt ROI dương trên direct cost savings |

> **Ghi chú:** Chi phí tool 63M/tháng (~756M/năm) chiếm tỷ trọng lớn so với tiết kiệm 128M/năm. Giá trị ROI thực sự đến từ ROAS improvement (+25% → ~600M/năm revenue uplift) thay vì tiết kiệm chi phí vận hành trực tiếp.

---

## 7. Đề Xuất Cuối Cùng (TO-BE Design Recommendation)

| # | Đề xuất | Độ ưu tiên | Thời gian thực hiện | Chi phí dự kiến |
|---|---------|-----------|--------------------|----|
| 1 | Implement Auto-QA Checklist | **Cao** | 3 tuần | 25M VND |
| 2 | Deploy ROAS Real-time Dashboard | **Cao** | 4 tuần | 30M VND |
| 3 | Template-based Campaign Config | **Cao** | 2 tuần | 15M VND |
| 4 | AI Budget Allocation + ML Insight | Trung bình | 6 tuần | 50M VND |
| 5 | Personalized Seller Invitation | Trung bình | 3 tuần | 20M VND |
| 6 | Auto-report + ML Post-campaign | Thấp | 4 tuần | 25M VND |

**Timeline:** 4 tháng (16 tuần) cho toàn bộ TO-BE transformation

---

## 8. Tài liệu tham khảo

- [Lazada Seller Center](https://sellercenter.lazada.vn) — Campaign management, seller invitation flow
- [Lazada University](https://university.lazada.vn) — Seller education, campaign training
- AS-IS BPMN: `processes/06-marketing.bpmn`
- TO-BE BPMN: `processes-to-be/06-marketing.bpmn`
- [analysis/06-marketing.md](../06-marketing.md) — Phân tích chi tiết quy trình

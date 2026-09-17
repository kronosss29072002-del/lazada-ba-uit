# So sánh AS-IS vs TO-BE: Quy trình Vận hành Nền tảng Công nghệ (IT Operations)

> **Quy trình:** 10 - Vận hành Nền tảng Công nghệ (IT Operations)
> **Nguồn AS-IS:** `processes/10-it-platform.bpmn`
> **Nguồn TO-BE:** `processes-to-be/10-it-platform.bpmn`
> **Ngày phân tích:** 2026-09-03
>
> **Ghi chú số liệu:** Các con số không nằm trong tài liệu gốc đều được **dán nhãn "ước tính"**. Bảng hoạt động và số liệu cấu trúc dựa trên **file BPMN thực tế**.

---

## 1. Tóm tắt thay đổi chính (TO-BE)

| # | Thay đổi TO-BE | Mục tiêu | Kết quả mong đợi |
|---|----------------|----------|------------------|
| 1 | AI Copilot gợi ý thiết kế + ước lượng effort (thay Design thủ công) | Giảm thời gian thiết kế kỹ thuật | Giảm cycle time thiết kế -50% |
| 2 | AI Copilot sinh code theo User Story (thay Code thủ công) | Tăng năng suất Dev + giảm bug | Giảm bug fix cycle -60% |
| 3 | AI tự động Review Code + phát hiện lỗi (thay Code Review thủ công) | Phát hiện sớm lỗi tại source | Code reviewchờ 4-6h → 15 phút (AI) |
| 4 | AI tự sinh test case & data test (thay viết test thủ công) | Tăng coverage + giảm thời gian viết test | Code coverage 70% → 90%+ |
| 5 | Canary Deployment 10% → 100% (thay Blue-Green 3 bước) | Giảm deployment failure + rollback nhanh | Failure rate 15% → 3% |
| 6 | K8s HPA autoscale tự động (thay provisioning thủ công) | Tối ưu tài nguyên theo traffic | Infrastructure waste -80% |
| 7 | AIOps giám sát & dự đoán sự cố (thay monitor thủ công) | Phát hiện sớm + tự phục hồi | MTTR 2-4h → 30-60 phút |
| 8 | Self-healing pods + auto-rollback (thay Rollback thủ công) | Giảm thời gian phục hồi sự cố | Rollback tự động <5 phút |
| 9 | Loại bỏ lane Security riêng — tích hợp SAST/SCA vào CI pipeline | Shift-left security, giảm response time | Security response 7-14 ngày → 1-3 ngày |
| 10 | Giảm 2 deploy steps (Pre-Staging + Staging riêng) → Canary tích hợp | Đơn giản hóa pipeline | CI/CD 45 phút → 15 phút |

---

## 2. Bảng so sánh hoạt động (Activity Comparison Table)

**Phân loại:** KEPT (giữ) | AUTOMATED (tự động hóa) | REMOVED (loại bỏ - NVA) | NEW (thêm mới)

| # | Hoạt động AS-IS | Hoạt động TO-BE (thay thế) | Phân loại | Giải thích thay đổi |
|---|-----------------|----------------------------|-----------|---------------------|
| 1 | Yêu cầu tính năng mới (Start) | Nhận yêu cầu tính năng / cải tiến (Start) | **KEPT** | Giữ nguyên |
| 2 | Tạo User Story & acceptance criteria (Task_CreateStory) | Thu thập & phân tích yêu cầu nghiệp vụ (Task_CollectReq) | **KEPT** | Đổi tên, bổ sung phân tích nghiệp vụ |
| 3 | Ưu tiên backlog & sprint planning (Task_Prioritize) | Viết User Story + tiêu chí chấp nhận (Task_UserStory) | **KEPT** | Hợp nhất 2 bước thành 1 |
| 4 | Gateway: Yêu cầu được chấp nhận vào sprint? (Gate_PrioritizeOK) | Gateway: Đủ ưu tiên để phát triển? (Gate_PrioritizeOK) | **KEPT** | Giữ nguyên logic |
| 5 | Thiết kế kiến trúc & API cho tính năng (Task_Design) | AI gợi ý thiết kế & ước lượng effort (Task_AISuggestDesign) | **AUTOMATED** | Thay thiết kế thủ công bằng AI-assisted design |
| 6 | Gateway: Thiết kế được phê duyệt? (Gate_DesignReview) | Gateway: Thiết kế được duyệt? (Gate_DesignReview) | **KEPT** | Dev xác nhận thiết kế AI, giữ human-in-the-loop |
| 7 | Viết code theo User Story & unit test (Task_Code) | AI sinh code theo user story — Copilot (Task_AICodeGen) | **AUTOMATED** | Thay code thủ công bằng AI Copilot code generation |
| 8 | Chạy unit test & code review (Task_UnitTest) | AI tự động review code + phát hiện lỗi (Task_AICodeReview) | **AUTOMATED** | Kết hợp code review + unit test trong AI pipeline |
| 9 | Gateway: Unit test pass? (Gate_UnitTestPass) | Gateway: AI review pass? (Gate_AIFixOK) | **AUTOMATED** | AI tự review + quyết định pass/fail, loop tự sửa |
| 10 | *(không có)* | AI tự sinh test case & data test (Task_AITestGen) | **NEW** | AI tự động sinh test case + test data, tăng coverage |
| 11 | *(không có)* | Chạy unit test + coverage tự động (Task_UnitTest) | **NEW** | Unit test tự động với ngưỡng coverage ≥90% |
| 12 | *(không có)* | Tích hợp module & build tự động (Task_Integrate) | **NEW** | Build + integrate tự động trong pipeline |
| 13 | Thực hiện System Test & Integration Test (Task_ST) | Kiểm thử tích hợp hệ thống (SIT) tự động (Task_SIT) | **AUTOMATED** | Chuyển từ ST/IT thủ công sang automated SIT |
| 14 | Gateway: QA test pass? (Gate_QAPass) | Gateway: QA pass? (Gate_QAPass) | **KEPT** | Giữ human QA gate, nhưng scope giảm |
| 15 | Sửa lỗi QA phát hiện & regression test (Task_Bugfix) | *(loại bỏ — AI tự sửa lỗi loop)* | **REMOVED (NVA)** | AI code gen + review tự xử lý bug, không cần loop thủ công |
| 16 | Performance test & load test (Task_PerfTest) | *(loại bỏ — tích hợp vào pipeline tự động)* | **REMOVED (NVA)** | Perf test được tích hợp vào CI/CD pipeline |
| 17 | Gateway: Performance test pass? (Gate_PerfOK) | *(loại bỏ — tích hợp vào pipeline)* | **REMOVED (NVA)** | Perf gate tích hợp trong automated pipeline |
| 18 | Demo tính năng cho Stakeholder (Task_DemoFeature) | Demo tính năng cho PO & stakeholder (Task_Demo) | **KEPT** | Giữ nguyên |
| 19 | Gateway: Stakeholder chấp nhận tính năng? (Gate_DemoOK) | Gateway: Demo đạt yêu cầu? (Gate_DemoOK) | **KEPT** | Giữ nguyên |
| 20 | Triển khai lên môi trường Pre-Staging (Task_PreStagingDeploy) | *(loại bỏ — Canary thay thế)* | **REMOVED (NVA)** | Canary 10%→100% thay 3 bước deploy riêng lẻ |
| 21 | Triển khai lên môi trường Staging (Task_StagingDeploy) | *(loại bỏ — Canary thay thế)* | **REMOVED (NVA)** | Staging gộp vào Canary deployment |
| 22 | Triển khai lên Production — Blue-Green Deploy (Task_ProdDeploy) | Triển khai Canary 10% → 100% (Task_CanaryDeploy) | **AUTOMATED** | Thay Blue-Green thủ công bằng Canary tự động |
| 23 | Giám sát metrics sau deploy 30 phút (Task_Monitor) | Tự động mở rộng tài nguyên — K8s HPA (Task_Autoscale) | **AUTOMATED** | Kết hợp monitor + autoscale |
| 24 | Gateway: Metrics hệ thống ổn định? (Gate_HealthOK) | Gateway: Health check sau deploy ổn? (Gate_HealthOK) | **KEPT** | Giữ health check gate |
| 25 | *(không có)* | AI giám sát & dự đoán sự cố — AIOps (Task_PredictIncident) | **NEW** | AIOps predictive monitoring thay threshold cứng |
| 26 | *(không có)* | Gateway: Phát hiện bất thường? (Gate_IncidentFound) | **NEW** | Gateway quyết định cần self-heal hay không |
| 27 | *(không có)* | Tự phục hồi / khởi động lại pod tự động (Task_SelfHeal) | **NEW** | Self-healing pods, giảm MTTR |
| 28 | *(không có)* | Gateway: Phục hồi thành công? (Gate_RecoverOK) | **NEW** | Kiểm tra self-heal có thành công không |
| 29 | Rollback về version trước — tạo Incident (Task_Rollback) | Rollback về version ổn định (Task_Rollback) | **KEPT** | Giữ rollback, nhưng tự động hơn |
| 30 | Xử lý sự cố infrastructure & incident (Task_ResolveIncident) | *(loại bỏ — AIOps tự xử lý)* | **REMOVED (NVA)** | AIOps + self-heal thay incident handling thủ công |
| 31 | Quét lỗ hổng bảo mật — SAST/DAST (Task_SecurityScan) | *(loại bỏ — tích hợp vào AI pipeline)* | **REMOVED (NVA)** | Security scan shift-left vào CI/CD pipeline |
| 32 | Gateway: Không có lỗ hổng nghiêm trọng? (Gate_SecurityOK) | *(loại bỏ — tích hợp vào pipeline)* | **REMOVED (NVA)** | Security gate tích hợp trong pipeline, không riêng lane |
| 33 | Áp dụng bản vá bảo mật khẩn cấp (Task_PatchSecurity) | *(loại bỏ — shift-left)* | **REMOVED (NVA)** | Patch thủ công loại bỏ, phát hiện sớm + auto-fix |
| 34 | Triển khai bản vá & regression test (Task_ApplyPatch) | *(loại bỏ — shift-left)* | **REMOVED (NVA)** | Patch deployment tích hợp pipeline |
| 35 | Gateway: Bản vá được áp dụng thành công? (Gate_PatchApplied) | *(loại bỏ — shift-left)* | **REMOVED (NVA)** | Không cần gate patch riêng |
| 36 | Rollback — hoàn nguyên về version trước (EndEvent_Rollback) | *(loại bỏ — gộp vào 1 end event)* | **REMOVED (NVA)** | Rollback dẫn đến 1 end event chung |

### Tổng hợp phân loại

| Phân loại | Số lượng | Danh sách |
|-----------|----------|-----------|
| **KEPT** | 8 | #1, 2, 3, 4, 6, 14, 18, 19 |
| **AUTOMATED** | 7 | #5 (AI Design), #7 (AI CodeGen), #8 (AI Code Review), #9 (AI Review Gate), #13 (Auto SIT), #22 (Canary Deploy), #23 (AutoScale) |
| **NEW** | 6 | #10 (AI Test Gen), #11 (Auto Unit Test), #12 (Auto Integrate), #25 (AIOps), #26-28 (Self-Heal flow) |
| **REMOVED (NVA)** | 13 | #15 (Bugfix loop), #16 (PerfTest), #17 (PerfOK gate), #20 (PreStaging), #21 (Staging), #30 (Incident), #31 (Security Scan), #32 (SecurityOK), #33 (Patch), #34 (Apply Patch), #35 (PatchApplied gate), #36 (Rollback end) |

**Nhận xét:** Quy trình TO-BE tăng cường đáng kể khả năng tự động hóa: 7 hoạt động thủ công được chuyển sang AI/service, 6 hoạt động mới bổ sung (AI test gen, AIOps, self-heal). Đáng chú ý, **toàn bộ lane Security bị loại bỏ** — security scan được shift-left tích hợp vào CI/CD pipeline. Bug fix loop thủ công (NVA lớn nhất, 2-5 ngày/release) bị loại bỏ hoàn toàn nhờ AI code review + auto-fix. Tỷ lệ VA/BVA/NVA ước tính sau TO-BE: **~35% / ~55% / ~10%** (so với ~22% / ~56% / ~22% AS-IS).

---

## 3. So sánh cấu trúc mô hình (Structure Comparison)

| Tiêu chí | AS-IS (file BPMN) | TO-BE (file BPMN) | Thay đổi |
|----------|-------------------|-------------------|----------|
| Số lanes | 5 (Product Owner, Dev Team, QA / Tester, DevOps / CI-CD, Security) | 5 (Product Owner, AI DevX / Copilot, Dev Team, QA / Tester, DevOps / AIOps) | 0 (giữ 5 lanes, thay Security → AI DevX, đổi tên DevOps → AIOps) |
| Số activities (tasks) | 18 (userTask: 13, serviceTask: 5) | 18 (userTask: 6, serviceTask: 12) | 0 giữ tổng, đảo tỷ lệ — serviceTask tăng mạnh nhờ AI自动化 |
| Số gateways (named decision) | 16 | 16 | 0 (giữ nguyên; 3 gateway security bị bỏ + 3 gateway self-heal bổ sung) |
| Số start events | 1 | 1 | 0 |
| Số end events | 2 (Triển khai thành công, Rollback) | 1 (Triển khai hoàn tất) | **-1** (gộp rollback + deploy thành công vào 1 end event) |
| Số sequence flows | 45 | 45 | 0 (giữ nguyên; nội dung luồng thay đổi nhưng số lượng tương đương) |
| userTask : serviceTask ratio | 13:5 (72%:28%) | 6:12 (33%:67%) | **Đảo ngược** — phần lớn trở thành automated service tasks |
| Độ phức tạp | Cao (5 lanes, security loop, bugfix loop, 3-step deploy) | Trung bình-Cao (5 lanes, AI loops, self-heal flow, nhưng bớt bugfix + security loops) | **Giảm tương đối** — bớt loops NVA, nhưng thêm AI + self-heal loops |

**Phân bố task theo lane:**

| Lane | AS-IS | TO-BE | Thay đổi |
|------|-------|-------|----------|
| Product Owner | 3 (CreateStory, Prioritize, DemoFeature) | 3 (CollectReq, UserStory, Demo) | 0 (giữ nguyên, đổi tên) |
| AI DevX / Copilot *(lane mới)* | — | 4 (AISuggestDesign, AICodeGen, AICodeReview, AITestGen) | **+4** (lane hoàn toàn mới) |
| Dev Team | 3 (Design, Code, UnitTest) | 3 (DesignReview, UnitTest, Integrate) | 0 (số lượng giữ, nội dung thay đổi) |
| QA / Tester | 3 (ST, Bugfix, PerfTest) | 2 (SIT, UAT) | **-1** (bỏ Bugfix, PerfTest) |
| DevOps / AIOps | 6 (PreStaging, Staging, ProdDeploy, Monitor, Rollback, ResolveIncident) | 10 (CICDAuto, CanaryDeploy, Autoscale, PredictIncident, SelfHeal, Rollback + 4 gateways) | **+4** (thêm autoscale, AIOps, self-heal; bỏ PreStaging, Staging, ResolveIncident) |
| Security *(lane xóa)* | 3 (SecurityScan, PatchSecurity, ApplyPatch) | — | **-3** (toàn bộ lane bị loại, tích hợp shift-left vào pipeline) |

---

## 4. Bảng so sánh Metrics (Định lượng)

> Các giá trị TO-BE là **ước tính** dựa trên giả định AI Copilot tăng năng suất Dev 40-60%, automated pipeline giảm deploy failure 80%.

| Metric | AS-IS (ước tính) | TO-BE (expected) | Cải thiện |
|--------|------------------|------------------|-----------|
| **Release cycle (story → production)** | **4-6 tuần** | **1-2 tuần** | **-67-75%** |
| **CI/CD pipeline duration** | **45 phút** | **15 phút** | **-67%** |
| **Deployment failure rate** | **15%** | **3%** | **-80%** |
| **MTTR (Mean Time to Recovery)** | **2-4 giờ** | **30-60 phút** | **-75-80%** |
| **Rollback time** | **30-60 phút** (thủ công) | **<5 phút** (tự động) | **-90%+** |
| **Bug fix cycle time** | **2-5 ngày** | **1-2 ngày** | **-50-60%** |
| **Security vulnerability response** | **7-14 ngày** | **1-3 ngày** | **-78-86%** |
| **Code review wait time** | **4-6 giờ/PR** | **15 phút (AI review)** | **-94%** |
| **Code coverage** | **~70%** | **≥90%** | **+20%+** |
| **Monthly feature releases** | **50** | **80-100** | **+60-100%** |
| **Infrastructure cost (tháng)** | **500M VND** | **350M VND** | **-30%** |
| **Tổng chi phí IT Operations (tháng)** | **3.9 tỷ VND** (labor 3.4 tỷ + infra 500M) | **0.9 tỷ VND** | **-77%** |
| **userTask : serviceTask ratio** | **67% : 33%** | **29% : 71%** | **Đảo ngược** — automation-centric |
| **Named gateways** | **16** | **16** | **0** (giữ nguyên; 3 gateway security bị bỏ + 3 gateway self-heal bổ sung) |

### 4.1. Phân bổ chi phí Infrastructure chi tiết (ước tính, per tháng)

| Thành phần | AS-IS (triệu VND/tháng) | TO-BE (triệu VND/tháng) | Thay đổi |
|------------|------------------------|------------------------|----------|
| Cloud compute (server, VM) | 200 | 120 | **-80** (K8s HPA autoscale, FinOps) |
| CI/CD tool licenses (Jenkins, GitLab) | 50 | 40 | -10 (giảm self-hosted, dùng cloud-native) |
| Monitoring & APM (Datadog, Grafana) | 60 | 50 | -10 (AIOps consolidate) |
| Security tools (SAST, DAST, SCA) | 40 | 30 | -10 (shift-left, dùng free-tier SAST) |
| AI/ML inference (Copilot, AIOps) | 0 | 80 | **+80** (mới — AI code gen, AI monitoring) |
| Container orchestration (K8s) | 50 | 30 | -20 (managed K8s) |
| **TỔNG** | **500** | **350** | **-150 (-30%)** |

### 4.2. Cycle Time chi tiết (ước tính, per feature release)

| Giai đoạn | AS-IS (phút) | TO-BE (phút) | Ghi chú |
|-----------|-------------|-------------|---------|
| Phân tích yêu cầu + User Story | 240 | 180 | AI hỗ trợ ước lượng effort |
| Thiết kế kỹ thuật | 480 | 150 | AI gợi ý design giảm -68% |
| Code Review (chờ reviewer) | 180 | 15 | AI review giảm -94% |
| Viết code | 960 | 480 | AI Copilot tăng năng suất -50% |
| Viết Unit Test + coverage | 180 | 30 | AI sinh test case tự động |
| CI/CD Pipeline (Build + Test) | 45 | 15 | Parallel testing + caching |
| Kiểm thử ST/IT | 360 | 120 | Automated SIT |
| Sửa lỗi (Bug Fix Loop) | 720 | 120 | AI review giảm 70% bugs |
| Security Scan | 60 | 0 | Shift-left, tích hợp pipeline |
| Performance Test | 180 | 0 | Tích hợp CI/CD |
| Demo + Phê duyệt | 60 | 60 | Giữ nguyên |
| Triển khai (Canary) | 30 | 10 | Canary 10%→100% tự động |
| Rollback (nếu fail) | 45 | 3 | Self-heal + auto-rollback |
| Giám sát Production | 60 | 30 | AIOps predictive + autoscale |
| **Tổng Cycle Time** | **3,550 phút ≈ 59 giờ (~6,9 ngày)** | **1,213 phút ≈ 20 giờ** | **-66%** |

> **Ghi chú:** ước tính xác suất-weighted trong analysis doc cho 3,323 phút ≈ 55,4 giờ ≈ 6,9 ngày làm việc — cùng cỡ với 59 giờ ở đây (sai khác ~7% do bình quân trung vị từng bước); cả hai quy về ~6,5-6,9 ngày và khớp `cycle_time.as_is = 6,9 ngày` trong data.json.

---

## 5. ROI — Ước tính đầu tư và thời gian hoàn vốn

> Toàn bộ số liệu mục này là **ước tính** cho mục đích trình bày BA (business case).

### 5.1. Đầu tư ban đầu (one-time, ước tính)

| Hạng mục | Chi phí (tỷ VND) | Ghi chú |
|----------|------------------|---------|
| AI Copilot license + integration (GitHub Copilot, CodeWhisperer) | 2.0 | Enterprise license + IDE integration cho 60 devs |
| AI Code Review engine + custom rules | 0.8 | Custom model fine-tune + integration vào pipeline |
| CI/CD Pipeline modernization (Canary, parallel testing) | 1.5 | Pipeline rewrite, infrastructure-as-code |
| Kubernetes HPA + autoscaling setup | 1.0 | K8s cluster upgrade, HPA configuration, FinOps tooling |
| AIOps platform (Datadog AIOps / Dynatrace) | 1.2 | License + custom anomaly detection models |
| Self-healing + auto-rollback engine | 0.8 | Kubernetes operator, health check automation |
| Security shift-left (SAST/SCA trong CI) | 0.6 | Tool integration, custom rule configuration |
| Training, rollout, migration | 0.5 | Team training trên AI tools, phased rollout |
| **TỔNG ĐẦU TƯ BAN ĐẦU** | **8.4 tỷ VND** (~350K USD, ước tính) | |

**Chi phí vận hành hằng năm:** ~2.5 tỷ VND/năm (AI licenses, cloud autoscale, AIOps).

### 5.2. Lợi ích hàng năm (ước tính)

**Giả định:** Đội IT 80 engineers, 50 releases/tháng, infra 500M VND/tháng.

| Nguồn lợi ích | Công thức | Giá trị (tỷ VND/năm) |
|---------------|-----------|----------------------|
| Giảm infrastructure waste (autoscale) | (500-350)M x 12 tháng | 1.8 |
| Giảm bug fix labor (2-5 → 1-2 ngày/release) | 60% reduction x 50 releases x avg 3 ngày | 4.5 |
| Tăng releases/tháng (50 → 90) | 40 additional releases x value | 6.0 |
| Giảm deployment failure cost (15% → 3%) | 12% reduction x 50 deploys x cost | 1.2 |
| Giảm MTTR downtime cost | (3h - 0.75h) x incidents/month x cost | 2.0 |
| Giảm security remediation cost | (14 - 2) days x vulnerability count x cost | 0.8 |
| **Tổng lợi ích tiềm năng** | | **16.3** |
| Lợi ích năm đầu thực thu (50%) | 16.3 x 50% | **8.15** |
| Trừ chi phí vận hành hằng năm | | -2.5 |
| **Lợi ích ròng năm đầu** | | **~5.65 tỷ VND/năm** |

### 5.3. Thời gian hoàn vốn (Payback)

| Kịch bản | Giả định | Payback |
|----------|----------|---------|
| **Cơ sở (Base)** | 80 engineers, 50 releases/tháng, đạt 50% tiềm năng | 8.4 / 5.65 ≈ **~18 tháng** |
| **Thận trọng (Conservative)** | Giảm 25% lợi ích, chi phí tăng 20% | 8.4 / (3.2) ≈ **~32 tháng** |

- **Kết luận ROI:** Kịch bản cơ sở ~18 tháng, đạt chuẩn phê duyệt đầu tư cho IT infrastructure. Lợi ích ròng 5 năm (cơ sở): (5.65 x 5) - 8.4 - (2.5 x 5) ≈ **~7.35 tỷ VND**.

---

## 6. Rủi ro TO-BE và giảm thiểu

| # | Rủi ro | Mức độ | Giải pháp giảm thiểu (Mitigation) |
|---|--------|--------|------------------------------------|
| 1 | **AI Copilot sinh code có bug logic —đưa vào các lỗi tiềm ẩn (subtle) defects** | Cao | (a) AI review phải pass trước khi human review; (b) Coverage gate ≥90%; (c) Canary deploy 10% trước khi full rollout; (d) Shadow mode 2 tháng đầu |
| 2 | **AIOps false positive — alert fatigue, bỏ qua sự cố thật** | Cao | (a) Baseline learning 1 tháng; (b) Alert grouping + severity tuning; (c) Manual on-call vẫn available; (d) Review alert accuracy hàng tuần |
| 3 | **Self-healing mask underlying issue — fix symptoms thay vì root cause** | Trung bình | (a) Log mọi self-heal event + root cause analysis; (b) Threshold: self-heal >3 lần/tháng → escalate; (c) Root cause must-fix within 48h |
| 4 | **AI Code Review bỏ sót critical security vulnerability** | Cao | (a) SAST/SCA vẫn chạy độc lập trong pipeline; (b) Pen test quarterly; (c) Security gate riêng cho high-risk changes; (d) Multi-layer defense (AI + tool + human) |
| 5 | **Team resistance — Dev không tin AI-generated code** | Trung bình | (a) Training workshop 2 tuần; (b) Pilot với non-critical features; (c) Show metrics: bug rate giảm sau AI adoption; (d) Chọn Copilot để Dev kiểm soát |
| 6 | **Canary deployment gây split-brain state (10% traffic trên version mới)** | Thấp-Trung bình | (a) Feature flags để isolate; (b) Database migration backward-compatible; (c) Health check gate nghiêm ngặt trước khi scale 100%; (d) Auto-rollback timeout |
| 7 | **Loại bỏ Security lane quá sớm — shift-left không đủ coverage** | Trung bình | (a) Phase 1: Giữ Security team review cho critical changes; (b) Phase 2: Review quarterly security metrics; (c) Nếu vulnerability rate tăng → restore Security lane |

---

## 7. Kết luận

1. **TO-BE giữ 8/18 hoạt động gốc**, tự động hóa 7 hoạt động (design, code, code review, SIT, deploy, monitor, autoscale), thêm 6 hoạt động mới (AI test gen, auto unit test, auto integrate, AIOps, self-heal flow), và loại bỏ 13 hoạt động NVA — đặc biệt đáng chú ý là **toàn bộ lane Security bị loại bỏ** (shift-left vào CI/CD), bug fix loop thủ công (2-5 ngày/release), và 2 bước deploy riêng lẻ (Pre-Staging + Staging).
2. **Metrics:** Release cycle giảm 67-75% (4-6 tuần → 1-2 tuần), CI/CD pipeline giảm 67% (45→15 phút), deployment failure giảm 80% (15%→3%), MTTR giảm 75-80% (2-4h → 30-60 phút), security response giảm 78-86% (7-14 ngày → 1-3 ngày), monthly releases tăng 60-100% (50 → 80-100), tổng chi phí IT Ops giảm 77% (3.9 tỷ → 0.9 tỷ VND/tháng).
3. **ROI:** Đầu tư ban đầu ~8.4 tỷ VND (ước tính), payback ~18 tháng (cơ sở) / ~32 tháng (thận trọng). Lợi ích ròng 5 năm ~7.35 tỷ VND. Chi phí infra giảm 30% (500M → 350M/tháng).
4. **Rủi ro lớn nhất:** AI-generated codeđưa vào các lỗi tiềm ẩn (subtle) bugs (mitigate bằng multi-layer: AI review + SAST/SCA + human review + canary deploy) và AIOps false positive (mitigate bằng baseline learning + manual on-call backup).
5. **Hành động tiếp theo:** (a) Phê duyệt Phase 1 — AI Copilot + automated CI/CD (~3.5 tỷ VND); (b) Pilot AI Copilot với 1 team trước khi rollout toàn bộ 60 devs; (c) Thiết lập baseline metrics (bug rate, deploy failure, MTTR) trước khi áp dụng AIOps; (d) Giữ Security team review cho critical changes trong 6 tháng đầu sau khi shift-left.

---

## 8. Tham chiếu

- AS-IS BPMN: `processes/10-it-platform.bpmn`
- TO-BE BPMN: `processes-to-be/10-it-platform.bpmn`
- Phân tích chi tiết: `docs/analysis/10-it-platform.md`

# Bộ Phỏng vấn riêng — Quy trình 10: IT Platform Operations (Vận hành IT Platform)

## A. Mục đích phỏng vấn & Đối tượng

### Mục đích
Thu thập dữ liệu về **vòng đời phát triển & vận hành tính năng trên nền tảng IT Lazada VN** — từ lập kế hoạch sprint, code review, CI/CD pipeline, Canary/Blue-Green deploy lên Kubernetes, giám sát hiệu năng (CPU/RAM/Error Rate), phản hồi sự cố (Incident Response & MTTR) và quản lý lỗ hổng bảo mật (Security Patching 7–14 ngày). Mục tiêu là hiểu rõ bottleneck trong quy trình release ~50 lần/tháng, tỷ lệ deploy thất bại ~15%, thời gian rollback 30–60 phút và MTTR 2–4h hiện tại.

### Thông tin người phỏng vấn
- **Họ tên (giả định):** Anh Trịnh Minh Khang
- **Vai trò:** Senior Engineering Manager / Head of DevOps & SRE — phụ trách nền tảng CI/CD, K8s cluster, observability stack (Prometheus/Grafana/ELK) và incident management cho các microservices cốt lõi (Order, Payment, Catalog) trên Lazada Việt Nam
- **Thâm niên:** 8 năm trong lĩnh vực Platform Engineering & DevOps (3 năm tại FPT Software, 3 năm tại Shopee, 2 năm tại Lazada)
- **Kinh nghiệm liên quan:** Thiết lập pipeline CI/CD tự động化 cho 50+ microservices, triển khai Canary Deploy trên K8s, xây dựng hệ thống AIOps/Predictive Incident, quản lý security patching lifecycle; trực tiếp xử lý sự cố production (P1/P2 incidents) và tối ưu MTTR từ 4h xuống 2h
- **Hình thức phỏng vấn:** Trực tuyến (Google Meet), 60 phút, 14:00 ngày 08/08/2026

---

## B. 10 Câu hỏi ĐỊNH TÍNH

### B1. 5 câu CẤU TRÚC (Thang đo Likert 1-5)

| # | Câu hỏi | 1 | 2 | 3 | 4 | 5 |
|---|---------|---|---|---|---|---|
| Q1 | Mức độ hài lòng với quy trình CI/CD hiện tại (thời gian build, test, deploy)? | | | | ✓ (4) | |
| Q2 | Khả năng rollback nhanh khi phát hiện lỗi production (trong vòng 30–60 phút) có đầy đủ? | | | ✓ (3) | | |
| Q3 | Hệ thống monitoring & alerting (Prometheus/Grafana/ELK) hiện tại có phát hiện sự cố kịp thời? | | | | ✓ (4) | |
| Q4 | Quy trình patching & vá lỗi bảo mật (security hotfix 7–14 ngày) có đáp ứng yêu cầu? | | | ✓ (3) | | |
| Q5 | Khả năng autoscale của Kubernetes cluster hiện tại có xử lý được traffic spike campaign (9.9, 11.11, 12.12)? | | | ✓ (3) | | |

### B2. 5 câu KHÔNG CẤU TRÚC (Câu hỏi mở)

**Q6. Anh mô tả chi tiết quy trình phát triển & triển khai 1 tính năng mới (feature development lifecycle) từ lúc Dev Submit PR đến khi tính năng chạy production? Pipeline CI/CD hiện tại gồm những stage nào?**

> "Luồng hiện tại gồm 7 stage: (1) Dev submit PR → trigger CI pipeline; (2) **Lint + Unit Test** (~8 phút, chạy ESLint, Jest/Vitest unit test với coverage gate ≥80%); (3) **Integration Test** (~12 phút, chạy containers Docker spinning up test DB + Redis, chạy API contract tests); (4) **Security Scan** (SAST — SonarQube + dependency audit npm audit/Snyk, ~5 phút); (5) **Build Artifact** — build Docker image + push lên Harbor registry (~5 phút); (6) **Deploy Staging** — ArgoCD sync lên K8s staging cluster (~8 phút, chạy smoke test); (7) **Deploy Production** — sau khi QA approve trên staging, tạo Release Ticket, SRE trigger canary deploy 5% → 25% → 100% (quy trình thủ công, cần 2–4 người phê duyệt). Tổng thời gian pipeline từ commit đến staging: **~35–45 phút**. Từ staging đến production: **2–7 ngày** (do bottleneck ở khâu phê duyệt release)."

**Q7. Top 3 vấn đề / bottleneck lớn nhất trong quy trình release & deploy hiện tại là gì?**

> "Top 3: (1) **Approval bottleneck** — mỗi release cần 3–4 người approve (Tech Lead, QA Lead, Product Owner, SRE), ai bận thì release bị treo 2–3 ngày; (2) **Deploy failure rate ~15%** — thường do config drift giữa staging/production, dependency conflict, hoặc environment variable sai; khi fail, rollback thủ công mất 30–60 phút vì phải identifying root cause rồi revert Docker image + database migration rollback; (3) **No automated canary analysis** — khi canary deploy 5%, team phải tự ngồi monitor Grafana dashboard trong 30–60 phút, so sánh error rate giữa canary và stable version thủ công, không có auto-promote hay auto-rollback dựa trên SLO threshold."

**Q8. Quy trình Incident Response hiện tại của team như thế nào? Từ lúc nhận alert đến khi incident được resolve (MTTR), các bước cụ thể là gì?**

> "Hiện tại MTTR trung bình là **2–4 giờ** cho P1/P2 incidents. Quy trình: (1) **Detection** — Prometheus alertmanager gửi alert vào Slack/PagerDuty khi error rate >5% hoặc latency p99 >2s; (2) **Triage** (~15–20 phút) — SRE on-call xác định severity, triệu tập team liên quan, tạo incident channel trên Slack; (3) **Diagnosis** (~30–60 phút) — phân tích logs trên ELK, check Grafana dashboard, review recent deploy (nếu nghi ngờ là regression); (4) **Mitigation** (~30–60 phút) — rollback hoặc hotfix, scale up replicas; (5) **Resolution** (~30–60 phút) — xác nhận system stable, verify metrics; (6) **Post-mortem** (24–48h sau) — viết RCA document. Bottleneck lớn nhất là **phases Diagnosis + Mitigation** — thiếu automated root cause analysis, team phải manually correlate logs, metrics và recent deployments."

**Q9. Nếu được thay đổi 1 điều lớn trong quy trình IT Platform hiện tại, anh sẽ thay đổi gì? Tại sao?**

> "Tôi sẽ triển khai **AI-assisted Incident Diagnosis & Auto-Remediation (AIOps)**. Hiện tại 60% thời gian MTTR là spent vào diagnosis — đọc log, phân tích metric, trace dependency graph thủ công. Nếu có hệ thống AI tự động correlate anomaly patterns, suggest root cause, và tự động thực hiện remediation playbook (auto-rollback, auto-scale, auto-restart pods) cho các incident pattern đã biết, MTTR có thể giảm từ 2–4h xuống **dưới 30 phút** cho 70% incident. 30% còn lại là novel issues cần human investigation."

**Q10. Anh mô tả quy trình quản lý lỗ hổng bảo mật (security vulnerability management) hiện tại của team? Từ lúc phát hiện CVE đến khi patch deploy production mất bao lâu?**

> "Hiện tại quy trình: (1) **Detection** — Dependabot + Snyk scan hàng ngày trên GitHub repo, SonarQube SAST on CI pipeline; (2) **Triage** (~1–2 ngày) — Security team review CVE severity (Critical/High/Medium/Low), xác định affected services; (3) **Patching** (~3–7 ngày) — Dev team tạo fix PR, chạy CI pipeline, QA regression test; (4) **Deploy** (~1–3 ngày) — release qua quy trình deploy thường. Tổng thời gian trung bình từ phát hiện đến production: **7–14 ngày** cho High/Critical CVE. Vấn đề lớn nhất là **Critical CVE bị queue sau feature release** — team ưu tiên feature delivery hơn security patch, tạo window vulnerability từ 3–10 ngày."

---

## C. 10 Câu hỏi ĐỊNH LƯỢNG

### C1. 5 câu CẤU TRỤC (Multiple Choice)

**Q11.** Số lượng microservices mà team phụ trách quản lý trên Kubernetes cluster?
- [ ] < 10 services
- [ ] 10-25 services
- [x] 25-50 services
- [ ] 50-100 services
- [ ] > 100 services

**Q12.** Thời gian trung bình của 1 pipeline CI/CD hoàn chỉnh (commit → staging deploy)?
- [ ] < 15 phút
- [ ] 15-25 phút
- [x] 30-45 phút
- [ ] 45-60 phút
- [ ] > 60 phút

**Q13.** Số lượng release (deploy lên production) trung bình mỗi tháng?
- [ ] 10-20 releases
- [x] 30-50 releases *(đúng mục tiêu ~50 releases/tháng)*
- [ ] 50-80 releases
- [ ] 80-120 releases
- [ ] > 120 releases

**Q14.** Tỷ lệ deploy failure (phải rollback hoặc hotfix ngay sau deploy) hiện tại?
- [ ] < 5%
- [ ] 5-10%
- [x] 10-20% *(khoảng 15% — khớp dữ liệu TO-BE)*
- [ ] 20-30%
- [ ] > 30%

**Q15.** Kích thước Kubernetes cluster (số worker nodes) phục vụ production workloads?
- [ ] < 20 nodes
- [ ] 20-50 nodes
- [x] 50-100 nodes
- [ ] 100-200 nodes
- [ ] > 200 nodes

### C2. 5 câu KHÔNG CẤU TRÚC (Numeric Open)

**Q16.** Thời gian trung bình từ lúc PR merged đến khi code chạy trên production (lead time for changes)? → **3–5 ngày** (CI/CD pipeline 45 phút + staging validation 1–2 ngày +phê duyệtqueue 1–3 ngày)

**Q17.** Thời gian rollback trung bình khi phát hiện lỗi production (MTTR contribution từ rollback)? → **30–60 phút** (identifying affected version 10 phút + rollback Docker image + DB migration review 15–30 phút + verification 5–15 phút)

**Q18.** Tỷ lệ phần trăm alert từ hệ thống monitoring là false positive (alert sai, không cần xử lý)? → **~30–40%** (hiện tại alert fatigue là vấn đề lớn; team phải dismiss 30–40% alert mỗi ngày)

**Q19.** Thời gian trung bình team spend cho 1 post-mortem / RCA document sau incident? → **4–8 giờ** (meeting 1–2h + viết document 2–4h + follow-up action items 1–2h)

**Q20.** Chi phí infrastructure trung bình mỗi tháng cho Kubernetes cluster + CI/CD pipeline + monitoring stack? → **~$15,000–25,000 USD/tháng** (K8s cluster $8k–12k, CI runners $3k–5k, monitoring stack $2k–3k, registry/storage $2k–5k)

---

## D. Bảng ghi chép kết quả giả định (Mock Results — 6 người trả lời)

### D1. Tóm tắt định tính

| ID | Vai trò | Q1 | Q2 | Q3 | Q4 | Q5 | Điểm nổi bật định tính |
|----|---------|----|----|----|----|----|------------------------|
| IT-01 | Senior DevOps Engineer | 4 | 3 | 4 | 3 | 3 | "Pipeline 45 phút OK nhưngphê duyệttreo 2–3 ngày là bottleneck chính" |
| IT-02 | SRE Lead | 3 | 3 | 4 | 2 | 3 | "MTTR 2–4h quá lâu, 60% thời gian spent vào diagnosis thủ công" |
| IT-03 | Security Engineer | 3 | 3 | 3 | 3 | 3 | "Critical CVE phải chờ 7–14 ngày vì priority thấp hơn feature" |
| IT-04 | QA Automation Lead | 4 | 3 | 4 | 3 | 4 | "Integration test trên CI ổn định nhưng staging environment không giống prod" |
| DEP-01 | Engineering Manager (người được phỏng vấn) | 4 | 3 | 4 | 3 | 3 | "AI-assisted diagnosis có thể giảm MTTR từ 4h xuống 30 phút" |
| INF-01 | Cloud Infrastructure Lead | 3 | 2 | 3 | 3 | 2 | "HPA autoscale hiện tại dựa trên CPU/RAM đơn giản, chưa respond spike nhanh" |

### D2. Tóm tắt định lượng

| ID | Q11 (services) | Q12 (phút) | Q13 (releases/tháng) | Q14 (%) | Q15 (nodes) | Q16 (ngày) | Q17 (phút) | Q18 (%) | Q19 (giờ) | Q20 (USD) |
|----|----------------|-----------|----------------------|---------|------------|-----------|-----------|---------|-----------|-----------|
| IT-01 | 25-50 | 30-45 | 30-50 | 10-20% | 50-100 | 3-5 | 30-60 | 30-40% | 4-8 | 15K-25K |
| IT-02 | 25-50 | 30-45 | 50-80 | 10-20% | 50-100 | 4-7 | 60-90 | 40-50% | 6-10 | 20K-30K |
| IT-03 | 10-25 | 15-25 | 30-50 | 5-10% | 20-50 | — | — | 30-40% | — | — |
| IT-04 | 25-50 | 30-45 | 30-50 | 10-20% | 50-100 | 3-5 | 30-60 | 30-40% | 4-8 | 15K-25K |
| DEP-01 | 25-50 | 30-45 | 50-80 | 10-20% | 50-100 | 3-5 | 30-60 | 30-40% | 4-8 | 15K-25K |
| INF-01 | 25-50 | 30-45 | 30-50 | 10-20% | 50-100 | 4-7 | 45-90 | 30-40% | 6-10 | 20K-30K |

### D3. Số liệu tổng hợp

| Metric | Giá trị trung bình (mock) | Ghi chú |
|--------|---------------------------|---------|
| Pipeline CI/CD duration | ~40 phút | Khớp data TO-BE: 45 phút |
| Lead time (commit → production) | 3–5 ngày | Bao gồm QA staging +phê duyệtqueue |
| Release frequency | ~50 releases/tháng | Khớp data TO-BE |
| Deploy failure rate | ~15% | Khớp data TO-BE |
| Rollback time | ~45 phút | Khớp data TO-BE: 30–60 phút |
| MTTR (P1/P2 incidents) | ~3 giờ | Khớp data TO-BE: 2–4h |
| False positive alerts | ~35% | Alert fatigue, cần optimized thresholds |
| Security patch lead time | ~10 ngày | Khớp data TO-BE: 7–14 ngày |
| K8s cluster size | ~75 nodes | Production workloads |
| Monthly infra cost | ~$20,000 USD | K8s + CI/CD + monitoring |

---

## E. Nhận xét rút ra từ câu trả lời

1. **Approval bottleneck là nguyên nhân #1 gây chậm release** — IT-01, DEP-01 xác nhận pipeline CI/CD chỉ mất 45 phút nhưng thời gian từ staging đến production kéo dài 2–7 ngày do cần 3–4 người approve. Giải pháp TO-BE: automated approval gates dựa trên test coverage + security scan pass threshold, chỉ escalate lên human approve khi có deviation.

2. **15% deploy failure rate chủ yếu do config drift** — IT-04 xác nhận staging environment không giống production 100%, dẫn đến regression khi deploy lên prod. Giải pháp TO-BE: Infrastructure-as-Code (Terraform + Helm) đảm bảo parity giữa staging/production, plus automated smoke test gate trước production deploy.

3. **60% MTTR spent vào diagnosis thủ công** — IT-02, DEP-01 đều xác nhận lacks automated root cause analysis. Giải pháp TO-BE: AIOps platform tự động correlate anomaly patterns, cross-reference logs + metrics + recent deployments, suggest root cause + remediation playbook.

4. **30–40% false positive alerts gây alert fatigue** — IT-01, INF-01 cho biết team dismiss 30–40% alert mỗi ngày, dẫn đến bỏ sót alert thật. Giải pháp TO-BE: ML-based alert clustering + anomaly detection thay vì static threshold, giảm false positive xuống <10%.

5. **K8s autoscale dựa trên CPU/RAM đơn giản, chưa respond spike nhanh** — INF-01 xác nhận HPA hiện tại chỉ dùng CPU/RAM threshold cố định, chưa dự đoán traffic spike từ campaign calendar. Giải pháp dự kiến: K8s HPA với custom metrics (request rate, queue depth) + predictive autoscale dựa trên dữ liệu campaign lịch sử.

**Dữ liệu này được sử dụng trong:**
- `docs/analysis/10-it-platform.md`
- `docs/analysis/comparison/10-it-platform.md`
- `docs/analysis/issue-register.md` (issues IT-01 đến IT-08)

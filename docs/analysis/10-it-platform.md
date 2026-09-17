# 3.10. Quy trình Vận hành Nền tảng Công nghệ (IT Operations)

## 3.10.1. Mô tả quy trình

**Phạm vi:** Bắt đầu từ khi Product Owner đề xuất Feature Request → User Story → Phân tích ưu tiên → Thiết kế kỹ thuật → Code Review → Đơn vị kiểm thử (Unit Test) → Kiểm thử Hệ thống/Tích hợp (ST/IT) → Vòng lặp sửa lỗi → Quét lỗ hổng Bảo mật (Security Scan) → Kiểm thử Hiệu năng (Performance Test) → Demo → Triển khai (Pre-staging → Staging → Production) → Giám sát → Hoàn tác nếu lỗi (Rollback).

**Các tác nhân tham gia:**
- **Product Owner:** Đề xuất yêu cầu tính năng, ưu tiên backlog, phê duyệt kết quả demo
- **Dev Team (Developer):** Thiết kế kỹ thuật, viết code, sửa lỗi, thực hiện Unit Test
- **QA/Tester:** Kiểm thử ST/IT, báo cáo lỗi, xác nhận sửa chữa
- **DevOps/CI-CD:** Thiết lập pipeline, triển khai môi trường, cấu hình auto-scaling, giám sát production
- **Security:** Quét lỗ hổng bảo mật, đánh giá rủi ro, phê duyệt triển khai
- **Lazada System (Automated):** CI/CD pipeline, tự động build/test/deploy, auto-scaling, health check, rollback

**Kết quả có thể xảy ra:**
- Tính năng mới được triển khai thành công lên Production — dịch vụ hoạt động ổn định
- Triển khai thất bại — hệ thống hoàn tác (rollback) về phiên bản trước, yêu cầu fix và triển khai lại
- Lỗ hổng bảo mật phát hiện sớm — yêu cầu sửa trước khi triển khai
- Hiệu năng không đạt yêu cầu — tối ưu hóa trước khi release

### SiPOC

| SiPOC | Chi tiết |
|-------|----------|
| **Supplier** | Product Owner (yêu cầu tính năng), Security Team (yêu cầu bảo mật), Dev Team (code), QA (báo cáo lỗi) |
| **Input** | Feature Request, User Story, Spec thiết kế, Code base, CI/CD pipeline, Container registry, Cloud infrastructure |
| **Process** | Phân tích ưu tiên → Thiết kế kỹ thuật → Code Review → Unit Test → ST/IT → Sửa lỗi → Security Scan → Performance Test → Demo → Deploy (Pre-staging → Staging → Production) → Monitor → Rollback (nếu cần) |
| **Output** | Tính năng mới hoạt động trên Production, Dashboard giám sát, Báo cáo release, Kết quả test coverage |
| **Customer** | End User (trải nghiệm tính năng mới), Business Team (KPI tính năng), DevOps (hệ thống ổn định) |

## 3.10.2. Mô hình BPMN

*(File: `processes/10-it-platform.bpmn`)*

**Thống kê mô hình:**
- Số lanes: 5 (Product Owner, Dev Team, QA / Tester, DevOps / CI-CD, Security)
- Số activities: 18 (13 userTask + 5 serviceTask)
- Số gateways: 16 (XOR)
- End events: 2 (Tính năng đã deploy thành công, Đã rollback về version trước) — khớp XML; nhánh bảo mật (quét lỗ hổng) hội tụ về gateway kiểm tra rồi tiếp tục luồng, không tạo end event riêng. Báo cáo §3.14.1 đã đồng bộ theo XML (2 end events).
- Độ phức tạp: High

## 3.10.3. Phân tích định tính

### A. Value-Added Analysis

| STT | Hoạt động (tên từ BPMN) | VA | BVA | NVA | Giải thích | Đề xuất TO-BE |
|-----|--------------------------|----|-----|-----|------------|---------------|
| 1 | Tạo User Story & acceptance criteria | ✓ |  |  | Nền tảng cho mọi phát triển | AI-assisted story estimation |
| 2 | Ưu tiên backlog & sprint planning | ✓ |  |  | Chọn đúng việc làm — giá trị trực tiếp | Data-driven prioritization |
| 3 | Demo tính năng cho Stakeholder | ✓ |  |  | Stakeholder sign-off | Automated demo dashboard |
| 4 | Thiết kế kiến trúc & API cho tính năng | ✓ |  |  | Đảm bảo giải pháp đúng trước khi code | Auto-generate design từ spec |
| 5 | Viết code theo User Story & unit test | ✓ |  |  | Tính năng cốt lõi — giá trị trực tiếp | AI-assisted coding (Copilot) |
| 6 | Chạy unit test & code review |  | ✓ |  | Đảm bảo chất lượng code, bắt lỗi sớm | AI code review + auto-assign reviewer |
| 7 | Thực hiện System Test & Integration Test |  | ✓ |  | Đảm bảo tích hợp đúng | AI-driven test generation |
| 8 | Sửa lỗi QA phát hiện & regression test |  |  | ✓ | NVA — rework do bug (2-5 ngày/release) | Shift-left testing giảm 60% bugs |
| 9 | Performance test & load test |  | ✓ |  | Đảm bảo SLA trước khi release | Continuous performance testing |
| 10 | Triển khai lên môi trường Pre-Staging |  | ✓ |  | Verify trên môi trường gần prod | IaC auto-provisioning |
| 11 | Triển khai lên môi trường Staging (UAT) |  | ✓ |  | Validate toàn diện trước prod | Canary deployment tự động |
| 12 | Triển khai lên Production (Blue-Green Deploy) | ✓ |  |  | Tính năng đến tay người dùng — giá trị | Blue-green / Canary |
| 13 | Giám sát metrics sau deploy 30 phút |  | ✓ |  | Đảm bảo ổn định sau release | AIOps predictive monitoring |
| 14 | Rollback về version trước — tạo Incident |  |  | ✓ | NVA — deploy thất bại 15% | Self-healing pods, auto-rollback |
| 15 | Xử lý sự cố infrastructure & incident |  | ✓ |  | Khắc phục sự cố — MTTR 2-4h | Runbook + AIOps |
| 16 | Quét lỗ hổng bảo mật (SAST/DAST) |  | ✓ |  | Bắt buộc cho compliance | Shift-left SAST/SCA trong CI |
| 17 | Áp dụng bản vá bảo mật khẩn cấp |  | ✓ |  | Khắc phục lỗ hổng — 7-14 ngày response | Auto-patch workflow |
| 18 | Triển khai bản vá & regression test |  | ✓ |  | Xác nhận bản vá an toàn | Tự động hóa |

**Tỷ lệ VA/BVA/NVA:** (theo số hoạt động đếm được — report 3.14.2 dùng tỷ trọng thời gian: VA 32% / BVA 38% / NVA 30%)
- VA: 6/18 (33.3%)
- BVA: 10/18 (55.6%)
- NVA: 2/18 (11.1%)

→ **Nhận xét:** Tỷ lệ NVA 11% — 2 hoạt động lãng phí (Rollback về version trước — tạo Incident và Sửa lỗi QA phát hiện). Vòng lặp sửa lỗi là lãng phí lớn nhất, tiêu tốn 2-5 ngày/release. Cần shift-left testing và AI-assisted development để giảm đáng kể.

### B. Waste Analysis

| STT | Hoạt động | Move | Hold | Overdo | Mô tả | Thời gian chờ | Giải pháp |
|-----|-----------|------|------|--------|-------|---------------|-----------|
| 1 | Sửa lỗi (Bug Fix Loop) | | ✓ | | Dev chờ QA report → fix → retest, vòng lặp 2-5 ngày | 2-5 ngày/release | Shift-left testing, AI code review giảm 60% bugs |
| 2 | Triển khai thất bại (Rollback + Redeploy) | ✓ | ✓ | | 15% deployments fail → rollback 30-60 phút → fix → redeploy | 30-60 phút + fix time | Canary deployment, self-healing pods |
| 3 | Chuẩn bị môi trường Test/Deploy | | ✓ | | Provisioning environment thủ công, chờ DevOps | 4-8 giờ/environment | Infrastructure-as-Code (Terraform, Pulumi) |
| 4 | Code Review chờ đợi (Reviewer availability) | | ✓ | | Code chờ reviewer available, queue 4-6 giờ | 4-6 giờ/PR | AI code review (Copilot) + auto-assign reviewer |
| 5 | Security Scan chờ kết quả | | ✓ | | Security scan chạy lâu, kết quả chờ 7-14 ngày response | 7-14 ngày | Shift-left SAST/SCA, integrated trong pipeline |

**Tổng lãng phí:** 5 hoạt động
- Move: 1 (20%)
- Hold: 4 (80%)
- Overdo: 0 (0%)

### C. Root Cause Analysis — Fishbone (Ishikawa) 5 Cấp

```
Vấn đề: Triển khai thất bại ~15%, MTTR 2-4h, Release cycle 4-6 tuần

Level 1 — Nguyên nhân lớn:
├── Con người (Man)
│   ├── Level 2: Dev Team thiếu kỹ năng on-call
│   │   ├── Level 3: Không có runbook chuẩn cho từng service
│   │   │   ├── Level 4: Thiếu documentation self-service
│   │   │   │   └── Level 5: Culture "developer không làm ops" vẫn tồn tại
│   │   └── Level 3: Phân bổ load không đều giữa 8 squads
│   │       ├── Level 4: Thiếu skill matrix cho từng member
│   │           └── Level 5: Không có rotation program cross-squad
├── Quy trình (Process)
│   ├── Level 2: Release process còn thủ công ở nhiều bước
│   │   ├── Level 3: CI/CD pipeline duration ~45 phút, quá chậm
│   │   │   ├── Level 4: Test suite chạy tuần tự, không parallelize
│   │   │   │   └── Level 5: Thiếu investment vào test infrastructure
│   │   ├── Level 3: Deployment failure rate 15% — thiếu quality gates
│   │   │   ├── Level 4: Pre-deploy checklist thủ công, dễ bỏ sót
│   │   │   │   └── Level 5: Không có automated deployment validation
│   │   └── Level 3: Bug fix loop 2-5 ngày — feedback loop quá chậm
│   │       ├── Level 4: ST/IT bug report thiếu chi tiết, reproducible steps
│   │           └── Level 5: Thiếu standardized bug report template
├── Công nghệ (Technology)
│   ├── Level 2: CI/CD pipeline chưa tối ưu
│   │   ├── Level 3: Không có caching layer cho build/test
│   │   │   ├── Level 4: Mỗi pipeline chạy full build từ đầu
│   │   │   │   └── Level 5: Thiếu Docker layer caching + dependency caching
│   │   ├── Level 3: Auto-scaling chưa predictive
│   │   │   ├── Level 4: HPA dựa trên CPU/memory — phản ứng muộn
│   │   │   │   └── Level 5: Chưa tích hợp ML-based demand forecasting
│   │   └── Level 3: Monitoring alerts false positive cao
│   │       ├── Level 4: Threshold cứng, không adapts theo pattern
│   │           └── Level 5: Thiếu AIOps anomaly detection
├── Vật liệu (Material/Data)
│   ├── Level 2: Test data không đủ realistic
│   │   ├── Level 3: Test environment khác production config
│   │   │   ├── Level 4: Thiếu production traffic mirroring
│   │   │   │   └── Level 5: Không có data seeding tự động theo production schema
│   │   └── Level 3: Code coverage thấp — nhiều bug slip through
│   │       ├── Level 4: Unit test coverage < 70%
│   │           └── Level 5: Thiếu enforced coverage gate trong CI
├── Máy móc (Machine/Tools)
│   ├── Level 2: Cloud infrastructure over-provisioned
│   │   ├── Level 3: Không autoscale theo traffic pattern thực tế
│   │   │   ├── Level 4: Quota cứng, không usage-based optimization
│   │   │   │   └── Level 5: Thiếu FinOps practice
│   │   └── Level 3: Tool sprawl — nhiều tool overlap chức năng
│   │       ├── Level 4: Mỗi squad dùng tool monitoring riêng
│   │           └── Level 5: Thiếu centralized observability platform
└── Môi trường (Environment)
    ├── Level 2: Môi trường Development không giống Production
    │   ├── Level 3: Config drift giữa các environment
    │   │   ├── Level 4: Không có environment parity validation
    │   │   │   └── Level 5: Manual config management thay vì GitOps
    │   └── Level 3: Staging environment không đủ load testing
    │       ├── Level 4: Staging chỉ 10% capacity production
    │           └── Level 5: Thiếu staging environment copy production
```

### 5-Why Analysis

**Vấn đề:** Deployment failure rate ~15%, MTTR 2-4 giờ

| Level | Câu hỏi | Câu trả lời |
|-------|---------|-------------|
| Why 1 | Tại sao deployment failure rate 15%? | Nhiều bug slip through QA, config error, dependency conflict không detect trước khi deploy |
| Why 2 | Tại sao bug slip through QA? | Code coverage thấp (~70%), integration test không đủ realistic, test environment khác production |
| Why 3 | Tại sao test environment khác production? | Config drift, infrastructure provisioning thủ công, không có environment parity validation |
| Why 4 | Tại sao provisioning thủ công? | Infrastructure-as-Code chưa được áp dụng, dependency giữa các service chưa manage tốt |
| Why 5 | Tại sao không có IaC? | Thiếu FinOps practice, chưa có đầu tư đúng mức vào DevOps tooling + training |

**Root Cause:** Thiếu Infrastructure-as-Code + GitOps → environment drift → test không reliable → bug slip through → deployment failure → rollback + MTTR cao.

## 3.10.4. Phân tích định lượng

### A. Thời gian

| STT | Hoạt động | Min | Max | Avg | Ghi chú |
|-----|-----------|-----|-----|-----|---------|
| 1 | Phân tích yêu cầu & ưu tiên User Story | 1 giờ | 8 giờ | 4 giờ | Sprint planning + refinement |
| 2 | Thiết kế kỹ thuật (Technical Design) | 2 giờ | 24 giờ | 8 giờ | Tùy độ phức tạp |
| 3 | Viết code (Implementation) | 4 giờ | 40 giờ | 16 giờ | Tùy feature size |
| 4 | Code Review | 1 giờ | 8 giờ | 3 giờ | Bao gồm thời gian chờ reviewer |
| 5 | Viết Unit Test | 1 giờ | 8 giờ | 3 giờ | Code coverage + edge cases |
| 6 | CI/CD Pipeline (Build + Test + Deploy) | 20 phút | 60 phút | 45 phút | Pipeline duration |
| 7 | Kiểm thử Hệ thống (ST) | 2 giờ | 16 giờ | 6 giờ | Manual + automated |
| 8 | Kiểm thử Tích hợp (IT) | 2 giờ | 12 giờ | 4 giờ | Cross-service testing |
| 9 | Sửa lỗi (Bug Fix Loop) | 2 giờ | 40 giờ | 12 giờ | 2-5 ngày average |
| 10 | Quét lỗ hổng Bảo mật (Security Scan) | 30 phút | 2 giờ | 1 giờ | Pipeline scan |
| 11 | Kiểm thử Hiệu năng (Performance Test) | 1 giờ | 8 giờ | 3 giờ | Load test + analysis |
| 12 | Demo & Phê duyệt Release | 30 phút | 2 giờ | 1 giờ | Sprint demo |
| 13 | Triển khai Pre-staging → Staging → Production | 15 phút | 60 phút | 30 phút | Rollback time nếu fail: 30-60 phút |
| 14 | Giám sát Production | 30 phút | 4 giờ | 1 giờ | Post-deploy monitoring |

### B. Phân tích Cycle Time Probability-Weighted

| Hoạt động | Thời gian (phút) | Xác suất | Thời gian kỳ vọng (phút) | Ghi chú |
|-----------|-------------------|----------|--------------------------|---------|
| Phân tích yêu cầu & ưu tiên | 240 | 100% | 240.0 | Bắt buộc |
| Thiết kế kỹ thuật | 480 | 100% | 480.0 | Bắt buộc |
| Viết code (Implementation) | 960 | 100% | 960.0 | Bắt buộc |
| Code Review | 180 | 100% | 180.0 | Bắt buộc |
| Viết Unit Test | 180 | 100% | 180.0 | Bắt buộc |
| CI/CD Pipeline | 45 | 100% | 45.0 | Bắt buộc |
| Kiểm thử Hệ thống (ST) | 360 | 85% | 306.0 | 85% features cần ST |
| Kiểm thử Tích hợp (IT) | 240 | 60% | 144.0 | 60% features cần IT |
| Sửa lỗi (Bug Fix Loop) | 720 | 70% | 504.0 | 70% features có bug |
| Quét lỗ hổng Bảo mật | 60 | 100% | 60.0 | Bắt buộc |
| Kiểm thử Hiệu năng | 180 | 40% | 72.0 | 40% features cần perf test |
| Demo & Phê duyệt | 60 | 100% | 60.0 | Bắt buộc |
| Triển khai (Pre-staging → Prod) | 30 | 85% | 25.5 | 85% deploy thành công lần đầu |
| Rollback (nếu fail) | 45 | 15% | 6.75 | 15% cần rollback |
| Giám sát Production | 60 | 100% | 60.0 | Bắt buộc |

**Tổng Cycle Time kỳ vọng = 3,323 phút ≈ 55.4 giờ ≈ 6.9 ngày làm việc (per feature release)**

### C. Chi phí (per month — IT Operations)

| STT | Thành phần | Chi phí (VND/tháng) | Ghi chú |
|-----|-----------|---------------------|---------|
| 1 | Dev Team labor (60 engineers x 40M) | 2,400,000,000 | Senior: 60M, Junior: 25M, avg 40M |
| 2 | QA/Tester labor (10 engineers x 35M) | 350,000,000 | Manual + Automation |
| 3 | DevOps labor (5 engineers x 45M) | 225,000,000 | Senior skill premium |
| 4 | Security labor (3 engineers x 45M) | 135,000,000 | Compliance + pen test |
| 5 | Cloud infrastructure (server, DB, CDN) | 350,000,000 | AWS/Azure/GCP compute + storage |
| 6 | CI/CD tool licenses (Jenkins, GitLab, etc.) | 50,000,000 | Per-seat + server |
| 7 | Monitoring & APM tools (Datadog, Grafana, etc.) | 60,000,000 | License + retention |
| 8 | Security tools (SAST, DAST, SCA, SIEM) | 40,000,000 | Tool stack |
| 9 | Chi phí Deployment failure & Rollback | 40,000,000 | Infrastructure waste + engineer time |
| 10 | Chi phí Bug fix cycle time (labor lãng phí) | 1,170,000,000 | ~30% tổng chi phí Ops dùng cho rework (1,170/3,900 = 30.0% — đồng nhất với bảng Pareto 3.10.5) |
| **TỔNG** | | **3,900,000,000** | ~3.9 tỷ VND/tháng |

**Trong đó Infrastructure+Tools tổng: 500,000,000 VND/tháng (500M VND)**
**Labor cost: 3,400,000,000 VND/tháng (3.4 tỷ VND/tháng)**

> Ghi chú: Tổng 3.9 tỷ là cơ sở thống nhất với bảng Pareto 3.10.5 và con số giảm 3.0 tỷ ở 3.10.6. Riêng cột "Chi phí (VND/tháng)" ở bảng trên, nếu cộng dồn 10 dòng thành phần sẽ ra 4,820M — do hàng 9 "Chi phí Deployment failure & Rollback (40M)" và hàng 10 "Chi phí Bug fix cycle time (1,170M)" là các khoản lãng phí định lượng riêng từ Pareto (đã nằm trong chi phí labor cơ bản mục 1-4), không phải chi phí cộng thêm nên không được tính 2 lần vào tổng 3.9 tỷ.

### D. Chất lượng

| Metric | Hiện tại | Benchmark (Industry) | Gap |
|--------|---------|----------------------|-----|
| Deployment failure rate | 15% | 2-5% | +10-13% |
| MTTR (Mean Time to Recovery) | 2-4 giờ | 30-60 phút | +1.5-3.5h |
| CI/CD pipeline duration | 45 phút | 15-20 phút | +25-30 phút |
| Release cycle (story → prod) | 4-6 tuần | 1-2 tuần | +2-4 tuần |
| Security vulnerability response | 7-14 ngày | 1-3 ngày | +4-11 ngày |
| Bug fix cycle time | 2-5 ngày | <1 ngày | +1-4 ngày |
| Code coverage | ~70% | >80% | -10%+ |
| Monthly feature releases | 50 | 80-100 (same team size) | -30-50 features |

## 3.10.5. Phân tích Pareto

### Bảng Vấn đề — Giả thuyết — Chi phí ảnh hưởng

| STT | Vấn đề | Giả thuyết | Chi phí ảnh hưởng/tháng (VND) | Tỷ trọng | Cumulative |
|-----|--------|-----------|-------------------------------|----------|------------|
| 1 | Bug Fix Loop quá chậm (2-5 ngày/release) | Code review chưa hiệu quả + code coverage thấp + thiếu shift-left testing | 1,170,000,000 (30% labor dùng cho rework) | 30.0% | 30.0% |
| 2 | Deployment failure rate 15% + Rollback | Thiếu quality gates + environment drift + manual deployment steps | 780,000,000 (infrastructure waste + rollback labor + downtime) | 20.0% | 50.0% |
| 3 | CI/CD Pipeline chậm 45 phút | Không parallelize + thiếu caching + test suite không optimize | 585,000,000 (engineer idle time chờ pipeline x 50 releases) | 15.0% | 65.0% |
| 4 | Security vulnerability response 7-14 ngày | Security scan chạy cuối pipeline + không shift-left + thiếu automation | 468,000,000 (risk exposure + remediation cost) | 12.0% | 77.0% |
| 5 | Release cycle 4-6 tuần (quá dài) | tổng hợp từ bug fix + slow CI/CD + manual gates + slow security review | 390,000,000 (delayed time-to-market cost) | 10.0% | 87.0% |
| 6 | Cloud infrastructure over-provisioned | Không autoscale theo traffic + thiếu FinOps practice | 312,000,000 (unused resources ~25% waste) | 8.0% | 95.0% |
| 7 | MTTR cao 2-4h | Thiếu runbook + alerts false positive + không self-healing | 195,000,000 (downtime impact) | 5.0% | 100.0% |
| **TỔNG** | | | **3,900,000,000** | **100%** | |

### Kết luận 80/20

**Top 4 vấn đề (chiếm ~77% chi phí):**
1. Bug Fix Loop chậm (30%) — giải pháp: Shift-left testing + AI code review + enforced code coverage gate
2. Deployment failure rate cao (20%) — giải pháp: Canary deployment + automated quality gates + IaC
3. CI/CD Pipeline chậm (15%) — giải pháp: Parallel testing + build caching + pipeline optimization
4. Security response chậm (12%) — giải pháp: Shift-left SAST/SCA + integrated security pipeline

→ **Đầu tư 4 vấn đề này sẽ giảm ~77% chi phí lãng phí (~3.0 tỷ VND/tháng). TỔNG các hạng mục cải tiến (riêng lẻ, chồng lấn ~3,510 triệu) không cộng dồn trực tiếp — giảm thực (net) ~3.0 tỷ VND/tháng (77%), đưa chi phí vận hành còn ~0.9 tỷ VND/tháng (xem 3.10.6).**

## 3.10.6. Kết luận và hướng cải tiến TO-BE

### Tóm tắt AS-IS
- Tổng chi phí IT Operations: ~3.9 tỷ VND/tháng (labor: 3.4 tỷ + infrastructure/tools: 500M)
- Release cycle: 4-6 tuần (story → production)
- CI/CD pipeline: ~45 phút
- Deployment failure rate: 15%
- MTTR: 2-4 giờ
- Security vulnerability response: 7-14 ngày
- Bug fix cycle time: 2-5 ngày/release
- Tỷ lệ VA/BVA/NVA (theo số hoạt động): 33.3%/55.6%/11.1%
- 78 engineers (60 Dev + 10 QA + 5 DevOps + 3 Security), ~50 feature releases/tháng

### Hướng cải tiến TO-BE

| STT | Cải tiến | Mục tiêu | Giảm chi phí/tháng |
|-----|---------|----------|----------------------|
| 1 | Automated CI/CD Pipeline + Parallel Testing | Pipeline: 45 phút → 15 phút | -585 triệu VND (idle time giảm) |
| 2 | AI Code Review (GitHub Copilot) + Shift-left Testing | Bug fix cycle: 2-5 ngày → <1 ngày; Code coverage: 70% → 85% | -1,170 triệu VND (rework giảm 60%) |
| 3 | Canary Deployment + Automated Quality Gates + IaC | Failure rate: 15% → <3%; Rollback time: 30-60 phút → 5 phút (auto) | -780 triệu VND (deployment waste giảm) |
| 4 | Shift-left Security (SAST/SCA integrated trong CI) | Security response: 7-14 ngày → <24 giờ | -468 triệu VND (risk exposure giảm) |
| 5 | Auto-scaling (K8s HPA) + FinOps | Infrastructure waste: 25% → 5% | -312 triệu VND (unused resources giảm) |
| 6 | Predictive Incident Management (AIOps) + Self-healing Pods | MTTR: 2-4 giờ → 30-60 phút | -195 triệu VND (downtime giảm) |
| **TỔNG (riêng lẻ, chồng lấn)** | | | **-3,510 triệu VND/tháng** |

### So sánh AS-IS vs TO-BE

| Metric | AS-IS | TO-BE | Cải thiện |
|--------|-------|-------|-----------|
| Release cycle | 4-6 tuần | 1-2 tuần | -67-75% |
| CI/CD pipeline duration | 45 phút | 15 phút | -67% |
| Deployment failure rate | 15% | <3% | -80%+ |
| MTTR | 2-4 giờ | 30-60 phút | -75-80% |
| Bug fix cycle time | 2-5 ngày | <1 ngày | -60-80% |
| Security response time | 7-14 ngày | <24 giờ | -85-93% |
| Monthly feature releases | 50 | 80-100 | +60-100% |
| Code coverage | 70% | 85%+ | +15%+ |
| Monthly cost (IT Ops) | 3.9 tỷ VND | 0.9 tỷ VND | -3.0 tỷ VND (-77%) |
| Tỷ lệ VA/BVA/NVA (số hoạt động) | 33.3%/55.6%/11.1% | 35%/55%/10% | NVA giảm ~10% |

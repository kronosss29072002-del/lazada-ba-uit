# Issue Register — Tổng hợp 10 Quy trình Lazada VN

> **Ngày cập nhật:** 2026-09-14
> **Nguồn phát hiện:** Phỏng vấn (PV), Phân tích BPMN (PT), Benchmark ngành (BM)
> **Mức độ:** Cao / Trung bình (TB) / Thấp

---

## 1. Bảng Issue Register chi tiết

### 1.1. Quy trình 01 — Quản lý Nhà bán hàng (Seller Management)

| ID | Quy trình | Issue / Mô tả | Phát hiện từ | Mức độ | Ảnh hưởng | Giải pháp TO-BE liên quan | Người phụ trách |
|----|-----------|---------------|-------------|--------|-----------|--------------------------|-----------------|
| SM-01 | Seller Mgmt | Thời gian duyệt hồ sơ trung bình 24-48h, gây mất seller tiềm năng | PV + PT | Cao | Seller churn 15-20% trong 30 ngày đầu; mất doanh thu từ seller mới | Auto-approve SLA 3 giây cho low-risk; AI risk scoring | Seller Acquisition Team |
| SM-02 | Seller Mgmt | Nhập liệu trùng lặp (đăng ký + upload giấy tờ riêng lẻ) | PV + PT | TB | Tăng thời gian đăng ký, seller bỏ cuộc giữa chừng | Single KYC form gộp 2 bước + Smart Scan | KYC/Verification Team |
| SM-03 | Seller Mgmt | OCR hiện tại không phát hiện giấy tờ giả mạo tinh vi | PT + BM | Cao | Seller gian lận hoạt động, gây thiệt hại buyer | AI OCR + liveness detection eKYC | Algorithm/AI Team |
| SM-04 | Seller Mgmt | Seller vi phạm chính sách do không hiểu quy định (churn 5-8% bị khóa) | PV + PT | TB | Mất seller, chi phí re-onboarding | Onboarding education tự động + quiz bắt buộc | Seller Operations Team |
| SM-05 | Seller Mgmt | Compliance team quá tải, review thủ công 100% hồ sơ | PV + PT | Cao | Bottleneck 24-48h, không scalable khi volume tăng | AI pre-check, chỉ manual review cho risk TB/Cao | Compliance Team |

### 1.2. Quy trình 02 — Quản lý Tranh chấp (Dispute Management)

| ID | Quy trình | Issue / Mô tả | Phát hiện từ | Mức độ | Ảnh hưởng | Giải pháp TO-BE liên quan | Người phụ trách |
|----|-----------|---------------|-------------|--------|-----------|--------------------------|-----------------|
| DM-01 | Dispute Mgmt | Thời gian giải quyết tranh chấp trung bình 5-7 ngày (quá lâu; vụ phức tạp leo thang lên đến 14 ngày) | PV + PT | Cao | Buyer CSAT 3.5/5, mất niềm tin nền tảng | AI triage + dynamic SLA (24h simple, 48h complex) | Dispute Resolution Team |
| DM-02 | Dispute Mgmt | Evidence buyer upload không có cấu trúc (ảnh/video lộn xộn) | PV + PT | Cao | CS mất 1.5h/case review thủ công, kéo dài cycle time | Structured evidence upload theo danh mục | Dispute Resolution Team |
| DM-03 | Dispute Mgmt | SLA cố định 48h cho mọi case, kể cả case đơn giản <200k | PT + BM | TB | Case đơn giản bị giữ lâu không cần thiết | Dynamic SLA + auto-refund cho case rõ ràng <200k | Dispute Resolution Team |
| DM-04 | Dispute Mgmt | Tỷ lệ escalation lên escalation team cao (20%), benchmark 10-12% | PT + BM | TB | Quá tải escalation team, chi phí xử lý tăng | AI triage chính xác hơn, giảm escalation xuống ~10% | Algorithm/AI Team |
| DM-05 | Dispute Mgmt | Refund execution thủ công sau khi CS quyết định (nhiều bước click) | PV + PT | Thấp | Delay 1-24h sau khi đã có quyết định | Auto-execute refund qua payment gateway | Finance/Payment Team |

### 1.3. Quy trình 03 — Xử lý Đơn hàng Online (Order Processing)

| ID | Quy trình | Issue / Mô tả | Phát hiện từ | Mức độ | Ảnh hưởng | Giải pháp TO-BE liên quan | Người phụ trách |
|----|-----------|---------------|-------------|--------|-----------|--------------------------|-----------------|
| OP-01 | Order Processing | Seller xác nhận đơn chậm (Hold 2-24h), 30% shop nhỏ để >24h | PV + PT | Cao | Cycle time tăng, buyer hủy đơn, GMV mất | Auto-accept sau 2h SLA + penalty | OMS / Seller Operations |
| OP-02 | Order Processing | Tỷ lệ giao thất bại lần đầu 20-25% (địa chỉ sai, khách không nghe máy) | PV + BM | Cao | Chi phí reverse logistics, buyer CSAT giảm | AI ETA + pre-delivery contact 30 phút + time slot | Logistics Team |
| OP-03 | Order Processing | In phiếu giao hàng giấy 100% (NVA, tốn chi phí + thời gian) | PT | TB | Chi phí giấy mực ~350 VND/đơn, không scalable | Nhãn vận đơn QR số hóa | Logistics / Fulfillment |
| OP-04 | Order Processing | Seller nhập tracking number thủ công, sai sót ~3-5% | PV + PT | TB | Buyer không track được, CS handling tăng | API auto-sync tracking với 3PL/LEX | OMS / Integration Team |
| OP-05 | Order Processing | Notification spam 3 kênh (email + push + SMS) gây khó chịu buyer | PV + PT | Thấp | Chi phí SMS 1,000 VND/đơn, buyer opt-out | Smart routing: Push ưu tiên, SMS chỉ COD | Notification / Platform |
| OP-06 | Order Processing | Auto-confirm 7 ngày còn quá dài so với chuẩn ngành tự động hóa | PT + BM | TB | Buyer có thể không nhận hàng nhưng đơn vẫn bị giữ lâu, giải ngân Seller bị chậm | Rút xuống dưới 24h (24-72h cho Shop uy tín) + auto-reminder | OMS / Policy Team |
| OP-07 | Order Processing | COD chiếm ~40-45% đơn hàng (giảm dần từ ~55-60% năm 2022), cash-intensive, khó đối soát | PV + BM | Cao | Rủi ro cash handling, chi phí collection cao | Khuyến khích chuyển online payment (incentive) | Payment / Finance Team |

### 1.4. Quy trình 04 — Hoàn trả & Refund (Return & Refund)

| ID | Quy trình | Issue / Mô tả | Phát hiện từ | Mức độ | Ảnh hưởng | Giải pháp TO-BE liên quan | Người phụ trách |
|----|-----------|---------------|-------------|--------|-----------|--------------------------|-----------------|
| RR-01 | Return/Refund | Thời gian hoàn refund 5-7 ngày (benchmark 2-3 ngày) | PV + BM | Cao | Buyer CSAT 3.6/5, repeat purchase giảm 15-20% | Tiered refund: instant cho low-risk <200k | Finance / Payment Team |
| RR-02 | Return/Refund | Warehouse inspection thủ công 3-7 ngày (bottleneck lớn nhất) | PV + PT | Cao | Chiếm ~50% tổng cycle time refund; chi phí warehouse 30,000 VND/đơn (CS labor 52,000 VND/đơn, tổng ~109,000 VND/đơn) | AI image analysis inspection (~30 phút) | Quality Inspection Team |
| RR-03 | Return/Refund | CS review evidence thủ công 24-48h cho mọi case | PV + PT | Cao | CS quá tải, chi phí 15,000 VND/case | AI evidence verification, CS chỉ xử lý exception | CS / Return Ops Team |
| RR-04 | Return/Refund | Over-approval: case <200k vẫn qua nhiều lớp duyệt | PT | TB | Lãng phí thời gian CS cho case giá trị thấp | Auto-approve return-less cho low-risk | Return Operations Team |
| RR-05 | Return/Refund | Chi phí reverse logistics cao (52,000 VND/đơn trả — CS labor; tổng ~109,000 VND/đơn trả) | PT + BM | TB | Tổng chi phí lớn hàng tháng cho return | Return-less refund cho hàng giá trị thấp | Finance / Logistics |
| RR-06 | Return/Refund | Refund phụ thuộc phương thức thanh toán (COD 1-3 ngày, card 5-15 ngày) | PT + BM | TB | Buyer nhận tiền chậm, đặc biệt với card | Định hướng Lazada Wallet (instant-24h) làm kênh ưu tiên | Payment Team |
| RR-07 | Return/Refund | Pickup trả hàng thủ công (4-24h chờ), KH phải ở nhà | PV + PT | TB | Khách bỏ lỡ pickup, vòng lặp lịch lại | Smart scheduling + drop-off point + QR code | Logistics / Return Ops |

### 1.5. Quy trình 05 — Chăm sóc Khách hàng (Customer Service)

| ID | Quy trình | Issue / Mô tả | Phát hiện từ | Mức độ | Ảnh hưởng | Giải pháp TO-BE liên quan | Người phụ trách |
|----|-----------|---------------|-------------|--------|-----------|--------------------------|-----------------|
| CS-01 | Customer Service | Thời gian chờ queue Tier 1 trung bình 8 phút (peak 30 phút) | PV + PT | Cao | CSAT 3.2/5, khách bỏ cuộc, escalation tăng | AI intent + sentiment routing, chatbot handle 50-60% | CS Ops Team |
| CS-02 | Customer Service | Khách phải mô tả lại issue khi chuyển từ chatbot sang agent | PV | TB | Waste Move, tăng AHT, giảm trải nghiệm | Auto-context fetch từ order/payment DB | Platform / CS Ops |
| CS-03 | Customer Service | Chatbot resolution rate thấp (~20%, benchmark 30-40% ngành VN) | PT + BM | Cao | Volume dồn về agent, chi phí tăng | AI intent classification + KB nâng cấp (resolve 20% → mục tiêu 45%) | Algorithm/AI Team |
| CS-04 | Customer Service | Staffing cố định, không theo real-time demand | PV + PT | TB | Over-staff off-peak, under-staff peak hours | Demand forecasting ML + flexible scheduling | CS Ops / HR |
| CS-05 | Customer Service | Tier 1 đọc lại transcript dài khi nhận case từ chatbot | PV + PT | Thấp | Mất 2-3 phút/case, tích lũy lớn ở scale | Auto-summary + context passing tự động | Platform / AI Team |
| CS-06 | Customer Service | SLA ticket cứng, không phân biệt mức độ khẩn cấp | PT + BM | TB | Case khẩn cấp xử lý chậm như case thường | SLA động theo sentiment/urgency + cảnh báo Supervisor | CS Ops Team |

### 1.6. Quy trình 06 — Marketing & Khuyến mãi (Marketing)

| ID | Quy trình | Issue / Mô tả | Phát hiện từ | Mức độ | Ảnh hưởng | Giải pháp TO-BE liên quan | Người phụ trách |
|----|-----------|---------------|-------------|--------|-----------|--------------------------|-----------------|
| MK-01 | Marketing | Time-to-market campaign chậm (3 tuần, benchmark 2 tuần) | PV + BM | Cao | Mất cơ hội thị trường, đối thủ launch trước | AI budget alloc + risk-tiered approval | Marketing Team |
| MK-02 | Marketing | Budget approval multi-layer 2-5 ngày cho mọi campaign | PV + PT | Cao | Bottleneck lớn nhất, delay toàn bộ pipeline | Risk-tiered: small <100M auto, large -> director | Finance / Marketing |
| MK-03 | Marketing | Seller recruitment thủ công (manual outreach), participation thấp | PV + PT | Cao | Campaign thiếu sản phẩm, GMV không đạt target | AI personalized invitation + auto-invite | Seller Operations |
| MK-04 | Marketing | Post-campaign reporting thủ công (2-3 ngày), insight chậm | PV + PT | TB | Insight chậm, không actionable kịp thời | Auto-report + ML insight generation | Marketing / Data Team |
| MK-05 | Marketing | Campaign config copy-paste thủ công, lỗi config ~9% | PT | TB | Launch sai voucher/price, ảnh hưởng buyer + seller | Template library + auto-config | Platform / Marketing |
| MK-06 | Marketing | Tuân thủ pháp lý khuyến mãi (Nghị định 81) kiểm tra thủ công | PV + PT | TB | Rủi ro phạt pháp lý, chậm launch | Auto-compliance check tích hợp quy định | Legal Team |

### 1.7. Quy trình 07 — Quản lý Nhân sự & Đào tạo (HR & Training)

| ID | Quy trình | Issue / Mô tả | Phát hiện từ | Mức độ | Ảnh hưởng | Giải pháp TO-BE liên quan | Người phụ trách |
|----|-----------|---------------|-------------|--------|-----------|--------------------------|-----------------|
| HR-01 | HR & Training | Content creation thủ công 2-4 tuần, mỗi khóa học tạo từ đầu | PV + PT | Cao | Chiếm 37.5% chi phí lãng phí (~600 triệu VND/quý); publish khóa mới 4-6 tuần | AI-generated content + template chuẩn hóa | L&D / Content Team |
| HR-02 | HR & Training | Finance approval 5-10 ngày, workflow tuần tự nhiều cấp | PV + PT | Cao | Bottleneck lớn nhất; nhân viên chờ không productive | Auto-approval threshold + parallel workflow | Finance / HR |
| HR-03 | HR & Training | Tỷ lệ hoàn thành đào tạo chỉ ~60% (benchmark 80-85%) | PV + BM | Cao | Re-training cost + underperformance; thiếu nhân lực chất lượng | Gamification + AI personalized learning | HR / L&D Team |
| HR-04 | HR & Training | Compliance audit thủ công hàng tuần, tốn nhân lực | PV + PT | TB | Vi phạm phát hiện muộn; 150 triệu VND/quý | Real-time compliance monitoring | Compliance / HR |
| HR-05 | HR & Training | Xử lý vi phạm chính sách đào tạo 3-7 ngày, phụ thuộc con người | PT + BM | TB | Vi phạm chưa xử lý kịp → rủi ro chính sách | Auto-escalation policy + workflow tự động | HR / Compliance |
| HR-06 | HR & Training | Thi đánh giá thủ công, không có auto-proctoring | PT | TB | Tốn nhân lực + rủi ro gian lận (pass lần đầu chỉ 70%) | AI auto-proctoring | L&D / IT Team |
| HR-07 | HR & Training | Thiếu gamification + KPI đào tạo real-time | PT + BM | TB | Không đo được ROI training; động lực học thấp | Dashboard real-time + AI skill gap analysis | HR / Data Team |

### 1.8. Quy trình 08 — Thanh toán & Đối soát (Payment & Settlement)

| ID | Quy trình | Issue / Mô tả | Phát hiện từ | Mức độ | Ảnh hưởng | Giải pháp TO-BE liên quan | Người phụ trách |
|----|-----------|---------------|-------------|--------|-----------|--------------------------|-----------------|
| PS-01 | Payment & Settlement | COD reconciliation chênh lệch 2-3% (~4,250-6,375 giao dịch/ngày) | PV + PT | Cao | 90-135 tỷ VND/tháng; shipper gian lận COD | Auto-reconciliation ML + COD digital verification (GPS + signature) | Finance / Logistics |
| PS-02 | Payment & Settlement | Settlement cycle chậm L+2 (online) / L+3 (COD) | PV + BM | Cao | Seller cash flow bị giữ; churn risk | Instant settlement (risk-based) cho trusted seller | Finance / Payment Team |
| PS-03 | Payment & Settlement | Payment gateway timeout + single gateway dependency | PT + BM | Cao | Payment success chỉ 94% (benchmark 98%); mất doanh thu | Multi-gateway failover + circuit breaker | Engineering / Payment GW |
| PS-04 | Payment & Settlement | Fraud detection 0.3% nhưng false positive cao, model chưa VN-specific | PT + BM | TB | Chặn giao dịch hợp lệ; 30 tỷ VND/tháng | AI risk scoring real-time + VN-specific patterns | Risk/Fraud / AI Team |
| PS-05 | Payment & Settlement | Withdrawal processing 24-48h qua ngân hàng | PV + BM | TB | Seller chờ tiền; 17 tỷ VND/tháng | Real-time banking API + ví Lazada instant | Finance / Banking Team |
| PS-06 | Payment & Settlement | COD reconciliation batch end-of-day, matching thủ công 2-4h/ngày | PT | TB | Không real-time, dễ sai sót | Auto-matching algorithm parallel | Finance / Data Team |
| PS-07 | Payment & Settlement | Double charge / duplicate transactions ~50/ngày | PT | Thấp | Khiếu nại buyer + chi phí xử lý | Idempotency key trong payment API | Engineering / Payment GW |

### 1.9. Quy trình 09 — Logistics & Giao nhận (Logistics & Delivery)

| ID | Quy trình | Issue / Mô tả | Phát hiện từ | Mức độ | Ảnh hưởng | Giải pháp TO-BE liên quan | Người phụ trách |
|----|-----------|---------------|-------------|--------|-----------|--------------------------|-----------------|
| LG-01 | Logistics & Delivery | Giao lại nhiều lần (15% đơn cần retry, giao lại tối đa 3 lần) | PV + PT | Cao | 85 tỷ VND/tháng; first-attempt success chỉ 75-80% | Slot hẹn giờ + predictive ETA ML + shipper gọi trước 15 phút | Logistics / LEX-3PL |
| LG-02 | Logistics & Delivery | Return/hoàn về cao 8-12% (địa chỉ sai, buyer vắng nhà) | PV + BM | Cao | 90 tỷ VND/tháng; chi phí reverse logistics | Address validation realtime + giảm retry ≤2 lần | Logistics / Platform |
| LG-03 | Logistics & Delivery | Sort Hub chậm 2-6 giờ, capacity utilization chỉ 75% | PT | TB | 55 tỷ VND/tháng; bottleneck giờ cao điểm | AI sorting + automated Hub + predictive capacity | Warehouse Ops |
| LG-04 | Logistics & Delivery | Tracking không realtime (90% vs benchmark 98%) | PV + PT | TB | CS handle tracking queries + mất niềm tin buyer | GPS API chuẩn cho LEX/3PL + live tracking | Platform / 3PL Integration |
| LG-05 | Logistics & Delivery | Chi phí last-mile province cao (40,000 VND vs benchmark 30-35k) | PT + BM | TB | 83,5 tỷ VND/tháng (last-mile + transit delay — Pareto dòng 5, 09-logistics L273); route chưa tối ưu | AI route optimization + drone pilot remote area | Logistics / Ops |
| LG-06 | Logistics & Delivery | ETA hiển thị không chính xác (dựa distance, chưa ML) | PV + PT | TB | Buyer không biết giờ giao chính xác → miss pickup | Predictive ETA ML (traffic + weather) | Data / AI Team |
| LG-07 | Logistics & Delivery | Địa chỉ sai/không đầy đủ từ checkout | PV + PT | TB | 20-25% giao thất bại lần đầu; hàng hoàn về | Address auto-fill + validation tại checkout | Platform / Checkout Team |

### 1.10. Quy trình 10 — Vận hành Nền tảng Công nghệ (IT Operations)

| ID | Quy trình | Issue / Mô tả | Phát hiện từ | Mức độ | Ảnh hưởng | Giải pháp TO-BE liên quan | Người phụ trách |
|----|-----------|---------------|-------------|--------|-----------|--------------------------|-----------------|
| IT-01 | IT Operations | Bug fix loop 2-5 ngày/release (70% features có bug) | PV + PT | Cao | 1,170 triệu VND/tháng (30% labor rework) | Shift-left testing + AI code review + coverage gate | Dev / QA Team |
| IT-02 | IT Operations | Deployment failure 15% + rollback 30-60 phút | PT + BM | Cao | 780 triệu VND/tháng; downtime | Canary deployment + automated quality gates + IaC | DevOps / Platform |
| IT-03 | IT Operations | CI/CD pipeline 45 phút, chạy tuần tự không caching | PT | Cao | Engineer idle 585 triệu VND/tháng | Parallel testing + build caching + optimize pipeline | DevOps / CI-CD Team |
| IT-04 | IT Operations | Security vulnerability response 7-14 ngày | PT + BM | TB | Rủi ro compliance + remediation cost cao | Shift-left SAST/SCA trong CI | Security Team |
| IT-05 | IT Operations | Release cycle 4-6 tuần (story → prod) quá dài | PV + BM | TB | Time-to-market chậm; mất cơ hội | Canary + tự động hóa gates | DevOps / Product |
| IT-06 | IT Operations | Cloud infrastructure over-provisioned ~25% waste | PT | TB | 312 triệu VND/tháng unused resources | Auto-scaling (K8s HPA) + FinOps | DevOps / Cloud |
| IT-07 | IT Operations | MTTR 2-4 giờ, alerts false positive cao | PT + BM | TB | Downtime 195 triệu VND/tháng | AIOps predictive monitoring + self-healing pods | SRE / DevOps |
| IT-08 | IT Operations | Code coverage chỉ ~70%, test environment khác production | PT | TB | Bug slip through; deployment failure nguồn gốc | Enforced coverage gate + environment parity (GitOps) | QA / DevOps |

---

## 2. Tổng hợp theo mức độ

| Mức độ | Số lượng | Tỷ lệ | Danh sách ID |
|--------|----------|-------|-------------|
| **Cao** | 27 | 42% | SM-01, SM-03, SM-05, DM-01, DM-02, OP-01, OP-02, OP-07, RR-01, RR-02, RR-03, CS-01, CS-03, MK-01, MK-02, MK-03, HR-01, HR-02, HR-03, PS-01, PS-02, PS-03, LG-01, LG-02, IT-01, IT-02, IT-03 |
| **Trung bình** | 34 | 52% | SM-02, SM-04, DM-03, DM-04, OP-03, OP-04, OP-06, RR-04, RR-05, RR-06, RR-07, CS-02, CS-04, CS-06, MK-04, MK-05, MK-06, HR-04, HR-05, HR-06, HR-07, PS-04, PS-05, PS-06, LG-03, LG-04, LG-05, LG-06, LG-07, IT-04, IT-05, IT-06, IT-07, IT-08 |
| **Thấp** | 4 | 6% | DM-05, OP-05, CS-05, PS-07 |
| **Tổng** | **65** | **100%** | |

---

## 3. Tổng hợp theo nguồn phát hiện

| Nguồn phát hiện | Số lượng | Tỷ lệ | Ghi chú |
|-----------------|----------|-------|---------|
| Phỏng vấn (PV) | 39 | 60% | Phát hiện từ phỏng vấn Seller, Buyer, CS agent, Marketing team, HR, Shipper/LEX, Dev/DevOps |
| Phân tích BPMN (PT) | 55 | 85% | Phát hiện từ VA/NVA/Waste analysis + cấu trúc mô hình |
| Benchmark ngành (BM) | 25 | 38% | So sánh với Shopee, TikTok Shop, industry standard |

> **Lưu ý:** Một issue có thể được phát hiện từ nhiều nguồn, do đó tổng % > 100%.

---

## 4. Ma trận ưu tiên (Impact x Urgency)

| | Urgency Cao | Urgency TB | Urgency Thấp |
|---|------------|-----------|-------------|
| **Impact Cao** | OP-01, OP-02, RR-01, RR-02, DM-01, CS-01, MK-01, HR-01, HR-02, PS-01, LG-01, LG-02, IT-01, IT-02 | SM-01, SM-03, SM-05, CS-03, MK-02, MK-03, HR-03, PS-02, PS-03, IT-03 | OP-07 |
| **Impact TB** | RR-03, DM-02, MK-04, MK-06, PS-04, LG-04, IT-04 | SM-02, SM-04, OP-03, OP-04, OP-06, DM-03, DM-04, RR-04, RR-05, RR-06, RR-07, CS-02, CS-04, CS-06, MK-05, HR-04, HR-05, HR-06, HR-07, PS-05, PS-06, LG-03, LG-05, LG-06, LG-07, IT-05, IT-06, IT-07, IT-08 | — |
| **Impact Thấp** | — | DM-05, CS-05, PS-07 | OP-05 |

---

## 5. Tham chiếu

| Tài liệu | Link |
|----------|------|
| Annotation VA/BVA/NVA 181 tasks | `docs/analysis/bpmn-va-annotation.md` |
| Fishbone diagrams (3 vấn đề) | `docs/analysis/fishbone-diagrams.md` |
| Phân tích định lượng quy trình 01-06 | `docs/analysis/01-seller-management.md` … `docs/analysis/06-marketing.md` |
| Phân tích định lượng quy trình 07-10 | `docs/analysis/07-hr-training.md` … `docs/analysis/10-it-platform.md` |
| BPMN AS-IS (nguồn tên task) | `processes/0X-*.bpmn` |
| BPMN TO-BE (giải pháp) | `processes-to-be/0X-*.bpmn` |

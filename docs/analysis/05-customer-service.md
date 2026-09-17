# 3.5. Quy trình Chăm sóc Khách hàng (Customer Service)

## 3.5.1. Mô tả quy trình

**Phạm vi:** Bắt đầu từ khi Customer tiếp nhận yêu cầu hỗ trợ → AI NLP phân loại → Chatbot tự động giải quyết / chuyển CS Tier 1 → Xác minh danh tính → Tier 1 hỗ trợ → Escalate Tier 2 nếu cần → Xác nhận hoàn tất → CSAT → Ghi nhận phiên.

**Các tác nhân tham gia:**
- **Customer:** Khách hàng — mô tả vấn đề, cung cấp chứng từ, xác nhận hoàn tất, chấm CSAT
- **Chatbot/AI:** Phân loại ý định NLP, tự động giải đáp (Lazada Assistant), kiểm tra SLA
- **CS Tier 1:** Tư vấn viên — xác minh danh tính, tiếp nhận, đưa giải pháp
- **CS Tier 2:** Chuyên viên — thẩm định chuyên sâu, xử lý dứt điểm
- **System:** Trích xuất thông tin đơn/tài khoản, lấy lịch sử tương tác, ghi nhật ký phiên, gửi nhắc nhở

**Kết quả có thể xảy ra:**
- Phiên hỗ trợ kết thúc thành công — vấn đề được giải quyết, CSAT thu được
- Ticket quá hạn SLA xử lý — yêu cầu không được xử lý kịp trong thời hạn
- Xác minh danh tính thất bại — không xác minh được khách hàng

### SiPOC

| SiPOC | Chi tiết |
|-------|----------|
| **Supplier** | Customer (vấn đề, chứng từ, phản hồi), Chatbot/AI (tri thức tự phục vụ), System (dữ liệu đơn/tài khoản) |
| **Input** | Yêu cầu hỗ trợ, ý định, mức độ khẩn cấp, SLA ticket |
| **Process** | Mô tả → NLP phân loại → SLA check → Chatbot / Tier 1 → Xác minh → Tier 1 giải quyết → Tier 2 (nếu cần) → Xác nhận → CSAT → Log session |
| **Output** | Phiên hỗ trợ thành công (kèm CSAT), Ticket quá hạn SLA, Xác minh thất bại |
| **Customer** | Customer (vấn đề được giải quyết), Lazada (dữ liệu chất lượng dịch vụ) |

## 3.5.2. Mô hình BPMN

*(File: `processes/05-customer-service.bpmn`)*

**Thống kê mô hình:**
- Số lanes: 5 (Customer, Chatbot/AI, CS Tier 1, CS Tier 2, System)
- Số activities: 18 (11 userTask + 7 serviceTask)
- Số gateways: 11 (XOR)
- End events: 3
- Độ phức tạp: Medium-High

## 3.5.3. Phân tích định tính

### A. Value-Added Analysis

| STT | Hoạt động (tên từ BPMN) | VA | BVA | NVA | Giải thích | Đề xuất TO-BE |
|-----|--------------------------|----|-----|-----|------------|---------------|
| 1 | Mô tả chi tiết vấn đề cần hỗ trợ | ✓ |  |  | KH trình bày nhu cầu — đầu vào | Guided category menu |
| 2 | Cung cấp thêm thông tin chứng từ | ✓ |  |  | Đủ context để giải quyết | Auto-fill từ order/user context |
| 3 | Khách hàng bấm xác nhận hoàn tất hỗ trợ | ✓ |  |  | Verify hài lòng — chốt ticket | One-tap confirm |
| 4 | Khách hàng chấm điểm khảo sát CSAT | ✓ |  |  | Đo lường trải nghiệm — đầu vào cải tiến | 2-question CSAT/CES |
| 5 | Chờ phản hồi từ tư vấn viên |  | ✓ |  | Chờ agent (cần thiết nhưng Hold 5-30 phút) | **Predictive staffing** giảm queue |
| 6 | Xác minh danh tính khách hàng |  | ✓ |  | Bảo mật — chống mạo danh | SSO/OTP nhanh |
| 7 | Tư vấn viên Tier 1 tiếp nhận & hỗ trợ | ✓ |  |  | Core service — giải quyết trực tiếp | Copilot gợi ý + auto-context |
| 8 | Tư vấn viên Tier 1 đưa giải pháp xử lý | ✓ |  |  | Kết quả giải quyết trực tiếp | Solution KB integration |
| 9 | Chuyên viên Tier 2 thẩm định chuyên sâu | ✓ |  |  | Case phức tạp cần chuyên môn | Clear handoff summary |
| 10 | Chuyên viên Tier 2 xử lý dứt điểm | ✓ |  |  | Phán quyết chuyên sâu | Checklist + SLA |
| 11 | Khảo sát đánh giá chất lượng (QA Follow-up) |  | ✓ |  | Đo chất lượng — kiểm soát | Auto-survey thay call thủ công |
| 12 | AI NLP phân loại ý định & mức độ khẩn cấp |  | ✓ |  | Routing đúng luồng — hỗ trợ chatbot | Nâng cấp NLP accuracy |
| 13 | Chatbot (Lazada Assistant) tự động giải đáp | ✓ |  |  | Giải quyết tức thì — giá trị cốt lõi hiện đại | Mở rộng knowledge base (tăng 40-50% auto-resolve) |
| 14 | Hệ thống kiểm tra SLA xử lý ticket |  | ✓ |  | Kiểm soát cam kết thời gian | Auto-escalate khi sắp quá hạn |
| 15 | Lấy lịch sử tương tác (auto) |  | ✓ |  | Context cho agent — giảm lặp | Auto-attach (đã auto) |
| 16 | Hệ thống trích xuất thông tin đơn & tài khoản |  | ✓ |  | Tự động lấy context → bỏ hỏi lại KH | Auto-context fetch (chống waste Move) |
| 17 | Ghi nhận nhật ký phiên & điểm CSAT |  | ✓ |  | Ghi nhận phục vụ phân tích | Giữ nguyên (auto) |
| 18 | Gửi nhắc nhở phản hồi cho khách hàng | ✓ |  |  | Nhắc KH theo dõi — giảm ticket kép | Auto-reminder, tránh spam |

**Tỷ lệ VA/BVA/NVA:**
- VA: 10/18 (56%)
- BVA: 8/18 (44%)
- NVA: 0/18 (0%)

→ **Nhận xét:** NVA 0% — không có hoạt động lãng phí thuần. BVA cao (44%) là cần thiết cho kiểm soát chất lượng và auditing. Chatbot tự phục vụ là cơ hội tăng trưởng lớn.

### B. Waste Analysis

| STT | Hoạt động | Move | Hold | Overdo | Mô tả | Thời gian chờ | Giải pháp |
|-----|-----------|------|------|--------|-------|---------------|-----------|
| 1 | Chờ phản hồi từ tư vấn viên | | ✓ | | Khách chờ, ticket treo trong queue | 10 phút-4h | Auto-assign + SLA alert |
| 2 | Xác minh danh tính khách hàng | ✓ | | | Hỏi nhiều câu hỏi bảo mật tốn thời gian | 3-10 phút | OTP 1 bước thay vì hỏi lịch sử đơn |
| 3 | Escalation lên Tier 2 khi chưa cần | ✓ | | | Tier 1 thiếu quyền hạn → escal không cần thiết | 30 phút-1 ngày | Mở rộng quyền hạn Tier 1 + clear criteria |
| 4 | Gửi nhắc nhở phản hồi cho khách hàng | | ✓ | | Ticket chờ khách phản hồi bị treo | 24-48h | Auto-close sau 24h không phản hồi |
| 5 | Khảo sát đánh giá chất lượng (QA Follow-up) | ✓ | | | QA review manual khi CSAT thấp | 1-2 ngày | AI phân tích sentiment tự động |

**Tổng lãng phí:** 5 hoạt động
- Move: 3 (60%)
- Hold: 2 (40%)
- Overdo: 0 (0%)

### C. Root Cause Analysis — Fishbone (Ishikawa) 5 Cấp

```
Vấn đề: CSAT thấp 3.2/5 và chatbot resolve rate thấp 20%

Level 1 — Nguyên nhân lớn:
├── Con người (Man)
│   ├── Level 2: CS Tier 1 thiếu quyền hạn xử lý
│   │   ├── Level 3: Phải escalate nhiều cases đơn giản
│   │   │   ├── Level 4: Quyền hoàn tiền/reship giới hạn ở Tier 2
│   │   │   │   └── Level 5: Risk control quá tập trung ở cấp cao
│   │   └── Level 3: CS xử lý thủ công nhiều bước
│   │       ├── Level 4: CRM/helpdesk chưa tích hợp giải pháp mẫu
│   │       │   └── Level 5: Thiếu knowledge base + macro tích hợp
├── Quy trình (Process)
│   ├── Level 2: Khách phải chờ phản hồi
│   │   ├── Level 3: Ticket queue không ưu tiên theo urgency
│   │   │   ├── Level 4: Routing chỉ theo intent, không theo SLA
│   │   │   │   └── Level 5: Thiếu SLA-based priority queue
│   │   └── Level 3: Nhiều vòng hỏi lại chứng từ
│   │       ├── Level 4: Không có structured evidence collection
│   │       │   └── Level 5: Chatbot không thu thập được context trước
├── Công nghệ (Technology)
│   ├── Level 2: Chatbot resolve rate thấp
│   │   ├── Level 3: Kịch bản tự phục vụ hạn chế
│   │   │   ├── Level 4: Knowledge base chưa đầy đủ/liên tục cập nhật
│   │   │   │   └── Level 5: KB maintenance thiếu ownership
│   │   └── Level 3: NLP không hiểu tiếng Việt tốt
│   │       ├── Level 4: Training data tiếng Việt ít
│   │       │   └── Level 5: VN-specific NLU chưa được đầu tư
└── Đo lường (Measurement)
    ├── Level 2: Không có real-time CSAT monitoring
    │   ├── Level 3: QA chỉ review khi CSAT thấp (reactive)
    │   │   ├── Level 4: Không có proactive quality sampling
    │   │   │   └── Level 5: QA process thủ công, định kỳ
    │   └── Level 3: Không có loop feedback từ CSAT vào training
    │       ├── Level 4: Training curriculum không cập nhật theo fail cases
    │       │   └── Level 5: L&D và Operations tách rời
```

### 5-Why Analysis

**Vấn đề:** CSAT thấp 3.2/5 (benchmark 4.2/5)

| Level | Câu hỏi | Câu trả lời |
|-------|---------|-------------|
| Why 1 | Tại sao CSAT thấp? | Khách phải chờ lâu, phải escalate, vấn đề không giải quyết ngay |
| Why 2 | Tại sao phải chờ và escalate? | Tier 1 thiếu quyền hạn, queue không ưu tiên theo SLA |
| Why 3 | Tại sao Tier 1 thiếu quyền hạn? | Risk control tập trung ở Tier 2 |
| Why 4 | Tại sao risk control tập trung? | Sợ nhân viên lạm dụng quyền hoàn tiền |
| Why 5 | Tại sao sợ lạm dụng? | Chưa có fraud detection + audit trail mạnh để cho phép phân quyền |

**Root Cause:** Phân quyền xử lý quá tập trung + chatbot tự phục vụ yếu + thiếu SLA-based priority queue.

## 3.5.4. Phân tích định lượng

### A. Thời gian

| STT | Hoạt động | Min | Max | Avg | Ghi chú |
|-----|-----------|-----|-----|-----|---------|
| 1 | Mô tả chi tiết vấn đề cần hỗ trợ | 1 phút | 10 phút | 3 phút | Customer |
| 2 | AI NLP phân loại ý định & mức độ khẩn cấp | 2 giây | 10 giây | 5 giây | Automated |
| 3 | Hệ thống kiểm tra SLA xử lý ticket | 2 giây | 10 giây | 5 giây | Automated |
| 4 | Hệ thống trích xuất thông tin đơn & tài khoản | 3 giây | 15 giây | 5 giây | Automated |
| 5 | Chatbot (Lazada Assistant) tự động giải đáp | 30 giây | 5 phút | 2 phút | 20% resolved |
| 6 | Xác minh danh tính khách hàng | 3 phút | 10 phút | 5 phút | Hỏi nhiều câu |
| 7 | Lấy lịch sử tương tác (auto) | 2 giây | 10 giây | 5 giây | Automated |
| 8 | Tư vấn viên Tier 1 tiếp nhận & hỗ trợ | 5 phút | 30 phút | 15 phút | Per session |
| 9 | Tư vấn viên Tier 1 đưa giải pháp xử lý | 5 phút | 20 phút | 10 phút | Per session |
| 10 | Cung cấp thêm thông tin chứng từ | 2 phút | 15 phút | 5 phút | 30% sessions |
| 11 | Chờ phản hồi từ tư vấn viên | 10 phút | 4 giờ | 1 giờ | Queue |
| 12 | Gửi nhắc nhở phản hồi cho khách hàng | 1 phút | 5 phút | 2 phút | Automated |
| 13 | Chuyên viên Tier 2 thẩm định chuyên sâu | 30 phút | 4 giờ | 1.5 giờ | 25% escalated |
| 14 | Chuyên viên Tier 2 xử lý dứt điểm | 15 phút | 2 giờ | 45 phút | 25% escalated |
| 15 | Khách hàng bấm xác nhận hoàn tất hỗ trợ | 1 phút | 5 phút | 2 phút | Customer |
| 16 | Khách hàng chấm điểm khảo sát CSAT | 1 phút | 3 phút | 1 phút | Customer |
| 17 | Khảo sát đánh giá chất lượng (QA Follow-up) | 15 phút | 1 giờ | 30 phút | 15% CSAT thấp |
| 18 | Ghi nhận nhật ký phiên & điểm CSAT | 2 giây | 10 giây | 5 giây | Automated |

### B. Phân tích Cycle Time Probability-Weighted

| Hoạt động | Thời gian (phút) | Xác suất | Thời gian kỳ vọng (phút) | Ghi chú |
|-----------|-------------------|----------|--------------------------|---------|
| Mô tả chi tiết vấn đề cần hỗ trợ | 3 | 100% | 3.0 | Bắt buộc |
| AI NLP phân loại ý định & mức độ khẩn cấp | 0.08 | 100% | 0.08 | Tức thì |
| Hệ thống kiểm tra SLA xử lý ticket | 0.08 | 100% | 0.08 | Tức thì |
| Hệ thống trích xuất thông tin đơn & tài khoản | 0.08 | 100% | 0.08 | Tức thì |
| Chatbot (Lazada Assistant) tự động giải đáp | 2 | 60% | 1.2 | 60% có kịch bản |
| Xác minh danh tính khách hàng | 5 | 80% | 4.0 | 80% đi qua Tier 1 |
| Lấy lịch sử tương tác (auto) | 0.08 | 80% | 0.06 | 80% Tier 1 |
| Tư vấn viên Tier 1 tiếp nhận & hỗ trợ | 15 | 80% | 12.0 | 80% Tier 1 |
| Tư vấn viên Tier 1 đưa giải pháp xử lý | 10 | 80% | 8.0 | 80% Tier 1 |
| Cung cấp thêm thông tin chứng từ | 5 | 24% | 1.2 | 30% × 80% |
| Chờ phản hồi từ tư vấn viên | 60 | 24% | 14.4 | 30% × 80% cần chờ |
| Gửi nhắc nhở phản hồi cho khách hàng | 2 | 12% | 0.24 | 50% × 24% |
| Chuyên viên Tier 2 thẩm định chuyên sâu | 90 | 20% | 18.0 | 25% escalated × 80% |
| Chuyên viên Tier 2 xử lý dứt điểm | 45 | 20% | 9.0 | 25% escalated × 80% |
| Khách hàng bấm xác nhận hoàn tất hỗ trợ | 2 | 100% | 2.0 | Bắt buộc |
| Khách hàng chấm điểm khảo sát CSAT | 1 | 100% | 1.0 | Bắt buộc |
| Khảo sát đánh giá chất lượng (QA Follow-up) | 30 | 15% | 4.5 | 15% CSAT thấp |
| Ghi nhận nhật ký phiên & điểm CSAT | 0.08 | 100% | 0.08 | Tức thì |

**Tổng Cycle Time kỳ vọng = 79 phút ≈ 1.3 giờ**
*(Chatbot resolved: ~8 phút; Tier 1 resolved: ~50 phút; Tier 2 escalated: ~3.2 giờ)*

### C. Chi phí (per contact)

| STT | Thành phần | Chi phí (VND) | Ghi chú |
|-----|-----------|---------------|---------|
| 1 | CS Tier 1 agent time | 20,833 | 25 phút × 50.000 VND/h (25/60 × 50.000 ≈ 20.833) |
| 2 | CS Tier 2 agent time (20% escalated) | 27,000 | 20% × 2.25h × 60,000 VND/h |
| 3 | Chatbot/AI infrastructure | 500 | NLP + KB |
| 4 | System infrastructure | 500 | CRM, SLA engine |
| 5 | QA follow-up (15% CSAT thấp) | 3,750 | 15% × 30 phút × 50,000 VND/h |
| **TỔNG** | | **52,600 VNĐ** | Per contact (làm tròn từ 52.583) |

**Volume ước tính:** ~2.5 triệu contacts/tháng
**Monthly cost:** ~131,5 tỷ VND/tháng (52.600 VNĐ × ~2,5 triệu contacts/tháng)

### D. Chất lượng (Quality Metrics)

| Metric (Chỉ số) | Hiện tại (AS-IS) | Benchmark (VN e-commerce) | Gap | Mục tiêu TO-BE |
|-----------------|------------------|---------------------------|-----|----------------|
| Thời gian phản hồi lần đầu (First Response Time) | 4-8h | 1-2h | +3-6h | **<30 phút** |
| Tỷ lệ hài lòng CSAT (Customer Satisfaction Score) | 3,2/5 | 4,0/5 | -0,8 | **4,0/5** |
| Tỷ lệ giải quyết lần đầu (First-Contact Resolution) | 55% | 70-75% | -15-20% | **80-85%** |
| Thời gian xử lý/ticket (Avg Handle Time) | 25 phút | 15 phút | +10 phút | **8 phút** |
| Chi phí/ticket (Cost per Ticket) | 50,000 VND | 30,000 VND | +20,000 VND | **15,000 VND** |
| Tỷ lệ ticket tự động Bot (Bot Resolution Rate) | 10% | 30-40% | -20-30% | **60-70%** |
| Tỷ lệ agent utilization (Agent Utilization Rate) | 65% | 80% | -15% | **90%** |
| SLA compliance (Tỷ lệ tuân thủ SLA) | 85% | 95% | -10% | **98%** |
| Tỷ lệ escalate Tier 2 (Escalation Rate) | 25% | 10-12% | +13-15% | **5-8%** |
| Tỷ lệ ticket treo (Stale Ticket Rate) | 15% | 3-5% | +10-12% | **<2%** |

> **Ghi chú:** Các số liệu benchmark dựa trên khảo sát industry VN e-commerce 2025-2026. Mục tiêu TO-BE dựa trên mô hình cải tiến AI/automation. Chi phí per contact làm tròn 52.600 VNĐ (tương đương ~52.000 trong Bảng 3.9/đối soát report).

## 3.5.5. Phân tích Pareto

### Bảng Vấn đề — Giả thuyết — Chi phí ảnh hưởng

| STT | Vấn đề | Giả thuyết | Chi phí ảnh hưởng/tháng (VND) | Tỷ trọng |
|-----|--------|-----------|-------------------------------|----------|
| 1 | Chatbot resolve rate thấp 20% | KB kém + NLP VN yếu | 45,000,000,000 (CS labor thay chatbot) | 34.9% |
| 2 | Escalation Tier 2 quá cao 25% | Tier 1 thiếu quyền hạn | 38,000,000,000 (Tier 2 cost cao hơn) | 29.5% |
| 3 | Khách chờ phản hồi lâu | Queue không ưu tiên theo SLA | 25,000,000,000 (churn + CSAT) | 19.4% |
| 4 | Xác minh danh tính nhiều bước | Friction cao, hỏi nhiều câu | 12,000,000,000 (thời gian + abandon) | 9.3% |
| 5 | QA review manual reactive | Không có proactive quality loop | 9,000,000,000 (QA labor + coaching) | 7.0% |
| **TỔNG** | | | **129,000,000,000** | **100%** |

### Kết luận 80/20

**Top 3 vấn đề (chiếm ~84% chi phí):**
1. Chatbot resolve rate thấp (34.9%) — giải pháp: mở rộng KB + đầu tư NLP VN
2. Escalation Tier 2 cao (29.5%) — giải pháp: phân quyền Tier 1 với audit trail
3. Khách chờ phản hồi lâu (19.4%) — giải pháp: SLA-based priority queue

→ **Giải quyết 3 vấn đề này sẽ giảm ~84% chi phí lãng phí (~108 tỷ VND/tháng).**

> **Lưu ý:** Các mục giảm chi phí riêng lẻ (tổng 129 tỷ) bị chồng lấn — ước tính giảm thực tế ~56 tỷ/tháng (131 tỷ → 75 tỷ).

## 3.5.6. Kết luận và hướng cải tiến TO-BE

### Tóm tắt AS-IS
- Cycle time kỳ vọng: ~1.3 giờ (chatbot ~8 phút, Tier 1 ~50 phút, Tier 2 ~3.2 giờ)
- Chi phí per contact: ~52,600 VNĐ
- Chatbot resolve rate: chỉ 20%
- Escalation rate: 25% (quá cao)

### Hướng cải tiến TO-BE

| STT | Cải tiến | Mục tiêu | Giảm chi phí (tháng) |
|-----|---------|----------|----------------------|
| 1 | Mở rộng knowledge base + đầu tư NLP tiếng Việt | Chatbot resolve: 20% → 45% (report P5: "hỗ trợ tự động 80% câu hỏi" — 80% là tỷ lệ tiếp nhận, 45% là tỷ lệ resolve) | -45 tỷ VND |
| 2 | Phân quyền Tier 1 + audit trail + fraud detection | Escalation: 25% → 12% | -38 tỷ VND |
| 3 | SLA-based priority queue + auto-assign | Response time: 1h → 15 phút | -25 tỷ VND |
| 4 | Xác minh OTP 1 bước thay vì hỏi nhiều câu | Verify: 5 phút → 1 phút | -12 tỷ VND |
| 5 | QA proactive + AI sentiment analysis | Quality loop real-time | -9 tỷ VND |
| **TỔNG (riêng lẻ, chồng lấn)** | | | **-129 tỷ VND/tháng** |

### So sánh AS-IS vs TO-BE

| Metric | AS-IS | TO-BE | Cải thiện |
|--------|-------|-------|-----------|
| CSAT | 3.2/5 | 4.0/5 | +0.8 |
| Chatbot resolve rate | 20% | 45% | +25% |
| First-contact resolution | 55% | 75% | +20% |
| Avg response time | 1 giờ | 15 phút | -75% |
| Escalation rate Tier 2 | 25% | 12% | -52% |
| Chi phí per contact | 52,600 VNĐ | 30,000 VNĐ | -43% |
| Monthly cost | 131 tỷ VND | 75 tỷ VND | -56 tỷ VND (-43%) |

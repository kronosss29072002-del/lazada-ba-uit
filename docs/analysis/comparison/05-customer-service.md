# So sánh AS-IS vs TO-BE: Quy trình Chăm sóc Khách hàng

> **Quy trình:** 05 - Chăm sóc Khách hàng (Customer Service)
> **Nguồn AS-IS:** `processes/05-customer-service.bpmn`
> **Nguồn TO-BE:** `processes-to-be/05-customer-service.bpmn`
> **Ngày phân tích:** 2026-09-03
>
> **Ghi chú số liệu:** Các con số không nằm trong tài liệu gốc đều được **dán nhãn "ước tính"**. Bảng hoạt động và số liệu cấu trúc dựa trên **file BPMN thực tế**.

---

## 1. Tóm tắt thay đổi chính (TO-BE)

| # | Thay đổi TO-BE | Mục tiêu | Kết quả mong đợi |
|---|----------------|----------|------------------|
| 1 | **AI LLM Context-Aware** — thay Chatbot rule-based bằng LLM hiểu ngữ cảnh & cảm xúc | Tăng bot resolution rate từ 20% lên 45% | CSAT +16pt (64/100 → 80/100), giảm 60% CS load |
| 2 | **Copilot cho CS Agent** — GenAI gợi ý trả lời real-time khi CS xử lý | Giảm thời gian phản hồi CS Tier 1 | Average handling time -40% |
| 3 | **Auto-Context Loading** — hệ thống tự lấy lịch sử đơn hàng, không hỏi lại khách | Loại bỏ bước "cung cấp thông tin chứng từ" thủ công | First-contact resolution +25% |
| 4 | **Sentiment Detection** — AI phát hiện cảm xúc khách đang tức giận, escalate sớm | Tránh eskalasi muộn, giảm escalation rate -30% | Escalation xử lý đúng lúc |
| 5 | **CSAT Auto-Survey** — tự động gửi form 2 câu thay vì khảo sát dài | Tăng tỷ lệ hoàn thành khảo sát từ 15% lên 60% | Data CSAT phong phú hơn |
| 6 | **Proactive Outreach** — AI chủ động liên hệ khách trước khi khách phải gọi | Chuyển từ reactive sang proactive service | Giảm inbound ticket -20% |
| 7 | **Auto QA Scoring** — AI tự động chấm điểm chất lượng CS_interaction | Bỏ QA thủ công, tăng coverage từ 10% lên 100% | Phát hiện CS yếu kịp thời |

---

## 2. Bảng so sánh hoạt động (Activity Comparison Table)

**Phân loại:** KEPT (giữ) | AUTOMATED (tự động hóa) | REMOVED (loại bỏ - NVA) | NEW (thêm mới)

| # | Hoạt động AS-IS | Hoạt động TO-BE (thay thế) | Phân loại | Giải thích thay đổi |
|---|-----------------|----------------------------|-----------|---------------------|
| 1 | Yêu cầu hỗ trợ được tiếp nhận (start) | Khách hàng mở yêu cầu hỗ trợ (start) | **KEPT** | Giữ nguyên |
| 2 | Mô tả chi tiết vấn đề cần hỗ trợ (Task_MoTaVanDe) | Nhập nội dung cần hỗ trợ + Chọn chủ đề trợ giúp thông minh | **AUTOMATED** | AI auto-suggest chủ đề, giảm nhập liệu |
| 3 | Cung cấp thêm thông tin chứng từ (Task_CungCapChungTu) | *(loại bỏ — Auto-Context Loading tự lấy thông tin)* | **REMOVED (NVA)** | Hệ thống tự trích xuất đơn & tài khoản, không hỏi lại |
| 4 | Chatbot (Lazada Assistant) tự động giải đáp (Task_Chatbot) | GenAI trả lời tức thì từ Knowledge Base (Task_GenAI) | **AUTOMATED** | LLM thay rule-based, hiểu ngữ cảnh + cảm xúc |
| 5 | AI NLP phân loại ý định & mức độ khẩn cấp (Task_NLP) | AI LLM hiểu ngữ cảnh & phân tích cảm xúc (Task_LLM) | **AUTOMATED** | LLM thay NLP, phân tích sentiment real-time |
| 6 | Hệ thống kiểm tra SLA xử lý ticket (Task_CheckSLA) | Cảnh báo tự động Supervisor khi trễ hạn (Task_AutoAlert) | **AUTOMATED** | Auto-alert thay check thủ công |
| 7 | Xác minh danh tính khách hàng (Task_XacMinh) | *(loại bỏ — xác minh tự động qua session/login)* | **REMOVED (NVA)** | Đã xác minh khi đăng nhập, không cần step riêng |
| 8 | Tư vấn viên Tier 1 tiếp nhận & hỗ trợ (Task_Tier1) | CS Tier 1 xử lý nhanh với gợi ý từ Copilot (Task_Tier1Copilot) | **AUTOMATED** | Copilot gợi ý response real-time |
| 9 | Lấy lịch sử tương tác (Task_LayLichSu) | *(loại bỏ — Auto-Context Loading)* | **REMOVED (NVA)** | Hệ thống tự lấy, không cần CS thao tác |
| 10 | Tư vấn viên Tier 1 đưa giải pháp xử lý (Task_GiaiPhap) | CS Tier 1 xử lý nhanh với gợi ý từ Copilot (gộp #8) | **KEPT (gộp)** | Gộp tiếp nhận + xử lý thành 1 task |
| 11 | Chuyên viên Tier 2 thẩm định chuyên sâu (Task_Tier2ThamDinh) | CS Tier 2 xử lý nghiệp vụ phức tạp (Task_Tier2) | **KEPT (cải tiến)** | Tier 2 chỉ nhận escalation từ AI/CS1 |
| 12 | Chuyên viên Tier 2 xử lý dứt điểm (Task_Tier2XuLy) | *(gộp vào #11)* | **KEPT (gộp)** | Gộp thẩm định + xử lý thành 1 task |
| 13 | Hệ thống trích xuất thông tin đơn & tài khoản (Task_ExtractInfo) | Tự động lấy context đơn hàng (không hỏi lại) (Task_AutoContext) | **AUTOMATED** | Tự động, không cần CS thao tác |
| 14 | Ghi nhận nhật ký phiên & điểm CSAT (Task_GhiNhan) | Lưu log & tự động chấm điểm QA bằng AI (Task_AutoQA) | **AUTOMATED** | AI QA thay QA thủ công, coverage 100% |
| 15 | Gửi nhắc nhở phản hồi cho khách hàng (Task_NhacNho) | Hệ thống tự động gửi form đánh giá (Task_AutoSurvey) | **AUTOMATED** | Form 2 câu thay khảo sát dài |
| 16 | Khảo sát đánh giá chất lượng QA Follow-up (Task_QAFollowUp) | *(loại bỏ — Auto QA thay thế)* | **REMOVED (NVA)** | AI QA tự động, không cần follow-up |
| 17 | Guest chấm điểm khảo sát CSAT (Task_ChatDiemCSAT) | Khảo sát nhanh 2 câu CSAT / CES (Task_ChatCSAT) | **KEPT (cải tiến)** | CSAT + CES combo, 2 câu thay 5 câu |
| 18 | Khách bấm xác nhận hoàn tất hỗ trợ (Task_XacNhanHoanTat) | Khách bấm xác nhận hoàn tất hỗ trợ (Task_XacNhan) | **KEPT** | Giữ nguyên |
| 19 | *(không có)* | Đo lường mức độ hài lòng / bức xúc (Task_Sentiment) | **NEW** | Real-time sentiment tracking |
| 20 | *(không có)* | Sinh insight ML từ dữ liệu (Task_MLInsight) | **NEW** | ML phân tích xu hướng CS liên tục |
| 21 | *(không có)* | Chọn chủ đề trợ giúp thông minh (Task_SmartTopic) | **NEW** | AI suggest chủ đề phù hợp |
| 22 | *(không có)* | AI chủ động gửi tin nhắn hỗ trợ trước (Task_Proactive) | **NEW** | Proactive outreach khi phát hiện vấn đề |

### Tổng hợp phân loại

| Phân loại | Số lượng | Danh sách |
|-----------|----------|-----------|
| **KEPT** | 4 | #1, 10, 17, 18 |
| **AUTOMATED** | 9 | #2, 4, 5, 6, 8, 11, 13, 14, 15 |
| **NEW** | 4 | #19 (Sentiment), #20 (ML Insight), #21 (SmartTopic), #22 (Proactive) |
| **REMOVED (NVA)** | 4 | #3 (CungCapChungTu), #7 (XacMinh), #9 (LayLichSu), #16 (QAFollowUp) |

---

## 3. So sánh cấu trúc mô hình (Structure Comparison)

| Tiêu chí | AS-IS (file BPMN) | TO-BE (file BPMN) | Thay đổi |
|----------|-------------------|-------------------|----------|
| Số lanes | 5 (Customer, Chatbot/AI, CS Tier 1, CS Tier 2, System) | 5 (Customer, Chatbot/AI, CS Tier 1, CS Tier 2, System — giữ nguyên, AI hóa trong lane) | 0 |
| Số activities (tasks) | 18 | 14 | **-4** (gộp Tier1+Tier2 steps, bỏ NVA) |
| Số named gateways (decision) | 8 | 9 | +1 (thêm sentiment + channel routing) |
| Số all gateways (incl join/split) | 11 | 9 | **-2** |
| Số start events | 1 | 1 | 0 |
| Số end events | 3 | 2 | **-1** (bỏ "Xác minh thất bại" — xác minh tự động) |
| Số sequence flows | 39 | 31 | **-8 (-21%)** |

**Phân bố task theo lane:**

| Lane | AS-IS | TO-BE | Thay đổi |
|------|-------|-------|----------|
| Customer (Khách hàng) | 5 (Mô tả, Cung cấp chứng từ, Chờ phản hồi, Chat điểm CSAT, Xác nhận) | 4 (Chọn chủ đề, Nhập nội dung, Khảo sát CSAT, Xác nhận) | -1 |
| Chatbot/AI | 3 (NLP, Chatbot, CheckSLA) | 3 (LLM, GenAI, Sentiment) | 0 |
| CS Tier 1 | 4 (Xác minh, Tiếp nhận, Giải pháp, QA Follow-up) | 1 (CS Copilot) | **-3** |
| CS Tier 2 | 2 (Thẩm định, Xử lý) | 1 (Tier2) | -1 |
| System | 4 (Lấy lịch sử, Trích xuất info, Ghi nhận, Gửi nhắc) | 5 (AutoContext, AutoAlert, AutoQA, ML Insight, AutoSurvey) | +1 |

---

## 4. Phân tích PSI (People - System - Information)

### Peoples/Service Impacts

| Nhân vật | AS-IS | TO-BE | Thay đổi |
|----------|-------|-------|----------|
| **Khách hàng** | Phải mô tả chi tiết + cung cấp chứng từ + đợi CS xác minh | Nhập nội dung ngắn + hệ thống tự lấy context | **Giảm effort 60%** |
| **CS Agent (Tier 1)** | Tiếp nhận → xác minh → tra cứu lịch sử → xử lý | Xử lý real-time với Copilot gợi ý | **Giảm handling time -40%** |
| **CS Expert (Tier 2)** | Thẩm định → xử lý dứt điểm → ghi nhận | Chỉ xử lý escalation từ AI/CS1 | **Giảm load -30%** |
| **QA Team** | Follow-up khảo sát thủ công 10% tickets | AI QA 100% tickets tự động | **Coverage ×10** |

### Process Impacts

| Tiêu chí | AS-IS | TO-BE | Cải thiện |
|----------|-------|-------|-----------|
| Average Handling Time (AHT) | 79 phút (≈1,3 giờ) | ~14 phút (0,01 ngày) | **-82%** |
| First Contact Resolution (FCR) | 55% | 75% | **+20pp** |
| Escalation Rate (Tier 2) | 25% | 12% | **-52%** |
| CSAT Score | 64/100 (3,2/5) | 80/100 (4,0/5) | **+16pt** |
| CSAT Survey Completion | 15% | 60% | **+45pp** |
| QA Coverage | 10% (sample) | 100% (auto) | **×10** |

### System Impacts

| Hệ thống | Thay đổi |
|----------|----------|
| Chatbot/AI Engine | NLP rule-based → LLM GenAI (GPT-4/Claude) |
| CS Copilot | Mới — tích hợp AI gợi ý real-time vào CS workspace |
| Sentiment Detection | Mới — real-time emotion tracking |
| Auto-Context | Mới — tự trích xuất lịch sử đơn + tài khoản |
| Auto QA | Mới — AI chấm điểm 100% tickets |
| Proactive Engine | Mới — chủ động liên hệ khách trước vấn đề |

---

## 5. Phân tích Rủi ro (Risk Assessment)

| # | Rủi ro | Mức | Xác suất | Giải pháp |
|---|--------|-----|----------|-----------|
| 1 | AI LLM trả lời sai (hallucination) gây phẫn nộ khách | Cao | Trung bình | Fallback CS1 khi AI confidence < 80% |
| 2 | Copilot gợi ý sai solution, CS tin tưởng mù quáng | Trung bình | Thấp | Human-in-the-loop: CS xác nhận trước khi gửi |
| 3 | Sentiment detection sai, escalate không đúng lúc | Trung bình | Trung bình | Threshold tuning + fallback rule-based |
| 4 | Auto QA scoring thiên vị (phân biệt đối xử một số CS) | Thấp | Thấp | Calibration hàng tháng + human audit 5% |
| 5 | Proactive outreach gây phiền (gửi tin nhắn khi khách không cần) | Trung bình | Trung bình | Opt-out available + frequency cap |

---

## 6. ROI / Cost-Benefit Analysis

| Hạng mục | Chi phí ước tính (VND/tháng) | Ghi chú |
|----------|------------------------------|---------|
| **Chi phí hiện tại (AS-IS)** | 52,600/ticket × 12,000 tickets ≈ **631,000,000** | CS team 20 người, AHT 79 phút |
| AI LLM API cost | 45,000,000/tháng | ~12,000 tickets, GPU/server included |
| CS Copilot license | 30,000,000/tháng | 20 CS agents × tool |
| CSAT/Auto-QA tools | 8,000,000/tháng | SaaS |
| **Chi phí mới (TO-BE)** | 30,000/ticket × 9,000 tickets = **270,000,000** | CS team 15 người, AHT ~14 phút |
| **Tổng chi phí TO-BE** | 270,000,000 + 83,000,000 = **353,000,000/tháng** | |
| **Tiết kiệm hàng tháng** | **278,000,000 VND/tháng** | Giảm 44.1% |
| **ROI năm 1** | **(278M × 12 - 150M setup) / 150M = 21.3×** | Setup bao gồm training, integration |
| **Payback period** | **~16 ngày** | Break-even cực nhanh |

---

## 7. Đề Xuất Cuối Cùng (TO-BE Design Recommendation)

| # | Đề xuất | Độ ưu tiên | Thời gian thực hiện | Chi phí dự kiến |
|---|---------|-----------|--------------------|----|
| 1 | Implement AI LLM + Auto-Context cho Chatbot | **Cao** | 6 tuần | 80M VND |
| 2 | Deploy CS Copilot cho Tier 1 | **Cao** | 4 tuần | 50M VND |
| 3 | Sentiment Detection + Auto-Escalation | Trung bình | 3 tuần | 30M VND |
| 4 | Auto QA Scoring System | Trung bình | 3 tuần | 25M VND |
| 5 | Proactive Outreach Engine | Thấp | 4 tuần | 20M VND |
| 6 | CSAT CES Auto-Survey | **Cao** | 1 tuần | 5M VND |

**Timeline:** 3 tháng (12 tuần) cho toàn bộ TO-BE transformation

---

## 8. Tài liệu tham khảo

- [Lazada Help Center VN](https://helpcenter.lazada.vn) — Chính sách CSKH, quy trình hỗ trợ
- [Lazada Seller Center](https://sellercenter.lazada.vn) — CS workspace, ticketing system
- AS-IS BPMN: `processes/05-customer-service.bpmn`
- TO-BE BPMN: `processes-to-be/05-customer-service.bpmn`
- [analysis/05-customer-service.md](../05-customer-service.md) — Phân tích chi tiết quy trình

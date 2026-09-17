# Phân tích Nguyên nhân - Kết quả (Fishbone / Ishikawa)

> Rubric yêu cầu: Phân tích các bên liên quan — chọn 1 trong 3 mô hình: Pareto, Root-cause, Fishbone.
> Đồ án áp dụng Fishbone cho 3 vấn đề nghiêm trọng nhất của 10 quy trình Lazada:
> 1. Giao hàng thất bại 20-25%
> 2. Tỷ lệ trả hàng / hoàn tiền cao (cycle 8,5 ngày)
> 3. CSKH chậm (queue Tier 1 ~15 phút, chatbot deflection thấp)

---

## Fishbone #1: Giao hàng thất bại 20-25%

```
                        PEOPLE                    PROCESS
                   ┌─────────────┐           ┌──────────────────┐
                   │ Shipper không│           │ Không bắt buộc   │
                   │ gọi/nhắn trước│          │ pre-delivery call│
                   ├─────────────┤           ├──────────────────┤
                   │ Buyer vắng nhà│          │ Retry policy cứng│
                   │ giờ hành chính│          │ (3 lần cố định)  │
                   ├─────────────┤           ├──────────────────┤
                   │ Shipper quá tải│         │ ⭐ KPI misalignment│
                   │ peak hours    │          │ (speed > success)│
                   └──────┬──────┘           └────────┬─────────┘
                          │                            │
                          ▼                            ▼
              ┌─────────────────────────────────────────────────┐
              │       GIAO HÀNG THẤT BẠI 20-25%                │
              └─────────────────────────────────────────────────┘
                          ▲                            ▲
                          │                            │
                   ┌──────┴──────┐           ┌────────┴─────────┐
                   │ Tracking thủ│           │ Thiếu time slot  │
                   │ công, sai ETA│          │ selection        │
                   ├─────────────┤           ├──────────────────┤
                   │ App notification│        │ Địa chỉ không    │
                   │ bị mute/spam  │          │ chuẩn hóa       │
                   ├─────────────┤           ├──────────────────┤
                   │ ⭐ Không có AI│         │ ⭐ Contract incentive│
                   │ ETA prediction│         │ phạt delay, không│
                   │               │          │ thưởng success   │
                   └─────────────┘           └──────────────────┘
                      TECHNOLOGY                 ENVIRONMENT/POLICY
```

### Phân loại nguyên nhân:

| Trục | Nguyên nhân | Mức độ ảnh hưởng | Giải pháp TO-BE |
|------|-------------|-----------------|------------------|
| **People** | Shipper không liên hệ trước khi giao | Cao | Pre-delivery SMS/call 30 phút bắt buộc |
| **People** | Buyer vắng nhà giờ hành chính | Trung bình | Time slot selection |
| **Process** | ⭐ KPI đo speed thay vì first-attempt success | **Rất cao** | Đổi KPI: first-attempt ≥ 85% |
| **Process** | Retry policy cứng (3 lần cố định) | Trung bình | Dynamic retry theo lý do thất bại |
| **Technology** | ⭐ Không có AI ETA prediction | **Rất cao** | AI ETA + auto-notification |
| **Technology** | Tracking thủ công, sai lệch | Trung bình | Real-time GPS tracking |
| **Environment** | ⭐ Contract 3PL phạt delay, không thưởng success | **Rất cao** | Restructure contract incentives |
| **Environment** | Địa chỉ không chuẩn hóa | Thấp | Address validation API |

**ROOT CAUSE:** KPI misalignment + Contract incentive structure → Hệ thống khuyến khích shipper giao nhanh thay vì giao thành công.

---

## Fishbone #2: Tỷ lệ trả hàng & hoàn tiền cao (cycle 8,5 ngày)

```
                        PEOPLE                    PROCESS
                   ┌─────────────┐           ┌──────────────────┐
                   │ Buyer lạm dụng│          │ ⭐ Inspection thủ │
                   │ return abuse  │          │ công tại kho     │
                   ├─────────────┤           │ (24-48h)       │
                   │ Seller mô tả │          ├──────────────────┤
                   │ hàng sai /   │          │ Refund nhiều lớp │
                   │ sai mẫu      │          │ duyệt            │
                   ├─────────────┤           ├──────────────────┤
                   │ Khách không  │          │ ⭐ Không có AI    │
                   │ ở nhà pickup │          │ image inspection │
                   └──────┬──────┘           └────────┬─────────┘
                          │                            │
                          ▼                            ▼
              ┌─────────────────────────────────────────────────┐
              │    TỶ LỆ TRẢ HÀNG & HOÀN TIỀN CAO 8,5 NGÀY   │
              └─────────────────────────────────────────────────┘
                          ▲                            ▲
                          │                            │
                   ┌──────┴──────┐           ┌────────┴─────────┐
                   │ Chưa có     │           │ ⭐ Policy auto-  │
                   │ return-less │          │ confirm quá dài  │
                   │ refund      │          │                  │
                   ├─────────────┤           ├──────────────────┤
                   │ Không kết   │          │ Refund COD chậm  │
                   │ nối WMS ↔   │          │ (1-3 ngày) do    │
                   │ 3PL realtime│          │ cash handling    │
                   ├─────────────┤           ├──────────────────┤
                   │ ⭐ Tracking  │          │ Thời gian hoàn   │
                   │ hàng trả thủ│          │ trả 7 ngày       │
                   │ công        │          │ cho buyer xa     │
                   └─────────────┘           └──────────────────┘
                      TECHNOLOGY                 ENVIRONMENT/POLICY
```

### Phân loại nguyên nhân:

| Trục | Nguyên nhân | Mức độ ảnh hưởng | Giải pháp TO-BE |
|------|-------------|-----------------|------------------|
| **People** | Buyer lạm dụng return (return abuse) | Cao | Return abuse detection (fraud score + AI) |
| **People** | Seller mô tả hàng sai / sai mẫu tạo return | Trung bình | Chất lượng listing GI (image guidelines) |
| **Process** | ⭐ Inspection thủ công tại kho 24-48h (SLA 12h) | **Rất cao** | AI image analysis inspection (~30 phút) |
| **Process** | Refund nhiều lớp duyệt, Over-approval <200k | Cao | Auto-approve return-less cho low-risk <200k |
| **Technology** | ⭐ Chưa có return-less refund | **Rất cao** | Return-less refund cho đơn giá trị thấp |
| **Technology** | Không kết nối WMS ↔ 3PL realtime | Trung bình | Integration API realtime |
| **Environment** | ⭐ Policy auto-confirm 7 ngày quá dài | **Rất cao** | Rút xuống dưới 24h (24-72h Shop uy tín) |
| **Environment** | Refund COD chậm do cash handling | Trung bình | Lazada Wallet ưu tiên (instant), khuyến khích online payment |

**ROOT CAUSE:** Inspection thủ công kéo dài (24-48h) + Over-approval nhiều lớp + Policy auto-confirm 7 ngày → Cycle 8,5 ngày, chi phí 52,000 VND/đơn trả.

---

## Fishbone #3: CSKH chậm (queue Tier 1 ~15 phút, chatbot deflection thấp)

```
                        PEOPLE                    PROCESS
                   ┌─────────────┐           ┌──────────────────┐
                   │ Khách phải   │          │ ⭐ Chatbot      │
                   │ mô tả lại    │          │ deflection thấp │
                   │ vấn đề       │          │ (35-40%)        │
                   ├─────────────┤           ├──────────────────┤
                   │ Agent Tier 1 │          │ Không có auto-  │
                   │ đọc transcript│         │ escalation dựa  │
                   │ dài          │          │ trên sentiment  │
                   ├─────────────┤           ├──────────────────┤
                   │ Thiếu training│         │ ⭐ Staffing cố  │
                   │ Tier 2       │          │ định, không theo│
                   │              │          │ demand thời điểm │
                   └──────┬──────┘           └────────┬─────────┘
                          │                            │
                          ▼                            ▼
              ┌─────────────────────────────────────────────────┐
              │       CSKH CHẬM (QUEUE 5-30', AHT CAO)         │
              └─────────────────────────────────────────────────┘
                          ▲                            ▲
                          │                            │
                   ┌──────┴──────┐           ┌────────┴─────────┐
                   │ ⭐ NLP intent│          │ SLA ticket cứng  │
                   │ accuracy thấp│         │ không phân biệt   │
                   ├─────────────┤           │ mức khẩn cấp     │
                   │ Không tự     │          ├──────────────────┤
                   │ động lấy    │          │ ⭐ Không có AI    │
                   │ context đơn │          │ sentiment routing │
                   ├─────────────┤           ├──────────────────┤
                   │ KB chatbot   │          │ Escalation Tier 2 │
                   │ chưa đủ câu  │          │ không có SLA trả  │
                   │ trả lời      │          │ lời rõ           │
                   └─────────────┘           └──────────────────┘
                      TECHNOLOGY                 ENVIRONMENT/POLICY
```

### Phân loại nguyên nhân:

| Trục | Nguyên nhân | Mức độ ảnh hưởng | Giải pháp TO-BE |
|------|-------------|-----------------|------------------|
| **People** | Khách phải mô tả lại vấn đề khi chuyển chatbot → agent | Cao | Auto-context fetch từ order/payment DB |
| **People** | Agent Tier 1 đọc transcript dài | Trung bình | Auto-summary + context passing    |
| **Process** | ⭐ Chatbot deflection thấp (35-40%) | **Rất cao** | Mở rộng KB + auto-resolve 50-60% |
| **Process** | ⭐ Staffing cố định không theo demand | **Rất cao** | Demand forecasting ML + flexible scheduling |
| **Technology** | ⭐ NLP intent accuracy thấp | **Rất cao** | Nâng cấp intent classification (confidence ≥ 80%) |
| **Technology** | Không tự động lấy context đơn hàng/tài khoản | Trung bình | Auto-attach context (hệ thống trích xuất) |
| **Environment** | ⭐ SLA ticket cứng, không phân biệt khẩn cấp | **Rất cao** | SLA động theo to emotion/urgency |
| **Environment** | Không có AI sentiment routing | Trung bình | Sentiment-based routing ưu tiên khách bức xúc |

**ROOT CAUSE:** Chatbot deflection thấp + NLP intent accuracy kém + Staffing cố định → Volume dồn về agent, queue dài, AHT cao, CSAT thấp.

---

## Tổng hợp Root Causes & Ưu tiên cải tiến

| # | Root Cause | Vấn đề | Tác động | Ưu tiên |
|---|-----------|--------|----------|---------|
| 1 | KPI misalignment (speed > success) | Giao thất bại 20-25% | Rất cao | 🔴 Phase 1 |
| 2 | Contract incentive structure | Giao thất bại 20-25% | Rất cao | 🔴 Phase 1 |
| 3 | Không có AI ETA prediction | Giao thất bại 20-25% | Rất cao | 🟡 Phase 2 |
| 4 | Inspection thủ công 24-48h | Return chậm 7-14 ngày | Rất cao | 🔴 Phase 1 |
| 5 | Policy auto-confirm 7 ngày | Return chậm 7-14 ngày | Rất cao | 🟡 Phase 2 |
| 6 | Chưa có return-less refund | Return chậm 7-14 ngày | Cao | 🟡 Phase 2 |
| 7 | Chatbot deflection thấp 35-40% | CSKH chậm | Rất cao | 🔴 Phase 1 |
| 8 | NLP intent accuracy thấp | CSKH chậm | Rất cao | 🟡 Phase 2 |
| 9 | Staffing cố định không theo demand | CSKH chậm | Rất cao | 🟡 Phase 2 |

---

## Tổng kết 5 trục nguyên nhân (5M framework)

| Trục (5M) | Giao hàng thất bại | Return/Refund chậm | CSKH chậm |
|-----------|-------------------|--------------------|------------|
| **Man (Con người)** | Shipper không liên hệ trước | Buyer lạm dụng return | Khách mô tả lại vấn đề |
| **Method (Quy trình)** | KPI speed > success | Inspection thủ công + Over-approval | Chatbot deflection thấp + Staffing cố định |
| **Machine (Công nghệ)** | Không AI ETA prediction | Chưa return-less + tracking thủ công | NLP intent accuracy thấp |
| **Measurement (Dữ liệu)** | Tracking thủ công sai ETA | Refund nhiều lớp duyệt | Không auto-context đơn hàng |
| **Environment (Môi trường/Pháp lý)** | Contract 3PL phạt delay | Policy auto-confirm 7 ngày | SLA ticket cứng |

---

> **Liên kết:** [bpmn-va-annotation.md](bpmn-va-annotation.md) (181 tasks VA/BVA/NVA) — [issue-register.md](issue-register.md) (65 issues)
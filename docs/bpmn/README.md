# BPMN Diagrams — Lazada Vietnam

Thư mục chứa tài liệu về **12 mô hình BPMN 2.0** (6 AS-IS + 6 TO-BE) cho các quy trình nghiệp vụ của **Lazada Vietnam** (sàn thương mại điện tử TMĐT).

## Danh sách quy trình

**AS-IS (hiện trạng):**

| STT | File | Quy trình | Loại | Độ phức tạp | Số gateway |
|-----|------|-----------|------|------------|------------|
| 01 | `processes/01-seller-management.bpmn` | Quản lý nhà bán hàng (onboarding) | Quản lý | High | 15 |
| 02 | `processes/02-dispute-management.bpmn` | Quản lý tranh chấp | Quản lý | High | 15 |
| 03 | `processes/03-order-processing.bpmn` | Xử lý đơn hàng online Lazada | Cốt lõi ⭐ | **Extra** | 17 |
| 04 | `processes/04-return-refund.bpmn` | Hoàn trả & Refund | Cốt lõi ⭐ | **Extra** | 17 |
| 05 | `processes/05-customer-service.bpmn` | Quy trình Chăm sóc khách hàng | Hỗ trợ | Medium | 11 |
| 06 | `processes/06-marketing.bpmn` | Marketing & Khuyến mãi | Hỗ trợ | High | 14 |

**TO-BE (cải tiến):**

| STT | File | Quy trình | Số gateway |
|-----|------|-----------|------------|
| 01 | `processes-to-be/01-seller-management.bpmn` | Quản lý nhà bán hàng TO-BE | 5 |
| 02 | `processes-to-be/02-dispute-management.bpmn` | Quản lý tranh chấp TO-BE | 8 |
| 03 | `processes-to-be/03-order-processing.bpmn` | Xử lý đơn hàng online TO-BE | 9 |
| 04 | `processes-to-be/04-return-refund.bpmn` | Hoàn trả & Refund TO-BE | 6 |
| 05 | `processes-to-be/05-customer-service.bpmn` | Chăm sóc khách hàng TO-BE | 9 |
| 06 | `processes-to-be/06-marketing.bpmn` | Marketing & Khuyến mãi TO-BE | 8 |

> **Lưu ý về số gateway:** Đây là số liệu **đếm thực tế** từ file XML (`<bpmn:...Gateway>`), không phải ước tính. TO-BE giảm mạnh số gateway nhờ tự động hóa & loại bỏ nhánh điều kiện thừa — ví dụ Seller Management giảm từ **15 → 5** gateway, Order Processing từ **17 → 9**.

## Quy ước đặt tên file

- Prefix số thứ tự: `01-`, `02-`, ...
- Slug tiếng Anh, lowercase, hyphen-separated
- Extension: `.bpmn` (BPMN 2.0 XML — importable vào Camunda Modeler / Bizagi)
- File TO-BE nằm trong thư mục riêng `processes-to-be/`, cùng tên với AS-IS

## Cấu trúc Pool & Lanes

| Quy trình | Pool chính | Lanes điển hình |
|-----------|-----------|-----------------|
| Seller Management | Lazada Platform | Seller, Ban Phê duyệt, Lazada System |
| Dispute Management | Lazada Platform | Buyer, System, Đối soát Logistics |
| Order Processing | Lazada Platform | Buyer, Seller, System, 3PL (LEX/J&T) |
| Return & Refund | Lazada Platform | Buyer, Seller, System, 3PL |
| Customer Service | Lazada Platform | Khách hàng, CS Agent, System |
| Marketing | Lazada Platform | Marketing Lead, System, Seller |

Chi tiết số lanes/activities hiện tại:

| File | Lanes | Activities |
|------|-------|------------|
| 01-seller-management | 4 | 14 |
| 02-dispute-management | 5 | 12 |
| 03-order-processing | 5 | 26 |
| 04-return-refund | 5 | 13 |
| 05-customer-service | 5 | 18 |
| 06-marketing | 5 | 21 |

## BPMN Modeling Checklist

Khi vẽ mỗi BPMN diagram, đảm bảo:

### Cấu trúc cơ bản
- [ ] Pool chính: "Lazada Platform" hoặc tên quy trình
- [ ] Lanes cho mỗi actor (Buyer, Seller, Lazada System, 3PL, ...)
- [ ] Start event (bắt đầu quy trình)
- [ ] End event (kết thúc — có thể nhiều end events)
- [ ] Sequence flows nối các activities

### Activities
- [ ] User tasks (human steps) — hình chữ nhật viền dày
- [ ] Service tasks (automated) — hình chữ nhật viền mỏng
- [ ] Sub-processes (nếu complex) — hình chữ nhật viền đôi

### Gateways
- [ ] XOR gateway (exclusive) — hình thoi chữ X → rẽ nhánh 1 trong N
- [ ] AND gateway (parallel) — hình thoi dấu + → thực hiện đồng thời
- [ ] OR gateway (inclusive) — hình thoi chữ O → 1 hoặc nhiều nhánh

### Best practices
- [ ] Không có dead ends (mọi path đều dẫn đến end event)
- [ ] Không có infinite loops (trừ khi có điều kiện thoát rõ ràng)
- [ ] Gateways có điều kiện rõ ràng (condition expressions)
- [ ] Exception handling (error events, compensation)
- [ ] Annotations cho các bước quan trọng

### Thống kê cần có
Mỗi BPMN cần ghi nhận (đã đếm cho Lazada ở bảng trên):
- Số lanes: (xem bảng trên)
- Số activities: (xem bảng trên)
- **Số gateways: (xem bảng trên — đếm thực tế từ file XML)**
- Độ phức tạp: Medium/High/Extra

## Tools

- **Primary:** [Camunda Modeler](https://camunda.com/download/modeler/) — chuẩn BPMN 2.0
- **Alternative:** Draw.io (app.diagrams.net) — BPMN shape library
- **Validation:** `scripts/validate-bpmn.py` + `scripts/soundness-check.py` (kiểm tra Petri Net soundness)
- **Online:** bpmn.io (online validator)

## Export

- Source files: `.bpmn` (BPMN 2.0 XML, edit được bằng Camunda Modeler)
- Export PNG: 300 DPI, white background
- Export PDF: A3 landscape nếu diagram rộng
- Đặt file export cùng thư mục, prefix `_export-` (xem `docs/screenshots/`)

## Tham khảo

- [BPMN 2.0 Specification](https://www.omg.org/spec/BPMN/2.0/)
- [Camunda BPMN Guide](https://docs.camunda.org/guides/bpmn-guide/)
- [BPMN Quick Reference](https://www.bpmn.org/)

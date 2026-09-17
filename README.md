# Đồ án Hệ thống Quản trị Quy trình Nghiệp vụ — Lazada Việt Nam

**Môn học:** IE203 — Hệ thống Quản trị Quy trình Nghiệp vụ  
**Mã lớp:** IE203.P11  
**Giảng viên:** ThS. Hà Lê Hoài Trung  
**Nhóm:** Nhóm Lazada BA  
**Năm học:** 2025–2026

---

## Mô tả

Đồ án phân tích **10 quy trình nghiệp vụ** của Lazada Việt Nam, được phân loại theo mô hình APQC Process Classification Framework (PCF):

| Nhóm | Số lượng | Quy trình |
|------|----------|-----------|
| **Quản lý (Management)** | 3 | Quản lý Nhà bán hàng (01), Quản lý Tranh chấp & Khiếu nại (02), Quản lý Nhân sự & Đào tạo (07) |
| **Cốt lõi (Core)** | 4 | Xử lý Đơn hàng online (03), Thanh toán & Đối soát (08), Logistics & Giao nhận (09), Hoàn trả & Hoàn tiền (04) |
| **Hỗ trợ (Support)** | 3 | Chăm sóc Khách hàng (05), Marketing & Promotions (06), Vận hành Nền tảng Công nghệ (10) |

**Cả 10 quy trình** đều được phân tích chi tiết bằng BPMN 2.0 (AS-IS + TO-BE), kiểm chứng Petri Net, và đầy đủ phân tích định tính + định lượng:

| # | Quy trình | Tầng | AS-IS (tasks / gateways) | TO-BE (tasks / gateways) | Soundness |
|---|-----------|------|--------------------------|---------------------------|-----------|
| 01 | Quản lý Nhà bán hàng | Management | 14 / 15 | 13 / 7 | SOUND |
| 02 | Quản lý Tranh chấp | Management | 12 / 16 | 13 / 9 | SOUND |
| 03 | Xử lý Đơn hàng online ⭐ | Core | 26 / 17 | 22 / 9 | SOUND |
| 04 | Hoàn trả & Hoàn tiền | Core | 13 / 18 | 16 / 9 | SOUND |
| 05 | Chăm sóc Khách hàng | Support | 18 / 11 | 14 / 9 | SOUND |
| 06 | Marketing & Promotions | Support | 21 / 15 | 16 / 8 | SOUND |
| 07 | Quản lý Nhân sự & Đào tạo | Management | 17 / 15 | 21 / 15 | SOUND |
| 08 | Thanh toán & Đối soát | Core | 22 / 16 | 17 / 14 | SOUND |
| 09 | Logistics & Giao nhận | Core | 20 / 13 | 17 / 19 | SOUND |
| 10 | Vận hành Nền tảng CNTT | Support | 18 / 16 | 18 / 16 | SOUND |

**Phương pháp nghiên cứu:**
- Mô hình hóa BPMN 2.0 với pools/lanes theo actor (mỗi mô hình ≥7 gateways)
- Kiểm chứng Petri Net (Soundness Verification) — 3 thuộc tính theo van der Aalst (10/10 SOUND)
- Phân tích VA/BVA/NVA + Phân tích lãng phí (Waste Analysis)
- Phân tích Pareto (80/20 rule) — biểu đồ PNG cho cả 10 quy trình
- Phân tích định lượng: Cycle Time, Processing Time, Efficiency, Chi phí, Chất lượng (Quality metrics)
- Root Cause Analysis (Fishbone 5 cấp + 5-Why)
- Phỏng vấn (10 câu định tính + 10 câu định lượng) cho mỗi quy trình
- So sánh AS-IS vs TO-BE (10 file comparison)

---

## Cấu trúc dự án

```
lazada-ba-project/
├── README.md                          ← Bạn đang ở đây
├── PROCESSES.md                       ← Tổng quan 10 quy trình BPMN
├── DEVELOPMENT.md                     ← Hướng dẫn development
├── DOAN-LAZADA-FINAL.md               ← Báo cáo đồ án hoàn chỉnh
│
├── processes/                         ← BPMN 2.0 XML AS-IS (10 files)
│   ├── 01-seller-management.bpmn      ← Management
│   ├── 02-dispute-management.bpmn     ← Management
│   ├── 03-order-processing.bpmn       ← Core (trọng tâm)
│   ├── 04-return-refund.bpmn          ← Core
│   ├── 05-customer-service.bpmn       ← Support
│   ├── 06-marketing.bpmn              ← Support
│   ├── 07-hr-training.bpmn            ← Management
│   ├── 08-payment-settlement.bpmn     ← Core
│   ├── 09-logistics-delivery.bpmn     ← Core
│   └── 10-it-platform.bpmn            ← Support
│
├── processes-to-be/                   ← BPMN 2.0 XML TO-BE (10 files)
│   ├── 01-seller-management.bpmn
│   ├── 02-dispute-management.bpmn
│   ├── 03-order-processing.bpmn
│   ├── 04-return-refund.bpmn
│   ├── 05-customer-service.bpmn
│   ├── 06-marketing.bpmn
│   ├── 07-hr-training.bpmn
│   ├── 08-payment-settlement.bpmn
│   ├── 09-logistics-delivery.bpmn
│   └── 10-it-platform.bpmn
│
├── docs/
│   ├── analysis/                      ← Phân tích 10 quy trình
│   │   ├── 01-seller-management.md    ← VA/BVA/NVA + Waste + Cycle Time + Cost
│   │   ├── 02-dispute-management.md
│   │   ├── 03-order-processing.md
│   │   ├── 04-return-refund.md
│   │   ├── 05-customer-service.md
│   │   ├── 06-marketing.md
│   │   ├── 07-hr-training.md
│   │   ├── 08-payment-settlement.md
│   │   ├── 09-logistics-delivery.md
│   │   ├── 10-it-platform.md
│   │   ├── comparison/               ← AS-IS vs TO-BE so sánh (10 files)
│   │   ├── fishbone-diagrams.md       ← Fishbone root cause
│   │   ├── issue-register.md          ← Đăng ký vấn đề
│   │   └── 5-why-supplementary.md     ← Phân tích 5-Why bổ sung
│   ├── bpmn/                          ← BPMN modeling guide
│   ├── petri-net/                     ← Soundness verification (10 files)
│   │   ├── soundness-01-seller-management.md
│   │   ├── soundness-02-dispute-management.md
│   │   ├── soundness-03-order-processing.md
│   │   ├── soundness-04-return-refund.md
│   │   ├── soundness-05-customer-service.md
│   │   ├── soundness-06-marketing.md
│   │   ├── soundness-07-hr-training.md
│   │   ├── soundness-08-payment-settlement.md
│   │   ├── soundness-09-logistics-delivery.md
│   │   └── soundness-10-it-platform.md
│   ├── screenshots/                   ← BPMN screenshots PNG (20 files) + Pareto (10 files)
│   └── project-plan-gantt.md          ← Kế hoạch thực hiện 12 tuần
│
├── report/                            ← Các chương báo cáo
│   ├── chapter-1-introduction.md      ← Chương 1: Giới thiệu Lazada
│   ├── chapter-2-architecture.md      ← Chương 2: Kiến trúc quy trình
│   ├── chapter-3-analysis.md          ← Chương 3: Mô hình hóa BPMN + Phân tích
│   ├── chapter-4-conclusion.md        ← Chương 4: Kết luận & Đề xuất
│   ├── DOAN-LAZADA-UIT.doc            ← Báo cáo Word (.doc, HTML-based, có ảnh BPMN)
│   ├── convert-to-word.py             ← Script convert MD → .doc
│   └── build_docx_std.py              ← Script build .docx (python-docx) — DOAN-LAZADA-UIT.docx tại thư mục gốc
│
├── presentation/
│   ├── slides.md                      ← Presentation Marp (20 slides)
│   └── slides.html                    ← HTML deck (20 slides, tự trình chiếu được)
│
├── appendix/
│   ├── interview-questions.md         ← Bộ câu hỏi phỏng vấn chuẩn
│   ├── interviews/                    ← Kịch bản phỏng vấn 10 quy trình
│   ├── task-assignment.md             ← Phân công task theo tuần
│   └── workshop-meeting-minutes.md    ← Biên bản workshop
│
├── stakeholder/
│   ├── matrix.md                      ← Ma trận Stakeholder
│   └── raci.md                        ← Ma trận RACI
│
├── metrics/
│   ├── dashboard.html                 ← Dashboard hiệu suất
│   └── data.json                      ← Dữ liệu metrics
│
├── viewer/                            ← BPMN viewer (bpmn-js)
│   ├── index.html                    ← Viewer 10 quy trình (AS-IS ↔ TO-BE toggle)
│   ├── public/                        ← libs bpmn-js
│   └── copy-libs.js
│
└── scripts/
    ├── validate-bpmn.py               ← Validate BPMN XML
    ├── check-1in1out.py               ← Kiểm tra mỗi activity 1-in/1-out
    ├── soundness-check.py             ← Kiểm tra tính âm thanh Petri Net (van der Aalst)
    ├── generate-screenshots.js        ← Tạo PNG từ BPMN
    ├── convert-to-word.py             ← Chuyển MD → Word (.doc)
    ├── fix-ref-parity.py              ← Đồng bộ ref/lane AS-IS ↔ TO-BE
    ├── generate-pareto-charts.py      ← Tạo 10 Pareto chart PNG (SVG→PNG)
    ├── polish_vietnamese_labels.py    ← Làm sạch nhãn tiếng Việt
    └── label-gateways.py              ← Gán nhãn gateway
```

---

## Tóm tắt thống kê

| Chỉ số | Giá trị |
|--------|---------|
| Tổng số quy trình phân tích | **10** |
| Quy trình mô hình hóa BPMN 2.0 | **10 AS-IS + 10 TO-BE** (mỗi mô hình ≥7 gateways) |
| Tổng gateway AS-IS | 15, 16, 17, 18, 11, 15, 15, 16, 13, 16 (= 152) |
| Tổng gateway TO-BE | 7, 9, 9, 9, 9, 8, 15, 14, 19, 16 |
| Soundness verified | **10/10 SOUND** |
| Phân tích định tính (VA/BVA/NVA + Waste + Fishbone + 5-Why) | **10 quy trình** |
| Phân tích định lượng (Cycle Time, Cost, Quality) | **10 quy trình** |
| Phân tích Pareto (80/20) | **10 biểu đồ PNG** |
| Phỏng vấn (10 định tính + 10 định lượng) | **10 quy trình** |
| AS-IS vs TO-BE so sánh | **10 file comparison** |
| Screenshots BPMN | **20 PNG** (10 AS-IS + 10 TO-BE) |
| Báo cáo Word | **DOAN-LAZADA-UIT.doc + .docx** |

---

## Quick Start

### Validate BPMN

```bash
python3 scripts/validate-bpmn.py processes/*.bpmn
```

### Kiểm tra Soundness

```bash
python3 scripts/soundness-check.py processes/*.bpmn
```

### Tạo screenshots BPMN

```bash
PUPPETEER_EXECUTABLE_PATH=/usr/bin/google-chrome node scripts/generate-screenshots.js
```

### Tạo Word document

```bash
# .doc (HTML-based, report/DOAN-LAZADA-UIT.doc)
cd report
python3 convert-to-word.py

# .docx (python-docx, DOAN-LAZADA-UIT.docx tại thư mục gốc)
cd ..
python3 report/build_docx_std.py
```

### Xem BPMN diagrams trong trình duyệt

```bash
# Cần phục vụ qua HTTP (viewer dùng fetch)
cd viewer
python3 -m http.server 8080
# mở http://localhost:8080/ — duyệt 10 quy trình, toggle AS-IS ↔ TO-BE
```

### Xem BPMN diagrams

**Camunda Modeler** (khuyến nghị):
- Tải về: https://camunda.com/download/modeler/
- Mở: `camunda-modeler processes/03-order-processing.bpmn`

**Online (bpmn.io demo):**
- Truy cập: https://demo.bpmn.io/
- Kéo-thả file `.bpmn` vào trang

**Local viewer (bpmn-js):** xem mục "Xem BPMN diagrams trong trình duyệt" ở trên (viewer dùng thư mục `public/` có sẵn, không cần npm install).

---

## Công cụ

| Công cụ | Mục đích |
|---------|----------|
| Camunda Modeler | Vẽ BPMN 2.0 |
| bpmn.io (online) | Xem BPMN nhanh |
| Python 3 | Validation + soundness scripts |
| Node.js + Puppeteer | Tạo screenshots BPMN |
| Marp | Tạo presentation slides |

---

## Nguồn tham khảo

| Nguồn | URL | Sử dụng cho |
|-------|-----|-------------|
| Lazada Seller Center VN | sellercenter.lazada.vn | Seller onboarding, chính sách, phí |
| Lazada Help Center VN | helpcenter.lazada.vn | Chính sách hoàn trả, bảo vệ buyer |
| Lazada University | university.lazada.vn | Đào tạo seller |
| Wikipedia — Lazada Group | en.wikipedia.org | Lịch sử, cơ cấu tổ chức |
| CafeF | cafef.vn | Phỏng vấn CEO, phân tích thị trường |
| YouNet ECI / Metric.vn | — | Thị phần, hoạt động seller |
| Google-Temasek-Bain | — | Báo cáo E-Conomy SEA |

---

> **Lưu ý:** Nhóm nghiên cứu không có quyền truy cập vào hệ thống dữ liệu nội bộ của Lazada Việt Nam. Các số liệu định lượng được ước tính dựa trên: (1) quan sát UX flow công khai trên app/website, (2) benchmark từ báo cáo ngành, (3) phân tích heuristic và expert judgment.

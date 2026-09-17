# TRƯỜNG ĐẠI HỌC CÔNG NGHỆ THÔNG TIN
## KHOA HỆ THỐNG THÔNG TIN
---

# ĐỒ ÁN MÔN QUY TRÌNH NGHIỆP VỤ (IE203)

## HỆ THỐNG QUẢN TRỊ QUY TRÌNH NGHIỆP VỤ CỦA CÔNG TY THƯƠNG MẠI ĐIỆN TỬ LAZADA VIỆT NAM

**Giảng viên hướng dẫn:** ThS. Hà Lê Hoài Trung  
**Mã lớp học:** IE203.P11  
**Nhóm thực hiện:** Nhóm Lazada BA (02 thành viên)  
**Năm học:** 2025 - 2026  

---

# DANH MỤC TỪ VIẾT TẮT

| Từ viết tắt | Tên tiếng Anh đầy đủ | Ý nghĩa tiếng Việt |
|-------------|----------------------|--------------------|
| **3PL** | Third-Party Logistics | Đơn vị cung cấp dịch vụ logistics bên thứ ba (GHN, J&T Express, GrabExpress...) |
| **AI** | Artificial Intelligence | Trí tuệ nhân tạo |
| **API** | Application Programming Interface | Giao diện lập trình ứng dụng |
| **AS-IS** | Current State Process | Quy trình hiện tại (chưa cải tiến) |
| **BA** | Business Analyst / Business Analysis | Phân tích nghiệp vụ |
| **BPM** | Business Process Management | Quản trị quy trình nghiệp vụ |
| **BPMN** | Business Process Model and Notation | Ký hiệu và Mô hình Quy trình Nghiệp vụ (chuẩn 2.0) |
| **BVA** | Business Value-Added | Hoạt động tăng giá trị kinh doanh (cần thiết cho vận hành/pháp lý) |
| **C2C** | Consumer-to-Consumer | Mô hình kinh doanh giữa cá nhân với cá nhân |
| **B2C** | Business-to-Consumer | Mô hình kinh doanh giữa doanh nghiệp với cá nhân |
| **COD** | Cash on Delivery | Thanh toán bằng tiền mặt khi nhận hàng |
| **CS** / **CSKH** | Customer Service / Customer Care | Chăm sóc và hỗ trợ khách hàng |
| **CT** | Cycle Time | Thời gian chu kỳ (tổng thời gian từ đầu đến cuối quy trình) |
| **FBL** | Fulfilled by Lazada | Dịch vụ lưu kho, đóng gói và vận chuyển bởi Lazada |
| **FTE** | Full-Time Equivalent | Định biên nhân sự toàn thời gian |
| **GMV** | Gross Merchandise Value | Tổng giá trị hàng hóa giao dịch |
| **KPI** | Key Performance Indicator | Chỉ số đánh giá hiệu quả công việc |
| **LEX** | Lazada Express | Đơn vị vận chuyển nội bộ thuộc hệ sinh thái Lazada |
| **LazMall** | Lazada Mall | Kênh gian hàng chính hãng trên Lazada (32.000+ thương hiệu) |
| **Lazada University** | Lazada Seller University | Nền tảng đào tạo người bán trên Lazada |
| **ML** | Machine Learning | Học máy |
| **NVA** | Non-Value-Added | Hoạt động không tạo ra giá trị (lãng phí cần cắt giảm) |
| **PT** | Processing Time | Thời gian xử lý thực tế (thời gian chạm trực tiếp) |
| **RACI** | Responsible, Accountable, Consulted, Informed | Ma trận phân công trách nhiệm (Thực hiện, Chịu trách nhiệm, Tham vấn, Thông báo) |
| **ROI** | Return on Investment | Tỷ suất lợi nhuận trên vốn đầu tư |
| **SiPOC** | Suppliers, Inputs, Process, Outputs, Customers | Biểu đồ tổng quan Nguồn cung - Đầu vào - Quy trình - Đầu ra - Khách hàng |
| **SLA** | Service Level Agreement | Cam kết chất lượng dịch vụ |
| **TO-BE** | Future State Process | Quy trình tương lai (sau khi cải tiến) |
| **UIT** | University of Information Technology | Trường Đại học Công nghệ Thông tin - ĐHQG TP.HCM |
| **VA** | Value-Added | Hoạt động gia tăng giá trị trực tiếp cho khách hàng |
| **VSM** | Value Stream Mapping | Sơ đồ chuỗi giá trị |
| **WT** | Waiting Time | Thời gian chờ đợi (thời gian chết trong quy trình) |
| **XOR** | Exclusive Gateway | Cổng điều kiện rẽ nhánh loại trừ trong BPMN |

---

# MỤC LỤC

- [TÓM TẮT ĐỒ ÁN](#tóm-tắt-đồ-án)
- [MỞ ĐẦU](#mở-đầu)
- [Chương 1. GIỚI THIỆU CÔNG TY THƯƠNG MẠI ĐIỆN TỬ LAZADA VIỆT NAM](#chương-1-giới-thiệu-công-ty-thương-mại-điện-tử-lazada-việt-nam)
  - [1.1. Tổng quan về Lazada](#11-tổng-quan-về-lazada)
  - [1.2. Cơ cấu tổ chức và hoạt động kinh doanh](#12-cơ-cấu-tổ-chức-và-hoạt-động-kinh-doanh)
- [Chương 2. HỆ THỐNG QUY TRÌNH NGHIỆP VỤ LAZADA (10 QUY TRÌNH)](#chương-2-hệ-thống-quy-trình-nghiệp-vụ-lazada-10-quy-trình)
  - [2.1. Kiến trúc quy trình nghiệp vụ của Lazada](#21-kiến-trúc-quy-trình-nghiệp-vụ-của-lazada)
  - [2.2. Sơ đồ kiến trúc nghiệp vụ](#22-sơ-đồ-kiến-trúc-nghiệp-vụ)
  - [2.3. Mối quan hệ giữa các quy trình](#23-mối-quan-hệ-giữa-các-quy-trình)
- [Chương 3. MÔ HÌNH HÓA CHI TIẾT CÁC QUY TRÌNH BẰNG BPMN VÀ PHÂN TÍCH QUY TRÌNH](#chương-3-mô-hình-hóa-chi-tiết-các-quy-trình-bằng-bpmn-và-phân-tích-quy-trình)
  - [3.1. Tổng quan quy trình xử lý đơn hàng online Lazada](#31-tổng-quan-quy-trình-xử-lý-đơn-hàng-online-lazada)
  - [3.2. Mô tả chi tiết quy trình xử lý đơn hàng online](#32-mô-tả-chi-tiết-quy-trình-xử-lý-đơn-hàng-online)
  - [3.3. Mô hình BPMN quy trình xử lý đơn hàng online (AS-IS)](#33-mô-hình-bpmn-quy-trình-xử-lý-đơn-hàng-online-as-is)
  - [3.4. Phân tích Định tính & Nguyên nhân Gốc rễ](#34-phân-tích-định-tính--nguyên-nhân-gốc-rễ)
  - [3.5. Phân tích Định lượng Quy trình Xử lý Đơn hàng Online](#35-phân-tích-định-lượng-quy-trình-xử-lý-đơn-hàng-online)
  - [3.6. Quy trình Quản lý Nhà bán hàng (Management #1)](#36-quy-trình-quản-lý-nhà-bán-hàng-management-1)
  - [3.7. Quy trình Quản lý Tranh chấp và Rủi ro (Management #2)](#37-quy-trình-quản-lý-tranh-chấp-và-rủi-ro-management-2)
  - [3.8. Quy trình Hoàn trả và Hoàn tiền (Core #4)](#38-quy-trình-hoàn-trả-và-hoàn-tiền-core-4)
  - [3.9. Quy trình Chăm sóc Khách hàng (Support #1)](#39-quy-trình-chăm-sóc-khách-hàng-support-1)
  - [3.10. Quy trình Marketing và Khuyến mãi (Support #2)](#310-quy-trình-marketing-và-khuyến-mãi-support-2)
  - [3.11. Quy trình Quản lý Nhân sự & Đào tạo (Management #3)](#311-quy-trình-quản-lý-nhân-sự--đào-tạo-management-3)
  - [3.12. Quy trình Thanh toán & Đối soát (Core #2)](#312-quy-trình-thanh-toán--đối-soát-core-2)
  - [3.13. Quy trình Logistics & Giao nhận (Core #3)](#313-quy-trình-logistics--giao-nhận-core-3)
  - [3.14. Quy trình Vận hành Nền tảng Công nghệ (Support #3)](#314-quy-trình-vận-hành-nền-tảng-công-nghệ-support-3)
  - [3.15. Phân tích AS-IS / TO-BE Tổng hợp và Sơ đồ BPMN Cải tiến](#315-phân-tích-as-is--to-be-tổng-hợp-và-sơ-đồ-bpmn-cải-tiến)
- [Chương 4. KẾT LUẬN VÀ ĐỀ XUẤT](#chương-4-kết-luận-và-đề-xuất)
  - [4.1. Kết luận](#41-kết-luận)
  - [4.2. Hạn chế của đồ án](#42-hạn-chế-của-đồ-án)
  - [4.3. Hướng phát triển tiếp theo](#43-hướng-phát-triển-tiếp-theo)
- [TÀI LIỆU THAM KHẢO](#tài-liệu-tham-khảo)
- [PHỤ LỤC A: BỘ CÂU HỎI PHỎNG VẤN CHUẨN](#phụ-lục-a-bộ-câu-hỏi-phỏng-vấn-chuẩn)
- [PHỤ LỤC B: BIỂU MẪU WORKSHOP VÀ KỊCH BẢN PHỎNG VẤN MẪU](#phụ-lục-b-biểu-mẫu-workshop-và-kịch-bản-phỏng-vấn-mẫu)
- [PHỤ LỤC C: KẾ HOẠCH THỰC HIỆN ĐỒ ÁN (GANTT CHART)](#phụ-lục-c-kế-hoạch-thực-hiện-đồ-án-gantt-chart)
- [PHỤ LỤC D: DANH MỤC THUẬT NGỮ VÀ SỔ TAY (GLOSSARY)](#phụ-lục-d-danh-mục-thuật-ngữ-và-sổ-tay-glossary)
- [DANH MỤC HÌNH VẼ](#danh-mục-hình-vẽ)
- [DANH MỤC BẢNG](#danh-mục-bảng)

---

# TÓM TẮT ĐỒ ÁN

Đồ án **"Hệ thống Quản trị Quy trình Nghiệp vụ của Công ty Thương mại Điện tử Lazada Việt Nam"** tập trung nghiên cứu, mô hình hóa và phân tích toàn diện **10 quy trình nghiệp vụ cốt lõi và hỗ trợ** của Lazada Việt Nam -- nền tảng thương mại điện tử thuộc tập đoàn Alibaba, với pháp nhân tại Việt Nam là **Công ty TNHH Recess**.

Báo cáo ứng dụng chuẩn ký hiệu quốc tế **BPMN 2.0 (Business Process Model and Notation)** kết hợp với các phương pháp phân tích quy trình hiện đại: phân tích giá trị gia tăng (**VA/BVA/NVA**), phân tích lãng phí (**Waste Analysis: Move/Hold/Overdo**), phân tích nguyên nhân gốc rễ (**Fishbone Diagram & 5-Why**), biểu đồ **Pareto (80/20)**, ma trận phân công trách nhiệm (**RACI**), và phân tích định lượng thời gian chu kỳ (**Cycle Time**), chi phí (**Unit Economics**), chất lượng lỗi (**Defect Metrics**).

Kết quả nghiên cứu chỉ ra những điểm nghẽn chính trong quy trình AS-IS hiện tại: thời gian chờ Seller xác nhận đơn kéo dài (Hold chiếm ~44% chi phí lãng phí), tỷ lệ giao hàng thất bại lần đầu cao (20-25% -- cao hơn trung bình ngành), quy trình hoàn trả/hoàn tiền kéo dài (trung bình 8,5 ngày, kiểm định hàng hoàn tại kho Return Center là bottleneck lớn nhất ~50% chu kỳ refund), và thời gian đối soát thanh toán tiềm ẩn rủi ro dòng tiền cho Seller. Dựa trên các phát hiện đó, đồ án đề xuất mô hình cải tiến **TO-BE** ứng dụng định danh eKYC tự động, phân tầng rủi ro đơn hàng (Risk-tiered Order Processing), Instant Refund cho đơn giá trị thấp, và Chatbot AI nâng cao, giúp cắt giảm mạnh thời gian chu kỳ: duyệt Seller -95%, hoàn tiền -78,8%, kiểm định kho -75%, thời gian chờ kết nối Agent -50% và giảm chi phí xử lý đơn vị tới -65,4%/đơn hoàn trả.

---

## MỞ ĐẦU

### 1. Tính cấp thiết của đề tài
Trong bối cảnh nền kinh tế số phát triển bùng nổ, Thương mại Điện tử (TMĐT) đã trở thành trụ cột quan trọng của ngành bán lẻ Việt Nam. Lazada Việt Nam, thuộc tập đoàn Alibaba International Digital Commerce (AIDC), xử lý hàng triệu lượt truy cập mỗi ngày với hơn 32.000 thương hiệu trên LazMall. Tuy nhiên, thị phần của Lazada tại Việt Nam đã giảm từ ~22% (2022) xuống ~10-12% (2024), trong khi Shopee duy trì vị thế dẫn đầu (~65-70%) và TikTok Shop tăng trưởng mạnh (~20%). Việc phân tích hệ thống quy trình của Lazada giúp nhận diện chính xác các điểm nghẽn và đưa ra giải pháp tái thiết kế quy trình hiệu quả, từ đó nâng cao trải nghiệm người dùng và khả năng cạnh tranh thị trường.

### 2. Mục tiêu nghiên cứu
- Systematize và lập bản đồ Kiến trúc Quy trình Nghiệp vụ tổng thể của Lazada gồm **10 quy trình tiêu biểu** (3 Quản lý, 4 Cốt lõi, 3 Hỗ trợ).
- Mô hình hóa chi tiết **10 quy trình trọng điểm** bằng chuẩn BPMN 2.0 trên phần mềm Camunda Modeler và bpmn-js viewer.
- Áp dụng các phương pháp định tính (VA/BVA/NVA, Waste Analysis, Fishbone, 5-Why, Pareto) và định lượng (Cycle Time, Cost Breakdown, Quality Error Rates) cho ít nhất 2 quy trình chính.
- Thiết kế mô hình quy trình TO-BE cải tiến, tính toán ROI và lập lộ trình triển khai chuyển đổi số.

### 3. Đối tượng và Phạm vi nghiên cứu
- **Đối tượng nghiên cứu:** Hệ thống quản trị quy trình nghiệp vụ (Business Process Management) của công ty thương mại điện tử Lazada Việt Nam, tập trung vào chuỗi vận hành đặt hàng – thanh toán – giao nhận – hoàn trả và các hoạt động hỗ trợ vận hành.
- **Phạm vi nghiên cứu:**
  - **Về quy trình:** 10 quy trình nghiệp vụ trọng điểm được phân loại theo 3 nhóm Quản lý (Quản lý Nhà bán hàng, Quản lý Tranh chấp & Rủi ro, Quản lý Nhân sự & Tài chính), Cốt lõi (Xử lý Đơn hàng Online, Thanh toán & Đối soát, Giao nhận & Vận chuyển, Hoàn trả & Hoàn tiền) và Hỗ trợ (CSKH, Marketing & Khuyến mãi, Vận hành Nền tảng CNTT) — được lập bản đồ chi tiết tại Chương 2 (Bảng 2.1).
  - **Về phương pháp và mô hình hóa:** Mô hình hóa bằng chuẩn BPMN 2.0 (mô hình AS-IS và TO-BE), kết hợp phân tích định tính (VA/BVA/NVA, Waste Analysis, Fishbone, 5-Why, Pareto, RACI) và định lượng (Cycle Time, Unit Economics, Defect Metrics).
  - **Giới hạn:** Không phân tích chi tiết các quy trình nội bộ khác ngoài 10 quy trình trọng điểm; số liệu định lượng mang tính ước tính từ phỏng vấn mẫu và báo cáo thị trường công khai (xem Mục 4.2).

### 4. Phương pháp nghiên cứu
- **Phương pháp thu thập bằng chứng:** Phân tích tài liệu secondary data từ báo cáo tài chính Alibaba Group, chính sách Lazada Seller Center, Lazada Help Center, Lazada University, và các báo cáo thị trường từ YouNet ECI, Metric.vn, Google-Temasek-Bain e-Conomy SEA.
- **Phương pháp phỏng vấn khảo sát:** Xây dựng bộ câu hỏi chuẩn 20 câu (10 định tính + 10 định lượng, Phụ lục A) và tổ chức phỏng vấn sâu 10 nhân sự nội bộ phụ trách 10 quy trình nghiệp vụ trọng điểm (02 đại diện nhóm BA, 08 nhân sự vận hành nội bộ phụ trách các quy trình 01–10, ghi chú trong Phụ lục B).
- **Phương pháp mô hình hóa & phân tích:** Sử dụng Camunda Modeler vẽ sơ đồ BPMN 2.0, kiểm tra tính đúng đắn cấu trúc bằng thuật toán Petri Net soundness check (`soundness-check.py`).

---

# Chương 1. GIỚI THIỆU CÔNG TY THƯƠNG MẠI ĐIỆN TỬ LAZADA VIỆT NAM

## 1.1. Tổng quan về Lazada

### 1.1.1. Lịch sử hình thành
Lazada được thành lập vào ngày 27/03/2012 tại Singapore bởi Maximilian Bittner với sự hỗ trợ từ Rocket Internet (nhà đầu tư start-up công nghệ Đức). Ban đầu, Lazada hoạt động theo mô hình Amazon -- bán hàng từ kho của riêng mình (B2C). Năm 2013, Lazada chuyển sang mô hình Marketplace cho phép seller bên thứ ba tham gia bán hàng. Năm 2015, Lazada đối mặt với thách thức lớn khi chỉ dưới 1% người dân Việt Nam mua sắm online (so với 10% trung bình quốc tế), buộc phải triển khai mạnh mẽ mô hình thanh toán khi nhận hàng (COD).

### 1.1.2. Alibaba thâu tóm -- Giai đoạn đầu tư lớn (2016-2022)
Tháng 4/2016, Tập đoàn Alibaba chi 1 tỷ USD để mua 51% cổ phần Lazada, đánh dấu bước ngoặt chiến lược. Tổng đầu tư của Alibaba vào Lazada giai đoạn 2016-2022 lên tới khoảng **4,2 tỷ USD**:

| Thời điểm | Sự kiện | Giá trị |
|-----------|---------|---------|
| **04/2016** | Alibaba mua 51% cổ phần | **$1 tỷ** |
| **06/2017** | Alibaba tăng cổ phần lên 83% | **$1 tỷ** |
| **05/2022** | Alibaba rót thêm vốn | **$378,25 triệu** |
| **09/2022** | Alibaba rót thêm vốn | **$912,5 triệu** |

Năm 2023, Alibaba tái cơ cấu thành 6 đơn vị kinh doanh. Lazada thuộc **Alibaba International Digital Commerce (AIDC)** và nhận thêm khoản đầu tư lên tới $1,8 tỷ từ AIDC.

### 1.1.3. Đại cơ cấu và Chuẩn bị cho tương lai (2023-2026)

| Thời điểm | Sự kiện |
|-----------|---------|
| **06/2022** | James Dong trở thành CEO Lazada Group (thay Chun Li) |
| **2023** | Alibaba tái cơ cấu; Lazada thuộc AIDC |
| **01/2024** | Đợt sa thải lớn -- giảm 25-50% nhân sự Đông Nam Á |
| **Cuối 2025** | Tích hợp TMall (kênh chính hãng Taobao) và Gmarket (sàn TMĐT Hàn Quốc) |
| **08/2026** | Bị phạt **350 triệu VND** tại Việt Nam (Ủy ban Cạnh tranh Quốc gia) |
| **2026** | Mục tiêu bổ sung 40 triệu sản phẩm quốc tế từ 20.000 nhà bán |

### 1.1.4. Đơn vị pháp nhân tại Việt Nam
- **Tên công ty:** **Công ty TNHH Recess** (đơn vị vận hành Lazada tại Việt Nam)
- Bị Ủy ban Cạnh tranh Quốc gia (Bộ Công Thương) xử phạt 350 triệu VND (08/2026) vì cung cấp thông tin không chính xác về dịch vụ, gây nhầm lẫn cho người tiêu dùng.

### 1.1.5. Quy mô và Thị phần

**Bảng 1.1: Thông tin quy mô Lazada Việt Nam**

| Chỉ số | Giá trị ước tính |
|--------|-----------------|
| **Thị phần GMV tại Việt Nam (2024)** | ~10-12% |
| **Thị phần GMV Shopee (so sánh)** | ~65-70% |
| **Thị phần GMV TikTok Shop (so sánh)** | ~20-22% |
| **GMV toàn cục Lazada (2023)** | ~$18-20 tỷ |
| **GMV Lazada VN (ước tính 2024)** | ~$2-2,5 tỷ |
| **Lượt truy cập hàng tháng (VN)** | 40-60 triệu lượt |
| **Số lượng Seller hoạt động (VN)** | ~100.000-300.000+ |
| **LazMall** | 32.000+ thương hiệu chính hãng |
| **Đơn vị vận chuyển liên kết** | LEX (Lazada Express), GHN, J&T Express, Ninja Van, BEST Express, Viettel Post, GrabExpress |

**Bảng 1.2: Thị phần TMĐT Việt Nam (2024)**

| Sàn TMĐT | Thị phần GMV ước tính | Xu hướng |
|----------|----------------------|----------|
| **Shopee** | ~65-70% | Duy trì vị thế dẫn đầu |
| **TikTok Shop** | ~20-22% | Tăng trưởng nhanh nhất |
| **Lazada** | ~10-12% | Đang mất thị phần |
| **Tiki** | ~2-3% | Cương cố ở niche chính hãng |

### 1.1.6. Lịch sử CEO Lazada Group

| Giai đoạn | CEO | Ghi chú |
|-----------|-----|---------|
| 03/2012 - 03/2018 | Maximilian Bittner | Người sáng lập |
| 03/2018 - 12/2018 | Lucy Peng | Giám đốc Alibaba |
| 12/2018 - 06/2020 | Pierre Poignant | |
| 06/2020 - 06/2022 | Chun Li | |
| 06/2022 - hiện tại | **James Dong** | |

## 1.2. Cơ cấu tổ chức và hoạt động kinh doanh

### 1.2.1. Cơ cấu tổ chức
Lazada Việt Nam được vận hành theo mô hình ma trận kết hợp giữa chức năng và khối nghiệp vụ sản phẩm:

```
                        ┌────────────────────────────────┐
                        │   CEO LAZADA GROUP              │
                        │   (James Dong)                  │
                        │   AIDC — Alibaba International  │
                        └──────────────┬─────────────────┘
                                       │
       ┌──────────────┬────────────────┼────────────────┬──────────────┐
       ▼              ▼                ▼                ▼              ▼
┌─────────────┐ ┌──────────────┐ ┌──────────────┐ ┌────────────┐ ┌────────────┐
│ KINH DOANH  │ │  VẬN HÀNH    │ │  CÔNG NGHỆ   │ │  HỖ TRỢ    │ │ TÀI CHÍNH  │
│ (Business)  │ │ (Operations) │ │ (Technology) │ │ (Support)  │ │ (Finance)  │
└──────┬──────┘ └──────┬───────┘ └──────┬───────┘ └─────┬──────┘ └─────┬──────┘
       │               │                │               │              │
  • Seller         • Xử lý đơn     • Platform      • Nhân sự      • Kế toán
  • Buyer          • Kho/Fulfill   • Data & AI     • Pháp lý      • Đối soát
  • LazMall        • LEX Express   • Bảo mật       • Compliance   • Ngân sách
  • Marketing      • CSKH          • DevOps        • Lazada Univ  • Risk
```

**Hình 1.1: Sơ đồ cơ cấu tổ chức Lazada Việt Nam**

### 1.2.2. Hoạt động kinh doanh
Hoạt động kinh doanh của Lazada tạo ra doanh thu từ các nguồn chính:
1. **Phí sàn (Platform Fees):** Hoa hồng giao dịch (1-10% tùy danh mục), phí thanh toán (~2%/giao dịch), phí vận chuyển, phí lưu kho (FBL).
2. **Quảng cáo TMĐT (Lazada Sponsored Solutions):** Quảng cáo tìm kiếm, quảng cáo khám phá, hiển thị ưu tiên.
3. **Dịch vụ kho vận (Fulfillment by Lazada - FBL):** Phí lưu kho, đóng gói và vận chuyển qua LEX Express.
4. **Cross-border Commerce:** TMall, Gmarket -- tích hợp hàng hóa quốc tế.

**Bảng 1.3: Mô hình phí hoa hồng theo ngành hàng**

| Nhóm hàng | Tỷ lệ hoa hồng ước tính |
|-----------|------------------------|
| Điện tử / Gia dụng | 1-2% |
| Thời trang | 3-5% |
| Mỹ phẩm / Sức khỏe | 3-5% |
| Tiêu dùng / FMCG | 1-4% |
| Nhà cửa đời sống | 3-5% |
| Mẹ và Bé | 3-5% |
| Thể thao / Du lịch | 3-5% |
| Hàng xách tay | 5-10% |

---

# Chương 2. HỆ THỐNG QUY TRÌNH NGHIỆP VỤ LAZADA (10 QUY TRÌNH)

## 2.1. Kiến trúc quy trình nghiệp vụ của Lazada

Để đảm bảo vận hành thông suốt hàng triệu giao dịch mỗi ngày, Lazada xây dựng kiến trúc quy trình gồm 3 nhóm chính: **Quản lý (Management)**, **Cốt lõi (Core)** và **Hỗ trợ (Support)**. Dưới đây là mô tả chi tiết từng quy trình theo mô hình Ngôi nhà (House Diagram) phân tầng:

### 2.1.1. Nhóm quy trình Quản lý (Management Process - 3 quy trình)

#### 1. Quy trình Quản lý Nhà bán hàng (Seller Management)
- **Tác nhân tham gia:** Seller, Lazada System (Automated), Compliance Team, Legal / Giám sát Vận hành.
- **Mô tả quy trình bằng ngôn ngữ - lời:**
  - *Bước 1:* Seller truy cập sellercenter.lazada.vn, nhập thông tin cá nhân/doanh nghiệp, số định danh CCCD/MST và tài khoản ngân hàng liên kết.
  - *Bước 2:* Hệ thống tự động kiểm tra OCR, đối chiếu MST, check danh sách cấm và xác thực trùng lặp thông tin; gửi OTP xác thực SĐT.
  - *Bước 3:* Seller tải lên CMND/CCCD + GPKD + Giấy chứng nhận (LazMall); hệ thống Validate định danh tự động và quét OCR kiểm tra giấy tờ giả.
  - *Bước 4:* Chuyên viên Compliance thẩm định thủ công hồ sơ (24-48h) đối với ca rủi ro cao; hệ thống chấm điểm rủi ro (Risk scoring) và phân tầng.
  - *Bước 5:* Hệ thống phê duyệt cấp quyền bán hàng hoặc gửi thông báo từ chối nêu rõ lý do; Seller thiết lập shop và bắt đầu listing sản phẩm.
  - *Bước 6:* Định kỳ giám sát điểm chất lượng (Seller Score) tự động; nếu vi phạm chính sách: cảnh cáo → tạm khóa 7 ngày → khóa vĩnh viễn.
- **Đối tượng khách hàng:** Người bán hàng (Seller) muốn thiết lập và phát triển gian hàng trên Lazada.
- **Những khả năng kết quả:** Phê duyệt thành công (Bắt đầu bán hàng); Từ chối hồ sơ (Yêu cầu bổ sung giấy tờ); Cảnh cáo / Suspended / Deactivated (Nếu phát hiện vi phạm).

#### 2. Quy trình Quản lý Tranh chấp & Rủi ro (Dispute & Risk Management)
- **Tác nhân tham gia:** Buyer, Lazada System (Automated), Seller, CS Agent, Escalation Team.
- **Mô tả quy trình bằng ngôn ngữ - lời:**
  - *Bước 1:* Khi có phát sinh khiếu nại không thể tự thỏa thuận giữa Buyer và Seller, Buyer khởi tạo Yêu cầu Tranh chấp trên ứng dụng (Tạo tranh chấp + lý do).
  - *Bước 2:* Hệ thống tự động thu thập dữ liệu đơn hàng và AI phân loại tranh chấp (Đơn giản/Phức tạp); vụ việc đơn giản được AI tự giải quyết, vụ việc phức tạp chuyển sang đối soát.
  - *Bước 3:* Hệ thống kiểm tra lịch sử SLA của Seller và gửi thông báo đối soát đến hai bên; Seller phản hồi trong hạn định 48 giờ (loop bổ sung bằng chứng nếu chưa đầy đủ).
  - *Bước 4:* CS Agent thẩm định toàn bộ hồ sơ, phân định lỗi thuộc về bên nào và ban hành quyết định xử lý.
  - *Bước 5:* Ra quyết định: Hoàn tiền cho Buyer (Buyer thắng), Bác bỏ khiếu nại (Giải ngân cho Seller), hoặc Chuyển hồ sơ cho Lazada Escalation Team.
  - *Bước 6:* Trường hợp chuyển lên, Hội đồng thẩm định & ra quyết định cuối — kết quả final & binding.
- **Đối tượng khách hàng:** Cả Người mua và Người bán có tranh chấp phát sinh trong giao dịch.
- **Những khả năng kết quả:** Hoàn tiền toàn bộ/một phần cho Buyer; Bác bỏ khiếu nại (Giải ngân cho Seller); Khóa tài khoản gian lận.

#### 3. Quy trình Quản lý Nhân sự & Tài chính nội bộ (HR & Finance Management)
- **Tác nhân tham gia:** HR Team, Lazada University, Seller / Nhân viên, Compliance.
- **Mô tả quy trình bằng ngôn ngữ - lời:**
  - *Bước 1:* Lập kế hoạch đào tạo theo quý; Giám đốc HR và Phòng Tài chính duyệt ngân sách đào tạo.
  - *Bước 2:* Xây dựng nội dung khóa học (onboarding, nâng cao, compliance) và Publish lên Lazada University; Seller/Nhân viên đăng ký tham gia, học tập và thi đánh giá kiến thức (≥70%).
  - *Bước 3:* Cấp chứng chỉ hoàn thành; Kiểm tra tuân thủ chính sách đào tạo định kỳ; nếu phát hiện vi phạm — cảnh cáo hoặc đình chỉ quyền truy cập.
  - *Bước 4:* Đánh giá hiệu quả đào tạo sau khóa học.
- **Đối tượng khách hàng:** Toàn bộ nhân viên nội bộ Lazada.
- **Những khả năng kết quả:** Ngân sách được duyệt; Báo cáo tài chính định kỳ; Điều chỉnh nhân sự.

### 2.1.2. Nhóm quy trình Cốt lõi (Core Process - 4 quy trình)

#### 4. Quy trình Xử lý Đơn hàng Online (Order Processing -- Quy trình Trọng tâm)
- **Tác nhân tham gia:** Buyer, Lazada System, Seller, Đơn vị Vận chuyển (LEX/3PL), Payment Gateway, Warehouse/FBL.
- **Mô tả quy trình bằng ngôn ngữ - lời:**
  - *Bước 1:* Buyer chọn sản phẩm, áp mã giảm giá/freeship và bấm "Đặt hàng".
  - *Bước 2:* Hệ thống kiểm tra tồn kho + validate thông tin đơn + kiểm tra gian lận (AI) và xử lý thanh toán (COD hoặc Online Payment).
  - *Bước 3:* Seller xác nhận đơn hàng (trong SLA 48h), đóng gói sản phẩm và bàn giao hàng cho 3PL/LEX (Pickup) hoặc Seller mang hàng ra bưu cục (Drop-off).
  - *Bước 4:* ĐVVC vận chuyển qua các trạm trung chuyển (Sort Center) và Shipper chặng cuối giao hàng đến tay Buyer (tối đa 3 lần thử).
  - *Bước 5:* Buyer nhận hàng, kiểm tra và bấm "Đã nhận được hàng" (hoặc hệ thống tự động hoàn tất sau 7 ngày); sau đó hệ thống giải ngân cho Seller.
- **Đối tượng khách hàng:** Người mua (Buyer) và Người bán (Seller).
- **Những khả năng kết quả:** Đơn giao thành công (Hoàn tất giao dịch); Đơn hàng bị hủy (Do Seller không xác nhận/Hết hàng); Đơn giao thất bại (Hoàn về Seller).

#### 5. Quy trình Thanh toán và Đối soát (Payment & Settlement)
- **Tác nhân tham gia:** Buyer, Payment Gateway (VNPay, OnePay, MoMo, ZaloPay), Hệ thống Kế toán Lazada, Finance Team, Seller.
- **Mô tả quy trình bằng ngôn ngữ - lời:**
  - *Bước 1:* Buyer thực hiện thanh toán khi đặt hàng (qua ví/thẻ) hoặc trả tiền mặt COD cho Shipper khi nhận hàng.
  - *Bước 2:* Tiền hàng được ghi nhận và giữ an toàn trong Tài khoản Bảo hộ Lazada Escrow.
  - *Bước 3:* Đơn vị vận chuyển đối soát số tiền COD đã thu với Hệ thống Tài chính hàng ngày.
  - *Bước 4:* Khi đơn hàng chuyển trạng thái "Hoàn tất", hệ thống tự động tính toán trừ phí sàn, phí vận chuyển và cộng tiền ròng vào Số dư Tài khoản Lazada của Seller.
  - *Bước 5:* Seller thực hiện rút tiền từ Số dư về ngân hàng liên kết (L+2 model).
- **Đối tượng khách hàng:** Người bán (Seller) nhận dòng tiền thanh toán và Lazada.
- **Những khả năng kết quả:** Thanh toán & giải ngân thành công; Giao dịch thất bại / Lỗi thanh toán (Hoàn tiền cho Buyer); Lệch dòng tiền đối soát (Chuyển Finance xử lý).

#### 6. Quy trình Giao nhận & Vận chuyển (Logistics & Delivery)
- **Tác nhân tham gia:** Seller, LEX Express / 3PL (GHN, J&T, Ninja Van, BEST Express, GrabExpress), Warehouse QC, Shipper chặng cuối, Buyer.
- **Mô tả quy trình bằng ngôn ngữ - lời:**
  - *Bước 1:* ĐVVC tiếp nhận bưu kiện từ Seller tại điểm Drop-off hoặc qua dịch vụ Pickup.
  - *Bước 2:* Bưu kiện được đưa về Kho gom (First-mile Hub) và quét mã vạch tracking.
  - *Bước 3:* Vận chuyển chặng trung gian (Line-haul) đến Kho phân loại trung tâm (Sortation Center).
  - *Bước 4:* Máy chia chọn tự động phân loại bưu kiện về các Last-mile Hub tương ứng.
  - *Bước 5:* Shipper nhận hàng, liên hệ Buyer và tiến hành giao hàng chặng cuối.
- **Đối tượng khách hàng:** Người mua nhận hàng đúng hạn và an toàn.
- **Những khả năng kết quả:** Giao hàng thành công ngay lần 1; Giao thất bại lần 1 (Hẹn giao lại lần 2/3); Giao thất bại toàn bộ (Chuyển hoàn bưu kiện về Seller).

#### 7. Quy trình Hoàn trả và Hoàn tiền (Return & Refund)
- **Tác nhân tham gia:** Buyer, Lazada System (Automated), CS Agent, 3PL/Warehouse, Payment Gateway.
- **Mô tả quy trình bằng ngôn ngữ - lời:**
  - *Bước 1:* Buyer ấn "Trả hàng/Hoàn tiền", chọn lý do (Full Return / Partial Refund / Only Refund) và tải lên hình ảnh/video bằng chứng.
  - *Bước 2:* Hệ thống tự động kiểm tra điều kiện hợp lệ (cửa sổ hoàn trả, đơn đủ điều kiện) và AI phân loại mức độ nghiêm trọng của bằng chứng khiếu nại.
  - *Bước 3:* CS Agent thẩm định hồ sơ bằng chứng; nếu yêu cầu hợp lệ, hệ thống phê duyệt phương án hoàn tiền hoặc trả hàng.
  - *Bước 4:* Trường hợp trả hàng, LEX/3PL đặt lịch hẹn Shipper đến lấy hàng hoàn (retry nếu thất bại) và kiểm định hàng hóa tại kho Return Center (≤12h).
  - *Bước 5:* Hệ thống phát lệnh hoàn tiền về phương thức thanh toán ban đầu của Buyer và gửi thông báo tiến độ tự động.
- **Đối tượng khách hàng:** Người mua (Buyer) muốn đổi trả sản phẩm lỗi / không vừa ý.
- **Những khả năng kết quả:** Hoàn tiền thành công; Bác bỏ yêu cầu trả hàng; Hoàn tiền không cần trả hàng (Đơn giá trị thấp).

### 2.1.3. Nhóm quy trình Hỗ trợ (Support Process - 3 quy trình)

#### 8. Quy trình Chăm sóc Khách hàng (Customer Service - CSKH)
- **Tác nhân tham gia:** Customer (Buyer/Seller), Chatbot/AI (Lazzie), CS Tier 1, CS Tier 2, System.
- **Mô tả quy trình bằng ngôn ngữ - lời:**
  - *Bước 1:* Khách hàng gửi yêu cầu hỗ trợ qua Live Chat, Hotline 1900 1010, Email, hoặc Help Center; AI NLP phân loại ý định & mức độ khẩn cấp.
  - *Bước 2:* Chatbot (Lazada Assistant) tự động giải đáp câu hỏi thường gặp (FAQ) nếu có kịch bản trả lời.
  - *Bước 3:* Nếu yêu cầu phức tạp, hệ thống kiểm tra SLA xử lý ticket và chuyển hội thoại đến Tư vấn viên Tier 1 (kèm xác minh danh tính khách hàng).
  - *Bước 4:* Tier 1 kiểm tra thông tin đơn hàng trên hệ thống CRM (lịch sử tương tác), tư vấn và đưa giải pháp xử lý trực tiếp.
  - *Bước 5:* Trường hợp vượt thẩm quyền, Chuyên viên Tier 2 thẩm định chuyên sâu và xử lý dứt điểm; gửi nhắc nhở phản hồi cho khách hàng nếu quá thời gian chờ.
  - *Bước 6:* Khách hàng xác nhận hoàn tất hỗ trợ và chấm điểm khảo sát CSAT; QA Follow-up đánh giá chất lượng sau đóng ticket.
- **Đối tượng khách hàng:** Người mua và Người bán cần trợ giúp thông tin.
- **Những khả năng kết quả:** Giải đáp thành công tức thì (Chatbot/Agent T1); Tạo Ticket theo dõi sự cố; Đóng yêu cầu và thu thập CSAT.

#### 9. Quy trình Marketing và Khuyến mãi (Marketing & Campaign)
- **Tác nhân tham gia:** Marketing Team, Approval, Lazada System, Sellers, Buyers.
- **Mô tả quy trình bằng ngôn ngữ - lời:**
  - *Bước 1:* Đội ngũ Marketing lập kế hoạch chiến dịch (Mega Sale 9.9, 11.11, 12.12, Flash Sale hàng ngày) và dự toán ngân sách.
  - *Bước 2:* Phê duyệt ngân sách theo hạng mức (Trưởng bộ phận / CFO / Hội đồng).
  - *Bước 3:* Creative Team thiết kế banner, landing page; Legal duyệt nội dung.
  - *Bước 4:* Mở cổng đăng ký chiến dịch trên Kênh Người Bán; Seller lựa chọn sản phẩm và cam kết mức giảm giá.
  - *Bước 5:* Hệ thống tự động thẩm định điều kiện seller (điểm chất lượng, lịch sử vi phạm) và duyệt sản phẩm hiển thị.
  - *Bước 6:* Kích hoạt Campaign, theo dõi GMV realtime và xử lý sự cố trong chiến dịch.
  - *Bước 7:* Post-campaign analysis (ROI, GMV vs mục tiêu).
- **Đối tượng khách hàng:** Người mua săn voucher/đồ rẻ và Người bán muốn bùng nổ doanh số.
- **Những khả năng kết quả:** Chiến dịch kích cầu thành công vượt KPI GMV; Điều chỉnh ngân sách giữa chừng; Hủy bỏ chương trình nếu gặp sự cố hệ thống.

#### 10. Quy trình Công nghệ Thông tin (IT & Platform Operations)
- **Tác nhân tham gia:** Product Owner, Dev Team, QA / Tester, DevOps / CI-CD, Security.
- **Mô tả quy trình bằng ngôn ngữ - lời:**
  - *Bước 1:* Product Owner tạo User Story & acceptance criteria; ưu tiên backlog & sprint planning.
  - *Bước 2:* Đội ngũ Kỹ thuật thiết kế kiến trúc & API, viết code theo User Story, chạy unit test & code review.
  - *Bước 3:* QA thực hiện System Test & Integration Test, Performance test & load test; Security quét lỗ hổng bảo mật (SAST/DAST).
  - *Bước 4:* DevOps triển khai lên Pre-Staging → Staging (UAT) → Production (Blue-Green Deploy); giám sát metrics sau deploy 30 phút (rollback nếu không ổn định).
  - *Bước 5:* Xử lý sự cố infrastructure & incident; áp dụng bản vá bảo mật khẩn cấp nếu phát hiện lỗ hổng nghiêm trọng.
- **Đối tượng khách hàng:** Toàn bộ nhân viên nội bộ và người dùng app/web Lazada.
- **Những khả năng kết quả:** Triển khai tính năng mới mượt mà (Deploy OK); Khắc phục sự cố hệ thống; Rollback phiên bản cũ nếu phát sinh lỗi.

---

## 2.2. Sơ đồ kiến trúc nghiệp vụ

Sơ đồ Kiến trúc Quy trình Nghiệp vụ tổng thể của Lazada được thể hiện qua mô hình phân tầng chuẩn mực:

```
┌─────────────────────────────────────────────────────────────────────────┐
│                  KIẾN TRÚC QUY TRÌNH NGHIỆP VỤ LAZADA                   │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  ┌────────────────── NHÓM QUẢN LÝ (3) ─────────────────┐               │
│  │  • Quản lý nhà bán hàng (Seller Management)          │               │
│  │  • Quản lý tranh chấp & rủi ro (Dispute & Risk Mgmt) │               │
│  │  • Quản lý nhân sự & tài chính (HR & Finance)        │               │
│  └──────────────────────────────────────────────────────┘               │
│                                                                         │
│  ┌────────────────── NHÓM CỐT LÕI (4) ─────────────────┐               │
│  │  • Xử lý đơn hàng online         ◄── QUY TRÌNH CHÍNH │               │
│  │  • Thanh toán và đối soát                            │               │
│  │  • Giao nhận và vận chuyển (Logistics)               │               │
│  │  • Hoàn trả và hoàn tiền                             │               │
│  └──────────────────────────────────────────────────────┘               │
│                                                                         │
│  ┌────────────────── NHÓM HỖ TRỢ (3) ──────────────────┐               │
│  │  • Chăm sóc khách hàng (Customer Service)            │               │
│  │  • Marketing và khuyến mãi (Campaign Management)     │               │
│  │  • Công nghệ thông tin (IT Operations)               │               │
│  └──────────────────────────────────────────────────────┘               │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```
**Hình 2.1: Sơ đồ kiến trúc quy trình nghiệp vụ Lazada**

---

### 2.2.1. Bảng tổng hợp 10 quy trình nghiệp vụ

**Bảng 2.1: Bảng tổng hợp 10 quy trình nghiệp vụ Lazada**

| STT | Tên quy trình | Nhóm | Tác nhân chính (Actors) Internal / External | Khách hàng của quy trình (Process Customer) | Kết quả có thể (Output + tiêu cực) |
|-----|--------------|------|---------------------------------------------|---------------------------------------------|------------------------------------|
| 1 | Quản lý Nhà bán hàng | Quản lý | Internal: Lazada System, Compliance Team, Legal / Giám sát Vận hành / External: Seller | Seller | Approved (Bắt đầu bán) / Rejected (Từ chối) / Suspended (Khóa TK) / Re-registered |
| 2 | Quản lý Tranh chấp & Rủi ro | Quản lý | Internal: Lazada System, CS Agent, Escalation Team / External: Buyer, Seller | Buyer, Seller | Resolved-buyer wins / Resolved-seller wins / Escalated / Withdrawn |
| 3 | Quản lý Nhân sự & Tài chính | Quản lý | Internal: HR Team, Lazada University, Compliance / External: Seller / Nhân viên | Internal Staff | Ngân sách duyệt / Báo cáo tài chính / Điều chỉnh NS |
| 4 | Xử lý Đơn hàng Online | Cốt lõi | Internal: Lazada System / External: Buyer, Seller, 3PL/Shipper, Payment Gateway | Buyer, Seller | Completed / Auto-cancelled / Seller-rejected / Return-initiated / COD-settled / Failed-delivery |
| 5 | Thanh toán & Đối soát | Cốt lõi | Internal: Lazada System (Escrow), Finance / External: Buyer, Payment Gateway (VNPay/MoMo/ZaloPay), Seller | Seller, Buyer | Thanh toán OK / Lệch dòng tiền / Error-refund |
| 6 | Giao nhận & Vận chuyển | Cốt lõi | Internal: Lazada System / External: Seller, LEX / 3PL (GHN, J&T, Grab, NINJAVAN), Shipper (Giao hàng), Buyer | Buyer | Giao thành công 1st / Retry / Chuyển hoàn Seller |
| 7 | Hoàn trả & Hoàn tiền | Cốt lõi | Internal: Lazada System, CS Agent, 3PL/Warehouse / External: Buyer, Payment Gateway | Buyer | Refunded / Rejected-return / Seller-compensated / Buyer-keeps-item |
| 8 | Chăm sóc Khách hàng | Hỗ trợ | Internal: Chatbot/AI, CS Tier 1, CS Tier 2, System / External: Customer (Buyer/Seller) | Customer | Resolved / Escalated / Closed-unresolved / CSAT-collected |
| 9 | Marketing & Khuyến mãi | Hỗ trợ | Internal: Marketing Team, Approval, Lazada System / External: Sellers, Buyers | Buyer, Seller | Launched / Rejected / Completed / Auto-renewed |
| 10 | Công nghệ Thông tin | Hỗ trợ | Internal: Product Owner, Dev Team, QA / Tester, DevOps / CI-CD, Security | Internal Staff | Deploy OK / Bug fix / Rollback |

---

## 2.3. Mối quan hệ giữa các quy trình

Các quy trình trong hệ thống quy trình nghiệp vụ của Lazada không hoạt động độc lập mà liên kết chặt chẽ qua luồng dữ liệu và sự kiện kích hoạt:
1. **Quản lý Nhà bán hàng (1)** thẩm định đầu vào, cấp quyền cho Seller tham gia vào **Xử lý Đơn hàng (4)** và **Marketing (9)**.
2. **Xử lý Đơn hàng (4)** kích hoạt **Thanh toán & Đối soát (5)** (khởi tạo giao dịch Escrow) và **Giao nhận & Vận chuyển (6)** (tạo vận đơn tracking).
3. Trường hợp bưu kiện giao hỏng/giao trễ trong **Giao nhận (6)** sẽ kích hoạt **Hoàn trả & Hoàn tiền (7)** hoặc **CSKH (8)**.
4. Nếu phát sinh xung đột không thể thỏa thuận ở **Hoàn trả (7)**, hệ thống tự động chuyển sang **Quản lý Tranh chấp & Rủi ro (2)** để hòa giải pháp lý.
5. **Marketing (9)** tương tác trực tiếp với **Quản lý Nhà bán hàng (1)** qua cơ chế thẩm định điều kiện seller tham gia campaign.

---

# Chương 3. MÔ HÌNH HÓA CHI TIẾT CÁC QUY TRÌNH BẰNG BPMN VÀ PHÂN TÍCH QUY TRÌNH

## 3.1. Tổng quan quy trình xử lý đơn hàng online Lazada

### 3.1.1. Phạm vi và mục tiêu
- **Phạm vi quy trình:** Bắt đầu khi Người mua (Buyer) nhấn nút "Đặt hàng" trên ứng dụng Lazada --> Kết thúc khi Người mua nhận hàng thành công và số tiền được giải ngân cho Người bán (Seller).
- **Mục tiêu:** Tối ưu thời gian xử lý đơn hàng, giảm thiểu thời gian chờ (Hold time), tăng tỷ lệ giao thành công ngay lần đầu tiên và giảm thiểu chi phí xử lý biên.

### 3.1.2. Sơ đồ SiPOC (Suppliers -- Inputs -- Process -- Outputs -- Customers)

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                         SƠ ĐỒ SiPOC XỬ LÝ ĐƠN HÀNG                           │
├──────────────┬──────────────┬────────────────────────┬──────────────┬───────────┤
│ SUPPLIERS    │ INPUTS       │ PROCESS                │ OUTPUTS      │ CUSTOMERS │
├──────────────┼──────────────┼────────────────────────┼──────────────┼───────────┤
│ • Buyers     │ • Thông tin  │ 1. Đặt hàng & Tiếp nhận│ • Đơn hàng   │ • Buyers  │
│ • Sellers    │   đơn hàng   │ 2. Người bán đóng gói  │   đã giao    │ • Sellers │
│ • Payment GW │ • Tiền thanh │ 3. Vận chuyển & Giao   │ • Tiền giải  │ • 3PL/LEX │
│ • LEX/3PL    │   toán/COD   │ 4. Hoàn tất & Đối soát │   ngân       │ • Finance │
│ • Lazada Sys │• Mã bưu kiện│                        │ • Đánh giá   │           │
└──────────────┴──────────────┴────────────────────────┴──────────────┴───────────┘
```
**Hình 3.1: Sơ đồ SiPOC quy trình xử lý đơn hàng online**

---

## 3.2. Mô tả chi tiết quy trình xử lý đơn hàng online

Quy trình diễn ra qua 4 giai đoạn chính:
1. **Giai đoạn 1: Đặt hàng và Tiếp nhận đơn:** Buyer chọn hàng, chọn phương thức thanh toán (COD ~40-45%, Online Payment ~55-60%), chọn ĐVVC và xác nhận đặt hàng. Lazada kiểm tra tồn kho và xử lý thanh toán (nếu trả trước).
2. **Giai đoạn 2: Người bán xử lý đơn:** Seller nhận thông báo đơn mới, kiểm tra tồn kho, xác nhận đơn (trong SLA 24-48h), chuẩn bị hàng, in phiếu giao, đóng gói và xác nhận "Chờ lấy hàng".
3. **Giai đoạn 3: Vận chuyển và Giao hàng:** Shipper 3PL/LEX nhận bưu kiện, chuyển về kho trung chuyển Sort Center, phân loại và giao chặng cuối cho Buyer. Tỷ lệ giao thất bại lần đầu: 20-25% (tương ứng tỷ lệ thành công 75-80%, thấp hơn trung bình ngành 82-88%).
4. **Giai đoạn 4: Hoàn tất và Đối soát:** Buyer nhận hàng thành công, hệ thống Escrow giải ngân cho Seller sau khi trừ phí sàn (L+2 model: funds available trong tài khoản Seller sau 1-2 ngày).

---

## 3.3. Mô hình BPMN quy trình xử lý đơn hàng online (AS-IS)

Sơ đồ BPMN 2.0 quy trình AS-IS đầy đủ gồm **5 Lanes (Buyer, Lazada System, Seller, 3PL/Shipper, Payment Gateway)**, **26 Tasks**, và **17 Cổng điều kiện (Gateways)** (đáp ứng tiêu chí >7 cổng phức tạp theo Rubric):

![Sơ đồ BPMN Quy trình Xử lý Đơn hàng Online AS-IS](docs/screenshots/03-order-processing-asis.png)  
**Hình 3.2: Sơ đồ BPMN quy trình xử lý đơn hàng online (AS-IS)**

```mermaid
flowchart TD
    Start([Start: Buyer chọn sản phẩm]) --> T1[Buyer bấm Đặt hàng & chọn PTTT]
    T1 --> G1{Phương thức thanh toán?}
    
    G1 -->|COD| T2[Hệ thống tạo đơn & chờ xử lý COD]
    G1 -->|Online Payment| T3[Payment Gateway xử lý giao dịch]
    G1 -->|Lazada Wallet| T3
    
    T3 --> G2{Thanh toán thành công?}
    G2 -->|Không| End1([Hủy đơn do lỗi thanh toán])
    G2 -->|Có| T4[Hệ thống tạo đơn & thông báo Seller]
    T2 --> T4
    
    T4 --> T5[Seller kiểm tra đơn & kho hàng]
    T5 --> G3{Seller accept hay reject?}
    G3 -->|Reject| T6[Seller bấm Hủy đơn] --> End2([Hủy đơn do hết hàng])
    G3 -->|Hết SLA 24-48h| T7[Hệ thống Auto-cancel] --> End2
    
    G3 -->|Accept| T8[Seller đóng gói & in waybill]
    T8 --> G4{Phương thức Fulfillment?}
    
    G4 -->|FBL - Kho Lazada| T9[Warehouse nhận & QC inspection]
    G4 -->|FBS - Seller tự giao| T10[LEX/3PL Pickup tại kho Seller]
    
    T9 --> G5{QC Pass/Fail?}
    G5 -->|Fail| T11[Trả hàng về Seller / Hủy kiện] --> End3([End: kiện bị từ chối])
    G5 -->|Pass| T12[Warehouse Pack + Label]
    T12 --> T13[Handoff cho LEX/3PL]
    
    T10 --> T14[3PL Scan nhận tại Hub]
    T13 --> T14
    
    T14 --> T15[In-transit: Trung chuyển qua Sort Center]
    T15 --> T16[Line-haul đến Last-mile Hub]
    T16 --> T17[Shipper giao hàng chặng cuối]
    
    T17 --> G6{Delivery attempt thành công?}
    G6 -->|Thất bại| G7{Đã giao 3 lần?}
    G7 -->|Chưa| T17
    G7 -->|Rồi| T18[Chuyển hoàn bưu kiện về Seller] --> End4([End: Giao thất bại])
    
    G6 -->|Thành công| G8{COD hay Online?}
    G8 -->|COD| T19[Shipper thu tiền COD] --> T20[Cập nhật Delivered]
    G8 -->|Online| T20
    
    T20 --> T21[Buyer confirm nhận / Auto-confirm 7 ngày]
    T21 --> G9{Buyer khiếu nại?}
    G9 -->|Có| T22[Chuyển Quy trình Hoàn trả/Refund]
    G9 -->|Không| T23[Escrow Release & Settlement]
    T23 --> T24[Trừ commission + phí → Giải ngân Ví Seller]
    T24 --> End5([End: Giao dịch hoàn tất])
```

> **Ghi chú:** Sơ đồ luồng tổng quan trên mô tả toàn chuỗi fulfillment (bao gồm các bước kho bãi/hub chi tiết thuộc Quy trình 9 — Logistics & Giao nhận). File BPMN chính thức ở Hình 3.2 giới hạn trong phạm vi Quy trình 3 — Xử lý Đơn hàng (Buyer → Seller → 3PL pickup → giao → settlement), với 26 Tasks và 17 Gateways khớp số liệu ở Bảng 3.1.
>
> **Ghi chú chung về sơ đồ mermaid:** Các sơ đồ luồng mermaid tại Mục 3.6–3.14 là **sơ đồ tổng quan ở mức nghiệp vụ (executive overview)** — gom các cổng gom luồng (join), cổng phụ và chi tiết lane/timer để minh họa luồng xử lý chính. **Số liệu chính thức** (số Tasks, Gateways, End Events, Lanes) lấy từ file BPMN 2.0 gốc và được nêu đầy đủ ở dòng thống kê ngay trên mỗi hình (khớp file BPMN trong `processes/` và `processes-to-be/`); các mermaid minh họa không thay thế file BPMN làm nguồn tham chiếu định lượng.

**Bảng 3.1: Thống kê các thành phần sơ đồ BPMN Xử lý Đơn hàng**

| Thành phần | Số lượng | Chi tiết |
|------------|----------|----------|
| **Lanes (Làn)** | 5 | Buyer, Lazada System, Seller, 3PL/Shipper, Payment Gateway (các hoạt động kho bãi/hub thuộc Quy trình 9 — Logistics) |
| **Activities (Tác vụ)** | 26 | Tác vụ thủ công và tác vụ hệ thống tự động |
| **Gateways (Cổng rẽ nhánh)** | 17 | 17 Cổng XOR Split & Join (Vượt tiêu chí >7 cổng của Rubric) |
| **Events (Sự kiện)** | 4 | 1 Start Event + 3 End Events (các nhánh kết thúc của quy trình) |

---

## 3.4. Phân tích Định tính & Nguyên nhân Gốc rễ

### 3.4.1. Phân tích Giá trị Gia tăng (VA / BVA / NVA Analysis)

**Bảng 3.2: Bảng phân tích Giá trị gia tăng quy trình Xử lý Đơn hàng**

| STT | Hoạt động (Task) | Người thực hiện | Loại giá trị | Giải thích lý do | Đề xuất khắc phục |
|-----|------------------|-----------------|--------------|------------------|-------------------|
| 1 | Đặt hàng & chọn PTTT | Buyer | **VA** | Trực tiếp thể hiện nhu cầu mua sắm của khách | Tối ưu UI/UX 1-click checkout |
| 2 | Kiểm tra thanh toán online | System/GW | **BVA** | Đảm bảo an toàn tài chính cho giao dịch | Tự động hóa 100% qua API |
| 3 | Warehouse QC inspection | Warehouse | **BVA** | Đảm bảo đúng SKU & số lượng trước khi giao | Tự động scan barcode giảm thủ công |
| 4 | Chờ Seller xác nhận (max 48h) | Seller | **NVA** | Thời gian chờ chết không tạo giá trị cho khách | Auto-confirm cho Shop uy tín (Diamond/Gold) |
| 5 | In phiếu & Đóng gói hàng | Seller | **VA** | Đảm bảo sản phẩm an toàn đến tay khách | Chuẩn hóa quy cách bao bì |
| 6 | Gửi hàng tại bưu cục/Pickup | Seller/Shipper | **BVA** | Cần thiết để bàn giao bưu kiện | Tối ưu tuyến đường gom hàng |
| 7 | Quét mã & Vận chuyển qua Hub | LEX/3PL | **BVA** | Luân chuyển bưu kiện qua các hub | Tự động hóa băng chuyền phân loại |
| 8 | Chờ giao hàng chặng cuối | Shipper | **NVA** | Khách vắng mặt / Không nghe máy gây chờ | Nhắn tin trước / Chọn khung giờ |
| 9 | Giao hàng & Thu tiền COD | Shipper | **VA** | Hoàn tất giao nhận & trao giá trị sản phẩm | Khuyến khích thanh toán không tiền mặt |
| 10 | Chờ auto-confirm (7 ngày) | System | **NVA** | Dọng vốn Seller không cần thiết | Rút ngắn còn 24-72h đối với Shop uy tín |
| 11 | Đối soát & Giải ngân (L+2) | Finance/System | **BVA** | Quyết toán dòng tiền cho Seller | Auto-payout ngay khi giao xong cho Shop Diamond |

---

### 3.4.2. Phân tích Lãng phí (Waste Analysis: Move / Hold / Overdo)

**Bảng 3.3: Bảng phân tích Lãng phí quy trình Xử lý Đơn hàng**

| STT | Loại lãng phí | Hoạt động phát sinh | Biểu hiện thực tế | Giải pháp khắc phục |
|-----|---------------|---------------------|-------------------|---------------------|
| 1 | **Hold (Chờ đợi)** | Chờ Seller xác nhận đơn | Seller không vào app xác nhận trong 24-48h, auto-cancel rate cao | Tự động xác nhận cho Shop tier cao; Push notification kết hợp SMS |
| 2 | **Hold (Chờ đợi)** | Chờ giao hàng chặng cuối | Shipper đến nhưng khách vắng mặt (15-20%) -- tỷ lệ COD refusal cao | Khảo sát chọn khung giờ giao; Xác nhận đơn trước khi ship |
| 3 | **Hold (Chờ đợi)** | Chờ Escrow Release & Settlement | Giữ tiền Escrow 7 ngày + L+2 settlement cycle | Rút ngắn time-to-payout cho Shop uy tín |
| 4 | **Move (Di chuyển)** | Qua nhiều node kho | Bưu kiện chuyển qua 4-5 trạm trung chuyển | Xây dựng Kho Vùng phân loại tập trung |
| 5 | **Overdo (Quá mức)** | Kiểm tra gian lận thủ công | Duyệt tay các đơn nghi ngờ boom hàng COD | Áp dụng Machine Learning chấm điểm rủi ro đơn hàng |

---

### 3.4.3. Biểu đồ Pareto (80/20 Rule Analysis)

Áp dụng quy tắc Pareto 80/20 để phân tích các nhóm lãng phí chính trong quy trình xử lý đơn hàng:

```
+-----------------------------------------------------------------------------------+
|      BIỂU ĐỒ PARETO PHÂN BỐ CHI PHÍ LÃNG PHÍ QUY TRÌNH XỬ LÝ ĐƠN HÀNG            |
+-----------------------------------------------------------------------------------+
| Tỷ lệ %                                                                           |
| 100% |                                                            *(100%)         |
|  90% |--------------------------------------------------*(87%)--+                 |
|  80% |                                          *(70.6%)        | [Pareto 80%]  |
|  44% |  [████████████]                                            |               |
|  27% |  [████████████]            [████████████]                  |               |
|  16% |  [████████████]            [████████████]    [████████████]|               |
|   9% |  [████████████]            [████████████]    [████████████]| [████████████]|
|   0% +----------------------------------------------------------------------------+
|        Seller xác nhận       Auto-confirm       Giao lại          Buyer hủy      |
|        chậm + hủy đơn         7 ngày            nhiều lần           đổi ý        |
|             44,1%                 26,5%            16,2%             8,8%        |
+-----------------------------------------------------------------------------------+
```
**Hình 3.3: Biểu đồ Pareto phân bố chi phí lãng phí quy trình xử lý đơn hàng**

- **Nhận xét Pareto:** **~87% tổng chi phí lãng phí** (~590 tỷ VND/tháng) tập trung ở 3 nhóm nguyên nhân chính: **Seller xác nhận chậm + hủy đơn (44,1%)**, **Auto-confirm 7 ngày kéo dài thời gian giải ngân (26,5%)** và **Giao lại nhiều lần (16,2%)** (Bảng Vấn đề–Giả thuyết–Chi phí, docs/analysis/03 §3.3.5). Theo quy tắc Pareto 80/20, ưu tiên xử lý 3 nhóm này để giành phần lớn hiệu quả giảm lãng phí.
- **Ghi chú phân loại:** Phân bố trên tính theo **chi phí ảnh hưởng/tháng** (lost GMV + rework + cash flow lock). Xét riêng phân loại thời gian (Waste Analysis Move/Hold/Overdo), Hold chiếm 83% thời gian chờ do Seller xác nhận 48h + auto-confirm 7 ngày.

---

### 3.4.4. Phân tích Nguyên nhân Gốc rễ (Fishbone & 5-Why Analysis)

#### Sơ đồ Fishbone #1: Tỷ lệ giao hàng thất bại lần đầu cao (20-25%)
- **Con người (Man):** Shipper không gọi trước khi giao; Buyer COD đổi ý không muốn nhận hàng (tỷ lệ COD refusal chiếm phần lớn).
- **Quy trình (Process):** Không cho chọn khung giờ giao cụ thể; Quy trình giao lại (re-delivery) không hẹn giờ trước; Thiếu cơ chế xác nhận đơn trước khi ship.
- **Công nghệ (Technology):** Địa chỉ Buyer nhập không chính xác (thiếu số nhà/ngõ); App chưa có tính năng định vị thời gian thực của Shipper; Chatbot CSKH xử lý sai vấn đề shipping.
- **Môi trường (Environment):** Thời tiết mưa bão; Tắc đường giờ cao điểm tại các đô thị lớn.

#### Phân tích 5-Why #1: Tại sao Seller chậm xác nhận đơn hàng >24 giờ?
1. *Why 1:* Tại sao Seller không xác nhận đơn hàng ngay? --> *Vì Seller không biết có đơn hàng mới.*
2. *Why 2:* Tại sao Seller không biết? --> *Vì không nhận được thông báo hoặc không mở Seller Center.*
3. *Why 3:* Tại sao không mở Seller Center? --> *Vì Seller nhỏ lẻ bán bán thời gian, không có nhân sự trực 24/7.*
4. *Why 4:* Tại sao hệ thống không tự xác nhận? --> *Vì cơ chế bắt buộc Seller phải bấm xác nhận thủ công để chốt tồn kho.*
5. *Why 5 (Root Cause):* **Cơ chế xác nhận đơn chưa linh hoạt -- ưu tiên thao tác thủ công thay vì tự động hóa theo phân hạng rủi ro gian hàng.**

#### Phân tích 5-Why #2: Tại sao tỷ lệ COD refusal cao (15-20%)?
1. *Why 1:* Tại sao Buyer từ chối nhận hàng COD? --> *Vì Buyer đổi ý hoặc tìm được giá tốt hơn trên sàn khác.*
2. *Why 2:* Tại sao Buyer dễ dàng đổi ý? --> *Vì không có cơ chế xác nhận cam kết nhận hàng trước khi ship.*
3. *Why 3:* Tại sao Lazada không áp dụng xác nhận? --> *Vì COD là phương thức chủ đạo (~40-45%) và muốn giữ trải nghiệm mua hàng dễ dàng.*
4. *Why 4:* COD refusal gây hậu quả gì? --> *Chi phí reverse logistics, lãng phí thời gian shipper, giảm seller score.*
5. *Why 5 (Root Cause):* **Thiếu cơ chế xác nhận cam kết nhận hàng trước khi xử lý đơn COD, kết hợp với chính sách hoàn tiền dễ dàng tạo động cơ "boom hàng".**

#### Sơ đồ Fishbone #2: Thời gian hoàn tiền kéo dài 8,5 ngày (chậm ~3 lần so với benchmark 2-3 ngày)
- **Con người (Man):** Nhân viên kho kiểm định từng kiện hoàn trả thủ công (không có AI so sánh ảnh); CS phải xem xét bằng chứng không có cấu trúc trước khi duyệt.
- **Quy trình (Process):** Pickup hàng trả theo lịch cố định, thất bại phải đặt lại lịch (+1-2 ngày); reverse logistics 1-2 ngày; kích hoạt lệnh hoàn tiền thủ công 1-6 giờ sau khi kiểm định pass.
- **Công nghệ (Technology):** Chưa áp dụng Instant Refund rộng rãi (chỉ đơn <200k & tín nhiệm cao); hoàn tiền về thẻ/bank mất 5-15 ngày làm việc theo chu kỳ bank/gateway; chưa có AI phân loại tự động hỗ trợ kiểm định kho.
- **Môi trường (Environment):** Quy định/bank clearing cycle phụ thuộc bên thứ ba; giờ hoạt động của kho và 3PL giới hạn theo ca.

#### Phân tích 5-Why #3: Tại sao hoàn tiền trung bình mất 8,5 ngày?
1. *Why 1:* Tại sao hoàn tiền mất 8,5 ngày? --> *Vì phải chờ pickup, vận chuyển ngược, kiểm định kho rồi mới kích hoạt hoàn tiền.*
2. *Why 2:* Tại sao phải chờ kiểm định kho? --> *Vì phải xác nhận hàng về đúng hiện trạng mới dám hoàn tiền, nhưng kiểm định thủ công 4-12 giờ mỗi kiện.*
3. *Why 3:* Tại sao kiểm định chậm? --> *Vì nhân viên kho kiểm tra manual từng mục, không có AI so sánh ảnh hỗ trợ.*
4. *Why 4:* Tại sao không đầu tư AI so sánh ảnh? --> *Vì chi phí đầu tư warehouse tooling cao và chưa được ưu tiên so với các dự án khác, cộng với rủi ro fraud khi hoàn tiền sớm.*
5. *Why 5 (Root Cause):* **Quy trình hoàn tiền phụ thuộc tuyến tính vào reverse logistics + kiểm định kho thủ công (8h) + kích hoạt lệnh thủ công (1-6h) mà chưa có Instant Refund cho nhóm rủi ro thấp và chưa AI hóa kiểm định — gây thời gian chu kỳ 8,5 ngày, gấp ~3 lần benchmark ngành (2-3 ngày).**

---

## 3.5. Phân tích Định lượng Quy trình Xử lý Đơn hàng Online

### 3.5.1. Phân tích Thời gian Chu kỳ (Probability-Weighted Cycle Time)

**Bảng 3.4: Bảng tính toán Thời gian chu kỳ các giai đoạn trong quy trình**

| Giai đoạn | Thời gian xử lý thực (PT) | Thời gian chờ (WT) | Thời gian chu kỳ (CT) | Trọng số xác suất | CT có trọng số |
|-----------|---------------------------|--------------------|-----------------------|-------------------|----------------|
| **1. Đặt hàng & Xác minh** | 5 phút (0,08h) | 10 phút (0,17h) | 0,25 giờ | 100% | 0,25 giờ |
| **2. Seller xác nhận & Đóng gói** | 20 phút (0,33h) | 14,0 giờ | 14,33 giờ | 100% | 14,33 giờ |
| **3. Warehouse QC & Packing (FBL)** | 15 phút (0,25h) | 4,0 giờ | 4,25 giờ | 40% | 1,70 giờ |
| **4. Vận chuyển chặng đầu & Hub** | 30 phút (0,50h) | 18,0 giờ | 18,50 giờ | 100% | 18,50 giờ |
| **5. Phân loại Sort Center & Linehaul** | 15 phút (0,25h) | 24,0 giờ | 24,25 giờ | 100% | 24,25 giờ |
| **6. Giao chặng cuối (Thành công 1st)** | 15 phút (0,25h) | 4,0 giờ | 4,25 giờ | 80% | 3,40 giờ |
| **7. Giao lại chặng cuối (Lần 2/3)** | 30 phút (0,50h) | 24,0 giờ | 24,50 giờ | 20% | 4,90 giờ |
| **8. Đối soát & Chờ giải ngân** | 5 phút (0,08h) | 36,0 giờ | 36,08 giờ | 100% | 36,08 giờ |
| **TỔNG CỘNG QUY TRÌNH (đến giao thành công, happy path)** | **2,24 giờ** | **124,17 giờ** | **126,41 giờ** | **-** | **103,41 giờ (~4,31 ngày)** |

- **Chỉ số Hiệu suất Thời gian (Process Time Efficiency - PTE):**
  PTE = (Tong PT / Tong CT) x 100% = (2,24 / 126,41) x 100% = 1,77%
- **Nhận xét:** **98,23% thời gian quy trình là thời gian chờ lãng phí (WT)**, chỉ có 1,77% thời gian là thực sự thao tác tạo giá trị. Đặc biệt, thời gian chờ giải ngân L+2 chiếm tỷ trọng lớn trong phase cuối.

---

### 3.5.2. Phân tích Chi phí (Unit Economics per Order)

**Bảng 3.5: Bảng phân bổ Chi phí xử lý biên 1 đơn hàng thành công (Đơn giá trung bình 280.000 VNĐ)**

| Thành phần chi phí | Chi phí (VNĐ) | Tỷ lệ % / Giá trị đơn | Ghi chú giải thích |
|--------------------|---------------|-----------------------|--------------------|
| Chi phí Hạ tầng IT & Băng thông | 900 VNĐ | 0,32% | Máy chủ Alibaba Cloud, API Gateway |
| Chi phí Đóng gói (Seller chịu) | 5.000 VNĐ | 1,79% | Hộp carton, băng dính, xốp nổ, phiếu in |
| Chi phí Vận chuyển Chặng đầu (Pickup) | 5.500 VNĐ | 1,96% | Shipper LEX/3PL gom hàng về Hub |
| Chi phí Phân loại Sort Center | 2.800 VNĐ | 1,00% | Vận hành máy chia chọn tự động |
| Chi phí Vận chuyển Chặng cuối (Last-mile) | 15.000 VNĐ | 5,36% | Trả công Shipper giao hàng |
| Chi phí Xử lý Thanh toán (Payment GW) | 4.000 VNĐ | 1,43% | Phí cổng VNPay / OnePay / MoMo |
| Chi phí Dự phòng Giao hỏng / COD refusal | 3.500 VNĐ | 1,25% | Chi phí xử lý khiếu nại + reverse logistics |
| Chi phí CSKH / Khiếu nại phân bổ | 2.200 VNĐ | 0,79% | Phân bổ chi phí CS theo đơn |
| **TỔNG CHI PHÍ VẬN HÀNH BIÊN (Unit Cost)** | **38.900 VNĐ** | **13,89%** | **Chi phí vận hành trực tiếp / đơn** |

---

## 3.6. Quy trình Quản lý Nhà bán hàng (Management #1)

### 3.6.1. Mô tả quy trình
Quy trình thẩm định hồ sơ Seller mới đăng ký (eKYC + OCR), phân hạng Shop (Standard, Gold, Diamond, LazMall), và quản lý hệ thống vi phạm (Warning --> Delist --> Suspended --> Deactivated --> Re-register).

### 3.6.2. Mô hình BPMN & Thống kê
Sơ đồ BPMN 2.0 Quản lý Nhà bán hàng gồm **4 Lanes (Seller, Lazada System, Compliance Team, Legal/Giám sát Vận hành)**, **14 Tasks**, **15 Gateways** (XOR — exclusiveGateway thuần):

![Sơ đồ BPMN Quy trình Quản lý Nhà bán hàng AS-IS](docs/screenshots/01-seller-management-asis.png)  
**Hình 3.4: Sơ đồ BPMN quy trình quản lý nhà bán hàng (AS-IS)**

```mermaid
flowchart TD
    S_SM([Start: Yêu cầu đăng ký gian hàng]) --> T_SM1[Điền thông tin định danh Seller]
    T_SM1 --> G_SM1{SĐT đã xác thực?}
    G_SM1 -->|Chưa xác thực| T_SM2[Gửi OTP xác thực SĐT] --> J_SM1((Gom luồng trước Upload))
    G_SM1 -->|Đã xác thực| J_SM1
    J_SM1 --> T_SM3[Upload CMND/CCCD + GPKD + Giấy chứng nhận (LazMall)]
    T_SM3 --> J_SM2((Gom luồng trước Validate)) --> T_SM4[Validate định danh tự động]
    T_SM4 --> G_SM2{Tài khoản NH hợp lệ?}
    G_SM2 -->|Không hợp lệ| T_SM5[Cập nhật tài khoản ngân hàng (giải ngân)] --> J_SM3((Gom luồng trước OCR))
    G_SM2 -->|Hợp lệ| J_SM3
    J_SM3 --> T_SM6[Quét OCR + kiểm tra giấy tờ giả]
    T_SM6 --> G_SM3{Giấy tờ hợp lệ?}
    G_SM3 -->|Hợp lệ| T_SM7[Chấm điểm rủi ro (Risk scoring)]
    G_SM3 -->|Không hợp lệ| J_SM4((Gom luồng trước Bổ sung hồ sơ)) --> T_SM8[Bổ sung / sửa hồ sơ]
    T_SM7 --> G_SM4{Có nghi vấn rủi ro cao?}
    G_SM4 -->|Không| G_SM5{Phân tầng rủi ro?}
    G_SM4 -->|Có nghi vấn| J_SM5((Gom luồng trước Compliance review))
    G_SM5 -->|Manual review| J_SM5
    G_SM5 -->|Auto duyệt| J_SM6((Gom luồng trước Thông báo))
    G_SM5 -->|Từ chối| J_SM4
    J_SM5 --> T_SM9[Compliance review thủ công (24-48h)] --> G_SM6{Kết quả thẩm định?}
    G_SM6 -->|Duyệt| J_SM6
    G_SM6 -->|Từ chối| J_SM6
    G_SM6 -->|Yêu cầu sửa hồ sơ| J_SM4
    T_SM8 --> G_SM7{Còn lượt sửa hồ sơ?}
    G_SM7 -->|Còn lượt| J_SM2
    G_SM7 -->|Hết lượt| End_SM5([End: Hồ sơ đã bị từ chối vĩnh viễn])
    J_SM6 --> T_SM10[Thông báo kết quả duyệt Seller Centre] --> G_SM8{Phân luồng sau thông báo?}
    G_SM8 -->|Kích hoạt gian hàng| End_SM1([End: Gian hàng Lazada đã được kích hoạt])
    G_SM8 -->|Giám sát vi phạm| T_SM11[Giám sát điểm đánh giá & vi phạm (auto)] --> G_SM9{Mức độ vi phạm?}
    G_SM9 -->|Nhẹ| T_SM12[Gửi cảnh cáo Seller] --> End_SM2([End: Gian hàng đã bị cảnh cáo])
    G_SM9 -->|Trung bình| T_SM13[Tạm khóa gian hàng (7 ngày)] --> End_SM3([End: Gian hàng đã bị tạm khóa])
    G_SM9 -->|Nghiêm trọng| T_SM14[Khóa gian hàng vĩnh viễn] --> End_SM4([End: Gian hàng đã bị khóa vĩnh viễn])
```

**Bảng 3.6: Phân tích Định tính & Định lượng Quản lý Nhà bán hàng**

| Hạng mục phân tích | Chi tiết kết quả |
|--------------------|------------------|
| **Tỷ lệ VA / BVA / NVA** | VA: 29%, BVA: 71%, NVA: 0% (không có hoạt động lãng phí thuần; BVA chủ yếu là các bước compliance/kiểm soát cần thiết, bottleneck chính là Compliance review thủ công 24-48h). |
| **Điểm nghẽn (Bottleneck)** | Compliance review thủ công 24-48h (85% hồ sơ vào manual queue); Phê duyệt thủ công giấy phép kinh doanh & giấy ủy quyền thương hiệu đối với LazMall. |
| **Thời gian chu kỳ (Cycle Time)** | Trung bình 40 giờ (~5 ngày làm việc, theo trọng số xác suất; tối thiểu 15 phút auto-check --> tối đa 5 ngày manual review). |
| **Chi phí thẩm định / Seller** | 24.500 VNĐ / hồ sơ đăng ký (gồm eKYC 2.000, tải hồ sơ 15.000, OTP SMS 500, đối soát giấy phép 1.000, lưu trữ 6.000 VNĐ). |

---

## 3.7. Quy trình Quản lý Tranh chấp và Rủi ro (Management #2)

### 3.7.1. Mô tả quy trình
Quy trình giải quyết các vụ việc khiếu nại phức tạp, nghi vấn gian lận COD, boom hàng hàng loạt hoặc tranh chấp pháp lý giữa Buyer và Seller.

### 3.7.2. Mô hình BPMN & Thống kê
Sơ đồ BPMN 2.0 Quản lý Tranh chấp gồm **5 Lanes (Buyer, Lazada System (Automated), Seller, CS Agent, Escalation Team)**, **12 Tasks**, **16 Gateways** (toàn bộ XOR — exclusiveGateway):

![Sơ đồ BPMN Quy trình Quản lý Tranh chấp AS-IS](docs/screenshots/02-dispute-management-asis.png)  
**Hình 3.5: Sơ đồ BPMN quy trình quản lý tranh chấp và rủi ro (AS-IS)**

```mermaid
flowchart TD
    S_DM([Start: Yêu cầu giải quyết tranh chấp]) --> T_DM1[Tạo tranh chấp + lý do]
    T_DM1 --> T_DM2[Tự động thu thập dữ liệu đơn hàng]
    T_DM2 --> T_DM3[AI phân loại tranh chấp (Đơn giản/Phức tạp)]
    T_DM3 --> G_DM0{Phân luồng sau AI phân loại}
    G_DM0 --> G_DM1{Vụ việc thuộc nhóm đơn giản?}
    G_DM0 --> G_DM2{Seller từng vi phạm SLA?}
    G_DM1 -->|Nhóm đơn giản| End_DM3([End: Tranh chấp đã được AI tự giải quyết])
    G_DM2 -->|Có vi phạm| J_DM1((Gom luồng trước Thông báo đối soát))
    G_DM2 -->|Chưa vi phạm| T_DM4[Kiểm tra lịch sử SLA] --> J_DM1
    J_DM1 --> T_DM5[Gửi thông báo đối soát đến hai bên]
    T_DM5 --> G_DM3{Seller phản hồi trong 48h?}
    G_DM3 -->|Không phản hồi| J_DM4((Gom nhánh kết thúc))
    G_DM3 -->|Phản hồi| T_DM6[Seller phản hồi (≤48h)] --> G_DM4{Phân luồng sau phản hồi?}
    G_DM4 -->|Đủ hồ sơ| J_DM2((Gom luồng trước CS thẩm định))
    G_DM4 -->|Cần bổ sung bằng chứng| J_DM3((Gom luồng trước Bổ sung bằng chứng))
    J_DM3 --> T_DM7[Bổ sung bằng chứng (nếu có)] --> G_DM5{Có bằng chứng cứng?}
    G_DM5 -->|Có| G_DM6{Bằng chứng đã đầy đủ & hợp lệ?}
    G_DM5 -->|Không| J_DM5((Gom luồng trước Yêu cầu bổ sung))
    G_DM6 -->|Đầy đủ| J_DM2
    G_DM6 -->|Chưa đầy đủ| J_DM5
    J_DM5 --> T_DM8[Yêu cầu bổ sung bằng chứng] --> J_DM3
    J_DM2 --> T_DM9[CS thẩm định toàn bộ hồ sơ tranh chấp] --> T_DM10[CS ban hành quyết định xử lý]
    T_DM10 --> G_DM7{Phân luồng sau quyết định?}
    G_DM7 --> G_DM8{Buyer thắng?}
    G_DM7 --> G_DM9{Đồng thuận?}
    G_DM7 --> T_DM11[Chuyển lên nhóm chuyên trách (Lazada Escalation)]
    G_DM8 -->|Buyer thắng| J_DM4
    G_DM8 -->|Không| End_DM2([End: Tranh chấp đã bị bác bỏ])
    G_DM9 -->|Đồng thuận| J_DM4
    G_DM9 -->|Không đồng thuận| T_DM11
    T_DM11 --> T_DM12[Hội đồng thẩm định & ra quyết định cuối] --> G_DM10{Quyết định cuối?} --> J_DM4
    J_DM4 --> End_DM1([End: Tranh chấp đã được giải quyết])
```

**Bảng 3.7: Phân tích Định tính & Định lượng Quản lý Tranh chấp**

| Hạng mục phân tích | Chi tiết kết quả |
|--------------------|------------------|
| **Tỷ lệ VA / BVA / NVA** | VA: 50%, BVA: 50%, NVA: 0% (không có hoạt động lãng phí thuần; BVA là các bước auditing/kiểm soát cần thiết, gây delay do gửi bằng chứng qua lại nhiều vòng). |
| **Điểm nghẽn (Bottleneck)** | Quá trình thu thập bằng chứng chưa chuẩn hóa; hình ảnh mở hộp bị mờ/thiếu thông tin. |
| **Thời gian chu kỳ (Cycle Time)** | Trung bình 5,2 ngày (Vụ phức tạp leo thang lên đến 14 ngày). |
| **Chi phí xử lý / Ca tranh chấp** | 68.000 VNĐ / vụ việc. |

---

## 3.8. Quy trình Hoàn trả và Hoàn tiền (Core #4)

### 3.8.1. Mô tả quy trình
Xử lý các yêu cầu trả hàng/hoàn tiền khi hàng vỡ hỏng, sai mẫu, không nhận được hàng hoặc Buyer đổi ý. Phân biệt 3 loại: Full Return, Partial Refund, Only Refund.

### 3.8.2. Sơ đồ BPMN quy trình Hoàn trả & Hoàn tiền
Sơ đồ BPMN AS-IS gồm **5 Lanes (Buyer, Lazada System, CS Agent, 3PL/Warehouse, Payment Gateway)**, **13 Tasks**, **18 Gateways**; mô hình TO-BE tối ưu tại Mục 3.15.2 gồm **16 Tasks**, **9 Gateways** (thêm 3 cổng AI: kiểm tra mức độ tin cậy của AI xác thực lỗi, kiểm tra pickup thành công và kiểm tra giải ngân thành công; lược giản 3 cổng kiểm tra thủ công — thời hạn hoàn trả, chất lượng bằng chứng và kiểm định hàng):

![Sơ đồ BPMN Quy trình Hoàn trả và Hoàn tiền AS-IS](docs/screenshots/04-return-refund-asis.png)  
**Hình 3.6: Sơ đồ BPMN quy trình hoàn trả và hoàn tiền (AS-IS)**

```mermaid
flowchart TD
    S_RR([Start: Buyer yêu cầu hoàn trả hàng]) --> T_RR1[Buyer gửi yêu cầu đổi trả và lý do]
    T_RR1 --> G_RR1{Còn trong thời gian hoàn trả?}
    G_RR1 -->|Trễ hạn| T_RR2[Xử lý yêu cầu trễ hạn] --> J_RR1[Gom luồng]
    G_RR1 -->|Trong hạn| J_RR1
    J_RR1 --> T_RR3[Kiểm tra tính hợp lệ tự động]
    
    T_RR3 --> G_RR2{Hợp lệ?}
    G_RR2 -->|Không| End_RR2([End: Yêu cầu hoàn trả bị từ chối])
    G_RR2 -->|Có| T_RR4[Buyer tải lên bằng chứng ảnh & video]
    
    T_RR4 --> T_RR5[AI phân loại bằng chứng khiếu nại]
    T_RR5 --> G_RR3{Bằng chứng đạt yêu cầu? & AI đủ tin cậy}
    G_RR3 -->|Ảnh mờ/Thiếu sót| T_RR4
    G_RR3 -->|Đạt| J_RR2[Gom luồng] --> T_RR6[CS thẩm định hồ sơ khiếu nại]
    
    T_RR6 --> G_RR4{CS phê duyệt yêu cầu đổi trả?}
    G_RR4 -->|Từ chối| End_RR2
    G_RR4 -->|Duyệt| G_RR5{Đơn <200k & Buyer tín nhiệm cao?}
    
    G_RR5 -->|Có − Return-less refund| J_RR3[Gom luồng trước Kích hoạt hoàn tiền]
    G_RR5 -->|Không − Cần trả hàng| T_RR7[Buyer bàn giao hàng trả cho LEX/3PL]
    T_RR7 --> T_RR8[Đặt lịch Shipper đến lấy hàng hoàn]
    
    T_RR8 --> T_RR9[LEX/3PL pickup hàng trả]
    T_RR9 --> G_RR6{Pickup thành công?}
    G_RR6 -->|Thất bại| T_RR10[Đặt lại lịch pickup] --> T_RR9
    G_RR6 -->|Thành công| T_RR11[Kiểm định hàng hoàn tại kho ≤12h]
    T_RR11 --> G_RR7{Hàng hoàn đúng hiện trạng & đủ điều kiện?}
    G_RR7 -->|Không đạt| End_RR2
    G_RR7 -->|Đạt| J_RR3
    
    J_RR3 --> T_RR12[Kích hoạt lệnh hoàn tiền]
    T_RR12 --> G_RR8{Phương thức hoàn tiền?}
    G_RR8 -->|Ví Lazada Wallet| J_RR4[Gom luồng]
    G_RR8 -->|Thẻ/Bank| J_RR4
    J_RR4 --> T_RR13[Gửi thông báo cập nhật tiến độ tự động] --> End_RR1([End: Đã hoàn tiền cho Buyer])
```

### 3.8.3. Phân tích Định tính & Định lượng Quy trình Hoàn trả & Hoàn tiền

**Bảng 3.8: Phân tích Giá trị Gia tăng (VA/BVA/NVA) — 13 hoạt động của quy trình**

| STT | Hoạt động | VA | BVA | NVA | Giải thích | Đề xuất TO-BE |
|-----|-----------|----|-----|-----|------------|---------------|
| 1 | Gửi yêu cầu đổi trả và lý do | ✓ | | | Nhu cầu chính đáng của KH | Guided form + lý do chuẩn hóa |
| 2 | Tải lên bằng chứng ảnh và video | ✓ | | | Bằng chứng cần thiết cho quyết định | Checklist guided + AI quality check |
| 3 | Xử lý yêu cầu trễ hạn | | ✓ | | Xử lý ngoại lệ khi KH bỏ lỡ deadline | Auto-extend 1 lần, nhắc reminder |
| 4 | Bàn giao hàng trả cho LEX / 3PL | ✓ | | | Bắt đầu logistics ngược | Drop-off point + QR code |
| 5 | CS thẩm định hồ sơ khiếu nại | | ✓ | | Cần cho fair decision — Hold lớn | **AI triage evidence** + CS chỉ review ngoại lệ |
| 6 | Kiểm định hàng hoàn tại kho (≤12h) | | | ✓ | Inspection thủ công tại kho — waste (bỏ qua khi return-less <200k) | **Return-less refund** low-risk + AI image analysis |
| 7 | Kiểm tra tính hợp lệ tự động | | ✓ | | Lọc yêu cầu không hợp lệ — chống lạm dụng | Auto instant; mở rộng luật |
| 8 | AI phân loại bằng chứng khiếu nại | | ✓ | | Phân loại nhanh — rút ngắn thời gian xử lý | Mở rộng auto-approve path |
| 9 | Gửi thông báo cập nhật tiến độ tự động | ✓ | | | KH theo dõi trạng thái — minh bạch | Giữ nguyên (auto) |
| 10 | Đặt lịch hẹn Shipper đến lấy hàng hoàn | ✓ | | | Lên lịch pickup — giảm Hold | Smart scheduling + drop-off point |
| 11 | Đặt lại lịch pickup | | ✓ | | Xử lý ngoại lệ (KH bận) | Tự động đề xuất 3 slot kế tiếp |
| 12 | Kích hoạt lệnh hoàn tiền | | | ✓ | Hoàn tiền thủ công sau khi đã duyệt — waste (nhiều bước click) | Auto-execute refund qua payment gateway |
| 13 | LEX / 3PL pickup hàng trả | ✓ | | | Vận chuyển hàng trả — logistics ngược | Scheduled pickup slot (giảm Hold 4-24h) |

**Tỷ lệ VA/BVA/NVA:** VA **6/13 (46%)**, BVA **5/13 (39%)**, NVA **2/13 (15%)** — NVA tập trung ở kiểm định kho thủ công và kích hoạt lệnh hoàn tiền thủ công, đúng 2 hoạt động mà mô hình TO-BE tự động hóa (Mục 3.15.2), đưa NVA về gần 0.

**Bảng 3.9: Bảng tính toán Thời gian chu kỳ và Chi phí xử lý 1 đơn Hoàn trả (Refund Unit Economics)**

| Chỉ số Định lượng | Giá trị hiện tại (AS-IS) | Giá trị mục tiêu (TO-BE) | Mức cải thiện |
|-------------------|--------------------------|--------------------------|---------------|
| **Thời gian giải quyết trung bình (Avg CT)** | 8,5 ngày (204 giờ) | 1,8 ngày (43,2 giờ) | **-78,8%** |
| **Thời gian xử lý thực (PT)** | 55 phút (0,92 giờ) | 18 phút (0,30 giờ) | **-67,3%** |
| **Hiệu suất thời gian quy trình (PTE)** | 0,45% | 0,69% | **+53,3%** |
| **Chi phí xử lý thủ công / ca (CS Staff)** | 52.000 VNĐ | 18.000 VNĐ | **-65,4%** |
| **Tỷ lệ khiếu nại leo thang (Escalation Rate)** | 20% | 5-8% | **-60-75%** |
| **Chỉ số Hài lòng Khách hàng (CSAT)** | 3,2 / 5,0 | 4,5 / 5,0 | **+40,6%** |

---

## 3.9. Quy trình Chăm sóc Khách hàng (Support #1)

### 3.9.1. Mô tả quy trình
Quy trình tiếp nhận và xử lý yêu cầu hỗ trợ từ Buyer/Seller qua các kênh Live Chat, Hotline 1900 1010, Email, Help Center với Chatbot AI Lazzie phân tầng tự động.

### 3.9.2. Sơ đồ BPMN quy trình CSKH
Sơ đồ BPMN gồm **5 Lanes (Customer, Chatbot/AI, CS Tier 1, CS Tier 2, System)**, **18 Tasks**, **11 Gateways**:

![Sơ đồ BPMN Quy trình CSKH AS-IS](docs/screenshots/05-customer-service-asis.png)  
**Hình 3.7: Sơ đồ BPMN quy trình chăm sóc khách hàng (AS-IS)**

```mermaid
flowchart TD
    S_CS([Start: Yêu cầu hỗ trợ từ khách hàng]) --> T_CS1[Mô tả chi tiết vấn đề cần hỗ trợ]
    T_CS1 --> T_CS2[AI NLP phân loại ý định & mức độ khẩn cấp]
    T_CS2 --> T_CS3[Hệ thống kiểm tra SLA xử lý ticket]
    T_CS3 --> G_CS1{SLA còn thời hạn xử lý?}
    G_CS1 -->|Hết hạn SLA| End_CS3([End: Ticket hỗ trợ đã quá hạn SLA])
    G_CS1 -->|Còn thời hạn| T_CS4[Hệ thống trích xuất thông tin đơn & tài khoản]
    T_CS4 --> G_CS2{Chatbot có sẵn kịch bản trả lời?}
    G_CS2 -->|Có| T_CS5[Chatbot (Lazada Assistant) tự động giải đáp] --> G_CS3{Chatbot giải quyết thành công?}
    G_CS3 -->|Thành công| J_CS1((Gom luồng trước Xác nhận hoàn tất))
    G_CS3 -->|Chưa thành công| J_CS2((Gom luồng trước Tier 1))
    G_CS2 -->|Không| T_CS6[Xác minh danh tính khách hàng] --> G_CS4{Xác minh danh tính thành công?}
    G_CS4 -->|Thất bại| End_CS2([End: Xác minh danh tính đã thất bại])
    G_CS4 -->|Thành công| G_CS5{Khách liên hệ lại lần 2?}
    G_CS5 -->|Có| J_CS2
    G_CS5 -->|Không| T_CS7[Lấy lịch sử tương tác (auto)] --> J_CS2
    J_CS2 --> T_CS8[Tư vấn viên Tier 1 tiếp nhận & hỗ trợ] --> T_CS9[Tư vấn viên Tier 1 đưa giải pháp xử lý]
    T_CS9 --> G_CS6{Tier 1 giải quyết thành công?}
    G_CS6 -->|Thành công| J_CS1
    G_CS6 -->|Cần thêm chứng từ| T_CS10[Cung cấp thêm thông tin chứng từ] --> T_CS11[Chờ phản hồi từ tư vấn viên]
    G_CS6 -->|Cần chuyên sâu| T_CS12[Chuyên viên Tier 2 thẩm định chuyên sâu] --> T_CS13[Chuyên viên Tier 2 xử lý dứt điểm] --> J_CS1
    T_CS11 --> G_CS7{Quá thời gian chờ phản hồi?}
    G_CS7 -->|Có| T_CS14[Gửi nhắc nhở phản hồi cho khách hàng] --> J_CS2
    G_CS7 -->|Không| J_CS2
    J_CS1 --> T_CS15[Khách hàng bấm xác nhận hoàn tất hỗ trợ] --> T_CS16[Khách hàng chấm điểm khảo sát CSAT]
    T_CS16 --> G_CS8{Đánh giá CSAT ≥ 4 sao?}
    G_CS8 -->|Từ 4 sao trở lên| J_CS3((Gom luồng trước Ghi nhận nhật ký))
    G_CS8 -->|Dưới 4 sao| T_CS17[Khảo sát đánh giá chất lượng (QA Follow-up)] --> J_CS3
    J_CS3 --> T_CS18[Ghi nhận nhật ký phiên & điểm CSAT] --> End_CS1([End: Phiên hỗ trợ đã kết thúc thành công])
```

### 3.9.3. Phân tích Định tính & Định lượng CSKH

**Bảng 3.10: Phân tích Giá trị gia tăng (VA/BVA/NVA) quy trình CSKH**

| Hoạt động | Phân loại | Tỷ lệ % | Đề xuất cải tiến |
|-----------|-----------|---------|------------------|
| Chatbot Lazzie trả lời FAQ tự động | **VA** | 35% | Mở rộng tri thức LLM Generative AI Chatbot |
| Agent Tier 1 xử lý vấn đề trực tiếp | **VA** | 25% | Auto-popup thông tin đơn hàng |
| Chờ kết nối Tổng đài viên | **NVA** | 20% | Tự động gọi lại (Call-back) |
| Agent tra cứu CRM thủ công | **BVA** | 12% | AI gợi ý answer trước khi agent reply |
| Chuyển tiếp Ticket Tier 2 | **BVA** | 8% | Phân luồng thông minh AI routing |

*(Nguồn: phân bổ ước tính theo thời gian tiếp xúc trung bình 79 phút/lượt — chatbot FAQ 60% kịch bản, Tier 1 resolve 80%, Tier 2 20%, QA 15%, kết hợp xác suất tiếp nhận; docs/analysis/05 §3.9.2. Tỷ lệ % là ước tính trọng số, không phải số liệu tuyệt đối.)*

---

## 3.10. Quy trình Marketing và Khuyến mãi (Support #2)

### 3.10.1. Mô tả quy trình
Quy trình thiết kế, phê duyệt, mở cổng đăng ký Seller và vận hành các chiến dịch Mega Campaign (9.9, 11.11, 12.12).

### 3.10.2. Mô hình BPMN & Thống kê
Sơ đồ BPMN 2.0 Marketing & Khuyến mãi gồm **5 Lanes (Marketing Team, Approval, Lazada System, Sellers, Buyers)**, **21 Tasks**, **15 Gateways**:

![Sơ đồ BPMN Quy trình Marketing AS-IS](docs/screenshots/06-marketing-asis.png)  
**Hình 3.8: Sơ đồ BPMN quy trình marketing và khuyến mãi (AS-IS)**

```mermaid
flowchart TD
    S_MK([Start: Lên kế hoạch chiến dịch Marketing]) --> T_MK1[Marketing Team thiết kế Concept & Budget]
    T_MK1 --> G_MK1{Hạng mức ngân sách?}
    
    G_MK1 -->|Dưới 100 triệu| T_MK2[Truong bo phan phe duyet]
    G_MK1 -->|Trên 100 triệu| T_MK3[CMO/CFO phe duyet]
    T_MK2 --> G_MK2{Phe duyet OK?}
    T_MK3 --> G_MK2
    G_MK2 -->|Tu choi| End_MK1([End: Huy chien dich])
    G_MK2 -->|Dong y| T_MK4[Creative Team thiet ke banner + landing page]
    
    T_MK4 --> T_MK5[Legal/Marcom duyet noi dung]
    T_MK5 --> G_MK3{No dung dat tuan thu?}
    G_MK3 -->|Khong| T_MK6[Chinh sua lai] --> T_MK4
    G_MK3 -->|Dat| T_MK7[Mo cang dang ky cho Seller]
    
    T_MK7 --> T_MK8[Seller dang ky san pham & muc giam gia]
    T_MK8 --> T_MK9[System tu dong tham dinh dieu kien seller]
    T_MK9 --> G_MK4{Seller du dieu kien?}
    G_MK4 -->|Khong| T_MK10[Tu choi Seller tham gia]
    G_MK4 -->|Du| T_MK11[System duyet SKU & Cau hinh Voucher]
    
    T_MK11 --> T_MK12[Kich hoat Campaign dung gio G]
    T_MK12 --> T_MK13[Buyer san Voucher & Dat hang]
    T_MK13 --> G_MK5{Hieu suat dat KPI?}
    G_MK5 -->|Dat| T_MK14[Xuat bao cao ROI post-campaign]
    G_MK5 -->|Khong dat| T_MK15[Tang voucher/ads hoac cat giam som]
    T_MK14 --> End_MK2([End: Hoan tat chien dich])
    T_MK15 --> End_MK2
```

**Bảng 3.11: Phân tích Định tính & Định lượng Marketing**

| Hạng mục phân tích | Chi tiết kết quả |
|--------------------|------------------|
| **Tỷ lệ VA / BVA / NVA** | VA: 57%, BVA: 33%, NVA: 10% (NVA do cấu hình chiến dịch thủ công và thu thập số liệu đối soát qua Excel; ước tính theo phân loại hoạt động). |
| **Điểm nghẽn (Bottleneck)** | Quy trình duyệt ngân sách qua nhiều cấp quản lý (Multi-layer approval). |
| **Thời gian triển khai (Time-to-Market)** | 3-4 tuần (từ ý tưởng đến khi chạy chiến dịch). |
| **Chi phí vận hành Campaign** | 420.000.000 VNĐ / Mega Campaign. |

---

## 3.11. Quy trình Quản lý Nhân sự & Đào tạo (Management #3)

### 3.11.1. Mô tả quy trình

Quy trình quản lý nhân sự & đào tạo bao trùm vòng đời nhân sự tại Lazada VN: tuyển dụng, onboarding, đào tạo nội bộ (LMS), chứng chỉ tuân thủ (compliance), và đánh giá năng lực. Quy trình hiện tại phụ thuộc lớn vào thao tác thủ công với vòng duyệt tài chính kéo dài 5–10 ngày.

**Hệ số Owning department:** HR + L&D, Line Manager, Finance
**Số lane:** 4 (AS-IS: HR Team, Lazada University, Seller / Nhân viên, Compliance) → 5 (TO-BE: thêm Finance; đổi Lazada University → Lazada University (AI), Compliance → Compliance (Hệ thống))
**End events:** 2 (Chương trình đào tạo đã hoàn tất, Vi phạm chính sách đã được xử lý)
**Activities:** 17 (AS-IS) → 21 (TO-BE) | **Gateways:** 15 → 15 (14 exclusive + 1 parallel AS-IS; TO-BE toàn bộ exclusive)

### 3.11.2. Phân tích Qualitative & Quantitative

| Chỉ số | Giá trị |
|--------|---------|
| VA / BVA / NVA | VA: 40%, BVA: 30%, NVA: 30% |
| Tỷ lệ hoàn thành khóa đào tạo | 60% (benchmark ≥90%) |
| Thời gian duyệt tài chính | 5–10 ngày |
| Chi phí đào tạo/đầu người | 2.5–5M VNĐ/năm |
| Completion rate Improvement (TO-BE) | 60% → 90% (+50%) |
| Gateways (AS-IS → TO-BE) | 15 → 15 |

### 3.11.3. BPMN AS-IS
![BPMN AS-IS Nhân sự & Đào tạo](docs/screenshots/07-hr-training-asis.png)  
**Hình 3.15: Sơ đồ BPMN quy trình nhân sự & đào tạo (AS-IS)**

### 3.11.4. BPMN TO-BE
![BPMN TO-BE Nhân sự & Đào tạo](docs/screenshots/07-hr-training-tobe.png)  
**Hình 3.16: Sơ đồ BPMN quy trình nhân sự & đào tạo (TO-BE)**

---

## 3.12. Quy trình Thanh toán & Đối soát (Core #2)

### 3.12.1. Mô tả quy trình

Quy trình thanh toán & đối soát xử lý toàn bộ dòng tiền: COD, thẻ, ví điện tử, escrow, đối soát ngân hàng, và giải ngân cho seller. COD discrepancy 2–3% (~40 tỷ/tháng) là lãng phí lớn nhất; settlement chậm L+2/L+3 gây stress dòng tiền seller.

**Số lane:** 5 (Buyer, Payment Gateway VNPay/MoMo/ZaloPay, Lazada System (Escrow), Finance, Seller)
**End events:** 3 (Seller đã nhận tiền thanh toán, Đối soát đã hoàn tất, Đã hoàn tiền về Buyer)
**Activities:** 22 (AS-IS) | **Gateways:** 16 (XOR + AND — 14 exclusive + 2 parallel)

### 3.12.2. Phân tích Qualitative & Quantitative

| Chỉ số | Giá trị |
|--------|---------|
| COD discrepancy | 2–3% (~40 tỷ VND/tháng) |
| Settlement cycle | L+2 (online) / L+3 (COD) (→ TO-BE: L+1 online / L+2 COD) |
| Gateway fees toàn sàn | ~67,5–112,5 tỷ VND/tháng (1,5–2,5% × 4.500 tỷ GMV) |
| Đối soát COD thủ công | 4–24h/case + 2–4h/ngày matching (→ TO-BE: ML auto-matching) |
| VA / BVA / NVA | VA: 63%, BVA: 27%, NVA: 9% (đếm 14/22, 6/22, 2/22 hoạt động) |
| Gateways (AS-IS → TO-BE) | 16 → 14 |

### 3.12.3. BPMN AS-IS
![BPMN AS-IS Thanh toán & Đối soát](docs/screenshots/08-payment-settlement-asis.png)  
**Hình 3.17: Sơ đồ BPMN quy trình thanh toán & đối soát (AS-IS)**

### 3.12.4. BPMN TO-BE
![BPMN TO-BE Thanh toán & Đối soát](docs/screenshots/08-payment-settlement-tobe.png)  
**Hình 3.18: Sơ đồ BPMN quy trình thanh toán & đối soát (TO-BE)**

---

## 3.13. Quy trình Logistics & Giao nhận (Core #3)

### 3.13.1. Mô tả quy trình

Quy trình logistics quản lý pickup → phân loại hub → vận chuyển → last-mile → retry/return. LEX kết hợp 3PL (GHN, J&T, Grab, Ninja Van). Năm lãng phí lớn nhất (Pareto, ~354 tỷ VND/tháng): Return/hoàn về kho (90 tỷ/tháng), Giao lại (85 tỷ/tháng), Chi phí last-mile cao (83,5 tỷ/tháng), Sort Hub inefficiency (55 tỷ/tháng), Tracking không realtime (40,5 tỷ/tháng).

**Số lane:** 5 (Seller, Lazada System, LEX/3PL (GHN, J&T, Grab, NINJAVAN), Shipper (Giao hàng), Buyer)
**End events:** 2 (Đơn hàng đã giao thành công, Hàng đã hoàn về Seller)
**Activities:** 20 (AS-IS) | **Gateways:** 13 (toàn bộ XOR — exclusiveGateway)

### 3.13.2. Phân tích Qualitative & Quantitative

| Chỉ số | Giá trị |
|--------|---------|
| First-attempt delivery | 75–80% (→ TO-BE: 92%) |
| Giao lại chi phí | 85 tỷ VND/tháng |
| Return/hoàn về kho chi phí | 90 tỷ VND/tháng |
| Hub sorting error chi phí | 55 tỷ VND/tháng |
| Tracking không realtime chi phí | 40,5 tỷ VND/tháng |
| Chi phí last-mile cao (province 40k vs benchmark 30-35k) | 83,5 tỷ VND/tháng |
| **Tổng chi phí lãng phí logistics** | **~354 tỷ VND/tháng** |
| Transit delay (thành phần trong last-mile) | 40 tỷ VND/tháng |
| VA / BVA / NVA | VA: 38%, BVA: 32%, NVA: 30% |
| Gateways (AS-IS → TO-BE) | 13 → 19 |

> **Phân bổ Pareto:** 5 lãng phí lớn nhất (≈354 tỷ VND/tháng): ① Giao lại nhiều lần 24,0% (85 tỷ); ② Return/hoàn về kho 25,4% (90 tỷ); ③ Sort Hub inefficiency 15,5% (55 tỷ); ④ Tracking không realtime 11,4% (40,5 tỷ); ⑤ Chi phí last-mile cao 23,6% (83,5 tỷ). TO-BE: ~246 tỷ VND/tháng (−108 tỷ, −31%).

### 3.13.3. BPMN AS-IS
![BPMN AS-IS Logistics & Giao nhận](docs/screenshots/09-logistics-delivery-asis.png)  
**Hình 3.19: Sơ đồ BPMN quy trình logistics & giao nhận (AS-IS)**

### 3.13.4. BPMN TO-BE
![BPMN TO-BE Logistics & Giao nhận](docs/screenshots/09-logistics-delivery-tobe.png)  
**Hình 3.20: Sơ đồ BPMN quy trình logistics & giao nhận (TO-BE)**

---

## 3.14. Quy trình Vận hành Nền tảng Công nghệ (Support #3)

### 3.14.1. Mô tả quy trình

Quy trình IT Operations quản lý release, bug fix, CI/CD, và ứng phó sự cố bảo mật. Bug fix loop 2–5 ngày và deploy failure 15% gây chi phí lớn. Đơn vị tham chiếu (lớn nhất): bug fix loop 1,17 tỷ VND/tháng, deploy fail 0,78 tỷ VND/tháng (tổng chi phí IT Ops 3,9 tỷ VND/tháng).

**Số lane:** 5 (Product Owner, Dev Team, QA/Tester, DevOps/CI-CD, Security)
**End events:** 2 (Tính năng đã deploy thành công, Đã rollback về version trước)
**Activities:** 18 (AS-IS) | **Gateways:** 16 (toàn bộ XOR — exclusiveGateway)

### 3.14.2. Phân tích Qualitative & Quantitative

| Chỉ số | Giá trị |
|--------|---------|
| Bug fix cycle time | 2–5 ngày (→ TO-BE: <1 ngày) |
| Deploy failure rate | 15% (→ TO-BE: <3%) |
| Security response time | 7–14 ngày (→ TO-BE: <24h) |
| Release cycle | 4–6 tuần (→ TO-BE: 1–2 tuần) |
| VA / BVA / NVA | VA: 32%, BVA: 38%, NVA: 30% |
| Gateways (AS-IS → TO-BE) | 16 → 16 |

### 3.14.3. BPMN AS-IS
![BPMN AS-IS Vận hành CNTT](docs/screenshots/10-it-platform-asis.png)  
**Hình 3.21: Sơ đồ BPMN quy trình vận hành CNTT (AS-IS)**

### 3.14.4. BPMN TO-BE
![BPMN TO-BE Vận hành CNTT](docs/screenshots/10-it-platform-tobe.png)  
**Hình 3.22: Sơ đồ BPMN quy trình vận hành CNTT (TO-BE)**

---

## 3.15. Phân tích AS-IS / TO-BE Tổng hợp và Sơ đồ BPMN Cải tiến

> **Nguồn dữ liệu tổng hợp:** Toàn bộ vấn đề phát hiện từ 10 quy trình được thống kê đầy đủ trong **Issue Register** (65 vấn đề, gồm phân loại mức độ Cao/TB/Thấp, nguồn phát hiện PV/PT/BM và ma trận ưu tiên Impact × Urgency) tại [docs/analysis/issue-register.md](docs/analysis/issue-register.md). Phần này trình bày kết quả tổng hợp RACI, BPMN TO-BE và các KPI cải thiện tiêu biểu; các bảng Pareto chi tiết theo từng quy trình nằm ở Mục 3.4-3.14.

### 3.15.1. Ma trận Phân công Trách nhiệm (RACI Matrix)

**Bảng 3.12: Ma trận RACI cho các hoạt động chính trong hệ thống 10 quy trình**

| Hoạt động Quy trình | Buyer | Seller | Lazada System | LEX/3PL | CSKH Team | Finance |
|---------------------|-------|--------|---------------|---------|-----------|---------|
| Duyệt đăng ký & Onboarding Seller (Q1) | I | **R** | **A / C** | I | C | I |
| Đặt hàng & Thanh toán (Q4) | **R** | I | **A / C** | I | I | C |
| Xác nhận & Đóng gói (Q4) | I | **R / A** | C | I | I | I |
| Warehouse QC & Packing (Q4) | I | I | **A** | C | I | I |
| Gom hàng & Vận chuyển (Q6) | I | I | C | **R / A** | I | I |
| Giao chặng cuối & COD (Q6) | **C** | I | I | **R / A** | I | C |
| Trả hàng & Hoàn tiền (Q7) | **R** | C | **A** | C | **R** | C |
| Giải ngân Ví Seller (Q5) | I | I | **A** | I | I | **R** |
| Xử lý tranh chấp (Q2) | **R** | **R** | **A** | C | **R** | C |
| CSKH & Hỗ trợ (Q8) | **R** | C | **A** | I | **R** | I |
| Marketing & Khuyến mãi (Q9) | C | C | **A / R** | I | C | C |
| Đào tạo & Phát triển năng lực (Q3) | I | **R** | **A / R** | I | I | C |
| Vận hành nền tảng CNTT & AIOps (Q10) | I | I | **A / R** | C | C | C |

*(Ghi chú: R = Responsible - Người thực hiện, A = Accountable - Người chịu trách nhiệm chính, C = Consulted - Người tham vấn, I = Informed - Người nhận thông báo)*

---

### 3.15.2. Sơ đồ BPMN Quy trình TO-BE (Cải tiến cho 10 quy trình)

Dưới đây là các hình ảnh mô hình BPMN TO-BE đã được tối ưu hóa loại bỏ nấc trung gian, ứng dụng eKYC tự động, AI phân tích rủi ro đơn hàng và tự động hóa cao:

#### 1. Sơ đồ BPMN TO-BE Xử lý Đơn hàng Online:
![Sơ đồ BPMN Xử lý Đơn hàng TO-BE](docs/screenshots/03-order-processing-tobe.png)  
**Hình 3.9: Sơ đồ BPMN quy trình xử lý đơn hàng online (TO-BE)**

#### 2. Sơ đồ BPMN TO-BE Quản lý Nhà bán hàng:
Sơ đồ TO-BE gồm **4 Lanes (Seller, Lazada System, Compliance Team, Legal/Giám sát Vận hành)**, **13 Tasks**, **7 Gateways** (toàn bộ XOR) và **5 End Events**; hồ sơ nghi vấn chuyển Compliance review thủ công có **Timer "Hạn chót SLA 24h" (PT24H)** — kết quả thẩm định phải trả về trong vòng 24 giờ (đối chiếu file `processes-to-be/01-seller-management.bpmn`).  
![Sơ đồ BPMN Quản lý Nhà bán hàng TO-BE](docs/screenshots/01-seller-management-tobe.png)  
**Hình 3.10: Sơ đồ BPMN quy trình quản lý nhà bán hàng (TO-BE)**

#### 3. Sơ đồ BPMN TO-BE Quản lý Tranh chấp & Rủi ro:
![Sơ đồ BPMN Quản lý Tranh chấp TO-BE](docs/screenshots/02-dispute-management-tobe.png)  
**Hình 3.11: Sơ đồ BPMN quy trình quản lý tranh chấp và rủi ro (TO-BE)**

#### 4. Sơ đồ BPMN TO-BE Hoàn trả & Hoàn tiền:
![Sơ đồ BPMN Hoàn trả & Hoàn tiền TO-BE](docs/screenshots/04-return-refund-tobe.png)  
**Hình 3.12: Sơ đồ BPMN quy trình hoàn trả và hoàn tiền (TO-BE)**

#### 5. Sơ đồ BPMN TO-BE Chăm sóc Khách hàng:
Sơ đồ TO-BE gồm **5 Lanes (Customer, Chatbot AI, CS Tier 1, CS Tier 2, System)**, **14 Tasks**, **9 Gateways** (toàn bộ XOR) và **2 End Events** (đối chiếu file `processes-to-be/05-customer-service.bpmn`).  
![Sơ đồ BPMN CSKH TO-BE](docs/screenshots/05-customer-service-tobe.png)  
**Hình 3.13: Sơ đồ BPMN quy trình chăm sóc khách hàng (TO-BE)**

#### 6. Sơ đồ BPMN TO-BE Marketing & Khuyến mãi:
![Sơ đồ BPMN Marketing TO-BE](docs/screenshots/06-marketing-tobe.png)  
**Hình 3.14: Sơ đồ BPMN quy trình marketing và khuyến mãi (TO-BE)**

> **Ghi chú:** Sơ đồ TO-BE của 4 quy trình còn lại (Nhân sự & Đào tạo, Thanh toán & Đối soát, Logistics & Giao nhận, Vận hành CNTT) được trình bày kèm phân tích chi tiết tại Mục 3.11.4 (Hình 3.16), 3.12.4 (Hình 3.18), 3.13.4 (Hình 3.20), 3.14.4 (Hình 3.22).

---

### 3.15.3. Bảng Tổng hợp Giải pháp Cải tiến TO-BE

**Bảng 3.13: Bảng tổng hợp giải pháp cải tiến TO-BE cho 10 quy trình**

| Mã | Quy trình | Giải pháp TO-BE áp dụng | Chỉ số KPI cải thiện kỳ vọng |
|----|-----------|-------------------------|------------------------------|
| **P1** | Order Processing | Tự động chấp nhận đơn sau hết SLA 2h (thay vì chờ Seller thủ công 24-48h); rút ngắn auto-confirm nhận hàng 7 ngày → 24-72h cho Shop Diamond/Gold; Cơ chế xác nhận nhận hàng trước khi ship COD | Tỷ lệ giao 1st thành công: 75–80% --> 92%; Giảm COD refusal: 15–20% --> 8% |
| **P2** | Return & Refund | Cấu hình Instant Refund cho đơn giá trị nhỏ (<200K) & Shop uy tín; Phân biệt auto/manual ngay gateway đầu | Thời gian hoàn tiền: 8,5 ngày --> 1,8 ngày (-78,8%) |
| **P3** | Seller Management | Ứng dụng eKYC & OCR tự động đọc duyệt chứng từ Seller; AI Risk Scoring + tự động kích hoạt gian hàng Low-risk trong 3 giây | Thời gian duyệt Seller: 40h --> 2h (-95%) |
| **P4** | Dispute Management | Form nộp bằng chứng chuẩn hóa cấu trúc + AI Image Verification + Auto-escalation theo giá trị | Giảm 60-75% tỷ lệ khiếu nại leo thang lên Senior (20% → 5-8%, Bảng 3.9) |
| **P5** | Customer Service | Tích hợp LLM Generative AI Chatbot Lazzie tiếp nhận tự động 80% yêu cầu (resolve ~45%); Omnichannel routing thông minh | AHT giảm 82% (79 phút → ~14 phút, KPI doc 05) |
| **P6** | Marketing Campaign | Luồng duyệt ngân sách phân tầng rủi ro (Risk-tiered Approval); Auto-report dashboard realtime | Time-to-Market: 3-4 tuần --> 1 tuần |
| **P7** | HR & Training | LMS tự động hóa onboarding + compliance quiz bắt buộc; Rút ngắn vòng duyệt tài chính | Tỷ lệ hoàn thành khóa đào tạo: 60% --> 90% (+50%) |
| **P8** | Payment & Settlement | Auto-reconcile COD + API tích hợp bank realtime | Settlement: L+2/L+3 --> L+1 (online) / L+2 (COD); COD discrepancy: 2–3% --> 0,5% |
| **P9** | Logistics & Delivery | AI Route Optimization + slot hẹn giờ + quy trình drop-off network | First-attempt delivery: 75-80% --> 92%; Giao lại: 20-25% --> 8% (-60-68%) |
| **P10** | IT Operations | CI/CD tự động hóa + AIOps giám sát sự cố realtime | Bug fix: 2–5 ngày --> <1 ngày; Deploy failure: 15% --> <3% |

*(Ghi chú: Sơ đồ BPMN TO-BE của 4 quy trình P7-P10 được trình bày tại Mục 3.11.4, 3.12.4, 3.13.4, 3.14.4 — Hình 3.16, 3.18, 3.20, 3.22.)*

---

# Chương 4. KẾT LUẬN VÀ ĐỀ XUẤT

## 4.1. Kết luận
Đồ án **"Hệ thống Quản trị Quy trình Nghiệp vụ Lazada Việt Nam"** đã hoàn thành toàn bộ các mục tiêu đề ra theo đúng yêu cầu bài tập môn học IE203:
1. Systematize thành công **10 quy trình nghiệp vụ** thuộc 3 nhóm Quản lý, Cốt lõi, Hỗ trợ với sơ đồ kiến trúc tổng thể theo mô hình Ngôi nhà (House Diagram).
2. Mô hình hóa đầy đủ **10 quy trình trọng điểm** bằng chuẩn BPMN 2.0 (10 file .bpmn AS-IS + 10 TO-BE, kèm ảnh tại docs/screenshots/), với cấu trúc mô hình AS-IS được xác thực hợp lệ 100% bởi bộ kiểm tra tự động (3 thuộc tính van der Aalst — docs/petri-net, soundness-check.py).
3. Áp dụng đồng bộ các phương pháp phân tích định tính (VA/BVA/NVA, Waste Analysis, Fishbone, 5-Why, Pareto) và định lượng (Cycle Time, Unit Economics, Defect Rates) sâu sắc.
4. Đề xuất các giải pháp TO-BE khả thi mang lại cải thiện định lượng rõ rệt: giảm thời gian chu kỳ 50-95% trên các quy trình trọng điểm (duyệt Seller 40h→2h -95%, hoàn tiền 8,5→1,8 ngày -78,8%, kiểm định kho 8h→2h -75%) và giảm 65,4% chi phí xử lý đơn vị (Bảng 3.9) và giảm 60-75% tỷ lệ khiếu nại leo thang. Các chỉ số định lượng mang tính ước tính từ dữ liệu phỏng vấn mẫu và báo cáo thị trường công khai (xem 4.2).

## 4.2. Hạn chế của đồ án
- Do hạn chế truy cập dữ liệu bảo mật nội bộ của Lazada, một số chỉ số định lượng thời gian và chi phí dựa trên giả định tính toán từ nguồn dữ liệu phỏng vấn mẫu, báo cáo thị trường công khai và chính sách Seller Center.
- Thị phần và số liệu tài chính Lazada Group không được tách biệt theo từng quốc gia, nên các con số về Lazada Việt Nam mang tính ước tính.
- Quy trình HR & Training (Quy trình #7) được mô tả ở mức tổng quan do tính chất phức tạp và liên quan đến dữ liệu nhạy cảm.

## 4.3. Hướng phát triển tiếp theo
- Triển khai thực thi trực tiếp các file BPMN 2.0 trên hệ thống BPMS Engine thực tế như **Camunda Automation Platform Engine** để chạy simulation đo lường tải thực tế.
- Mở rộng phân tích định lượng bằng dữ liệu giả lập Monte Carlo cho Cycle Time và chi phí.
- Nghiên cứu tích hợp AI/ML model chấm điểm rủi ro đơn hàng real-time để giảm tỷ lệ COD refusal.
- Tích hợp phân tích Cross-border Commerce (TMall/Gmarket) và FBL Warehouse Operations như sub-process riêng.

---

# TÀI LIỆU THAM KHẢO

1. Lazada Vietnam (2026), *Seller Center & Help Center*, [Online]. Available: https://sellercenter.lazada.vn
2. Wikipedia (2026), *Lazada Group*, [Online]. Available: https://en.wikipedia.org/wiki/Lazada_Group
3. CafeF (2026), *Sau 14 năm tại Việt Nam, Lazada sẽ phát triển theo hướng nào trong giai đoạn mới*, [Online]. Available: https://cafef.vn/sau-14-nam-tai-viet-nam-lazada-se-phat-trien-theo-huong-nao-trong-giai-doan-moi-188260325124722081.chn
4. CafeF (2026), *Lazada bị phạt 350 triệu đồng*, [Online]. Available: https://cafef.vn/lazada-bi-phat-350-trieu-dong-188260817200639733.chn
5. CafeF (2026), *LazMall và cuộc all-in của Lazada (Interview CEO Jason Liu)*, [Online]. Available: https://cafef.vn/lazmall-va-cu-all-in-cua-lazada-188260604192934021.chn
6. ThS. Hà Lê Hoài Trung (2026), *Bài giảng Hệ thống Quản trị Quy trình Nghiệp vụ (IE203)*, Trường Đại học Công nghệ Thông tin — ĐHQG TP.HCM.
7. OMG (2011), *Business Process Model and Notation (BPMN) Version 2.0 Specification*, Object Management Group.
8. Dumas, M., La Rosa, M., Mendling, J., & Reijers, H. A. (2018), *Fundamentals of Business Process Management (2nd ed.)*, Springer.
9. Google-Temasek-Bain (2024), *e-Conomy SEA 2024 Report*, [Online].
10. YouNet ECI (2024), *E-commerce Market Share Report Vietnam 2024*, [Online].

---

# PHỤ LỤC A: BỘ CÂU HỎI PHỎNG VẤN CHUẨN

*(Bao gồm 20 câu hỏi phỏng vấn chuẩn hóa: 10 định tính + 10 định lượng)*

## A. 10 Câu hỏi ĐỊNH TÍNH

### A1. 5 câu CẤU TRÚC (Thang đo Likert 1-5)
- **Q1:** Mức độ hài lòng chung của Anh/Chị đối với quy trình xử lý đơn hàng trên Lazada? (1: Rất không hài lòng --> 5: Rất hài lòng)
- **Q2:** Mức độ thuận tiện khi thực hiện thao tác quản lý đơn hàng trên Seller Center Lazada? (1: Rất bất tiện --> 5: Rất thuận tiện)
- **Q3:** Đánh giá tính hữu ích của Chatbot Lazzie trong việc hỗ trợ giải đáp vấn đề nhanh chóng? (1: Không hữu ích --> 5: Rất hữu ích)
- **Q4:** Mức độ hợp lý của thời gian quy định cho Seller xác nhận đơn hàng (24-48 giờ)? (1: Rất không hợp lý --> 5: Rất hợp lý)
- **Q5:** Mức độ công bằng và minh bạch của quy trình xử lý khiếu nại Hoàn trả/Hoàn tiền của Lazada? (1: Rất thiếu công bằng --> 5: Rất công bằng)

### A2. 5 câu KHÔNG CẤU TRÚC (Câu hỏi mở Open-ended)
- **Q6:** Anh/Chị hãy mô tả chi tiết các bước thực tế từ lúc nhận thông báo đơn mới đến khi giao thành công bưu kiện cho LEX/3PL?
- **Q7:** Những khó khăn hoặc sự cố thường gặp nhất trong quá trình vận hành đơn hàng hàng ngày là gì?
- **Q8:** Nếu được đề xuất thay đổi 1 bước trong quy trình hiện tại, Anh/Chị muốn thay đổi bước nào nhất và tại sao?
- **Q9:** Hệ thống Lazada có những điểm nghẽn nào ảnh hưởng trực tiếp đến trải nghiệm mua hàng của Buyer (ví dụ: giao trễ, hoàn tiền chậm)?
- **Q10:** Anh/Chị xử lý thế nào khi gặp trường hợp đơn hàng bị khiếu nại hoàn tiền không chính đáng hoặc boom hàng COD?

## B. 10 Câu hỏi ĐỊNH LƯỢNG

### B1. 5 câu CẤU TRÚC (Trắc nghiệm nhiều lựa chọn)
- **Q11:** Trung bình gian hàng của Anh/Chị xử lý bao nhiêu đơn hàng mỗi ngày? (<10 đơn / 10-50 đơn / 50-100 đơn / >100 đơn)
- **Q12:** Thời gian trung bình để hoàn tất đóng gói 1 bưu kiện là bao lâu? (<5 phút / 5-15 phút / 15-30 phút / >30 phút)
- **Q13:** Tỷ lệ đơn hàng bị trả về / hoàn tiền trên tổng số đơn của gian hàng là bao nhiêu %? (<2% / 2-5% / 5-10% / >10%)
- **Q14:** Tần suất LEX/3PL đến kho gom hàng trung bình bao nhiêu lần một ngày? (1 lần / 2 lần / >2 lần)
- **Q15:** Chi phí vật tư đóng gói trung bình cho 1 đơn hàng tiêu chuẩn là bao nhiêu VNĐ? (<3.000 / 3.000-5.000 / >5.000 VNĐ)

### B2. 5 câu KHÔNG CẤU TRÚC (Nhập số liệu thực tế)
- **Q16:** Thời gian trung bình từ lúc đơn hàng phát sinh đến khi bưu kiện được LEX/3PL quét mã nhận hàng là bao nhiêu giờ?
- **Q17:** Tỷ lệ % đơn hàng giao thành công ngay ở lần giao đầu tiên (1st attempt) của gian hàng là bao nhiêu %?
- **Q18:** Tổng chi phí vận hành biên ước tính để xử lý 1 đơn hàng (bao gồm nhân công, bao bì, điện nước) là bao nhiêu VNĐ?
- **Q19:** Trong các đợt Mega Sale (9.9, 11.11, 12.12), lượng đơn hàng tăng gấp bao nhiêu lần so với ngày thường?
- **Q20:** Thời gian trung bình từ khi Buyer bấm "Trả hàng" đến khi tiền được giải quyết hoàn tất là bao nhiêu ngày?

---

# PHỤ LỤC B: BIỂU MẪU WORKSHOP VÀ KỊCH BẢN PHỎNG VẤN MẪU

**TRƯỜNG ĐẠI HỌC CÔNG NGHỆ THÔNG TIN - ĐHQG TP.HCM**  
**BIÊN BẢN WORKSHOP KHẢO SÁT & PHỎNG VẤN QUY TRÌNH NGHIỆP VỤ LAZADA**  

- **Thời gian:** 09:00 - 12:00, Ngày 20 tháng 08 năm 2026 (khớp biên bản workshop)  
- **Địa điểm:** Phòng họp Online (Teams Meeting ID: 482-573-218)  
- **Chủ trì:** Nhóm nghiên cứu Đồ án Lazada BA  
- **Thành phần tham dự:** 10 người phỏng vấn sâu từ các bộ phận nội bộ Lazada VN (Seller Operations, Dispute Resolution, Fulfillment Operations, Return & Refund, Customer Service, Marketing, HR & Training, Payment & Settlement, Logistics/LEX, IT Platform) — chi tiết tại `appendix/interviews/01…10`.  

**NỘI DUNG THẢO LUẬN & GHI NHẬN:**
1. *Ý kiến đại diện Seller:* Thời gian chờ LEX đến lấy hàng (Pickup) trong ngày Mega Sale thường bị trễ 12-24h so với hẹn. Đề xuất mở rộng điểm Drop-off tự động và tối ưu cutoff time linh hoạt.
2. *Ý kiến đại diện LEX Shipper:* Tỷ lệ COD refusal cao (15-20%) gây lãng phí thời gian và nhiên liệu. Đề xuất Lazada áp dụng cơ chế xác nhận nhận hàng trước khi ship và AI gợi ý định vị địa chỉ.
3. *Ý kiến đại diện CSKH:* Quy trình thẩm định hình ảnh trả hàng thủ công mất trung bình 18 phút/case, cần AI tự động so sánh ảnh trước và sau khi đóng gói để tăng tốc inspection.

---

# PHỤ LỤC C: KẾ HOẠCH THỰC HIỆN ĐỒ ÁN (GANTT CHART)

**Bảng C.1: Kế hoạch thực hiện đồ án 12 tuần (Gantt Chart)**

| Tuần thứ | Hạng mục công việc chính | Sản phẩm đầu ra (Deliverable) | Người thực hiện |
|----------|--------------------------|-------------------------------|-----------------|
| Tuần 1 - 2 | Thu thập tài liệu, khảo sát 10 quy trình | Sơ đồ Kiến trúc Quy trình & PROCESSES.md | Cả 2 thành viên |
| Tuần 3 - 4 | Vẽ 10 sơ đồ BPMN 2.0 AS-IS | 10 file XML `.bpmn` chuẩn Camunda | Cả 2 thành viên |
| Tuần 5 - 6 | Phân tích định tính VA/NVA/Waste/Fishbone | Các bảng phân tích định tính & Pareto | Thành viên A & B |
| Tuần 7 - 8 | Phân tích định lượng Cycle Time & Chi phí | Bảng tính toán Cycle Time & Unit Economics | Thành viên B |
| Tuần 9 - 10| Thiết kế mô hình TO-BE & Đề xuất KPI | 10 file BPMN TO-BE & Ma trận RACI | Cả 2 thành viên |
| Tuần 11- 12| Hoàn thiện báo cáo Master & Slide Marp | File `DOAN-LAZADA-FINAL.md` & Marp Slides| Cả 2 thành viên |

---

# PHỤ LỤC D: DANH MỤC THUẬT NGỮ VÀ SỔ TAY (GLOSSARY)

**Bảng D.1: Danh mục 30 Thuật ngữ Quản trị Quy trình & TMĐT Lazada**

| STT | Thuật ngữ (Term) | Định nghĩa & Giải thích chi tiết |
|-----|------------------|----------------------------------|
| 1 | **Activity (Tác vụ)** | Một bước công việc được thực hiện trong quy trình BPMN. |
| 2 | **AS-IS Model** | Mô hình phản ánh hiện trạng thực tế của quy trình khi chưa cải tiến. |
| 3 | **BPMN 2.0** | Ký hiệu đồ họa chuẩn hóa quốc tế để biểu diễn quy trình nghiệp vụ. |
| 4 | **BVA (Business Value-Added)** | Hoạt động không tạo giá trị trực tiếp cho khách nhưng cần thiết cho vận hành. |
| 5 | **Cycle Time (CT)** | Tổng thời gian trôi qua từ khi bắt đầu đến khi kết thúc quy trình. |
| 6 | **Drop-off** | Hình thức Seller tự mang bưu kiện đã đóng gói ra bưu cục ĐVVC. |
| 7 | **eKYC** | Electronic Know Your Customer -- xác minh danh tính điện tử qua OCR & selfie. |
| 8 | **Escrow Account** | Tài khoản bảo hộ giữ tiền giao dịch của Lazada trước khi giải ngân. |
| 9 | **Exclusive Gateway (XOR)** | Cổng điều kiện trong BPMN chỉ cho phép duy nhất 1 nhánh được thực thi. |
| 10 | **FBL (Fulfilled by Lazada)** | Dịch vụ lưu kho, đóng gói và vận chuyển bởi Lazada (tương tự FBA). |
| 11 | **Fishbone Diagram** | Biểu đồ xương cá Ishikawa dùng để tìm nguyên nhân gốc rễ của vấn đề. |
| 12 | **Fulfillment** | Quy trình toàn bộ từ khâu lưu kho, nhặt hàng, đóng gói đến giao nhận. |
| 13 | **Hold Waste** | Lãng phí do thời gian chờ đợi trệch nhịp giữa các bước trong quy trình. |
| 14 | **Lane (Làn)** | Đường làn trong sơ đồ BPMN phân định trách nhiệm của từng tác nhân. |
| 15 | **Last-mile Delivery** | Giai đoạn vận chuyển chặng cuối từ kho bưu cục đến tay người nhận. |
| 16 | **LEX (Lazada Express)** | Đơn vị vận chuyển nội bộ thuộc hệ sinh thái Lazada. |
| 17 | **Line-haul** | Vận chuyển chặng giữa tuyến cố định kết nối giữa các kho trung chuyển. |
| 18 | **LazMall** | Kênh gian hàng chính hãng 100% trên Lazada với chính sách hoàn trả 15 ngày. |
| 19 | **Move Waste** | Lãng phí do di chuyển hàng hóa/dữ liệu qua quá nhiều nấc trung gian. |
| 20 | **NVA (Non-Value-Added)** | Hoạt động lãng phí không tạo ra bất kỳ giá trị nào, cần loại bỏ. |
| 21 | **Overdo Waste** | Lãng phí do thực hiện dư thừa thao tác hoặc kiểm tra quá mức cần thiết. |
| 22 | **Parallel Gateway (AND)** | Cổng rẽ nhánh song song cho phép thực thi đồng thời nhiều tác vụ. |
| 23 | **Pareto Chart** | Biểu đồ kết hợp cột và đường thể hiện quy tắc 80% hậu quả do 20% nguyên nhân. |
| 24 | **Petri Net Soundness** | Đội đúng đắn toán học của mô hình BPMN (không bị kẹt lặp Deadlock). |
| 25 | **Pickup** | Dịch vụ Shipper của ĐVVC đến tận kho của Seller để lấy hàng. |
| 26 | **Processing Time (PT)** | Thời gian làm việc thực tế chạm trực tiếp vào tác vụ. |
| 27 | **RACI Matrix** | Bảng phân công trách nhiệm: Responsible, Accountable, Consulted, Informed. |
| 28 | **SiPOC Diagram** | Khung nhìn tổng quát quy trình gồm Supplier, Input, Process, Output, Customer. |
| 29 | **TO-BE Model** | Mô hình quy trình tương lai lý tưởng sau khi đã cải tiến tối ưu. |
| 30 | **Waiting Time (WT)** | Thời gian chết chờ đợi trong quy trình (WT = CT - PT). |

---

# DANH MỤC HÌNH VẼ

- **Hình 1.1:** Sơ đồ cơ cấu tổ chức Lazada Việt Nam
- **Hình 2.1:** Sơ đồ kiến trúc quy trình nghiệp vụ Lazada
- **Hình 3.1:** Sơ đồ SiPOC quy trình xử lý đơn hàng online
- **Hình 3.2:** Sơ đồ BPMN quy trình xử lý đơn hàng online (AS-IS)
- **Hình 3.3:** Biểu đồ Pareto phân bố lãng phí quy trình
- **Hình 3.4:** Sơ đồ BPMN quy trình quản lý nhà bán hàng (AS-IS)
- **Hình 3.5:** Sơ đồ BPMN quy trình quản lý tranh chấp và rủi ro (AS-IS)
- **Hình 3.6:** Sơ đồ BPMN quy trình hoàn trả và hoàn tiền (AS-IS)
- **Hình 3.7:** Sơ đồ BPMN quy trình chăm sóc khách hàng (AS-IS)
- **Hình 3.8:** Sơ đồ BPMN quy trình marketing và khuyến mãi (AS-IS)
- **Hình 3.9:** Sơ đồ BPMN quy trình xử lý đơn hàng online (TO-BE)
- **Hình 3.10:** Sơ đồ BPMN quy trình quản lý nhà bán hàng (TO-BE)
- **Hình 3.11:** Sơ đồ BPMN quy trình quản lý tranh chấp và rủi ro (TO-BE)
- **Hình 3.12:** Sơ đồ BPMN quy trình hoàn trả và hoàn tiền (TO-BE)
- **Hình 3.13:** Sơ đồ BPMN quy trình chăm sóc khách hàng (TO-BE)
- **Hình 3.14:** Sơ đồ BPMN quy trình marketing và khuyến mãi (TO-BE)
- **Hình 3.15:** Sơ đồ BPMN quy trình nhân sự & đào tạo (AS-IS)
- **Hình 3.16:** Sơ đồ BPMN quy trình nhân sự & đào tạo (TO-BE)
- **Hình 3.17:** Sơ đồ BPMN quy trình thanh toán & đối soát (AS-IS)
- **Hình 3.18:** Sơ đồ BPMN quy trình thanh toán & đối soát (TO-BE)
- **Hình 3.19:** Sơ đồ BPMN quy trình logistics & giao nhận (AS-IS)
- **Hình 3.20:** Sơ đồ BPMN quy trình logistics & giao nhận (TO-BE)
- **Hình 3.21:** Sơ đồ BPMN quy trình vận hành CNTT (AS-IS)
- **Hình 3.22:** Sơ đồ BPMN quy trình vận hành CNTT (TO-BE)

---

# DANH MỤC BẢNG

- **Bảng 1.1:** Thông tin quy mô Lazada Việt Nam
- **Bảng 1.2:** Thị phần TMĐT Việt Nam (2024)
- **Bảng 1.3:** Mô hình phí hoa hồng theo ngành hàng
- **Bảng 2.1:** Bảng tổng hợp 10 quy trình nghiệp vụ Lazada
- **Bảng 3.1:** Thống kê các thành phần sơ đồ BPMN Xử lý Đơn hàng
- **Bảng 3.2:** Bảng phân tích Giá trị gia tăng quy trình Xử lý Đơn hàng
- **Bảng 3.3:** Bảng phân tích Lãng phí quy trình Xử lý Đơn hàng
- **Bảng 3.4:** Bảng tính toán Thời gian chu kỳ các giai đoạn trong quy trình
- **Bảng 3.5:** Bảng phân bổ Chi phí xử lý biên 1 đơn hàng thành công
- **Bảng 3.6:** Phân tích Định tính & Định lượng Quản lý Nhà bán hàng
- **Bảng 3.7:** Phân tích Định tính & Định lượng Quản lý Tranh chấp
- **Bảng 3.8:** Phân tích Giá trị Gia tăng (VA/BVA/NVA) quy trình Hoàn trả & Hoàn tiền
- **Bảng 3.9:** Bảng tính toán Thời gian chu kỳ & Chi phí xử lý 1 đơn Hoàn trả
- **Bảng 3.10:** Phân tích Giá trị gia tăng (VA/BVA/NVA) quy trình CSKH
- **Bảng 3.11:** Phân tích Định tính & Định lượng Marketing
- **Bảng 3.12:** Ma trận RACI cho các hoạt động chính trong hệ thống quy trình
- **Bảng 3.13:** Bảng tổng hợp giải pháp cải tiến TO-BE cho 10 quy trình
- **Bảng C.1:** Kế hoạch thực hiện đồ án 12 tuần (Gantt Chart)
- **Bảng D.1:** Danh mục 30 Thuật ngữ Quản trị Quy trình & TMĐT Lazada

---
**HẾT BÁO CÁO**

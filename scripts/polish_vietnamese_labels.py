#!/usr/bin/env python3
"""
Polish Vietnamese diacritics and naming conventions for all BPMN elements.
"""

import glob
import xml.etree.ElementTree as ET

NS_BPMN = "http://www.omg.org/spec/BPMN/20100524/MODEL"
ET.register_namespace("bpmn", NS_BPMN)
ET.register_namespace("bpmndi", "http://www.omg.org/spec/BPMN/20100524/DI")
ET.register_namespace("dc", "http://www.omg.org/spec/DD/20100524/DC")
ET.register_namespace("di", "http://www.omg.org/spec/DD/20100524/DI")
ET.register_namespace("xsi", "http://www.w3.org/2001/XMLSchema-instance")

NS = {"bpmn": NS_BPMN}

DICTIONARY = {
    # 02 Dispute
    "Tao dispute + ly do": "Tạo khiếu nại tranh chấp",
    "Auto-collect order data": "Tự động thu thập dữ liệu đơn hàng",
    "AI triage: simple/complex": "AI phân loại tranh chấp (Đơn giản/Phức tạp)",
    "Notify ca 2 ben": "Thông báo cho Buyer & Seller",
    "AI tu giai quyet": "AI tự động xử lý giải quyết",
    "Bo sung evidence (neu co)": "Bổ sung bằng chứng (Ảnh/Video)",
    "Seller phan hoi (<=48h)": "Seller phản hồi bằng chứng (≤48h)",
    "CS review toan bo evidence": "CS thẩm định hồ sơ tranh chấp",
    "CS dua quyet dinh": "CS đưa ra phán quyết",
    "Buyer thang?": "Buyer thắng khiếu nại?",
    "Dong thuan?": "Hai bên đồng thuận phán quyết?",
    "Chuyen len senior team": "Chuyển lên Hội đồng Khiếu nại Cấp cao",
    "Senior review + decision": "Hội đồng thẩm định & ra quyết định cuối",
    "Quyet dinh cuoi?": "Phán quyết cuối cùng?",
    "Giai quyet xong": "Tranh chấp giải quyết xong",
    "Tranh chap bac bo": "Tranh chấp bị bác bỏ",
    
    # 02 Dispute TO-BE
    "Tao dispute + ly do": "Tạo tranh chấp & lý do",
    "Upload evidence co cau truc (anh/video theo danh muc)": "Upload bằng chứng chuẩn hóa",
    "Tu dong thu thap du lieu don hang": "Hệ thống tự động trích xuất log đơn hàng",
    "AI phan loai evidence (anh/video) tu dong": "AI Vision phân tích & kiểm định bằng chứng",
    "Case ro rang & gia tri <200k?": "Bằng chứng rõ ràng & Giá trị <200k?",
    "Tu dong hoan tien (case ro rang <200k)": "Tự động Instant Refund (<200k)",
    "Thong bao 2 ben kem SLA dong": "Gửi thông báo & kích hoạt SLA tự động",
    "Seller phan hoi evidence trong SLA": "Seller nộp bằng chứng phản biện",
    "CS review evidence da duoc AI phan loai": "CS thẩm định hồ sơ (đã qua AI chấm điểm)",
    "CS dua quyet dinh": "CS ban hành quyết định",
    "Ket qua xu ly?": "Kết quả xử lý tranh chấp?",
    "Chuyen len escalation team": "Chuyển Hội đồng Trọng tài Escalation",
    "Senior review + quyet dinh cuoi": "Hội đồng phê duyệt phán quyết tối hậu",
    "Quyet dinh senior?": "Phán quyết của Senior?",
    "Hoan tat giai quyet (hoan tien/boi thuong)": "Thực thi hoàn tiền / bồi thường",
    "Giai quyet xong": "Tranh chấp xử lý hoàn tất",
    "Tranh chap bac bo": "Bác bỏ khiếu nại gian lận",

    # 03 Order Processing
    "Xem lai don hang": "Xem lại chi tiết giỏ hàng",
    "Thanh toan don hang": "Thực hiện thanh toán đơn hàng",
    "Phuong thuc thanh toan?": "Phương thức thanh toán?",
    "Validate thong tin don": "Validate thông tin & địa chỉ",
    "Gateway verify thanh toan": "Cổng thanh toán xác thực giao dịch",
    "Giu tien tam thoi (COD)": "Ghi nhận trạng thái Escrow (COD)",
    "Khoa inventory + tao don": "Khóa tồn kho & tạo đơn hàng",
    "Kiem tra gian lan (AI)": "AI kiểm tra gian lận & voucher",
    "Gian lan?": "Phát hiện gian lận?",
    "Kiem tra ton kho": "Kiểm tra số lượng tồn kho khả dụng",
    "Con hang?": "Còn hàng trong kho?",
    "Seller phan hoi trong 48h?": "Seller xác nhận trong 48h?",
    "Seller xac nhan don": "Seller xác nhận chuẩn bị hàng",
    "Seller dong goi": "Seller đóng gói & dán phiếu gửi",
    "Ban giao hang cho 3PL": "Bàn giao hàng cho ĐVVC SPX",
    "3PL pickup": "SPX lấy hàng & quét barcode tại kho",
    "Tao van don tu dong": "Tạo mã vận đơn & định tuyến Hub",
    "Tracking real-time": "Cập nhật định vị đơn hàng realtime",
    "Giao hang (attempt)": "Shipper giao hàng tận nơi",
    "Giao thanh cong?": "Giao hàng thành công?",
    "Dem so lan giao lai": "Đếm số lần giao thất bại",
    "Retry < 3?": "Số lần thử lại ≤ 3 lần?",
    "Nhan hang tu shipper": "Buyer nhận hàng & kiểm tra ngoại quan",
    "Xac nhan da nhan hang": "Buyer nhấn 'Đã nhận được hàng'",
    "Buyer da confirm?": "Buyer xác nhận đơn hàng?",
    "Auto-confirm (7 ngay)": "Hệ thống tự động xác nhận sau 7 ngày",
    "Giai ngan cho Seller": "Giải ngân tiền vào Ví Shopee của Seller",
    "Don hoan tat": "Đơn hàng hoàn tất thành công",
    "Buyer huy don": "Buyer yêu cầu hủy đơn hàng",
    "Don bi huy": "Đơn hàng đã bị hủy",
    "Auto-cancel don": "Hệ thống tự động hủy đơn",
    "Auto-cancel (Seller timeout 48h)": "Hủy đơn do Seller quá hạn 48h",
    "Thong bao huy don": "Gửi thông báo hủy đơn cho 2 bên",
    "Don da thanh toan online?": "Đơn đã thanh toán trực tuyến?",
    "Auto-refund Buyer": "Tự động hoàn tiền cho Buyer",
    "Execute refund": "Thực hiện hoàn tiền qua Cổng thanh toán",
    "Da refund": "Tiền đã hoàn về tài khoản Buyer",

    # 03 Order TO-BE
    "Tao don hang": "Buyer đặt hàng & chọn voucher",
    "Thanh toan don hang": "Thanh toán qua ShopeePay/SPayLater",
    "Phuong thuc thanh toan?": "Phương thức thanh toán?",
    "Validate tu dong": "Validate địa chỉ & GPS Autocomplete",
    "Cổng thanh toán verify": "Cổng thanh toán xác thực tức thì",
    "Khóa inventory & tao don": "Khóa tồn kho Real-time & tạo đơn",
    "Kiem tra gian lan AI": "AI Fraud Detection phát hiện gian lận",
    "Gian lan?": "Phát hiện gian lận?",
    "Shop Mall?": "Gian hàng Shopee Mall?",
    "Auto-confirm don Mall (2h)": "Tự động xác nhận đơn Mall (2h)",
    "Seller xac nhan don (SLA 12h)": "Seller xác nhận đơn (SLA 12h)",
    "Seller dong goi": "Seller đóng gói & in Smart AWB",
    "Ban giao SPX Hub": "Bàn giao SPX Smart Sorting Hub",
    "Smart Routing & GPS Tracking": "Định tuyến thông minh & GPS Tracking",
    "Giao hang chot hen gio": "Shipper giao hàng theo khung giờ hẹn",
    "Giao thanh cong?": "Giao hàng thành công?",
    "Nhan hang & danh gia": "Buyer nhận hàng & đánh giá 5 sao",
    "Buyer confirm?": "Buyer bấm xác nhận?",
    "Tu dong xac nhan sau 3 ngay": "Tự động giải ngân sau 3 ngày",
    "Giai ngan tuc thi qua vi ShopeePay": "Giải ngân tức thì vào Ví ShopeePay",
    "Don hoan tat": "Đơn hàng hoàn tất mỹ mãn",
    "Tu dong huy don": "Hệ thống tự động hủy đơn",
    "Don da thanh toan online?": "Đơn thanh toán trực tuyến?",
    "Instant Refund": "Instant Refund hoàn tiền tức thì",
    "Execute refund": "Cổng thanh toán xử lý hoàn tiền",
    "Da hoan tien": "Tiền đã hoàn về ví Buyer",

    # 04 Return AS-IS
    "Submit yeu cau + ly do": "Gửi yêu cầu Trả hàng / Hoàn tiền",
    "Check eligibility tu dong": "Hệ thống kiểm tra điều kiện trả hàng",
    "Hop le?": "Đơn hàng còn hạn đổi trả?",
    "Yeu cau bi tu choi": "Yêu cầu bị từ chối do quá hạn",
    "Upload evidence (anh/video)": "Upload ảnh/video khuyết tật sản phẩm",
    "AI triage evidence": "AI phân loại bằng chứng khiếu nại",
    "Low-risk (<200k)?": "Đơn giá trị nhỏ (<200k) & Shop uy tín?",
    "CS review evidence": "CS thẩm định hồ sơ khiếu nại",
    "CS approve?": "CS phê duyệt yêu cầu đổi trả?",
    "Ban giao hang tra cho 3PL": "Buyer bàn giao hàng hoàn cho SPX",
    "Scheduled pickup slot": "Đặt lịch hẹn Shipper đến lấy hàng hoàn",
    "3PL pickup hang tra": "SPX thu hồi bưu kiện hoàn trả",
    "Inspect hang tra ve (<=12h)": "Kho SPX kiểm định hàng hoàn (≤12h)",
    "Inspection pass?": "Hàng hoàn đúng hiện trạng & đủ phụ kiện?",
    "Auto-notify tung buoc": "Gửi thông báo tiến độ cho Buyer & Seller",
    "Refund cho Buyer": "Kích hoạt lệnh hoàn tiền",
    "Refund hoan tat": "Hoàn tiền cho Buyer hoàn tất",

    # 04 Return TO-BE
    "Submit yeu cau tra hang": "Gửi yêu cầu Trả hàng & Hoàn tiền",
    "Check eligibility tu dong": "Hệ thống kiểm tra điều kiện trả hàng",
    "Hop le?": "Đủ điều kiện đổi trả?",
    "Yeu cau bi tu choi": "Yêu cầu bị từ chối",
    "Upload evidence (Smart Photo/Video)": "Upload hình ảnh/video Smart Proof",
    "AI triage: low-risk vs normal": "AI phân loại rủi ro khiếu nại",
    "Low-risk (<200k)?": "Đơn giá trị <200k & Buyer tín nhiệm cao?",
    "AI verify evidence": "AI Vision thẩm định lỗi bao bì/sản phẩm",
    "AI pass?": "AI xác thực lỗi đạt độ tin cậy >95%?",
    "CS review (khi AI khong chac)": "CS hỗ trợ thẩm định ca nghi vấn",
    "Instant refund (item-less)": "Instant Refund - Hoàn tiền tức thì (Không cần trả hàng)",
    "SLA 24h refund": "Kích hoạt hoàn tiền tự động trong 24h",
    "Dynamic pickup scheduling": "Lên lịch thu hồi hàng thông minh",
    "Ban giao hang tra cho 3PL": "Buyer bàn giao bưu kiện hoàn cho Shipper",
    "3PL pickup hang tra": "SPX thu hồi bưu kiện hoàn",
    "AI Image Analysis Inspection": "AI Camera quét mã & ngoại quan tại Hub",
    "Process refund (SLA 24h)": "Xử lý lệnh hoàn tiền tự động",
    "Execute refund qua gateway": "Cổng thanh toán giải ngân tiền hoàn",
    "Auto-notify tung buoc": "Thông báo tiến độ realtime qua App",
    "Refund hoan tat": "Hoàn tất Trả hàng & Hoàn tiền",

    # 05 CS AS-IS
    "Khach hang lien he CS": "Khách hàng liên hệ Trung tâm CSKH",
    "Kenh tiep nhan?": "Kênh tiếp nhận hỗ trợ?",
    "Phan loai intent": "AI NLP phân loại ý định & mức độ khẩn cấp",
    "Kiem tra SLA ticket": "Hệ thống kiểm tra SLA xử lý ticket",
    "SLA con hieu luc?": "SLA còn thời hạn xử lý?",
    "Chatbot xu ly duoc?": "Chatbot có sẵn kịch bản trả lời?",
    "Chatbot tu giai quyet": "Chatbot tự động giải đáp thắc mắc",
    "Chatbot giai quyet xong?": "Khách hàng hài lòng với Chatbot?",
    "Fetch order/user context": "Hệ thống trích xuất thông tin đơn & tài khoản",
    "CS Tier 1 xu ly": "Chuyên viên CS Tier 1 tiếp nhận & hỗ trợ",
    "Tier 1 giai quyet xong?": "CS Tier 1 xử lý dứt điểm?",
    "Chuyen CS Tier 2": "Chuyển tiếp lên CS Tier 2 chuyên sâu",
    "CS Tier 2 xu ly": "Chuyên viên CS Tier 2 phối hợp nội bộ/3PL",
    "Tier 2 giai quyet xong?": "CS Tier 2 giải quyết thành công?",
    "Xac nhan da giai quyet": "Khách hàng xác nhận vấn đề đã giải quyết",
    "Khach dong y ket qua?": "Khách hàng đồng ý phương án xử lý?",
    "Ghi log phien + luu CSAT": "Lưu lịch sử hội thoại & điểm CSAT",
    "Danh gia CSAT": "Khách hàng chấm điểm khảo sát CSAT",
    "CSAT >= 4*?": "Điểm đánh giá CSAT ≥ 4 sao?",
    "Quality follow up / training": "Bộ phận QA kiểm toán chất lượng cuộc gọi",
    "Escalate ticket vuot SLA": "Cảnh báo khẩn cấp ticket vượt SLA",
    "Tiep nhan ticket": "Trưởng nhóm CS tiếp nhận ticket trễ hạn",
    "Xu ly ticket noi bo / 3PL": "Đôn đốc xử lý với phòng ban / ĐVVC",
    "Cap nhat ket qua cho customer": "Cập nhật tiến độ xử lý cho khách hàng",
    "Issue da giai quyet": "Vấn đề khiếu nại đã giải quyết hoàn tất",
    "Mo lai van de": "Khách hàng yêu cầu mở lại khiếu nại",

    # 05 CS TO-BE
    "Khach hang lien he CS": "Khách hàng mở yêu cầu hỗ trợ",
    "Kenh tiep nhan?": "Kênh tương tác?",
    "Khach chu dong lien he": "Khách hàng chủ động chat/gọi",
    "He thong ra soat at-risk": "Hệ thống AI chủ động rà soát đơn rủi ro",
    "Chon van de tu thuc don huong dan": "Chọn chủ đề trợ giúp thông minh",
    "Khach phan hoi ve don hang": "Nhập nội dung cần hỗ trợ",
    "Chu dong lien he don hang co rui ro": "AI chủ động gửi tin nhắn hỗ trợ trước",
    "Khach can ho tro them?": "Khách cần gặp tư vấn viên?",
    "Da thoa man cho don hang luc giao?": "Khách hàng đã yên tâm?",
    "AI phan loai intent tu dong": "AI LLM hiểu ngữ cảnh & phân tích cảm xúc",
    "AI phan tich cam xuc khach": "Đo lường mức độ hài lòng / bức xúc",
    "Can ho tro nguoi": "Yêu cầu chuyển gặp chuyên viên",
    "Binh thuong": "Trạng thái cảm xúc bình thường",
    "Tu dong lay context don hang": "Hệ thống gắn sẵn toàn bộ log đơn hàng",
    "Chatbot tu tin giai quyet (80%)?": "Chatbot AI tự tin xử lý (≥80%)?",
    "Tra loi tu dong tu Knowledge Base": "GenAI trả lời tức thì từ Knowledge Base",
    "20% chuyen nguoi": "Chuyển tư vấn viên khi vượt khả năng AI",
    "CS Tier 1 xu ly (kem context tu dong)": "CS Tier 1 xử lý nhanh với gợi ý từ Copilot",
    "Tier 1 ket qua xu ly?": "Kết quả xử lý của CS Tier 1?",
    "CS Tier 2 xu ly chuyen sau": "CS Tier 2 xử lý nghiệp vụ phức tạp",
    "Tier 2 ket qua?": "Kết quả xử lý của CS Tier 2?",
    "Thong bao Supervisor khi vuot SLA": "Cảnh báo tự động Supervisor khi trễ hạn",
    "Xac nhan da giai quyet": "Khách hàng bấm xác nhận hoàn tất hỗ trợ",
    "Danh gia CSAT (2 cau hoi)": "Khảo sát nhanh 2 câu hỏi CSAT / CES",
    "Tu dong gui khao sat CSAT": "Hệ thống tự động gửi form đánh giá",
    "Ghi log phien + luu CSAT tu dong": "Lưu log & tự động chấm điểm QA bằng AI",
    "Issue da giai quyet": "Phiên hỗ trợ kết thúc thành công",

    # 06 Marketing AS-IS
    "Y tuong campaign": "Khởi tạo ý tưởng Chiến dịch Khuyến mãi",
    "Research + brief": "Nghiên cứu thị trường & lập bản đề xuất",
    "Design concept + plan": "Thiết kế concept & lập kế hoạch chi tiết",
    "Kiem tra tuan thu": "Kiểm tra tính tuân thủ pháp lý khuyến mãi",
    "Tuan thu?": "Đạt chuẩn pháp lý & chính sách sàn?",
    "Review ngan sach": "Thẩm định ngân sách & tỷ suất ROI",
    "Ngan sach?": "Ngân sách có vượt hạn mức cơ bản?",
    "Director approve (large budget)": "Giám đốc Khối phê duyệt ngân sách lớn",
    "Auto-invite sellers": "Hệ thống gửi lời mời tham gia đến Sellers",
    "Seller xac nhan tham gia": "Seller xem xét thư mời chiến dịch",
    "Seller xac nhan?": "Seller đồng ý tham gia?",
    "Seller dang ky tham gia": "Seller nộp danh sách sản phẩm khuyến mãi",
    "Seller chuan bi san pham + khuyen mai": "Seller chuẩn bị tồn kho & cài đặt giá sốc",
    "Config campaign (template)": "Cấu hình chiến dịch trên hệ thống",
    "Auto-test voucher": "Hệ thống kiểm tra & giả lập áp mã voucher",
    "Trung voucher?": "Phát hiện xung đột / chồng chéo voucher?",
    "Tu dong giai quyet xung dot khuyen mai": "Tự động phân tách & giải quyết xung đột mã",
    "Voucher test OK?": "Kiểm thử voucher thành công?",
    "QA campaign truoc launch": "Kiểm toán QA toàn diện trước giờ G",
    "QA pass?": "Chiến dịch vượt qua bài test QA?",
    "Launch campaign": "Kích hoạt Chiến dịch Khuyến mãi (Go-Live)",
    "Buyer browse campaign": "Buyer truy cập săn deal Mega Sale",
    "Buyer mua hang": "Buyer đặt hàng áp mã giảm giá sàn",
    "Monitor performance real-time": "Theo dõi hiệu năng hệ thống & doanh số realtime",
    "Auto-generate report": "Hệ thống tự động xuất báo cáo sơ bộ",
    "Cho/bo sung du lieu report": "Thu thập bổ sung số liệu đối soát",
    "Bao cao du lieu day du?": "Số liệu báo cáo đã đầy đủ?",
    "Bao cao post-campaign": "Lập báo cáo tổng kết & đánh giá ROI",
    "Campaign hoan tat": "Chiến dịch kết thúc thành công",

    # 06 Marketing TO-BE
    "Y tuong chien dich": "Khởi tạo Ý tưởng Chiến dịch Siêu Sale",
    "Nghien cuu thi truong + brief": "AI Market Insights phân tích xu hướng & lập Brief",
    "Thiet ke concept + ke hoach": "Thiết kế Concept & Kế hoạch ngân sách động",
    "AI phan bo ngan sach": "AI tối ưu phân bổ ngân sách theo ngành hàng",
    "Ngan sach vuot nguong?": "Ngân sách vượt ngưỡng phê duyệt tự động?",
    "Giam doc phe duyet (ngan sach lon)": "Giám đốc phê duyệt ngân sách đặc biệt",
    "Ca nhan hoa loi moi seller": "AI cá nhân hóa lời mời cho từng Top Seller",
    "Tach luong chuan bi": "Kích hoạt luồng chuẩn bị song song",
    "Seller dang ky tham gia": "Seller xác nhận tham gia trên Seller Centre",
    "Seller chuan bi san pham + voucher": "Seller chuẩn bị hàng & cài đặt Flash Sale",
    "SLA chuan bi cua seller (48h)": "Thời hạn Seller chuẩn bị hàng (48h)",
    "Config campaign tu dong tu template": "Tự động cấu hình chiến dịch qua Smart Template",
    "San sang launch?": "Tất cả các luồng đã sẵn sàng Go-Live?",
    "Auto QA check": "AI Smart QA kiểm thử tự động 100% voucher",
    "Launch campaign": "Kích hoạt Chiến dịch Siêu Sale trên toàn sàn",
    "Tach luong van hanh & mua sam": "Vận hành song song: Mua sắm & Giám sát hệ thống",
    "Buyer xem khuyen mai": "Buyer săn Deal & chốt đơn Livestream",
    "Buyer mua hang": "Buyer thanh toán áp mã FreeShip & Shopee Voucher",
    "Giam sat ROAS real-time": "AI Dashboard theo dõi ROAS & GMV Real-time",
    "Giam sat bot gian lan voucher": "AI Anti-Fraud ngăn chặn bot gom voucher",
    "Cap nhat dashboard real-time": "Cập nhật biểu đồ doanh số từng giây",
    "Auto-report sau chien dich + ML insight": "AI tự động xuất Báo cáo ROI & Đề xuất cải tiến",
    "Dong bo ket thuc chien dich": "Đồng bộ kết thúc các luồng vận hành",
    "QA pass?": "Đạt chuẩn kiểm toán sau chiến dịch?",
    "Chien dich hoan tat": "Chiến dịch Siêu Sale thành công rực rỡ",
    "Het thoi gian chien dich": "Hết thời gian chiến dịch"
}

def polish_file(filepath):
    tree = ET.parse(filepath)
    root = tree.getroot()
    process = root.find(".//bpmn:process", NS)
    if process is None:
        return
    
    count = 0
    for elem in process.iter():
        name = elem.get("name")
        if name:
            trimmed = name.strip()
            if trimmed in DICTIONARY:
                elem.set("name", DICTIONARY[trimmed])
                count += 1
            else:
                # partial replacement
                for k, v in DICTIONARY.items():
                    if trimmed == k:
                        elem.set("name", v)
                        count += 1
                        break
                        
    tree.write(filepath, encoding="UTF-8", xml_declaration=True)
    print(f"Polished {filepath}: updated {count} element names.")

for f in sorted(glob.glob("processes/*.bpmn") + glob.glob("processes-to-be/*.bpmn")):
    polish_file(f)

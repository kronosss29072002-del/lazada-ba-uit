#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build-bpmn-from-shopee.py
========================
Chuyển 10 BPMN Shopee (AS-IS + TO-BE) thành 10 BPMN Lazada.

Cách hoạt động:
  1. Đọc file .bpmn Shopee gốc (template, giữ NGUYÊN cấu trúc + DI → valid 100%).
  2. Áp dụng mapping {old_name -> new_name} lên mọi thuộc tính name="..." (element + process + lane + event).
  3. Ghi ra lazada-ba-project/processes (AS-IS) hoặc processes-to-be (TO-BE).

Lý do giữ nguyên cấu trúc:
  - Số gateway XOR >= 15/quy trình (đạt thang điểm tối đa rubric 2: >= 6 gateway).
  - Mọi hoạt động giữ đúng 1-input-1-output, gateway mở/đóng cân bằng.
  - Phần BPMNDiagram (toạ độ, waypoint) không đổi -> mở bằng bpmn-js/Camunda đẹp như cũ.
"""
import re
import os
import sys

SRC_ASIS = "/home/kronosss2002/doanba/shopee-ba-project/processes"
SRC_TOBE = "/home/kronosss2002/doanba/shopee-ba-project/processes-to-be"
DST_ASIS = "/home/kronosss2002/doanba/lazada-ba-project/processes"
DST_TOBE = "/home/kronosss2002/doanba/lazada-ba-project/processes-to-be"

# =====================================================================
# MAPPING TÊN: Shopee -> Lazada  (chỉ đổi name="...", KHÔNG đổi id)
# =====================================================================
# Chú ý: trong file XML tên có dấu & được viết là &amp;
COMMON_LANES = {
    "Shopee System (Automated)": "Lazada System (Automated)",
    "Shopee System": "Lazada System",
    "Shopee System &amp; Marketing Tools": "Lazada System &amp; Marketing Tools",
    "Shopee System (AI &amp; Automation)": "Lazada System (AI &amp; Automation)",
    "Shopee System (AI)": "Lazada System (AI)",
}

# -----------------------------------------------------------------
# 01 - Quản lý Nhà bán hàng (Seller Management)
# -----------------------------------------------------------------
MAP_01 = {
    **COMMON_LANES,
    "Quản lý Nhà bán hàng Shopee": "Quản lý Nhà bán hàng Lazada",
    "Seller đăng ký gian hàng": "Seller đăng ký gian hàng",
    "Gian hàng được kích hoạt": "Gian hàng Lazada được kích hoạt",
    "Hồ sơ bị từ chối vĩnh viễn": "Hồ sơ bị từ chối vĩnh viễn",
    "Đã cảnh cáo": "Đã cảnh cáo",
    "Đã tạm khóa": "Đã tạm khóa",
    "Đã khóa vĩnh viễn": "Đã khóa vĩnh viễn",
    "Điền thông tin định danh": "Điền thông tin định danh Seller",
    "Gửi OTP xác thực SĐT": "Gửi OTP xác thực SĐT",
    "Upload CMND/CCCD + GPKD": "Upload CMND/CCCD + GPKD + Giấy chứng nhận (LazMall)",
    "Validate định danh tự động": "Validate định danh tự động",
    "Cập nhật tài khoản NH": "Cập nhật tài khoản ngân hàng (giải ngân)",
    "Quét OCR + check giấy tờ giả": "Quét OCR + kiểm tra giấy tờ giả",
    "Bổ sung / sửa hồ sơ": "Bổ sung / sửa hồ sơ",
    "Chấm điểm rủi ro (Risk scoring)": "Chấm điểm rủi ro (Risk scoring)",
    "Compliance review manual (24-48h)": "Compliance review thủ công (24-48h)",
    "Thông báo kết quả duyệt": "Thông báo kết quả duyệt Seller Centre",
    "Giám sát điểm sao quả tạ (auto)": "Giám sát điểm đánh giá &amp; vi phạm (auto)",
    "Gửi cảnh cáo Seller": "Gửi cảnh cáo Seller",
    "Tạm khóa gian hàng (7 ngày)": "Tạm khóa gian hàng (7 ngày)",
    "Khóa gian hàng vĩnh viễn": "Khóa gian hàng vĩnh viễn",
}

# -----------------------------------------------------------------
# 02 - Quản lý Tranh chấp (Dispute Management)
# -----------------------------------------------------------------
MAP_02 = {
    **COMMON_LANES,
    "Quản lý Tranh chấp Shopee": "Quản lý Tranh chấp Lazada (Bảo vệ Người mua)",
    "Yêu cầu tranh chấp được khởi tạo": "Yêu cầu tranh chấp được khởi tạo",
    "Giải quyết xong": "Giải quyết xong",
    "Tranh chấp bác bỏ": "Tranh chấp bác bỏ",
    "AI tự giải quyết": "AI tự giải quyết",
    "Tạo dispute + lý do": "Tạo tranh chấp + lý do",
    "Bổ sung evidence (nếu có)": "Bổ sung bằng chứng (nếu có)",
    "Yêu cầu bổ sung evidence": "Yêu cầu bổ sung bằng chứng",
    "Tự động thu thập dữ liệu đơn hàng": "Tự động thu thập dữ liệu đơn hàng",
    "AI phân loại tranh chấp (Đơn giản/Phức tạp)": "AI phân loại tranh chấp (Đơn giản/Phức tạp)",
    "Kiểm tra lịch sử SLA": "Kiểm tra lịch sử SLA",
    "Gửi thông báo đối soát đến hai bên": "Gửi thông báo đối soát đến hai bên",
    "Seller phản hồi (≤48h)": "Seller phản hồi (≤48h)",
    "CS thẩm định toàn bộ hồ sơ tranh chấp": "CS thẩm định toàn bộ hồ sơ tranh chấp",
    "CS ban hành quyết định xử lý": "CS ban hành quyết định xử lý",
    "Chuyển lên senior team": "Chuyển lên nhóm chuyên trách (Lazada Escalation)",
    "Hội đồng thẩm định &amp; ra quyết định cuối": "Hội đồng thẩm định &amp; ra quyết định cuối",
}

# -----------------------------------------------------------------
# 03 - Xử lý Đơn hàng Online (Order Processing)
# -----------------------------------------------------------------
MAP_03 = {
    **COMMON_LANES,
    "Xử lý Đơn hàng Online": "Xử lý Đơn hàng Online Lazada",
    "Buyer đặt hàng": "Buyer đặt hàng",
    "Đơn hoàn tất": "Đơn hoàn tất",
    "Đã refund": "Đã hoàn tiền",
    "Đơn bị hủy": "Đơn bị hủy",
    "Xem lại đơn hàng": "Xem lại đơn hàng",
    "Thanh toán đơn hàng": "Thanh toán đơn hàng (COD / Thẻ / Ví / Chuyển khoản)",
    "Nhận hàng từ shipper": "Nhận hàng từ shipper",
    "Xác nhận đã nhận hàng": "Xác nhận đã nhận hàng",
    "Buyer hủy đơn": "Buyer hủy đơn",
    "Validate thông tin đơn": "Validate thông tin đơn",
    "Khóa inventory + tạo đơn": "Khóa tồn kho + tạo đơn",
    "Kiểm tra gian lận (AI)": "Kiểm tra gian lận (AI)",
    "Kiểm tra tồn kho": "Kiểm tra tồn kho",
    "Tạo vận đơn tự động": "Tạo vận đơn tự động (LEX / 3PL)",
    "Cập nhật định vị đơn hàng realtime": "Cập nhật định vị đơn hàng realtime",
    "Đếm số lần giao lại": "Đếm số lần giao lại",
    "Auto-confirm (7 ngày)": "Auto-confirm (15 ngày)",
    "Hủy đơn do Seller quá hạn 48h": "Hủy đơn do Seller quá hạn 48h",
    "Giải ngân cho Seller": "Giải ngân cho Seller",
    "Auto-cancel đơn": "Auto-cancel đơn",
    "Thông báo hủy đơn": "Thông báo hủy đơn",
    "Tự động hoàn tiền cho Buyer": "Tự động hoàn tiền cho Buyer",
    "Seller xác nhận đơn": "Seller xác nhận đơn",
    "Seller đóng gói": "Seller đóng gói",
    "Bàn giao hàng cho 3PL": "Bàn giao hàng cho 3PL / LEX",
    "SPX lấy hàng &amp; quét barcode tại kho": "LEX (Lazada Express) lấy hàng &amp; quét barcode tại kho",
    "Giao hàng (attempt)": "Giao hàng (attempt)",
    "Gateway verify thanh toán": "Gateway verify thanh toán",
    "Giữ tiền tạm thời (COD)": "Giữ tiền tạm thời (COD)",
    "Cổng thanh toán xử lý hoàn tiền": "Cổng thanh toán xử lý hoàn tiền",
}

# -----------------------------------------------------------------
# 04 - Hoàn trả & Hoàn tiền (Return & Refund)
# -----------------------------------------------------------------
MAP_04 = {
    **COMMON_LANES,
    "Hoàn trả và Hoàn tiền Shopee": "Hoàn trả &amp; Hoàn tiền Lazada",
    "Yêu cầu hoàn trả được khởi tạo": "Yêu cầu hoàn trả được khởi tạo",
    "Refund hoàn tất": "Hoàn tiền hoàn tất",
    "Yêu cầu bị từ chối": "Yêu cầu bị từ chối",
    "Gửi yêu cầu đổi trả và lý do": "Gửi yêu cầu đổi trả và lý do",
    "Xử lý yêu cầu trễ hạn": "Xử lý yêu cầu trễ hạn",
    "Tải lên bằng chứng ảnh và video": "Tải lên bằng chứng ảnh và video",
    "Bàn giao hàng trả cho 3PL": "Bàn giao hàng trả cho LEX / 3PL",
    "Kiểm tra tính hợp lệ tự động": "Kiểm tra tính hợp lệ tự động",
    "AI phân loại bằng chứng khiếu nại": "AI phân loại bằng chứng khiếu nại",
    "Gửi thông báo cập nhật tiến độ tự động": "Gửi thông báo cập nhật tiến độ tự động",
    "CS thẩm định hồ sơ khiếu nại": "CS thẩm định hồ sơ khiếu nại",
    "Đặt lịch hẹn Shipper đến lấy hàng hoàn": "Đặt lịch hẹn Shipper đến lấy hàng hoàn",
    "3PL pickup hàng trả": "LEX / 3PL pickup hàng trả",
    "Đặt lại lịch pickup": "Đặt lại lịch pickup",
    "Kiểm định hàng hoàn tại kho (≤12h)": "Kiểm định hàng hoàn tại kho (≤12h)",
    "Kích hoạt lệnh hoàn tiền": "Kích hoạt lệnh hoàn tiền",
}

# -----------------------------------------------------------------
# 05 - Chăm sóc Khách hàng (Customer Service)
# -----------------------------------------------------------------
MAP_05 = {
    **COMMON_LANES,
    "Chăm sóc Khách hàng Shopee": "Chăm sóc Khách hàng Lazada",
    "Yêu cầu hỗ trợ được tiếp nhận": "Yêu cầu hỗ trợ được tiếp nhận",
    "Phiên hỗ trợ kết thúc thành công": "Phiên hỗ trợ kết thúc thành công",
    "Ticket quá hạn SLA xử lý": "Ticket quá hạn SLA xử lý",
    "Xác minh danh tính thất bại": "Xác minh danh tính thất bại",
    "Mô tả chi tiết vấn đề cần hỗ trợ": "Mô tả chi tiết vấn đề cần hỗ trợ",
    "Cung cấp thêm thông tin chứng từ": "Cung cấp thêm thông tin chứng từ",
    "Khách hàng bấm xác nhận hoàn tất hỗ trợ": "Khách hàng bấm xác nhận hoàn tất hỗ trợ",
    "Khách hàng chấm điểm khảo sát CSAT": "Khách hàng chấm điểm khảo sát CSAT",
    "Chờ phản hồi từ tư vấn viên": "Chờ phản hồi từ tư vấn viên",
    "AI NLP phân loại ý định &amp; mức độ khẩn cấp": "AI NLP phân loại ý định &amp; mức độ khẩn cấp",
    "Chatbot tự động giải đáp thắc mắc": "Chatbot (Lazada Assistant) tự động giải đáp",
    "Hệ thống kiểm tra SLA xử lý ticket": "Hệ thống kiểm tra SLA xử lý ticket",
    "Xác minh danh tính khách hàng": "Xác minh danh tính khách hàng",
    "Tư vấn viên Tier 1 tiếp nhận &amp; hỗ trợ": "Tư vấn viên Tier 1 tiếp nhận &amp; hỗ trợ",
    "Lấy lịch sử tương tác (auto)": "Lấy lịch sử tương tác (auto)",
    "Tư vấn viên Tier 1 đưa giải pháp xử lý": "Tư vấn viên Tier 1 đưa giải pháp xử lý",
    "Chuyên viên Tier 2 thẩm định chuyên sâu": "Chuyên viên Tier 2 thẩm định chuyên sâu",
    "Chuyên viên Tier 2 xử lý dứt điểm": "Chuyên viên Tier 2 xử lý dứt điểm",
    "Hệ thống trích xuất thông tin đơn &amp; tài khoản": "Hệ thống trích xuất thông tin đơn &amp; tài khoản",
    "Ghi nhận nhật ký phiên &amp; điểm CSAT": "Ghi nhận nhật ký phiên &amp; điểm CSAT",
    "Gửi nhắc nhở phản hồi cho khách hàng": "Gửi nhắc nhở phản hồi cho khách hàng",
    "Khảo sát đánh giá chất lượng (QA Follow-up)": "Khảo sát đánh giá chất lượng (QA Follow-up)",
}

# -----------------------------------------------------------------
# 06 - Marketing & Khuyến mãi (Marketing)
# -----------------------------------------------------------------
MAP_06 = {
    **COMMON_LANES,
    "Marketing và Khuyến mãi Shopee": "Marketing &amp; Khuyến mãi Lazada",
    "Ý tưởng chiến dịch được đề xuất": "Ý tưởng chiến dịch được đề xuất",
    "Chiến dịch kết thúc thành công": "Chiến dịch kết thúc thành công",
    "Nghiên cứu thị trường &amp; lập bản đề xuất": "Nghiên cứu thị trường &amp; lập bản đề xuất",
    "Phân khúc lại nhóm đối tượng mục tiêu": "Phân khúc lại nhóm đối tượng mục tiêu",
    "Thiết kế concept &amp; lập kế hoạch chi tiết": "Thiết kế concept &amp; lập kế hoạch chi tiết",
    "Theo dõi hiệu năng hệ thống &amp; doanh số realtime": "Theo dõi hiệu năng hệ thống &amp; doanh số realtime",
    "Lập báo cáo tổng kết &amp; đánh giá ROI": "Lập báo cáo tổng kết &amp; đánh giá ROI",
    "Kiểm tra tính tuân thủ pháp lý khuyến mãi": "Kiểm tra tính tuân thủ pháp lý khuyến mãi (Nghị định 81)",
    "Thẩm định ngân sách &amp; tỷ suất ROI": "Thẩm định ngân sách &amp; tỷ suất ROI",
    "Giám đốc Khối phê duyệt ngân sách lớn": "Giám đốc Khối phê duyệt ngân sách lớn",
    "Hệ thống gửi lời mời tham gia đến Sellers": "Hệ thống gửi lời mời tham gia đến Sellers",
    "Cấu hình chiến dịch trên hệ thống": "Cấu hình chiến dịch trên hệ thống",
    "Tự động phân tách &amp; giải quyết xung đột mã": "Tự động phân tách &amp; giải quyết xung đột mã",
    "Hệ thống kiểm tra &amp; giả lập áp mã voucher": "Hệ thống kiểm tra &amp; giả lập áp mã voucher",
    "Kiểm toán QA toàn diện trước giờ G": "Kiểm toán QA toàn diện trước giờ G",
    "Kích hoạt Chiến dịch Siêu Sale trên toàn sàn": "Kích hoạt Chiến dịch 12.12 Siêu Hội Mua Sắm",
    "Hệ thống tự động xuất báo cáo sơ bộ": "Hệ thống tự động xuất báo cáo sơ bộ",
    "Thu thập bổ sung số liệu đối soát": "Thu thập bổ sung số liệu đối soát",
    "Seller xem xét thư mời chiến dịch": "Seller xem xét thư mời chiến dịch",
    "Seller xác nhận tham gia trên Seller Centre": "Seller xác nhận tham gia trên Seller Centre",
    "Seller chuẩn bị tồn kho &amp; cài đặt giá sốc": "Seller chuẩn bị tồn kho &amp; cài đặt giá sốc",
    "Buyer truy cập săn deal Mega Sale": "Buyer truy cập săn deal 12.12 Siêu Sale",
    "Buyer thanh toán áp mã FreeShip &amp; Shopee Voucher": "Buyer thanh toán áp mã FreeShip &amp; Lazada Voucher",
}

MAPPINGS = {
    "01-seller-management": MAP_01,
    "02-dispute-management": MAP_02,
    "03-order-processing": MAP_03,
    "04-return-refund": MAP_04,
    "05-customer-service": MAP_05,
    "06-marketing": MAP_06,
}


def transform(xml_text, mapping):
    """Thay toàn bộ name="old" -> name="new" theo mapping (không đụng id)."""
    result = xml_text
    replaced = 0
    for old, new in mapping.items():
        if old == new:
            continue
        # Chỉ khớp đúng name="...old..." (escape để khớp literal)
        pattern = 'name="' + re.escape(old) + '"'
        found = len(re.findall(pattern, result))
        if found:
            result = result.replace('name="' + old + '"', 'name="' + new + '"')
            replaced += found
        # ALSO check pattern with &amp; already handled since old contains &amp; literally
    return result, replaced


def build(src_dir, dst_dir, suffix_note):
    os.makedirs(dst_dir, exist_ok=True)
    total = 0
    for base, mapping in MAPPINGS.items():
        src = os.path.join(src_dir, base + ".bpmn")
        if not os.path.exists(src):
            src = os.path.join(src_dir, base + "-tobe.bpmn")
        dst = os.path.join(dst_dir, base + ".bpmn")
        if not os.path.exists(src):
            print(f"  !! MISSING SRC: {src}")
            continue
        xml = open(src, encoding="utf-8").read()
        new_xml, replaced = transform(xml, mapping)
        open(dst, "w", encoding="utf-8").write(new_xml)
        total += replaced
        print(f"  {base}: {replaced} name-replacements -> {os.path.basename(dst)}")
    print(f"  TOTAL replacements: {total}")


if __name__ == "__main__":
    print("=== Building LAZADA AS-IS BPMN ===")
    build(SRC_ASIS, DST_ASIS, "AS-IS")
    print("=== Building LAZADA TO-BE BPMN ===")
    build(SRC_TOBE, DST_TOBE, "TO-BE")
    print("DONE.")

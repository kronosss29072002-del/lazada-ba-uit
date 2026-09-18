#!/usr/bin/env python3
"""
Label branch sequence flows of split gateways with curated Vietnamese names.
Teacher rule (Buổi 10): "nhãn cổng thì có rồi đó, nhãn nhánh thì không có"
→ every split gateway's outgoing edges need visible branch labels.

Curated map: flow ID → label, derived from the flow's semantics (answer to the
gateway question / target activity). Idempotent: only sets missing names.
"""
import xml.etree.ElementTree as ET
import glob, sys

NS = 'http://www.omg.org/spec/BPMN/20100524/MODEL'
def tn(n): return f'{{{NS}}}{n}'
def local(t): return t.split('}')[-1] if '}' in t else t

CURATED = {
    # ===== processes-to-be =====
    'F14': 'Giám sát vi phạm AI',
    'F22': 'Kích hoạt gian hàng',
    'Flow_Simple_NotifyTimer': 'Khiếu nại đơn giản',
    'Flow_Complex_NotifyTimer': 'Khiếu nại phức tạp',
    'Flow_Deliver_Success': 'Giao thành công',
    'Flow_Deliver_Fail': 'Giao thất bại',
    'Flow_Eligible_Upload': 'Hồ sơ hợp lệ',
    'Flow_Eligible_Reject': 'Không hợp lệ',
    'Flow_Gate_LowRisk': 'Rủi ro thấp',
    'Flow_Gate_Handover': 'Rủi ro cao',
    'Flow_AI_Pass': 'Đạt (>95%)',
    'Flow_AI_Uncertain': 'Chưa đạt',
    'Flow_Gate_Timer': 'Hết thời gian chờ',
    'Flow_Pickup_Yes': 'Pickup thành công',
    'Flow_Pickup_No': 'Pickup thất bại',
    'Flow_Payout_Yes': 'Giải ngân thành công',
    'Flow_Payout_Retry': 'Giải ngân thất bại',
    'Flow_Invite_Config': 'Cấu hình campaign',
    'Flow_Invite_Register': 'Seller đăng ký',
    'Flow_Launch_Dashboard': 'Vận hành & theo dõi',
    'Flow_Launch_Browse': 'Buyer mua sắm',
    'Flow_Gate_Small': 'Trong hạn mức',
    'Flow_Gate_Large': 'Vượt hạn mức',
    'Flow_QA_Yes': 'Đạt chuẩn',
    'Flow_QA_No': 'Chưa đạt chuẩn',
    'Flow_Wallet_Statement': 'Gửi bảng đối soát',
    'Flow_Wallet_Check': 'Seller kiểm tra Ví',
    'Flow_Route_Predict': 'Dự báo ETA',
    'Flow_Route_GenAWB': 'Tạo AWB',
    'Flow_Drone_Sort': 'Phân loại tại Hub',
    'Flow_Drone_Receive': 'Drone nhận hàng',
    'Flow_Drone_Notify': 'Thông báo lịch giao',
    'Flow_Out_DeliverGate': 'Kiểm tra giao lần đầu',
    'Flow_Out_Notify': 'Cập nhật vị trí',
    'Flow_GenAWB_Sort': 'Phân loại tại Hub',
    'Flow_GenAWB_Track': 'Push tracking',
    # ===== processes (AS-IS) =====
    'Flow_Notify_End': 'Kích hoạt gian hàng',
    'Flow_Notify_Monitor': 'Giám sát vi phạm',
    'Flow_Evidence_SolidYes': 'Có bằng chứng cứng',
    'Flow_Evidence_SoftNo': 'Không/thiếu bằng chứng',
    'Flow_History_Yes': 'Đã vi phạm SLA',
    'Flow_History_No': 'Chưa vi phạm SLA',
    'Flow_SLA_Yes': 'Phản hồi đúng hạn',
    'Flow_SLA_No': 'Quá hạn 48h',
    'Flow_Evidence_Complete': 'Bằng chứng đầy đủ',
    'Flow_Evidence_Incomplete': 'Thiếu bằng chứng',
    'Flow_Wins_Settle': 'Buyer thắng',
    'Flow_Wins_Not': 'Buyer thua/bác bỏ',
    'Flow_Triage_History': 'Phức tạp (tra SLA)',
    'Flow_Triage_simple': 'Đơn giản',
    'Flow_SellerReply_Review': 'CS thẩm định',
    'Flow_SellerReply_Rejoin': 'Bổ sung bằng chứng',
    'Flow_Decide_Wins': 'Buyer thắng',
    'Flow_Decide_Compromise': 'Đồng thuận 2 bên',
    'Flow_Decide_Escalate': 'Escalate',
    'Flow_Gate_Online': 'Thanh toán online',
    'Flow_Gate_COD': 'Thanh toán COD',
    'Flow_Fraud_Inventory': 'Không gian lận',
    'Flow_Fraud_Cancel': 'Nghi gian lận',
    'Flow_Inventory_Seller': 'Còn hàng',
    'Flow_Inventory_Cancel': 'Hết hàng',
    'Flow_GateSeller_Confirm': 'Seller xác nhận đúng hạn',
    'Flow_GateSeller_Timeout': 'Seller quá hạn 48h',
    'Flow_Cancel_Gate_Yes': 'Buyer hủy đơn',
    'Flow_Cancel_Gate_No': 'Không hủy',
    'Flow_Retry_Deliver': 'Còn lượt giao lại',
    'Flow_Retry_Cancel': 'Hết lượt giao lại',
    'Flow_GateConfirm_Yes': 'Buyer đã confirm',
    'Flow_GateConfirm_Auto': 'Auto-confirm 7 ngày',
    'Flow_Cancel_Notify': 'Đã thanh toán online',
    'Flow_Cancel_End': 'Chưa thanh toán (COD)',
    'Flow_Package3PL': 'Bàn giao cho 3PL/LEX',
    'Flow_Waybill_Track': 'Cập nhật tracking',
    'Flow_Confirm_Package': 'Seller đồng ý đóng gói',
    'Flow_Confirm_Refuse': 'Seller từ chối',
    'Flow_Refuse_Cancel': 'Tự động hủy đơn',
    'Flow_Window_Yes': 'Còn hạn hoàn trả',
    'Flow_Window_No': 'Hết hạn hoàn trả',
    'Flow_LowRisk_Refund': 'Rủi ro thấp',
    'Flow_Evidence_Good': 'Bằng chứng đạt',
    'Flow_Evidence_Blurry': 'Bằng chứng không rõ',
    'Flow_Refund_Original': 'Hoàn về nguồn thanh toán',
    'Flow_Refund_Credit': 'Hoàn vào Ví/credit',
    'Flow_Inspect_Refund': 'Đạt kiểm định',
    'Flow_Inspect_Reject': 'Không đạt kiểm định',
    'Flow_Approve_Gate': 'Duyệt — kiểm tra thêm',
    'Flow_Reject_Notify': 'Từ chối yêu cầu',
    'Flow_Approve_Handover': 'Duyệt — bàn giao',
    'Flow_Triage_Quality': 'Chất lượng bằng chứng',
    'Flow_Triage_AIReview': 'CS thẩm định AI',
    'Flow_Review_Approve': 'Phê duyệt',
    'Flow_Review_Reject': 'Từ chối',
    'Flow_Repeat_Yes': 'Khách liên hệ lại',
    'Flow_Repeat_No': 'Không liên hệ lại',
    'Flow_BotSuccess_Confirm': 'Bot giải quyết xong',
    'Flow_BotSuccess_T1': 'Chuyển Tier 1',
    'Flow_SLA_Valid': 'Còn hạn SLA',
    'Flow_SLA_Expired': 'Quá hạn SLA',
    'Flow_Verify_Pass': 'Xác minh thành công',
    'Flow_Verify_Fail': 'Xác minh thất bại',
    'Flow_Gate_BotYes': 'Bot có kịch bản',
    'Flow_Gate_BotNo': 'Bot không xử lý được',
    'Flow_T1_Resolve_Confirm': 'Tier 1 giải quyết xong',
    'Flow_T1_Escalate': 'Escalate Tier 2',
    'Flow_T1_ProvideInfo': 'Cần thêm thông tin',
    'Flow_Timeout_Yes': 'Quá thời gian chờ',
    'Flow_Timeout_No': 'Còn thời gian chờ',
    'Flow_CSAT_Good': 'CSAT ≥ 4 sao',
    'Flow_CSAT_Bad': 'CSAT < 4 sao',
    'Flow_Audience_Yes': 'Đối tượng phù hợp',
    'Flow_Audience_No': 'Chưa phù hợp',
    'Flow_Promo_No': 'Không trùng lặp',
    'Flow_Promo_Yes': 'Trùng lặp voucher',
    'Flow_Report_Yes': 'Số liệu đầy đủ',
    'Flow_Report_No': 'Thiếu số liệu',
    'Flow_Compliance_Pass': 'Đạt tiêu chuẩn',
    'Flow_Compliance_Fail': 'Chưa đạt',
    'Flow_Test_Pass': 'Voucher hoạt động',
    'Flow_Test_Fail': 'Voucher lỗi',
    'Flow_Gate_QAYes': 'Đạt chuẩn QA',
    'Flow_Gate_QANo': 'Chưa đạt QA',
    'Flow_Confirm_Yes': 'Seller đồng ý',
    'Flow_Confirm_No': 'Seller từ chối',
    'Flow_Publish_GateEnroll': 'Đủ số lượng đăng ký',
    'Flow_Publish_Compliance': 'Kiểm tra tuân thủ',
    'Flow_Refund_Back': 'Hoàn tiền cho Buyer',
    'Flow_Verify_GateValid': 'Giao dịch hợp lệ',
    'Flow_Verify_GateIPN': 'Đối soát IPN/Webhook',
    'Flow_Wallet_Invoice': 'Xuất hóa đơn',
    'Flow_Bugfix_ST': 'System Test & Integration',
    'Flow_Bugfix_ST2': 'Quét bảo mật SAST/DAST',
}

def apply_labels(path, dry=False):
    tree = ET.parse(path); root = tree.getroot()
    flows = {sf.get('id'): sf for sf in root.iter(tn('sequenceFlow'))}
    added = 0
    for g in root.iter():
        if not local(g.tag).endswith('Gateway'):
            continue
        out = [o.text.strip() for o in g.findall('bpmn:outgoing', {'bpmn': NS})]
        if len(out) < 2:
            continue
        for fid in out:
            sf = flows.get(fid)
            if sf is None or (sf.get('name') or '').strip():
                continue
            label = CURATED.get(fid)
            if not label:
                print(f"  !! NO CURATED LABEL for {fid} in {path}")
                continue
            sf.set('name', label)
            added += 1
    if added and not dry:
        tree.write(path, encoding='UTF-8', xml_declaration=True)
    return added

def main():
    files = [f for f in sys.argv[1:] if not f.startswith('-')]
    dry = '--dry' in sys.argv
    if not files:
        files = sorted(glob.glob('processes/*.bpmn')) + sorted(glob.glob('processes-to-be/*.bpmn'))
    total = 0
    for path in files:
        n = apply_labels(path, dry)
        total += n
        print(f"[{'dry' if dry else 'ok'}] {path}: +{n}")
    print(f"\nTOTAL: {total}")
    return 0

if __name__ == '__main__':
    main()

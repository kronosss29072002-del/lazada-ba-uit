#!/usr/bin/env python3
"""Rename start/end events to teacher's convention:
- startEvent  = DANH TỪ first (noun), e.g. "Yêu cầu đăng ký gian hàng"
- endEvent    = ĐỘNG TỪ / state completed (verb), e.g. "Gian hàng đã được kích hoạt"
Also purges placeholder names missing diacritics (e.g. "Da thong bao cho khach").
IMPORTANT: only renames events that clearly violate; keeps already-conforming ones.
"""
import xml.etree.ElementTree as ET
import sys, shutil, os

NS='http://www.omg.org/spec/BPMN/20100524/MODEL'
def local(t): return t.split('}')[-1] if '}' in t else t

# (file, eventId, newName) — exact IDs from current files
RENAMES = [
    # ===== AS-IS =====
    ('processes/01-seller-management.bpmn','StartEvent_Register','Yêu cầu đăng ký gian hàng'),
    ('processes/01-seller-management.bpmn','End_Approved','Gian hàng Lazada đã được kích hoạt'),
    ('processes/01-seller-management.bpmn','End_Rejected','Hồ sơ đã bị từ chối vĩnh viễn'),
    ('processes/01-seller-management.bpmn','End_Warned','Gian hàng đã bị cảnh cáo'),
    ('processes/01-seller-management.bpmn','End_Suspended','Gian hàng đã bị tạm khóa'),
    ('processes/01-seller-management.bpmn','End_Banned','Gian hàng đã bị khóa vĩnh viễn'),
    ('processes/02-dispute-management.bpmn','StartEvent_Dispute','Yêu cầu giải quyết tranh chấp'),
    ('processes/02-dispute-management.bpmn','End_Settled','Tranh chấp đã được giải quyết'),
    ('processes/02-dispute-management.bpmn','End_Rejected','Tranh chấp đã bị bác bỏ'),
    ('processes/02-dispute-management.bpmn','End_AIResolved','Tranh chấp đã được AI tự giải quyết'),
    ('processes/03-order-processing.bpmn','StartEvent_Checkout','Yêu cầu đặt hàng'),
    ('processes/03-order-processing.bpmn','End_Delivered','Đơn hàng đã hoàn tất'),
    ('processes/03-order-processing.bpmn','End_Refunded','Đã hoàn tiền cho Buyer'),
    ('processes/03-order-processing.bpmn','End_Cancelled','Đơn hàng đã bị hủy'),
    ('processes/04-return-refund.bpmn','StartEvent_Request','Yêu cầu hoàn trả hàng'),
    ('processes/04-return-refund.bpmn','End_Refunded','Đã hoàn tiền cho Buyer'),
    ('processes/04-return-refund.bpmn','End_Rejected','Yêu cầu hoàn trả đã bị từ chối'),
    ('processes/05-customer-service.bpmn','StartEvent_Contact','Yêu cầu hỗ trợ từ khách hàng'),
    ('processes/05-customer-service.bpmn','End_Resolved','Phiên hỗ trợ đã kết thúc thành công'),
    ('processes/05-customer-service.bpmn','End_SLAExpired','Ticket hỗ trợ đã quá hạn SLA'),
    ('processes/05-customer-service.bpmn','End_VerifyFail','Xác minh danh tính đã thất bại'),
    ('processes/06-marketing.bpmn','StartEvent_Idea','Ý tưởng chiến dịch mới'),
    ('processes/06-marketing.bpmn','End_CampaignDone','Chiến dịch đã kết thúc thành công'),
    ('processes/07-hr-training.bpmn','StartEvent_Q1Plan','Nhu cầu đào tạo đầu quý'),
    ('processes/07-hr-training.bpmn','EndEvent_Complete','Chương trình đào tạo đã hoàn tất'),
    ('processes/07-hr-training.bpmn','EndEvent_Violation','Vi phạm chính sách đã được xử lý'),
    ('processes/08-payment-settlement.bpmn','StartEvent_Checkout','Thanh toán đơn hàng'),
    ('processes/08-payment-settlement.bpmn','EndEvent_Paid','Seller đã nhận tiền thanh toán'),
    ('processes/08-payment-settlement.bpmn','EndEvent_Settled','Đối soát đã hoàn tất'),
    ('processes/08-payment-settlement.bpmn','EndEvent_Refunded','Đã hoàn tiền về Buyer'),
    ('processes/09-logistics-delivery.bpmn','StartEvent_OrderConfirmed','Đơn hàng đã được xác nhận'),
    ('processes/09-logistics-delivery.bpmn','EndEvent_Delivered','Đơn hàng đã giao thành công'),
    ('processes/09-logistics-delivery.bpmn','EndEvent_Returned','Hàng đã hoàn về Seller'),
    ('processes/10-it-platform.bpmn','StartEvent_FeatureReq','Yêu cầu tính năng / sự cố mới'),
    ('processes/10-it-platform.bpmn','EndEvent_Deployed','Tính năng đã deploy thành công'),
    ('processes/10-it-platform.bpmn','EndEvent_Rollback','Đã rollback về version trước'),
    # ===== TO-BE =====
    ('processes-to-be/01-seller-management.bpmn','SE_Reg','Yêu cầu đăng ký gian hàng'),
    ('processes-to-be/01-seller-management.bpmn','EE_Appr','Gian hàng Lazada đã được kích hoạt'),
    ('processes-to-be/01-seller-management.bpmn','EE_Warn','Gian hàng đã bị cảnh cáo'),
    ('processes-to-be/01-seller-management.bpmn','EE_Susp','Gian hàng đã bị tạm khóa'),
    ('processes-to-be/01-seller-management.bpmn','EE_Ban','Gian hàng đã bị khóa vĩnh viễn'),
    ('processes-to-be/02-dispute-management.bpmn','StartEvent_Dispute','Tranh chấp mới phát sinh'),
    ('processes-to-be/02-dispute-management.bpmn','End_Settled','Tranh chấp đã được giải quyết'),
    ('processes-to-be/02-dispute-management.bpmn','End_Refunded','Đã tự động hoàn tiền thành công'),
    ('processes-to-be/02-dispute-management.bpmn','End_Rejected','Tranh chấp đã bị bác bỏ'),
    ('processes-to-be/03-order-processing.bpmn','StartEvent_Checkout','Yêu cầu đặt hàng'),
    ('processes-to-be/03-order-processing.bpmn','End_Delivered','Đơn hàng đã hoàn tất'),
    ('processes-to-be/03-order-processing.bpmn','End_Refunded','Đã hoàn tiền cho Buyer'),
    ('processes-to-be/04-return-refund.bpmn','StartEvent_Request','Yêu cầu hoàn trả hàng'),
    ('processes-to-be/04-return-refund.bpmn','End_Refunded','Đã hoàn tiền cho Buyer'),
    ('processes-to-be/04-return-refund.bpmn','End_Rejected','Yêu cầu hoàn trả đã bị từ chối'),
    ('processes-to-be/05-customer-service.bpmn','StartEvent_Contact','Yêu cầu hỗ trợ từ khách hàng'),
    ('processes-to-be/05-customer-service.bpmn','End_Resolved','Phiên hỗ trợ đã kết thúc thành công'),
    ('processes-to-be/05-customer-service.bpmn','End_Proactive','Đã chủ động thông báo kết quả cho khách hàng'),
    ('processes-to-be/06-marketing.bpmn','StartEvent_Idea','Ý tưởng chiến dịch mới'),
    ('processes-to-be/06-marketing.bpmn','End_CampaignDone','Chiến dịch đã hoàn tất'),
    ('processes-to-be/07-hr-training.bpmn','StartEvent_NewQuarter','Nhu cầu đào tạo đầu quý'),
    ('processes-to-be/07-hr-training.bpmn','EndEvent_Complete','Chương trình đào tạo đã hoàn tất'),
    ('processes-to-be/07-hr-training.bpmn','EndEvent_Violation','Vi phạm chính sách đã được xử lý'),
    ('processes-to-be/08-payment-settlement.bpmn','StartEvent_Checkout','Thanh toán đơn hàng'),
    ('processes-to-be/08-payment-settlement.bpmn','EndEvent_Settled','Đối soát đã hoàn tất'),
    ('processes-to-be/08-payment-settlement.bpmn','EndEvent_Refunded','Đã hoàn tiền tự động về Buyer'),
    ('processes-to-be/09-logistics-delivery.bpmn','StartEvent_OrderConfirmed','Đơn hàng đã được xác nhận'),
    ('processes-to-be/09-logistics-delivery.bpmn','EndEvent_Delivered','Đơn hàng đã giao thành công'),
    ('processes-to-be/09-logistics-delivery.bpmn','EndEvent_Returned','Đơn hàng đã hoàn về Seller'),
    ('processes-to-be/10-it-platform.bpmn','StartEvent_FeatureReq','Yêu cầu tính năng / cải tiến mới'),
    ('processes-to-be/10-it-platform.bpmn','EndEvent_Deployed','Dự án đã triển khai hoàn tất'),
]

def main():
    dry = '--dry' in sys.argv
    only = [f for f in sys.argv[1:] if not f.startswith('-')]
    by_file = {}
    for path, eid, newname in RENAMES:
        if only and path not in only:
            continue
        by_file.setdefault(path, []).append((eid, newname))
    total = 0
    for path, items in sorted(by_file.items()):
        tree = ET.parse(path); root = tree.getroot()
        present = {e.get('id') for e in root.iter() if e.get('id')}
        applied, missing = [], []
        for eid, newname in items:
            if eid not in present:
                missing.append(eid); continue
            for e in root.iter():
                if e.get('id') == eid:
                    e.set('name', newname)
                    applied.append((eid, newname))
                    total += 1
                    break
        # purge placeholder event names missing diacritics (e.g. "Da thong bao cho khach")
        for e in root.iter():
            if local(e.tag) not in ('startEvent','endEvent'): continue
            nm = e.get('name') or ''
            if nm and all(ord(c) < 128 for c in nm) and ' ' in nm:
                # ascii-only event name = placeholder like "Da thong bao cho khach"
                e.set('name', 'Đã hoàn tất xử lý')
                applied.append((e.get('id'), 'Đã hoàn tất xử lý'))
                total += 1
        if applied and not dry:
            if not os.path.exists(path + '.bak'):
                shutil.copy2(path, path + '.bak')
            tree.write(path, encoding='utf-8', xml_declaration=True)
        print(f"{'[DRY]' if dry else '[FIXED]'} {path}: {len(applied)} renamed")
        for eid, n in applied:
            print(f"    {eid} -> \"{n}\"")
        if missing:
            print(f"    !! MISSING ids: {missing}")
    print(f"\nTOTAL renamed: {total}" + (" (dry run)" if dry else ""))

if __name__ == '__main__':
    main()

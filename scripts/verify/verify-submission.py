#!/usr/bin/env python3
"""Verifier tổng hợp — PASS/FAIL toàn bộ số liệu canonical (Phase 8/9/10/11)."""
import re, glob, json, os, zipfile

checks = []
def check(desc, cond, src=""):
    checks.append((desc, bool(cond), src))

md = open('DOAN-LAZADA-FINAL.md', encoding='utf-8').read()

# ===== 1. Báo cáo — các số canonical =====
check("Report: 20-25% delivery failure", "20-25%" in md)
check("Report: success 75-80%", "75-80%" in md)
check("Report: CS Staff 52.000 VNĐ", "52.000 VNĐ" in md)
check("Report: CS -65,4%", "-65,4%" in md)
check("Report: Avg CT 8,5 ngày", "8,5 ngày" in md)
check("Report: CT -78,8%", "-78,8%" in md)
check("Report: Escalation -60-75%", "-60-75%" in md)
check("Report: P3 Seller 40h→2h", "40 giờ" in md and "2 giờ" in md)
check("Report: 10 nhân sự phỏng vấn sâu", "10 nhân sự nội bộ" in md)
check("Report: không còn **|", "**|" not in md)

# ===== 2. Phụ trợ phân tích =====
five = open('docs/analysis/5-why-supplementary.md', encoding='utf-8').read()
check("5-why: từ chối nhận hàng (đủ dấu)", "từ chối nhận hàng" in five)
check("5-why: không còn 'từ ch nhận'", "từ ch nhận" not in five)

d05 = open('docs/analysis/05-customer-service.md', encoding='utf-8').read()
check("d05: 52,600 VNĐ", "52,600" in d05)
check("d05: ~131,5 tỷ", "~131,5 tỷ" in d05)

# ===== 3. Comparison docs — ROI (decimal = dấu chấm) =====
def comp(n):
    return open(f'docs/analysis/comparison/{n}.md', encoding='utf-8').read()

c1 = comp('01-seller-management')
check("d01: 0.32 churn", "0.32" in c1)
check("d01: 4.73 tỷ", "4.73 tỷ" in c1)

c2 = comp('02-dispute-management')
check("d02: 4.065 tổng", "4.065" in c2)

c3 = comp('03-order-processing')
check("d03: 148.5 tỷ", "148.5 tỷ" in c3)

c4 = comp('04-return-refund')
check("d04: 13.44 tổng", "13.44" in c4)
check("d04: ~10 tháng/~24 tháng", "10 tháng" in c4 and "24 tháng" in c4)

c8 = comp('08-payment-settlement')
check("d08: 0.77 interest", "0.77" in c8)
check("d08: 146.24", "146.24" in c8)
check("d08: ~21 ngày", "21 ngày" in c8)

c10 = comp('10-it-platform')
check("d10: 7.35 tỷ", "7.35 tỷ" in c10)

c6 = comp('06-marketing')
check("d06: không còn 依靠", "依靠" not in c6)

# ===== 4. data.json / dashboard alignment =====
dj = json.load(open('metrics/data.json'))
check("data.json: 10 processes", len(dj['processes']) == 10)
check("data.json: d05 as_is 52600", dj['processes']['05-customer-service']['cost_per_unit']['as_is'] == 52600)
check("data.json: d04 as_is 109000", dj['processes']['04-return-refund']['cost_per_unit']['as_is'] == 109000)

# dashboard inline đồng bộ
html = open('metrics/dashboard.html', encoding='utf-8').read()
start = html.index('const DATA = {')
depth = 0; end = None
for j in range(start + len('const DATA = {') - 1, len(html)):
    if html[j] == '{': depth += 1
    elif html[j] == '}':
        depth -= 1
        if depth < 0: end = j + 1; break
dash = None
for endtry in range(html.index('const DATA = {'), len(html)):
    if html[endtry] == ';':
        try:
            dash = json.loads(html[start:endtry].replace('const DATA = ', '').strip())
            break
        except Exception:
            pass
if dash is None:
    raise SystemExit('FATAL: cannot parse dashboard DATA')
check("dashboard: 10 processes", len(dash['processes']) == 10)
d05d = dash['processes'].get('05-customer-service', {})
check("dashboard: d05 52600", d05d.get('cost_per_unit', {}).get('as_is') == 52600)

# ===== 5. BPMN tasks/gateways (đếm serviceTask+userTask, gateways) =====
NS = '{http://www.omg.org/spec/BPMN/20100524/MODEL}'
def count_bpmn(path):
    t = re.sub(r'xmlns:[a-z]+="[^"]*"', '', open(path, encoding='utf-8').read())
    tasks = len(re.findall(r'<(?:bpmn:|\w+:)?(?:user|service|script|manual|receive|send|businessRule)Task\b', t))
    gws = len(re.findall(r'<(?:bpmn:|\w+:)?(?:exclusive|parallel|inclusive|eventBased)Gateway\b', t))
    return tasks, gws

ok_all = True
for tag in sorted(glob.glob('processes/0*.bpmn')) + sorted(glob.glob('processes/1*.bpmn')):
    t, g = count_bpmn(tag)
    ok = t > 0 and g > 0
    ok_all &= ok
    check(f"BPMN {os.path.basename(tag)} (tasks={t}, gw={g})", ok)
check("BPMN: tất cả 10 AS-IS có task+gateway", ok_all)

# ===== 6. Derived artifacts =====
check("docx tồn tại", os.path.exists('DOAN-LAZADA-UIT.docx'))
check(".doc tồn tại", os.path.exists('report/DOAN-LAZADA-UIT.doc'))
check("report.html tồn tại", os.path.exists('report.html'))
check("index.html tồn tại", os.path.exists('index.html'))

zx = zipfile.ZipFile('DOAN-LAZADA-UIT.docx')
txt = re.sub(r'<[^>]+>', '', zx.read('word/document.xml').decode('utf-8'))
check("docx: chứa 52.000 VNĐ", "52.000 VNĐ" in txt)
check("docx: chứa -78,8%", "-78,8%" in txt)

rhtml = open('report.html', encoding='utf-8').read()
check("report.html: không còn **|", "**|" not in rhtml)

# ===== 7. ZIP =====
z = zipfile.ZipFile('/home/kronosss2002/doanba/Lazada-BA-IE203-P11.zip')
zn = z.namelist()
check("ZIP: ≥ 142 files (không .bak)", len(zn) >= 142)
check("ZIP: không có file .bak", not any(".bak" in n for n in zn))
zrep = [n for n in zn if n.endswith('DOAN-LAZADA-FINAL.md')]
if zrep:
    zt = z.read(zrep[0]).decode('utf-8')
    check("ZIP report: không còn **|", "**|" not in zt)
zd05 = [n for n in zn if n.endswith('docs/analysis/05-customer-service.md')]
if zd05:
    check("ZIP d05: ~131,5 tỷ", "~131,5 tỷ" in z.read(zd05[0]).decode('utf-8'))

passed = sum(1 for _, c, _ in checks if c)
failed = [(d, s) for d, c, s in checks if not c]
print(f"TOTAL: {len(checks)} | PASS: {passed} | FAIL: {len(failed)}")
for d, s in failed:
    print(f"  ✗ {d}  ({s})")
if not failed:
    print("ALL CANONICAL CHECKS VERIFIED ✓")

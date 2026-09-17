#!/usr/bin/env python3
"""Tái tạo report.html + index.html từ DOAN-LAZADA-FINAL.md (nguồn chính thức).

Các file HTML bản trước (Sep 3) bị stale so với report cập nhật (Sep 14).
Script này convert markdown -> HTML tự chứa (self-contained, inline CSS)
với cùng ngôn ngữ thiết kế của bản cũ: cover, danh mục viết tắt, mục lục,
chương, bảng có style, print CSS. Ảnh BPMN được tham chiếu tương đối
docs/screenshots/ (mở bằng HTTP server).

Output:
  report.html  — toàn bộ báo cáo
  index.html   — trang bìa + mục lục
"""
import os, re, html as html_mod
import markdown

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MD = os.path.join(ROOT, 'DOAN-LAZADA-FINAL.md')
OUT_REPORT = os.path.join(ROOT, 'report.html')
OUT_INDEX = os.path.join(ROOT, 'index.html')

CSS = """
:root{--primary:#a44ad7;--secondary:#1e3a8a;--accent:#059669;--danger:#dc2626;--bg:#fff;--text:#1e293b;--muted:#64748b;--border:#e2e8f0;--code-bg:#f8fafc}
*{box-sizing:border-box}
body{font-family:'Segoe UI',Arial,sans-serif;line-height:1.7;color:var(--text);background:var(--bg);max-width:1000px;margin:0 auto;padding:2rem 3rem;font-size:15px}
@media print{body{font-size:11pt;padding:0;max-width:none}.no-print{display:none!important}h1,h2,h3{page-break-after:avoid}table,pre{page-break-inside:avoid}}
@media(max-width:768px){body{padding:1rem;font-size:14px}}
h1{color:var(--primary);border-bottom:2px solid var(--primary);padding-bottom:.5rem;margin-top:2rem}
h2{color:var(--secondary);margin-top:2rem}
h3{color:var(--text);margin-top:1.5rem}
table{border-collapse:collapse;width:100%;margin:1.5rem 0;font-size:.92em;box-shadow:0 1px 3px rgba(0,0,0,.05)}
th{background:var(--secondary);color:#fff;padding:.7rem .9rem;text-align:left}
td{padding:.6rem .9rem;border-bottom:1px solid var(--border)}
tr:nth-child(even) td{background:var(--code-bg)}
pre{background:var(--code-bg);border-left:4px solid var(--primary);padding:1rem;overflow-x:auto;font-size:.88em;border-radius:4px}
code{background:var(--code-bg);padding:.1rem .4rem;border-radius:3px;font-size:.9em;font-family:Consolas,monospace}
pre code{background:none;padding:0}
blockquote{border-left:4px solid var(--primary);background:#fff7ed;padding:1rem 1.5rem;margin:1.5rem 0;border-radius:0 4px 4px 0}
ul,ol{padding-left:1.8rem}li{margin:.3rem 0}
hr{border:none;border-top:2px dashed var(--border);margin:2rem 0}
.cover{text-align:center;margin:4rem 0 3rem;padding:2rem 1rem 3rem;border-bottom:4px double var(--primary)}
.cover h1{font-size:1.9rem;border:none;margin-top:0;line-height:1.45}
.cover h2{font-size:1.25rem;border:none;color:var(--muted);line-height:1.5}
.cover p{text-align:center;font-size:1.05em}
.cover p strong{color:var(--accent)}
.toc a{color:var(--secondary);text-decoration:none;font-weight:600}
.toc a:hover{color:var(--primary)}
.nav{display:flex;justify-content:space-between;margin:2rem 0;padding:1rem;background:var(--code-bg);border-radius:8px}
.nav a{color:var(--secondary);text-decoration:none;font-weight:bold}
.nav a:hover{color:var(--primary)}
img{max-width:100%;height:auto}
.markdown-body img{max-width:100%}
"""

def gh_slugify(value, separator):
    """Slug theo chuẩn GitHub: giữ nguyên dấu tiếng Việt (khớp các href
    trong MỤC LỤC viết tay), bỏ ký tự đặc biệt, khoảng trắng -> '-'.
    Ví dụ: '1.1. Tổng quan về Lazada' -> '11-tổng-quan-về-lazada'."""
    value = value.lower().strip()
    value = re.sub(r'[^\w\s-]', '', value, flags=re.UNICODE)
    value = re.sub(r'[-\s]+', separator, value)
    return value.strip(separator)


def md_to_html(md_text):
    """Convert markdown -> HTML. `toc` extension gán id cho heading (h1/h2/h3)
    để các liên kết trong MỤC LỤC (#...) nhảy đúng chương mục."""
    return markdown.markdown(
        md_text,
        extensions=['tables', 'fenced_code', 'sane_lists', 'nl2br', 'toc'],
        extension_configs={'toc': {'slugify': gh_slugify, 'permalink': False}},
        output_format='html5',
    )


HRE = re.compile(r'<h([1-6])([^>]*)>(.*?)</h\1>', re.S)


def fix_anchors(body_html):
    """Đảm bảo mọi href trong MỤC LỤC viết tay đều có heading đích có id.
    Slug do markdown sinh đôi khi lệch với slug viết tay (vd '&' → '--');
    khi đó gán id theo chính slug trong href, khớp bằng nội dung heading."""
    links = re.findall(r'<a href="#([^"]+)">(.*?)</a>', body_html, re.S)
    want = {}
    for slug, text in links:
        t = re.sub(r'<[^>]+>', '', text)
        t = re.sub(r'\s+', ' ', t).strip().lower()
        want.setdefault(t, slug)
    existing_ids = set(re.findall(r'\bid="([^"]+)"', body_html))
    pending = {t: s for t, s in want.items() if s not in existing_ids}

    def plain(inner):
        t = re.sub(r'<[^>]+>', '', inner)
        return re.sub(r'\s+', ' ', t).strip().lower()

    def repl(m):
        lvl, attrs, inner = m.group(1), m.group(2), m.group(3)
        t = plain(inner)
        if t in pending:
            slug = pending.pop(t)
            if re.search(r'\bid=', attrs):
                attrs = re.sub(r'\bid="[^"]*"', 'id="' + slug + '"', attrs, count=1)
            else:
                attrs += ' id="' + slug + '"'
        return '<h' + lvl + attrs + '>' + inner + '</h' + lvl + '>'

    return HRE.sub(repl, body_html)


def cover_block(body_html):
    """Bọc trang bìa vào div.cover: mọi thứ trước h1 'DANH MỤC TỪ VIẾT TẮT'
    (trường, khoa, tên đồ án, thông tin nhóm). Trả nguyên nếu không tìm thấy."""
    m = re.search(r'<h1[^>]*>DANH MỤC', body_html)
    if not m:
        return body_html
    return f'<div class="cover">{body_html[:m.start()]}</div>{body_html[m.start():]}'

def wrap(title, body_html):
    return f"""<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{html_mod.escape(title)}</title>
<style>{CSS}</style>
</head>
<body>
{body_html}
</body>
</html>
"""

def main():
    with open(MD, encoding='utf-8') as f:
        md_text = f.read()

    body = fix_anchors(cover_block(md_to_html(md_text)))

    # report.html — toàn bộ nội dung
    with open(OUT_REPORT, 'w', encoding='utf-8') as f:
        f.write(wrap('Đồ án IE203 — Phân tích BPM Lazada Việt Nam', body))
    print(f'✓ {OUT_REPORT} ({os.path.getsize(OUT_REPORT)//1024} KB)')

    # index.html — trang bìa + mục lục (đến trước Chương 1)
    toc_cut = md_text.find('# Chương 1')
    if toc_cut == -1:
        toc_cut = len(md_text)
    front = md_text[:toc_cut]
    front_body = md_to_html(front)
    with open(OUT_INDEX, 'w', encoding='utf-8') as f:
        f.write(wrap('Đồ án IE203 — Lazada BPM', front_body))
    print(f'✓ {OUT_INDEX} ({os.path.getsize(OUT_INDEX)//1024} KB)')

if __name__ == '__main__':
    main()
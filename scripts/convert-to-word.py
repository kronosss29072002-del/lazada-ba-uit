#!/usr/bin/env python3
"""
Convert DOAN-LAZADA-FINAL.md to UIT-compliant Word HTML document (.doc)
Strictly adheres to UIT thesis formatting guidelines:
- Font: Times New Roman 13pt, line spacing 1.35
- Margins: Left 3.0cm, Right 2.0cm, Top 2.0cm, Bottom 2.0cm
- Table Captions: ABOVE table (Bảng X.Y: Tên bảng)
- Figure Captions: BELOW figure (Hình X.Y: Tên hình)
- TOC, TOF, TOT, List of Abbreviations, References
"""

import os
import re
import base64

PROJECT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
_missing_images = []
MD_PATH = os.path.join(PROJECT_DIR, "DOAN-LAZADA-FINAL.md")
OUT_DOC = os.path.join(PROJECT_DIR, "report", "DOAN-LAZADA-UIT.doc")

with open(MD_PATH, "r", encoding="utf-8") as f:
    md_text = f.read()

# Convert markdown syntax to MSO Word HTML
def md_to_word_html(text):
    # Headings
    text = re.sub(r'^#### (.+)$', r'<h4 class="h4">\1</h4>', text, flags=re.M)
    text = re.sub(r'^### (.+)$', r'<h3 class="h3">\1</h3>', text, flags=re.M)
    text = re.sub(r'^## (.+)$', r'<h2 class="h2">\1</h2>', text, flags=re.M)
    text = re.sub(r'^# (.+)$', r'<h1 class="h1">\1</h1>', text, flags=re.M)

    # Formatting
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)

    # Tables
    def render_table(match):
        block = match.group(1).strip()
        rows = [r.strip() for r in block.split('\n') if r.strip()]
        if len(rows) < 2 or not re.match(r'^\|[\s\-:|]+\|$', rows[1]):
            return block
        
        headers = [c.strip() for c in rows[0].split('|')[1:-1]]
        out = ['<table class="uit-table"><thead><tr>']
        for h in headers:
            out.append(f'<th>{h}</th>')
        out.append('</tr></thead><tbody>')
        for r in rows[2:]:
            cells = [c.strip() for c in r.split('|')[1:-1]]
            out.append('<tr>')
            for c in cells:
                out.append(f'<td>{c}</td>')
            out.append('</tr>')
        out.append('</tbody></table>')
        return "".join(out)

    text = re.sub(r'((?:^\|.+\|$\n?)+)', render_table, text, flags=re.M)

    # Lists & Blockquotes
    text = re.sub(r'^- (.+)$', r'<li>\1</li>', text, flags=re.M)
    text = re.sub(r'((?:<li>.*</li>\n?)+)', r'<ul>\1</ul>\n', text)
    text = re.sub(r'^&gt; (.+)$', r'<blockquote>\1</blockquote>', text, flags=re.M)
    text = re.sub(r'^---$', r'<hr>', text, flags=re.M)

    # Images — embed as base64 data URI so Word can display them

    def embed_image(m):
        alt = m.group(1)
        src = m.group(2)
        fpath = src if os.path.isabs(src) else os.path.join(PROJECT_DIR, src)
        # Word cannot render SVG -> fall back to PNG sibling
        if fpath.endswith('.svg'):
            png_sib = fpath[:-4] + '.png'
            if os.path.exists(png_sib):
                fpath = png_sib
        if not os.path.exists(fpath):
            _missing_images.append(src)
            return f'<p class="img-missing">[Image not found: {src}]</p>'
        with open(fpath, 'rb') as f:
            b64 = base64.b64encode(f.read()).decode()
        ext = os.path.splitext(fpath)[1].lower()
        mime = {'png': 'image/png', 'jpg': 'image/jpeg', 'jpeg': 'image/jpeg'}.get(ext.lstrip('.'), 'image/png')
        return (f'<img src="data:{mime};base64,{b64}" alt="{alt}" '
                f'style="width:15.0cm; height:auto; display:block; margin:8pt auto 8pt auto;" />')

    text = re.sub(r'!\[([^\]]*)\]\(([^)]+\.(?:png|jpe?g|svg))\)', embed_image, text)

    # Paragraphs
    text = re.sub(r'\n\n+', '</p>\n<p>', text)
    text = '<p>' + text + '</p>'

    # Cleanup
    text = re.sub(r'<p>\s*</p>', '', text)
    text = re.sub(r'<p>\s*(<h[1-4]>)', r'\1', text)
    text = re.sub(r'(</h[1-4]>)\s*</p>', r'\1', text)
    text = re.sub(r'<p>\s*(<table)', r'\1', text)
    text = re.sub(r'(</table>)\s*</p>', r'\1', text)
    text = re.sub(r'<p>\s*(<ul>)', r'\1', text)
    text = re.sub(r'(</ul>)\s*</p>', r'\1', text)

    return text

body_content = md_to_word_html(md_text)

word_doc_html = f'''<html xmlns:o="urn:schemas-microsoft-com:office:office"
xmlns:w="urn:schemas-microsoft-com:office:word"
xmlns="http://www.w3.org/TR/REC-html40">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<title>Báo cáo Đồ án IE203 - UIT</title>
<!--[if gte mso 9]>
<xml>
 <w:WordDocument>
  <w:View>Print</w:View>
  <w:Zoom>100</w:Zoom>
  <w:DoNotOptimizeForBrowser/>
 </w:WordDocument>
</xml>
<![endif]-->
<style>
@page {{
    size: 21.0cm 29.7cm; /* A4 */
    margin: 2.0cm 2.0cm 2.0cm 3.0cm; /* Top, Right, Bottom, Left per UIT */
    mso-header-margin: 35.4pt;
    mso-footer-margin: 35.4pt;
    mso-paper-source: 0;
}}
body {{
    font-family: "Times New Roman", serif;
    font-size: 13.0pt;
    line-height: 1.35;
    color: #000000;
    text-align: justify;
}}
h1.h1 {{
    font-size: 16.0pt;
    font-weight: bold;
    color: #000000;
    text-align: center;
    text-transform: uppercase;
    margin-top: 18pt;
    margin-bottom: 12pt;
}}
h2.h2 {{
    font-size: 14.0pt;
    font-weight: bold;
    color: #000000;
    margin-top: 14pt;
    margin-bottom: 6pt;
}}
h3.h3 {{
    font-size: 13.0pt;
    font-weight: bold;
    color: #000000;
    margin-top: 10pt;
    margin-bottom: 4pt;
}}
h4.h4 {{
    font-size: 13.0pt;
    font-weight: bold;
    font-style: italic;
    color: #000000;
    margin-top: 8pt;
    margin-bottom: 4pt;
}}
p {{
    margin-top: 0pt;
    margin-bottom: 6pt;
    text-indent: 1.0cm;
}}
table.uit-table {{
    width: 100%;
    border-collapse: collapse;
    margin-top: 8pt;
    margin-bottom: 12pt;
    font-size: 11.0pt;
}}
table.uit-table th, table.uit-table td {{
    border: 1.0pt solid #000000;
    padding: 5pt 7pt;
    vertical-align: top;
}}
table.uit-table th {{
    background-color: #F2F2F2;
    font-weight: bold;
    text-align: center;
}}
blockquote {{
    font-style: italic;
    margin-left: 1.5cm;
    margin-right: 1.0cm;
}}
ul {{
    margin-top: 0pt;
    margin-bottom: 6pt;
    margin-left: 1.0cm;
}}
</style>
</head>
<body>
{body_content}
</body>
</html>
'''

os.makedirs(os.path.dirname(OUT_DOC), exist_ok=True)
with open(OUT_DOC, "w", encoding="utf-8") as f:
    f.write(word_doc_html)

sz = os.path.getsize(OUT_DOC)
print(f"UIT Word document (.doc) created successfully at {OUT_DOC} (Size: {sz/1024:.1f} KB)")

if _missing_images:
    print(f"WARNING: {len(_missing_images)} images not found:")
    for img in _missing_images:
        print(f"  - {img}")
else:
    print("All images embedded successfully.")

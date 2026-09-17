#!/usr/bin/env python3
"""
Build DOAN-LAZADA-UIT.docx from DOAN-LAZADA-UIT.doc (HTML-based .doc)
with embedded base64 images.
"""
import os
import re
import base64
import zipfile
import struct

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.join(SCRIPT_DIR, '..')

DOC_PATH = os.path.join(SCRIPT_DIR, 'DOAN-LAZADA-UIT.doc')
DOCX_PATH = os.path.join(PROJECT_DIR, 'DOAN-LAZADA-UIT.docx')

if not os.path.exists(DOC_PATH):
    print(f"ERROR: {DOC_PATH} not found. Run convert-to-word.py first.")
    exit(1)

print("Reading HTML...")
with open(DOC_PATH, 'r', encoding='utf-8') as f:
    html = f.read()

# Extract base64 images
images = []
def extract_img(m):
    full = m.group(0)
    alt_m = re.search(r'alt="([^"]*)"', full)
    alt = alt_m.group(1) if alt_m else f'Image {len(images)+1}'
    b64_m = re.search(r'base64,([A-Za-z0-9+/=]+)', full)
    if not b64_m:
        return full
    b64_data = b64_m.group(1)
    img_id = len(images) + 1
    images.append({
        'id': img_id,
        'alt': alt,
        'data': base64.b64decode(b64_data),
        'filename': f'image{img_id}.png'
    })
    return f'__IMG_{img_id}__'

html_clean = re.sub(r'<img[^>]*base64[^>]*>', extract_img, html)
print(f"Extracted {len(images)} images")

# Get PNG dimensions
def get_png_size(data):
    if len(data) < 24:
        return 800, 600
    w, h = struct.unpack('>II', data[16:24])
    return w, h

# Build drawing XML
def build_drawing(img_id, img_data, r_id):
    w, h = get_png_size(img_data)
    cx = 5400000  # 15cm in EMU
    cy = int(cx * h / w)
    if cy > 5040000:  # Cap at 14cm
        scale = 5040000 / cy
        cx = int(cx * scale)
        cy = 5040000

    return f'''<w:r><w:rPr><w:noProof/></w:rPr><w:drawing><wp:inline distT="0" distB="0" distL="0" distR="0"><wp:extent cx="{cx}" cy="{cy}"/><wp:effectExtent l="0" t="0" r="0" b="0"/><wp:docPr id="{img_id+100}" name="Image {img_id}"/><wp:cNvGraphicFramePr><a:graphicFrameLocks xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" noChangeAspect="1"/></wp:cNvGraphicFramePr><a:graphic xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main"><a:graphicData uri="http://schemas.openxmlformats.org/drawingml/2006/picture"><pic:pic xmlns:pic="http://schemas.openxmlformats.org/drawingml/2006/picture"><pic:nvPicPr><pic:cNvPr id="{img_id+100}" name="{img_id}.png"/><pic:cNvPicPr/></pic:nvPicPr><pic:blipFill><a:blip r:embed="{r_id}"/><a:stretch><a:fillRect/></a:stretch></pic:blipFill><pic:spPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="{cx}" cy="{cy}"/></a:xfrm><a:prstGeom prst="rect"><a:avLst/></a:prstGeom></pic:spPr></pic:pic></a:graphicData></a:graphic></wp:inline></w:drawing></w:r>'''

# Replace placeholders
for img in images:
    r_id = f'rId{img["id"]+10}'
    drawing = build_drawing(img['id'], img['data'], r_id)
    html_clean = html_clean.replace(f'__IMG_{img["id"]}__', drawing)

# Extract body
body_match = re.search(r'<body[^>]*>(.*)</body>', html_clean, re.DOTALL)
body_html = body_match.group(1) if body_match else html_clean

# Convert HTML to OOXML (simplified)
body_xml = body_html
body_xml = re.sub(r'<p[^>]*>', '<w:p><w:r><w:t xml:space="preserve">', body_xml)
body_xml = re.sub(r'</p>', '</w:t></w:r></w:p>', body_xml)
for i in range(1, 5):
    body_xml = re.sub(f'<h{i}[^>]*>', f'<w:p><w:pPr><w:pStyle w:val="Heading{i}"/></w:pPr><w:r><w:t xml:space="preserve">', body_xml)
    body_xml = re.sub(f'</h{i}>', '</w:t></w:r></w:p>', body_xml)
body_xml = re.sub(r'<table[^>]*>.*?</table>', '', body_xml, flags=re.DOTALL)
body_xml = re.sub(r'<ul[^>]*>', '', body_xml)
body_xml = re.sub(r'</ul>', '', body_xml)
body_xml = re.sub(r'<li[^>]*>', '<w:p><w:r><w:t xml:space="preserve">• ', body_xml)
body_xml = re.sub(r'</li>', '</w:t></w:r></w:p>', body_xml)
body_xml = re.sub(r'<[^>]+>', '', body_xml)
body_xml = re.sub(r'\s+', ' ', body_xml)

document_xml = f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:wp="http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing" xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:pic="http://schemas.openxmlformats.org/drawingml/2006/picture">
<w:body>
{body_xml}
<w:sectPr>
<w:pgSz w:w="11906" w:h="16838"/>
<w:pgMar w:top="1134" w:right="1134" w:bottom="1134" w:left="1701" w:header="0" w:footer="0" w:gutter="0"/>
</w:sectPr>
</w:body>
</w:document>'''

rels = ['<?xml version="1.0" encoding="UTF-8" standalone="yes"?>',
        '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">']
for img in images:
    r_id = f'rId{img["id"]+10}'
    rels.append(f'<Relationship Id="{r_id}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image" Target="media/{img["filename"]}"/>')
rels.append('</Relationships>')
rels_xml = '\n'.join(rels)

content_types = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
<Default Extension="xml" ContentType="application/xml"/>
<Default Extension="png" ContentType="image/png"/>
<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
</Types>'''

with zipfile.ZipFile(DOCX_PATH, 'w', zipfile.ZIP_DEFLATED) as z:
    z.writestr('[Content_Types].xml', content_types)
    z.writestr('word/document.xml', document_xml)
    z.writestr('word/_rels/document.xml.rels', rels_xml)
    for img in images:
        z.writestr(f'word/media/{img["filename"]}', img['data'])

print(f"✓ Built {DOCX_PATH}")
print(f"  Size: {os.path.getsize(DOCX_PATH)/1024:.1f} KB")
print(f"  Images embedded: {len(images)}")

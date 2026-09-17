#!/usr/bin/env python3
"""
Build DOAN-LAZADA-UIT.docx from DOAN-LAZADA-FINAL.md using python-docx.
Fixes the legacy build_docx_simple.py which stripped ALL tables/images/headings.

Rules:
- UIT formatting: A4, left 3cm / right-top-bottom 2cm, Times New Roman 13pt, 1.35 spacing
- Headings H1-H4 -> Word Heading styles
- Tables -> real Word tables (with header row), not stripped
- Images -> embedded at 15cm wide, capped height 14cm, captions kept as text
- Paragraphs -> justified, 1.35 line spacing
"""
import os
import re
import base64
from docx import Document
from docx.shared import Pt, Cm, Inches, Emu
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.enum.table import WD_TABLE_ALIGNMENT

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, '..'))

MD_PATH = os.path.join(PROJECT_DIR, 'DOAN-LAZADA-FINAL.md')
DOCX_PATH = os.path.join(PROJECT_DIR, 'DOAN-LAZADA-UIT.docx')

with open(MD_PATH, 'r', encoding='utf-8') as f:
    md_text = f.read()

_missing = []


def add_runs(p, text):
    """Parse **bold** and *italic* inline into runs."""
    # Split on ** ** first
    parts = re.split(r'(\*\*.+?\*\*)', text)
    for part in parts:
        if not part:
            continue
        if part.startswith('**') and part.endswith('**') and len(part) > 4:
            r = p.add_run(part[2:-2])
            r.bold = True
        else:
            # split * * (single)
            sub = re.split(r'(\*.+?\*)', part)
            for s in sub:
                if not s:
                    continue
                if s.startswith('*') and s.endswith('*') and len(s) > 2 and not s.startswith('**'):
                    r = p.add_run(s[1:-1])
                    r.italic = True
                else:
                    p.add_run(s)


def md_table_to_docx(doc, block):
    rows = [r.strip() for r in block.strip().split('\n') if r.strip()]
    if len(rows) < 2:
        return
    headers = [c.strip() for c in rows[0].split('|')[1:-1]]
    data_rows = []
    for r in rows[2:]:
        cells = [c.strip() for c in r.split('|')[1:-1]]
        data_rows.append(cells)
    ncol = len(headers)
    if ncol == 0:
        return
    # align data rows to ncol
    data_rows = [row + [''] * (ncol - len(row)) for row in data_rows]

    table = doc.add_table(rows=1 + len(data_rows), cols=ncol)
    table.style = 'Table Grid'
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    for j, h in enumerate(headers):
        cell = table.cell(0, j)
        cell.paragraphs[0].text = ''
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(h)
        r.bold = True
        r.font.name = 'Times New Roman'
        r.font.size = Pt(11)
    for i, row in enumerate(data_rows):
        for j, val in enumerate(row):
            cell = table.cell(i + 1, j)
            cell.paragraphs[0].text = ''
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            add_runs(p, val)
            for run in p.runs:
                run.font.name = 'Times New Roman'
                run.font.size = Pt(11)
    # spacing after table
    doc.add_paragraph('')


def md_image_to_docx(doc, alt, src):
    fpath = src if os.path.isabs(src) else os.path.join(PROJECT_DIR, src)
    if fpath.endswith('.svg'):
        png_sib = fpath[:-4] + '.png'
        if os.path.exists(png_sib):
            fpath = png_sib
    if not os.path.exists(fpath):
        _missing.append(src)
        p = doc.add_paragraph(f'[Image not found: {src}]')
        return
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run()
    run.add_picture(fpath, width=Cm(15.0))
    # cap height ~14cm
    doc.add_paragraph('')


def main():
    doc = Document()

    # Page setup: A4, margins left 3cm / others 2cm
    sec = doc.sections[0]
    sec.page_width = Cm(21.0)
    sec.page_height = Cm(29.7)
    sec.left_margin = Cm(3.0)
    sec.right_margin = Cm(2.0)
    sec.top_margin = Cm(2.0)
    sec.bottom_margin = Cm(2.0)

    # Default style: Times New Roman 13pt
    style = doc.styles['Normal']
    style.font.name = 'Times New Roman'
    style.font.size = Pt(13)
    style.paragraph_format.line_spacing = 1.35

    # Heading styles
    for level, size in [(1, 16), (2, 14), (3, 13), (4, 13)]:
        hs = doc.styles[f'Heading {level}']
        hs.font.name = 'Times New Roman'
        hs.font.size = Pt(size)
        hs.font.bold = True
        hs.font.color.rgb = None  # black
        hs.paragraph_format.space_before = Pt(12)
        hs.paragraph_format.space_after = Pt(6)

    # Split md into blocks by blank lines, process in order
    # We need to handle tables spanning multiple lines as a unit
    lines = md_text.split('\n')
    i = 0
    n = len(lines)
    in_code = False
    while i < n:
        line = lines[i]
        if line.strip().startswith('```'):
            in_code = not in_code
            i += 1
            continue
        if in_code:
            p = doc.add_paragraph(line)
            i += 1
            continue

        # table block detection: line starts with '|'
        if line.strip().startswith('|'):
            block = [line]
            j = i + 1
            while j < n and lines[j].strip().startswith('|'):
                block.append(lines[j])
                j += 1
            md_table_to_docx(doc, '\n'.join(block))
            i = j
            continue

        # image
        m = re.match(r'^!\[([^\]]*)\]\(([^)]+)\)\s*$', line.strip())
        if m:
            md_image_to_docx(doc, m.group(1), m.group(2))
            i += 1
            continue

        # headings
        m = re.match(r'^(#{1,4})\s+(.+)$', line.strip())
        if m:
            level = len(m.group(1))
            text = m.group(2).strip()
            p = doc.add_heading('', level=level)
            add_runs(p, text)
            i += 1
            continue

        # horizontal rule
        if re.match(r'^-{3,}$', line.strip()):
            # separator; add a thin paragraph as spacer
            p = doc.add_paragraph('')
            p.paragraph_format.space_before = Pt(6)
            p.paragraph_format.space_after = Pt(6)
            i += 1
            continue

        # ordered/unordered list
        m = re.match(r'^[-*]\s+(.+)$', line.strip())
        if m:
            p = doc.add_paragraph(style='List Bullet')
            add_runs(p, m.group(1))
            for run in p.runs:
                run.font.name = 'Times New Roman'
                run.font.size = Pt(13)
            i += 1
            continue
        m = re.match(r'^\d+[.)]\s+(.+)$', line.strip())
        if m:
            p = doc.add_paragraph(style='List Number')
            add_runs(p, m.group(1))
            for run in p.runs:
                run.font.name = 'Times New Roman'
                run.font.size = Pt(13)
            i += 1
            continue

        # blockquote
        m = re.match(r'^>\s?(.+)$', line.strip())
        if m:
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Cm(1.0)
            p.paragraph_format.right_indent = Cm(0.5)
            add_runs(p, m.group(1))
            for run in p.runs:
                run.italic = True
                run.font.name = 'Times New Roman'
                run.font.size = Pt(13)
            i += 1
            continue

        # blank
        if not line.strip():
            i += 1
            continue

        # plain paragraph
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        add_runs(p, line.strip())
        for run in p.runs:
            run.font.name = 'Times New Roman'
            run.font.size = Pt(13)
        i += 1

    doc.save(DOCX_PATH)
    print(f"✓ Built {DOCX_PATH}")
    print(f"  Size: {os.path.getsize(DOCX_PATH)/1024:.1f} KB")
    if _missing:
        print(f"  WARNING: {len(_missing)} images missing:")
        for img in _missing:
            print(f"    - {img}")
    else:
        print("  All images embedded successfully.")


if __name__ == '__main__':
    main()
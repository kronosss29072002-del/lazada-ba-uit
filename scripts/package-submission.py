#!/usr/bin/env python3
"""Đóng gói bộ nộp đồ án IE203 — Lazada BA.

Tạo Lazada-BA-IE203-P11.zip gồm các deliverable được chấm điểm:
  - Báo cáo tổng hợp (DOAN-LAZADA-FINAL.md)
  - Báo cáo Word (.docx + .doc)
  - 10 BPMN AS-IS + 10 BPMN TO-BE (processes/, processes-to-be/)
  - Ảnh BPMN (docs/screenshots/) + phân tích (docs/analysis/, docs/petri-net/)
  - Presentation (slides.md + slides.html)
  - Demo viewer (viewer/) — offline-capable
  - Tài liệu phụ trợ (appendix/, stakeholder/, metrics/, DEVELOPMENT.md, PROCESSES.md, README.md)

Loại trừ: scripts nội bộ, .claude, transient files (_probe*, *.bak*), symlinks.
"""
import os, zipfile, shutil, sys
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # thư mục gốc dự án
PKG = "Lazada-BA-IE203-P11.zip"

# Top-level path (root-relative) -> zip parent folder
INCLUDE_DIRS = [
    "processes", "processes-to-be", "docs", "presentation",
    "viewer", "appendix", "stakeholder", "metrics", "report",
]
INCLUDE_FILES = [
    "README.md", "PROCESSES.md", "DEVELOPMENT.md", "DOAN-LAZADA-FINAL.md",
    "package.json", "index.html", "report.html", "DOAN-LAZADA-UIT.docx",
]
# report/ chứa scripts + .doc — chỉ lấy .doc (báo cáo Word)
REPORT_KEEP = {"DOAN-LAZADA-UIT.doc"}

SKIP_PARTS = {
    ".claude", "node_modules", "__pycache__",
    "_probe_tmp.html", "DOAN-LAZADA-FINAL.md.bak", "DOAN-LAZADA-FINAL.md.bak2",
    "copy-libs.js",  # dev-time bootstrap, không cần trong bộ nộp
}

def zip_dir(zf, src_dir, zip_prefix):
    added = 0
    for cur, dirs, files in os.walk(src_dir):
        dirs[:] = [d for d in dirs if d not in SKIP_PARTS and not d.startswith(".")]
        rel_cur = os.path.relpath(cur, src_dir)
        for f in files:
            if f in SKIP_PARTS or f.endswith((".pyc", ".swp")) or ".bak" in f or ".prelayout" in f:
                continue
            if os.path.basename(src_dir) == "report" and f not in REPORT_KEEP:
                continue
            zip_name = os.path.join(zip_prefix, rel_cur, f) if rel_cur != "." else os.path.join(zip_prefix, f)
            zf.write(os.path.join(cur, f), zip_name)
            added += 1
    return added

def main():
    out = os.path.join(os.path.dirname(ROOT), PKG)
    count = 0
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as zf:
        for d in INCLUDE_DIRS:
            src = os.path.join(ROOT, d)
            if os.path.isdir(src):
                count += zip_dir(zf, src, d)
        for f in INCLUDE_FILES:
            p = os.path.join(ROOT, f)
            if os.path.isfile(p):
                zf.write(p, f)
                count += 1
    size_mb = os.path.getsize(out) / 1e6
    print(f"✓ {PKG}: {count} files, {size_mb:.1f} MB → {out}")
    print(f"  Nội dung: báo cáo (MD+Word), 20 BPMN, screenshots, phân tích, presentation, viewer demo.")

if __name__ == "__main__":
    main()
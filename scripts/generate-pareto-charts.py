#!/usr/bin/env python3
"""Generate Pareto PNG charts for all 10 Lazada processes.
Each chart shows the top waste/problem categories with 80/20 cumulative line."""
import os, subprocess, sys

OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "docs", "screenshots")
os.makedirs(OUT_DIR, exist_ok=True)

# Process data: (number, title, categories with costs in billion VND)
PROCESSES = [
    (1, "Quản lý Nhà bán hàng", [
        ("Compliance review 24-48h", 4.0),
        ("OCR sai → bổ sung HS", 2.5),
        ("OTP xác thực riêng lẻ", 1.5),
        ("Bank validation fail", 1.0),
        ("Resubmit loop", 0.8),
    ]),
    (2, "Quản lý Tranh chấp", [
        ("Mediation chờ seller", 3.2),
        ("Evidence collection", 2.0),
        ("Manual case routing", 1.5),
        ("Refund processing", 1.2),
        ("Escalation delay", 0.8),
    ]),
    (3, "Xử lý Đơn hàng", [
        ("Pickup scheduling delay", 5.0),
        ("Hub sorting error", 3.5),
        ("Manual waybill", 2.0),
        ("Stock mismatch", 1.5),
        ("Packaging rework", 1.0),
    ]),
    (4, "Hoàn trả & Hoàn tiền", [
        ("Return logistics", 4.5),
        ("Manual inspection", 3.0),
        ("Refund approval delay", 2.5),
        ("Condition dispute", 1.5),
        ("Reseller restock", 0.8),
    ]),
    (5, "Chăm sóc Khách hàng", [
        ("Ticket routing manual", 3.0),
        ("Agent handle time", 2.5),
        ("Escalation queue", 2.0),
        ("CSAT follow-up", 1.0),
        ("Knowledge search", 0.8),
    ]),
    (6, "Marketing & Khuyến mãi", [
        ("Campaign approval", 2.5),
        ("Content moderation", 2.0),
        ("Coupon fraud", 1.5),
        ("Manual A/B test", 1.0),
        ("Report aggregation", 0.8),
    ]),
    (7, "Nhân sự & Đào tạo", [
        ("Finance approval 5-10 ngày", 0.60),
        ("Low completion rate 60%", 0.45),
        ("Manual course assign", 0.30),
        ("Compliance cert 48-72h", 0.20),
        ("No skill gap analysis", 0.15),
    ]),
    (8, "Thanh toán & Đối soát", [
        ("COD discrepancy 2-3%", 40.0),
        ("Slow settlement L+2/L+3", 32.0),
        ("Gateway failures", 19.0),
        ("Fraud detection gap", 12.0),
        ("Manual reconciliation", 8.0),
    ]),
    (9, "Logistics & Giao nhận", [
        ("Giao lại (return attempt)", 85.0),
        ("Hub sorting error", 55.0),
        ("Transit delay", 40.0),
        ("Wrong address", 30.0),
        ("COD collection gap", 25.0),
    ]),
    (10, "Vận hành CNTT", [
        ("Bug fix loop 2-5 ngày", 1170),
        ("Deploy failure 15%", 780),
        ("CI/CD pipeline chậm", 585),
        ("Security response 7-14 ngày", 468),
        ("Release cycle dài", 390),
    ]),
]

def generate_svg(num, title, categories):
    total = sum(c[1] for c in categories)
    cum = 0
    data = []
    for name, val in categories:
        cum += val
        pct = val / total * 100
        cum_pct = cum / total * 100
        data.append((name, pct, cum_pct))

    n = len(data)
    bar_w = 100
    chart_left = 120
    chart_right = 820
    chart_top = 110
    chart_bottom = 430
    chart_h = chart_bottom - chart_top
    spacing = (chart_right - chart_left) / n
    x_centers = [chart_left + spacing * (i + 0.5) for i in range(n)]

    bars_svg = ""
    points = []
    for i, (name, pct, cum_pct) in enumerate(data):
        cx = x_centers[i]
        bx = cx - bar_w / 2
        h = (pct / 100) * chart_h
        by = chart_bottom - h
        cy = chart_bottom - (cum_pct / 100) * chart_h
        points.append((cx, cy, cum_pct))
        # Truncate long labels
        label = name if len(name) <= 22 else name[:20] + "…"
        raw_val = categories[i][1]
        # Bar value label: inside bar top (white) when bar tall enough,
        # otherwise above bar — never collides with cumulative badge.
        if h >= 30:
            bar_pct = (f'<text x="{cx}" y="{by + 19}" text-anchor="middle" '
                       f'font-size="13" font-weight="bold" fill="#ffffff">{pct:.1f}%</text>')
        else:
            bar_pct = (f'<text x="{cx}" y="{by - 10}" text-anchor="middle" '
                       f'font-size="13" font-weight="bold" fill="#1e3a8a">{pct:.1f}%</text>')
        bars_svg += (f'''
  <rect x="{bx}" y="{by}" width="{bar_w}" height="{h}" fill="#3b82f6" rx="4" stroke="#1d4ed8" stroke-width="1.5"/>
  {bar_pct}
  <text x="{cx}" y="{chart_bottom + 20}" text-anchor="middle" font-size="11" font-weight="600" fill="#1e293b">{label}</text>
  <text x="{cx}" y="{chart_bottom + 35}" text-anchor="middle" font-size="10" fill="#64748b">{raw_val:.1f} tỷ</text>''')

    path_d = f"M {points[0][0]} {points[0][1]}"
    for cx, cy, _ in points[1:]:
        path_d += f" L {cx} {cy}"

    dots_svg = ""
    for idx, (cx, cy, cum_pct) in enumerate(points):
        # Cumulative badge: default above the dot; if it would collide with
        # the bar-top area (first bars where cy ~= by), push it higher.
        # Also clamp so badge never runs into title/subtitle (y < 92).
        by_i = chart_bottom - (data[idx][1] / 100) * chart_h
        badge_y = cy - 36
        if badge_y + 20 > by_i - 4 and by_i - 4 - 20 >= 92:
            # not enough gap above bar -> place badge higher above bar top
            badge_y = by_i - 26 - 20
        if badge_y < 92:
            badge_y = 92
        # nudge last badge leftwards so it never clips the right axis
        bx_badge = cx - 22
        if bx_badge + 44 > chart_right - 4:
            bx_badge = chart_right - 4 - 44
        dots_svg += f'''
  <circle cx="{cx}" cy="{cy}" r="6" fill="#ef4444" stroke="#ffffff" stroke-width="2"/>
  <rect x="{bx_badge}" y="{badge_y}" width="44" height="20" fill="#fef2f2" rx="4" stroke="#ef4444" stroke-width="1"/>
  <text x="{bx_badge + 22}" y="{badge_y + 14}" text-anchor="middle" font-size="11" font-weight="bold" fill="#991b1b">{cum_pct:.0f}%</text>'''

    # Grid lines
    grid_svg = ""
    for pct_val in [20, 40, 60, 80, 100]:
        y = chart_bottom - (pct_val / 100) * chart_h
        grid_svg += f'\n  <line x1="{chart_left}" y1="{y}" x2="{chart_right}" y2="{y}" stroke="#e2e8f0" stroke-dasharray="4,4" stroke-width="1"/>'

    # Y-axis labels
    ylabels = ""
    for pct_val in [0, 20, 40, 60, 80, 100]:
        y = chart_bottom - (pct_val / 100) * chart_h
        ylabels += f'\n  <text x="{chart_left - 10}" y="{y + 4}" text-anchor="end" font-size="12" fill="#334155" font-weight="600">{pct_val}%</text>'
        ylabels += f'\n  <text x="{chart_right + 10}" y="{y + 4}" text-anchor="start" font-size="12" fill="#b91c1c" font-weight="600">{pct_val}%</text>'

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 950 580" width="950" height="580" style="background:#ffffff; font-family: system-ui, -apple-system, sans-serif;">
  <rect width="950" height="580" fill="#ffffff" rx="12"/>
  <text x="475" y="42" text-anchor="middle" font-size="18" font-weight="bold" fill="#0f172a">BIỂU ĐỒ PARETO — P{num}: {title}</text>
  <text x="475" y="65" text-anchor="middle" font-size="13" fill="#64748b">Quy tắc 80/20: Top vấn đề chiếm ~80% chi phí lãng phí</text>
  <text x="475" y="85" text-anchor="middle" font-size="12" fill="#94a3b8">Tổng chi phí ảnh hưởng: {total:,.1f} tỷ VND/tháng (ước tính)</text>
  {grid_svg}
  <line x1="{chart_left}" y1="{chart_top}" x2="{chart_left}" y2="{chart_bottom}" stroke="#475569" stroke-width="2"/>
  <line x1="{chart_right}" y1="{chart_top}" x2="{chart_right}" y2="{chart_bottom}" stroke="#475569" stroke-width="2"/>
  <line x1="{chart_left}" y1="{chart_bottom}" x2="{chart_right}" y2="{chart_bottom}" stroke="#475569" stroke-width="2"/>
  <text x="40" y="{(chart_top + chart_bottom) / 2}" text-anchor="middle" font-size="13" font-weight="bold" fill="#1e3a8a" transform="rotate(-90 40 {(chart_top + chart_bottom) / 2})">Tỷ lệ Lãng phí (%)</text>
  <text x="910" y="{(chart_top + chart_bottom) / 2}" text-anchor="middle" font-size="13" font-weight="bold" fill="#b91c1c" transform="rotate(90 910 {(chart_top + chart_bottom) / 2})">Tỷ lệ Tích lũy (%)</text>
  {ylabels}
  <line x1="{chart_left}" y1="{chart_bottom - 0.8 * chart_h}" x2="{chart_right}" y2="{chart_bottom - 0.8 * chart_h}" stroke="#10b981" stroke-width="2.5" stroke-dasharray="6,4"/>
  <rect x="{chart_right - 160}" y="{chart_bottom - 0.8 * chart_h - 20}" width="150" height="26" fill="#ecfdf5" rx="4" stroke="#10b981" stroke-width="1"/>
  <text x="{chart_right - 85}" y="{chart_bottom - 0.8 * chart_h - 3}" text-anchor="middle" font-size="12" font-weight="bold" fill="#047857">Ngưỡng Pareto 80%</text>
  {bars_svg}
  <path d="{path_d}" fill="none" stroke="#ef4444" stroke-width="3.5" stroke-linejoin="round"/>
  {dots_svg}
  <rect x="275" y="510" width="400" height="45" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1"/>
  <rect x="295" y="527" width="18" height="12" fill="#3b82f6" stroke="#1d4ed8"/>
  <text x="320" y="537" font-size="12" fill="#334155" font-weight="600">Tỷ lệ lãng phí theo nhóm (%)</text>
  <line x1="500" y1="533" x2="525" y2="533" stroke="#ef4444" stroke-width="3"/>
  <circle cx="512.5" cy="533" r="4" fill="#ef4444"/>
  <text x="535" y="537" font-size="12" fill="#334155" font-weight="600">Tỷ lệ tích lũy (%)</text>
</svg>'''

def svg_to_png(svg_path, png_path):
    """Convert SVG to PNG using rsvg-convert or Inkscape or Chrome."""
    for cmd in [
        ["rsvg-convert", "-o", png_path, svg_path],
        ["inkscape", "--export-type=png", f"--export-filename={png_path}", svg_path],
    ]:
        try:
            subprocess.run(cmd, check=True, capture_output=True, timeout=30)
            return True
        except (FileNotFoundError, subprocess.CalledProcessError, subprocess.TimeoutExpired):
            continue
    return False

def main():
    count = 0
    for num, title, categories in PROCESSES:
        svg_content = generate_svg(num, title, categories)
        svg_path = os.path.join(OUT_DIR, f"pareto-{num:02d}.svg")
        png_path = os.path.join(OUT_DIR, f"pareto-{num:02d}.png")

        with open(svg_path, "w", encoding="utf-8") as f:
            f.write(svg_content)
        print(f"SVG: {svg_path}")

        if svg_to_png(svg_path, png_path):
            sz = os.path.getsize(png_path)
            print(f"  PNG: {png_path} ({sz // 1024} KB)")
            count += 1
        else:
            print(f"  PNG conversion failed — install librsvg2-bin or inkscape")
            print(f"  SVG saved at: {svg_path}")

    print(f"\nDone. {count} PNG charts generated in {OUT_DIR}")

if __name__ == "__main__":
    main()

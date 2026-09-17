#!/usr/bin/env python3
import os

OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "docs", "screenshots")
os.makedirs(OUT_DIR, exist_ok=True)
OUT_SVG = os.path.join(OUT_DIR, "pareto-waste.svg")

categories = [
    ("Hold (Chờ đợi)", 45.0),
    ("Defects (Sai sót)", 30.0),
    ("Move (Di chuyển)", 15.0),
    ("Overdo (Quá mức)", 10.0)
]

cum = 0
data = []
for name, val in categories:
    cum += val
    data.append((name, val, cum))

svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 550" width="100%" height="100%" style="background:#ffffff; font-family: system-ui, -apple-system, sans-serif;">
  <rect width="900" height="550" fill="#ffffff" rx="12"/>
  
  <!-- Title -->
  <text x="450" y="42" text-anchor="middle" font-size="20" font-weight="bold" fill="#0f172a">BIỂU ĐỒ PARETO PHÂN BỐ LÃNG PHÍ QUY TRÌNH XỬ LÝ ĐƠN HÀNG SHOPEE</text>
  <text x="450" y="68" text-anchor="middle" font-size="14" fill="#64748b">Quy tắc Pareto 80/20: 75% lãng phí tập trung ở Chờ đợi (Hold) và Sai sót (Defects)</text>

  <!-- Grid lines -->
  <g stroke="#e2e8f0" stroke-dasharray="4,4" stroke-width="1">
    <line x1="100" y1="120" x2="800" y2="120"/>
    <line x1="100" y1="180" x2="800" y2="180"/>
    <line x1="100" y1="240" x2="800" y2="240"/>
    <line x1="100" y1="300" x2="800" y2="300"/>
    <line x1="100" y1="360" x2="800" y2="360"/>
    <line x1="100" y1="420" x2="800" y2="420"/>
  </g>

  <!-- 80% Pareto Reference Line -->
  <line x1="100" y1="180" x2="800" y2="180" stroke="#10b981" stroke-width="2.5" stroke-dasharray="6,4"/>
  <rect x="640" y="160" width="150" height="26" fill="#ecfdf5" rx="4" stroke="#10b981" stroke-width="1"/>
  <text x="715" y="177" text-anchor="middle" font-size="12" font-weight="bold" fill="#047857">Ngưỡng Pareto 80%</text>

  <!-- Axes -->
  <line x1="100" y1="100" x2="100" y2="420" stroke="#475569" stroke-width="2"/>
  <line x1="800" y1="100" x2="800" y2="420" stroke="#475569" stroke-width="2"/>
  <line x1="100" y1="420" x2="800" y2="420" stroke="#475569" stroke-width="2"/>

  <!-- Y Axis Left Labels (%) -->
  <text x="85" y="425" text-anchor="end" font-size="12" fill="#334155" font-weight="600">0%</text>
  <text x="85" y="365" text-anchor="end" font-size="12" fill="#334155" font-weight="600">20%</text>
  <text x="85" y="305" text-anchor="end" font-size="12" fill="#334155" font-weight="600">40%</text>
  <text x="85" y="245" text-anchor="end" font-size="12" fill="#334155" font-weight="600">60%</text>
  <text x="85" y="185" text-anchor="end" font-size="12" fill="#334155" font-weight="600">80%</text>
  <text x="85" y="125" text-anchor="end" font-size="12" fill="#334155" font-weight="600">100%</text>
  <text x="40" y="260" text-anchor="middle" font-size="13" font-weight="bold" fill="#1e3a8a" transform="rotate(-90 40 260)">Tỷ lệ Lãng phí Từng mục (%)</text>

  <!-- Y Axis Right Labels (Cum %) -->
  <text x="815" y="425" text-anchor="start" font-size="12" fill="#b91c1c" font-weight="600">0%</text>
  <text x="815" y="365" text-anchor="start" font-size="12" fill="#b91c1c" font-weight="600">20%</text>
  <text x="815" y="305" text-anchor="start" font-size="12" fill="#b91c1c" font-weight="600">40%</text>
  <text x="815" y="245" text-anchor="start" font-size="12" fill="#b91c1c" font-weight="600">60%</text>
  <text x="815" y="185" text-anchor="start" font-size="12" fill="#b91c1c" font-weight="600">80%</text>
  <text x="815" y="125" text-anchor="start" font-size="12" fill="#b91c1c" font-weight="600">100%</text>
  <text x="860" y="260" text-anchor="middle" font-size="13" font-weight="bold" fill="#b91c1c" transform="rotate(90 860 260)">Tỷ lệ Tích lũy (%)</text>

  <!-- Bars & Labels -->
'''

x_centers = [187.5, 362.5, 537.5, 712.5]
bar_width = 100

points = []

for i, (name, val, cum_val) in enumerate(data):
    cx = x_centers[i]
    bx = cx - bar_width / 2
    h = (val / 100.0) * 320.0
    by = 420.0 - h
    cy = 420.0 - (cum_val / 100.0) * 320.0
    points.append((cx, cy, cum_val))

    svg_content += f'''  <!-- Bar {i+1} -->
  <rect x="{bx}" y="{by}" width="{bar_width}" height="{h}" fill="#3b82f6" rx="4" stroke="#1d4ed8" stroke-width="1.5"/>
  <text x="{cx}" y="{by - 10}" text-anchor="middle" font-size="14" font-weight="bold" fill="#1e3a8a">{val:.0f}%</text>
  <text x="{cx}" y="445" text-anchor="middle" font-size="13" font-weight="bold" fill="#1e293b">{name}</text>
'''

path_d = f"M {points[0][0]} {points[0][1]}"
for cx, cy, _ in points[1:]:
    path_d += f" L {cx} {cy}"

svg_content += f'''  <!-- Cumulative Line -->
  <path d="{path_d}" fill="none" stroke="#ef4444" stroke-width="3.5" stroke-linejoin="round"/>
'''

for cx, cy, cum_val in points:
    svg_content += f'''  <circle cx="{cx}" cy="{cy}" r="6" fill="#ef4444" stroke="#ffffff" stroke-width="2"/>
  <rect x="{cx - 22}" y="{cy - 28}" width="44" height="20" fill="#fef2f2" rx="4" stroke="#ef4444" stroke-width="1"/>
  <text x="{cx}" y="{cy - 14}" text-anchor="middle" font-size="11" font-weight="bold" fill="#991b1b">{cum_val:.0f}%</text>
'''

svg_content += '''
  <!-- Legend -->
  <rect x="250" y="485" width="400" height="45" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1"/>
  <rect x="270" y="502" width="18" height="12" fill="#3b82f6" stroke="#1d4ed8"/>
  <text x="295" y="512" font-size="12" fill="#334155" font-weight="600">Tỷ lệ lãng phí theo nhóm (%)</text>
  
  <line x1="480" y1="508" x2="505" y2="508" stroke="#ef4444" stroke-width="3"/>
  <circle cx="492.5" cy="508" r="4" fill="#ef4444"/>
  <text x="515" y="512" font-size="12" fill="#334155" font-weight="600">Tỷ lệ tích lũy (%)</text>
</svg>
'''

with open(OUT_SVG, "w", encoding="utf-8") as f:
    f.write(svg_content)

print(f"Pareto SVG generated successfully at {OUT_SVG}")

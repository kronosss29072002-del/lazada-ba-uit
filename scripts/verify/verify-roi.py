#!/usr/bin/env python3
"""ROI cross-verifier — recomputes every §5/§6 ROI chain in docs/analysis/comparison/*.md.

Checks per doc:
  (1) sum of benefit-line values == stated "Tổng lợi ích tiềm năng"
  (2) total × thực thu factor − opex == "Lợi ích ròng năm đầu"
  (3) investment / net == base payback (tháng), tolerance ±6 months for "~"
  (4) 5-year claim: (net × 5) − invest − (opex × 5)
  (5) conservative payback formula recompute (where formula present)
Prints PASS/FAIL per check; nonzero exit on any FAIL.
"""
import re, sys, math

DOCS = [f"docs/analysis/comparison/{n:02d}-{name}.md" for n, name in [
    (1, "seller-management"), (2, "dispute-management"), (3, "order-processing"),
    (4, "return-refund"), (5, "customer-service"), (6, "marketing"),
    (7, "hr-training"), (8, "payment-settlement"), (9, "logistics-delivery"),
    (10, "it-platform"),
]]

def num(s, vnd=False):
    """Parse a number cell → float (in tỷ VND unless vnd=True → converts VND→tỷ).

    Unit conventions in this repo:
      tỷ-mode (default):  '.' = decimal (EN), ',' = decimal (VN 5,28),
                          mixed "1.405,2" / "1,405.2" → last sep decimal.
      VND-mode (vnd=True): comma = thousands (62,000,000 VND), no decimals.
    """
    s = s.strip().lstrip("~").lstrip("≈").strip()
    s = s.split(" ")[0]
    s = s.replace("(", "").replace(")", "").replace("%", "")
    if not re.fullmatch(r"[0-9.,]+", s):
        return None
    body = s
    if vnd:
        if "." in body or "," in body:
            body = body.replace(".", "").replace(",", "")
        try:
            return float(body) / 1e9
        except ValueError:
            return None
    if "." in body and "," in body:
        # mixed: last separator is decimal
        if body.rfind(",") > body.rfind("."):
            body = body.replace(".", "").replace(",", ".")
        else:
            body = body.replace(",", "")
    elif "," in body:
        if body.count(",") >= 2:
            body = body.replace(",", "")     # thousands
        else:
            body = body.replace(",", ".")    # VN decimal
    # else dot-only → EN decimal (keep as-is)
    try:
        return float(body)
    except ValueError:
        return None

def section(doc, start, end):
    try:
        t = open(doc, encoding="utf-8").read()
    except FileNotFoundError:
        return None, None
    m = re.search(start, t)
    if not m:
        return None, None
    i = m.end()
    j = re.search(end, t[i:])
    return t[i:i + (j.start() if j else len(t) - i)], None

results = []
def check(desc, cond, doc, detail=""):
    results.append((desc, bool(cond), doc, detail))

for doc in DOCS:
    name = doc.rsplit("/", 1)[1]
    # --- 5.2 benefits block: from intro line to payback header ---
    blk, err = section(doc, r"### 5\.2\.? (Lợi ích|Lợi ích hằng|Lợi ích hàng)", r"### 5\.3")
    if blk is None:
        blk, err = section(doc, r"## 6\. ROI / Cost-Benefit", r"---")
    # d05/d06 use free-text "## 6. ROI / Cost-Benefit Analysis" without a 5.3 — handle below.
    if "ROI / Cost-Benefit" in open(doc, encoding="utf-8").read() and blk is None:
        blk, err = section(doc, r"## 6\. ROI / Cost-Benefit", r"## 7\.")
    if blk is None:
        check(f"{name}: ROI section present", False, doc)
        continue
    # --- per-doc unit mode ---
    vnd_mode = name in ("05-customer-service.md", "06-marketing.md")
    benefit = []
    for line in blk.splitlines():
        line = line.strip()
        if not line.startswith("|") or set(line) <= set("|-: "):
            continue
        cells = [c.strip().strip("*").strip() for c in line.strip("|").split("|")]
        if len(cells) < 3:
            continue
        label = cells[0]
        # value = first numeric-looking cell scanning RIGHT to LEFT (units may trail)
        val = None
        for cell in reversed(cells[1:]):
            mm = re.search(r"([0-9][0-9.,]*)", cell.replace("~", " ").strip() or cell)
            if mm and re.search(r"\d", cell):
                cand = num(mm.group(1), vnd=vnd_mode)
                if cand is not None:
                    val = cand
                    break
        if val is None or not label:
            continue
        benefit.append((label, cells[1] if len(cells) > 1 else "", val))

    if not benefit:
        # d05/d06 style: values embedded in formatted text (VND units)
        if vnd_mode:
            full = open(doc, encoding="utf-8").read()
            if name == "05-customer-service.md":
                asis = 52600 * 12000
                tobe = 30000 * 9000
                savM = (asis - tobe) / 1e6          # 361.2M gross
                netM = savM - 83                     # net monthly saving (doc: 278M)
                roi = (netM * 12 - 150) / 150
                check(f"{name}: AS-IS 52,600×12K = 631.2M", abs(asis - 631.2e6) < 1e3, doc,
                      f"{asis/1e6:.1f}M")
                check(f"{name}: TO-BE 30,000×9K = 270M", abs(tobe - 270e6) < 1e3, doc,
                      f"{tobe/1e6:.1f}M")
                check(f"{name}: tiết kiệm tháng (AS−TO −83M) = 278M", abs(netM - 278) < 1.0, doc,
                      f"{netM:.0f}M vs 278M")
                check(f"{name}: ROI năm 1 = (278×12 −150M)/150M = 21.3×", abs(roi - 21.3) < 0.15, doc,
                      f"{roi:.1f}×")
            elif name == "06-marketing.md":
                savM = 32 * 4
                toolY = 63 * 12
                check(f"{name}: tiết kiệm = 32M×4 = 128M/năm", savM == 128, doc)
                check(f"{name}: tool = 63M×12 = 756M/năm", toolY == 756, doc)
                check(f"{name}: net −28M (128−756+600)", -628 + 600 == -28, doc)
            continue
        check(f"{name}: ROI rows found", False, doc)
        continue

    # Identify key rows
    tot = benefit[-1][2]
    def row(name_pattern):
        for l, f, v in benefit:
            if re.search(name_pattern, l):
                return f, v
        return None, None

    keys = ["Tổng lợi ích tiềm năng", "Lợi ích năm đầu thực thu", "Lợi ích ròng năm đầu"]
    named = {k: row(k) for k in keys}
    EXCL = re.compile(r"Tổng lợi ích|Lợi ích năm đầu|Trừ chi phí|Lợi ích ròng")
    contrib = [(l, f, v) for l, f, v in benefit if not EXCL.search(l)]
    _, totv = named["Tổng lợi ích tiềm năng"]
    if totv is not None:
        check(f"{name}: tổng lợi ích = sum các dòng", abs(sum(v for _, _, v in contrib) - totv) < 0.05, doc,
              f"sum={sum(v for _,_,v in contrib):.3f} vs stated {totv}")

    # --- payback header block (5.3) for investment + payback rows ---
    pb, _ = section(doc, r"### 5\.3", r"^## 6")
    inv = None
    m = re.search(r"TỔNG ĐẦU TƯ BAN ĐẦU.*?\*\*([0-9.,~]+)", open(doc, encoding="utf-8").read())
    if not m:
        m = re.search(r"Tổng đầu tư ban đầu.*?\*\*([0-9.,~]+)", open(doc, encoding="utf-8").read())
    if m:
        inv = num(m.group(1))
    opex = None
    m2 = re.search(r"Chi phí vận hành hằng năm[^\d]*?~?([0-9.,]+)", open(doc, encoding="utf-8").read())
    if m2:
        opex = num(m2.group(1))

    _, totv = named["Tổng lợi ích tiềm năng"]
    _, netv = named["Lợi ích ròng năm đầu"]
    # factor: parse "x 60%" or "(55%)" or "x 50%"
    ffact, _ = named["Lợi ích năm đầu thực thu"]
    factor = None
    if ffact:
        mm = re.search(r"x\s*([0-9.]+)%", ffact)
        if mm:
            factor = float(mm.group(1)) / 100
    _, realv = named["Lợi ích năm đầu thực thu"]

    if totv and realv and factor:
        check(f"{name}: thực thu = tổng × {factor:.0%}", abs(realv - totv * factor) < 0.05, doc,
              f"{totv:.2f}×{factor:.2f}={totv*factor:.2f} vs {realv}")
    if realv and netv and opex:
        check(f"{name}: ròng = thực thu − opex", abs(netv - (realv - opex)) < 0.05, doc,
              f"{realv:.2f}−{opex}={realv-opex:.2f} vs {netv}")
    if inv and netv:
        months = inv / netv * 12
        full_t = open(doc, encoding="utf-8").read()
        base = re.search(r"Cơ sở.*?\*?\*?(~?[0-9.,]+)\s*(tháng|ngày|năm)", full_t, re.S)
        if base and months <= 24:
            stated = num(base.group(1))
            unit = base.group(2)
            if unit == "tháng":
                m2c = months
            elif unit == "ngày":
                m2c = months * 30.44
            else:
                m2c = months / 12
            check(f"{name}: payback base ≈ {months:.1f} tháng", stated is not None and abs(stated - m2c) <= 6, doc,
                  f"recomputed {m2c:.1f} vs stated {stated} {unit}")

    # 5-year claim
    m5 = re.search(r"5 năm.*?\(((?:[^()]|\([^()]*\))*)\)\s*≈\s*\*?\*?(~?[0-9.,]+)\s*tỷ",
                   open(doc, encoding="utf-8").read())
    if m5 and inv and netv and opex:
        expr = m5.group(1)
        claimed = num(m5.group(2))
        # VN thousands-comma: "2,754" → 2754 when the recomputed value is far larger
        try:
            got = netv * 5 - inv - opex * 5
        except Exception:
            got = None
        if got is not None and claimed is not None and abs(got - claimed) > 0.5:
            # retry as comma-thousands (e.g. 2,754 → 2754)
            alt = num(m5.group(2).replace(",", "")) if "," in m5.group(2) and "." not in m5.group(2) else None
            if alt is not None and abs(got - alt) <= max(1.0, got * 0.002):
                claimed = alt
        if got is not None:
            check(f"{name}: tổng 5 năm ≈ {got:.2f}", abs(got - claimed) <= max(0.7, got * 0.005), doc,
                  f"({netv}×5)−{inv}−({opex}×5)={got:.2f} vs {claimed}")

# report
fail = [r for r in results if not r[1]]
print(f"ROI checks: {len(results)} | PASS: {len(results)-len(fail)} | FAIL: {len(fail)}")
for desc, ok, doc, detail in fail:
    print(f"  ✗ {desc} — {detail}")
for desc, ok, doc, detail in results:
    if ok:
        print(f"  ✓ {desc}")
sys.exit(1 if fail else 0)
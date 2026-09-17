#!/usr/bin/env python3
"""Verify metrics/data.json + dashboard against BPMN ground truth and comparison docs.

Checks:
  (1) task/gateway counts per process match canonical ground truth
  (2) cycle_time.as_is/to_be are consistent with comparison docs (documented mapping)
  (3) cost_per_unit matches the comparison docs
  (4) every dashboard-embedded data.json value matches the on-disk data.json
  (5) no stale d07/d08 figures anywhere in metrics/
Exit nonzero on any FAIL.
"""
import re, json, sys

ROOT = "."
GT = {  # as_tasks, as_gw, to_tasks, to_gw  (canonical, verified)
    "01-seller-management": (14, 15, 13, 7),
    "02-dispute-management": (12, 16, 13, 9),
    "03-order-processing": (26, 17, 22, 9),
    "04-return-refund": (13, 18, 16, 9),
    "05-customer-service": (18, 11, 14, 9),
    "06-marketing": (21, 15, 16, 8),
    "07-hr-training": (17, 15, 21, 15),
    "08-payment-settlement": (22, 16, 17, 14),
    "09-logistics-delivery": (20, 13, 17, 19),
    "10-it-platform": (18, 16, 18, 16),
}
results = []
def check(desc, cond, detail=""):
    results.append((desc, bool(cond), detail))

data = json.load(open("metrics/data.json", encoding="utf-8"))
procs = data["processes"]

# (1) counts vs ground truth
for k, v in procs.items():
    got = (v["tasks_count"]["as_is"], v["gateways_count"]["as_is"],
           v["tasks_count"]["to_be"], v["gateways_count"]["to_be"])
    check(f"{k}: counts match ground truth", got == GT.get(k), f"{got} vs {GT.get(k)}")

# (2) cycle_time consistency table — source of truth from comparison/analysis docs
#     (as_is, to_be, unit) documented in the sources; to_be == doc value or sane rounded
CYCLES = {
    "01-seller-management": ((5.0, 0.083, "ngày"), "40 giờ ≈ 5 ngày → 2 giờ (d01 cmp)"),
    "02-dispute-management": ((5.2, 2.8, "ngày"), "5,2 → 2,8 ngày (d02 cmp)"),
    "03-order-processing": ((4.31, 3.2, "ngày"), "analysis: ~4.3 ngày happy-path (d03)"),
    "04-return-refund": ((8.5, 1.8, "ngày"), "8,5 → 1,8 ngày (d04 cmp)"),
    "05-customer-service": ((0.054, 0.01, "ngày"), "79 phút → ~14 phút (d05 cmp)"),
    "06-marketing": ((21.1, 7.0, "ngày"), "campaign cycle (d06)"),
    "07-hr-training": ((54.0, 17.0, "ngày"), "54 → 15-20 ngày (d07 cmp)"),
    "08-payment-settlement": ((2.9, 1.5, "ngày"), "~2.9 → ~1.5 ngày (d08 cmp)"),
    "09-logistics-delivery": ((4.0, 1.5, "ngày"), "4,0 → 1,5 ngày (d09 cmp)"),
    "10-it-platform": ((6.9, 2.0, "ngày"), "~6,9 ngày → ~20 giờ (d10 cmp)"),
}
for k, v in procs.items():
    (a, b, u), src = CYCLES[k]
    ct = v["cycle_time"]
    check(f"{k}: cycle_time as_is={a}", abs(ct["as_is"] - a) < 1e-9, f"{ct['as_is']} vs {a}")
    check(f"{k}: cycle_time to_be≈doc ({src})", abs(ct["to_be"] - b) < 1e-9 or b <= ct["to_be"] <= b * 1.01,
          f"{ct['to_be']} vs doc {b}")

# (3) cost_per_unit against docs (values pulled from comparison docs)
COSTS = {
    "01-seller-management": (24500, 12000),
    "02-dispute-management": (68000, 19000),
    "03-order-processing": (38900, 19000),
    "04-return-refund": (109000, 45000),
    "05-customer-service": (52600, 30000),
    "06-marketing": (62000000, 30000000),
    "07-hr-training": (4000000, 1800000),
    "08-payment-settlement": (2750, 1200),
    "09-logistics-delivery": (23450, 18000),
    "10-it-platform": (3900000000, 900000000),
}
for k, v in procs.items():
    (a, b) = COSTS[k]
    c = v["cost_per_unit"]
    check(f"{k}: cost_as_is={a:,}", c["as_is"] == a, f"{c['as_is']} vs {a}")
    check(f"{k}: cost_to_be={b:,}", c["to_be"] == b, f"{c['to_be']} vs {b}")

# (3b) report/chapter-3-analysis.md stat lines match BPMN ground truth
CH3 = "report/chapter-3-analysis.md"
ch3 = open(CH3, encoding="utf-8").read()
# inline lines: "WF-net: P places / T transitions"
INLINE = {
    "07": (17, 15, 43, 32), "08": (22, 16, 49, 38),
    "09": (20, 13, 42, 33), "10": (18, 16, 45, 34),
}
sections = re.split(r"(### 3\.\d+\.)", ch3)
cur = None
section_to_proc = {"3.7": "07", "3.8": "08", "3.9": "09", "3.10": "10"}
inline_checked = 0
for part in sections:
    hm = re.match(r"### 3\.(\d+)\.", part)
    if hm:
        cur = f"3.{hm.group(1)}"
    m = re.search(r"Activities (\d+).*?Gateways (\d+).*?WF-net: (\d+) places / (\d+) transitions", part)
    if m and cur in section_to_proc:
        proc = section_to_proc[cur]
        a, g, p, t = map(int, m.groups())
        exp_a, exp_g, exp_p, exp_t = INLINE[proc]
        check(f"chapter-3 {cur} (d{cur[2:]}): acts/gws/P/T match BPMN",
              (a, g, p, t) == (exp_a, exp_g, exp_p, exp_t),
              f"{a}/{g}, {p}/{t} vs {exp_a}/{exp_g}, {exp_p}/{exp_t}")
        inline_checked += 1
# block lines: "Places: P, Transitions: T"
BLOCK = {
    "04": (43, 31), "01": (42, 29), "02": (38, 28),
    "05": (39, 29), "06": (47, 36),
}
block_checked = 0
for name, (exp_p, exp_t) in BLOCK.items():
    # find nearest preceding "processes/NN-" ref
    idx = 0
    while True:
        fm = ch3.find(f"processes/{name}-", idx)
        if fm == -1:
            break
        after = ch3[fm:fm + 2500]
        pm = re.search(r"Places: (\d+), Transitions: (\d+)", after)
        if pm:
            p, t = int(pm.group(1)), int(pm.group(2))
            check(f"chapter-3 d{name}: Places/Transitions match BPMN",
                  p == exp_p and t == exp_t, f"{p}/{t} vs {exp_p}/{exp_t}")
            block_checked += 1
        idx = fm + 20
check("chapter-3: 4 inline + 5 block stat lines found", inline_checked == 4 and block_checked >= 5,
      f"inline={inline_checked} block={block_checked}")

# (4) dashboard.html embeds the same values
dash = open("metrics/dashboard.html", encoding="utf-8").read()
for k, v in procs.items():
    # find the JSON block for this process inside the dashboard
    m = re.search(re.escape(f'"{k}"') + r'\s*:\s*\{', dash)
    if not m:
        check(f"dashboard: block for {k} present", False)
        continue
    seg = dash[m.start():m.start() + 2000]
    for field, key in [("cycle_time", "cycle_time"), ("cost_per_unit", "cost_per_unit")]:
        val = v[field]
        ok = all(str(val.get(ik)) in seg for ik in ("as_is", "to_be"))
        check(f"dashboard: {k}.{field} matches data.json", ok, f"{val}")

# (5) no stale figures
stale = re.findall(r"713\.7|41\.08|8\.8 tỷ|5\.28|4\.08 tỷ|16\.5 tháng", dash + open("metrics/data.json", encoding="utf-8").read())
check("metrics: no stale d07/d08 figures", not stale, str(stale))

fails = [r for r in results if not r[1]]
print(f"Metrics checks: {len(results)} | PASS: {len(results)-len(fails)} | FAIL: {len(fails)}")
for desc, _, det in fails:
    print(f"  ✗ {desc} — {det}")
for desc, ok, det in results:
    if ok:
        print(f"  ✓ {desc}")
sys.exit(1 if fails else 0)
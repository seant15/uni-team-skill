#!/usr/bin/env python3
"""Concept rollup and period blocks for a Meta audit.

Usage:
  python rollup.py ads.json            # ad rows -> concept table
  python rollup.py weeks.json --weeks  # weekly account rows -> 4-week blocks + funnel

ads.json: list of rows as returned by ads_get_ad_entities level=ad (ad_entities parsed),
          needs name, amount_spent.value, omni_purchase, omni_purchase_values.value,
          impressions, landing_page_view, omni_add_to_cart.
weeks.json: list of level=ad_account rows with time_increment="7".
Optional --concept-regex to override how ad names are grouped.
"""
import json, re, sys
from collections import defaultdict

STRIP = re.compile(r"(\s*[-|\u2013]\s*(copy( \d+)?|translated)\b.*$)|(\s*\|\s*\d{8}.*$)", re.I)

def num(v):
    if v is None: return 0.0
    if isinstance(v, dict): v = v.get("value")
    try: return float(v)
    except (TypeError, ValueError): return 0.0

def concept(name, rx=None):
    if rx:
        m = re.search(rx, name)
        return m.group(1).strip() if m else name
    return STRIP.sub("", name).strip() or name

def ads_table(rows, rx=None):
    agg = defaultdict(lambda: dict(n=0, spend=0, p=0, val=0, imp=0, lpv=0, atc=0))
    for r in rows:
        g = agg[concept(r["name"], rx)]
        g["n"] += 1; g["spend"] += num(r.get("amount_spent")); g["p"] += num(r.get("omni_purchase"))
        g["val"] += num(r.get("omni_purchase_values")); g["imp"] += num(r.get("impressions"))
        g["lpv"] += num(r.get("landing_page_view")); g["atc"] += num(r.get("omni_add_to_cart"))
    total = sum(g["spend"] for g in agg.values()) or 1
    print("| Concept | Ads | Spend | Share | Purchases | CPA | ROAS | CPM | ATC/LPV |")
    print("|---|---|---|---|---|---|---|---|---|")
    for c, g in sorted(agg.items(), key=lambda x: -x[1]["spend"]):
        cpa = f"{g['spend']/g['p']:.0f}" if g["p"] else "-"
        roas = f"{g['val']/g['spend']:.2f}" if g["spend"] else "-"
        cpm = f"{g['spend']/g['imp']*1000:.2f}" if g["imp"] else "-"
        atc = f"{g['atc']/g['lpv']*100:.1f}%" if g["lpv"] else "-"
        flag = " (directional)" if g["p"] < 5 else ""
        print(f"| {c.replace('|', '/')} | {g['n']} | {g['spend']:.2f} | {g['spend']/total*100:.1f}% | {int(g['p'])}{flag} | {cpa} | {roas} | {cpm} | {atc} |")

def weeks_table(rows, block=4):
    keys = ["amount_spent", "impressions", "reach", "landing_page_view", "omni_add_to_cart",
            "omni_initiated_checkout", "omni_purchase", "omni_purchase_values"]
    print("| Block | Spend | CPM | Purch | CPA | AOV | ROAS | ATC/LPV | IC/ATC | P/IC |")
    print("|---|---|---|---|---|---|---|---|---|---|")
    for i in range(0, len(rows), block):
        chunk = rows[i:i + block]
        s = {k: sum(num(r.get(k)) for r in chunk) for k in keys}
        sp, p = s["amount_spent"], s["omni_purchase"]
        label = f"{chunk[0].get('date_start')} to {chunk[-1].get('date_stop')}"
        div = lambda a, b: a / b if b else 0
        print(f"| {label} | {sp:.0f} | {div(sp, s['impressions'])*1000:.2f} | {int(p)} | {div(sp, p):.0f} | "
              f"{div(s['omni_purchase_values'], p):.0f} | {div(s['omni_purchase_values'], sp):.2f} | "
              f"{div(s['omni_add_to_cart'], s['landing_page_view'])*100:.1f}% | "
              f"{div(s['omni_initiated_checkout'], s['omni_add_to_cart'])*100:.1f}% | "
              f"{div(p, s['omni_initiated_checkout'])*100:.1f}% |")

if __name__ == "__main__":
    args = sys.argv[1:]
    if not args: sys.exit(__doc__)
    data = json.load(open(args[0]))
    if isinstance(data, dict): data = data.get("ad_entities", data)
    if isinstance(data, str): data = json.loads(data)
    rx = args[args.index("--concept-regex") + 1] if "--concept-regex" in args else None
    weeks_table(data) if "--weeks" in args else ads_table(data, rx)

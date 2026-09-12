#!/usr/bin/env python3
"""
Expand a UNI matrix spec into a Meta Ads Manager bulk-import workbook.

    python3 build_bulk_xlsx.py matrix-spec.yaml -o KUL_202609_batch.xlsx

Emits one row per ad. All ID columns are left blank, which tells Meta to CREATE.
Campaign Status is forced to PAUSED. Budgets are written as integer minor units.

Headers follow Meta's bulk template. Meta changes them occasionally: export one
ad from the target account and diff the header row before a large import.
"""
import argparse, json, sys, re
from pathlib import Path

try:
    from openpyxl import Workbook
except ImportError:
    sys.exit("openpyxl required:  pip install openpyxl --break-system-packages")

HEADERS = [
    "Campaign ID", "Campaign Name", "Campaign Objective", "Campaign Status",
    "Buying Type", "Campaign Daily Budget", "Campaign Lifetime Budget",
    "Campaign Bid Strategy", "Special Ad Categories",
    "Ad Set ID", "Ad Set Name", "Ad Set Daily Budget", "Ad Set Lifetime Budget",
    "Ad Set Run Status", "Start Time", "End Time",
    "Optimization Goal", "Billing Event", "Pixel ID", "Conversion Event",
    "Countries", "Cities", "Age Min", "Age Max", "Gender", "Locales",
    "Interests", "Custom Audiences", "Excluded Custom Audiences",
    "Placements", "Device Platforms",
    "Ad ID", "Ad Name", "Ad Status", "Title", "Body", "Link",
    "Image Hash", "Video ID", "Image File Name",
    "Display Link", "Caption", "Description", "Call to Action",
    "URL Tags", "Page ID", "Instagram Account ID",
]

# Ad-name format codes. VID covers any moving asset (video, UGC, GIF).
FORMAT_CODE = {
    "VID": "VID", "VIDEO": "VID", "UGC": "VID", "GIF": "VID",
    "IMG": "IMG", "IMAGE": "IMG", "STAT": "IMG", "STATIC": "IMG",
    "CAR": "CAR", "CAROUSEL": "CAR",
}

OBJ_SHORT = {
    "OUTCOME_SALES": "SALES", "OUTCOME_LEADS": "LEADS",
    "OUTCOME_TRAFFIC": "TRAFFIC", "OUTCOME_ENGAGEMENT": "ENGAGE",
    "OUTCOME_AWARENESS": "AWARE", "OUTCOME_APP_PROMOTION": "APP",
}


def load(path):
    raw = Path(path).read_text()
    if path.endswith((".yaml", ".yml")):
        try:
            import yaml
        except ImportError:
            sys.exit("pyyaml required for YAML specs:  pip install pyyaml --break-system-packages")
        return yaml.safe_load(raw)
    return json.loads(raw)


def minor_units(value):
    """Accept 50, 50.0 or '$50.00' and return integer cents."""
    if value in (None, ""):
        return ""
    n = float(re.sub(r"[^0-9.]", "", str(value)))
    return int(round(n * 100))


def seg(s):
    return re.sub(r"[^A-Za-z0-9+_-]", "-", str(s)).strip("-")


def build(spec):
    c = spec["campaign"]
    obj = c["objective"]
    launch_date = str(spec.get("launch_date", "")).strip()
    if not re.fullmatch(r"\d{8}", launch_date):
        sys.exit("launch_date must be MMDDYYYY, e.g. 09122026")
    cbo = str(c.get("budget_level", "CBO")).upper() == "CBO"

    campaign_name = c.get("name") or "|".join([
        spec["client"], OBJ_SHORT.get(obj, obj), seg(c["geo_code"]),
        str(c["period"]), seg(c["theme"]),
    ])

    rows, warnings = [], []

    for aud in spec["audiences"]:
        adset_name = aud.get("name") or "|".join([
            spec["client"],
            f"{seg(aud['type'])}-{seg(aud['label'])}",
            seg(aud.get("optimization_goal", spec["defaults"].get("optimization_goal", ""))),
            seg(aud.get("placement", "ADV+")),
        ])

        if cbo and aud.get("daily_budget"):
            warnings.append(f"CBO is on - dropping ad-set budget on '{adset_name}'")

        # learning-phase check
        daily = aud.get("daily_budget") or (
            float(re.sub(r"[^0-9.]", "", str(c.get("daily_budget", 0)))) / max(len(spec["audiences"]), 1)
            if c.get("daily_budget") else 0
        )
        cpa = spec.get("target_cpa")
        if cpa and daily:
            weekly = (float(daily) * 7) / float(cpa)
            # Under CBO Meta pools spend toward winners, so a thin per-ad-set figure is a
            # warning rather than a hard stop. Under ABO each ad set is on its own.
            if weekly < 25:
                warnings.append(
                    f"{'WARN' if cbo else 'BLOCKER'} '{adset_name}': ~{weekly:.1f} events/week "
                    "(<25). Unlikely to exit learning - consolidate ad sets, switch to CBO, "
                    "raise budget, or optimize for a higher-funnel event.")
            elif weekly < 50:
                warnings.append(
                    f"WARN '{adset_name}': ~{weekly:.1f} events/week (<50). Learning phase at risk.")

        for cr in spec["creatives"]:
            copy = {**spec.get("defaults", {}).get("copy", {}), **cr.get("copy", {})}
            # UNI ad naming standard:  [VID/IMG/CAR] | [Ad Name] | [MMDDYYYY]
            ad_name = cr.get("name") or " | ".join([
                FORMAT_CODE.get(str(cr["format"]).upper(), str(cr["format"]).upper()),
                str(cr["ad_name"]).strip(),
                launch_date,
            ])
            rows.append({
                "Campaign Name": campaign_name,
                "Campaign Objective": obj,
                "Campaign Status": "PAUSED",
                "Buying Type": c.get("buying_type", "AUCTION"),
                "Campaign Daily Budget": minor_units(c.get("daily_budget")) if cbo else "",
                "Campaign Lifetime Budget": minor_units(c.get("lifetime_budget")) if cbo else "",
                "Campaign Bid Strategy": c.get("bid_strategy", ""),
                "Special Ad Categories": c.get("special_ad_categories", ""),
                "Ad Set Name": adset_name,
                "Ad Set Daily Budget": "" if cbo else minor_units(aud.get("daily_budget")),
                "Ad Set Lifetime Budget": "" if cbo else minor_units(aud.get("lifetime_budget")),
                "Ad Set Run Status": "PAUSED",
                "Start Time": c.get("start_time", ""),
                "End Time": c.get("end_time", ""),
                "Optimization Goal": aud.get("optimization_goal", spec["defaults"].get("optimization_goal", "")),
                "Billing Event": aud.get("billing_event", spec["defaults"].get("billing_event", "IMPRESSIONS")),
                "Pixel ID": spec["account"].get("pixel_id", ""),
                "Conversion Event": spec["defaults"].get("conversion_event", ""),
                "Countries": c.get("countries", ""),
                "Cities": c.get("cities", ""),
                "Age Min": c.get("age_min", ""),
                "Age Max": c.get("age_max", ""),
                "Gender": c.get("gender", ""),
                "Locales": c.get("locales", ""),
                "Interests": aud.get("interests", ""),
                "Custom Audiences": aud.get("custom_audiences", ""),
                "Excluded Custom Audiences": aud.get("excluded_custom_audiences", ""),
                "Placements": aud.get("placements", spec["defaults"].get("placements", "")),
                "Device Platforms": spec["defaults"].get("device_platforms", ""),
                "Ad Name": ad_name,
                "Ad Status": "PAUSED",
                "Title": copy.get("headline", ""),
                "Body": copy.get("primary_text", ""),
                "Link": copy.get("link", spec["defaults"].get("link", "")),
                "Image Hash": cr.get("image_hash", ""),
                "Video ID": cr.get("video_id", ""),
                "Image File Name": cr.get("image_file", ""),
                "Display Link": copy.get("display_link", ""),
                "Caption": copy.get("caption", ""),
                "Description": copy.get("description", ""),
                "Call to Action": copy.get("cta", spec["defaults"].get("cta", "")),
                "URL Tags": copy.get("url_tags", spec["defaults"].get("url_tags", "")),
                "Page ID": spec["account"]["page_id"],
                "Instagram Account ID": spec["account"].get("instagram_id", ""),
            })

    # copy-limit + uniqueness checks
    seen = set()
    for r in rows:
        key = (r["Ad Set Name"], r["Ad Name"])
        if key in seen:
            warnings.append(f"BLOCKER duplicate ad name in ad set: {r['Ad Name']}")
        seen.add(key)
        if len(str(r["Title"])) > 255:
            warnings.append(f"BLOCKER headline >255 chars on {r['Ad Name']}")
        if str(r["Ad Name"]).count("|") != 2:
            warnings.append(f"BLOCKER ad name not 3-segment: {r['Ad Name']}")
        if len(str(r["Body"])) > 2200:
            warnings.append(f"BLOCKER primary text >2200 chars on {r['Ad Name']}")
        if r["Link"] and not str(r["Link"]).startswith("http"):
            warnings.append(f"BLOCKER link is not http(s) on {r['Ad Name']}")
        if not (r["Image Hash"] or r["Video ID"] or r["Image File Name"]):
            warnings.append(f"BLOCKER no creative asset on {r['Ad Name']}")

    per_adset = {}
    for r in rows:
        per_adset[r["Ad Set Name"]] = per_adset.get(r["Ad Set Name"], 0) + 1
    for name, n in per_adset.items():
        if n > 50:
            warnings.append(f"BLOCKER '{name}' has {n} ads (Meta cap 50)")
        elif n > 6:
            warnings.append(f"WARN '{name}' has {n} ads; Meta typically delivers only 3-6")

    return rows, warnings


def main():
    p = argparse.ArgumentParser()
    p.add_argument("spec")
    p.add_argument("-o", "--out", default="meta_bulk_import.xlsx")
    a = p.parse_args()

    rows, warnings = build(load(a.spec))

    wb = Workbook()
    ws = wb.active
    ws.title = "Bulk Import"
    ws.append(HEADERS)
    for r in rows:
        ws.append([r.get(h, "") for h in HEADERS])
    wb.save(a.out)

    print(f"{len(rows)} ad rows -> {a.out}")
    if warnings:
        print("\n--- PRE-FLIGHT ---")
        for w in sorted(warnings, key=lambda s: not s.startswith("BLOCKER")):
            print(" ", w)
        if any(w.startswith("BLOCKER") for w in warnings):
            print("\nBlockers present. Do not import until resolved.")
            sys.exit(1)
    else:
        print("Pre-flight clean.")


if __name__ == "__main__":
    main()

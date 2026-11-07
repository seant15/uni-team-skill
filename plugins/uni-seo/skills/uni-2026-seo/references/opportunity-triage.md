---
name: uni-2026-seo-opportunity-triage
description: Classify a Search Console opportunity before you choose a URL or write a draft. Measurement rules, verdicts, the 4-gate check for new pages.
---

# Opportunity triage

Read this before Step 2.4 (pick the URL). Not every keyword is a writing job. Classify it first, then choose the play. A rewrite that should have been three internal links wastes the client's approval round.

## Measurement rules (apply before any number goes on a card or a Doc)

| Rule | Why | Source |
|---|---|---|
| Count clicks and impressions at **page level** (or property totals). Use query rows to discover demand only | Anonymized queries are left out of query rows, so summed query rows come in below the chart totals | Google Search Central, "A deep dive into Search Console performance data filtering and limits", https://developers.google.com/search/blog/2022/10/performance-data-deep-dive (verified 2026-11-07) |
| Use **finalised** data for comparisons. Fresh data may still change | The API returns only finalised data unless `dataState=all`; data after `first_incomplete_date` "may still change noticeably". Dates are America/Los_Angeles | Search Console API, Search Analytics: query, https://developers.google.com/webmaster-tools/v1/searchanalytics/query (verified 2026-11-07) |
| House rule: the freshest day you compare is **today minus 3 days** | A safety margin over the fresh window. Google publishes no fixed lag; this number is ours | UNI house default |
| Average position across days or pages is **weighted by impressions**: `sum(position x impressions) / sum(impressions)` | A plain mean lets two impressions at position 60 cancel 20,000 at position 8 | UNI house default |
| Triage on **28 days**. Judge a shipped change on **complete Monday-Sunday weeks**. Never label a 28-day figure "weekly" | Partial or relabelled windows create false wins and drops | UNI house default |
| A missing day is missing, not zero | Filling gaps invents data | UNI house default |

## Verdicts (house defaults; tune per site and write the tuned values in the lock file)

Evaluate per page and query family (head term plus close variants).

| Verdict | Default test (28 days, finalised) | Play | Fail = |
|---|---|---|---|
| Winning | Position 3 or better, CTR at or above the site's own page-1 CTR | Protect. Do not rewrite | A good page loses its ranking to a "refresh" |
| Page 1, no clicks | Position 1-10, 100+ impressions, CTR under a quarter of the site's page-1 CTR | Check **which URL** Google ranks first. Wrong URL (often the homepage) = build or strengthen the right destination. Right URL = title, meta, intent | Title rewritten on a page Google is not even choosing |
| Striking distance | Position 11-20, 50+ impressions | Relevance check, 2-5 contextual internal links, tighten title or H1 only if intent is off. Keep the URL | A full rewrite or URL change resets a page that was climbing |
| Buried with demand | Position past 20, 100+ impressions | Confirm the client really sells or serves it. Then authority: hub structure, internal links, supporting guides, earned links | Mass title rewrites; a title does not lift a page from position 40 |
| Cannibalised | 2+ URLs each take 20%+ of the family's impressions | Pick one owner, point links at it, consolidate the other | A third page splits the query further |
| Absent with demand | Real demand, no page that matches the intent | Run the 4-gate check. Pass = new URL brief | A page written for volume nobody here can serve |
| Starving / named wrong (catalogue sites) | Thin or out-of-stock category; products named by internal SKU instead of the model buyers search | A catalogue or naming decision for the client, not an article | Content propping up an empty shelf; an invented model number |

## The 4-gate check (Absent with demand)

All four must be yes. One no = no new URL; write the reason in the lock file.

1. **Relevant** - the client actually sells or does this.
2. **Available** - in stock, or served in that area.
3. **Ownable intent** - the live SERP shows pages like ours, not only marketplaces, Wikipedia, or a different intent.
4. **Useful traffic** - this visitor could become a lead or a buyer.

## Worth (estimate, say so)

`worth = impressions_28d x (site page-1 CTR - current CTR)`. Use the CTR this site already earns on page 1, not an industry curve. Halve striking-distance estimates. Give no click value for Buried. State the unit ("per 28 days").

## What goes on the client Doc

One line per chosen URL in the INTERNAL section: verdict, evidence (impressions, weighted position, clicks, date range ending on a finalised day), worth with its unit, and the play. The client sees the plan and the reason, not the verdict jargon.

# Meta audit checklist - leaf items

Score each leaf PASS / FAIL / WATCH / BLOCKED. BLOCKED = the tool or UI did not return the field. Never invent a pass. Thresholds marked (UNI) are house rules of thumb from past audits, not Meta rules. Thresholds marked (Meta) have a source in `platform-reality-2026.md`.

---

## 1. SETUP - Tracking

| Leaf | PASS when | Fail means |
|---|---|---|
| Pixel + Conversions API both live | Server events arriving, real time or hourly | Meta optimizes on a partial signal |
| Purchase EMQ | 8+ / 10 (UNI); Meta asks for Good or Great | Fewer purchases matched, weaker optimization |
| Upper-funnel EMQ (PageView, ViewContent, ATC) | 6.5+ (UNI) | Retargeting and lookalike seeds are thin |
| Click ID (fbc) coverage on Purchase and PageView | 60%+ (UNI) | Ad clicks not stitched to the order; flag even when EMQ looks high |
| Purchase dedup (event_id on both browser and server) | No "improve event ID coverage" warning | Double counting |
| Add to Cart sanity | ATC per LPV under ~25% unless a cart app explains it | Gift / upsell apps firing extra ATC; do not read ATC rate as intent |
| Catalog connected, feed healthy | Catalog + product sets exist, no MUST_FIX | No dynamic retargeting possible |
| Customer list | Synced or refreshed in the last 90 days | Lookalikes built on a stale seed |
| Website custom audiences | Visitors, ATC, IC, purchasers populated and used | No purchaser exclusion, no retargeting |
| Attribution setting per campaign | Same setting across campaigns being compared | Cross-campaign ROAS is not comparable. Always state the setting next to a ROAS |

## 2. CAMPAIGN - Stats

| Leaf | Read |
|---|---|
| 4-week blocks over 90 days | Spend/day, CPM, avg weekly reach, CPA, AOV, ROAS per block |
| Best block vs current block | Which variable moved: CPM, conversion rate, or AOV |
| Weekly ROAS line | Point to the week it broke and what changed that week (activity log) |
| Total line | 90-day spend, purchases, tracked revenue, ROAS, AOV in one callout |

## 3. FREQUENCY - Reach

| Leaf | WATCH / FAIL when |
|---|---|
| Weekly reach vs weekly spend | Spend up 50%+ and reach flat = saturation (UNI) |
| 30-day frequency by age band | Core band above ~6 while CPM climbs (UNI) |
| Spend share by age band vs return | Cheapest strong band under 20% of spend = underfunded |
| Retargeting pool | Retargeting reach tiny with frequency 10+ = top of funnel is not feeding it |

## 4. TRAFFIC COST - CPM, CPC, placements

| Leaf | Read |
|---|---|
| CPM, CPC, CTR first week vs last week | CTR flat + CPC up = auction or audience, not creative |
| Placement table (spend, share, CPM, link CPC, ROAS) | Feeds, Reels, Stories separately |
| Placement restrictions on ad sets | Manual placements that exclude Reels on a video-led account = FAIL unless tested |
| Format fit | Statics served into Reels and Stories at scale = creative gap, not a placement to cut |
| Seasonality note | Q4 CPM rise is partly market-wide; say which part is controllable |

## 5. CREATIVE - by concept

| Leaf | Read |
|---|---|
| Concept rollup | Strip "Copy", "TRANSLATED", date suffixes; group ads by concept. Report ads per concept |
| Concentration | One concept above 60% of spend = single point of failure (UNI) |
| Concept table | Spend, share, purchases, CPA, ROAS, CPM, ATC per LPV |
| Video hook and hold | 3-sec play / impressions, 25% and 95% watched / impressions, avg watch time |
| Video vs static | Link CTR and CPC side by side; say which format is doing which job |
| New launches | Step 4 readout in SKILL.md, per concept, with launch date |
| Meta labels | Creative limited / Creative fatigue in Delivery (Meta). Quote, do not over-read |
| Winners carried forward | Winners paused with their campaign instead of moved to an always-on slot = FAIL |

## 6. STRUCTURE - Campaigns, ad sets, learning

| Leaf | FAIL when |
|---|---|
| Spending ad sets in 30 days vs purchases per week | Purchases per week per ad set far below 50 (Meta) for every ad set |
| Learning status | No ad set "Active"; all LEARNING or Learning Limited (FAIL status in API) |
| Budget needed to exit learning | Compute: 30-day CPA x 50 / 7 = daily budget per ad set. State it next to actual daily budget |
| Advantage+ audience | Off on single-interest ad sets with no test reason |
| Overlap / fragmentation | Several live ad sets with same creatives and similar audiences; Meta fragmentation flags |
| One campaign per promo | New promo = new campaign each time, learning restarts |
| Budget edits | Activity log: edits of 20%+ or several edits per week on the same campaign |
| Housekeeping | Dozens of paused campaigns, dormant pixels, odd account names |

## 7. FUNNEL - Site and checkout

| Leaf | Read |
|---|---|
| Step rates | LPV to ATC, ATC to IC, IC to purchase, LPV to purchase, per 4-week block |
| Peer percentiles | From the peer benchmark tool; a step below p25 is the lead finding |
| Live product page check | Price, offer consistency, shipping threshold, delivery times, duties / VAT note, payment methods, reviews |
| Live cart check | Free-shipping bar, upsell, express checkout. Add to cart once and note what fires |
| Offer math | AOV vs free-shipping or gift threshold |
| Landing pages per audience | New audience segments with no matching collection page |

## 8. AUDIENCE - Geo and demo

| Leaf | Read |
|---|---|
| Country table | Spend share, purchases, ROAS, CPM. Zero-purchase countries over 1x CPA spend = WATCH |
| CPM outliers | A country at 2x+ the account CPM: check its ad set placements before blaming the market |
| Age x gender | Spend share vs ROAS; say which band is underfunded |

## 9. META SIGNALS

| Leaf | Read |
|---|---|
| Opportunity score | Score and items, with points and the lift string quoted. Match object_ids to entities read |
| Peer benchmark | Lead with the main KPI, then funnel steps above and below peers |
| Auto-recommendations | Advantage+ creative enhancements, value optimization, Reels opt-in: propose only where the data supports it, never auto-apply |

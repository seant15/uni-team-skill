---
name: uni-meta-ads-audit
description: Runs a read-only Meta (Facebook / Instagram) ads account audit in the locked UNI section order - tracking, stats, reach and frequency, traffic cost and placements, creative by concept, structure and learning, funnel and site, audience and geo - then an attack plan where every step traces to a finding. Use for "audit this Meta account", "Facebook ads audit", "why did ROAS drop", "how are the new creatives doing", prospect audits before a proposal, and monthly deep-dives on a client account. Proposes only. Never mutates the account.
---

# Meta ads account audit

Meta audits go wrong in three predictable ways: the numbers get read at ad level when the creative is one concept copied twenty times, a cost problem gets blamed on creative when the leak is at checkout, and the recommendations float free of the findings. This skill fixes the order of work so none of that happens.

This skill is read-only. Do not pause, create, edit, duplicate or reactivate anything. Every change is a proposal with an approval gate. If asked to apply changes in the same turn, stop and hand back to the account owner.

Use the same section order as the last three UNI prospect audits. Do not reorder, merge or skip a section. A section with no data is scored BLOCKED, not dropped.

---

## Step 1 - Interview

The interview gate is the rule in `uni-standards:uni-output`. Ask once, in one batch, skip what is supplied. Never invent an account ID, a target, or a margin.

Required inputs:

1. Which ad account (ID, not only the brand name). Many brands have two accounts. List them and confirm which one carries the spend
2. Mode: **prospect** (audit + plan, goes to a proposal) or **client** (audit + plan for an account we already run)
3. The question behind the audit, in the requester's words ("why is it unstable when we scale", "how are the new visuals doing", "can it carry Black Friday")
4. Target CPA or ROAS, AOV, and margin if known. Otherwise report actuals and say no target was given
5. What launched recently and when (new creatives, offers, audiences, site changes). The audit compares before and after these dates
6. Store-side numbers if shared (Shopify / Klaviyo revenue, returning-customer share). Label them "as shared by the client" with the date
7. Output format: Notion (default), Google Doc, or text

Stop and ask if: two accounts both spent in the window and nobody said which; the purchase event is not the optimization event on a sales account; or someone wants changes made in the same turn.

Unattended run: proceed with stated assumptions at the top of the deliverable. Do not deadlock.

---

## Step 2 - Pull the data

Follow [references/mcp-pull-sequence.md](references/mcp-pull-sequence.md). Order: account list, campaigns 90 days, weekly account rows, ad level 30 days, breakdowns (placement, country, age x gender), dataset quality, ad set settings and learning state, activity log, then Meta's own trend, peer benchmark and opportunity score tools.

Default windows: 90 complete days for the trend, last 30 complete days for the deep-dive, both ending yesterday in the account time zone. State the ISO dates and the currency before any number.

Write every pull to a file and compute in code. Never add up ad rows in your head. [scripts/rollup.py](scripts/rollup.py) does the period blocks and the concept rollup.

Reconcile first: the 30-day total from the country breakdown must match the account row. A mismatch above 2% means stop and find the gap before scoring.

---

## Step 3 - Walk the checklist

Score every leaf in [references/checklist.md](references/checklist.md) PASS / FAIL / WATCH / BLOCKED. Sections, in this order:

1. **SETUP - Tracking.** Pixel + CAPI, EMQ per event, click ID (fbc) coverage, dedup, catalog, customer list freshness, attribution settings per campaign
2. **CAMPAIGN - Stats.** 4-week blocks across 90 days: spend/day, CPM, reach, cost per purchase, AOV, ROAS
3. **FREQUENCY - Reach.** Weekly reach vs spend, frequency by age band, whether reach grows when spend grows
4. **TRAFFIC COST - CPM, CPC, placements.** CTR flat while CPC rises means auction or saturation, not creative. Placement table with spend share
5. **CREATIVE - by concept.** Roll ads up to concepts first. Spend share, ROAS, CPA, hook and hold for video. New launches get their own readout (Step 4)
6. **STRUCTURE - Campaigns, ad sets, learning.** Count of spending ad sets, learning status, events per week vs the 50-event bar, Advantage+ audience state, overlap, budget edits from the activity log
7. **FUNNEL - Site and checkout.** LPV to ATC to IC to purchase, peer percentile per step, then a live check of the product page and cart
8. **AUDIENCE - Geo and demo.** Country and age x gender share of spend vs return
9. **META SIGNALS.** Opportunity score items, peer benchmark gaps, Creative limited / fatigue labels. Quote them, do not obey them

Rule for every section: one table of evidence, then 2 to 5 bullets that say what the numbers mean. A number without a "so what" is noise.

---

## Step 4 - New creative readout

When the brief mentions new visuals, answer four questions per concept, with the launch date stated:

| Question | Read from |
|---|---|
| Did it get enough spend to judge? | Spend vs 1x and 2x the account CPA. Under 1x CPA = no verdict yet |
| Did the click work? | Link CTR, cost per LPV, ATC per LPV vs the incumbent concept |
| Did it sell? | Purchases, CPA, ROAS, with the attribution setting named |
| Why did delivery go where it went? | Same ad set as the incumbent? Placement mix? Country mix? |

"Not enough spend to judge" is a finding, not a gap. Say how much budget a fair test needs: about 2x target CPA per concept, in a slot where it does not compete with the incumbent winner.

---

## Step 5 - Attack plan

Every step traces to a numbered finding. Write "Addresses finding N" under each. A step with no finding behind it is a service being sold; cut it.

Structure, in this order:

1. **This week** - stabilize. No rebuild during a peak or a live promo. Hygiene fixes, tests that need no new assets
2. **Next 2 to 3 weeks** - structure. Usually: one scale campaign, one testing campaign with fixed per-concept budget, retargeting. Name the ad sets to merge or pause, and where their budget goes
3. **After the peak** - evergreen structure, written as a short code block with budget shares
4. **Creative system** - cadence, formats, what is needed from the client
5. **Process** - week by week, first two weeks specific

Promotion and cut rules must carry numbers from this account (for example: promote at 5+ purchases at or under target CPA; cut at 1.5x to 2x target CPA spent with no purchase).

Prospect mode adds Pricing and Next Steps sections. **Leave Pricing as a placeholder** "[pricing from UNI Service Catalog - Sean]". This skill never writes fees.

---

## Step 6 - Validate before delivering

| Check | Fail = |
|---|---|
| Account ID, currency, windows and attribution setting stated at the top | Reader cannot check a single number |
| 30-day total reconciled to the account row | Scoring a partial pull |
| Creative read at concept level, with ad count per concept | "Twenty winners" that are one video |
| All 9 sections present, BLOCKED where data was missing | Silent skip |
| Mixed attribution settings called out before cross-campaign comparison | Comparing 1-day-view numbers to click-only numbers |
| Every attack-plan step says which finding it addresses | Floating recommendations |
| Small samples labelled (under 5 purchases = directional) | A 24x ROAS on two orders sold as a winner |
| No mutations performed or implied as done | Safety break |
| No client pricing written; hyphens only; `uni-output` gate passed | House-standard fail |

Then run `uni-output` on the deliverable. Client-facing numbers carry source and date.

Report template and section skeleton: [references/report-template.md](references/report-template.md). Patterns seen in past audits, useful as hypotheses to test, never as conclusions: [references/audit-patterns.md](references/audit-patterns.md). Platform facts with sources: [references/platform-reality-2026.md](references/platform-reality-2026.md).

---

## Self-Improvement

At the end of every run, before ending:
1. Did any step fail or need a workaround (a tool field missing, a breakdown refused)?
2. Did the user correct or reject a finding or a recommendation?
3. Did a new pattern show up that belongs in `audit-patterns.md`?

Only propose a change if it meaningfully improves the skill. Propose it as a diff for a pull request against `seant15/uni-team-skill` - never edit the installed copy.

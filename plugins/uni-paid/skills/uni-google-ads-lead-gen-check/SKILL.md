---
name: uni-google-ads-lead-gen-check
description: Runs a read-only Google Ads lead-gen optimization check in the locked 9-section checklist order, then a campaign-to-ad-group-to-keyword-to-search-term-to-landing-page intent ladder. Use when someone asks to scan, audit, optimize, checklist, or review a Google Ads lead-gen account, or to draft account optimizations without mutating the account.
---

# Google Ads lead-gen check

Lead-gen accounts fail when spend is scored without intent. A converting click on the wrong specialty, a paused trial that looks ENABLED, or a keyword that does not match its campaign name will produce a clean-looking CPL and a bad book of work.

This skill is read-only. Propose. Do not pause, create, edit, or remove anything. If asked to push changes, stop and hand back to a human. Retire path is pause, never remove.

Default window is 90 complete days in the account timezone, ending yesterday, matching the checklist sheet. State the ISO dates before querying. Use conversions and CPL. Do not use ROAS unless the brief says conversion value is a real lead-gen goal.

Checklist source (Sheet1): `https://docs.google.com/spreadsheets/d/1RtQdRjxyXzTMWW994jRegPbs-BHMQ6UlvF0U-H4Out8/edit`. If the requester attaches another sheet, use that instead. Leaf items live in [references/checklist-order.md](references/checklist-order.md). Do not skip a numbered section or reorder it.

---

## Step 1 - Interview

The interview gate is the rule in `uni-standards:uni-output`. Ask once, in one batch. Skip what is already supplied. Never invent a customer ID, target CPL, or "main" account.

Required inputs:

1. Which Google Ads customer to scan (name is not enough if two accounts share a brand)
2. Manager / MCC login ID if the account sits under one
3. Target CPL band, or "no target, report actual only"
4. What counts as a primary conversion (form, qualified call, booking)
5. Window, if not the 90-day default
6. Output format (Notion / Google Doc / text). Default Notion unless they say otherwise.

Stop and ask if: two accounts share the brand and both have recent spend; conversion value is being used as the bid goal on a lead account; or they want mutations in the same turn as the scan.

If this is an unattended run, proceed with stated assumptions at the top of the deliverable. Do not deadlock.

---

## Step 2 - Resolve what is actually on

Confirm `customer.id`, descriptive name, currency, time zone, and customer status.

Then classify every non-REMOVED campaign on four fields, not one:

| Field | Why |
|---|---|
| `campaign.status` | Switch position (ENABLED can still be dead) |
| `campaign.serving_status` | SERVING vs ENDED vs PENDING vs SUSPENDED |
| Ad group and ad status | A live campaign with paused groups is not a live test |
| Cost in the window | 0 spend means it is not in the optimization set |

Do not recommend "pause this trial" when `serving_status` is already ENDED or the groups are PAUSED and window spend is 0. That is hygiene, not P0. Details: [references/serving-hygiene.md](references/serving-hygiene.md).

Reconcile campaign cost and conversion sums to account totals before drawing conclusions. A material mismatch means stop scoring and report the break.

Cheap queries first: account totals, enabled+serving campaigns, conversion actions. Query patterns: [references/gaql-queries.md](references/gaql-queries.md).

---

## Step 3 - Intent ladder (required, before scoring keywords)

For every SERVING campaign with spend in the window, walk five layers. Method and labels: [references/intent-ladder.md](references/intent-ladder.md).

1. Campaign - the job the name and bid claim to buy
2. Ad group / asset group - the job the group is supposed to isolate
3. Keywords or PMax signals - match type and what is actually enabled
4. Search terms / insights - what was bought
5. Final URL - whether the page can fulfill that query

Score each layer ALIGNED / LEAK / CANNIBAL / WRONG SPECIALTY / PRICE RESEARCH. A converting LEAK is still a LEAK. Do not treat CPL as proof of intent.

PMax has no keywords. Use asset groups as the ad-group layer and search-term insights as the query layer.

---

## Step 4 - Walk the checklist in sheet order

Score every leaf PASS / FAIL / WATCH / BLOCKED. BLOCKED means the API or UI did not return the field. Do not invent a pass.

Do the nine sections in this order. Do not jump to Recommendations first.

1. Keyword Search Review - search terms, negatives, waste, harvest, high CPC vs account, high CPA vs account, match types, auction insights if the API allows, serving-status warnings
2. Ad Review - ads by group (conversion rate, quality, CTR, Ad Strength), split-test state (a second RSA that is PAUSED + PENDING is not a live test), landing page conversion and broken/disapproved URLs, limited approvals and disapprovals, extensions listed on the sheet
3. Quality Score - keywords and ads at or below 5, or Below average components; say whether the fix is copy, page, or expected CTR
4. Bid optimisation - hour, day of week, age, gender, income if present, location, audiences; new audiences to add. Observation only unless the brief asks for modifier math
5. Conversion action checks - which actions are ENABLED, which are primary, whether they fired; call actions if phone is in the mix. Flag primary junk (local actions, YouTube views) even if volume is 0
6. Location targeting - targeted vs observed; off-geo spend; bid modifiers only if the data supports them
7. Campaign goal settings - bidding strategy vs name vs actual CPL vs stated target. If actual CPL is sustainably below tCPA, propose lowering the target. If conversions stalled, find a structural reason before proposing a new goal
8. Quality control - budget vs spend pacing; ENABLED+SERVING campaigns with $0 or runaway CPA. Do not query payment profiles
9. Recommendations tab - list type and impact; apply vs dismiss with a reason. Never auto-apply. Reject Search-to-Display expansion on lead-gen Search unless the brief asks for it

---

## Step 5 - Draft proposals

Rank P0 / P1 / P2. Each item needs: evidence (metric or query), expected effect, risk, and the exact human approval gate.

P0 is live waste or live wrong-intent spend, not corpses. Do not write REMOVE. Write pause, negate, or move.

Then run **uni-output** on the deliverable before it leaves. No em dashes. No client pricing. No fabricated IDs.

---

## Step 6 - Validate before delivering

| Check | Fail = |
|---|---|
| Account ID and window stated, totals reconciled | Scoring a ghost account |
| SERVING vs ENABLED vs ENDED classified | "Pause" advice on a dead trial |
| Intent ladder present for every spending Search/PMax campaign | Keyword table with no campaign job |
| All 9 checklist sections scored, including BLOCKED | Silent skip |
| Lead-gen uses CPL / conversions, not invented ROAS | Wrong goal |
| Every proposal has evidence and an approval gate | Un-actionable advice |
| No mutations performed or implied as already done | Safety break |
| Hyphen only; uni-output gate passed | House-standard fail |

---

## Self-Improvement

At the end of every run, before ending:
1. Did any step fail or need a workaround?
2. Did the user correct or reject anything meaningful?
3. Did the checklist sheet add or rename a leaf?

Only propose a change if it meaningfully improves the skill. Propose it as a diff for a pull request against `seant15/uni-team-skill` - never edit the installed copy.

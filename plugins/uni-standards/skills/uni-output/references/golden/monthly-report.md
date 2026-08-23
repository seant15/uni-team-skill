# GOLDEN SAMPLE - Monthly Performance Report

> **Status:** UNI house template, authored by Sean. Figures in the examples are illustrative.
> **Format:** built in markdown, **exported to Google Doc in plain text** for the client - see the formatting note near the end.
> **Companion:** `weekly-report.md` is the portfolio roll-up. This is the per-brand deep review. They are different documents and neither substitutes for the other.
> **Hard requirements at the bottom of this file.**

---

**What this is:** the monthly review and digest of a media buyer's work on one brand. Weekly reports say *what happened*. The monthly says *what we learned, what it cost, and what we're doing next.*

**Structure - always these five sections, always this order:**

```
0. Internal Cover  ← strip before sending
1. Executive Summary
2. Performance Detail (one table, MoM)
3. Moves Log (what we did, flagged)
4. Deep Dive (why the flagged ones went that way)
5. Next Stage Plan
```

Same order every month, every brand, every buyer. The consistency is the point - the reader learns where to look once and never hunts again.

**Length ceiling:** 3 pages. Section 1 readable in 60 seconds. If a section is bloating, the detail belongs in an appendix.

---

# SECTION 0 - INTERNAL COVER

**Delete this section before the client sees the doc.** This is the buyer talking to the lead.

```
Brand:            [name]
Buyer:            [name]
Period:           [Month Year] · vs [previous Month]
Accounts:         [Google Ads ID] · [Meta Ad Account ID]
Total spend:      $[X]     Budget:  $[X]     Pacing: [X]%

Health:           🟢 On track  /  🟡 Watch  /  🔴 At risk
One-line read:    [What's actually going on, said plainly.]

Client mood:      [What they're happy/unhappy about, said honestly]
Risks not in the client version:
  - [e.g. tracking is unreliable, numbers may restate]
  - [e.g. creative pipeline is dry, next month has nothing new to test]
Where I need backup: [what the buyer needs from the lead]
```

---

# SECTION 1 - EXECUTIVE SUMMARY

For the person who reads nothing else. Five numbers, three sentences, one decision.

```
EXECUTIVE SUMMARY - [Brand] · [Month Year]

The month in one line:
[One sentence. What happened and why it matters.]

The five numbers:
                     This month     Last month      Change
Spend                $[X]           $[X]            [+/-X%]
[Leads / Purchases]  [X]            [X]             [+/-X%]
[CPL / CPA]          $[X]           $[X]            [+/-X%]
[Revenue / ROAS]     [X]            [X]             [+/-X%]
Conv. rate           [X]%           [X]%            [+/-X pts]

What drove it:
- [Driver 1 - the biggest single reason the numbers moved]
- [Driver 2]
- [Driver 3]

What we're doing about it:
[One sentence pointing at Section 5.]

Needs a decision from you:
[The one thing you need the client/lead to say yes or no to. Or: "Nothing this month."]
```

**Rules for this section**

- Five numbers. Not six. Pick the ones tied to the brand's actual goal - if it's lead gen, ROAS doesn't belong here.
- Lead with the truth, good or bad. A bad month reported straight buys more trust than a good month spun.
- "What drove it" means causes, not restated metrics. *"CPA rose 34%"* is the number. *"CPA rose because our two best creatives hit frequency 3.8 and we had no replacements ready"* is the driver.
- Never introduce a number here that doesn't reappear in Section 2.

---

# SECTION 2 - PERFORMANCE DETAIL

Everything in one table. Account by account, campaign by campaign, this month against last.

```
PERFORMANCE DETAIL - [Month] vs [Previous Month]
```

| Account | Campaign | Spend | Δ | Conv | Δ | CPA/CPL | Δ | ROAS | Δ | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| Google | Brand Search | $X | +X% | X | +X% | $X | -X% | X.Xx | +X% | ▲ |
| Google | Non-Brand | $X | +X% | X | +X% | $X | +X% | X.Xx | -X% | ▼ |
| Google | PMax | $X | +X% | X | +X% | $X | -X% | X.Xx | +X% | ● |
| Meta | Prospecting | $X | +X% | X | +X% | $X | +X% | X.Xx | -X% | ▼ |
| Meta | Retargeting | $X | +X% | X | +X% | $X | -X% | X.Xx | +X% | ▲ |
| Meta | Test - [name] | $X | new | X | new | $X | - | X.Xx | - | ★ |
| - | **TOTAL** | **$X** | **+X%** | **X** | **+X%** | **$X** | **-X%** | **X.Xx** | **+X%** | |

**Verdict key:** ▲ Scaling · ● Holding · ▼ Needs fixing · ✕ Killed this month · ★ New test

**Rules for this table**

- Every campaign that spent a dollar appears. No cherry-picking. Killed campaigns stay in the table with ✕ so the trend line stays honest.
- Δ is always month-over-month, same-length periods. If the months differ in length (28 vs 31 days), note it under the table and compare daily averages instead.
- Every row gets a verdict. A row without a verdict means nobody looked at it.
- Impressions, clicks, CTR, CPM, frequency → secondary table or appendix. They don't earn a spot in the primary view unless they *explain* something in Section 4.
- Anomalies get a footnote, not a paragraph: `* Tracking gap Aug 18-20, conversions understated ~12%.`

**Optional secondary table** - only if the brand's story needs it:

| Account | Campaign | Impr | Clicks | CTR | CPC | CPM | Freq |
|---|---|---|---|---|---|---|---|

---

# SECTION 3 - MOVES LOG

Everything we did this month, as a scannable list. Pulled from ClickUp tasks and change history - this should mostly write itself.

```
WHAT WE DID - [Month]
```

| Date | Campaign | Move | Type | Hypothesis | Result | Flag |
|---|---|---|---|---|---|---|
| Aug 3 | Meta Prospecting | Launched 4 UGC creatives | Test | Proof-led hooks beat problem-led | UGC-03 $22 CPA vs $34 avg | 🟢 |
| Aug 7 | Google Non-Brand | Added 34 negatives | Optimize | Cut irrelevant B2B traffic | Wasted spend -$1.2k/mo | 🟢 |
| Aug 11 | Meta Retargeting | Split 7d / 30d windows | Structural | 7d converts cheaper, deserves own budget | No separation, merged back | 🟡 |
| Aug 14 | Google PMax | Raised tCPA $30 → $45 | Optimize | Unlock volume at acceptable CPA | Volume +8%, CPA +51% | 🔴 |
| Aug 22 | Meta Prospecting | Scaled UGC-03 to $250/day | Scale | Winner holds at higher spend | CPA held to $26 | 🟢 |

**Flag key:** 🟢 Nailed it · 🟡 Inconclusive · 🔴 Bad call

**Rules for this section**

- **Type** is one of: Test · Optimize · Scale · Structural · Reactive (client/platform forced it).
- **Every move needs a hypothesis written before the result.** A move with no hypothesis was a guess, and it goes in the log flagged 🟡 with "no hypothesis recorded" - that's information about the process, not just the campaign.
- Bullets, not paragraphs. One line per move. The explaining happens in Section 4.
- 🔴 is not a punishment. A well-designed test that failed is a good month's work; an unstructured change that happened to work is not. Flag the *decision quality*, not just the outcome.
- Target 5-12 moves. Under 5 means the account was on autopilot. Over 12 means we were flailing - say so.
- Anything the client asked for that we advised against goes here, flagged, with the outcome. This is how "we told you so" becomes a professional record instead of an argument.

---

# SECTION 4 - DEEP DIVE

Only the flagged moves - 🟢 and 🔴, plus any 🟡 worth resolving. Usually 2-4 entries. Same shape every time.

```
DEEP DIVE
```

**🟢 [Move name] - [Campaign]**
- **What we did:** [one line]
- **Why:** [the hypothesis, and what made us believe it]
- **What happened:** [the numbers, with the comparison]
- **Why it worked:** [the actual mechanism - not "it performed well"]
- **What we do with it:** [scale it / apply it to the other account / build the next 5 around it]

**🔴 [Move name] - [Campaign]**
- **What we did:** [one line]
- **Why:** [the hypothesis]
- **What happened:** [the numbers, including the cost of being wrong]
- **Why it didn't work:** [the mechanism - what we misread]
- **What it cost:** $[X] and [X] days of learning time
- **What we changed:** [reverted / adjusted / what we'd do differently]

**Rules for this section**

- "Why it worked" must name a mechanism, not restate the result. *"CTR was higher"* is a result. *"The proof-led hook front-loaded the 3-week result in the first 2 seconds, so we paid for fewer unqualified views"* is a mechanism. Mechanisms transfer to other campaigns. Results don't.
- Every 🔴 states its cost in dollars and days. Not to assign blame - so the next test gets budgeted honestly.
- Every deep dive ends with a forward action, and that action must show up in Section 5. No orphan insights.

---

# SECTION 5 - NEXT STAGE PLAN

Two modes. Pick one and commit - don't hedge between them.

## Mode A - Directional

Use when the account needs a strategic shift rather than a task list. Conceptual is allowed. Vague is not.

```
NEXT STAGE - DIRECTION

The bet:      [What we believe is now the biggest lever. One sentence.]
Why now:      [What this month proved that makes this the right move.]
What changes: [What the account looks like different in 60 days.]
Proof point:  [The number that tells us the bet is landing, and by when.]
Kill trigger: [The number that tells us to stop, and by when.]
What we need: [Budget / creative / landing page / client input - be specific.]
First moves:  [3-5 concrete things happening in the next 2 weeks.]
```

A direction without a proof point and a kill trigger is a wish. Both are mandatory.

## Mode B - Action List

Use when the direction is already set and next month is execution.

```
NEXT STAGE - ACTIONS
```

| # | Action | Campaign | Owner | By | Expected impact | Needs client? |
|---|---|---|---|---|---|---|
| 1 | Scale UGC-03 to $400/day in 2 steps | Meta Prospecting | [buyer] | Sep 5 | +40 purchases/mo at ≤$30 CPA | No |
| 2 | Build 5 proof-format creatives | Meta Prospecting | [creative] | Sep 12 | Replace fatiguing winners | Assets needed |
| 3 | Revert PMax tCPA to $32, feed-only test | Google PMax | [buyer] | Sep 2 | Recover CPA to ~$34 | No |
| 4 | Rebuild non-brand into intent tiers | Google Non-Brand | [buyer] | Sep 18 | -15% wasted spend | No |
| 5 | LP speed fix - 4.2s → under 2s | All | [client dev] | Sep 20 | +10-15% CVR | Yes - needs dev |

**Rules for this section**

- Every action has an owner and a date. No owner = it won't happen.
- Expected impact is a number with a direction. "Improve performance" isn't an expected impact.
- The "Needs client?" column is the ask. Anything marked Yes gets restated in Section 1 under "Needs a decision from you."
- Cap at 6 actions. Ten actions is a list nobody executes.
- Every action traces back to something in Section 3 or 4. If it doesn't, either the insight is missing or the action is invented.

---

# NOTES - HOW THIS GETS USED

**Cadence.** Report lands by the 5th working day of the new month. Buyer drafts, lead reviews before the client sees it. The internal cover is the buyer's honest read; the lead's job is to catch anything the buyer is too close to see.

**This is a review of the buyer, not just the account.** Sections 3 and 4 are where that shows. A buyer whose moves log is thin, or whose moves have no hypotheses, has a process problem regardless of what the numbers did. A buyer with clean hypotheses and a couple of well-reasoned 🔴s is doing the job right.

**Weekly vs monthly.** Weekly = what happened and what's next week. Monthly = what we learned and where we're heading. Never copy-paste four weeklies into a monthly - if the monthly reads like a stack of weeklies, the thinking didn't happen.

**How AI fills this.** Sections 2 and 3 are mechanical: pull platform data for the two periods into the table, pull ClickUp task history and platform change logs into the moves log. Sections 1, 4, and 5 are judgment - AI drafts, the buyer owns. Never ship an AI-written "why it worked."

**Flags are the currency.** 🟢 and 🔴 are how the team learns across brands. At quarter close, pull every 🟢 mechanism across all accounts - that's the house playbook, built from evidence instead of opinion.

**Formatting when it goes out.** Per UNI reporting house style, the client-facing export strips markdown symbols: plain-text headings in Title Case or ALL CAPS, space-aligned tables, no `###` and no `**`. Build in this template, export clean.

**The honesty rule.** Bad months get reported at the same length and detail as good ones.

**All-green check.** If every flag in the moves log is green, raise it with the buyer before the report goes out: *"Every move this month came back green. Worth a look - was anything genuinely tested, or is something not making it into the log?"* Sometimes the answer is that it really was a clean month, and that is a fine answer. The point is that nobody notices an all-green month on their own, and the two failure modes it can hide - nothing was tested, or something is being left out - are both expensive. Ask, accept the answer, move on.

---

## Hard requirements

1. **Five sections, always this order**, plus the internal cover that gets deleted before sending. Consistency is the feature.
2. **Three pages maximum.** Section 1 readable in 60 seconds.
3. **Five numbers in the executive summary. Not six.** Tied to the brand's actual goal.
4. **Every number in Section 1 reappears in Section 2.** No orphan figures.
5. **Every campaign that spent a dollar appears in the table**, including killed ones, marked as killed.
6. **Every move has a hypothesis written before the result.** No hypothesis means it was a guess, and it gets logged as one.
7. **Every deep dive names a mechanism, not a result.** Mechanisms transfer to other campaigns. Results do not.
8. **Every red flag states its cost in dollars and days.**
9. **Every deep dive ends in a Section 5 action, and every Section 5 action traces back to Section 3 or 4.** No orphan insights, no invented actions.
10. **A direction without a proof point and a kill trigger is a wish.** Both mandatory in Mode A.
11. **No pricing.** Media spend and budget pacing are performance data. Fees, retainers and rates are not, and never appear.
12. **Zero em dashes and en dashes.** Hyphens only.
13. **Client export is plain text.** Title Case or ALL CAPS headings, space-aligned tables, no `###`, no `**`.
14. **All-green triggers a question, not a rejection.** If every flag is green, ask the buyer whether anything was genuinely tested and whether anything is missing from the log. A clean month is a legitimate answer.

## The flag key is the one emoji exemption in all of UNI output

`uni-output` bans emoji everywhere. **The green / amber / red flags in Sections 3 and 4 are the single named exemption**, and this document is the reason the exemption exists.

They earn it because they are not decoration and not a style choice. They encode **decision quality**, consistently, across every account and every buyer, which is what makes the quarterly cross-brand pull possible: every green mechanism from every account, in one place, built from evidence rather than opinion. No other symbol in UNI output does that job.

**The exemption does not generalise.** "It has a legend, so it is data" is not a licence to introduce emoji elsewhere. If a new one seems warranted, it goes to Sean.

The verdict marks in the Section 2 table are plain glyphs, not emoji, so they were never covered by the ban. Same for arrows and bullets. Use them where they carry meaning.

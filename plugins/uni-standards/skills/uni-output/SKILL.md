---
name: uni-output
description: The UNI house standard for anything that leaves the building - client-facing or team-facing. Use this BEFORE writing any deliverable (report, audit, proposal, brief, recap, recommendation, update) and as the final gate before sending. Also use when someone asks "is this up to standard", "make this UNI style", "clean this up before I send it", or when a draft feels bloated, generic, or AI-written. Defines the three permitted output formats (Notion markdown, Google Doc, text message), the intake interview, and the AI-slop ban list.
---

# UNI Output Standard

Everything UNI ships is **direct, minimal, and load-bearing**. In a market moving this fast, a client's signal that we are worth keeping is that our documents respect their time and still contain more substance than anyone else's.

The rule that governs every judgment call below:

> **Internal analysis can be as long as it needs to be. Output cannot.**
> Do the thinking at full length. Ship the conclusion.

## Scope

**This skill covers operations only.** UNI team skills never generate, quote, estimate, or negotiate pricing - not retainers, not media budgets framed as a price, not scope-to-fee mapping. If a task drifts toward commercials, stop and hand it back to Sean. Say so plainly rather than producing a placeholder number.

## Typography - non-negotiable

**UNI never uses the em dash (`—`, U+2014) or the en dash (`–`, U+2013). We use the hyphen `-` (U+002D). 100% of the time, in every format.**

This is not a preference. It applies to client documents, internal docs, ad copy, text messages, Notion, Google Docs, and anything a skill in this repo produces. The em dash is the loudest single tell that a document was machine-written, and one of them undoes an otherwise clean page.

| | |
|---|---|
| Wrong | `Spend is up 40% — mostly on one campaign.` |
| Right | `Spend is up 40%, mostly on one campaign.` |
| Right | `Spend is up 40% - mostly on one campaign.` |

Where an em dash was doing real work, prefer a comma, a colon, or a full stop. A spaced hyphen is fine, but two in one paragraph means the sentences want splitting.

Same rule for ranges: write `Aug 1-21`, `1-5`, `3-8`. Never `Aug 1–21`.

**Search the finished document for both characters before sending.** It is check 0 on the gate below.

---

## The interview gate - applies to every UNI skill

**No UNI skill produces a deliverable from an incomplete brief.** This is the rule the whole system rests on, and every skill in this repo implements it the same way.

### How it runs

**1. Check what is missing.** Compare the request against that skill's required-inputs list. Anything not supplied is missing, including things the requester probably assumed were obvious.

**2. Ask once, in one batch.** Numbered questions, all at the same time. Never drip one question, get an answer, then ask another - that is four round trips for something that should take one. Skip anything already supplied; re-asking is its own failure.

**3. Where a safe default exists, propose it instead of asking open.** "Assuming Notion unless you say otherwise" gets answered in two seconds. "What format would you like?" costs a message.

**4. Lock the brief before producing.** Once the answers are in, restate the brief in under 10 lines and confirm before writing anything substantial:

```
BRIEF LOCK
Client:      ...
Deliverable: ...        Format: ...
Audience:    ...        Purpose: ...
Constraints: ...
Assuming:    ... (anything inferred rather than told)
Proceeding unless you correct any of the above.
```

The Assuming line is the important one. It surfaces every inference in a place the requester can catch it cheaply, before the work is done rather than after.

**5. Never fill a gap with a plausible value.** No invented numbers, no `[TBD]` left in a shipped document, no guessing at a client's tone. If it is unknown, it is a question.

### The stop-and-ask list

Every skill names the cases where guessing is worse than asking. Those are hard stops - the skill does not proceed, even with the rest of the brief complete. Across all skills the standing hard stops are:

- **A number whose source or date range is ambiguous**
- **Two data sources that disagree**
- **A claim with no evidence behind it**
- **Anything that touches pricing or commercial terms**
- **A brand with no stated tone and no example to work from**

### The one exception

If the requester says to proceed without answers, or the run is unattended and nobody is there to reply, **do not deadlock.** Make the most reasonable call, put the assumptions at the top of the deliverable under `ASSUMPTIONS - confirm before this goes to the client`, and carry on. A stalled deliverable helps nobody; an unlabelled guess is worse than both.

---

## Step 1 - Interview before you write

Never draft from a thin brief. Ask for what is missing, in one batch, then write. If the requester supplied it already, do not re-ask.

**Always establish:**

1. **Client / brand** - who is this for, what do they actually sell
2. **Brand positioning and tone** - premium, mass, technical, playful, clinical? Ask for one existing piece they consider on-brand
3. **Audience** - who reads this document, and what do they already know
4. **Purpose** - what should the reader do or decide after reading
5. **Format** - Notion, Google Doc, or text message (see Step 2)
6. **Hard constraints** - length ceiling, must-include figures, anything legally or contractually mandated
7. **Data source** - where the numbers come from, and the exact date range

**Ask, don't assume, when it changes the writing:**

- Is this the first thing this reader sees from us, or a continuation?
- Are we delivering good news, bad news, or a recommendation they may resist?
- Is any figure provisional or still being validated?

**Stop and ask** if: the date range is ambiguous, two data sources disagree, or the brief implies a commercial decision. Never fill a gap with a plausible number.

---

## Step 2 - Only three output formats exist

| Format | When | How to produce it |
|---|---|---|
| **Notion (markdown)** | Internal docs, SOPs, briefs, research, anything the team works inside | Clean markdown. H2/H3 only, no H1 in body. **One blank line before and after every section heading, table, and list** - Notion renders dense blocks as a wall and nobody reads a wall. Tables over bullet walls where the content is comparative. No emoji as section markers. |
| **Google Doc** | Anything a client reads or comments on - reports, audits, proposals, strategy docs | Written so it survives being commented on line by line. Short paragraphs, each making one point. Numbers in a table, not in prose. **Client-facing exports are plain text**: Title Case or ALL CAPS headings, space-aligned tables, no `###`, no `**`. Build in markdown, export clean. |
| **Text message** | Quick updates, flags, approvals, "heads up" | Under 5 lines. One subject only. No greeting theater. Lead with the thing that changed. |

Anything else - a PDF, a deck, a spreadsheet - is a **conversion of one of these three**, and needs Sean's explicit go-ahead. Do not invent a fourth format because it feels nicer.

The lint file in Step 2b is not a fourth format. It is the machine-checkable intermediate a paid-media deliverable passes through on its way to one of these three.

---

## Step 2b - The paid-media output contract

Four skills produce something a buyer pastes straight into Ads Manager, or hands to a designer: `meta-ad-copy`, `meta-targeting`, `ad-ideas`, `creative-brief`. Their content has not been the problem. **Their shape has.** A deliverable the buyer has to reformat by hand costs more than writing it from scratch, so it quietly stops getting used.

Prose rules did not hold. Versions of the rules below already sat in those files and were skipped, because nothing in the pipeline could refuse the output. **So the contract is mechanical and it is checked by a script.**

The same test applies to any rule added here later: **if nothing can tell whether you followed it, it is not a rule.** That is why none of these skills asks you to draft a large internal pool and hand over the best few. Nobody downstream can see the pool, so the instruction costs nothing to skip and the file reads identical either way. Write the number of pieces the contract asks for, hold each one to the bar, and rewrite the ones that miss.

```
python skills/uni-output/scripts/lint-ads-output.py <file> --type meta-copy|targeting|ad-ideas|brief
```

**Where the linter sits depends on how you got these skills; nothing else about it changes.** In this marketplace it travels with `uni-standards` at `skills/uni-output/scripts/lint-ads-output.py`. In an AI Agentic OS checkout it is `tools/checks/lint-ads-output.py`. Same script, same flags, same exit codes. Every command line in this file and in the other four is written for one layout - **if yours differs, resolve the path once at the start of the session and substitute it everywhere.** Do not paste a second path into the skill files; a file carrying two commands gets skimmed and the wrong one gets run. A path that does not resolve is a missing gate, not a passing one, so a command that errored is never reported as "checked".

**Write the deliverable to a file, run the lint, fix every P1, then paste or send.** Exit code 1 means it is not deliverable. A deliverable that never went through the lint is a draft, and saying "checked" without the exit code is the failure this section exists to stop.

Run it before *and* after any fix, and report the line in the handoff:

```
Lint: meta-copy 5/5 pass (P1=0, P2=1)
```

### Contract 1 - Meta primary text

Write to file in exactly this shape, one block per variant. The delimiters are what makes it parseable; do not reword them.

```
=== VARIANT 1 ===
Angle: three words
Length: short | long-fb | long-aida
Register: 3
Placement: feed | reels | stories
PRIMARY TEXT
New arrivals just landed.

Boutique quality your mini will actually want to wear, priced like it isn't. Shop the new collection.
END PRIMARY TEXT
Headline: New Arrivals Are Here
Description: -
CTA: SHOP_NOW
Counts: hook 25 / total 128
```

**The counting convention, because an example is not a spec.** `hook` is the length of block 1 with surrounding whitespace stripped. `total` is the length of the whole primary text between the delimiters, stripped at both ends, **with the blank lines between blocks counted** - they are characters and they cost you visible space. In the example above that is 25 and 128. The lint recomputes both and tolerates one character of drift, so a convention that is off by two fails.

**A header above the first `=== VARIANT 1 ===` is allowed and often required** - the `ASSUMPTIONS` block belongs there when you were told to proceed without answers. The parser scans for delimiters rather than requiring the file to open with one.

Hard rules, all lintable:

| # | Rule | P1 fail = |
|---|---|---|
| 1 | Short copy is **at least two blocks** separated by one blank line. **Block 1 is the hook, exactly one sentence, always alone.** | Hook buried in a paragraph |
| 2 | **Block 2 carries at most two sentences and may include the CTA.** If the body needs two sentences of its own, the CTA moves to a third block. Short copy never exceeds three blocks. | CTA buried behind two sentences of body |
| 3 | Long copy: **no paragraph over three sentences.** Bullet and feature blocks are exempt. | Wall of text |
| 4 | Long copy: **the last paragraph is the CTA and nothing else**, one or two sentences, and it has to be strong. | Ad ends on a feature |
| 5 | The hook carries the specific thing inside the **first 40 characters**. | Nothing lands before the fold |
| 6 | `reels` and `stories` placements deliver **short only**. Long copy is Feed only. `Length` values are `short`, `long-fb` (feature and benefit) and `long-aida`. | 900 characters on a Reel |
| 7 | **No emoji unless the buyer asked for them in this request.** | House rule broken |
| 8 | `Counts:` present and arithmetically correct. Count, do not estimate. | Unverifiable delivery |
| 9 | **One `Register:` value across the whole file.** The length test holds register constant so length is the only variable. | Two tests at once, reads as neither |
| 10 | **Exactly five variants.** Five is Meta's per-ad maximum for primary text. Write five and get them right - do not draft a pool and trim it. | A short file, or an unverifiable "top five of twenty" |

**Three character numbers are in play and only one is enforced.** 40 is the rule - it is what survives a small screen and an accessibility text size. 125 is roughly where mobile Feed folds on a normal phone. 80 is how early it can fold on a bad one. Write to 40 and treat the other two as context.

**The fold trade-off, decided 2026-09-08.** Blank lines cost a rendered line each, so the two-block structure can push the CTA below "See more" in Feed. That is accepted: the person who taps See more is the person with intent. Do not silently collapse the blocks to win the fold, and do not present the block structure to a client as a performance rule. It is a readability and paste-ability rule.

### Contract 2 - Meta interest targeting

```
=== CLUSTER 1: Bargain-hunter moms ===
Tier: 2
Chain: moms who chase boutique-for-less also treasure-hunt at off-price retailers
Kill: CPA over 1.5x Tier 1 after 2x ticket price spent
INTERESTS
- name: TJ Maxx | id: 6003... | size: 12M-14M | checked: 2026-09-08 | status: live
- name: Marshalls | id: - | size: - | checked: 2026-09-08 | status: UNCONFIRMED
- name: Ross Dress for Less | id: - | size: - | checked: 2026-09-08 | status: UNCONFIRMED
END INTERESTS
```

| # | Rule | P1 fail = |
|---|---|---|
| 1 | **At least five cluster directions per run.** | Buyer got one idea, not a test plan |
| 2 | **Three to five interests per cluster.** Over eight splits into two clusters. | Unreadable OR-soup |
| 3 | The `name` field is a **literal string the buyer can type into the Ads Manager detailed-targeting search box.** `TJ Maxx` and `Cricut` qualify. `Aesthetic motherhood / cottagecore mom content` and `gentle parenting creators` do not - those are personas, and they belong in `Chain`, never in `name`. | Dead-on-arrival cluster |
| 4 | Every row carries `status`: `live` (seen in Ads Manager or returned valid by the API, with the ID recorded) or `UNCONFIRMED`. **Never write `live` for a row you did not actually check.** | A hallucination wearing a validation stamp |
| 5 | Every `UNCONFIRMED` row says, once per deliverable, that it must be typed into the Ads Manager search box before launch. | Buyer launches on a deleted interest |
| 6 | `id` recorded for every `live` row. Meta renames interests; the ID is the only stable key. | Cannot re-find it next quarter |
| 7 | Every cluster has a stateable `Chain` and a `Kill` condition. | A list, not a hypothesis |

**When the Marketing API is unreachable** (as of 2026-09-08 the Facebook Ads MCP on this machine fails discovery): every row ships `UNCONFIRMED`, and the deliverable says so in one line at the top. Do not claim a validation sweep happened. Also give the buyer, per cluster, one fallback that does not depend on an interest existing at all - broad plus creative, a lookalike, or a custom-audience play - so a dead cluster does not cost him the whole test.

### Contract 3 - Ad ideas

```
=== CONCEPT 1: Cinemagraph Twirl ===
Hook: She's going to live in this all fall.
Gap: absent - nobody in category animates a single still
Angle: demonstration
Idea: Animate only the skirt on an existing model shot. Face and background stay still.
Format: video, 4-6s loop, Reels and Stories
Producible: existing studio shot plus an image-to-video tool. No new shoot.
Risk: AI motion on a face reads as uncanny. Isolate to fabric.
```

| # | Rule | P1 fail = |
|---|---|---|
| 1 | **One field per line.** Label, colon, content. Never two fields on one line. | The wall of text the buyer reported |
| 2 | **One blank line between concepts.** | Concepts run together |
| 3 | `Hook:` is the **second line, right after the concept name**, and it is a written sentence, not a description of one. "A hook about durability" fails. | Buyer cannot skim to the thing that matters |
| 4 | All seven fields present: Hook, Gap, Angle, Idea, Format, Producible, Risk. | Half a concept |
| 5 | **Readability: Flesch-Kincaid grade 7 or below on the concept body.** The lint computes it and prints the number. Do not self-declare a grade - the script decides. Grade over 10 is P1, 8 to 10 is P2. | Unreadable internal doc |
| 6 | **Five to seven concepts.** Write those and get them right - do not draft a pool and trim it. | A short file, or an unverifiable shortlist |

Readability is a deliberately soft-edged rule: the grade formula correlates loosely with how humans actually experience a text, so the script reports the number rather than pretending it is truth. **Fix it by shortening sentences and dropping jargon, not by deleting the precision in `Risk`.** A vague risk line is worse than a hard-to-read one.

### Contract 4 - Creative brief

**The default output is a real Google Doc, created through the Docs API, not markdown pasted into chat.** Markdown or Notion only when the requester explicitly asks for it.

| # | Rule | P1 fail = |
|---|---|---|
| 1 | Doc created via `docs_create`, then structured with `docs_formatText`. Handoff includes the Doc URL. | Requester has to build the document |
| 2 | **Heading 1** for the brief title. **Heading 2** per concept or job. **Heading 3** for `Do not`, the deadline, and any hard rule, so it separates visually. | Hard rules buried in a paragraph |
| 3 | Field labels bold: Format, Overlay, CTA, Must show, Do not, Deadline. The overlay line itself is bold, because it gets burned into the artwork. | Designer guesses what is locked |
| 4 | **No markdown artifacts in the Doc body**: no `###`, no `**`, no pipe tables. Use Docs headings and Docs tables. | Hash symbols in a client-adjacent document |
| 5 | One blank paragraph between blocks. One concept scannable in one screen. | Wall of text with nicer fonts |
| 6 | A **plain-text fallback block in chat** alongside the link, so the brief survives a permissions or folder problem. | Broken link means no brief |

**Highlight colour is not available.** The Docs tooling here does bold, italic, underline and headings only. Do not promise a highlight and do not fake one with brackets or caps. Heading 3 plus bold is the approved emphasis, decided 2026-09-08.

**Images cannot be embedded** either. Visual references ship as **annotated links** - every link says what to take and what to ignore. That still satisfies `creative-brief`'s rule that references are attached rather than described, but only if the link actually resolves. Check it.

---

## Step 3 - Write it

### Structure

- **Answer first.** Paragraph one states the conclusion or the number. Reasoning follows. Never build to a reveal.
- **One idea per paragraph.** Three sentences is a good paragraph. Six is usually two paragraphs.
- **Headings are claims, not labels.** "Spend is up 40% on one campaign" beats "Performance Overview."
- **Every number carries its date range and source.** `$4,210 spend · Aug 1-21 · Google Ads UI` - not `about $4.2k`.
- **Recommendations are specific and assigned.** "Pause ad set 3 and shift budget to ad set 1" beats "consider optimizing underperformers."
- **Say what you don't know.** A named gap builds more trust than a smoothed-over one.

### The AI-slop ban list

These patterns get a deliverable sent back. They are the tells that a document was generated rather than written.

**Banned openers and connectives**
- "In today's fast-paced digital landscape"
- "It's important to note that" / "It's worth noting"
- "Let's dive in" / "Let's take a look at"
- "In conclusion" / "To sum up" as a section
- "Whether you're X or Y, ..."

**Banned constructions**
- The "not just X, but Y" frame, in any variant
- Triads used for rhythm rather than meaning ("clear, concise, and compelling")
- Rhetorical questions used as headings
- Em-dash-heavy sentences stacked back to back
- Restating the heading as the first sentence under it
- A closing paragraph that summarizes what the reader just read

**Banned padding**
- Any sentence that would not change the reader's decision if deleted
- Adjectives with no measurement behind them: robust, powerful, seamless, cutting-edge, game-changing, comprehensive, holistic
- Hedges stacked on hedges: "may potentially help to somewhat improve"
- Explaining what a standard metric is to someone who buys media for a living

**Banned formatting habits**
- **Emoji, anywhere.** As bullets, as section markers, in headings, in body text, in ad copy. One exemption only, below.

> **The one emoji exemption: the monthly report flag key.**
>
> The green / amber / red circles in the Moves Log and Deep Dive of `golden/monthly-report.md` are permitted, and they are the *only* permitted emoji in any UNI output. They encode decision quality across every account and every buyer, which is what makes the quarterly cross-brand pull possible. Nothing else earns it.
>
> This exemption does not generalise. "It has a legend, so it is data" is not an argument for a new emoji anywhere else - if you think one is warranted, it goes to Sean, not into a document.
>
> Plain glyphs are not emoji and are unaffected: the verdict marks in the performance table, arrows, bullets, box-drawing. Use them freely where they carry meaning.
- Bold applied to whole sentences
- Bullet lists where a table is clearly right
- More than two levels of nesting

**The deletion test:** read the draft and cut every sentence that does not change a decision. If the document still says everything it said before, it was correct to cut.

### Tone

Plain, confident, no theater. We are not impressed with ourselves and we do not perform enthusiasm. Bad news is stated as directly as good news - the reader finds out from us before they find it in the account.

---

## Step 4 - Gate it before sending

Run this checklist silently. Fix P1 items yourself. Report P2 items to the requester.

| # | Check | P1 fail = |
|---|---|---|
| 0 | **Zero em dashes or en dashes in the document** | A single `-` or `-` anywhere |
| 1 | Conclusion is in the first paragraph | Reader has to hunt for the point |
| 2 | Every figure has a date range and a source | An unsourced number is in the document |
| 3 | Format is one of the three permitted | It's a deck, a PDF, or something invented |
| 4 | No pricing, fees, or commercial terms anywhere | Any fee, rate, or retainer figure appears |
| 5 | Slop scan against the ban list above | Any banned pattern survives |
| 6 | Deletion test applied | A sentence remains that changes no decision |
| 7 | Every recommendation names the action and the object | "Optimize underperformers" style vagueness |
| 8 | Client name, dates, and currency are correct throughout | A stale client name or wrong currency |
| 9 | Notion: blank line around every heading, table and list | Unreadable wall of blocks |
| 10 | Paid-media deliverable: `lint-ads-output.py` ran and exited 0, and the pass line is in the handoff | Contract in Step 2b unchecked, or "checked" claimed without an exit code |

If a P1 fails, fix and re-run. Only then deliver.

### Golden samples

`references/golden/` holds one approved example per deliverable type:

| File | Deliverable |
|---|---|
| `proposal-audit.md` | PPC audit and proposal |
| `analytics-audit.md` | Analytics and tracking audit |
| `creative-brief.md` | Creative brief, full batch and short form |
| `weekly-report.md` | Weekly portfolio roll-up, one line per client |
| `monthly-report.md` | Monthly per-brand performance review |
| `text-message-update.md` | Team communication, Slack and ClickUp |
 **When one exists for the format you're producing, match it.** A sample outranks any prose rule above it - that is the point of having them.

If no sample exists yet for this deliverable type, say so in the handoff so the gap is visible.

For a second pair of eyes on someone else's draft, use **uni-output-qa** instead - it reviews and coaches rather than rewrites.

---

## Self-Improvement

At the end of every run, before ending:
1. Did any step fail or need a workaround?
2. Did the user correct or reject anything meaningful?
3. Did you discover something a future run might need?

Only propose a change if it meaningfully improves the skill. Propose it as a diff for a pull request against `seant15/uni-team-skill` - never edit the installed copy, and never treat your own proposal as approved.

---
name: meta-ad-copy
description: Write Meta (Facebook/Instagram) ad copy - primary text, headlines, descriptions - inside the official character limits and in the client's brand register. Use for any request to write, rewrite, refresh, or expand Facebook or Instagram ad copy, to fix fatigued creative, or to produce text-overlay lines for a static or video ad. Interviews for brand tone and the elevated-vs-sales register before writing, and validates every line against the locked character reference.
---

# Meta ad copy

Two things break Meta copy: writing past the truncation point, and writing in a register the brand would never use. This skill handles both before it writes a word.

**Read `references/meta-text-limits.md` before producing any copy.** Do not recall limits from memory - they change and the file is the record. Every number in it is tagged `[HARD-OFFICIAL]`, `[SOFT-OFFICIAL]`, or `[UNVERIFIED]`; never present an unverified number to a client as fact.

---

## Step 1 - Retrieve, assume, then ask once

Do not write from "we need Meta copy for client X." Equally: **do not open with six questions.** The buyer has most of the answers sitting in files you can read, and a toll gate in front of the copy is the fastest way to make him write it himself.

**Order of operations, and it is not negotiable:**

1. **Retrieve first.** Read the product or collection page, the brand kit, the reviews, the last brief for this client, the ClickUp history. Most of the list below is already written down somewhere.
2. **Assume out loud.** State what you found in the `BRIEF LOCK`, with everything inferred on the `Assuming:` line. One correction is cheaper for the buyer than six answers.
3. **Then ask, once, only for what retrieval could not settle and that would change the copy.** Numbered, one batch.

**Ask these four before the register dial.** They change the ad more than the 1-5 number does. Skip a line only when the brief already answers it.

1. Creative job - founder talking about why they started, or a product demo.
2. Scope - the whole line, or one named product.
3. Reader - first-time cold, or someone who already knows the brand.
4. Paste target - how many Primary text slots, how many Headline slots, and the customer-facing offer for the Description row.

Mark every line as retrieved or assumed, and say where a retrieved value came from. **Never fill a gap with a plausible value** - an invented offer or an invented figure is a worse failure than a question. The full rule is in `uni-standards:uni-output` under *The interview gate*.


### Brand - required

1. **What does the brand actually sell**, in one sentence, in their words not ours
2. **Brand tone** - ask for **one existing ad or page they consider on-brand**. One real example beats three adjectives.
3. **Words the brand owns, and words the brand bans.** Most clients have both and rarely volunteer them.
4. **Claims we are allowed to make** - any figure, guarantee, or superlative that has been cleared. If it isn't cleared, it doesn't go in the ad.

### The register dial - required, and it is decisive

This is the question that most changes the output, and briefs almost never contain it. **If it is not in the original context, ask.** Do not average the two and produce something with no point of view.

| | **Elevated** | **Sales** |
|---|---|---|
| Opening | Statement or observation | Problem or offer |
| Urgency | Absent | Explicit |
| Price/discount | Never in the copy | Often the hook |
| Sentence shape | Short, declarative, confident | Direct address, "you", questions |
| CTA | `LEARN_MORE`, `SHOP_NOW` | `GET_OFFER`, `SHOP_NOW`, `SIGN_UP` |
| Risk | Reads soft, converts slower, protects brand | Converts faster, erodes brand if overused |

Ask the requester to place it: **1 = pure brand, 5 = pure direct response.** Get a number. Then ask whether it's the same for retargeting - it usually is not; cold traffic often sits at 2-3 and retargeting at 4-5.

### Campaign context - required

5. **Objective and optimization goal** - determines which CTAs are even available
6. **Placements** - Feed, Stories, Reels, or all. Character recommendations differ sharply.
7. **Funnel stage** - cold, warm, retargeting
7b. **Awareness level** - unaware / problem-aware / solution-aware / product-aware. This decides where the copy has to start. Product-aware traffic does not need the problem explained to it, and unaware traffic will not read an offer.
8. **What already ran and how it did** - if this is a refresh, the losing copy is the most useful input in the brief
9. **Voice of customer** - reviews, support tickets, sales call notes, comments on past ads. Ask for the file or the link. The strongest lines in an ad are usually already written by a customer; we are transcribing, not inventing.

### Offer, features, benefits - copy cannot be written without these three

This is where thin ads come from. A variant with no offer and no specific feature has nothing to say, so it says "boutique quality at affordable prices" five different ways and the buyer correctly calls it generic.

| | What it is | Where to retrieve it |
|---|---|---|
| **Offer** | What the click actually gets, in this campaign, right now. A discount, a shipping threshold, a bundle, a free trial, a deadline. Plus where it lands. | Site banner, cart page, brand kit, the last campaign brief. Reconcile conflicts - a banner saying free shipping over $100 and a footer saying all orders is a stop-and-ask. |
| **Features** | What the product concretely has. Fabric, mechanism, dimensions, ingredients, warranty, what is in the box. | Product page, spec table, PDP bullets |
| **Benefits** | What each feature does for this reader, in their words | Reviews and support tickets. Benefits invented in-house read as invented. |

**Go and find them before asking.** Read the collection page and the reviews. If after retrieval you still have no offer, no specific feature, or no benefit traceable to a customer's own words, **stop and say which of the three is missing.** Do not write a fourth generic variant to fill the gap.

**Stop and ask** if: no cleared claims exist but the brief implies a performance promise; the offer and the landing page disagree; or the client is in a Special Ad Category (Housing, Employment, Credit, Social/Political) - that constrains both targeting and claims.

**Unless the buyer already said not to ask.** Then `uni-standards:uni-output` -> *The interview gate* -> *The one exception* applies: proceed on the value that matches the brief on file, and open the deliverable with an `ASSUMPTIONS - confirm before this goes to the client` block naming the conflict and which side you took. A shipping banner that disagrees with a footer is a line in that block, not a reason to hand back nothing.

---

## Step 2 - Write

### Block structure - the rule the buyer sends copy back over

Copy that arrives as one dense paragraph gets reformatted by hand before it can go into Ads Manager, which costs more than writing it from scratch. **Formatting is the deliverable, not a garnish.**

The full contract, including the file shape the lint reads, is `uni-standards:uni-output` -> *The paid-media output contract* -> Contract 1. The shape:

```
New arrivals just landed.

Boutique quality your mini will actually want to wear, priced like it isn't. Shop the new collection.
```

- **Block 1 is the opening. One or two sentences. Always alone, always followed by a blank line.** A short ad may open on one short line. A belief ad or a story opens wide enough to wrap to about two or three lines.
- **Block 2 carries at most two sentences and may include the CTA.** That is the default shape.
- **If the body needs two sentences of its own, the CTA moves to a third block.** Short copy stops at three blocks.
- **Long copy: no paragraph over three sentences.** Bullet and feature blocks are exempt.
- **Long copy closes on the CTA and nothing else**, one or two sentences, and it has to be strong. An ad that ends on a feature has no ask.

### Where the fold lands

The cut behind "See more" is driven by rendered lines, not by a character count, so a blank line costs a whole line of the visible budget. Feed usually folds around 125 characters and a small screen with accessibility text sizing can fold by 80.

**40 is the Reels and Stories target.** Feed may run past 40. The opening still has to land inside about 125 characters, where a normal phone folds. If the first block does not work as the entire ad, the copy is not finished.

The block structure can therefore push the CTA below the fold in Feed. **That is accepted** - the person who taps "See more" is the person with intent. Two things follow: do not collapse the blocks to win the fold, and never present the block structure to a client as a performance rule. There is no public test data behind it. It is a readability and paste-ability rule, and that is enough.

### The length test - always run both

UNI does not pick a length. **We test short against long, every time**, because which one wins is a property of the brand and the audience, not something anyone can call in advance.

**Short - 2 to 3 sentences, elevated.**
No bullets. No stacked benefits. It reads like a statement someone confident made, not like a page of selling. Works when the product is visually self-explanatory, the brand carries weight, or the audience is product-aware and does not need convincing, only reminding. Short copy sits most naturally at register 1 to 2.

> Fifteen years of pro-style ranges. Now in a showroom you can actually walk into.
> Paramus, open weekends.

**Long - feature and benefit structure, or AIDA.**
Bullets or a short structured block. Works when the product needs explaining, when there are multiple objections to clear, or when the audience is problem-aware and has to be walked to the solution. Long copy sits most naturally at register 4 to 5.

**Those affinities are not permission to drift off the register the client gave you.** If the answer was 3, all five variants are register 3 - the length test holds register constant so that length is the only variable. A file with short at 2 and long at 4 tests two things at once and reads as neither. Where the natural affinity pulls against the client's number, the number wins and you say in the handoff that it did.

Two structures to pick from, and say which one you used:

| | |
|---|---|
| **Feature and benefit** | Hook. Then 3-4 lines, each pairing one concrete feature with the thing it does for the reader. Then the CTA. Every bullet earns its line or it gets cut. |
| **AIDA** | Attention (the hook, inside 40 characters) → Interest (the specific mechanism or fact that makes it credible) → Desire (the outcome in their life, in their words) → Action (one CTA, no stacking). |

**Deliver both lengths when the sheet has room for both.** Label each primary. Tell the buyer to run different lengths as separate ads, not as one ad with mixed lengths, or the test reads nothing. The kit below decides how many, not a fixed five.

The fold applies to both. A long ad still has to earn the "See more" click.

**Reels and Stories deliver short only.** Meta's own recommendation for Reels primary text is around 40 characters; long copy there is thrown away. Long copy is a Feed asset. If the brief says all placements, deliver short for Reels and Stories and long for Feed, labelled per placement - do not hand over one length and let the buyer sort it out.

**Default split when the brief names Feed plus a vertical placement:** two short on the vertical placement, one short on Feed, two long on Feed. That keeps three short against two long for the length test while giving each placement something it can actually run. Deviate when the media plan says to, and say why.

**No emoji in the body or in bullets.** A single trailing pointer on the belief ad's CTA is legal when the source ads already use one. Stories and the short ad do not get it. Any other emoji needs the buyer to ask in this request, and the lint runs with `--allow-emoji`.

### Volume and grading

**Deliver the sheet's slots, and never more than five.** Five is the API ceiling, not a quota. Do not pad a 3-slot sheet to five. **Do not generate a large pool and shortlist it.** If a variant cannot clear the bar below, rewrite that variant.

Every primary clears all five of these:

1. On Reels and Stories the opening carries the specific thing inside **40 characters**. On Feed it wraps to about two or three lines and still lands inside **~125**
2. There is a specific, verifiable thing in it - a number, a name, a mechanism. Vague ads lose.
3. It matches the register number the client gave
4. The brand would actually say this sentence out loud
5. It differs from the other four in **angle**, not wording. Five rewordings of one idea is one ad, not five.

### The three-seat check

Before a variant survives, it has to clear three lenses. This is the `writing-room` method, applied to paid:

1. **Attention** - do the first three words interrupt a scroll? Pattern interrupt beats clickbait; a specific number beats a vague claim.
2. **Relatability** - does it sound like a person, one clear emotion, conversational rather than presentational?
3. **Conversion** - does it survive a skeptic? Peer-to-peer credibility, no vendor jargon, proof before hype.

A variant that only passes one of the three is a draft, not a candidate.

**No fabrication, ever.** Statistics, testimonials, guarantees and superlatives come from the cleared-claims list or the VOC file. If it is not in one of those two places, it does not go in the ad. This is a hard rule inherited from `copywriting` and `conversion-copywriting`.

Do not show the discarded fifteen unless asked. Do show the **angle** each surviving variant takes, in three words, so the buyer can pick by strategy rather than by vibe.

### The kit, locked 2026-10-05

This wins over the old quota of five one-line variants, and over writing a SKU spec when the creative is a belief video.

**What you deliver**

- One short primary. Two or three sentences. No bullets. The first sentence can be one short line.
- One belief primary. Keep their belief opening when the sheet already has one. Then plain bullets, one short proof line, then the CTA.
- One or two story primaries. A real user's words, then what wearing it feels like, then at most one benefit sentence. Size and the free exchange show up in one story, not in every primary.
- Headlines match the sheet. Three is normal. A cell is one headline even when it contains a comma. `What You Wear Is a Supplement, Add To The Work` is one asset. Do not split it.
- One description. The offer, in words a stranger can read. Do not invent a coupon code. Do not replace the offer line Sean wrote with a disclaimer.

**Refresh**

Start from the copy already in the sheet. Keep a belief opening that is already their voice. Cut `we sell it`, `you buy it`, and any line that says the garment does what a supplement promises. `So we built` can stay. Do not replace their opening with a new metaphor.

**Whole line vs one product**

A whole-line ad may name the category, the cut, and a number that is on the site. It does not name a SKU, a fabric weight, a price, or a color unless the brief names that product. When a quote's "it" is a SKU on the page, keep the sentence and do not insert the product name into the quote.

**Testimonials**

`Name, fact, place: "exact words."`

A second sentence from the same person is the next paragraph, in quotes, without repeating the name. After the quote, say what wearing it feels like, then turn it to you. Do not mention the webpage, the layout, or where the quote sits on the page.

**Length**

A story paragraph is at most three sentences. One longer sentence is enough when it already reads as two or three lines. Do not add sentences to hit a count. Long copy on a standard primary is not trimmed to 1,024 characters. That cap is only an `asset_feed_spec` body. See `references/meta-text-limits.md`.

**Paste shape**

The buyer edits a sheet. Lead the handoff with Primary text, Headline, and Description, in that order. The `=== VARIANT ===` file is what the lint reads. Do not call a headline a title.

### Text overlay

When the ad needs a text overlay on the image or video, treat it as a separate deliverable from primary text - it is read in under a second at thumbnail size.

- **3-6 words.** If it needs 8, the idea is not sharp yet.
- Legible at thumbnail. No sentence-case paragraphs on an image.
- **Never repeat the headline verbatim.** The overlay stops the scroll; the headline closes.
- Overlay and primary text should carry **different** halves of the message, not the same half twice.

If the request came through `creative-brief`, the overlay lines belong back in that brief, not delivered standalone.

### Structure of the deliverable

**Write the primaries to a file in this exact shape, then lint the file.** One block per primary. The delimiters are what make it machine-checkable; do not reword them.

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

`Description` is `-` unless the placement shows one. **Count characters, do not estimate them** - the lint recomputes both numbers and fails the variant if they are off by more than one.

---

## Step 3 - Validate before delivering

**Run the gate first. It is a script, and it can refuse.**

```
python skills/uni-output/scripts/lint-ads-output.py <file> --type meta-copy
```

Exit 1 means not deliverable. Fix every P1, re-run, and put the result line in the handoff:

```
Lint: meta-copy 5/5 pass (P1=0, P2=1)
```

**Do not report "checked" without an exit code.** The lint covers block structure, hook budget, paragraph sentence counts, CTA isolation, placement-length match, emoji, character-count honesty and dashes. Everything below is what a script cannot judge.

| Check | Fail = |
|---|---|
| Every field counted against `references/meta-text-limits.md` | A field over a `[HARD-OFFICIAL]` limit |
| Offer, features and benefits are all present and retrieved, not invented | A generic ad with nothing to say |
| ≤5 primary texts, ≤5 headlines, ≤5 descriptions | Over the API asset cap |
| CTA exists for this objective in Ads Manager | Promised a button that isn't in the dropdown |
| Every claim is on the cleared list | An unapproved performance or superlative claim |
| Register matches the number the client gave | Elevated brand handed sales copy, or vice versa |
| Each primary is a different job in the kit, not a rewording of the same one | Delivered one ad several times |
| A short and a long, when the sheet has room for both | No length test, so the test reads nothing |
| Every claim traceable to cleared list or VOC file | Fabricated proof |
| Zero em dashes or en dashes | House typography rule broken |
| No banned brand words | - |
| Special Ad Category rules respected if applicable | Restricted claim or targeting implication |

Then run **uni-output** on the deliverable before it leaves.

---

## Self-Improvement

At the end of every run, before ending:
1. Did any step fail or need a workaround?
2. Did the user correct or reject anything meaningful?
3. Did you discover something a future run might need?

Character limits change without announcement. If a limit in `references/meta-text-limits.md` proved wrong in Ads Manager, that is a P1 fix - propose the corrected row with today's date. Only propose a change if it meaningfully improves the skill, and propose it as a diff for a pull request against `seant15/uni-team-skill` - never edit the installed copy.

---
name: google-ad-copy
description: Write Google Ads text assets - headlines, descriptions, long headlines, sitelinks, callouts - to the exact character limits and asset counts of the specific campaign type. Use for any request to write, rewrite, expand or fix Google Ads copy for Search/RSA, Performance Max, Demand Gen, Display, or App campaigns, and when Ad Strength is Poor or a build was rejected on editorial policy. Interviews for campaign type and brand register first, because the limits and templates differ per type.
---

# Google Ads copy

Google copy fails for a different reason than Meta copy. On Meta the risk is truncation. On Google the risk is **writing to the wrong campaign type's spec** - a Demand Gen headline is 40 characters, an RSA headline is 30, and PMax needs at least one headline under 15. Copy written to the wrong spec gets silently rejected or silently downgraded.

**Read `references/google-text-limits.md` before producing any copy.** Do not recall limits from memory.

---

## Step 1 - Interview

**Interview gate.** Ask everything below in one batch, skip what is supplied, then lock the brief before producing. Never fill a gap with a plausible value. The full rule is in `uni-standards:uni-output` under *The interview gate*.

### Campaign type - required, and it is the first question

Nothing else can be answered before this. **Never write generic "Google ad copy."**

| Type | Headline | Description | The trap |
|---|---|---|---|
| **Search / RSA** | 30 × up to 15 (min 3) | 90 × up to 4 (min 2) | Pinning kills combinatorics |
| **Performance Max** | 30 × 3-15, **≥1 must be ≤15** | 90 × 2-5, plus long headline 90 × 1-5 | The old 60-char short description no longer exists |
| **Demand Gen** | 40 × 1-5, **≥1 must be ≤30** | 90 × 1-5 | Without a ≤30 headline it cannot serve on Display |
| **Display / RDA** | short 30 × 1-5, long 90 × 1 | 90 × 1-5 | Long headline is a single asset, not a set |
| **App** | 30 × 1-5 | 90 × 1-5 | Copy is not auto-translated |

Every type except Search also requires a **business name at 25 characters** - and in PMax it must match the domain or verified legal entity exactly, with no promotional wording.

### Brand - required

1. **What the brand sells**, in one sentence, in their words
2. **One existing ad or landing page they consider on-brand**
3. **Words owned and words banned**
4. **Cleared claims** - figures, guarantees, superlatives that have been approved. Uncleared claims do not go in the ad.

### The register dial - required, ask if not in the brief

**1 = pure brand, 5 = pure direct response.** Get a number.

On Google the register shows up differently than on Meta: at 1-2, headlines are category and capability statements; at 4-5 they are offer, price framing, and urgency. The same 30 characters, aimed completely differently. Do not average.

### Campaign context - required

5. **Keywords and match types** (Search) or **audience signals** (PMax/Demand Gen)
6. **Landing page URL** - read it. Copy that promises something the page doesn't deliver is a Quality Score problem, not a copy problem.
7. **Existing Ad Strength** and what Google's action items say
8. **Compliance text** that legally must appear in every ad - this is the only justification for pinning
9. **Language** - double-byte languages count 1 character as 2 across every field

**Stop and ask** if: the landing page contradicts the offer; there are no cleared claims but the brief implies a performance promise; or the vertical is regulated (finance, health, legal) - Google's restricted-category rules constrain the copy.

---

## Step 2 - Write to the type

### Responsive Search Ads

**Fill all 15 headlines and all 4 descriptions.** Asset volume is an official Ad Strength input.

Cover these angles across the 15 - one angle per headline, no repeats:

1. Exact keyword match (the keyword must fit **entirely inside one headline**, or it does not count toward relevance)
2. Keyword variant / close paraphrase
3. Primary benefit
4. Secondary benefit
5. Differentiator vs the category
6. Proof - number, years, volume, rating
7. Offer or incentive
8. Objection handled
9. Audience call-out
10. Urgency or timing
11. Brand name
12. Location, if local
13. Process - how it works, in 30 characters
14. Guarantee or risk reversal
15. Direct CTA

Descriptions (4 × 90): benefit expansion · proof and credibility · offer plus CTA · objection handled. Long-tail keywords that exceed 30 characters belong here, not in a headline.

**Pinning:** default to none. If a disclaimer legally must appear, pin to Headline 1, Headline 2, or Description 1 - Headline 3 and Description 2 are not guaranteed to show. Pin **several distinct assets** to that position, never one.

### Performance Max

- 11+ headlines at 30, **at least one at 15 or under** - write 2-3 short ones deliberately, don't hope one comes in short
- 2+ long headlines at 90 - these read as sentences, not headline fragments
- 4+ descriptions at 90
- Business name at 25, exact match to domain or legal entity

### Demand Gen

- 5 headlines at 40, **at least one at 30 or under.** Verify this before delivering - without it, Ad Strength is Incomplete and the campaign cannot serve on Display.
- 3+ descriptions at 90
- Business name at 25

### Display / RDA

- 5 short headlines at 30, one long headline at 90, 5 descriptions at 90, business name at 25
- The long headline appears alone in some placements - it must work as a standalone ad

### Assets / extensions

Sitelinks 25 chars, descriptions 35 × 2 **as a pair** - write both or neither. **No two sitelinks may share link text**, even with different URLs. Callouts 25 chars, aim for 8-10. Structured snippets: 3-10 values at 25 chars from the 13 fixed headers, **no promotional words** ("Sale", "Free shipping" are rejected).

Ad Strength now scores **6+ sitelinks** across account, campaign and ad group combined.

---

## Step 3 - Editorial policy pass

Google rejects on these. Check before delivering.

- No excessive caps - `SALE`, `FrEe`, `S.A.L.E`. Abbreviations, promo codes and brand names are the exceptions.
- No repeated punctuation (`Now!!`), no symbol-for-letter (`f1owers`, `fr@e`), **no emoji**
- **No gimmicky repetition - including across other assets in the same ad group.** This is why 15 headlines must be 15 ideas, not 15 rewordings of three.
- No missing or excessive spacing
- Sitelinks: no duplicate link text, no attention-grabbing punctuation
- Structured snippets: no repeated values, no promotional language

---

## Step 4 - Validate before delivering

| Check | Fail = |
|---|---|
| Every asset counted against the **campaign type's** row in the reference | One field written to the wrong type's spec |
| PMax: ≥1 headline ≤15 chars | Asset group incomplete |
| Demand Gen: ≥1 headline ≤30 chars | Cannot serve on Display |
| RSA: 15 headlines, 4 descriptions filled | Ad Strength penalty on asset volume |
| Each headline is a distinct angle | Editorial repetition violation |
| Target keyword fits entirely inside one headline | Relevance signal not counted |
| Pinning restrained and justified | Ad Strength penalty for no reason |
| Business name 25 chars, exact match (non-Search) | Rejection |
| Editorial pass clean | Rejection |
| Every claim on the cleared list | Unapproved claim |
| Copy matches the landing page | Quality Score problem |

**Print the character count next to every asset.** Do not estimate.

Then run **uni-output** on the deliverable before it leaves.

### One thing to tell the client correctly

Ad Strength is **not** used to calculate Ad Rank, Quality Score, or auction wins, and does not determine whether an ad can serve - Google states this outright. It measures asset diversity and combination coverage. Do not present it to a client as a ranking factor.

---

## Self-Improvement

At the end of every run, before ending:
1. Did any step fail or need a workaround?
2. Did the user correct or reject anything meaningful?
3. Did you discover something a future run might need?

If a limit in `references/google-text-limits.md` proved wrong in the Google Ads UI, that is a P1 fix - propose the corrected row with today's date. Only propose a change if it meaningfully improves the skill, and propose it as a diff for a pull request against `seant15/uni-team-skill` - never edit the installed copy.

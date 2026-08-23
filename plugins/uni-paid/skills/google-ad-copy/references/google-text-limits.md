# Google Ads text limits - locked reference

**Verified 2026-08-23 against support.google.com and developers.google.com.** Re-verify every 6 months.

All limits are **hard** unless marked otherwise - Google's UI blocks you at the counter. Double-byte languages (Chinese, Japanese, Korean) count **1 character as 2** across every field.

---

## Responsive Search Ads - Search campaigns

| Asset | Chars | Count |
|---|---|---|
| Headline | **30** | min 3, max 15 |
| Description | **90** | min 2, max 4 |
| Display path | **15** each | 2 fields |
| Final URL | 2,048 | 1 |

⚠️ **Doc conflict:** the RSA help page states the UI minimum as 3 headlines / 2 descriptions; the specs table states 1-15 / 1-4 (the API floor). **Write to 3/2 as the floor.**

### Pinning

Pinnable positions: Headline 1, 2, 3 · Description 1, 2.

- Text that must appear in **every** ad (legal disclaimers) must be pinned to **Headline 1, Headline 2, or Description 1**. Headline 3 and Description 2 are not guaranteed to show.
- Google's own words: *"pinning isn't recommended for most advertisers and can affect ad strength."*
- If compliance forces a pin, pin **multiple non-duplicate assets to the same position** rather than one - a single pinned asset caps the combinatorics hardest.

### Search "Ad assets" block (not RSA - do not conflate)

The Search specs page also lists a separate assets block: Headlines **25 chars**, 1-20 (4 recommended); Descriptions 90 chars, 1-5; Business name 25 chars ×1 required; Logo 1:1 required; Square 1:1 image 1-20 required. Google does not name which format this belongs to. **Never apply the 25-char headline to an RSA.**

---

## Performance Max - asset groups

| Asset | Chars | Count | Recommended |
|---|---|---|---|
| Headline | **30** - and **at least one must be ≤15** | min 3, max 15 | 11+ |
| Long headline | **90** | min 1, max 5 | 2+ |
| Description | **90** | min 2, max 5 | 4+ |
| Business name | **25** | 1, required | - |
| Display path | 15 each | 1-2 | 2 |

- **Business name must exactly match the domain or verified legal entity.** No promo copy, no extra symbols.
- ⚠️ **Changed:** the old required **60-character short description no longer exists.** Descriptions are 90 characters, minimum 2. Anything in an old template using a 60-char field is stale - fix it.
- Assets: Horizontal 1.91:1 and Square 1:1 recommended 4+ each (max 20), Vertical 4:5 2+ (max 20), Logo 1:1 required 1 (max 5). Video: one per orientation recommended, ≥10s, max 15 - Google auto-generates video if none supplied.
- With Brand Guidelines on, business name and logo bind at **campaign** level, not asset-group level.
- 1-100 asset groups per campaign. Asset groups cannot be shared across campaigns.

---

## Demand Gen

| Asset | Chars | Count | Recommended |
|---|---|---|---|
| Headline | **40** - but **at least one must be ≤30** | 1-5 | 5 |
| Description | **90** | 1-5 | 3 |
| Business name | **25** | 1, required | - |
| Final URL | 2,048 | 1, required | - |

⚠️ **The ≤30 rule is load-bearing.** Without one headline at 30 or under, Ad Strength reads "Incomplete" and the campaign **cannot serve on Display.** This is the single most common Demand Gen build error.

Images: Horizontal 1.91:1 required 1-20 (3 rec) · Square 1:1 1-20 (3 rec) · Logo 1:1 1-5, min 144×144 · Vertical 4:5 optional. Video 10-60s.

---

## Display / Responsive Display Ads

| Asset | Chars | Count |
|---|---|---|
| Short headline | **30** | 1-5, required |
| Long headline | **90** | 1, required |
| Description | **90** | 1-5, required |
| Business name | **25** | 1, required |

Images: Horizontal 1.91:1 1-15 (5 rec, min 600×314) · Square 1:1 1-15 (5 rec, min 300×300) · Logo 1:1 1-5 (min 128×128) · Logo 4:1 1-5 (min 512×128). Video 16:9 / 1:1 / 2:3, 1-5 each, ~30s preferred.

---

## App campaigns

Headline **30** chars, 1-5 (5 rec, required) · Description **90** chars, 1-5 (5 rec, required). Images max 20, video max 20 (10-60s).

**Copy is not auto-translated.** Language targeting must match the language the copy is written in.

---

## Assets / extensions

| Asset | Chars | Count |
|---|---|---|
| Sitelink text | **25** (double-byte 12) | show: 6 desktop / 8 mobile; min 2 to display; 4 on Video & Demand Gen |
| Sitelink description 1 & 2 | **35** each, **must be filled as a pair** | - |
| Callout | **25** (double-byte 12) | up to 10 shown per ad |
| Structured snippet values | **25** each | 3-10 values; 13 fixed header options |
| Price header / description | **25** each | 3-8 offerings (5+ rec) |
| Promotion | **Google publishes no character limit** - verify live | - |

Recommended sitelink volume: 4+ at account level, 6+ on high-traffic ad groups. Ad scheduling: max 6 windows/day, 42 total.

⚠️ Promotion assets with an **occasion** must be created or edited **within 6 months of the start date** to be eligible to serve. 34 occasions available.

---

## Editorial policy - what it forbids in copy

Source: [Editorial policy](https://support.google.com/adspolicy/answer/6021546)

- **Capitalization** - no excessive or gimmicky caps: `FLOWERS`, `FlOwErS`, `F.L.O.W.E.R.S`. Allowed exceptions: common abbreviations (ASAP), promo codes, trademarked/brand names.
- **Punctuation & symbols** - no repeated punctuation (`flowers!!`), no symbol-for-letter substitution (`f1owers`, `fl@wers`), **no emoji**, no non-standard superscript. Allowed: trademark punctuation matching the landing page, star ratings (`5* hotel`), asterisks on legal disclaimers.
- **Repetition** - no gimmicky or unnecessary repetition of a name, word or phrase, **including across other assets in the same ad group.** This directly constrains how you write 15 RSA headlines: they must be substantively distinct, not 15 rewordings.
- **Spacing** - no missing or excessive spaces.
- **Spelling and grammar** - must be standard and intelligible.
- **Sitelinks** - no two sitelinks with identical link text even if the URLs differ; no attention-seeking punctuation (`!`, `►`); third-party URLs must carry the full domain in the text.
- **Structured snippets** - no repeated values within or across headers, no promotional language ("Sale", "Free shipping"), no emoticons.
- **Trademarks** - competitors may bid on brand keywords; Google does not police trademarks in keywords or display URL subdomains. Trademark use in ad text is permitted for resellers, informational sites, and ordinary descriptive use.

---

## Ad Strength - what it is and isn't

Source: [About Ad Strength](https://support.google.com/google-ads/answer/9921843)

Google's own correction of the common misconception: *"Ad Strength is a feedback tool for asset diversity and combination testing. It isn't used to calculate Ad Rank, Quality Score, or auction wins."* It also does not determine serving eligibility.

Official inputs:
1. **Asset-keyword relevance** - a keyword must fit **entirely within one headline** to count. Split across two headlines, it doesn't. Long-tail terms over 30 characters belong in a 90-character description.
2. **Asset volume** - work toward 15 headlines and 4 descriptions.
3. **Asset diversity** - no repeated words, phrases, or selling points across assets.
4. **Sitelink sufficiency** - **6+ sitelinks** across account/campaign/ad-group combined, including dynamic sitelinks, is now a scored factor.
5. **Restrained pinning** - more pinning and more duplication lowers the score.

"Incomplete" is usually caused by: missing Final URL, ad not in an ad group, or **no keywords in the ad group.**

Terminology change: *"Text customization"* is the new name for *"Automatically created assets."*

Google's cited figures (their internal data - label as such if quoted to a client): Poor → Excellent Ad Strength on RSAs + sitelinks correlates with 15% more conversions; 1→2 RSAs per ad group +6.6% conversions, 2→3 +3.7%.

---

## Not verifiable from official sources - do not invent numbers

1. Promotion asset field character limits
2. Maximum number of sitelinks / callouts / structured snippets that can be **added** (Google publishes display caps and recommendations only)
3. RSA display URL rules beyond the two 15-char paths
4. Which ad format the Search page's "25-char headline × 1-20" assets block belongs to

## Sources

[RSA](https://support.google.com/google-ads/answer/7684791) · [Search specs](https://support.google.com/google-ads/answer/17092074) · [PMax specs](https://support.google.com/google-ads/answer/17091269) · [PMax text assets](https://support.google.com/google-ads/answer/14528373) · [Demand Gen specs](https://support.google.com/google-ads/answer/17091672) · [RDA specs](https://support.google.com/google-ads/answer/17090561) · [App specs](https://support.google.com/google-ads/answer/17091671) · [Sitelinks](https://support.google.com/google-ads/answer/2375416) · [Callouts](https://support.google.com/google-ads/answer/6079510) · [Structured snippets](https://support.google.com/google-ads/answer/6280012) · [Price assets](https://support.google.com/google-ads/answer/7065415) · [Promotion assets](https://support.google.com/google-ads/answer/7367521) · [Editorial policy](https://support.google.com/adspolicy/answer/6021546) · [Capitalization](https://support.google.com/adspolicy/answer/14848295) · [Punctuation & symbols](https://support.google.com/adspolicy/answer/14847994) · [Trademarks](https://support.google.com/adspolicy/answer/6118) · [Ad Strength](https://support.google.com/google-ads/answer/9921843) · [PMax assets API](https://developers.google.com/google-ads/api/docs/performance-max/assets) · [SitelinkAsset API](https://developers.google.com/google-ads/api/reference/rpc/v22/SitelinkAsset)

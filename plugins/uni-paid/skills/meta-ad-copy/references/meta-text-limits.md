# Meta ad text limits - locked reference

**Verified 2026-08-23.** Re-verify every 6 months, or immediately if an ad is rejected or truncated unexpectedly.

Every number below is tagged. **Never present an UNVERIFIED number to a client as fact.**

- `[HARD-OFFICIAL]` - Meta's own developer docs. Exceed it and the API rejects the ad.
- `[SOFT-OFFICIAL]` - Meta's own "Text Recommendations." Exceeding it is allowed; the text gets truncated in the feed.
- `[UNVERIFIED]` - industry sources only, could not be confirmed against a Meta page.

---

## 1. Hard limits - the only officially documented maxima

Source: [Asset Feed Spec Options, Marketing API](https://developers.facebook.com/docs/marketing-api/ad-creative/asset-feed-spec/options/)

| Field | Hard max | Tag |
|---|---|---|
| Primary text (`bodies`) | **1,024 characters** | `[HARD-OFFICIAL]` |
| Headline (`titles`) | **255 characters** | `[HARD-OFFICIAL]` |
| Description (`descriptions`) | **255 characters** | `[HARD-OFFICIAL]` |

**Scope caveat:** these are documented for `asset_feed_spec` - i.e. dynamic / Advantage+ creative. Meta publishes **no** stated maximum for a plain `object_story_spec` creative. Do not tell a client "the limit is 1,024" for a standard single-image ad; say the recommended range instead.

**Numbers circulating that are wrong:** 63,206 (that is the Facebook *post* limit), 2,200 (Instagram *caption* limit), "headline hard max 40" (that is a recommendation, not a cap). Do not repeat these.

## 2. Asset counts per ad - hard, API-enforced

Same source. `[HARD-OFFICIAL]`

| Asset | Max per ad |
|---|---|
| Primary texts | 5 |
| Headlines | 5 |
| Descriptions | 5 |
| Call-to-action types | 5 |
| Link URLs | 5 |
| Images | 10 |
| Videos | 10 |
| **Total assets, all types combined** | **30** |

This supersedes older guidance about "four additional text options." Five is the number.

## 3. Recommended lengths by placement

Facebook Feed row is `[SOFT-OFFICIAL]`, confirmed against Meta's own Ads Guide. **Every other row is `[UNVERIFIED]`** - consistent across three 2026 industry sources but not confirmable against a Meta page from our environment (Meta blocks automated access to `facebook.com/business/ads-guide`).

| Placement | Primary text | Headline | Description | Tag |
|---|---|---|---|---|
| Facebook Feed | 50-150 | 27 | - | `[SOFT-OFFICIAL]` |
| Instagram Feed | 125 | 40 | - | `[UNVERIFIED]` |
| Stories (FB / IG / Messenger) | 125 | 40 | - | `[UNVERIFIED]` |
| Facebook Reels | 40 | 55 | - | `[UNVERIFIED]` |
| Instagram Reels - Awareness | 44 | 40 | - | `[UNVERIFIED]` |
| Instagram Reels - Traffic | 72 | 40 | - | `[UNVERIFIED]` |
| Ads on Reels (overlay banner) | 60 | 10 | - | `[UNVERIFIED]` |
| Marketplace | 125 | 40 | 20 or 30 (sources conflict) | `[UNVERIFIED]` |
| Facebook Search Results | 125 | 40 | 30 | `[UNVERIFIED]` |
| Facebook Right Column | - | 40 | 30 | `[UNVERIFIED]` |
| Carousel (per card) | 125 shared | 40 | 20 | `[UNVERIFIED]` |

### The one number that actually governs writing

**~125 characters is where mobile feed truncates to "See more."** Every source agrees. This is distinct from Meta's stated 50-150 recommendation for FB Feed - both are true, they measure different things.

**Working rule: the hook has to land inside the first 125 characters.** Anything after that is read only by someone already interested.

## 4. Call-to-action buttons

CTA is an enum, not free text - no character limit to manage. Full API superset pulled from Meta's own Python Business SDK, Marketing API v26.0 (`AdCreativeLinkDataCallToAction.Type`), `[HARD-OFFICIAL]`.

Commonly used in UNI accounts:
`SHOP_NOW, LEARN_MORE, SIGN_UP, BOOK_NOW, GET_QUOTE, GET_OFFER, CONTACT_US, SEND_MESSAGE, WHATSAPP_MESSAGE, APPLY_NOW, DOWNLOAD, SUBSCRIBE, ORDER_NOW, GET_DIRECTIONS, CALL_NOW, REQUEST_TIME, BOOK_A_CONSULTATION, MAKE_AN_APPOINTMENT, GET_STARTED, SEE_MENU, WATCH_MORE, PLAY_GAME, INSTALL_APP, DONATE_NOW, VIEW_PRODUCT, ADD_TO_CART, BUY_NOW, NO_BUTTON`

Newer AI-commerce values present in v26.0: `SHOP_WITH_AI`, `TRY_ON_WITH_AI`.

**Important:** the API list is a superset. **Ads Manager shows a shorter subset that depends on objective and placement.** Never promise a client a specific CTA button without confirming it appears for that objective. If it isn't in the dropdown, it isn't available.

## 5. Lead-gen instant forms

- Max custom questions: **15** `[UNVERIFIED]` - not documented by Meta.
- Character limits for intro headline, intro description, question labels, answer options, thank-you screen: **no reliable source found, official or otherwise.** Meta's spec page is bot-blocked and has no archive.

**Do not guess these.** If a lead-form build needs exact limits, check live in Ads Manager and add the confirmed number to this file with today's date.

## 6. Re-verification protocol

When re-checking:
1. Open Ads Manager, create a draft ad, and read the character counters directly. That is the ground truth for the current UI.
2. Check the [asset feed spec options page](https://developers.facebook.com/docs/marketing-api/ad-creative/asset-feed-spec/options/) for hard maxima.
3. Update the row, change its tag if it graduates from `[UNVERIFIED]` to confirmed, and note the date.
4. Open a PR. Do not edit an installed copy.

## Sources

- [Asset Feed Spec Options - Marketing API](https://developers.facebook.com/docs/marketing-api/ad-creative/asset-feed-spec/options/)
- [Ad Creative Link Data - Marketing API](https://developers.facebook.com/docs/marketing-api/reference/ad-creative-link-data/)
- [facebook-python-business-sdk, AdCreativeLinkDataCallToAction](https://github.com/facebook/facebook-python-business-sdk)
- Meta Ads Guide, Image / Facebook Feed / Awareness - [archived 2024-04-14](http://web.archive.org/web/20240414191624/https://www.facebook.com/business/ads-guide/image/facebook-feed)

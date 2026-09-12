# Meta build limits and enums

Every row carries how it was established. `[LIVE]` means observed directly in a Meta ad account
on the date shown. `[DOC]` means taken from Meta's own documentation at the URL shown.
`[UNVERIFIED]` means widely repeated but not confirmed by us against either - treat it as a
working assumption and correct it the first time production contradicts it.

## Objectives (ODAX)

`OUTCOME_SALES` · `OUTCOME_LEADS` · `OUTCOME_TRAFFIC` · `OUTCOME_ENGAGEMENT` ·
`OUTCOME_AWARENESS` · `OUTCOME_APP_PROMOTION`

`[LIVE 2026-09-11]` `OUTCOME_SALES` observed on a live sales campaign.
`[UNVERIFIED]` Legacy names (`CONVERSIONS`, `LINK_CLICKS`, `LEAD_GENERATION`) are said to be
auto-mapped. Send the ODAX name so the mapping is never in question.

Campaign objective and buying type are immutable after creation. A wrong objective means a new
campaign, not an edit. `[UNVERIFIED]`

## Optimisation goal and billing event

Meta rejects illegal combinations at row or object level. Rather than carrying a matrix that goes
stale, **export one working ad in the target objective from the account in question and copy its
values.** That is the only reliably current source.

Pairs observed working:

| Objective | Optimisation goal | Billing event | |
|---|---|---|---|
| `OUTCOME_SALES` | `OFFSITE_CONVERSIONS` | `IMPRESSIONS` | `[LIVE 2026-09-11]` |
| `OUTCOME_LEADS` (on-site form) | `LEAD_GENERATION` | `IMPRESSIONS` | `[UNVERIFIED]` |
| `OUTCOME_TRAFFIC` | `LINK_CLICKS` or `LANDING_PAGE_VIEWS` | `IMPRESSIONS` | `[UNVERIFIED]` |
| `OUTCOME_AWARENESS` | `REACH` | `IMPRESSIONS` | `[UNVERIFIED]` |

`destination_type` is objective-dependent and optional. `UNDEFINED` means "not applicable" on
combinations where Meta accepts nothing else. It is not a misconfiguration and is not worth
rebuilding an ad set over. `[LIVE 2026-09-11]` observed on `OUTCOME_SALES` + `OFFSITE_CONVERSIONS`.

## Budgets

**Integers in minor units.** USD $50.00 per day is `5000`. There is no decimal field.
`[LIVE 2026-09-11]` a campaign reading `daily_budget: "10000"` was running at $100/day.

Always read the created object back and check the number. Every budget incident traces to this line.

CBO and ABO are exclusive. When the campaign holds the budget, ad-set budget fields must be blank,
and a cloned ad set inherits no budget of its own. `[LIVE 2026-09-11]`

## Structural caps

| Cap | | |
|---|---|---|
| 50 ads per ad set | hard | `[UNVERIFIED]` |
| Roughly 3 to 6 ads per ad set actually receive delivery | behavioural, not enforced | `[UNVERIFIED]` |
| Active campaigns, ad sets and ads per account run in the low thousands | archive rather than accumulate | `[UNVERIFIED]` |
| Graph API batch: 50 operations per request | hard | `[DOC]` https://developers.facebook.com/docs/graph-api/batch-requests/ |

## Rate limiting

Marketing API rate limits scale with account spend and are enforced per app and per account.
`[DOC 2026-09-11]` https://developers.facebook.com/docs/marketing-api/overview/rate-limiting/

Campaign creation through a partner MCP may be capped more tightly than Meta's own limit.
`[UNVERIFIED]` figures around 100/hour and 300/day have been cited by one vendor.

When a write is blocked, stop and report. Retrying in a loop burns the remaining quota and can
extend the block.

## Learning phase

An ad set needs roughly **50 optimisation events per week** to exit the learning phase.
`[UNVERIFIED]` - universally cited, not confirmed by us against an official page. The number is
used as a planning gate, not as a promise to a client.

New ads receive a fresh learning allocation. Uploading unvalidated creative spends that allocation
finding out what organic could have told you for free.

## Text limits

| Field | Limit | |
|---|---|---|
| Headline | 255 characters | `[UNVERIFIED]` |
| Primary text | 2,200 characters, visually truncates near 125 | `[UNVERIFIED]` |
| Description | short, treat 30 characters as the safe display budget | `[UNVERIFIED]` |

For copy being written rather than ported, use `uni-paid`'s `meta-ad-copy` and its locked
`references/meta-text-limits.md` instead of this table. This skill ports copy; that skill writes it.

## Creative specifications

| Format | Spec | |
|---|---|---|
| Feed image | 1:1 or 4:5, at least 600x600 | `[UNVERIFIED]` |
| Stories and Reels | 9:16, at least 500x888 | `[UNVERIFIED]` |
| Video | MP4 or MOV, H.264 | `[UNVERIFIED]` |
| Carousel | 2 to 10 cards, one aspect ratio across all cards, a link per card | `[UNVERIFIED]` |

## Creative enhancements

A creative created through the API defaults to **every** Advantage+ feature opted out. Nothing is
inherited from the ad set, the campaign, or a sibling ad. A hand-built ad in Ads Manager typically
carries eight to ten features opted in. `[LIVE 2026-09-11]` both states observed in the same
campaign on the same day.

Consequence: new ads and existing ads in one campaign are not comparable on creative unless the
enhancement profile is matched deliberately. `text_optimizations` deserves its own decision because
it permits Meta to rewrite approved copy.

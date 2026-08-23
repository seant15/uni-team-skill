# Meta detailed targeting - platform reality

**Verified 2026-08-23.** This file exists because most targeting advice online is 2021 advice. Re-verify every 6 months.

---

## 1. Controls vs suggestions - the structural change

Source: [About Audience controls and Audience suggestions](https://www.facebook.com/business/help/938372127764391)

| Hard **controls** (actually constrain delivery) | Soft **suggestions** (signals only) |
|---|---|
| Location | Age |
| Minimum age | Gender |
| Language | **Detailed targeting** |
| **Custom audience exclusions** | Custom audience inclusions |

Meta, verbatim: *"Suggestions don't always constrain your audience… if you suggest the gender Women, it's possible that your ads could also deliver to men."*

### The no-opt-out list

From [Use detailed targeting](https://www.facebook.com/business/help/440167386536513), verbatim:

> *"If you optimize for Link clicks, Landing page views, Conversations, Conversion, App Events, App installs or Value, you will see Advantage+ detailed targeting automatically applied with no option to opt out."*

That covers essentially every performance goal an agency runs. On those campaigns, interest selection **cannot** be enforced.

The escape hatch - *"Further limit your audience"* / *"Further limit the reach of your ads"* with *"Use as a suggestion"* unchecked - exists for **Age, Gender and Custom audience inclusions**. Meta's Advantage+ campaign documentation does **not** list Detailed targeting among the un-checkable items, consistent with the no-opt-out sentence above.

Turning Advantage+ audience off flips the ad set to "Advantage+ off" and forfeits its optimizations. Raising minimum age or adding a custom audience exclusion does **not** cost Advantage+ status.

API: `targeting_automation.advantage_audience` = `1` / `0`. Since v23.0 new ad sets must set it explicitly or error. With it on, `age_min` is restricted to 18-25 and `age_max` is forced to 65. As of **v26.0 (2026-07-29)** the explicit requirement extends to Housing / Employment / Financial special-ad-category campaigns.

---

## 2. What has been removed

| Date | Change |
|---|---|
| **2022-01-19** | Sensitive detailed targeting options removed: health causes, race/ethnicity, sexual orientation, religious practices and groups, political beliefs and social causes. [Meta announcement](https://www.facebook.com/business/news/removing-certain-ad-targeting-options-and-expanding-our-ad-controls) |
| 2024-08, 2025-06 | Two waves of "not widely used / too granular" interest removals |
| **2024-07-29 → 2025-01-31** | **Detailed targeting EXCLUSIONS removed.** Existing ad sets ran until Jan 31 2025, then stopped. Meta's stated justification: 22.6% lower median cost per conversion without them. |
| **2025-06-23 → 2026-01-15** | **Largest consolidation wave.** In-product notice: *"Some detailed targeting options have been combined. Starting Jan 15, 2026, ad sets using the unavailable options will stop delivering."* Hit sports, food, music genres, car models and lifestyle leaves. **Meta published no list of what was removed.** Agencies found out by validating live ad sets. |

### Standing restrictions

- **Under 18:** location, age and gender only. No detailed targeting, custom audiences, lookalikes or saved audiences.
- **Special Ad Categories** (Housing, Employment, Credit/Financial, Social Issues/Elections/Politics): restricted detailed targeting lists; **no Advantage+ audience**; Advantage+ detailed targeting unavailable for social/political. Geo floor of 15 miles / 24 km, no ZIP targeting.
- **Click-to-WhatsApp ads:** detailed targeting not available at all.
- **Lookalike exclusions are not possible under Advantage+ audience.** Meta: *"exclusion constrains your audience and reduces your delivery opportunities."*

⚠️ **Stale doc warning:** Meta's Advantage+ detailed targeting help page still contains the line *"Any exclusions… continue to apply."* That language predates the exclusion removal. Do not cite it.

---

## 3. Discovery - how interests are actually found

There is no published master list and there never was one. Audience Insights was retired 2021-07-01. Meta's own targeting-search doc states: *"Not all available interests will be returned in a search"* and *"Interests may be renamed at any time, and validating by name may fail when this happens."*

**Store IDs, not names.**

### In Ads Manager (three paths, all current)

1. **AI describe-your-audience** - type sentences, phrases, keywords or hashtags, then "Find options." Avoid sensitive topics.
2. **Search bar** - original detailed targeting search. Dropdown caps at roughly 25 results, which is why many valid interests never surface here.
3. **Browse** - by Demographics / Interests / Behaviors. The taxonomy tree still exists, contrary to common belief.

### Marketing API v26.0

**Global `/search`** - no ad account required:

```
GET /v26.0/search?type=adinterest&q=baseball&limit=1000&locale=en_US
GET /v26.0/search?type=adinterestsuggestion&interest_list=["Basketball"]
GET /v26.0/search?type=adTargetingCategory&class=interests
GET /v26.0/search?type=adinterestvalid&interest_list=["Japan"]
```

Other `type` values: `adgeolocation`, `adlocale`, `adeducationschool`, `adeducationmajor`, `adworkemployer`, `adworkposition`.
`class` values: `interests`, `behaviors`, `demographics`, `life_events`, `industries`, `income`, `family_statuses`, `user_device`, `user_os`.

Response fields: `id`, `name`, `audience_size_lower_bound`, `audience_size_upper_bound`, `path` (the taxonomy breadcrumb), `description`, `topic`, `type`.
**Default `limit` is 8 - always set it explicitly.**

**Ad-account edges** - richer, needs an account:

```
GET /v26.0/act_<ID>/targetingbrowse                  # full taxonomy tree walk
GET /v26.0/act_<ID>/targetingsearch?q=harvard&limit_type=interests
GET /v26.0/act_<ID>/targetingsuggestions?targeting_list=[{'type':'interests','id':6003263791114}]
GET /v26.0/act_<ID>/targetingvalidation?targeting_list=[{'type':'interests','id':6003283735711}]
GET /v26.0/act_<ID>/delivery_estimate?targeting_spec=<json>&optimization_goal=...
```

`limit_type`: `interests`, `education_schools`, `education_majors`, `work_positions`, `work_employers`, `relationship_statuses`, `college_years`, `education_statuses`, `family_statuses`, `industries`, `life_events`, `behaviors`, `income`.

Documented quirk: without `limit_type`, results with fewer than 2,000 people are filtered into four categories only (work_employers, work_positions, education_majors, education_schools).

Permissions: `ads_read` for reads, `ads_management` for writes, `business_management` for agency-scoped accounts. Advanced Access + App Review + Business Verification required to operate on client accounts at scale. Rate limits are a rolling 1-hour window.

### The archive pattern, if UNI ever automates this

1. `targetingbrowse` walk per `limit_type` → seed set with `path` breadcrumbs
2. Recursive `targetingsuggestions` / `adinterestsuggestion` expansion from seeds
3. Store by **ID**, with breadcrumb and audience bounds
4. Scheduled `targetingvalidation` sweep to catch deprecations **before** ad sets stop delivering

This is exactly how agencies survived the January 2026 cull. A snapshot plus a validation cron is defensible. A static shipped list is not.

---

## 4. Taxonomy

Top level, verified: **Demographics · Interests · Behaviors.**

Second-level buckets below are **practitioner consensus, not Meta documentation**, and predate the 2025-26 consolidation. Use as orientation; treat `targetingbrowse` output as truth.

- **Demographics** - Education (level, field, schools, majors, college years) · Employment (industries, job titles, employers) · Relationship (status, interested in) · Financial (household income, US only) · Life events · Parental status
- **Interests** - Business & industry · Entertainment · Family & relationships · Fitness & wellness · Food & drink · Hobbies & activities · Shopping & fashion · Sports & outdoors · Technology
- **Behaviors** - Anniversary · Consumer classification · Digital activities · Expats · Mobile device user · Purchase behavior · Travel · Seasonal & events

---

## 5. Stacking, limits, minimums

**Logic** - Meta, verbatim: *"if you add 3 interests (for example, movies, books and TV), we'll look for people who match… movies, books **or** TV."* OR within a layer. **"Narrow Audience" / "Define further"** adds an AND layer. API equivalent: `flexible_spec` - OR inside each element, AND across elements. Requires `geo_locations`, `custom_audiences`, `product_audience_specs` or `dynamic_audience_ids` also present.

**Documented API limits:**

| Field | Limit |
|---|---|
| Custom audiences included | 500 |
| Custom audiences excluded | 500 |
| education_schools / majors / work_employers / work_positions | 200 each |
| user_adclusters (broad category) | 50 |
| locales | 50 · regions 200 · zips 50,000 · geo_markets 2,500 |
| **interests** | **no documented maximum** |

**Minimum audience size: not published by Meta.** The commonly repeated "1,000 minimum" and "500k-3M sweet spot" have no Meta source and should never be quoted to a client as platform rules. The only documented threshold is the 2,000-person filter on work/education categories when `limit_type` is omitted.

Audience size estimates: Meta cautions that with Advantage+ expansion the estimate *"will not reflect the total number of Meta Accounts that meet the targeting criteria."*

---

## Sources

[Use detailed targeting](https://www.facebook.com/business/help/440167386536513) · [About detailed targeting](https://www.facebook.com/business/help/182371508761821) · [Audience controls vs suggestions](https://www.facebook.com/business/help/938372127764391) · [About Advantage+ audience](https://www.facebook.com/business/help/273363992030035) · [About Advantage+ detailed targeting](https://www.facebook.com/business/help/128066880933676) · [Create a campaign using Advantage+ audience](https://www.facebook.com/business/help/793748385630490) · [Advantage+ campaign audience settings](https://www.facebook.com/business/help/25941857932125812) · [Estimated audience size](https://www.facebook.com/business/help/1665333080167380) · [Removing certain ad targeting options (2022)](https://www.facebook.com/business/news/removing-certain-ad-targeting-options-and-expanding-our-ad-controls) · [Targeting Search API](https://developers.facebook.com/docs/marketing-api/audiences/reference/targeting-search) · [Detailed Targeting API](https://developers.facebook.com/docs/marketing-api/audiences/reference/detailed-targeting/) · [Advanced Targeting API](https://developers.facebook.com/docs/marketing-api/audiences/reference/advanced-targeting) · [Advantage+ Audience API](https://developers.facebook.com/docs/marketing-api/audiences/reference/targeting-expansion/advantage-audience/) · [Graph API v26.0 release](https://developers.facebook.com/blog/post/2026/07/29/introducing-graph-api-v26-and-marketing-api-v26/) · [Brandwatch: Meta detailed targeting changes](https://social-media-management-help.brandwatch.com/en/articles/13215856-meta-changes-to-detailed-targeting-interests-in-advertise) · [Jon Loomer: Meta Ads Targeting 2026](https://www.jonloomer.com/meta-ads-targeting-2026/) · [Jon Loomer: detailed targeting exclusions removed](https://www.jonloomer.com/qvt/detailed-targeting-exclusions/) · [The Markup: removed interests corpus](https://github.com/the-markup/facebook-removed-interests)

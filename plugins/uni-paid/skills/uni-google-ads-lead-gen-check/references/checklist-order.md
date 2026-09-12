# Checklist order (locked)

Source sheet (Sheet1), retrieved 2026-09-11:
`https://docs.google.com/spreadsheets/d/1RtQdRjxyXzTMWW994jRegPbs-BHMQ6UlvF0U-H4Out8/edit`

Default lookback written on the sheet: 90 Days.

Walk sections 1-9 in this order. A TRUE/FALSE cell on the sheet is an operator checkbox, not a skip flag. Still verify.

## 1. Keyword Search Review

- Search Term Audit (add extra negative KWs)
  - add extra negative KWs to stop unrelated searches
  - add extra search terms (long tail or short)
- Identify keywords that are not performing well
  - Keywords with a high CPC compared to the account average
  - Keywords which have a high cost per conversion compared to the account average
  - Keywords with a status warning (low search volume, below first page bid, rarely shown due to low quality score)
- Review match types
  - Are there keywords which can be added as phrase or exact match
- Auction Insights Report
  - Are there new competitors or have competitors increased their spend
- Keyword status
  - Do any keywords have a 'below first page bid estimate' warning
  - Do any keywords have a 'rarely shown due to low quality score' warning
  - Do any keywords have a 'low search volume' warning

## 2. Ad Review

- Review Ads by Ad Group
  - Identify Ads with poor performance by conversion rate
  - Identify Ads with poor performance by low quality score
  - Identify Ads with poor performance by low CTR
  - Review Ad Strength: Add or update until we get a Good or Excellent score
- Complete Ad Copy Split Testing (Run Manual Tests with 2 different ads per ad group)
  - Testing the best performing headlines and descriptions and the best positions for headlines and descriptions
- Landing Page Review
  - Are different landing pages performing better in terms of conversion rate
  - check all landing pages to make sure that URLs are working and that Google Ads is not disapproving any ads due to 404s, slow page load times etc
- Ad Copy Warnings
  - check all ads to make sure that google ads has not applied any limited approvals, which could be affecting the visibility of the ad
  - have any ads been disapproved. If so, make changes and re-submit ads
- Ad Extensions Check and Recommendations
  - sitelink extensions
  - callout extensions
  - structured snippet extension
  - call extension
  - lead form extension
  - location extensions (GMB linking)
  - affiliate location extensions
  - price extension
  - promotion extension
  - image extensions

## 3. Quality Score (keywords and ads)

- Identify Keywords and Ads that have a low Quality score
- changes to ad copy to help with KW targeting and quality score
- landing page updates to help with KW targeting
- Google Analytics checks to review bounce rate and average session time

GA bounce / session time is often BLOCKED from Ads API alone. Say so. Do not invent GA numbers.

## 4. Bid Optimisation - Audience and Demographic Targeting

Search for possible bid optimisations to improve performance, under dimensions:

- Hour of the day / Day of the week
- Demographics by: age, gender, income, location
- Audiences
- Review new potential new audiences to add

## 5. Conversion Action Checks

- Are all conversion actions working
- If tracking phone calls, review the call extension report

## 6. Location Targeting

- Identify searches from non targeted location (and exclude locations)
- Review location performance and add bid optimisations (if required)

## 7. Campaign Goal Settings

Is current campaign goal still the best option

- For CPA Goal: is this higher than the current performance. (If actual CPA is lower than CPA goal the CPA goal should be reduced)
- Has your number of conversions stalled. (if no other reason can be found test another campaign goal)

Name vs field: a campaign named Max Clicks or tCPA $X is not proof of the live bidding strategy. Read `bidding_strategy_type` and the target micros.

## 8. Quality Control

- Budget pacing checks
- Payment and Account budgets

Do not query payment profiles or billing documents. Pace against daily budget vs spend only.

## 9. Recommendations Tab

- Review system generated recommendations and implement or reject

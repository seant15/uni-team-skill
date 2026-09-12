# GAQL query pack

Use the Google Ads API or an MCP that runs GAQL. Do not recall field names from memory if a query fails - drop the field and mark that leaf BLOCKED.

Date filter: `segments.date BETWEEN '{start}' AND '{end}'` with the ISO window from the skill.

Do not put customer IDs in this file.

## Identity

```
SELECT customer.id, customer.descriptive_name, customer.currency_code,
  customer.time_zone, customer.status
FROM customer
```

## Campaigns (status, serving, bids, window metrics)

```
SELECT campaign.id, campaign.name, campaign.status, campaign.serving_status,
  campaign.advertising_channel_type, campaign.bidding_strategy_type,
  campaign.maximize_conversions.target_cpa_micros,
  campaign_budget.amount_micros,
  metrics.impressions, metrics.clicks, metrics.cost_micros,
  metrics.conversions, metrics.average_cpc, metrics.cost_per_conversion,
  metrics.search_impression_share,
  metrics.search_budget_lost_impression_share,
  metrics.search_rank_lost_impression_share
FROM campaign
WHERE campaign.status != 'REMOVED'
```

If `serving_status` is unrecognized, drop it and infer from end date, group status, and window cost. Mark serving classification WATCH.

## Account totals (reconcile)

```
SELECT metrics.impressions, metrics.clicks, metrics.cost_micros,
  metrics.conversions, metrics.cost_per_conversion
FROM customer
WHERE segments.date BETWEEN '{start}' AND '{end}'
```

## Conversion actions

```
SELECT conversion_action.id, conversion_action.name, conversion_action.status,
  conversion_action.type, conversion_action.category,
  conversion_action.primary_for_goal
FROM conversion_action
WHERE conversion_action.status != 'REMOVED'
```

```
SELECT campaign.name, segments.conversion_action_name, metrics.conversions
FROM campaign
WHERE segments.date BETWEEN '{start}' AND '{end}'
  AND metrics.conversions > 0
```

## Ad groups

```
SELECT campaign.name, ad_group.id, ad_group.name, ad_group.status,
  metrics.impressions, metrics.clicks, metrics.cost_micros, metrics.conversions
FROM ad_group
WHERE campaign.status != 'REMOVED'
  AND ad_group.status != 'REMOVED'
  AND segments.date BETWEEN '{start}' AND '{end}'
```

## Keywords

```
SELECT campaign.name, ad_group.name,
  ad_group_criterion.keyword.text, ad_group_criterion.keyword.match_type,
  ad_group_criterion.status,
  ad_group_criterion.quality_info.quality_score,
  ad_group_criterion.quality_info.search_predicted_ctr,
  ad_group_criterion.quality_info.creative_quality_score,
  ad_group_criterion.quality_info.post_click_quality_score,
  ad_group_criterion.system_serving_status,
  ad_group_criterion.approval_status,
  metrics.impressions, metrics.clicks, metrics.cost_micros,
  metrics.conversions, metrics.average_cpc, metrics.ctr
FROM keyword_view
WHERE segments.date BETWEEN '{start}' AND '{end}'
  AND ad_group_criterion.status != 'REMOVED'
```

## Search terms

```
SELECT campaign.name, ad_group.name, search_term_view.search_term,
  search_term_view.status, metrics.impressions, metrics.clicks,
  metrics.cost_micros, metrics.conversions
FROM search_term_view
WHERE segments.date BETWEEN '{start}' AND '{end}'
  AND metrics.cost_micros > 0
ORDER BY metrics.cost_micros DESC
```

## Ads and landing pages

```
SELECT campaign.name, ad_group.name, ad_group_ad.ad.id, ad_group_ad.ad.type,
  ad_group_ad.status, ad_group_ad.ad_strength,
  ad_group_ad.policy_summary.approval_status, ad_group_ad.ad.final_urls,
  metrics.impressions, metrics.clicks, metrics.cost_micros, metrics.conversions
FROM ad_group_ad
WHERE segments.date BETWEEN '{start}' AND '{end}'
  AND ad_group_ad.status != 'REMOVED'
```

```
SELECT landing_page_view.unexpanded_final_url, metrics.impressions,
  metrics.clicks, metrics.cost_micros, metrics.conversions
FROM landing_page_view
WHERE segments.date BETWEEN '{start}' AND '{end}'
  AND metrics.impressions > 0
```

## Assets / extensions

```
SELECT campaign.name, asset.type, campaign_asset.status
FROM campaign_asset
WHERE campaign_asset.status != 'REMOVED'
```

```
SELECT asset.type, customer_asset.status
FROM customer_asset
WHERE customer_asset.status != 'REMOVED'
```

## Time, demo, geo, audience

```
SELECT segments.hour, metrics.cost_micros, metrics.conversions
FROM customer
WHERE segments.date BETWEEN '{start}' AND '{end}'
```

```
SELECT segments.day_of_week, metrics.cost_micros, metrics.conversions
FROM customer
WHERE segments.date BETWEEN '{start}' AND '{end}'
```

```
SELECT campaign.name, ad_group_criterion.age_range.type,
  metrics.cost_micros, metrics.conversions
FROM age_range_view
WHERE segments.date BETWEEN '{start}' AND '{end}'
```

```
SELECT campaign.name, ad_group_criterion.gender.type,
  metrics.cost_micros, metrics.conversions
FROM gender_view
WHERE segments.date BETWEEN '{start}' AND '{end}'
```

```
SELECT campaign.name, campaign_criterion.type, campaign_criterion.negative,
  campaign_criterion.proximity.radius,
  campaign_criterion.location.geo_target_constant
FROM campaign_criterion
WHERE campaign_criterion.type IN ('LOCATION', 'PROXIMITY', 'LOCATION_GROUP')
```

```
SELECT campaign.name, ad_group_criterion.display_name, ad_group_criterion.type,
  metrics.cost_micros, metrics.conversions
FROM ad_group_audience_view
WHERE segments.date BETWEEN '{start}' AND '{end}'
```

## Shared negatives and recommendations

```
SELECT shared_set.name, shared_set.type, shared_set.member_count,
  shared_set.status
FROM shared_set
WHERE shared_set.status != 'REMOVED'
```

```
SELECT recommendation.type, recommendation.campaigns
FROM recommendation
```

## PMax stand-ins

```
SELECT campaign.name, asset_group.name, asset_group.status,
  metrics.impressions, metrics.clicks, metrics.cost_micros, metrics.conversions
FROM asset_group
WHERE segments.date BETWEEN '{start}' AND '{end}'
```

```
SELECT campaign.name, campaign_search_term_insight.category_label,
  metrics.impressions, metrics.clicks
FROM campaign_search_term_insight
WHERE segments.date BETWEEN '{start}' AND '{end}'
```

Auction insights field names drift by API version. If the query is rejected, mark that leaf BLOCKED. Do not guess competitor domains.

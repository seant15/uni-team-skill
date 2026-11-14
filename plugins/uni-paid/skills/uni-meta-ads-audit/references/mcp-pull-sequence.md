# Data pull sequence (Meta Ads MCP)

Verified against the Meta Ads MCP tool set on 2026-11-13. Field names change; run `ads_get_field_context` on any field before first use in a session. If a tool returns `next_actions` with read-only required steps, run them before answering.

Save every result to a file before computing. Keep one folder per audit run.

| # | Tool | Arguments | Why |
|---|---|---|---|
| 1 | `ads_get_ad_accounts` | - | Find every account for the brand. Check `is_queryable`, currency |
| 2 | `ads_get_ad_entities` level=campaign | `date_preset=last_90d`, filter `amount_spent > 0`, fields: name, effective_status, objective, created_time, daily_budget, bid_strategy, attribution_setting, amount_spent, impressions, reach, frequency, cpm, ctr, cost_per_link_click, omni_purchase, omni_purchase_values, purchase_roas | Campaign map and attribution settings |
| 3 | `ads_get_ad_entities` level=ad_account | 90-day `time_range`, `time_increment="7"`, fields: spend, impressions, reach, frequency, cpm, ctr, cost_per_link_click, link_click, landing_page_view, omni_add_to_cart, omni_initiated_checkout, omni_purchase, omni_purchase_values, purchase_roas | Weekly trend and funnel |
| 4 | `ads_get_ad_entities` level=ad | last 30 days, sort `amount_spent_descending`, add created_time, creative_id, adset_name, campaign_name, outbound_clicks_ctr, video_play_actions, video_p25/p95_watched_actions, video_avg_time_watched_actions | Creative rollup. Page with `cursor` until spend covered is 95%+ |
| 5 | level=ad_account, breakdowns `publisher_platform` + `platform_position` | last 30 days | Placement table |
| 6 | level=ad_account, breakdown `country` | last 30 days, add IC and ATC | Geo table and the reconciliation total |
| 7 | level=ad_account, breakdowns `age` + `gender` | last 30 days | Demo table |
| 8 | `ads_get_datasets` then `ads_get_dataset_quality` | pixel id, `query_type=["web"]` | EMQ and match-key coverage per event |
| 9 | level=adset | last 30 days, fields: learning_stage_info, targeting, optimization_goal, daily_budget, created_time, frequency | Learning state, Advantage+ audience flag, placements, interests |
| 10 | `ads_account_get_activity_logs` | `event_category=budget`, last 30 days; repeat with `status` if needed | Budget edits and who made them |
| 11 | `ads_insights_performance_trend` | `analysis_level=AD`, `hide_ui=true` | Meta's own improving / declining read |
| 12 | `ads_insights_performance_vs_peers` | `date_preset=last_30d` | Funnel percentiles vs peer cohort |
| 13 | `ads_get_opportunity_score` | - | Account score and recommendations with URLs |

Notes:

- Account-level requests do not accept `filtering` or `sort`.
- `video_play_actions` on an auto-play feed is close to impressions. Use p25 and p95 over impressions for hook and hold, not plays.
- `learning_stage_info.status = FAIL` in the API is "Learning limited" in Ads Manager.
- `attribution_setting` values seen: `1d_view_7d_click`, `1d_view_7d_click_1d_ev` (includes engage-through), `multiple`. Report them as written.
- Live site checks (product page, cart) use a browser or WebFetch, not the ads tools.

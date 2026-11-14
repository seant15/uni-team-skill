# Troubleshooting

## Import / API errors

| Symptom | Cause | Fix |
|---|---|---|
| "Invalid objective/optimization goal combination" | Illegal ODAX triple | Export a working ad in that objective from the account; copy its Optimization Goal and Billing Event |
| "Pixel not found" | Pixel belongs to another account | Share it via Business Settings, or use the account's own pixel |
| "Image hash not found" | Hash is from a different ad account | Re-upload the image to this account and use the new hash |
| "Filename not provided" | Case or extension mismatch | Match the filename character-for-character; check the zip actually contains it |
| "The video you're trying to upload is in a format that isn't supported" | The file has **no extension** (`fileExtension: ""`), so Meta cannot type it. Not a codec problem | Rename with the extension, then `ads_create_upload_url` with the full `file_name` and `mime_type` |
| Upload by `media_url` fails on a Drive / Dropbox link | Share links return a sign-in page, not bytes | Download with the Drive connector, then use `ads_create_upload_url` + `ads_finalize_upload` |
| Two copies of the same video in the library | A video `completion_token` was finalized twice | Check `ads_get_ad_videos` by name before re-finalizing; delete the spare in Ads Manager |
| "Referenced item unavailable" (3858794) or creative create fails on a video | Video still transcoding, or a hash from another account | Poll `ads_get_ad_videos` until `video_status` is `ready`, then retry |
| New ads carry different Advantage+ enhancements from the template | Official MCP turns default enhancements on for new inline creatives where the account allows | Read `advantage_plus_creative_defaults` on the result; match the template with `advantage_plus_creative_features` or set defaults OFF |
| Objects show `status=DRAFT` and nothing delivers | Account is in draft mode; creates were staged | Review with `ads_get_ad_entities object_state=draft`, then publish with `ads_activate_entity` only on an explicit go |
| Copied ad set name is wrong | Copy keeps or suffixes the source name | Rename with `ads_update_entity` immediately after |
| "Cannot update field" | Objective or Buying Type is immutable | Create a new campaign |
| Ad set budget rejected | Campaign uses CBO | Blank the ad-set budget columns |
| Budget is 100× wrong | Minor-unit confusion | Budgets are integer cents. $50/day = `5000`. Read the created object back |
| Import rejected on size | Row count / file size cap | Split into 1,000-2,000 row files |
| Rows land in wrong columns | Header whitespace or renamed headers | Re-export headers from the account and rebuild the file |
| Write blocked / rate limited | Creation cap hit | Stop and report. Do not retry in a loop or switch tools |
| Account write fails entirely | Account status 2 / 3 / 101 | Stop. Escalate to the client - this is an account health issue, not a build issue |

## Post-launch symptoms

| Symptom | Likely cause | Fix |
|---|---|---|
| Placements are not what was set | Advantage+ reactivated on import | Edit the ad set placements in the UI and re-verify |
| Ads created but getting zero delivery | Too many ads per ad set, or still in review | Expect 3-6 delivering per ad set; check review status |
| Ad set stuck in learning | Not enough weekly events | Consolidate ad sets, switch to CBO, or raise budget - recompute the learning math |
| New ads have no likes/comments | Duplicated creative creates a new post | Rebuild referencing the existing post ID |
| Spend but no conversions recorded | Pixel/event mismatch or UTM gap | Verify the event fires, check dedup between pixel and CAPI |
| Reporting can't split by creative | Ad names inconsistent or duplicated | Rename now, before more data accrues; enforce the convention next batch |

## Escalation rules

Stop and hand back to the buyer - do not improvise - when:

- The ad account is disabled, closed or flagged
- A write is rate-limited or repeatedly rejected
- The Special Ad Category answer is uncertain
- The build is partially complete and an error interrupted it (report exactly what exists)
- The brief asks for something that violates Meta's ad policies

A partial build left undocumented in a client account is the worst possible outcome. Always
report exactly which objects were created before the stop.

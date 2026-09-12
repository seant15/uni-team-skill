# Troubleshooting

## Import / API errors

| Symptom | Cause | Fix |
|---|---|---|
| "Invalid objective/optimization goal combination" | Illegal ODAX triple | Export a working ad in that objective from the account; copy its Optimization Goal and Billing Event |
| "Pixel not found" | Pixel belongs to another account | Share it via Business Settings, or use the account's own pixel |
| "Image hash not found" | Hash is from a different ad account | Re-upload the image to this account and use the new hash |
| "Filename not provided" | Case or extension mismatch | Match the filename character-for-character; check the zip actually contains it |
| "The video you're trying to upload is in a format that isn't supported" | The cloud-storage file has **no extension** (`fileExtension: ""`), so Meta cannot type it. Not a codec problem | Upload per file with `upload_ad_video_file` passing explicit `filename` (with `.mp4`) and `mime_type` |
| "No Google Drive connection found" | The MCP's own cloud-storage authorization is missing. Claude's Drive connector is a different thing | User connects Drive/Dropbox at `pipeboard.co/connections`, using an account that can see the folder |
| "Referenced item unavailable" (3858794) | Video still transcoding, or a hash from another account | Poll `get_ad_video` until `video_status: ready`, then retry. `dry_run` will not catch this |
| New ads have no Advantage+ enhancements | Creatives default to all `OPT_OUT`; nothing is inherited | Pass `creative_features_spec` matching the template ad, or state clearly that enhancements are off |
| Duplicated ad set arrived full of old ads | `include_ads` defaults to true | Re-duplicate with `include_ads=false`, delete the wrong copy |
| Duplicated ad set name carries two dates | `duplicate_adset` only appends a suffix | Rename with `update_adset` immediately after |
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

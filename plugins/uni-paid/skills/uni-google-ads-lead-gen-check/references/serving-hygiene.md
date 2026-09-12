# Serving hygiene

`campaign.status = ENABLED` is a switch, not proof of delivery.

| serving_status (typical) | Meaning | Treat as |
|---|---|---|
| SERVING | Eligible to show | Live. Score it. |
| ENDED | End date in the past | Dead. Not a P0 pause. Optional hygiene: flip status to PAUSED so nobody reopens the date. |
| PENDING | Not started or limited | Not live yet. |
| SUSPENDED | Billing or policy hold | Report. Do not "optimize" it as if it were pacing. |

Also check the layer below the campaign:

- Ad groups PAUSED + campaign ENABLED = not a live test
- Ads DISAPPROVED on an ENDED campaign = policy residue, not current delivery
- Window cost = 0 = keep it out of the optimization set

A/B or "trial" campaigns are often left ENABLED after someone set an end date or paused the groups. Re-read serving_status and group status before you write "stop the trial."

Source for status vs serving: Google Ads API campaign resource (verify in the live API if an enum is missing). Tagged unverified if your client library does not return `serving_status`.

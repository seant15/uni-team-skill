# Intent ladder

Run this after the account is resolved and before you score checklist section 1 as if keywords were independent.

A lead-gen Search account is a stack. If the stack disagrees with itself, the metrics lie.

```
Campaign job
  -> Ad group / asset group job
    -> Enabled keyword or signal
      -> Actual search term / insight
        -> Final URL
```

## Labels (use these words, not new ones)

| Label | Meaning |
|---|---|
| ALIGNED | Layer does the job the parent layer claimed |
| LEAK | Layer bought a nearby but cheaper or broader intent |
| CANNIBAL | Same query is eligible in two live campaigns or groups |
| WRONG SPECIALTY | Query is a different trade (example: orthodontics on an emergency dentistry campaign) |
| PRICE RESEARCH | Query is cost / insurance / cheap / funded, and the campaign is not a pricing campaign |

A conversion on WRONG SPECIALTY or LEAK is not a win. Write it as "converted, wrong intent."

## What to pull per layer

Campaign: name, channel, bidding type, tCPA if any, daily budget, window cost / conv / CPL.

Ad group: name, status, window cost / conv. PMax: asset group name and status.

Keywords: enabled text and match type. Separate ENABLED+0 impressions from ENABLED+spend. Broad on a "phrase only" campaign is a stack break.

Search terms: spend-ranked. Tag ADDED / EXCLUDED / NONE. NONE + spend is either harvest or negate.

Landing page: unexpanded final URL cost / conv. Two URLs in one ad group need a winner. An offer URL that is paused while a weaker URL is live is a stack break.

## Cross-campaign pass

After each campaign ladder, list queries that appear in more than one SERVING campaign (brand terms on competitor PMax, generic "dentist near me" on a treatment campaign, All-on-X syntax inside a single-implant campaign). Those are CANNIBAL rows, not "more coverage."

## What not to do

Do not dump every enabled keyword. Show the heaviest spend, every converting mismatch, and a short sample of enabled-but-idle terms that prove the group is over-built.

Do not call a second RSA a split test if it is PAUSED or Ad Strength is PENDING and it has no impressions.

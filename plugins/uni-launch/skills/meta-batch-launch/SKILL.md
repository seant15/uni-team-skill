---
name: meta-batch-launch
description: Build many Meta ads at once - a creative matrix, a cloned ad set, a bulk upload sheet. Use when someone says "batch launch", "bulk upload Facebook ads", "launch a creative test", "3 creatives x 3 audiences", "duplicate this ad set and put these new creatives in it", "spin up the Q4 test matrix", or asks for more than a handful of ad sets or ads in one go. Not for single-ad edits, reporting, or optimisation.
---

# Meta batch launch

Without this skill a buyer builds a twelve-ad test by hand, two of the ads carry a budget
100x off because the API takes cents, and the ad names come out inconsistent enough that the
monthly report cannot split by creative. The work is not the clicking. The work is the
arithmetic and the naming that nobody checks until the money is spent.

**Everything is built paused. Publishing is a separate, explicit instruction naming that batch.**

## Step 1 - Interview

Ask in one batch. Skip what was supplied. Pull known values from the client file rather than
re-asking.

| Group | Establish |
|---|---|
| Account | Ad account id, and that its status is active |
| Identity | Facebook Page id, Instagram account id, pixel or dataset id, conversion event |
| Campaign | ODAX objective, budget amount, daily vs lifetime, CBO or ABO, geo, age, schedule |
| Compliance | Special Ad Category - housing, employment, credit, social issues, or none |
| Matrix | The audiences (2-3), the creatives (3-5), where the asset files live |
| Copy | One shared set, or one per creative. Landing URL and UTM convention |
| Naming | The client's convention if they have one, otherwise `references/naming-and-matrix.md` |
| Target | Target CPA - needed for the learning-phase gate, and there is no default worth guessing |

### Stop and ask - guessing is worse than asking

- **Special Ad Category.** A wrong answer gets the account flagged, not warned.
- **Target CPA.** Without it the learning-phase gate cannot run, and the gate is the point.
- **CBO or ABO.** Budget at the wrong level silently conflicts and the import fails.
- **Which ad set is the source** on a clone, and whether its audience changes. If the answer is
  "clone it and also change the audience", say that moves two variables and confirm before doing it.
- **Landing URL** when the creatives imply different destinations.
- **Asset location.** See `references/asset-ingestion.md` before promising a timeline. This is the
  step that fails most often, and it fails on authorisation, not on ad mechanics.

## Step 2 - The work

### Pick the rail first

| Rail | Use when |
|---|---|
| Meta Ads MCP | The agency has API access to the account. Fastest up to roughly 50 ads |
| Meta native XLSX bulk import | Ads Manager login only, or 50+ ads, or a cross-account clone |

Probe the account list. Statuses other than active stop the build - report it as an account
health problem, not a build error. Never switch rails silently.

### Structure the matrix

Audiences live on ad sets. Creatives live on ads. Three audiences and four creatives is **one
campaign, three ad sets, twelve ads** - not three campaigns, which fragments both the budget and
the learning phase.

Run the learning-phase gate on every ad set before building anything:

```
weekly events = (daily budget x 7) / target CPA
```

| Result | Do |
|---|---|
| 50 or more | Build it |
| 25 to 50 | Warn, and recommend CBO or fewer ad sets |
| Under 25 | Stop. Show the arithmetic, propose consolidating, raising budget, or a higher-funnel event |

Show the sum, never the conclusion alone. "30 purchases per week per ad set" is an argument.
"This will not exit learning" is an assertion the buyer can wave away.

### The clone-and-extend path

The most common real request is not "build a matrix", it is "duplicate this ad set and put these
new creatives in it". Handle it as its own path.

1. Read the source ad set. Clone targeting, budget, optimisation goal, billing event, placements
   and schedule. Change nothing that was not asked for.
2. Read one **template ad** in the same campaign. Lift its copy, CTA, landing URL and **URL tags
   verbatim**. Writing fresh UTMs forks the client's reporting silently.
3. Read the template ad's `creative_features_spec`. New creatives are born with every Advantage+
   enhancement opted out, while a hand-built ad usually has eight to ten opted in. Ship without
   comparing and the creative test is confounded before it starts. Show the buyer the gap and let
   them choose. Flag `text_optimizations` separately - it lets Meta rewrite approved copy.
4. Build the new ad set paused. Leave the original untouched.

Mechanics that bite, all verified against a live account on 2026-09-11:

| Behaviour | Handle |
|---|---|
| `duplicate_adset` copies the source's ads by default | Pass `include_ads=false` |
| It only appends a name suffix, leaving two dates in the name | Rename with `update_adset` immediately |
| `tracking_specs` are inherited correctly | Do not hand-build them |
| Meta may adjust placements for compatibility | Report it. It is Meta's rule, not a build error |

### Build order

```
assets -> campaign -> ad set(s) -> creative(s) -> ad(s)
```

Build the first ad set and its first ad end to end, read them back, confirm the budget number
came back as intended, then loop the rest. One misread budget unit repeated across twelve ads is
a cleanup job. Caught on ad one it is a retry.

If a write is rate-limited or rejected: stop, report exactly which objects exist, and wait. Never
retry in a loop, never switch tools to route around a cap. A half-built campaign nobody documented
is worse than no campaign.

## Step 3 - Validate before delivering

| Check | Fail = |
|---|---|
| Budgets are integers in minor units, and the created object was read back | A campaign running at 100x or 1/100th of the intended spend |
| Learning-phase arithmetic run per ad set and shown | A matrix that mathematically cannot produce a readable result |
| Page id present, landing URL starts with `https://`, pixel belongs to this account | Meta refuses the ad, or it runs untracked |
| CBO on and ad-set budgets blank, or ABO and campaign budget blank | Import rejected on a budget conflict |
| Objective, optimisation goal and billing event are a legal combination | Row-level rejection at import |
| Every ad name follows the convention and is unique inside its ad set | Report pivots on creative silently collapse |
| Every video reports ready before a creative references it | "Referenced item unavailable" - and `dry_run` does not catch it |
| Creative enhancements compared against the template ad, difference stated | Confounded creative test |
| Image hash or video id belongs to **this** ad account | Asset does not resolve |
| Headline and primary text inside the limits in `references/meta-build-limits.md` | Truncated or rejected copy |
| Special Ad Category answered, and targeting respects it | Account flag |
| Object counts reconciled against the build plan after the build | Silent partial build |
| Zero em dashes or en dashes | House typography rule broken |

Then run **uni-output** on the deliverable before it leaves.

Deliver the build plan table, the object counts, anything changed from the brief and why, and the
one date to come back and read results. Creative reads need three to five days and meaningful
spend. Never hand back "done".

## References

| File | Holds |
|---|---|
| `references/meta-build-limits.md` | Objectives, limits and structural caps, each tagged verified or unverified |
| `references/asset-ingestion.md` | How creative files reach Meta, and the three traps that stop a launch |
| `references/naming-and-matrix.md` | The naming convention, matrix expansion, learning-phase math |
| `references/xlsx-bulk-import.md` | The XLSX rail: columns, creative rules, cross-account cloning |
| `references/troubleshooting.md` | Every error seen in production, with the fix |
| `references/worked-example.md` | An anonymised real launch, end to end |
| `scripts/build_bulk_xlsx.py` | Matrix spec to Meta-ready workbook, exits non-zero on any blocker |
| `templates/matrix-spec.example.yaml` | The intake, as a fillable spec |

## Self-Improvement

At the end of every run, before ending:
1. Did any step fail or need a workaround?
2. Did the user correct or reject anything meaningful?
3. Did you discover something a future run might need?

Meta changes bulk template headers, objective combinations and enhancement defaults without
announcement. If a fact in `references/meta-build-limits.md` proved wrong against a live account,
that is a P1 fix - propose the corrected row with today's date and how it was observed. Only
propose a change if it meaningfully improves the skill, and propose it as a diff for a pull
request against `seant15/uni-team-skill` - never edit the installed copy.

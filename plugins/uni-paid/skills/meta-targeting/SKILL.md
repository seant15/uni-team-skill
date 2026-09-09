---
name: meta-targeting
description: Build a Meta detailed-targeting plan using UNI's interest-web method - expanding a customer persona across life dimensions (media, people, gear, home, work) and two-steps-removed adjacencies to surface interest sets competitors never think to test. Use for any request about Facebook or Instagram interest targeting, audience building, detailed targeting, "who should we target", audience refresh, or when an interest-based ad set stopped delivering. Interviews the requester on the persona first, then searches, expands, validates, and hands back a tiered test plan.
---

# Meta interest targeting - the UNI interest web

## Read this before anything else

Two facts about Meta in 2026 change what this skill can honestly deliver. Both are verified against Meta's own documentation. Read `references/platform-reality-2026.md` for the full picture and sources.

**1. For most performance goals, detailed targeting is a signal, not a fence.**

Meta's own words: if you optimize for **Link clicks, Landing page views, Conversations, Conversion, App Events, App installs, or Value**, Advantage+ detailed targeting is *"automatically applied with no option to opt out."* Interests you select are **suggestions**. Meta will deliver outside them.

The only true audience **controls** left are: **Location, Minimum age, Language, and Custom audience exclusions.** Everything else - age, gender, detailed targeting, custom audience inclusions - is a suggestion.

So interest selection is now a **seeding and reading exercise**, not a fencing exercise. We are telling the algorithm where to start looking and giving ourselves a readable variable to test. That is still worth doing well - it measurably changes early delivery - but never tell a client an interest "locks" the audience. It does not.

**2. Detailed targeting exclusions are gone.** Removed July 2024; ad sets using them stopped delivering January 31, 2025. You cannot exclude an interest. **Custom audience exclusions still work** and remain a hard control - that is where "exclude purchasers 30d" lives, and it is unaffected.

**3. There is no master interest list, and there never was one.** Meta has never published one. The January 15, 2026 consolidation removed and merged a large number of interests **without publishing what was removed** - agencies discovered the damage by validating their live ad sets. Any static list you find online is a decaying snapshot.

**Therefore this skill does not ship an interest list. It ships a method, and a per-client snapshot with a validation sweep.** If someone asks for "the full list of Meta interests," the honest answer is that it does not exist and that a validated per-client set is worth more.

---

## Step 1 - Interview the requester

The quality of the interest web is set entirely by the quality of the persona. Never expand from a one-line brief. Ask in one batch; skip what's supplied.

**Interview gate.** Ask everything below in one batch, skip what is supplied, then lock the brief before producing. Never fill a gap with a plausible value. The full rule is in `uni-standards:uni-output` under *The interview gate*.


### The product

1. **What is being sold, and what does it cost?** Price bracket changes the persona more than the category does.
2. **What problem does the buyer think they are solving?** Their framing, not the client's marketing framing.
3. **What is the purchase trigger?** A moment, a season, a life event, a breakage, a status shift.
4. **Who buys but is not the user?** Gifting and household-decision products need a second persona.

### The persona - go concrete, refuse abstractions

Push back on "women 25-45 interested in wellness." That is not a persona, it is a census bracket.

5. **Describe one real customer.** Age, where they live, what they do for work, household shape.
6. **What is their day actually like?** Where does the product fit in it?
7. **What do they already spend money on** that isn't this product?
8. **What do they read, watch, or listen to?**
9. **Who do they follow or admire?**
10. **What is in their home** that signals they're this person?
11. **What do they call themselves?** The identity label matters - Meta interests are frequently identity labels.

### Campaign context

12. **Objective and optimization goal** - decides whether interests are a signal or can be enforced at all
13. **Budget and expected test duration** - sets how many interest sets we can honestly test
14. **What has already been tested**, and what won or lost. Repeating a dead test is the most common waste here.
15. **Special Ad Category?** Housing, Employment, Credit, Social/Political - detailed targeting is restricted and Advantage+ audience is unavailable.
16. **Existing custom audiences** - purchasers, site visitors, engagers, lists. These matter more than interests now.

**Stop and ask** if: the persona comes back as demographics only; there is no analytics or customer data to ground it; or the client is under 18 targeting (location, age and gender only - no detailed targeting at all).

---

## Step 2 - Build the interest web

This is UNI's method. Its purpose is to reach **interest space competitors do not think to test** - which is where the cheap inventory lives, because everyone else is bidding on the five obvious interests.

### The two rules that govern everything

**The 50% relevance rule.** An interest does not need to be 100% about our buyer. **50% is enough to be worth testing.** A magazine our buyer reads for one of its six sections is a valid interest. Insisting on pure relevance is what herds every agency onto the same five interests.

**The 50% logic rule.** But it must be at least **50% logically self-consistent** - you must be able to state the chain out loud in one sentence, and it must not be embarrassing. *"People into home espresso buy Japanese kitchen knives, because both are 'one good tool for life' purchases"* - that holds. *"People into espresso like camping"* - that does not. If you cannot say the chain, cut the interest.

Together: **loose on relevance, strict on reasoning.**

### The dimensions

Expand the persona across each dimension. For each, do a **real web search** - do not generate from memory, because the point is to find things you did not already know about this world.

| Dimension | What you're looking for | Search like |
|---|---|---|
| **Media** | Magazines, publications, YouTube channels, podcasts, shows, newsletters this person actually consumes | "best magazines for [persona interest] 2026", "top podcasts [niche]" |
| **People** | Celebrities, athletes, authors, founders, influencers they follow or admire | "who do [persona] follow", "biggest names in [niche]" |
| **Gear** | The products and equipment bought *for* this interest - brands, tools, kit | "essential gear for [activity]", "[niche] starter kit" |
| **Home** | What sits in their house that signals this identity - appliances, furniture, decor, categories | "what's in a [persona]'s kitchen/garage/home office" |
| **Work** | Job titles, industries, employers, professional tools and software | "job titles in [industry]", "software used by [role]" |
| **Retail** | Where they shop - retailers, marketplaces, DTC brands | "where do [persona] buy [category]" |
| **Events & community** | Conventions, races, festivals, forums, associations | "[niche] events 2026", "[niche] community" |

The first five are UNI's core set. Retail and Events are extensions - cut them if the persona is thin.

### Two steps out

Direct adjacency is where competitors already are. **The value is at two steps.**

- **One step:** buyer likes running → interest "Running." Everyone has this.
- **Two steps:** buyer likes running → runners track everything → **interest in quantified-self tools, sleep tracking, wearables that aren't running watches.** Fewer bidders, chain still holds.

For each dimension, after listing the direct interests, ask: **"what does this population *also* care about, that is not about our category at all?"** That answer is the two-step layer, and it is what this method exists to produce.

Target roughly **one-third direct, two-thirds two-step** in the final set. If the web is all direct interests, the method was not applied.

### Start from the library

`references/interest-library.md` holds UNI's baseline interest vocabulary, keyed by interest ID. Start expansion from it rather than from a blank page, and add anything new you validate back into it by pull request.

The library is a seed list, not an authority. **Every row still gets validated before it reaches a client deliverable.**

### The name field is a search string, not a description

This is the rule the deliverable dies on. A media buyer took `Aesthetic motherhood / cottagecore mom content`, `Dr. Becky Kennedy / gentle parenting creators` and `Mommy and Me (fashion/lifestyle)` to Ads Manager, could not find any of them, and lost the whole cluster.

**The `name` field must be a literal string the buyer can type into the detailed-targeting search box.** `TJ Maxx`. `Cricut`. `Gymnastics`. `Carter's`. Short, a proper noun or a platform category, one thing.

Everything that made you choose it - the persona, the aesthetic, the creator whose audience you are approximating - goes in `Chain`. **A persona in the `name` field is a P1, no matter how good the reasoning behind it is.** The reasoning is not what the buyer pastes.

Three signatures the lint rejects, and you should reject before it does:

| Reject | Why | Do instead |
|---|---|---|
| `Aesthetic motherhood / cottagecore mom content` | genre description, not a taxonomy entry | put the aesthetic in `Chain`, name a brand or category the platform actually carries |
| `Dr. Becky Kennedy / gentle parenting creators` | a creator plus an audience guess, joined by a slash | one row per searchable label. Search the person's name alone and see whether Meta carries it. |
| `Church / Christian parenting content engagers` | two concepts and a behaviour invented in-house | `Hobby Lobby`, `Vacation Bible School` - things that exist |

If the honest answer is that no platform interest expresses the idea, **say that instead of inventing a label.** A named gap is useful; a plausible string is a trap.

### Validate every candidate exists

Interest names drift and Meta deletes without notice. **A name is not proof an interest exists.**

- In Ads Manager: type it into the detailed targeting search box. If it does not appear, it is gone. Record the **audience size** shown.
- Via API where available: `GET /v26.0/search?type=adinterest&q=<name>&limit=1000`, and validate with `type=adinterestvalid`. **Store the interest ID, not the name** - names are renamed, IDs are stable. See `references/platform-reality-2026.md` for the full endpoint set.

Anything that cannot be confirmed to exist does not go in the deliverable as a confirmed row. Mark it rather than dropping it silently - that is useful information about the current state of Meta's taxonomy.

**Two statuses, and only two:**

| `status` | Means | Requires |
|---|---|---|
| `live` | You actually saw it in Ads Manager, or the API returned it valid | the interest **ID** recorded, plus the date you checked |
| `UNCONFIRMED` | You could not check it | one line in the deliverable telling the buyer to type it into the Ads Manager search box before launch |

**Never write `live` for a row you did not check.** That is the one failure mode worse than the current state: today a fabricated interest is obvious to the buyer, and a fabricated interest carrying a validation stamp is not. The lint fails any `live` row with no ID for exactly this reason.

**When the API is unreachable** - as of 2026-09-08 the Facebook Ads MCP on this machine fails discovery, so it is - every row ships `UNCONFIRMED` and the deliverable says so in one line at the top. Do not describe a validation sweep that did not happen.

Before falling back to UNCONFIRMED, try in this order: the Graph API Explorer with a personal token (`type=adinterestvalid` takes a name list), then a third-party interest explorer that proxies the same endpoint, then Ads Manager by hand for the highest-value rows. Confirming five interests by hand beats shipping twenty-five guesses.

**Every cluster also carries one fallback that does not need an interest to exist at all** - broad plus the right creative, a lookalike, or a custom-audience play. A dead cluster then costs the buyer one ad set, not the test.

---

## Step 3 - Turn the web into a test plan

A list of 60 interests is not a deliverable. Tiered, testable sets are.

**Group into clusters of 3-5 interests that share one theme.** Over eight in one cluster splits into two. A cluster is a hypothesis, and it must be nameable in three words - "Gear-obsessed hobbyist," "Time-poor parent," "Aspiring professional." If you cannot name it, it is not a coherent cluster.

**Deliver at least five cluster directions per run.** One or two clusters is an idea, not a test plan, and a buyer fighting frequency needs somewhere to move budget to this week.

Five clusters times three to five interests is fifteen to twenty-five rows to stand behind. **Do not pad to hit the number.** If the honest count of defensible clusters is four, deliver four, say the fifth would have been invented, and name what would unblock it - usually customer data or a working API. A padded fifth cluster is the mechanism that produced `cottagecore mom content` in the first place.

**Write the deliverable to a file in the shape the lint reads** (`uni-standards:uni-output` -> *The paid-media output contract* -> Contract 2):

```
=== CLUSTER 1: Off-price treasure hunters ===
Tier: 2
Chain: moms who chase boutique quality at a lower price already treasure-hunt at off-price chains
Kill: CPA over 1.5x Tier 1 after 2x ticket price spent
Fallback: broad targeting with the price-comparison creative
INTERESTS
- name: TJ Maxx | id: - | size: - | checked: 2026-09-08 | status: UNCONFIRMED
- name: Marshalls | id: - | size: - | checked: 2026-09-08 | status: UNCONFIRMED
- name: Ross Dress for Less | id: - | size: - | checked: 2026-09-08 | status: UNCONFIRMED
END INTERESTS
```

Order by tier:

| Tier | What it is | Expectation |
|---|---|---|
| **Tier 1 - Proven adjacent** | Direct interests, high confidence, probably already competitive | Benchmark. Establishes the number to beat. |
| **Tier 2 - Two-step** | The method's real output. Fewer bidders. | Where the win comes from, when it comes. |
| **Tier 3 - Long shot** | 50%-relevance sets with a chain you can state but wouldn't bet on | Cheap lottery tickets. Small budget, kill fast. |

For each set, deliver: **name · 3-8 interests with IDs and audience sizes · the logic chain in one sentence · what result would prove or kill it.**

### Stacking mechanics

- Interests inside one ad set are **OR** - anyone matching any of them qualifies. Interests are not additive filters.
- **"Narrow further"** creates an AND layer between groups. Still available in 2026.
- **You cannot exclude an interest.** Use custom audience exclusions instead.
- No documented minimum audience size. The "1,000 minimum" and "500k-3M sweet spot" figures circulating online have **no Meta source** - do not repeat them to a client as rules.

### Set the expectation honestly

Close the deliverable with one sentence stating that on this campaign's optimization goal, these interests function as **suggestions** and Meta will deliver beyond them - so the test reads as *"which seed produced the better outcome,"* not *"which audience saw the ad."* A buyer who does not know this will misread the results.

---

## Step 4 - Validate before delivering

**Run the gate first. It is a script, and it can refuse.**

```
python skills/uni-output/scripts/lint-ads-output.py <file> --type targeting
```

Exit 1 means not deliverable. Fix every P1, re-run, and put the result line in the handoff:

```
Lint: targeting 5 clusters pass (P1=0, P2=1) - 15 rows UNCONFIRMED
```

The lint catches persona-shaped names, slash-packed rows, `live` without an ID, missing check dates, cluster and row counts, and a missing "type it into the search box" instruction. Everything below is what a script cannot judge.

| Check | Fail = |
|---|---|
| Every `live` row was genuinely seen in Ads Manager or returned valid by the API | A hallucination carrying a validation stamp |
| Every cluster has a stateable logic chain | 50% logic rule violated |
| At least half the interests are two-step | Method not applied; delivered the obvious list |
| No detailed-targeting **exclusions** anywhere | Feature no longer exists |
| Custom audience exclusions specified where relevant | Retargeting overlap left unhandled |
| Signal-vs-control expectation stated in writing | Buyer will misread the test |
| Special Ad Category / under-18 rules respected | Restricted or non-serving build |

Then run **uni-output** on the deliverable before it leaves.

---

## Maintenance

Interest sets rot. Meta consolidated heavily in January 2026 and gave no list of what it removed.

**Re-validate every live client's interest sets quarterly**, and immediately if an ad set's delivery drops without a budget or bid change. Store the per-client validated set with its date; a snapshot older than a quarter is a lead, not a fact.

---

## Self-Improvement

At the end of every run, before ending:
1. Did any step fail or need a workaround?
2. Did the user correct or reject anything meaningful?
3. Did you discover something a future run might need?

Two things specifically worth capturing: an interest that turned out not to exist (add it to the client's dead list), and a two-step chain that actually won (that chain is reusable across clients and is the most valuable thing this skill produces). Propose changes as a diff for a pull request against `seant15/uni-team-skill` - never edit the installed copy.

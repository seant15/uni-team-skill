# Interest web - worked example

A teaching example so the method is unambiguous. The client is invented; the mechanics are real.

**Client:** DTC brand selling a $340 electric kettle with temperature control.
**Persona from the interview:** 34, urban apartment, works in software or design, makes pour-over coffee at home on weekends, owns a grinder that cost more than most people's coffee machine, reads product reviews before buying anything.

---

## Step 1 - Expand across dimensions

Direct interests marked **[D]**, two-step marked **[2]**. Two-step should outnumber direct roughly 2:1.

### Media
- **[D]** Serious Eats · Bon Appétit · America's Test Kitchen
- **[2]** Wirecutter - *chain: this buyer researches before purchase; a review-site interest identifies the behavior, not the category*
- **[2]** Monocle · Kinfolk - *chain: the aesthetic this person buys into extends past coffee*
- **[2]** Hacker News / Ars Technica - *chain: the software-job half of the persona*

### People
- **[D]** James Hoffmann - *the coffee YouTube axis*
- **[2]** Marie Kondo - *chain: a $340 kettle is an intentional-object purchase, not a convenience purchase*
- **[2]** Kevin Kelly / Cool Tools - *chain: "one good tool for life" buyers cluster*

### Gear
- **[D]** Espresso · Coffee roasting · Chemex · AeroPress
- **[2]** Japanese kitchen knives - *chain: same buyer psychology - one expensive object, bought once, used daily*
- **[2]** Mechanical keyboards - *chain: the software-job persona, same "spend disproportionately on a daily-use object" pattern*
- **[2]** Fountain pens - *same chain, different object*

### Home
- **[D]** Small kitchen appliances · Kitchen (interest)
- **[2]** Muji · HAY · Design Within Reach - *chain: this kettle is going on a counter that already looks a certain way*
- **[2]** Houseplants - *chain: apartment-dweller who curates a small space. Roughly 50% relevant. Testable.*

### Work
- **[D]** - none directly
- **[2]** Software engineering · UX design · Product management - *chain: income bracket plus the persona's stated job*
- **[2]** Figma · GitHub - *chain: tool-level identity signal for the same population*

### Retail
- **[2]** Williams Sonoma · Sur La Table - *chain: where this purchase gets browsed offline*
- **[2]** MoMA Design Store - *chain: the intentional-object axis again*

---

## Step 2 - Group into named sets

| Set | Tier | Interests | Logic chain | Kill condition |
|---|---|---|---|---|
| **Coffee obsessive** | 1 | Espresso, Coffee roasting, James Hoffmann, Chemex, AeroPress | Directly in-category. Everyone bids here. | Benchmark set - never killed, it's the number to beat |
| **One good tool** | 2 | Japanese kitchen knives, Mechanical keyboards, Fountain pens, Cool Tools | This buyer spends disproportionately on a single daily-use object and keeps it for a decade | CPA >1.5× Tier 1 after 2× ticket price spent |
| **Curated apartment** | 2 | Muji, HAY, Design Within Reach, MoMA Design Store, Houseplants | The kettle is a visible object on a counter this person already curates | Same rule |
| **Tech salary** | 2 | Software engineering, UX design, Figma, Hacker News | Income bracket plus persona-confirmed occupation | Same rule |
| **Researcher** | 3 | Wirecutter, Consumer Reports, America's Test Kitchen | Buys on evidence - a behavior interest, not a category interest. 50% relevance, chain holds. | Small budget, kill fast |

Roughly one-third direct, two-thirds two-step. That ratio is the tell that the method was actually applied.

---

## Step 3 - Validate

For every interest above, before it ships:

1. Search it in Ads Manager detailed targeting. Absent = gone. **Record the audience size.**
2. Record the **interest ID**. Names get renamed; IDs don't.
3. Anything not found gets marked "not found 2026-08-23" in the deliverable, not deleted silently.

Expect casualties. The January 2026 consolidation hit lifestyle and hobby leaves hardest, which is exactly where the two-step layer lives.

---

## Step 4 - Frame the test correctly

The campaign optimizes for Conversions, so Advantage+ detailed targeting is on with no opt-out. State this in the deliverable:

> These five sets are seeds, not fences. Meta will deliver beyond them. What we are reading is which seed produced the better outcome - not which audience saw the ad.

Custom audience exclusions still work and still apply: exclude purchasers 30d on prospecting sets.

---

## Chains worth reusing across clients

The chain, not the interest, is the reusable asset. When a two-step set wins, record the chain here.

- **"One good tool for life"** - expensive daily-use object buyers cluster across categories: knives, keyboards, pens, kettles, boots, bags
- **"Curated small space"** - apartment dwellers who buy design objects; connects home goods, plants, storage, lighting
- **"Buys on evidence"** - review-site and testing-publication interests identify a *behavior* rather than a category, and travel across almost any considered purchase

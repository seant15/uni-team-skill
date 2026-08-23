---
name: ad-ideas
description: Generate ad concepts grounded in what competitors are actually running, not in generic brainstorm output. Use when a client needs fresh creative angles, when performance has flattened and the team is out of ideas, when entering a new category, or for a competitor ad teardown. Searches live ad libraries first, maps the category's saturated angles, then produces concepts positioned against the gap. Feeds winning concepts into creative-brief.
---

# Ad ideas

Ideation without research produces the same five ads the category already runs. The sequence here is deliberately backwards from how most brainstorms go: **look at what exists, find what's missing, then generate.**

The deliverable is not "20 ideas." It is a small number of concepts each positioned against a specific gap in what competitors are running.

---

## Step 1 - Interview

Ask in one batch. Skip what's supplied.

**Interview gate.** Ask everything below in one batch, skip what is supplied, then lock the brief before producing. Never fill a gap with a plausible value. The full rule is in `uni-standards:uni-output` under *The interview gate*.


### The business

1. **What does the brand sell, and what does it cost?**
2. **Who actually buys it**, and what do they compare it against before buying?
3. **What is genuinely different about it?** Push for something verifiable. "Better quality" is not an answer; "we're the only one that ships assembled" is.
4. **What do customers say in reviews and support tickets?** Their words are the raw material - the best hooks are usually already written by a customer.

### The competitive set

5. **Name 3-5 direct competitors.** If the client can't, that's the first finding.
6. **Who is the category leader**, and who is the fastest-growing challenger? They run different playbooks and both are worth reading.

### Constraints

7. **Register - elevated or sales, 1-5.** Same dial as `meta-ad-copy`.
8. **What can the brand actually produce?** Concepts requiring a video crew are worthless to a client with a phone and a product on a table. Ask before ideating.
9. **Cleared claims** - what can we say
10. **What has been tested and what died?** Do not re-propose a dead concept.

**Stop and ask** if: there is no verifiable differentiator; the client wants ideas but cannot produce anything beyond static product shots; or the category is regulated and claims are constrained.

---

## Step 2 - Research what's actually running

**Do the search. Do not generate from memory.** The entire value of this skill is grounding.

### Sources

- **Meta Ad Library** (`facebook.com/ads/library`) - every active Meta ad, by advertiser. Filter to the last 90 days. **How long an ad has been running is the single most useful signal available** - nobody keeps a losing ad live for four months.
- **Google Ads Transparency Center** - active Google and YouTube creative by advertiser
- **Category search** - recent campaigns, awards, and teardowns for the vertical
- **Review mining** - the client's own reviews and competitors' 1-star and 3-star reviews. Three-star reviews are the richest: they name the real objection without being noise.

### Map what you find

For each competitor, record: **angle used · format · how long it's been running · the hook in their first line.**

Then produce the category map:

| | |
|---|---|
| **Saturated angles** | What three or more competitors are all saying. Do not enter here - you'll pay to be compared. |
| **Long-running ads** | Anything live 90+ days. This is proven demand for that angle, in this category, with this audience. Study why it works before deciding whether to counter it. |
| **Absent angles** | What nobody is saying. Two kinds: the genuine gap, and the thing everyone tried and abandoned. **Ask which one it is before building on it.** |
| **Objections nobody handles** | From 3-star reviews. Usually the highest-value opening available. |

This map is a deliverable in its own right. Clients pay for it. Deliver it even when the ideas that follow get rejected.

---

## Step 3 - Generate against the gap

Every concept must state the gap it occupies. A concept without a stated gap is a guess.

Generate **15-20 internally**, then **deliver 5-7**. Discard anything that duplicates an angle already saturated in the map - unless the plan is to deliberately out-execute a proven angle, which is a legitimate strategy but must be named as such.

**Cover distinct angle families.** Five variations of one idea is one idea:

| Family | The move |
|---|---|
| **Problem-first** | Open on the pain, in the customer's exact words |
| **Objection-led** | Lead with the thing they're about to worry about |
| **Mechanism** | Show *why* it works - the strongest angle when the product genuinely differs |
| **Comparison** | Against the category's default solution, not against a named competitor |
| **Identity** | "People like you use this." Requires a real persona. |
| **Demonstration** | Show it working. Undefeated for physical products. |
| **Anti-category** | Argue against how the category normally sells. High risk, high ceiling, needs brand confidence. |

### Deliverable per concept

```
[Three-word name]
Gap:      which map cell this occupies, and why it's open
Angle:    which family
Idea:     one sentence
Hook:     the actual first line, written not described
Format:   static / video / UGC / carousel - and why this one
Producible: what the client needs to make it
Risk:     the specific reason this could fail
```

**The hook must be written, not described.** "A hook about durability" is not a hook. "This is the third year I've had it and it still doesn't wobble" is.

**Name the risk on every concept.** A concept list where everything is presented as a winner is a sales document, not a strategy document, and the buyer stops trusting it by concept four.

---

## Step 4 - Hand off

Concepts the client approves go into **`creative-brief`**, one brief per concept, with visual references sourced there. Do not deliver concepts and briefs in the same document - the client is making a *selection* decision at this stage, and a fully-briefed concept biases the choice toward whichever one you happened to develop.

Ad copy for approved concepts goes through **`meta-ad-copy`** or **`google-ad-copy`**.

---

## Step 5 - Validate before delivering

| Check | Fail = |
|---|---|
| Ad libraries actually searched, not recalled | Concepts describe last year's category |
| Category map delivered with saturated / long-running / absent / unhandled | No grounding for the ideas |
| Every concept names its gap | Guess presented as strategy |
| At least four distinct angle families | One idea delivered five times |
| Every hook is written, not described | Client cannot evaluate it |
| Every concept is producible with what the client has | Wasted concept |
| Every concept has a named risk | Sales document, not strategy |
| No dead concepts re-proposed | Wasted the client's memory |
| No pricing or commercial terms | Out of scope for team skills |

Then run **uni-output** before it leaves.

---

## Self-Improvement

At the end of every run, before ending:
1. Did any step fail or need a workaround?
2. Did the user correct or reject anything meaningful?
3. Did you discover something a future run might need?

Worth capturing specifically: an angle family that keeps winning for a particular vertical, and any competitor whose long-running ads are consistently worth studying. Both are reusable across clients. Propose changes as a diff for a pull request against `seant15/uni-team-skill` - never edit the installed copy.

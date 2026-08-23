# GOLDEN SAMPLE - Weekly Report

> **Status:** UNI house format, specified by Sean.
> **Format:** `text message`. One line per client. Slack or wherever the team reads.
> **This is a portfolio roll-up, not a per-brand report.** The monthly is the per-brand deep review. Never write one in the shape of the other.
> **Hard requirements at the bottom.**

---

## The format

One line per client. Nothing else.

```
[CLIENT NAME] $[spend] Spent @ [ROAS or CPA], [one sentence: what we are doing and why]
```

Three parts, always in this order:

1. **Who** - client name
2. **What it cost and what it returned** - spend, and the one efficiency number that matters for that client
3. **Where we are pointing it** - one sentence naming the direction: optimising what, scaling, or slowing down

That third part is the whole point of the document. Spend and ROAS are on the dashboard already. **What the reader cannot get anywhere else is what the buyer decided to do about it.**

---

## Worked example

```
WEEKLY - Aug 18-24

Voyara            $4.2k @ $87 CPL, cutting the two ad sets over $120 CPL and
                  moving budget into the medical-program funnel that is holding at $61.
Harlow Google     $9.8k @ 3.4x, scaling. PMax is carrying it, so pushing tCPA down
                  $5 this week to see if efficiency holds at higher spend.
Harlow Meta       $3.1k @ 2.1x, slowing down. Frequency hit 4.1 on the two winners
                  and we have no replacements until the new batch lands Thursday.
Nova Fitness      $6.4k @ $34 CPA, holding. Nothing to change until the LP test
                  finishes Friday - moving now would contaminate it.
Orbit Dental      $1.9k @ $210 CPL, optimising. Search terms are pulling in
                  cosmetic queries we do not serve; 40 negatives going in today.

Needs a decision: Harlow Meta creative - approve the emergency batch or accept
a slow week? @Sean by Tue.
```

Five clients, five lines, one ask. Under 8 lines of substance, which is the `uni-output` text-message ceiling.

---

## The one sentence

This is where weekly reports live or die. Four shapes, and every client gets exactly one:

| Direction | Says | Must include |
|---|---|---|
| **Scaling** | it works, we are pushing more through it | what is carrying it, and what the next increment is |
| **Optimising** | it works partly, we are cutting the part that does not | the specific thing being cut, with its number |
| **Slowing down** | something is degrading | what degraded, the number, and what unblocks it |
| **Holding** | deliberately not touching it | why touching it now would cost us |

**"Holding" is a legitimate answer and needs a reason.** A buyer who writes "holding" five weeks running is not holding, they are on autopilot, and the line should say so.

**Banned:** "monitoring", "looking into it", "performance is steady", "continuing to optimise". None of them name a decision.

---

## Which efficiency number

One per client, the one tied to their actual goal. Not both.

- **E-commerce** - ROAS
- **Lead gen** - CPL, and CPA on qualified leads if the client passes back qualification data
- **Local / appointments** - cost per booking, or cost per call if that is what gets counted

If the client's goal metric is not trustworthy this week (tracking gap, attribution change), **say that instead of the number.** `Orbit Dental $1.9k @ CPL unreliable, GA4 gap Aug 19-21, restating Monday` is a better line than a number nobody can act on.

---

## Cadence and use

Monday morning, covering the previous week. Buyer writes their own clients, lead assembles.

**One ask at the bottom, or none.** If three clients need decisions, that is three separate `[APPROVE]` messages per `text-message-update.md`, not three asks buried in a status roll-up.

**The weekly is not a monthly in miniature.** No moves log, no deep dive, no tables. If a week genuinely needs explaining at length, that is a separate message with the detail, linked.

---

## Hard requirements

1. **One line per client.** A client needing two lines needs a separate message.
2. **All three parts present:** name, spend at efficiency, direction sentence.
3. **The direction sentence names a decision**, not a state. Scaling, optimising, slowing down, or holding with a reason.
4. **One efficiency metric per client**, matched to their goal.
5. **An untrustworthy number is stated as untrustworthy**, with the reason and when it will be restated.
6. **Under 8 lines of substance.** Over that, it is a document.
7. **At most one ask**, at the bottom, with a person and a deadline. More asks means more messages.
8. **No pricing.** Media spend only.
9. **Zero em dashes and en dashes.** Hyphens only.
10. **Every client that spent money appears.** A client omitted because the week was bad is the one the reader most needs to see.

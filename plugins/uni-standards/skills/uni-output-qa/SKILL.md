---
name: uni-output-qa
description: Internal peer review of a teammate's draft against the UNI output standard. Use when someone asks to "review this before it goes out", "QA this report", "check this against our standard", "did I miss anything", or when a lead is signing off on a junior's deliverable. Returns scored, line-referenced feedback written TO THE PERSON so they learn the fix - it does not silently rewrite their work.
---

# UNI Output QA

This is peer review, not ghostwriting. Someone wrote something. Your job is to tell them what to change and why, at a level of specificity they can act on in ten minutes.

**The hard rule: do not rewrite the document.** Quote the line, name the problem, show one corrected version of that line, move on. The author fixes it. Rewriting robs them of the lesson and hides the pattern from whoever reviews them next.

The one exception: a factual error you can verify - a wrong date, a currency mismatch, a number that contradicts another number in the same doc. Flag those as P1 with the correct value, because those are facts, not craft.

---

## Step 1 - Establish what you're reviewing

Ask, unless already supplied:

**Interview gate.** Ask everything below in one batch, skip what is supplied, then lock the brief before producing. Never fill a gap with a plausible value. The full rule is in `uni-standards:uni-output` under *The interview gate*.


1. **Who wrote it and what's their level?** Feedback to a strategist and feedback to a new assistant are different documents.
2. **Who is the reader?** Client, prospect, or internal. A doc can be perfect for one and wrong for the other.
3. **Which of the three formats is it?** Notion, Google Doc, or text message.
4. **What's the deadline?** Determines whether you give the full teaching version or the triage version.
5. **Has it already been sent?** If yes, the review becomes a lesson for next time and a decision about whether a correction goes out.

Read the whole draft before writing a single note. Partial reviews produce contradictory feedback.

**Check the golden sample first.** `../uni-output/references/golden/` holds the approved example for each deliverable type. If one exists for this format, review against it - the gap between the draft and the sample is your note list, already written.

---

## Step 2 - Score it

Score each dimension 1-5. **3 is "ships." Below 3 is "fix before sending."**

| Dimension | 5 looks like | 1 looks like |
|---|---|---|
| **Answer-first** | Conclusion in paragraph one | Conclusion buried on page two, or absent |
| **Evidence** | Every figure has date range + source | Numbers float free, or "approximately" |
| **Density** | Every sentence changes a decision | Padding, restated headings, summary paragraphs |
| **Voice** | Plain, direct, no theater | AI slop patterns, hype adjectives, hedging |
| **Typography** | Hyphens only, no em or en dashes | Any `-` or `-` present |
| **Actionability** | Recommendations name action + object + owner | "Consider optimizing" |
| **Format discipline** | Correct one of the three formats, clean | Invented format, emoji, nested bullet swamp. *Exception: the monthly report flag key is permitted - see `uni-output`.* |
| **Correctness** | Names, dates, currency, math all check out | Any factual error |

Report the eight scores as a compact line, then the total out of 40. Do not soften a score to be kind - the score is the fastest signal the author gets.

---

## Step 3 - Write the feedback

Structure every note the same way. Three lines, no more:

```
[P1] Line 14 - "Performance was strong across the board."
Why: no number, and "strong" is our word not theirs. The reader can't verify it.
Fix: "ROAS hit 3.4 on Aug 1-21, up from 2.1 in July (Meta Ads Manager)."
```

**Severity:**
- **P1** - cannot send. Factual error, unsourced number, pricing content, missing conclusion, format violation, **any em dash or en dash**.
- **P2** - should fix. Slop patterns, padding, vague recommendations, weak headings.
- **P3** - worth knowing. Style preferences, better options, things that will matter on the next one.

**Cap the notes.** Maximum 8 notes for a full document. If there are more than 8, the draft has a structural problem, not a line problem - say that instead and name the one structural fix. Twenty line-notes teaches nothing; it just demoralizes.

**Then one line of praise, and make it specific.** "The campaign-level table is exactly right - it answers the question before the reader asks it." Generic encouragement is noise; a named strength is a thing they will repeat.

---

## Step 4 - Close with the pattern

End every review with a single sentence naming the **one habit** that, if fixed, removes the most notes next time.

> "Your recurring pattern is stating a judgment before the number that supports it. Flip the order and four of these six notes disappear."

That sentence is the actual deliverable. Everything above it is evidence for it.

---

## Output format

Deliver as a text message if there are 3 notes or fewer. Notion markdown otherwise. Never as a Google Doc - QA notes are internal and should not sit somewhere a client could stumble into.

Never send the review and the fixed draft together. The author fixes it.

---

## Self-Improvement

At the end of every run, before ending:
1. Did any step fail or need a workaround?
2. Did the user correct or reject anything meaningful?
3. Did you discover something a future run might need?

Only propose a change if it meaningfully improves the skill. Propose it as a diff for a pull request against `seant15/uni-team-skill` - never edit the installed copy, and never treat your own proposal as approved.

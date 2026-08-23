---
name: creative-brief
description: Write a creative brief a designer or editor can execute without asking follow-up questions - with visual references attached, not described. Use when briefing static ads, video ads, UGC, or a full creative batch, when handing work to a freelancer or in-house designer, or when a round of creative came back wrong and the brief was the reason. Interviews for brand and offer first, sources real visual references, and pulls text-overlay lines from meta-ad-copy.
---

# Creative brief

A brief fails in exactly one way: the designer has to guess. Every rule here exists to remove a guess.

**The non-negotiable: a brief without visual references is not a brief.** Words like "clean," "premium," "bold" and "modern" mean a different thing to every person who reads them. Two reference images settle in one second what three paragraphs cannot settle at all.

---

## Step 1 - Interview

Ask in one batch. Skip what the requester already supplied.

**Interview gate.** Ask everything below in one batch, skip what is supplied, then lock the brief before producing. Never fill a gap with a plausible value. The full rule is in `uni-standards:uni-output` under *The interview gate*.


### Brand

1. **What does the brand sell**, one sentence, in their words
2. **Brand assets** - logo files, fonts, hex codes, and whether there's a brand guideline document. Ask for the file, not a description.
3. **Two or three pieces of the brand's own creative they consider on-brand**, and one they consider off-brand. The off-brand one is often more informative.
4. **Hard visual rules** - colors that are banned, logo placement requirements, mandatory legal text

### The ad

5. **Platform and placement** - Meta Feed, Reels, Stories, YouTube, Google Display. Determines aspect ratio and how long the viewer looks.
6. **Format** - static, motion, UGC, carousel, testimonial
7. **Objective and funnel stage** - cold traffic needs a hook; retargeting needs a reason and an offer
8. **The offer** - what the click gets, exactly
9. **How many concepts and how many variants each** - "make some ads" is not a quantity
10. **Deadline and who executes it** - in-house designer, freelancer, editor, or AI generation. Changes the level of specification needed.

### The angle - required

11. **What is the single idea this creative carries?** One idea per concept. A creative carrying three ideas carries none.
12. **What does the viewer believe now, and what should they believe after?** This is the actual brief; everything else is execution.
13. **What has already been tested and what won or lost?** Losing creative is the highest-value input available.

### Register

14. **Elevated or sales, 1-5** - same dial as `meta-ad-copy`. Get a number. It determines whether the creative looks like a magazine page or a promotion.

**Stop and ask** if: there is no offer; the requester wants "a few options" with no angle specified; or the brand assets don't exist yet - that is a separate job that has to happen first.

---

## Step 2 - Source visual references

This is the step people skip, and it's the one that makes the brief work.

For each concept, attach **2-4 real images**. Sources, in order of preference:

1. **The brand's own past winners** - settles the argument fastest
2. **Meta Ad Library / Google Ads Transparency Center** - competitor and category ads currently running. Live ads beat mood boards because someone is paying to run them.
3. **The category's adjacent aesthetic** - if the register is elevated, the reference may come from editorial or product photography rather than from advertising

For every reference, state **what to take and what to ignore**:

> Reference 2 - take the lighting and the negative space on the left third. **Ignore** the color palette and the model. We are not shooting a person.

An unannotated reference is worse than none - the designer copies the wrong thing from it.

**If a reference cannot be sourced, say so explicitly in the brief** and describe the shot in physical terms instead - camera angle, distance, what's in frame, what light is doing. Never fall back to adjectives.

---

## Step 3 - Write the brief

**Read the golden sample first:** `uni-standards/skills/uni-output/references/golden/creative-brief.md`. It carries the full-batch structure with Asset IDs, the short form for a three-ad job, and the hard requirements for both. Match it.


One page per concept. If it runs to two, the concept has two ideas in it - split them.

```
CONCEPT [n] - [three-word name]

The idea
  One sentence. What this ad argues.

Belief shift
  Before: [what they think now]
  After:  [what they think after]

Visual
  What is in frame, from what angle, in what light.
  Physical description - not adjectives.

References
  [image] - take X, ignore Y
  [image] - take X, ignore Y

Text overlay
  [3-6 words]     ← from meta-ad-copy, see below
  Placement: [where, and why it doesn't collide with the subject]

Copy pairing
  Primary text and headline this creative runs with.
  Overlay and copy must carry DIFFERENT halves of the message.

Specs
  Ratio(s): [1:1 / 4:5 / 9:16]
  Safe zones: [platform-specific]
  Deliverables: [count and file types]

Do not
  [the two or three specific things that would make this wrong]
```

The **"Do not"** block prevents more revision rounds than any other section. Use it.

### Text overlay

**Always route overlay lines through `meta-ad-copy`.** Do not write them here. That skill holds the truncation rules, the brand register dial, and the cleared-claims check, and overlay text is subject to all three.

Two rules that live here:

- **Overlay and primary text must not say the same thing.** The overlay stops the scroll; the copy closes. If the overlay is the headline in a different font, one of them is wasted.
- **3-6 words.** If the idea needs 8, it isn't sharp yet - send it back to the angle, not to the designer.

### Variants

When briefing a batch, be explicit about **what varies and what is locked**. "Five variants" without this produces five unrelated ads and an untestable result.

> Locked: product shot, lighting, logo placement.
> Varies: overlay line only, five versions, one per hook angle.

---

## Step 4 - Validate before sending

| Check | Fail = |
|---|---|
| Every concept carries exactly one idea | Designer guesses which idea matters |
| 2-4 annotated visual references per concept | Adjectives doing a reference's job |
| Every reference says what to take and what to ignore | Wrong thing gets copied |
| Overlay lines came from `meta-ad-copy` | Untruncated, off-register, or uncleared claim |
| Overlay and copy carry different halves | Half the ad wasted |
| "Do not" block present and specific | Avoidable revision round |
| Ratios and safe zones stated per placement | Cropped logo, cut text |
| Deliverable count and file types stated | Ambiguous handoff |
| No pricing or commercial terms | Out of scope for team skills |

Then run **uni-output** before it leaves. A brief is a deliverable.

---

## Self-Improvement

At the end of every run, before ending:
1. Did any step fail or need a workaround?
2. Did the user correct or reject anything meaningful?
3. Did you discover something a future run might need?

Worth capturing specifically: any brief that still came back wrong, and the missing line that would have prevented it. That line belongs in the template. Propose changes as a diff for a pull request against `seant15/uni-team-skill` - never edit the installed copy.

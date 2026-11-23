---
name: creative-brief
description: Write a creative brief a designer or editor can execute without asking follow-up questions - with visual references attached, not described. Use when briefing static ads, video ads, UGC, or a full creative batch, when handing work to a freelancer or in-house designer, or when a round of creative came back wrong and the brief was the reason. Also the kickoff for a new creative task ("start a creative brief", "new creative task"). Interviews for brand and offer first, reads the client's Brand and Creative cards and recent creative tasks in ClickUp, sources real visual references, pulls text-overlay lines from meta-ad-copy, and files the approved brief as a ClickUp task.
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

### The client's standing cards - read them before you ask anything

If ClickUp is connected, open `Brand Card || Client Name` and `Creative Card || Client Name` in the client's `[UNI] DELIVERY` folder first. They are the one home for facts this interview would otherwise ask again (shared rule and full field map: `uni-standards:uni-output` -> *The interview gate* -> *The client's standing cards*):

| The card already answers | So skip or pre-fill |
|---|---|
| Brand Card: what the brand sells, products to push, audience priority, brand rules and claims wording | Questions 1 and 4, and the claims any overlay line may use |
| Creative Card: creative standard, Drive folder, raw footage links, good examples | Questions 2 and 3 |

Use what the card says and name the card as the source. Ask only for what is empty or missing. Do not edit a card from this skill: a wrong or empty cell goes back to the requester as a question. No cards yet, or no ClickUp connection: say so in one line and run the full interview.

### Past work in ClickUp - read it before you ask question 13

If ClickUp is connected, pull the last 5 tasks from the client's `Creative` list in their `[UNI] DELIVERY` folder before the interview batch goes out. Use them for three things:

- **Do not repeat a recent angle.** Name the angles already briefed, so the new concept is different on purpose.
- **Pre-fill question 13** with what those tasks say won or lost, and ask the requester to confirm it instead of asking cold.
- **Flag an open creative task on the same account.** Two live briefs for one offer is a question for the requester, not a choice.

No ClickUp connection, or no earlier creative tasks: say so in one line ("no prior creative history - this brief sets the baseline") and carry on. Never invent history.

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

### Format - a Google Doc by default, not markdown in a chat window

**Build a real Google Doc.** A requester who has to strip hash symbols and asterisks before the designer can read it is doing the last step of your job. Markdown or Notion only when they explicitly ask.

`docs_create` for the body as plain text, then `docs_formatText` for structure: **Heading 1** for the title, **Heading 2** per concept, **Heading 3** for `Do not`, the deadline and any hard rule, **bold** on field labels and on the overlay line itself. Fetch the Doc back with `docs_getText` before handing over the link, and paste a plain-text fallback into chat next to it.

Two limits of the tooling to design around, not to promise past:

- **No highlight colour** - bold, italic, underline and headings only. Heading 3 plus bold is the approved emphasis (decided 2026-09-08). Do not fake a highlight with brackets or caps.
- **No image embedding** - so the references in Step 2 ship as **annotated links**, and every one of them has to actually resolve. Check them. An unopenable reference is worse than none, because the designer works from memory instead.

The full contract is `uni-standards:uni-output` -> *The paid-media output contract* -> Contract 4.

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

**Run the gate first. It is a script, and it can refuse.**

```
python skills/uni-output/scripts/lint-ads-output.py <file> --type brief
```

It checks for a real Doc URL, markdown artifacts left in the body, a missing `Do not` block, reference links and dashes. Exit 1 means not deliverable. Fix every P1, re-run, and put `Lint: brief pass (P1=0, P2=n)` in the handoff. Everything below is what a script cannot judge.

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

## Step 5 - File it in ClickUp, after approval

Show the requester the finished Doc and wait for a yes. A brief nobody approved is a draft, and a draft in the designer's queue gets built.

On approval, if ClickUp is connected, create one task:

| Field | Value |
|---|---|
| List | The client's `Creative` list in their `[UNI] DELIVERY` folder |
| Name | `Creative | Brand name | Task title` - specific, for example "Summer sale static - 3 variants" |
| Description | The Doc link first, then the one-idea line per concept, deliverable count and deadline in plain text. No markdown symbols. |
| Due date | The deadline from question 10 |
| Status | `Process` |
| Assignee | Only the person the requester named. Otherwise leave it empty. |

Read the list's status names before you create the task; a status that does not exist fails the call. Confirm with the task link.

No ClickUp connection: hand back the Doc link and say the task was not created. Do not describe a task that does not exist.

---

## Self-Improvement

At the end of every run, before ending:
1. Did any step fail or need a workaround?
2. Did the user correct or reject anything meaningful?
3. Did you discover something a future run might need?

Worth capturing specifically: any brief that still came back wrong, and the missing line that would have prevented it. That line belongs in the template. Propose changes as a diff for a pull request against `seant15/uni-team-skill` - never edit the installed copy.

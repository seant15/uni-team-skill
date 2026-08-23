# GOLDEN SAMPLE - Team Communication (text message)

> **Status:** UNI house template, authored by Sean.
> **Format:** the `text message` format from `uni-output`. Slack and ClickUp flavours below.
> **This is the shortest of the three formats and the one used most.** Most internal failures are message failures, not work failures.
> **Hard requirements at the bottom of this file.**

---

**The rule: One message. One ask. Under 8 lines.**

If someone has to read your message twice to find out what you want from them, the message failed. Doesn't matter how polite it was.

---

## The 4-Block Structure

Every message that starts a thread has four blocks. Three of them are one line each.

```
[TAG]
Context:  Brand · Project/Campaign · [task link]
Situation: What's happening. Max 3 lines. Numbers, not adjectives.
Ask:      What you need + from who + by when.
```

That's it. If your message doesn't fit, it's not a message - it's a doc or a meeting.

---

## Block 1 - The Tag

Pick one. One message = one tag. If you need two tags, send two messages.

| Tag | Means | Reader knows instantly |
|---|---|---|
| `[HELP]` | I'm blocked or stuck | Someone needs to unblock me |
| `[APPROVE]` | I need a yes/no or a pick | A decision is waiting on you |
| `[IDEA]` | Thinking out loud, want a gut check | No action needed, just a read |
| `[MEET]` | I need synchronous time | Look at your calendar |
| `[FYI]` | Nothing needed from you | Read and move on |

`[FYI]` is the only tag allowed to have no ask. Everything else must end with one.

---

## Block 2 - The Context Line

**Mandatory whenever you open a thread cold.** If it's a reply inside an existing thread, skip it.

Format: `Brand · Project or Campaign · [link]`

```
Context: Acme Skincare · Meta Q3 Retargeting · [CU-8f2k91]
```

Nobody on this team is holding your task in their head. "The creative isn't working" is useless. *Which brand, which campaign, which creative, and where do I look* is the whole job of this line.

**Rule:** if there's a ClickUp task, the link goes here. No link = the reader has to go hunting = you've moved your work onto them.

---

## Block 3 - The Situation

Max 3 lines. Facts and numbers only.

- Numbers always carry a timeframe and a comparison. `CPA $41` means nothing. `CPA $41 last 7d, up from $28 the week before` is a sentence someone can act on.
- What you already tried goes here, in one line. It stops people suggesting the thing you did on Tuesday.
- No adjectives doing the work of data. "Performing terribly" → give the number.

---

## Block 4 - The Ask

The single most-skipped block and the reason most threads die.

Must contain: **what you need · who you need it from · by when.**

- "By EOD Tue" - always a real deadline. Never "asap," never "when you get a chance," never nothing.
- "Thoughts?" is not an ask. Name the decision: *"Kill it or give it 3 more days at $80/day?"*
- Give options where you can. A yes/no or an A/B gets answered in 10 seconds. An open question sits for a day.

---

## The Four Message Types (copy-paste)

### `[HELP]` - I'm blocked

```
[HELP]
Context: Acme Skincare · Google Search Brand · [CU-8f2k91]
Situation: Conversion tracking stopped firing Aug 18. GTM tag is live,
GA4 shows the event, Google Ads shows 0 since the 18th. Already
re-linked the accounts and re-imported the conversion.
Ask: @Mira - can you check the Ads conversion setup by EOD Mon? I'm
blocked on reporting until then.
```

### `[APPROVE]` - I need a decision

```
[APPROVE]
Context: Nova Fitness · Meta Prospecting · [CU-7d1x44]
Situation: UGC-03 is at $22 CPA over 14d / $3.1k spend vs account
average $34. Current budget $120/day, hitting frequency 2.4.
Ask: @Sean - approve scaling to $250/day starting Thu? Yes / No /
Scale to $180 instead. Need it by Wed 5pm to launch on time.
```

### `[IDEA]` - Gut check, no action needed

```
[IDEA]
Context: Acme Skincare · Meta account-wide
Situation: Our top 3 winners are all "before/after at 3 weeks."
Everything problem-first has flopped. Suggests the hook that works
here is proof, not pain.
Ask: @Sean - worth building the next 5 creatives entirely around
proof formats? Not urgent, just want a gut check this week.
```

### `[MEET]` - I need time

```
[MEET]
Context: Nova Fitness · Q4 planning · [CU-9a3b02]
Situation: Q4 budget nearly doubles and current structure won't
absorb it - need to agree on restructure before Oct 1.
Ask: @Sean @Mira - 30 min this week. Agenda: (1) CBO vs ABO,
(2) new market split, (3) who builds. Tue 10am or Thu 2pm?
```

---

## STRICTLY DON'T

Non-negotiables. These are the actual costs, not style preferences.

1. **No "hey, you there?" as a standalone message.** Ping-and-wait costs two round trips. Send the whole ask.
2. **No ask buried at the bottom of a wall of text.** Ask goes in the last block, clearly labeled - never hidden in paragraph four.
3. **No context-free openers.** "This isn't working" / "can you check this" / "the client is asking" - which brand, which campaign, which link.
4. **No bundling unrelated asks.** Four asks in one message = three of them get forgotten. Four messages.
5. **No naked screenshots.** Every image needs a caption saying what to look at and what's wrong.
6. **No asking what the task already answers.** Check the ClickUp task and the last report first. If the answer is there, you've cost someone else five minutes to save yourself one.
7. **No numbers without a timeframe and comparison.** Every metric carries a window and a baseline.
8. **No urgency inflation.** "URGENT" only when money is burning or a client is waiting today. Overuse it and it stops working - for everyone, permanently.
9. **No "any update?"** Restate the original ask and the date you asked. Bumps are fine; amnesiac bumps aren't.
10. **No DM for anything the channel needs to see.** Decisions made in DMs don't exist. Conversely - don't dump a 1:1 performance issue into a channel.
11. **No solving in the thread when it's a meeting.** Three back-and-forths without resolution = someone calls `[MEET]`.
12. **No emoji-only replies on anything with a dollar figure.** 👍 is not approval to spend $250/day. Type the word.

---

## Two Flavors

### Slack

Full 4 blocks, always. There's no task attached, so the context line does all the load-bearing work.

- Tag goes in the first line, plain: `[APPROVE]`
- Thread the follow-ups. Never restart a thread for the same topic.
- Reply in-thread; use "also send to channel" only for a resolution the room needs.
- Close the loop: when it's resolved, post the outcome in-thread and react ✅. An unclosed thread is an open task in someone's head.

### ClickUp (comments on a task)

The task already carries brand, campaign, assignee, and due date. So you drop the context line and lean on the fields.

```
[APPROVE]
Situation: UGC-03 at $22 CPA over 14d vs account avg $34, freq 2.4.
Ask: @Sean - scale to $250/day Thu? Y / N / $180. Need by Wed 5pm.
```

- Assign the comment to the person you're asking. An unassigned comment is a wish.
- Set the due date on the ask, not the task.
- Resolve the comment when it's answered. Don't reply "thanks" and leave it open.
- Decisions live in ClickUp. If a decision happened in Slack, paste it into the task - Slack is where things get discussed, ClickUp is where things become true.

---

## A Few Working Rules

**Response expectations.** `[HELP]` blocked → same day. `[APPROVE]` → by the stated deadline, and if you can't, say so in one line rather than going quiet. `[IDEA]` → within the week. `[FYI]` → never, that's the point.

**Silence isn't approval.** If your deadline passes without an answer, bump once, then escalate. Never spend money on an unanswered `[APPROVE]`.

**Escalation ladder.** Thread → bump at the deadline → DM the person → bring in Sean. Each step gets one attempt before the next.

**Length test.** If it takes more than 8 lines, you're writing a doc. Write the doc, link it, and put a 2-line summary plus the ask in the message.

**The rewrite test.** Before you hit send, read only your last line. Would a person who read nothing else know exactly what to do? If not, rewrite the ask.

---

## Hard requirements

1. **One message. One ask. Under 8 lines.** Over 8 lines means write the doc, link it, and put a 2-line summary plus the ask in the message.
2. **One tag per message.** Two tags means two messages.
3. **Context line whenever the thread opens cold.** Brand, campaign, task link. Skip it only inside an existing thread.
4. **Every metric carries a timeframe and a comparison.** `CPA $41` is not information.
5. **The ask names what, from whom, by when.** "Thoughts?" is not an ask.
6. **A real deadline.** Never "asap", never "when you get a chance", never nothing.
7. **Every screenshot has a caption** saying what to look at and what is wrong.
8. **No spending on an unanswered approval.** Silence is not approval.
9. **Emoji-only replies are never approval on anything with a dollar figure.** Type the word.
10. **Decisions live in ClickUp.** If it happened in Slack, paste it into the task.
11. **Zero em dashes and en dashes.** Hyphens only.
12. **The rewrite test before sending:** read only your last line. Would someone who read nothing else know exactly what to do?

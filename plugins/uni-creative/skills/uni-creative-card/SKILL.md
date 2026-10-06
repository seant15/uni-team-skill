---
name: uni-creative-card
description: >
  Fills a client's standing creative card: brand creative standard, Drive
  folder, raw footage with links, and a few good examples. Use when someone
  says creative card, creative standard, footage library, or where designers
  should pull assets. Retrieves first, asks once for anything with no source,
  then writes the full tab. Does not brief one ad and does not write ad copy.
---

# Creative card

Designers fail when the brand rule, the files, and the good examples live in different places. This card is that index. It is not a one-job brief.

This is not `creative-brief` (one execution brief, with a deadline and an assignee) and not `meta-ad-copy`. The numbers a buyer must not guess are `uni-brand-card`. On a new client, run both and write both tabs in the same update.

Read [references/schema.md](references/schema.md) before you write. That file is the lock.

## Step 1 - Retrieve, then one question batch

Search before you ask. Use the client Drive folder, the brand guideline, the creative planner, and the last brief. List footage from the folder you actually opened. Do not invent a file.

Required before a write:

- At least one creative rule
- The Drive folder, or a confirmed "there is no folder"
- Raw footage links, or a confirmed "there is no library"
- One good example, or a confirmed "there is none"

If any of those is missing, do not write the sheet. Send one message listing only the gaps. If you are also filling the brand card, put that skill's open cells in the same message.

An empty Drive search is not confirmation. Ask: "I did not find a footage library. Is there a folder I should use, or is there none?"

Do not clear a "confirm before overlay" claim yourself. Ask.

Workbook: in the private OS, read `memory/reference_uni-client-cards.md`. Anywhere else, ask once for the spreadsheet URL if it is not already in the thread. Do not create a second workbook.

## Step 2 - One write

Write only after the required pieces are sourced or answered.

New client: add `{Client} Creative` and, in the same update, the account tab from `uni-brand-card`. Do not edit existing tabs.

Existing tab: fill empty cells only. Never replace a value that is already there.

Links use `=HYPERLINK(url,"Open")`. No client email or phone. No evergreen-ban row.

## Step 3 - Check before you say it is done

- Four blocks, in order, with the columns in the schema.
- The removed row and the rights column are absent.
- No guessed file, quote, or claim.
- Filled cells on older tabs are unchanged.
- ASCII hyphen only.
- A new client has both tabs.

Then stop. Do not open `creative-brief` unless the user asks for a specific ad.

## Self-Improvement

At the end of every run, before ending:

1. Did any step fail or need a workaround?
2. Did the user correct or reject anything meaningful?
3. Did you discover something a future run might need?

Only propose a change if it meaningfully improves the skill. Propose it as a diff for a pull request against `seant15/uni-team-skill` - never edit the installed copy, and never treat your own proposal as approved.

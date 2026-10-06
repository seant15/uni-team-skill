---
name: uni-brand-card
description: >
  Fills a client's standing brand card in the review Google Sheet: account size,
  Target CPA, Target ROAS, AOV, seasonality, brand rules, and brand goal.
  Use when someone says brand card, account card, or lock the numbers a buyer
  must not guess. Retrieves first, asks once for anything with no source, then
  writes the full tab. Does not write ad copy or a one-job creative brief.
---

# Brand card

Buyers fail when they guess the target. This card is the only place those numbers are locked. A report target is not the card until the user says it is.

This is not `creative-brief` (one job for a designer) and not `ad-ideas`. The creative standard, Drive folder, footage, and examples are `uni-creative-card`. On a new client, run both and write both tabs in the same update.

Read [references/schema.md](references/schema.md) before you write. That file is the lock.

## Step 1 - Retrieve, then one question batch

Search before you ask. Use the review workbook, the client folder, the brand guideline, the last account brief, and any note the user already locked. ClickUp is a folder name only (`DELIVERY -> {Name}`).

Cite every filled cell in your own notes. Do not add a citation column to the sheet.

Required cells:

- Client
- Account size
- Target CPA
- Target ROAS
- AOV
- Seasonality
- Brand rules
- Brand goal

If any required cell has no source, do not write the sheet. Send one message listing only those cells. Skip anything already supplied or sourced. If you are also filling the creative card, put that skill's open gaps in the same message.

A weekly ROAS, a daily budget, or a case-study window is not an answer. Ask whether that figure is the card value.

If the user says to leave a cell blank, that is the answer. Write it empty.

Workbook: in the private OS, read `memory/reference_uni-client-cards.md`. Anywhere else, ask once for the spreadsheet URL if it is not already in the thread. Do not create a second workbook.

## Step 2 - One write

Write only after every required cell is sourced or answered.

New client: add `{Client} Account` and, in the same update, the creative tab from `uni-creative-card`. Do not edit existing tabs.

Existing tab: fill empty cells only. Never replace a value that is already there.

No client email or phone. No Deal row. Context notes are optional and must be sourced.

## Step 3 - Check before you say it is done

- The eight fields are present, in order, and the removed fields are absent.
- No number was guessed.
- Filled cells on older tabs are unchanged.
- ASCII hyphen only.
- A new client has both tabs.

Then stop. Do not open a creative brief.

## Self-Improvement

At the end of every run, before ending:

1. Did any step fail or need a workaround?
2. Did the user correct or reject anything meaningful?
3. Did you discover something a future run might need?

Only propose a change if it meaningfully improves the skill. Propose it as a diff for a pull request against `seant15/uni-team-skill` - never edit the installed copy, and never treat your own proposal as approved.

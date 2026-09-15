---
name: uni-google-doc
description: Build or restyle a UNI client Google Doc from the field-guide IR (kicker, title, deck, p/h/c/box/table). Use when uni-output format is Google Doc, or when creating, formatting, or fixing a Google Doc. Not for Notion, Sheets write, SEO approval packets (uni-2026-seo), or pixel-identical PDFs.
---

# UNI Google Doc

Without this skill, agents paste markdown into a Doc or guess character indexes. Headings look like body text, tables stay as pipes, and multi-tab documents get the wrong ranges. The Black Friday playbook looked right because the blocks were typed first and native styles were applied on a new single-tab Doc.

`uni-output` owns voice, interview, and the slop ban. This skill owns Doc structure. When format is Google Doc, `uni-output` loads this skill before any Docs write.

## Step 1 - Interview

Skip anything already locked by `uni-output`. Ask once for what is still missing:

1. New Doc, or which existing Doc URL
2. If the existing Doc has tabs: which tab to mutate
3. Audience and what they should do after reading
4. Must-include tables or checks

Stop and ask if the URL is missing on an edit, if two tabs could be the target, or if Sean asked for a designed PDF (that is a conversion, not this skill).

## Step 2 - Write the IR

Read `references/ir.md`. Produce JSON with `title`, optional `kicker` / `deck`, and `sections[]` of `p` / `h` / `c` / `box` / `table`. One idea per `p`. Headings are claims. Numbers in tables. Then read `references/apply.md` and run it.

New Doc: skeleton insert into a **new single-tab** file, then apply from `documents.get`. Existing Doc: live paragraph match on the named tab only.

## Step 3 - Validate

| # | Check | P1 fail = |
|---|---|---|
| 0 | Zero em dashes or en dashes | Any `—` or `–` |
| 1 | `documents.get` ran after the last write | Styles claimed from `docs_getText` or from a local file |
| 2 | `title` is `TITLE`; section heads are `HEADING_1`/`HEADING_2`; `h` blocks are `HEADING_3` | Those lines are `NORMAL_TEXT` |
| 3 | Every IR table is a native Docs table | Pipe characters remain |
| 4 | No `###`, `**`, or emoji | Markdown artifacts in the Doc |
| 5 | Chat has the Doc URL plus a plain-text fallback | Link-only handoff |
| 6 | Apply script exit 0, or an explicit "unstyled, script could not run" | "Formatted" with no readback |

Then run `uni-output` Step 4 on the prose. SEO packets stay on `uni-2026-seo`.

## Self-Improvement

At the end of every run, before ending:
1. Did any step fail or need a workaround?
2. Did the user correct or reject anything meaningful?
3. Did you discover something a future run might need?

Only propose a change if it meaningfully improves the skill. Propose it as a diff for a pull request against `seant15/uni-team-skill` - never edit the installed copy.

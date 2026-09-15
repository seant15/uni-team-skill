# Apply a UNI Google Doc

Read this when you are about to create or restyle a Doc. The IR is in `ir.md`.

## What you may not do

- Guess `startIndex` from a local txt / markdown file.
- Call `docs_formatText` with indexes you counted in the chat window.
- Trust `docs_getText`. It returns plain text. It cannot prove `namedStyleType`.
- Write into a multi-tab Doc without a live `tabId` from `documents.get`.
- Collapse tabs because the URL has `?tab=`.
- Paste `###` or `**` or `| col | col |` into the finished Doc.

## Route

| Situation | Do this |
|---|---|
| New client-facing Doc | Create a **new single-tab** Doc. Render the IR as plain text. Insert it. Then apply styles from a fresh `documents.get`. |
| Existing single-tab Doc you own | `documents.get`, match **whole paragraphs**, apply, get again. |
| Existing multi-tab Doc | Get every tab id and title first. Mutate only the tab Sean named. Same whole-paragraph match. If Sean did not name a tab, stop and ask. |
| SEO approval packet | `uni-2026-seo` `client-doc-format.md`. Do not replace that path. |
| Codex session with the OpenAI `google-docs` skill loaded | Use that skill for `batchUpdate` mechanics. Still fill the UNI IR first. Do **not** put UNI client files in the ChatGPT Drive folder. |

Cursor Workspace MCP can create a Doc and apply `heading1`-`heading6` / bold / italic. It cannot set `TITLE` or `SUBTITLE`, cannot insert a native table, and cannot read `namedStyleType`. For a UNI deliverable, run the apply script after create.

## Script

`scripts/apply-google-doc.mjs`

Needs Node, `googleapis`, and OAuth tokens at `~/.google-workspace-mcp/tokens.json`. Credentials: `GOOGLE_CREDENTIALS_PATH`, or `~/.google-workspace-mcp/oauth-client.json`. No machine-specific paths in the skill.

From a checkout that already has `googleapis` (Agentic OS: `tools/google-workplace-mcp`):

```
node skills/uni-google-doc/scripts/apply-google-doc.mjs --ir path/to/ir.json --document-id ID [--tab-id TAB]
node skills/uni-google-doc/scripts/apply-google-doc.mjs --ir path/to/ir.json --skeleton
```

`--skeleton` prints the plain-text body for `docs_create` / `docs_writeText`. Then pass the new document id to the same script without `--skeleton`.

The script:

1. `documents.get` with `includeTabsContent`
2. Applies `namedStyleType` by live paragraph `startIndex` (order after a skeleton insert, exact paragraph text on an existing Doc)
3. Turns leftover pipe tables into native tables, header row bold
4. Checkbox bullets on `c` blocks; shading on `box` blocks
5. `documents.get` again and prints style counts. Exit 1 if expected TITLE / HEADING_* / TABLE counts miss

## After apply

Handoff must include:

- Doc URL
- Style readback line, e.g. `Doc styles: TITLE=1 HEADING_1=6 HEADING_3=12 TABLE=8 P1=0`
- Plain-text fallback in chat

If the script cannot run (no tokens, Cowork-only), stop. Do not guess indexes. Give Sean the IR JSON and the skeleton, and say the Doc is unstyled.

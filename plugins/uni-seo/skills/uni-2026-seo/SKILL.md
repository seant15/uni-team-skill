---
name: uni-2026-seo
description: >
  UNI 2026 client SEO approval packet. Intake a Google Sheet or Drive
  draft folder, run the SEO gates, lock a local draft, then build a
  client-facing Google Doc with headings, real tables, and brand photos.
  Use when someone says client approval doc, SEO approval packet, from
  the Google Sheet, rewrite this blog for the client, or /uni-2026-seo.
  Never publish. Not a live WordPress or Shopify push.
---

# uni-2026-seo

A client-facing SEO draft that still looks like a markdown paste is not a packet. This skill turns a Sheet or Drive folder into a Doc the client can approve. It stops at draft. It never publishes.

Route the finished Doc through `uni-standards:uni-output` before anyone sends it.

## Step 1 - Interview

Ask in one batch. Skip what is already in the thread. Never invent a site URL, a price, or a claim the live page does not print.

**Interview gate.** The full rule is in `uni-standards:uni-output` under *The interview gate*.

1. **Brand and public site URL**
2. **CMS** - Shopify, WordPress, or other
3. **Source** - Google Sheet, Drive folder of drafts, or both. Get the link, not a description
4. **Job** - new URL, rewrite a live URL, or salvage a rejected draft
5. **Queries to win, and queries the money page already owns** - a blog must not steal a product page
6. **Photo source** - official site only, a named Drive folder, or PHOTO NEEDED. No stock pretending to be first-hand
7. **Competitor names on the client Doc** - default no, unless the requester writes yes
8. **Where to lock the local file** - client workspace `seo/locked/` if that tree exists

**Stop and ask** if: there is no site URL; there is no source Sheet or Drive; the requester asks to publish or set a CMS status to live; or the target is a site whose weekly SEO loop is a different OS skill (do not run this packet on that loop).

## Step 2 - The work

Read `references/client-doc-format.md` and `references/seo-gates.md` before writing.

1. Confirm the site. Fetch the live homepage and any URL you will rewrite. Do not write against the wrong domain.
2. Pull the source. Sheet = outline, GSC, or calendar. Drive = full drafts. Read every file. Do not guess from titles.
3. Lock official facts from live product and support pages only: price, size, output, warranty, support hours. Do not invent a certification, a lab test, a first-hand review, or an invoice the team never saw.
4. Pick URLs with Search Console, not vibes. If an existing URL already ranks for the query, rewrite it. If a product page already owns the query, do not open a blog that steals it. Do not launch another "best of" on a cluster you already hold.
5. Write the local lock first (`seo/locked/` when that folder exists). Body copy uses the hyphen `-` only. Client-visible body has no `YYYY-MM-DD` timestamps. Machine dates in JSON-LD stay in the lock file, not on the client Doc.
6. Run the gates in `references/seo-gates.md`. Fail = do not build the client Doc.
7. Build the Google Doc with the Docs API (headings, real tables, inline images). Workspace MCP can create and move files. It cannot be the final layout. Do not paste markdown into the Doc.
8. Polish: hyperlinks on body product names, official pages, sources, phone, and email. No links on Meta Title, Meta Description, Keywords, Target Keyword, Search Intent, or any line that contains `Alt:`. Rename schema dumps and gate logs INTERNAL. Send only CLIENT REVIEW.

## Step 3 - Validate before delivering

| Check | Fail = |
|---|---|
| Site URL matches the live site you fetched | Packet goes to the wrong brand |
| Every price and spec is on a live official page | Invented catalog |
| No new URL that cannibalizes a live owner | Two pages split one query |
| Client Doc uses Heading 1/2/3, real tables, real images | Markdown paste |
| Meta five fields and Alt lines have no links | Client sees blue keywords in the header |
| Hyphen only, no em dash, no en dash | House typography fail |
| No ISO date stamp in client-visible body | Stale "as of" line |
| FAQ is H2/H3, schema is not FAQPage / HowTo / ItemList | Gate fail |
| Zero first-hand tests labeled draft only | "Safe to publish" lie |
| Routed through uni-output | Slop or em dash slips the send |

Tell the requester: CLIENT REVIEW URL, local lock path, gate result, still draft only. Never say safe to publish.

## Self-Improvement

At the end of every run, before ending:
1. Did any step fail or need a workaround?
2. Did the user correct or reject anything meaningful?
3. Did you discover something a future run might need?

Propose changes as a diff for a pull request against `seant15/uni-team-skill` - never edit the installed copy.

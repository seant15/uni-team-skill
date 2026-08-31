---
name: uni-2026-seo-client-doc-format
description: Client-facing Google Doc rules for UNI 2026 SEO approval packets
---

# Client approval Doc format

Do not paste markdown into a Google Doc. The client sees headings, real tables, real images, and clickable links.

## Build

1. Workspace tools can create an empty Doc, move it, and rename it. Final layout uses the Docs API `batchUpdate`.
2. Put it in the shared client folder. Title starts with `CLIENT REVIEW`.
3. Gate logs, JSON-LD dumps, and strategy notes go in a second Doc titled `INTERNAL`. Send only CLIENT REVIEW.

## Styles

- One Heading 1. That H1 is the target query.
- Sections are Heading 2. Questions are Heading 3.
- Comparisons use `insertTable`. Bold gray header row. Do not style an empty cell (the API returns 400).
- Images use `insertInlineImage`. Next line is plain text: `Caption. Alt: ...`
- On write-quota 429, wait about 70 seconds and retry. Finish one Doc before starting the next.

## Links

- Body: product names, official pages, authority sources, phone, email
- Meta Title / Meta Description / Keywords / Target Keyword / Search Intent: no links
- Any caption that contains `Alt:`: no links
- Longest phrase first so short names do not eat longer ones

## Punctuation and dates

- Hyphen `-` only. No em dash (U+2014). No en dash (U+2013). Same rule as `uni-output`.
- Client-visible body has no `YYYY-MM-DD` timestamps. Write "checked on {site}", not a retrieval date.
- `datePublished` belongs in the local lock / JSON-LD, not on the client Doc.

## Photos

- Official site images, or a Drive folder the requester named
- Skip text-overlay, claim, or poster versions
- If there is no approved photo, leave PHOTO NEEDED. Do not use stock as first-hand evidence.

## Default copy locks (change only if the requester writes it)

- Do not name competing brands on the client Doc
- Do not invent certifications, lab tests, install times, or unaudited invoices
- Health or dental pages need "this is not medical advice" plus linked sources
- FAQ is headings. JSON-LD must not use FAQPage, HowTo, ItemList, MedicalWebPage, or an invented ratingValue

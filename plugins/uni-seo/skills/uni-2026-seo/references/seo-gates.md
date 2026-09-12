---
name: uni-2026-seo-gates
description: Portable SEO gates. SpeakerVerdict scripts win when that repo is on the machine.
---

# SEO gates

These gates are the packet, not decoration. Fail = do not build the client Doc. Fail = never say publish.

## Always (every machine)

- Draft only. Do not set Shopify, WordPress, or any CMS status to live.
- Do not invent first-hand tests, photos, scores, or `ratingValue`.
- FAQ in the article is H2/H3. Structured data must not use FAQPage, HowTo, or ItemList.
- Do not add MedicalWebPage on a health rewrite.
- `llms.txt` is not a deliverable for this packet.
- JSON-LD, if present, uses `@graph` plus stable `@id`. Missing schema is not an error. Invented schema is.
- Every price in schema also appears in visible body text.
- Zero first-hand evidence: label the packet draft only and say what is still missing.

## When SpeakerVerdict / UNI Agentic OS is on this machine

Those scripts are the hard gate. Do not relax them for a prettier Doc.

Run, if the files exist:

- `seo-content-qa` in SpeakerVerdict mode (draft only, never "safe to publish")
- `ventures/082026 speakerverdict/ops/qa/content_verify.py`
- `ventures/082026 speakerverdict/ops/qa/slop_score.py`
- `ventures/082026 speakerverdict/ops/seo/validate_schema.py`
- `ventures/082026 speakerverdict/ops/seo/citability.py`

Conflict table (SV wins):

| Topic | Softer SEO advice | SV / this packet |
| --- | --- | --- |
| FAQ schema | Some GEO guides allow FAQPage | Banned |
| llms.txt | Some GEO guides treat it as a lever | Weight 0, not a deliverable |
| Publish | Generic SEO pipelines go live | Stop at draft |
| First-hand evidence | Optional on a client brochure | Required to publish; missing = draft only |
| Client Doc dates | Dated claims in the visible body | Visible body has no ISO stamp; schema may keep machine dates |

If the target site is the SpeakerVerdict weekly blog loop, stop this skill. Use that site's weekly SEO skill instead.

## Tools

- Google Workspace: search Drive, read Sheets, read Docs, move and rename
- Docs API + Drive API (same OAuth as Workspace): tables, images, precise links. Token stays in the machine store. Never write secrets into a skill file.
- Fetch live PDPs and cited sources. Do not cite a page you did not open.
- Do not use a page builder or image generator to fill PHOTO NEEDED

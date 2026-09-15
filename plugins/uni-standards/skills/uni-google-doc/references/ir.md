# IR - field guide blocks

The Black Friday playbook was a 9-page field guide drawn by ReportLab, then a native Google Doc. The reusable part is the block list, not the PDF page chrome (orange bar, `02 / 09` footer, fixed page breaks). Those belong to a PDF conversion and need Sean's explicit go-ahead.

Write the deliverable as this JSON before touching Docs. Hyphen `-` only. No em dash, no en dash, no markdown hashes, no `**`.

```json
{
  "title": "Make More of Your Black Friday Traffic",
  "kicker": "UNI MARKETING AGENCY  /  FASHION EDITION  /  2026",
  "deck": "Four sales opportunities worth finding before your next promotion",
  "sections": [
    {
      "kicker": "01 / START HERE",
      "heading": "Map People Before You Map Promotions",
      "headingLevel": 1,
      "deck": "ONE PRIMARY MESSAGE PER PERSON, AT EACH MOMENT",
      "blocks": [
        { "type": "p", "text": "One idea. Three sentences or fewer." },
        { "type": "h", "text": "Keep the groups clean" },
        { "type": "c", "text": "A check the reader can mark done." },
        { "type": "box", "text": "START WITH COVERAGE. The load-bearing warning." },
        {
          "type": "table",
          "headers": ["Priority group", "Message and destination"],
          "rows": [["VIPs and repeat buyers", "Early access. Send to the member collection."]]
        }
      ]
    }
  ]
}
```

## Fields (from the 2026-09-13 script)

| IR field | BF script | Google Doc named style / treatment |
|---|---|---|
| `kicker` | `kick` on each page (`01 / START HERE`) | `NORMAL_TEXT` |
| `title` | `title` (may contain a line break in PDF) | `TITLE`. One document title. Flatten line breaks to a space. |
| `deck` | `deck` (ALL CAPS subtitle) | `SUBTITLE` |
| `sections[].kicker` | page kicker | `NORMAL_TEXT` |
| `sections[].heading` | page title | `HEADING_1` (or `HEADING_2` if `headingLevel` is 2) |
| `sections[].deck` | page deck | `NORMAL_TEXT`, bold |
| `p` | `p()` | `NORMAL_TEXT` |
| `h` | `h()` | `HEADING_3` |
| `c` | `c()` checkbox | `NORMAL_TEXT` + checkbox bullet |
| `box` | `box()` tinted callout | `NORMAL_TEXT`, italic, paragraph shading `#EDF2F1` |
| `table` | `table(headers, rows, widths)` | native Docs table, bold header row. `widths` are PDF-only; omit them |

Cover line `UNI / FIELD GUIDE` and the page footer are PDF chrome. Do not fake them with markdown or emoji.

## Palette (reference only)

From the BF script. Docs gets heading styles + callout shading. Do not promise full PDF colour on every paragraph.

| Token | Hex | Use |
|---|---|---|
| INK | `#182A32` | body (Docs default is fine) |
| MUTED | `#52666D` | kicker in PDF |
| ORANGE | `#C95021` | PDF accent. UNI web accent is `#E85D04`. Do not recolour the whole Doc unless Sean asks. |
| PAPER | `#FAFAF8` | PDF page |
| TINT | `#EDF2F1` | callout shading |
| LINE | `#CFDAD7` | PDF rules |

## Do not put in the IR

- Pipe tables as a `p` string
- `###` or `**`
- Character indexes
- Tab ids (those come from `documents.get`)
- Pricing

# Brand card schema

Locked 2026-10-06. Do not add a column or a field that this file does not list.

## Tab

- Tab name: `{Client} Account`
- Row 1: `{Client} - Account card`
- Row 2: blank
- Row 3: `Field` | `Value`
- No Status column. No Source column.

## Fields, in this order

1. Client
2. Account size (Small / Medium / Large)
3. Target CPA
4. Target ROAS
5. AOV (average order value)
6. Seasonality
7. Brand rules
8. Brand goal

`Brand goal` is the field the buyer treats as the number or outcome the client cares about. Do not rename it back to a longer label.

## Removed. Do not add these back.

- Gross margin
- Daily budget cap
- Conversion lag
- What the client approves
- Deal, including as a context row

## Context

After the fields, one blank row, then:

- `Context (not the account card)`
- `Item` | `Note`

Allowed notes, only when a source states them: platforms, site, store, ClickUp as `DELIVERY -> {Name}`, a weekly-check line, a proof window.

Do not put a client email or phone on the sheet.

A weekly-check target, a case-study ROAS, or a daily budget stays in Context. It becomes Target CPA, Target ROAS, AOV, or Brand goal only after the user confirms that exact value in this run.

## Write rules

- Sheet language is English.
- ASCII hyphen only. No em dash. No en dash.
- New client: add this tab and the creative tab. Do not edit any other tab.
- Existing tab: write empty cells only. Never replace a cell that already has a value.
- A conflict between a source and a filled cell is a question, not an overwrite.
- Do not create a second workbook.

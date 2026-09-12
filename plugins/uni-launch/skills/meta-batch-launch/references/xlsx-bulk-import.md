# XLSX Rail - Meta Native Bulk Import

No API, no developer app, no connector. The buyer imports a workbook in
**Ads Manager → Import & Export → Import ads in bulk**. Works on any account the buyer can
already log into - including client accounts UNI has no API access to.

## The core mechanic

Meta processes the file **row by row**, and the ID columns decide the operation:

- **ID column blank → create a new object**
- **ID column filled → update that existing object**
- One file can mix both.

To edit existing ads: export them first, change cells, keep the ID values, re-import.
To clone a structure: export, **clear every ID column**, swap account-specific IDs, import.

## Column reference

Header names must match Meta's export exactly - **trimmed, no stray whitespace**. The
safest way to get current headers is to export one valid ad from the target account and use
that file as the template. The list below is the working set.

### Campaign level
| Column | Notes |
|---|---|
| Campaign ID | blank = create |
| Campaign Name | follow the naming convention |
| Campaign Objective | `OUTCOME_SALES` `OUTCOME_LEADS` `OUTCOME_TRAFFIC` `OUTCOME_ENGAGEMENT` `OUTCOME_AWARENESS` `OUTCOME_APP_PROMOTION` |
| Campaign Status | `ACTIVE` or `PAUSED` - **always `PAUSED` on first import** |
| Buying Type | `AUCTION` (or `RESERVED`) - immutable once set |
| Campaign Daily Budget / Campaign Lifetime Budget | whole-number minor units, no currency symbol. Fill only for CBO |
| Campaign Bid Strategy | |
| Special Ad Categories | leave blank only if genuinely none apply |

### Ad set level
| Column | Notes |
|---|---|
| Ad Set ID | blank = create |
| Ad Set Name | |
| Ad Set Daily Budget / Ad Set Lifetime Budget | **leave blank if the campaign uses CBO** |
| Ad Set Run Status | |
| Start Time / End Time | ISO 8601 |
| Optimization Goal | `OFFSITE_CONVERSIONS` `LINK_CLICKS` `REACH` `IMPRESSIONS` `THRUPLAY` `LEAD_GENERATION` |
| Billing Event | `IMPRESSIONS` `LINK_CLICKS` `THRUPLAY` |
| Pixel ID | required for conversion optimization |
| Conversion Event · Conversion Window | |
| Countries · Cities · Age Min · Age Max · Gender · Locales | |
| Interests · Custom Audiences · Excluded Custom Audiences | IDs must exist in this account |
| Placements · Device Platforms | |

### Ad level
| Column | Notes |
|---|---|
| Ad ID | blank = create |
| Ad Name · Ad Status | |
| Title | headline |
| Body | primary text |
| Link | must include `https://` |
| Image Hash **or** Video ID **or** Image File Name | see creative rules below |
| Display Link · Caption · Description | |
| Call to Action | button type |
| URL Tags | UTMs |
| Page ID · Instagram Account ID | |

### Legal objective ↔ goal ↔ billing combinations

Meta rejects illegal combinations at row level. Rather than memorising the matrix: **export
one working ad in the target objective from the account and copy its Optimization Goal and
Billing Event values.** That is the only reliably current source.

Common working pairs:
- `OUTCOME_SALES` → `OFFSITE_CONVERSIONS` / `IMPRESSIONS`
- `OUTCOME_LEADS` (on-site form) → `LEAD_GENERATION` / `IMPRESSIONS`
- `OUTCOME_TRAFFIC` → `LINK_CLICKS` / `IMPRESSIONS` or `LINK_CLICKS`
- `OUTCOME_AWARENESS` → `REACH` / `IMPRESSIONS`

## Creative: three ways in

1. **Image Hash / Video ID** - reference assets already in the account's library. Fastest,
   and the only option that guarantees no upload failure. Hashes are **account-specific**.
2. **Image File Name** - upload new files alongside the workbook. Filenames must match the
   cell value **character-for-character, extension included, case-sensitive**. This is the
   single most common cause of failed imports.
3. **Zip upload** - bundle every referenced file into one archive alongside the workbook.

**Keeping social proof:** a bulk-created ad is a *new* post and starts at zero likes and
comments. To carry engagement across ad sets, reference the existing **post ID** instead of
rebuilding the creative.

## File limits

Reported limits differ by source and by account (Meta has changed them). Treat these as the
safe working envelope rather than gospel, and verify against the current Ads Manager screen:

- Keep each file to **1,000-2,000 rows** and split larger batches
- Keep file size small - older guidance cites a ~2 MB XLSX cap, newer cites 50 MB
- Several hundred ads per file is the practical comfortable ceiling

If a file is rejected on size or row count, split it. Do not fight the limit.

## Warnings vs errors

- **Warnings** let the import proceed (e.g. "placement not available for this objective").
  Read them anyway - a swallowed placement warning is how Advantage+ silently overrides a
  manual placement selection.
- **Errors** block the import, and are row- and column-specific. Fix and re-upload.

Always read the summary count of created objects after import and reconcile it against the
build plan before publishing.

## Cross-account cloning

1. Export the source structure
2. Clear **Campaign ID, Ad Set ID, Ad ID**
3. Replace: Page ID · Pixel ID · Instagram Account ID · Custom Audience IDs · Catalog ID
4. Re-upload creative assets to the destination account (hashes do not transfer)
5. Import as `PAUSED` and QA before activating

Learning-phase data, post engagement, and account-level optimization signals **do not
travel between accounts**. A cloned structure is a fresh start, not a warm one.

## What the XLSX rail cannot do

- Edit immutable fields (Campaign Objective, Buying Type)
- Preserve post engagement on duplicated creative
- Select video thumbnail frames (URL only)
- Fully express the newest Advantage+ / Catalog DCO configurations - those need the UI
- Fine-grained Dynamic Creative variant selection beyond supplying the variants

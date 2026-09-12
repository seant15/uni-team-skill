# Worked example - a clone-and-extend launch

A real launch, anonymised. Client is "Client A", a DTC jewellery brand. Every id is fake. The
sequence, the failures and the decisions are exactly as they happened, on 2026-09-11.

## The brief

> Duplicate the current ad set in this campaign and launch a few new ads with our naming template.
> Confirm the ad copy before we launch, pull an ad from the same campaign as a template, UTM needs
> to be there. Creatives are in this folder.

Seven files: four videos, three images.

## What the interview surfaced

Reading the account first, before asking anything, changed the shape of the job:

| Found | Consequence |
|---|---|
| Campaign is CBO at $100/day, one ad set, **12 ads already active** | Adding a second ad set splits a committed budget across 17 ads. Meta delivers 3 to 6 per ad set |
| The 12 existing ads use a **four-segment** name; the brief specified three | Two conventions would coexist. Raised, not silently resolved |
| The template ad uses a DOF asset feed - three primary texts, three headlines | "Same copy" was ambiguous and needed an explicit answer |
| Template `url_tags` are all Meta dynamic variables | Reusable verbatim. No UTM hand-editing at all |

The buyer was shown the budget arithmetic and chose to proceed without raising it. That decision
was recorded in the launch record rather than argued twice.

Two of the seven creatives were cancelled at this stage. They were never built, and their assets
were never referenced.

## Where it actually broke

**1. The MCP had no cloud-storage authorisation.** The folder upload failed outright. The agency's
own Drive connector is a different authorisation from the ad MCP's. Fixed by the user in a minute,
but it stops the launch cold until they do it.

**2. All four videos failed as "format isn't supported".** Not a codec problem. The files had been
uploaded to Drive **without file extensions** - `fileExtension: ""` against `mimeType: video/mp4`.
Meta types the upload from the filename. Fixed by uploading each file individually with an explicit
`filename` ending `.mp4` and `mime_type: video/mp4`. Re-encoding would have wasted an hour.

**3. Creative enhancements silently came out all opted out.** The template ad had ten Advantage+
features opted in. Caught on readback, before activation, by diffing the new creative against the
template. The buyer chose to ship with enhancements off so the approved copy ran verbatim - a
valid choice, made knowingly, and written down because it confounds the comparison against the
existing ads.

## The sequence that worked

```
duplicate_adset   include_ads=false, status PAUSED
update_adset      rename, because the suffix left two dates in the name
upload images     -> image_hash, synchronous
upload videos     one at a time, explicit filename + mime_type -> video_id
poll video status until ready
bulk_create_ad_creatives   url_tags lifted verbatim from the template ad
bulk_create_ads            status PAUSED
read back                  names, status, copy, UTM, CTA, landing URL
bulk_update_ads            status ACTIVE
update_adset               status ACTIVE
```

Five ads live. Elapsed time was dominated entirely by the two asset failures, not by the building.

## What it cost to learn

| Lesson | Where it now lives |
|---|---|
| Cloud-storage auth is separate and blocks everything | `asset-ingestion.md` |
| Missing file extension reads as a codec error | `asset-ingestion.md`, `troubleshooting.md` |
| Enhancements are never inherited | `SKILL.md` Step 2, `meta-build-limits.md` |
| `duplicate_adset` drags the old ads along by default | `SKILL.md` Step 2 |
| `tracking_specs` inherit correctly and need no help | `SKILL.md` Step 2 |
| Adding an ad set to a live CBO splits a committed budget | `naming-and-matrix.md` |

# Asset Ingestion - getting creative files into Meta

Rail: Meta's official ads MCP (`https://mcp.facebook.com/ads`, the "Facebook Ads" connector in
Claude). Tool names and limits below are taken from that server's own tool descriptions,
checked 2026-11-13. Not yet exercised end to end on a live batch; treat the first API launch as
the verification run and log anything that differs in `troubleshooting.md`.

The step that breaks most often on a real batch launch. Read this before promising a timeline.

## The core constraint

The MCP is hosted by Meta. It cannot read files on a laptop, in a Drive folder, or in the
model's workspace by path. Every asset reaches Meta by one of:

| Route | Tools | Works for |
|---|---|---|
| Public URL | `ads_creative_upload_media` with `upload_source=URL`, `media_type`, `media_url` | assets already on a public CDN |
| File the model can read (sandbox, or downloaded from Drive / Dropbox / Canva first) | `ads_create_upload_url` -> `curl` POST the bytes -> `ads_finalize_upload` | private client files. The default route |
| Local file picked by the user | `ads_creative_upload_media` with `upload_source=LOCAL_FILE` (only where the client shows MCP Apps) | one-off uploads from the user's machine |

Limits on the upload-URL route: images up to 30 MiB, videos up to 100 MiB, one URL per file,
MIME types `image/jpeg`, `image/png`, `image/gif`, `video/mp4`, `video/quicktime`.

Drive, Dropbox and Canva **share links do not work as `media_url`**: they return a sign-in page
or an HTML interstitial, not the bytes. Download the file with the Drive connector (or ask for
it), then use the upload-URL route.

Client creative is not made public to work around this. If no private route is available, say so
and ask where the assets can be put, rather than sharing a client's folder to the open web.

## Trap 1: files without an extension

Assets exported straight into Google Drive often arrive with **no file extension** - Drive
metadata shows `fileExtension: ""` even though `mimeType` is `video/mp4`. Meta types uploads from
the name. On the upload-URL route pass the real name with its extension and the MIME type
yourself:

```
ads_create_upload_url(ad_account_id=..., file_name="CLIENT_Ad_Name.mp4",
                      mime_type="video/mp4", file_size=<bytes from stat>)
```

Rename the downloaded file to carry the extension before you stat and upload it. Tell the editor
to keep extensions on export - it saves a round trip next time.

## Trap 2: one file per URL, one finalize per token

Each `ads_create_upload_url` call is good for one file. Each `completion_token` is finalized once.
Finalizing a video twice creates two videos: if a video finalize fails without a clear error,
check `ads_get_ad_videos` for the file name before calling it again. URLs expire (`expires_at`);
ask for a new one rather than reusing.

## Videos process asynchronously

`ads_finalize_upload` returns an image `hash` straight away, but a video comes back as
`video_id` with a `video_status` that is still transcoding. Poll
`ads_get_ad_videos(ad_account_id, video_ids=[...])` until `status.video_status` is `ready` before
`ads_create_creative` references it. A creative built on a video that is not ready fails. If the
status is `error`, `upload_failed` or `expired`, stop polling and restart the upload.

## There are no bulk create tools

The official MCP creates one creative and one ad per call. A 12-ad matrix is 12
`ads_create_creative` calls and 12 `ads_create_ad` calls. Plan for it, and build the first one end
to end before looping (SKILL.md, Build order). For 50+ ads use the XLSX rail instead.

Variants that used to need separate ads can live in one creative: `multi_media` (2-10 images or
videos, Meta picks per impression) and `primary_texts` / `headlines` / `descriptions` (up to 5
each, Sales / Leads / Engagement / Awareness objectives only). Do not use this to hide a creative
test: a concept test still needs one concept per ad so results split.

## URL parameters are set at creation

`url_tags` on `ads_create_creative` cannot be added after the creative exists. Copy them verbatim
from the template ad before creating anything.

## Order of operations that works

```
1. Verify every asset's extension, size and location
2. Images: upload -> finalize -> image_hash         (synchronous)
3. Videos: upload -> finalize -> video_id           (async)
4. Poll ads_get_ad_videos until every video is ready
5. ads_create_creative, one per ad (url_tags, instagram_user_id, Advantage+ choices set here)
6. ads_create_ad, one per ad, under the paused ad set
7. Read back every object; publish only on an explicit go (ads_activate_entity)
```

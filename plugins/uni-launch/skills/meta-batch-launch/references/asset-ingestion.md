# Asset Ingestion - getting creative files into Meta

The step that breaks most often on a real batch launch. Read this before promising a timeline.

## The core constraint

The Meta Ads MCP runs as a hosted service. It cannot see files on your laptop, on the media
buyer's machine, or in Claude's own workspace. Every asset must reach Meta by one of:

| Route | Tool | Works for |
|---|---|---|
| Public URL | `bulk_upload_ad_videos` / `bulk_upload_ad_images` | assets already on a CDN |
| Cloud storage file id | `upload_ad_video_file` (`drive_file_id` / `dropbox_file_id`) | private Drive / Dropbox files |
| Whole cloud folder | `create_creatives_from_drive_folder` / `..._dropbox_folder` | a folder of mixed images and video |
| Base64 bytes | `upload_ad_image` (`image_base64`) | small images only |
| Private Pipeboard URL | upload at `pipeboard.co/creatives`, pass the URL | confidential assets |

**Never base64 a video.** A 25 MB mp4 becomes ~34 MB of base64 and will blow the context window
long before it reaches Meta. Videos go by URL or cloud file id, full stop.

Client creative is not made public to work around this. If no private route is available, say so
and ask where the assets can be put, rather than sharing a client's folder to the open web.

## Trap 1: the MCP needs its OWN cloud-storage connection

Claude having a Google Drive connector does **not** give the Meta Ads MCP access to Drive. They are
separate authorizations. A folder call fails with:

> No Google Drive connection found. Connect Google Drive at https://pipeboard.co/connections

The fix is on the user's side: connect Drive (or Dropbox) at `pipeboard.co/connections`. Check
whoever's account owns the folder can actually see it - agency folders are often owned by a
teammate, not by the person doing the connecting.

## Trap 2: files without an extension fail as "unsupported format"

Assets exported straight into Google Drive frequently arrive with **no file extension** - Drive
metadata shows `fileExtension: ""` even though `mimeType` is `video/mp4`. Meta types the upload
off the filename, so every one of them fails with:

> The video you're trying to upload is in a format that isn't supported.

This is not a codec problem and re-encoding will not fix it. The fix:

```
upload_ad_video_file(
  account_id=..., drive_file_id=...,
  filename="CLIENT_Ad_Name.mp4",   # supply the extension yourself
  mime_type="video/mp4"
)
```

Check `fileExtension` on every Drive asset before a batch. When it is empty, skip the folder call
and upload file by file with an explicit filename. Tell the editor to keep extensions on export -
it saves a whole round trip next time.

## Trap 3: the folder call is all-or-nothing

`create_creatives_from_drive_folder` uploads **every** asset in the folder. There is no include or
exclude list. When some creatives in the folder were cancelled, either:

- accept the extra assets (they sit unused in the ad account library, harmless), or
- upload the wanted files one at a time by `drive_file_id`.

Say which one you did. Unused library assets are cheap, but an unexplained extra asset in a client
account looks like a mistake.

## Videos process asynchronously

`upload_ad_video_file` returns a `video_id` immediately, but Meta is still transcoding. Poll
`get_ad_video(account_id, video_id)` until `video_status` is `ready` before building a creative
against it. Referencing a video that is still processing fails with "Referenced item unavailable"
(subcode 3858794) - and `dry_run` does **not** catch it, because Meta's validate-only pass is
lighter than its live create pass.

## Order of operations that works

```
1. Verify every asset's extension and location
2. Upload images   -> image_hash   (fast, synchronous)
3. Upload videos   -> video_id     (async)
4. Poll video status until ready
5. bulk_create_ad_creatives
6. bulk_create_ads
```

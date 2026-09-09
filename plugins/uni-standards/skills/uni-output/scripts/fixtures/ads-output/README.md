# Regression fixtures for `lint-ads-output.py`

Both directions matter. A gate that only rejects is as useless as one that only accepts,
because the first thing a rushed operator does with a gate that blocks good work is stop
running it.

The `bad-*` fixtures are the real deliverables a media buyer reported on 2026-09-08, kept
close to what he actually received. The `good-*` fixtures are the shapes Sean approved the
same day. If a change to the linter makes a `good-*` file fail, the change is wrong.

| Fixture | Type | Expect | What it pins |
|---|---|---|---|
| `good-copy.txt` | `meta-copy` | exit 0 | The approved short shape: hook alone in block 1, block 2 carrying body plus CTA. Two blocks and three sentences is legal. Long copy with a bullet block is legal. A complete file: five variants, one register, both lengths, zero P2. |
| `bad-five.txt` | `meta-copy` | exit 1 | The two rules that had nothing behind them until 2026-09-09: five variants delivered, and one register across the file. Two variants at registers 3 and 5 - the shape is otherwise clean, so these are the only findings. |
| `bad-copy.txt` | `meta-copy` | exit 1 | One dense paragraph, CTA buried, emoji nobody asked for, character counts that do not match the text, seven sentences in one long-copy paragraph |
| `bad-counts.txt` | `meta-copy` | exit 1 | The counting convention, on byte-identical primary text. `hook` is block 1 stripped; `total` is the whole primary text stripped, blank lines counted. Also pins the tolerance boundary: one character of drift forgiven, two not. Added because two documents once printed different counts for the same example and the wrong one survived on the tolerance edge. |
| `good-targeting.txt` | `targeting` | exit 0 | Five clusters, three literal searchable names each, every row UNCONFIRMED with the Ads Manager instruction present and an interest-free fallback per cluster |
| `bad-targeting.txt` | `targeting` | exit 1 | Persona strings in the `name` field, slash-packed rows, `live` with no interest ID, a missing check date, three clusters instead of five |
| `bad-ideas.txt` | `ad-ideas` | exit 1 | Three fields on one line, hook that describes a hook instead of being one, hook not first, jargon prose scoring far past the readability ceiling |
| `bad-brief.txt` | `brief` | exit 1 | Markdown headings, bold and pipe tables left in the body, no Doc URL, no `Do not` block, an em dash, a promised highlight the tooling cannot do |

## Run them

```powershell
python skills/uni-output/scripts/fixtures/ads-output/run-fixtures.py
```

Exit 0 means every fixture landed on its expected verdict.

## Adding a fixture

Add it when a real deliverable fails in a way the linter missed. Name it `bad-<thing>.txt`,
keep it close to the output that actually shipped rather than a tidied-up illustration, and
add the row above with what it pins. A fixture invented to exercise a code path teaches
nobody anything later.

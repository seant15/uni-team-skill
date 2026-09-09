# UNI Team Skills

The shared skill store for UNI Marketing Agency. Install once, get every update automatically, propose improvements by pull request.

This repo is public so the team can install and test without a GitHub invite. Skills contain no client names, spend, or account IDs. Still never commit those.

---

## Install

Click-by-click setup for teammates: https://claude.ai/code/artifact/6f405020-c0f0-48ec-b28c-cc5e76967ca1

See [INSTALL.md](INSTALL.md) for the full guide per app. Summary below.

UNI is currently on individual Pro/Max seats, so each person installs it themselves.

### Cowork / Claude desktop

Follow the click-by-click setup first: https://claude.ai/code/artifact/6f405020-c0f0-48ec-b28c-cc5e76967ca1

Or: Cowork tab → **Customize** → **Plugins** → add marketplace `seant15/uni-team-skill`. Zip files in `dist/` are the fallback. Then **start a new session**. Full walkthrough in INSTALL.md.

### Claude Code

```
/plugin marketplace add seant15/uni-team-skill
/plugin install uni-standards@uni-team-skill
/plugin install uni-paid@uni-team-skill
/reload-plugins
```

### Codex

```
codex plugin marketplace add seant15/uni-team-skill
codex plugin add uni-standards@uni-team-skill
```

### Which plugins do I install?

| Role | Install |
|---|---|
| Meta media buyer | `uni-standards` + `uni-paid` |
| Google media buyer | `uni-standards` + `uni-paid` |
| Creative strategist | `uni-standards` + `uni-creative` |
| General team / assistants | `uni-standards` |

**Everyone installs `uni-standards`.** It holds the output standard every deliverable passes through.

### Updating

Cowork: Sean sends new zips, upload them again, start a new session. Claude Code: `/plugin marketplace update uni-team-skill` then `/reload-plugins`. Codex: `codex plugin marketplace upgrade uni-team-skill`.

---

## What's in here

### uni-standards
| Skill | Does |
|---|---|
| `uni-output` | The house standard. Three permitted formats, the interview gate every skill implements, the typography rule, the AI-slop ban list, and the delivery gate. Holds the six golden samples. Paid-media shape is refused by `scripts/lint-ads-output.py`. |
| `uni-output-qa` | Peer review of a teammate's draft. Scores it, gives line-referenced feedback to the person, names the one habit to fix. Does not rewrite their work. |

### uni-creative
| Skill | Does |
|---|---|
| `creative-brief` | Briefs a designer can execute without follow-up questions. Visual references attached and annotated, overlay lines routed through `meta-ad-copy`. |
| `ad-ideas` | Concepts grounded in live ad-library research. Maps the category's saturated and absent angles first, then generates against the gap. |

### uni-paid
| Skill | Does |
|---|---|
| `meta-ad-copy` | Meta copy inside the official limits and in the client's register. Holds the locked character reference. |
| `google-ad-copy` | Google copy written to the specific campaign type's spec - RSA, PMax, Demand Gen, Display, App all differ. |
| `meta-targeting` | The UNI interest-web method. Expands a persona across life dimensions and two-step adjacencies, validates every interest, delivers a tiered test plan. |

---

## Runs on Claude and Codex

One repo, both toolchains, one copy of every skill.

| | Claude Code / Cowork | Codex |
|---|---|---|
| Marketplace | `.claude-plugin/marketplace.json` | `.agents/plugins/marketplace.json` |
| Plugin manifest | `plugins/<name>/.claude-plugin/plugin.json` | `plugins/<name>/.codex-plugin/plugin.json` |
| Skills | `plugins/<name>/skills/<skill>/SKILL.md` | same files |

The skills are shared, not duplicated. Both tools read the same `SKILL.md` with the same `name` and `description` frontmatter.

**When you add or change a plugin, update both manifests.** Bumping only one means half the team stops getting updates and nobody notices for a month.

Skill bodies are written provider-neutrally - they say "the model", never "Claude" - so they read correctly in either tool. Keep it that way.

Cursor, Gemini CLI and Windsurf also read `SKILL.md` and can load these from `~/.agents/skills/`. Untested by us.

---

## House rules

**1. Edit here and push. Never edit your installed copy.** The next sync overwrites it and the work is gone.

**2. `main` is protected. Changes arrive as pull requests.** Sean approves. Two-line diffs still get read. *Second reviewer: currently none - this is a known single point of failure. Revisit when the team grows.*

**3. Bump the version in both plugin manifests or nothing ships.** A merge without a version bump sits in the repo doing nothing. Touch all four files in rule 8.

**4. Never commit client names, ad account IDs, spend figures, API keys, or PII.** Golden samples must be anonymised before they land here.

**5. No pricing, ever.** These skills cover operations. Fees, retainers and commercial terms go through Sean, not through a skill.

**6. Full app restart after any install or update.** This causes more "it's broken" messages than every real bug combined.

**7. No em dashes, no en dashes. Hyphens only.** This applies to every file in this repo and to everything the skills produce. It is check 0 on the output gate.

**8. Both manifests, every time.** A version bump touches `.claude-plugin/` and `.codex-plugin/` and the two marketplace files. Update one and half the team silently stops receiving changes.

**9. Facts get tagged.** Any platform limit or spec written into a reference file carries a verification date and a source URL. If you can't source it, mark it unverified rather than guessing.

---

## Anatomy of a UNI skill

Every skill in this repo has the same four parts. Keep it that way - see `CONTRIBUTING.md` for the template.

1. **Frontmatter** - `name` matching the folder name, and a `description` that says *when to use it*. A vague description means Claude never picks the skill up.
2. **Interview gate** - ask everything in one batch, skip what is supplied, lock the brief before producing, never fill a gap with a plausible value. Plus a stop-and-ask list for cases where guessing is worse than asking. The canonical rule lives in `uni-output`; every skill points at it.
3. **The work** - the actual method.
4. **Validation gate**, then **Self-Improvement** block.

**Does a skill actually ask when it lacks information?** Yes, by design, all seven. Each names its required inputs, asks for anything missing in a single batch, restates the brief for confirmation, and refuses to invent a value it was not given. The one exception is an unattended run with nobody to answer, where the skill proceeds and puts its assumptions at the top of the deliverable rather than deadlocking.

---

## Golden samples

Six, in `plugins/uni-standards/skills/uni-output/references/golden/`. Each carries the sample plus a numbered Hard requirements block. Both `uni-output` and `uni-output-qa` read them, and a sample outranks any prose rule.

| File | Deliverable |
|---|---|
| `proposal-audit.md` | PPC audit and proposal |
| `analytics-audit.md` | Analytics and tracking audit |
| `creative-brief.md` | Creative brief, full batch and short form |
| `weekly-report.md` | Weekly portfolio roll-up, one line per client |
| `monthly-report.md` | Monthly per-brand performance review |
| `text-message-update.md` | Team communication, Slack and ClickUp |

---

## Status

v0.4.0. Seven skills, three plugins, six golden samples, 302-interest seed library. Claude and Codex manifests both present.

**Not done yet:**
- First validation pass on `interest-library.md` - all 302 rows are `unconfirmed` and none carry Meta interest IDs
- `uni-seo` plugin - parked until the first three are proven
- Migration of the remaining skills from Sean's personal account
- Second PR reviewer
- Team or Enterprise plan later, so org-level install can replace per-seat setup. See INSTALL.md.

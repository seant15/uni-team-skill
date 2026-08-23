# Contributing

## Proposing a change

1. Branch off `main`. Short-lived - hours to a day or two.
2. Make the change **in this repo**, never in your installed copy.
3. Bump `version` in **both** `.claude-plugin/plugin.json` and `.codex-plugin/plugin.json`, plus the matching entry in `.claude-plugin/marketplace.json`. If you add or remove a plugin, also update `.agents/plugins/marketplace.json`. A version bump that ships to both toolchains touches four files. Patch for a wording fix, minor for a new skill or a changed method.
4. Rebuild the zips in `dist/` - that is how Cowork users receive it:
   ```
   cd plugins && for p in uni-standards uni-creative uni-paid; do zip -qr ../dist/$p.zip $p; done
   ```
5. Open a PR. Say in one line what changed and what problem it solves.
6. Sean reviews and merges. Squash merge, delete the branch.

Never push directly to `main`.

## Adding a new skill

```
plugins/<plugin>/skills/<skill-name>/
├── SKILL.md
└── references/          # optional - locked facts, worked examples, templates
```

The folder name is the skill name. The `name` in the frontmatter must match it exactly.

Then add a row to the README table. A skill nobody knows exists is a skill nobody uses.

## SKILL.md template

```markdown
---
name: skill-name
description: What it does, then WHEN to use it - the trigger phrases someone would actually type. This field is how Claude decides whether to load the skill. Vague description = never invoked.
---

# Skill name

One or two sentences on what breaks without this skill.

## Step 1 - Interview
Ask in one batch, skip what's supplied. Always establish: brand, tone,
audience, offer, format, constraints. Include an explicit **stop and ask**
list for the cases where guessing is worse than asking.

## Step 2 - The work
The actual method.

## Step 3 - Validate before delivering
A table of checks with what a failure means. End by routing through uni-output.

## Self-Improvement

At the end of every run, before ending:
1. Did any step fail or need a workaround?
2. Did the user correct or reject anything meaningful?
3. Did you discover something a future run might need?

Only propose a change if it meaningfully improves the skill. Propose it as a
diff for a pull request against `seant15/uni-team-skill` - never edit the
installed copy.
```

## Writing rules for skills

- **Second person, imperative.** "Ask for the brand's tone." Not "the skill should ask."
- **Tables over prose** for anything comparative - specs, checks, options.
- **Every platform fact carries a source URL and a verification date.** Untraceable numbers go in a `references/` file tagged unverified, not in the skill body as fact.
- **Name the failure mode.** "Fail = the ad set stops delivering" teaches more than "make sure to validate."
- **Every skill implements the interview gate.** A skill that will produce a deliverable from a one-line brief is not finished. Non-negotiable, checked at review.
- **No em dashes, no en dashes.** Hyphens only, in the skill file and in whatever it produces.
- Keep SKILL.md under roughly 200 lines. Longer material belongs in `references/`, which loads only when needed.

## Testing before you open the PR

```
claude --plugin-dir ./plugins/<plugin>
/plugin-name:skill-name
```

Run the skill on a real task, not a hypothetical one. Most skill bugs are missing interview questions, and they only surface against real work.

## Never commit

Client names · ad account IDs · spend figures · API keys · `.env` files · PII · un-anonymised deliverables.

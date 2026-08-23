# UNI Team Skills - agent instructions

This repo is a Claude Code plugin marketplace. It also works with any agent that reads markdown skill files.

## For Codex, Cursor, or other agents

Skills live at `plugins/<plugin>/skills/<skill-name>/SKILL.md`. Each is self-contained markdown with YAML frontmatter. Copy the ones you need into your agent's skills directory, or point your agent at this repo.

## Operating rules for any agent working in this repo

1. **Never edit an installed copy of a skill.** Edit the file here and open a pull request.
2. **Bump the version** in the plugin's `.claude-plugin/plugin.json` and the matching entry in `.claude-plugin/marketplace.json`, or the change reaches nobody.
3. **Never commit secrets, client names, ad account IDs, spend figures, or PII.**
4. **Never add pricing or commercial content to a skill.** These skills cover operations only.
5. **Platform facts need a source URL and a verification date.** If it can't be sourced, tag it unverified. Do not guess a character limit.
6. Only `plugin.json` goes inside `.claude-plugin/` and `.codex-plugin/`. `skills/` and `references/` sit at the plugin root.
7. **This repo ships manifests for both Claude and Codex.** A change touches four files: `.claude-plugin/marketplace.json`, `.agents/plugins/marketplace.json`, and each plugin's `.claude-plugin/plugin.json` and `.codex-plugin/plugin.json`. Update all four or half the team stops receiving updates.
8. **Write skill bodies provider-neutrally.** Say "the model", never "Claude" - the same files run in Codex, Cursor and Gemini CLI.

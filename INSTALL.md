# Install guide

Click-by-click setup (same as the README): https://claude.ai/code/artifact/6f405020-c0f0-48ec-b28c-cc5e76967ca1

Pick your row, follow it, ignore the rest.

| You are | Your app | Go to |
|---|---|---|
| Meta buyer, Google buyer, creative strategist, assistant | Claude desktop (Cowork) | [Path A](#path-a---claude-desktop-cowork) |
| Sean, or anyone using the terminal | Claude Code | [Path B](#path-b---claude-code) |
| Anyone using Codex | Codex CLI | [Path C](#path-c---codex) |

**Which plugins you need:**

| Role | Install |
|---|---|
| Meta media buyer | `uni-standards` + `uni-paid` + `uni-launch` |
| Google media buyer | `uni-standards` + `uni-paid` |
| Creative strategist | `uni-standards` + `uni-creative` |
| General team, assistants | `uni-standards` |
| SEO / content | `uni-standards` + `uni-seo` |

Everyone installs `uni-standards`. It holds the output rules everything else passes through.

---

## Path A - Claude desktop (Cowork)

**Time: 5 minutes. No GitHub account needed. No terminal.**

Preferred: add marketplace `seant15/uni-team-skill` on the Plugins page (the repo is public). If that fails, use the zip files.

Zip fallback: you will get zips from Sean: `uni-standards.zip`, plus `uni-creative.zip`, `uni-paid.zip`, `uni-seo.zip`, and/or `uni-launch.zip` for your role. Save them somewhere you can find again, like your Downloads folder. **Do not unzip them.** Claude wants the zip as-is.

### Step 1 - open the plugins page

1. Open the **Claude** desktop app.
2. At the top of the window, click the **Cowork** tab.
3. In the left sidebar, click **Customize**.
4. Click the **Plugins** tab.

### Step 2 - upload each plugin

5. Find the option to **upload a plugin file** on that page.
6. Choose `uni-standards.zip`.
7. Repeat for the other zip files your role needs.

### Step 3 - turn the skills on

8. Click the plugin you just installed to open it.
9. Check that its **skills are listed and enabled**. A plugin can install successfully with its skills switched off, and then nothing works and it looks like the plugin is broken.

### Step 4 - start a fresh session

10. **Close your current Cowork session and start a new one.** Plugins load when a session starts. If you install a plugin and keep working in the session you already had open, it will not be there.

### Step 5 - check it worked

In a new session, type:

```
Use uni-output to check this: Performance was strong across the board this month.
```

If it comes back telling you that sentence has no number in it and cannot be verified, the install worked. If it just agrees with you or says it does not know what uni-output is, go to [Troubleshooting](#troubleshooting).

### About folders

Plugins and folders are two different things and neither needs the other.

- **Plugins** = what Claude knows how to do. Installed under Customize, applies everywhere.
- **Folders** = which files on your computer Claude can open and edit. Set per project.

A skill works with no folder attached. You only need a folder when the work involves files on your computer - opening a spreadsheet, saving a report.

To attach one: **Projects** in the left sidebar, **+**, pick **Use an existing folder**, name it, and attach the folder you want. Claude can then read and write inside that folder during that project's sessions, and nowhere else.

### Getting updates

When Sean ships a change, he sends new zip files. Upload them the same way, then start a new session. Same as the first install.

---

## Path B - Claude Code

**Time: 2 minutes.** The repo is public, so no GitHub invite is required.

```
/plugin marketplace add seant15/uni-team-skill
/plugin install uni-standards@uni-team-skill
/plugin install uni-paid@uni-team-skill
/plugin install uni-seo@uni-team-skill
/plugin install uni-launch@uni-team-skill
```

Then either restart, or run:

```
/reload-plugins
```

Check it worked:

```
/uni-standards:uni-output
```

If it does not appear, run `/plugin` and open the **Errors** tab.

### Getting updates

Auto-update is off by default for third-party marketplaces, so pull them yourself:

```
/plugin marketplace update uni-team-skill
```

Then `/reload-plugins`.

**If the update fails on authentication**, run `gh auth setup-git` once and try again. Background refreshes run without your credential helper, which is a known rough edge; the manual command above uses your credentials properly.

---

## Path C - Codex

**Time: 2 minutes.** The repo carries Codex manifests alongside the Claude ones, so the same repo serves both.

```
codex plugin marketplace add seant15/uni-team-skill
codex plugin add uni-standards@uni-team-skill
codex plugin add uni-paid@uni-team-skill
codex plugin list
```

The skills are the same files Claude reads. There is no separate copy to keep in sync.

**If you would rather not use the plugin system**, Codex also loads loose skills. Clone the repo and symlink the skills you want:

```
git clone git@github.com:seant15/uni-team-skill.git ~/src/uni-team-skill
mkdir -p ~/.agents/skills
ln -s ~/src/uni-team-skill/plugins/uni-standards/skills/uni-output ~/.agents/skills/uni-output
```

**The path is `~/.agents/skills`, not `~/.codex/skills`.** This is the single most common mistake. Update with `git pull`.

---

## Troubleshooting

**"Claude says it doesn't know what uni-output is."**
Nine times out of ten: you installed it and kept working in the same session. Start a new session.

**"It's installed but the skills don't fire."**
Open the plugin under Customize and check the skills are enabled. Installed and enabled are two different states.

**"I installed it in the Code tab and it's not in Cowork."**
They are separate. Cowork loads what is enabled on your claude.ai account and does not read the Claude Code CLI's local directory. Install it again under Cowork's Customize page.

**"Marketplace sync failed" when adding a repository in Cowork.**
The repo is public, so this should work now. If it still fails, use the zip files in Path A. That used to be required when the repo was private (Cowork marketplace sync runs server-side and could not read a private repo on an individual seat).

**Claude Code only: skills missing after a successful install.**
```
rm -rf ~/.claude/plugins/cache
```
Then restart Claude Code and reinstall the plugin.

---

## For Sean - the distribution decision

**Decision 2026-08-23: repo is public.** The team can install and test without a GitHub invite. Click-by-click setup lives at https://claude.ai/code/artifact/6f405020-c0f0-48ec-b28c-cc5e76967ca1

Trade-off accepted: the method is readable by anyone. Golden samples stay anonymised. Client names, spend, and account IDs still never land here.

Zip files in `dist/` stay as a Cowork fallback if marketplace add fails. Team or Enterprise plan remains the later path for org-level private install.

**Before you send anything to the team, install one plugin yourself on a Cowork seat and run the Step 5 check.** There have been reports of marketplace-installed plugins registering in the UI while their skill files never mount, with the zip path working - but verify on your own machine rather than trusting that.

---

## Which files to send

Built into `dist/`:

- `uni-standards.zip` - everyone
- `uni-creative.zip` - creative strategist
- `uni-paid.zip` - both media buyers
- `uni-seo.zip` - SEO / content
- `uni-launch.zip` - Meta buyers who build campaigns. Ships the Meta Ads MCP server.

Rebuild after any change:

```
cd plugins && for p in uni-standards uni-creative uni-paid uni-seo uni-launch; do zip -qr ../dist/$p.zip $p; done
```

Bump the version in each plugin's `.claude-plugin/plugin.json` and `.codex-plugin/plugin.json` first, or people will not be able to tell which copy they have.

#!/usr/bin/env python3
"""Delivery gate for UNI paid-media deliverables.

The four paid-media skills (meta-ad-copy, meta-targeting, ad-ideas,
creative-brief) already carried these rules as prose and the rules were
skipped, because nothing in the pipeline could refuse the output. This script
is the thing that refuses.

Contract: skills/uni-output/SKILL.md, "The paid-media output contract".

    python skills/uni-output/scripts/lint-ads-output.py <file> --type meta-copy
    python skills/uni-output/scripts/lint-ads-output.py <file> --type targeting
    python skills/uni-output/scripts/lint-ads-output.py <file> --type ad-ideas
    python skills/uni-output/scripts/lint-ads-output.py <file> --type brief

Exit 0 = deliverable. Exit 1 = a P1 failed, do not send.
P2 findings never change the exit code; they go in the handoff.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

# --------------------------------------------------------------------------
# shared
# --------------------------------------------------------------------------

DASHES = {"\u2014": "em dash", "\u2013": "en dash"}

# Ranges that cover pictographs, emoticons, transport, flags and the
# dingbats Meta copy tends to pick up. Deliberately excludes plain glyphs
# such as arrows and box drawing, which uni-output permits.
EMOJI_RE = re.compile(
    "["
    "\U0001f000-\U0001faff"
    "\u2600-\u27bf"
    "\ufe0f"
    "\U0001f1e6-\U0001f1ff"
    "]"
)

SENTENCE_END_RE = re.compile(r"[.!?](?:[\"')\]]+)?(?:\s|$)")

# A persona or content-genre label masquerading as a Meta interest. These are
# exactly the strings the media buyer could not find in Ads Manager.
PERSONA_TOKENS = (
    "aesthetic",
    "content",
    "creators",
    "culture",
    "vibes",
    "lifestyle",
    "mindset",
    "community of",
    "-coded",
    "core mom",
    "engagers",
    "enthusiasts who",
    "people who",
    "moms who",
    "parents who",
)


@dataclass
class Report:
    kind: str
    p1: list[str] = field(default_factory=list)
    p2: list[str] = field(default_factory=list)
    stats: dict = field(default_factory=dict)

    def fail(self, msg: str) -> None:
        self.p1.append(msg)

    def warn(self, msg: str) -> None:
        self.p2.append(msg)

    @property
    def ok(self) -> bool:
        return not self.p1


def sentence_count(text: str) -> int:
    """Sentences in a paragraph. Bullet lines count as one each."""
    stripped = text.strip()
    if not stripped:
        return 0
    hits = len(SENTENCE_END_RE.findall(stripped))
    # A paragraph with no terminal punctuation is still one sentence.
    return max(hits, 1)


def is_bullet_block(text: str) -> bool:
    lines = [ln.strip() for ln in text.strip().splitlines() if ln.strip()]
    if not lines:
        return False
    bullets = sum(1 for ln in lines if re.match(r"^([-*\u2022]|\d+[.)])\s", ln))
    return bullets >= max(2, len(lines) // 2)


def blocks_of(text: str) -> list[str]:
    """Split on blank lines, preserving order, dropping empties."""
    return [b for b in re.split(r"\n\s*\n", text.strip()) if b.strip()]


def check_house_typography(text: str, rep: Report, where: str) -> None:
    for ch, name in DASHES.items():
        if ch in text:
            rep.fail(f"{where}: contains {name}. House rule is ASCII hyphen only.")


def flesch_kincaid_grade(text: str) -> float | None:
    """Flesch-Kincaid grade level. Reported, never self-declared.

    Correlation with human-perceived readability is loose, so the caller
    treats a high grade as a prompt to shorten sentences, not as truth.
    """
    words = re.findall(r"[A-Za-z][A-Za-z'\-]*", text)
    if len(words) < 20:
        return None
    sentences = max(len(SENTENCE_END_RE.findall(text)), 1)
    syllables = sum(count_syllables(w) for w in words)
    return round(
        0.39 * (len(words) / sentences) + 11.8 * (syllables / len(words)) - 15.59, 1
    )


def count_syllables(word: str) -> int:
    w = word.lower().strip("'-")
    if not w:
        return 0
    vowels = "aeiouy"
    total, prev_vowel = 0, False
    for ch in w:
        is_vowel = ch in vowels
        if is_vowel and not prev_vowel:
            total += 1
        prev_vowel = is_vowel
    if w.endswith("e") and not w.endswith(("le", "ee", "ye")) and total > 1:
        total -= 1
    return max(total, 1)


def parse_records(text: str, header_re: re.Pattern) -> list[tuple[str, str]]:
    """Split a deliverable into (header, body) on === HEADER === lines."""
    out: list[tuple[str, str]] = []
    matches = list(header_re.finditer(text))
    for i, m in enumerate(matches):
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        out.append((m.group(1).strip(), text[m.end():end]))
    return out


def field_value(body: str, label: str) -> str | None:
    m = re.search(rf"^{re.escape(label)}:[ \t]*(.*)$", body, re.MULTILINE)
    return m.group(1).strip() if m else None


# --------------------------------------------------------------------------
# meta-copy
# --------------------------------------------------------------------------

VARIANT_RE = re.compile(r"^===\s*(VARIANT[^=]*)===\s*$", re.MULTILINE)
PRIMARY_RE = re.compile(
    r"^PRIMARY TEXT[ \t]*$\n(.*?)^END PRIMARY TEXT[ \t]*$",
    re.MULTILINE | re.DOTALL,
)
HOOK_BUDGET = 40
SHORT_LENGTHS = {"short"}
LONG_LENGTHS = {"long-fb", "long-aida"}
SHORT_ONLY_PLACEMENTS = {"reels", "stories"}


def lint_meta_copy(text: str, allow_emoji: bool) -> Report:
    rep = Report("meta-copy")
    check_house_typography(text, rep, "deliverable")

    variants = parse_records(text, VARIANT_RE)
    rep.stats["variants"] = len(variants)
    if not variants:
        rep.fail(
            "No '=== VARIANT n ===' blocks found. See uni-output Contract 1 for the shape."
        )
        return rep
    if len(variants) != 5:
        rep.fail(
            f"{len(variants)} variants. Meta accepts 5 primary texts per ad, and the "
            "contract is five delivered - not a pool trimmed to five, and not a short "
            "file. Write the missing ones or cut to five."
        )

    for header, body in variants:
        tag = header.strip()
        pm = PRIMARY_RE.search(body)
        if not pm:
            rep.fail(f"{tag}: missing PRIMARY TEXT / END PRIMARY TEXT delimiters.")
            continue
        primary = pm.group(1).rstrip("\n")

        length = (field_value(body, "Length") or "").lower()
        placement = (field_value(body, "Placement") or "").lower()
        if length not in SHORT_LENGTHS | LONG_LENGTHS:
            rep.fail(
                f"{tag}: Length is '{length or 'missing'}'. "
                f"Use one of: short, long-fb, long-aida."
            )

        if not allow_emoji:
            found = sorted({ord(c) for c in EMOJI_RE.findall(primary)})
            if found:
                # Report codepoints, not the glyphs - a cp1252 console cannot
                # print them and the linter must never crash on its own findings.
                points = ", ".join(f"U+{cp:04X}" for cp in found)
                rep.fail(
                    f"{tag}: {len(found)} emoji in primary text ({points}). "
                    f"Emoji only when the buyer asked in this request "
                    f"(re-run with --allow-emoji)."
                )

        blocks = blocks_of(primary)
        rep.stats.setdefault("shape", []).append(
            {tag: f"{len(blocks)} blocks / "
                  f"{sum(sentence_count(b) for b in blocks if not is_bullet_block(b))} sentences"}
        )

        # Rule 1 - hook alone in block 1.
        if len(blocks) < 2:
            rep.fail(
                f"{tag}: primary text is one block. "
                f"The first sentence sits alone, then a blank line."
            )
        else:
            hook_block = blocks[0]
            if sentence_count(hook_block) > 1:
                rep.fail(
                    f"{tag}: block 1 carries {sentence_count(hook_block)} sentences. "
                    f"The hook stands alone."
                )
            if "\n" in hook_block.strip():
                rep.warn(f"{tag}: hook block wraps onto a second line. Tighten it.")

            # Rule 5 - the specific thing lands inside 40 characters.
            hook_len = len(hook_block.strip())
            rep.stats.setdefault("hooks", []).append({tag: hook_len})
            if hook_len > 125:
                rep.fail(
                    f"{tag}: hook is {hook_len} chars, past the mobile fold at ~125."
                )
            elif hook_len > HOOK_BUDGET:
                rep.warn(
                    f"{tag}: hook is {hook_len} chars. Target {HOOK_BUDGET} so it "
                    f"survives a small screen and accessibility text sizing."
                )

        # Rule 2 - block 2 holds two sentences at most; a third sentence of body
        # pushes the CTA into its own block. Short copy stops at three blocks.
        if length in SHORT_LENGTHS:
            for i, block in enumerate(blocks[1:], start=2):
                if is_bullet_block(block):
                    continue
                n = sentence_count(block)
                if n > 2:
                    rep.fail(
                        f"{tag}: block {i} carries {n} sentences. Two at most, and "
                        f"if the body needs both, the CTA moves to its own block."
                    )
            if len(blocks) > 3:
                rep.fail(
                    f"{tag}: short copy is {len(blocks)} blocks. "
                    f"Three is the ceiling; past that it is long copy."
                )

        # Rules 3 and 4 - long copy paragraphing and CTA-only close.
        if length in LONG_LENGTHS:
            for i, block in enumerate(blocks, start=1):
                if is_bullet_block(block):
                    continue
                n = sentence_count(block)
                if n > 3:
                    rep.fail(
                        f"{tag}: paragraph {i} has {n} sentences. Long copy caps at 3 "
                        f"per paragraph (bullet blocks exempt)."
                    )
            if blocks:
                last = blocks[-1]
                if is_bullet_block(last):
                    rep.fail(f"{tag}: long copy ends on a bullet block, not a CTA.")
                else:
                    n = sentence_count(last)
                    if n > 2:
                        rep.fail(
                            f"{tag}: closing paragraph has {n} sentences. "
                            f"The CTA paragraph is 1 to 2 sentences and nothing else."
                        )

        # Rule 6 - Reels and Stories are short only.
        if placement in SHORT_ONLY_PLACEMENTS and length in LONG_LENGTHS:
            rep.fail(
                f"{tag}: placement '{placement}' with '{length}'. "
                f"Reels and Stories deliver short only."
            )

        # Rule 8 - counts present and correct.
        counts = field_value(body, "Counts")
        if not counts:
            rep.fail(f"{tag}: missing 'Counts: hook N / total N'. Count, do not estimate.")
        else:
            m = re.search(r"hook\s+(\d+)\s*/\s*total\s+(\d+)", counts, re.IGNORECASE)
            if not m:
                rep.fail(f"{tag}: Counts line unparseable: '{counts}'.")
            elif blocks:
                claimed_hook, claimed_total = int(m.group(1)), int(m.group(2))
                real_hook = len(blocks[0].strip())
                real_total = len(primary.strip())
                if abs(claimed_hook - real_hook) > 1:
                    rep.fail(
                        f"{tag}: hook count says {claimed_hook}, actual {real_hook}."
                    )
                if abs(claimed_total - real_total) > 1:
                    rep.fail(
                        f"{tag}: total count says {claimed_total}, actual {real_total}."
                    )

    lengths = {(field_value(b, "Length") or "").lower() for _, b in variants}
    if not (lengths & SHORT_LENGTHS) or not (lengths & LONG_LENGTHS):
        rep.warn(
            "Only one length represented. UNI tests short against long every time, "
            "or the test reads nothing."
        )

    # Rule 9 - one register across the file, so length is the only variable.
    registers = [(field_value(b, "Register") or "").strip() for _, b in variants]
    if any(not r for r in registers):
        rep.fail("Every variant needs 'Register: n' - the number the client gave.")
    distinct = sorted({r for r in registers if r})
    if len(distinct) > 1:
        rep.fail(
            f"Variants span registers {', '.join(distinct)}. The length test holds "
            "register constant; mixed registers test two things at once and read as "
            "neither. Pick the client's number and write all five to it."
        )
    return rep


# --------------------------------------------------------------------------
# targeting
# --------------------------------------------------------------------------

CLUSTER_RE = re.compile(r"^===\s*(CLUSTER[^=]*)===\s*$", re.MULTILINE)
INTERESTS_RE = re.compile(
    r"^INTERESTS[ \t]*$\n(.*?)^END INTERESTS[ \t]*$", re.MULTILINE | re.DOTALL
)
MIN_CLUSTERS = 5
MIN_PER_CLUSTER = 3
MAX_PER_CLUSTER = 8
TARGET_PER_CLUSTER = 5


def lint_targeting(text: str) -> Report:
    rep = Report("targeting")
    check_house_typography(text, rep, "deliverable")

    clusters = parse_records(text, CLUSTER_RE)
    rep.stats["clusters"] = len(clusters)
    if not clusters:
        rep.fail(
            "No '=== CLUSTER n: name ===' blocks found. See uni-output Contract 2."
        )
        return rep
    if len(clusters) < MIN_CLUSTERS:
        rep.fail(
            f"{len(clusters)} cluster directions. Minimum is {MIN_CLUSTERS} per run."
        )

    unconfirmed_total = 0
    for header, body in clusters:
        tag = header.strip()
        if not field_value(body, "Chain"):
            rep.fail(f"{tag}: no 'Chain:' line. A cluster without a stateable chain "
                     f"is a list, not a hypothesis.")
        if not field_value(body, "Kill"):
            rep.fail(f"{tag}: no 'Kill:' condition. State what result kills it.")

        im = INTERESTS_RE.search(body)
        if not im:
            rep.fail(f"{tag}: missing INTERESTS / END INTERESTS delimiters.")
            continue

        rows = [ln.strip() for ln in im.group(1).splitlines() if ln.strip()]
        rows = [r for r in rows if r.startswith("-")]
        if len(rows) < MIN_PER_CLUSTER:
            rep.fail(
                f"{tag}: {len(rows)} interests. Minimum {MIN_PER_CLUSTER} per cluster."
            )
        if len(rows) > MAX_PER_CLUSTER:
            rep.fail(
                f"{tag}: {len(rows)} interests. Over {MAX_PER_CLUSTER} splits into "
                f"two clusters."
            )
        elif len(rows) > TARGET_PER_CLUSTER:
            rep.warn(f"{tag}: {len(rows)} interests. Target is 3 to 5.")

        for row in rows:
            fields = dict()
            for part in row.lstrip("- ").split("|"):
                if ":" in part:
                    k, v = part.split(":", 1)
                    fields[k.strip().lower()] = v.strip()

            name = fields.get("name", "")
            status = fields.get("status", "").lower()
            iid = fields.get("id", "")
            checked = fields.get("checked", "")

            if not name:
                rep.fail(f"{tag}: row has no 'name:' field -> {row}")
                continue

            # Rule 3 - the name must be typeable into the Ads Manager search box.
            low = name.lower()
            hit = next((t for t in PERSONA_TOKENS if t in low), None)
            if hit:
                rep.fail(
                    f"{tag}: '{name}' reads as a persona, not an interest "
                    f"(matched '{hit}'). Put it in Chain. The name field must be a "
                    f"literal string the buyer can type into detailed targeting."
                )
            if "/" in name:
                rep.fail(
                    f"{tag}: '{name}' packs two things into one interest. "
                    f"One searchable label per row."
                )
            if len(name.split()) > 5:
                rep.warn(
                    f"{tag}: '{name}' is {len(name.split())} words. Real interest "
                    f"labels are short. Verify it exists."
                )

            if status not in {"live", "unconfirmed"}:
                rep.fail(
                    f"{tag}: '{name}' status is '{status or 'missing'}'. "
                    f"Use live or UNCONFIRMED."
                )
            if status == "live":
                if not iid or iid == "-":
                    rep.fail(
                        f"{tag}: '{name}' marked live with no id. Meta renames "
                        f"interests; the ID is the only stable key. If you did not "
                        f"actually check it, the status is UNCONFIRMED."
                    )
            elif status == "unconfirmed":
                unconfirmed_total += 1
            if not re.match(r"^\d{4}-\d{2}-\d{2}$", checked or ""):
                rep.fail(f"{tag}: '{name}' has no 'checked: YYYY-MM-DD' date.")

    rep.stats["unconfirmed_rows"] = unconfirmed_total
    if unconfirmed_total:
        if not re.search(
            r"ads manager.{0,80}(search box|search field|detailed targeting)",
            text,
            re.IGNORECASE | re.DOTALL,
        ):
            rep.fail(
                f"{unconfirmed_total} UNCONFIRMED rows but no line telling the buyer "
                f"to type them into the Ads Manager search box before launch."
            )
        if not re.search(r"fallback|broad\b|lookalike|custom audience", text, re.IGNORECASE):
            rep.warn(
                "Every cluster can die on a deleted interest and no interest-free "
                "fallback is offered. Give one per cluster."
            )
    if re.search(r"\bexclu(de|sion)\w*\b.{0,40}\binterest", text, re.IGNORECASE):
        rep.warn(
            "Reads like a detailed-targeting exclusion. Those were removed in 2025; "
            "use custom audience exclusions."
        )
    return rep


# --------------------------------------------------------------------------
# ad-ideas
# --------------------------------------------------------------------------

CONCEPT_RE = re.compile(r"^===\s*(CONCEPT[^=]*)===\s*$", re.MULTILINE)
CONCEPT_FIELDS = ["Hook", "Gap", "Angle", "Idea", "Format", "Producible", "Risk"]
FKGL_P1 = 10.0
FKGL_P2 = 8.0
DESCRIBED_HOOK_RE = re.compile(
    r"^(a |an )?(hook|line|headline)\s+(about|on|that|which)\b", re.IGNORECASE
)


def lint_ad_ideas(text: str) -> Report:
    rep = Report("ad-ideas")
    check_house_typography(text, rep, "deliverable")

    concepts = parse_records(text, CONCEPT_RE)
    rep.stats["concepts"] = len(concepts)
    if not concepts:
        rep.fail("No '=== CONCEPT n: name ===' blocks found. See uni-output Contract 3.")
        return rep
    if not 5 <= len(concepts) <= 7:
        rep.fail(
            f"{len(concepts)} concepts. The contract is 5 to 7 delivered - not a pool "
            "trimmed down, and not a short file."
        )

    for header, body in concepts:
        tag = header.strip()
        lines = [ln for ln in body.splitlines() if ln.strip()]

        # Rule 1 - one field per line.
        for ln in lines:
            labels = [f for f in CONCEPT_FIELDS if re.search(rf"\b{f}:", ln)]
            if len(labels) > 1:
                rep.fail(
                    f"{tag}: {len(labels)} fields on one line ({', '.join(labels)}). "
                    f"One field per line."
                )

        # Rule 4 - all seven present.
        missing = [f for f in CONCEPT_FIELDS if field_value(body, f) is None]
        if missing:
            rep.fail(f"{tag}: missing field(s): {', '.join(missing)}.")

        # Rule 3 - hook first, and written.
        if lines:
            first = lines[0].strip()
            if not first.startswith("Hook:"):
                rep.fail(
                    f"{tag}: first line is '{first[:40]}'. Hook comes first so the "
                    f"buyer can skim."
                )
        hook = field_value(body, "Hook")
        if hook is not None:
            if not hook:
                rep.fail(f"{tag}: Hook is empty.")
            elif DESCRIBED_HOOK_RE.match(hook):
                rep.fail(
                    f"{tag}: Hook describes a hook instead of being one -> '{hook}'."
                )
            elif not SENTENCE_END_RE.search(hook + " ") and len(hook.split()) > 8:
                rep.warn(f"{tag}: Hook has no terminal punctuation -> '{hook}'.")

    # Rule 2 - blank line between concepts.
    for header, body in concepts[:-1]:
        if not body.endswith("\n\n") and not re.search(r"\n\s*\n\s*$", body):
            rep.warn(f"{header.strip()}: no blank line before the next concept.")

    # Rule 5 - readability, computed not declared.
    prose = "\n".join(
        (field_value(b, f) or "")
        for _, b in concepts
        for f in ("Idea", "Gap", "Producible", "Risk")
    )
    grade = flesch_kincaid_grade(prose)
    rep.stats["flesch_kincaid_grade"] = grade
    if grade is None:
        rep.warn("Too little prose to compute a readability grade.")
    elif grade > FKGL_P1:
        rep.fail(
            f"Flesch-Kincaid grade {grade}. Target 7, hard ceiling {FKGL_P1}. "
            f"Shorten sentences and drop jargon. Do not shorten Risk into vagueness."
        )
    elif grade > FKGL_P2:
        rep.warn(f"Flesch-Kincaid grade {grade}. Target is 7 or below.")
    return rep


# --------------------------------------------------------------------------
# brief
# --------------------------------------------------------------------------

DOC_URL_RE = re.compile(r"https://docs\.google\.com/document/d/[\w-]+")


def lint_brief(text: str) -> Report:
    rep = Report("brief")
    check_house_typography(text, rep, "deliverable")

    if not DOC_URL_RE.search(text):
        rep.fail(
            "No Google Doc URL in the handoff. The default brief output is a real Doc "
            "created via docs_create, not markdown pasted into chat."
        )

    for pattern, msg in (
        (r"^#{1,6}\s", "markdown heading (`#`)"),
        (r"\*\*[^*\n]+\*\*", "markdown bold (`**`)"),
        (r"^\s*\|.*\|\s*$", "markdown pipe table"),
    ):
        if re.search(pattern, text, re.MULTILINE):
            rep.fail(
                f"Body contains a {msg}. Use Docs headings, Docs bold and Docs tables."
            )

    if not re.search(r"^\s*Do not\b", text, re.MULTILINE | re.IGNORECASE):
        rep.fail("No 'Do not' block. It prevents more revision rounds than any other "
                 "section.")
    if not re.search(r"^\s*(Overlay|Text overlay)\b", text, re.MULTILINE | re.IGNORECASE):
        rep.warn("No overlay line found. If the creative carries text, lock it here.")
    if re.search(r"highlight", text, re.IGNORECASE):
        rep.warn(
            "Mentions highlight. The Docs tooling has no highlight colour; "
            "Heading 3 plus bold is the approved emphasis."
        )

    links = re.findall(r"https?://\S+", text)
    rep.stats["links"] = len(links)
    if len(links) < 2:
        rep.warn(
            "Fewer than two reference links. Images cannot be embedded, so annotated "
            "links are the only way references reach the designer."
        )
    return rep


# --------------------------------------------------------------------------
# cli
# --------------------------------------------------------------------------

LINTERS = {
    "meta-copy": lambda t, a: lint_meta_copy(t, a.allow_emoji),
    "targeting": lambda t, a: lint_targeting(t),
    "ad-ideas": lambda t, a: lint_ad_ideas(t),
    "brief": lambda t, a: lint_brief(t),
}


def main() -> int:
    # Deliverables carry client copy in any language. A Windows cp1252 console
    # must not be able to crash the gate.
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):
            pass

    ap = argparse.ArgumentParser(
        description="Delivery gate for UNI paid-media deliverables."
    )
    ap.add_argument("file", type=Path, help="the deliverable, written to a file")
    ap.add_argument("--type", required=True, choices=sorted(LINTERS))
    ap.add_argument(
        "--allow-emoji",
        action="store_true",
        help="only when the buyer asked for emoji in this request",
    )
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    if not args.file.is_file():
        print(f"lint-ads-output: no such file: {args.file}", file=sys.stderr)
        return 2

    text = args.file.read_text(encoding="utf-8")
    rep = LINTERS[args.type](text, args)

    if args.json:
        print(
            json.dumps(
                {
                    "type": rep.kind,
                    "file": str(args.file),
                    "pass": rep.ok,
                    "p1": rep.p1,
                    "p2": rep.p2,
                    "stats": rep.stats,
                },
                indent=2,
            )
        )
        return 0 if rep.ok else 1

    print(f"lint-ads-output: {rep.kind} :: {args.file}")
    for k, v in rep.stats.items():
        print(f"  {k}: {v}")
    for msg in rep.p1:
        print(f"  P1  {msg}")
    for msg in rep.p2:
        print(f"  P2  {msg}")
    verdict = "PASS" if rep.ok else "BLOCK"
    print(f"  -> {verdict} (P1={len(rep.p1)}, P2={len(rep.p2)})")
    return 0 if rep.ok else 1


if __name__ == "__main__":
    sys.exit(main())

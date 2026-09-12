# Naming and matrix expansion

## Why naming is load-bearing

Every downstream report slices on name segments. A batch launched with inconsistent names cannot
be analysed by creative, angle or audience without manual cleanup. Lock the convention before the
first row is written. Never change it mid-batch.

Separator is ` | ` - space, pipe, space. Exactly that, every time.

## Ad name - the UNI standard

```
[VID/IMG/CAR] | [Ad Name] | [MMDDYYYY]
```

`VID | Gold or Silver | 09122026`

| Segment | Rule |
|---|---|
| Format code | `VID` for any moving asset including UGC and GIF, `IMG` for static, `CAR` for carousel |
| Ad name | The creative's human name, Title Case, spaces allowed, no pipes. Derive from the asset filename when the client supplies named assets |
| Launch date | `MMDDYYYY`, the date it goes live, not the date it was built |

**Known trade-off, recorded so nobody rediscovers it.** This carries no creative id and no
hook or angle tag. Two revisions of the same concept launched on different dates read as two
unrelated ads, and hooks cannot be ranked across clients from ad names alone. When a batch needs
that resolution, put the version in the name segment (`Gold or Silver v2`) rather than inventing a
fourth segment.

Older ads in client accounts may carry a four-segment form with an angle or CTA slot
(`VID | Bracelet B-roll | Recovery Angle | 06202025`). Do not retrofit them. Do expect report
pivots that split on segment position to handle both.

## Campaign and ad set names

Follow whatever the account already uses. A shape seen in production:

```
Campaign   TOF (US) | CBO | Adv+ | MMDDYYYY
Ad set     Broad | US | All Gender | 25-65+ | MMDDYYYY
```

Funnel stage, geo, budget mode, placement mode, date. When cloning an ad set for a new creative
batch, insert what makes it distinguishable before the date rather than appending after it:

```
Broad | US | All Gender | 25-65+ | Colorway | MMDDYYYY
```

The duplicate tool only appends a suffix, which leaves the source's date in the middle of the new
name. Rename properly straight after. Do not ship a two-date name.

## Matrix expansion

### The default: creative x audience

```
audiences: [A1, A2, A3]
creatives: [C1, C2, C3, C4]
```

Output: **one campaign, three ad sets, twelve ads.** Every creative in every ad set.

This isolates the creative variable within each audience, so a winning creative reads independent
of who saw it.

### When copy is also a variable

Only on an explicit request. Three audiences x four creatives x two copy sets is 24 ads, and no
single ad gets enough budget to reach significance. Push back: test copy in a second round against
the winning creative, not simultaneously.

### Budget split

| Mode | Use when | Watch |
|---|---|---|
| CBO | Audiences are comparable in size and the goal is finding the winner fast | Ad-set budget fields must be blank |
| ABO | Each audience must get a guaranteed read, or sizes differ wildly | Campaign budget field must be blank |

### The learning-phase gate

```
weekly events per ad set = (daily budget x 7) / target CPA
```

| Result | Verdict |
|---|---|
| 50 or more | Fine |
| 25 to 50 | Warn. Recommend CBO or fewer ad sets |
| Under 25 | Block on ABO. Warn on CBO, where Meta pools spend toward winners |

Show the arithmetic. `$120 x 7 / $28 = 30 per week` is an argument a buyer can act on. "This will
not exit learning" is one they can wave away.

Adding an ad set to an existing CBO campaign **splits a budget that is already committed.** Run
the gate against the post-split number, not the pre-split one, and say plainly what the existing
ad sets lose.

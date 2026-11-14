# Meta platform facts used in audits

**Verified 2026-11-13.** Re-verify every 6 months. Primary = Meta's own page. Secondary = a third-party write-up quoting or summarising Meta; treat as directional and do not quote it to a client as a Meta statement.

---

## Learning phase

- An ad set exits learning after about 50 optimization events in the week after its last significant edit. Primary: [About the learning phase](https://www.facebook.com/business/help/112167992830700). Below that the status is Learning limited.
- Working formula (UNI): target or actual CPA x 50 / 7 = the daily budget one ad set needs to exit learning. Put it next to the real budget in every Structure section.
- Large budget changes, targeting edits, optimization event changes and new creative can restart learning. Secondary, widely cited 20% budget rule: [lionelz.com learning phase guide, updated 2026-03](https://lionelz.com/en/blog/facebook-learning-phase-essentials/). Treat 20% as a house guard, not a Meta number.

## Attribution (changed in 2026)

- March 2026: click-through attribution now requires a link click. Other interactions (likes, shares, comment clicks, 5-second video views) moved to a new 1-day **engage-through** window. Billing did not change. Default for website conversion ad sets became 7-day click, 1-day engage-through, 1-day view. Secondary: [Jon Loomer, How Meta Ads Attribution Works in 2026](https://www.jonloomer.com/meta-ads-attribution-2026/); [PPC Land on the engaged-view change from 10 to 5 seconds](https://ppc.land/meta-rewrites-click-attribution-rules-finally-aligning-with-google-analytics/).
- January 2026: 7-day and 28-day view windows removed from the Ads Insights API; 1-day view remains. Secondary: same PPC Land article.
- Audit rule: state the attribution setting per campaign. A campaign that counts engage-through will look better than one that does not, with no change in real sales.

## Event Match Quality

- EMQ is a 0 to 10 score on Conversions API website events, shown per event in Events Manager and based on recent events. The browser pixel alone has no EMQ. Secondary summary of Meta's help page: [Madgicx glossary, EMQ](https://madgicx.com/glossary/event-match-quality). Meta's rating bands are Poor / Okay / Good / Great; aim for Good or Great.
- fbc (click ID) must be sent unhashed and is one of the strongest match keys. High EMQ with low fbc coverage still means ad clicks are not stitched to orders. Secondary: [CustomerLabs on fbc](https://www.customerlabs.com/blog/improve-your-event-match-quality-from-ok-to-great).

## Creative fatigue labels

- Delivery column shows **Creative limited** when cost per result is higher than your past ads but under 2x, and **Creative fatigue** at 2x or more. Labels show most reliably on ad sets with a single creative. Secondary quoting Meta: [Novo Ads on creative fatigue](https://novoads.ai/en/blog/creative-fatigue); [PPC Land, creative fatigue](https://ppc.land/creative-fatigue/).

## Andromeda and creative diversity

- Meta's retrieval system (Andromeda) is content-aware: it reads the creative to decide who sees it. Practical effect reported across agencies: broad targeting beats narrow interest stacks, simplified structures win, fatigue arrives faster, and near-identical variants count as one idea. Secondary: [Search Engine Land on Andromeda and GEM](https://searchengineland.com/meta-ai-driven-advertising-system-andromeda-gem-468020).
- Meta-reported test widely repeated: one ad set with 25 diverse creatives got 17% more conversions at 16% lower cost than five ad sets with five creatives each. Secondary only: [Chatterbuzz](https://www.chatterbuzzmedia.com/blog/meta-andromeda-creative-targeting/). Unverified at primary source; do not quote to a client as fact.
- Audit rule: count distinct concepts, not ads. "TRANSLATED" and "Copy" versions of one video are one concept.

## Detailed targeting

- On conversion, value and most performance goals, Advantage+ detailed targeting applies with no opt-out; interests are signals. Full detail and sources: `meta-targeting/references/platform-reality-2026.md` in this plugin.
- Consequence for audits: an ad set "testing" one interest with Advantage+ audience off is not a clean interest test either. Read interest ad sets as delivery slots, not audience proof.

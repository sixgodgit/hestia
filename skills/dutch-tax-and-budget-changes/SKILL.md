---
name: dutch-tax-and-budget-changes
description: "Use when explaining Dutch tax/budget changes; personalize."
version: 1.0.0
version: 1.0.0
author: sixgod
license: CC BY-NC 4.0
metadata:
  hermes:
    tags: [Netherlands, Tax, Budget, Policy, Citations, Personalization]
    category: research
    related_skills: [grounded-citations, blocked-page-recovery, dutch-official-documents, dutch-zzp-ondernemer]
---

# Dutch Tax & Budget Changes

Covers any "what did the government announce" / "what does it mean for me"
question about Dutch national fiscal policy: Prinsjesdag and the
Miljoenennota / Rijksbegroting / Belastingplan package, the Voorjaarsnota and
Najaarsnota updates, and the measure lists published with them.

For running the business itself — KVK registration, btw-id and btw filing
periods, KOR, invoicing and retention, Zvw and AOV cover, municipal permits for
working from home — use `dutch-zzp-ondernemer` instead of this skill.

For a household's own entitlements — kinderbijslag, kindgebonden budget,
zorgtoeslag, huurtoeslag, kinderopvangtoeslag, and the gemeente's minimum
schemes — use `dutch-toeslagen-and-benefits`, which carries the per-year amount
grid, the eligibility branches and the municipal income lines.

Two deliverables, always together: a **cited summary** of what was announced,
and a **personalized impact list** for this user. A summary without the
personalization, or personalization without citations, is half the job.

## Output shape (standing user preferences)

- Reply in Simplified Chinese; keep Dutch legal terms in parentheses on first
  use (koopkracht, eigen risico, arbeidskorting, overdrachtsbelasting). The
  user reads Dutch sources but wants Chinese prose.
- Flat structure: short bold labels or one bullet list. No nested headings, no
  process narration, no restating the question.
- Bracket citation on every sentence carrying an outside fact, and end with the
  rendered `Sources:` block (procedure in `grounded-citations`).
- Separate "already decided" from "proposal": nothing in this package is law
  before the vote, and a minority cabinet's package can be negotiated away.

## Procedure

1. **Fix the reference year.** Prinsjesdag is the third Tuesday of September;
   the documents published that day cover the NEXT calendar year
   (Miljoenennota <Y+1>, Belastingplan <Y+1>). Run `date` and compute — the
   press headlines it "Prinsjesdag <Y>" while the documents are dated <Y+1>,
   which is a reliable source of off-by-one errors.
2. **Primary sources before news.** Leaks reach the press first and misstate
   totals; the official pages are the only place the settled figures land.
   `references/miljoenennota-document-map.md` maps which document holds which
   number — read it before fetching.
3. **Then two or three press/advisor roundups** to surface the measures the
   official pages bury inside tables, plus the per-income-group koopkracht.
4. Register every URL in the citation ledger as it arrives, before drafting;
   then `sources.py verify --strict --min-coverage 0.5` on the draft.
5. For the personalized half follow "Personalizing" below, including the
   one-question-per-unknown clarify form when facts are missing.

## Fetching these sites

A 403 from an anonymous fetch tool is not evidence that the page is gated.
Dutch government and tax-advisor sites (rijksoverheid.nl, rijksfinancien.nl,
cpb.nl, advisor blogs) serve fine to `curl` with a browser-shaped UA, and a
live fetch beats an archived snapshot on provenance — try this before the
archive ladder in `blocked-page-recovery`:

```bash
UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128 Safari/537.36"
for u in "$URL1" "$URL2"; do
  curl -sSL -A "$UA" -o "/tmp/pg_$(printf %s "$u" | md5sum | cut -c1-8).html" \
    -w "%{http_code} $u\n" "$u"
done
```

`curl` returns raw HTML, so convert before reading (a 200 on a JS-only page
still yields no prose):

```bash
python3 scripts/html_to_text.py /tmp/pg_*.html
```

DPG Media titles (Parool, AD, Volkskrant) answer with a consent gate instead
of the article — the body is the outlet's chrome and no prose. Cite only what
the search description literally states, or use another outlet; never write as
if you read the body.

Gemeente content pages (denhaag.nl) render client-side and answer `curl` with a
near-empty body even on a 200. Use the literal text of the search-result
description, or read the rule itself at `lokaleregelgeving.overheid.nl`
(e.g. the Beleidsregels minimavoorzieningen of the gemeente in question).

## Personalizing ("what's in it for me")

Apply this user's standing fiscal profile, and **omit** what does not apply
rather than dumping it — a list of inapplicable measures reads as noise:

- **Profile (a default frame, not a filter on what the question is about):**
  ZZP / eenmanszaak with no employees, single, no children, owner-occupied home
  in Den Haag, no car, small tech business.
- **Relevant:** zelfstandigenaftrek / startersaftrek / stakingsaftrek,
  innovatiebox, EIA and investment deductions, IB bracket rates and the frozen
  toptarief start, arbeidskorting, box 3 heffingvrij vermogen, eigen risico +
  zorgpremie + zorgtoeslag, waterbelasting, and business-facing funds
  (NII, NADI, Groeifonds) plus any startups/scale-ups bill in the package.
- **Not applicable to that one-person frame, skip it:** employer premiums
  (Whk, Aof, Awf, Ufo), bestelauto/vrachttruck MRB, fuel accijns, commuting
  allowance, ouderenkorting, AOW-leeftijd. Child- and toeslag-related lines are
  "not applicable" only while the frame really is one person — family-household
  questions (children, a partner, rent, child benefit) arrive through this same
  channel, so filtering their lines out is the failure mode; compute that
  household and hand the entitlement half to `dutch-toeslagen-and-benefits`.
- Municipal matters (OZB, afvalstoffenheffing, local permits) are decided in
  the gemeente's own budget, not here — say so once instead of guessing.
- Ask for what you cannot know with ONE clarify form, choices not prose
  (income band, business form, housing status, vehicle). Never assume an
  income and build the answer on it.

## Pitfalls

- **Never read a measure's effective year off a stripped-text measure table.**
  Empty cells disappear when HTML becomes text, so column position is lost and
  a value slides under the wrong year. Get effective dates from the prose
  "Toelichting maatregelen" section, or from the official pre-disclosure annex
  (search `open.overheid.nl` for "voorlopige inhoud pakket Belastingplan <Y>").
- **Match measures by title, not by number.** Measure numbering is not shared
  across the uitgavenkader / inkomstenkader tables and their explanations; a
  numbered row can have no explanation at that number, and a differently
  numbered paragraph explains it.
- **Report the cabinet's own figures and the CPB's doorrekening side by side
  when they disagree** — the EMU-saldo can differ by several tenths of a point
  for the same year. Never average, reconcile, or silently pick one; name both
  and attribute them.
- **Gross vs net buying-power money.** A "€X miljard koopkrachtreparatie"
  headline is the gross package; the net lastenverlichting is smaller when part
  of it is financed by raising other taxes. When the user asks what it costs
  them, lead with the net figure and attribute the correction to whoever
  computed it.
- **Advisor pre-disclosure material predates the final package** and can be
  reversed in the wetsvoorstel. Label it as pre-announcement and prefer the
  adopted text for anything the user will act on.

## Verification

- Headline totals cross-checked across the ministry release, the Miljoenennota
  text and the CPB page; any difference stated, not smoothed.
- Every outside figure carries a citation and `sources.py verify` exits clean.
- The personalized list names only measures that actually touch this user's
  profile, and labels each one's status (in force 1 Jan <Y+1> / proposal).

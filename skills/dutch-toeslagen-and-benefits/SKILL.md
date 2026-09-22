---
name: dutch-toeslagen-and-benefits
description: "Use when computing Dutch household benefits (toeslagen)."
version: 1.0.0
version: 1.0.0
author: sixgod
license: CC BY-NC 4.0
metadata:
  hermes:
    tags: [Netherlands, Toeslagen, Benefits, Kinderbijslag, KindgebondenBudget, Zorgtoeslag, Huurtoeslag, DenHaag]
    category: research
    related_skills: [dutch-tax-and-budget-changes, dutch-zzp-ondernemer, grounded-citations, dutch-official-documents]
---

# Dutch Toeslagen & Household Benefits

"How much can this household get?" — kinderbijslag, kindgebonden budget,
zorgtoeslag, huurtoeslag, kinderopvangtoeslag, the income-related tax credits
(IACK, arbeidskorting context), the gemeente's minimum schemes (Ooievaarspas,
kwijtschelding, bijzondere bijstand, Leergeld), and what the household's
children can claim on their own (DUO, their own zorgtoeslag).

Boundaries: policy *news* (Prinsjesdag, Belastingplan, koopkracht) is
`dutch-tax-and-budget-changes`; the business side (btw, KOR, urencriterium,
Zvw) is `dutch-zzp-ondernemer`; writing the resulting letter or form is
`dutch-official-documents`.

## Output shape (standing user preferences)

- Simplified Chinese prose, Dutch terms in parentheses on first use
  (toetsingsinkomen, alleenstaande-ouderkop, proefberekening, bijstandsnorm).
- Flat structure: short bold labels plus one bullet list. No nested headings,
  no process narration, no restating the question.
- Bracket citation on every sentence carrying an outside fact, and end with the
  rendered `Sources:` block (procedure in `grounded-citations`).
- **Put the year on every amount** and say "按 <Y> 年规则" once, because the whole
  grid resets each January.
- Split the reply into: what is certain (income-independent), what the income
  yields, what applies only under a condition (renting, childcare), and what
  this income rules out. The user asked for "全部福利" — an exhaustive list is
  wanted, but every line still needs its condition or it reads as a promise.
- The user's stored profile is single, no children, ZZP — that is NOT the
  household being asked about. Family members' households (children, a partner,
  benefit income) come up; take the composition from the question itself.
- Close with the one or two facts that pin the number (toeslagpartner, rent vs
  owner-occupied, childcare hours) and offer to recompute — do not open with a
  clarify form when the income was already given.

## Procedure

1. **Fix the year.** Run `date`; quote the current calendar year's grid even if
   the question cites last year's figures.
2. **Convert the user's numbers to the yardstick the law uses.**
   `toetsingsinkomen` = gross annual *household* income, never net pay. Take the
   monthly gross × 12, add 8% vakantiegeld when the figure was given excl.
   holiday allowance, and state which you assumed. Net monthly pay is only a
   sanity check (AHK + arbeidskorting should explain the gap).
3. **Fix the household frame before computing** — it changes both the ceiling
   and the phase-out threshold: toeslagpartner or not, children under 18 on
   1 January, rent vs owner-occupied, which children are in registered
   childcare. If only the income is known, compute **both** the single-parent
   and the with-partner branch (the difference is the alleenstaande-ouderkop
   plus a different drempelinkomen), label each, and ask the user to confirm one
   line. Guessing one branch is wrong about half the time. When the partner's
   income is itself unknown, add a band table over plausible combined incomes so
   the user can read off their own row — a table answers the question now, a
   clarify form only delays it.
4. **Pull the official amounts** (next section). Never reuse last year's grid
   from memory or from an advisor blog.
5. **Compute with a tool, not mentally**: ceiling → subtract the phase-out
   percentage × (income − drempelinkomen) → round as the official rule does
   (whole euros, monthly = yearly/remaining months rounded down). Show yearly
   and monthly. Also compute the **zero point** (drempelinkomen + ceiling ÷
   phase-out rate) — that one number is what answers "do we still get anything
   at this income".
6. Register every URL in the citation ledger as it is fetched, render the
   `Sources:` block, run `sources.py verify --strict`.

## Getting the official amounts

- The Belastingdienst "Hoeveel ... krijg ik?" pages **no longer publish the
  amount tables** — they push you to the proefberekening. The numbers live in
  the downloadable brochures under "Brochures en publicaties":
  `Informatieblad kindgebonden budget <Y>`, `Berekening kinderopvangtoeslag <Y>`
  (carries the full income → reimbursement-percentage table), and
  `Toeslagenkaart <Y>` — one grid with every threshold for the year.
- Fetch them with a browser UA, take the hrefs out of the index page, then read
  the PDFs directly (`read_file` extracts the text layer; tables come out as
  run-on prose that still preserves every figure).
  `scripts/fetch_bd_brochures.sh <year> [outdir]` does the whole loop.
- **Take the deep-link URLs out of the toeslagen hub pages**
  (`/nl/kindgebonden-budget/`, `/nl/huurtoeslag/`, `/nl/zorgtoeslag/`): their
  "Snel naar" block holds the real subpage paths, so regex the `href`s out of
  the raw HTML instead of constructing paths — invented Belastingdienst depth
  URLs (`.../kindgebonden-budget-2026`, `.../hypotheekrente-aftrek`,
  `.../eigenwoningforfait`) all 404.
- **Check the document code printed in the PDF footer** (e.g. `TG 710`,
  `1Z61PL`) against the year before quoting — the brochure index lists several
  years side by side and it is easy to grab the wrong one.
- The index page lags: the newest Toeslagenkaart is not always linked from it
  yet. The filename pattern is
  `download.belastingdienst.nl/toeslagen/docs/toeslagenkaart_<year>_tg7101z<NN>pl.pdf`;
  if that 404s, a mirror of the same Dienst Toeslagen PDF is acceptable once the
  footer code confirms the year — cite it as the Dienst Toeslagen publication it is.
- Second sources for the income-independent half: rijksoverheid.nl `Bedragen
  ... <Y>` pages, the SVB pages for kinderbijslag (amounts + betaaldagen), and
  the SZW `Uitkeringsbedragen per 1 januari <Y>` PDF on open.overheid.nl for
  WML-linked norms.
- Third-party roundups (Consumentenbond, Knab, AFAS kengetallen, calculator
  sites) **are leads only**: they disagree with each other on components and
  some still print the previous year. Verify every ceiling against the official
  PDF, then cite the official PDF.

## Pitfalls

- **Income for toeslagen is gross and it is the household's.** Using net pay
  understates the toetsingsinkomen and produces entitlements the household
  cannot get; add both partners' income and the partner's assets.
- **A child living at home is not a toeslagpartner.** Since 1 January 2025
  neither a child nor a parent counts as one, so an adult child at home must not
  be merged into the household frame and must not cancel the
  alleenstaande-ouderkop. For huurtoeslag a co-resident still counts as
  medebewoner above the year's vrijgesteld inkomen. `toeslagen.nl/partner`
  lists the situations that do create one (shared child, notarial
  samenlevingscontract, joint owner-occupied home, and situation 5 for a single
  housemate alongside a minor child) — read that page for a shared-address
  household instead of reasoning from "someone else is registered here".
- **Component amounts differ between secondary sources; only the official
  Toeslagenkaart settles them.** Cross-check every derived component
  arithmetically against a published total in the same table (one-child
  single-parent total minus one-child partner total = the alleenstaande-ouderkop).
  A component that does not reconcile is a wrong-year figure.
- **kinderbijslag and kindgebonden budget stop at 18** — the 18+ child adds
  nothing to either, and their side is DUO studiefinanciering (their own
  application) plus their own zorgtoeslag. Kindgebonden budget stops
  automatically when the child turns 18.
- **Kinderopvangtoeslag exists only for registered (LRK) care and only when
  every parent works**; hours are capped at 230 per month per child, the
  reimbursement percentage depends on the combined income *and* on whether the
  child is the 1st or a later child in care, and only children under 12 (day
  care / BSO) qualify.
- **Huurtoeslag requires renting.** Owner-occupied housing = €0 whatever the
  income. Since 2026 there is no maximum-rent eligibility gate, but the
  calculation still tops out at the year's maximale huur, and the multi-person
  household's entitlement is reduced linearly above the ijkpunt. A mortgage
  payment is not rent and never enters this calculation — but the reverse side
  matters for an owning household: deductible mortgage interest lowers the
  toetsingsinkomen below the gross salary (nudging kindgebonden budget and
  zorgtoeslag up slightly) while the eigenwoningforfait lifts it again.
- **Assets are tested on 1 January** for the whole year, and the huurtoeslag
  ceiling is far lower than the zorgtoeslag / kindgebonden budget one. State
  which date and which ceiling applies; an 18+ child's assets stay outside the
  parent's kindgebonden budget test.
- **The municipal minima schemes are what falls away first at middle incomes.**
  Den Haag sets its lines as 150% / 130% / 110% of the bijstandsnorm (Ooievaarspas
  at 150%, individuele inkomenstoeslag at 110%) and publishes them as **monthly
  net amounts incl. vakantiegeld** — quote the monthly norm, never a derived
  annual figure. Even above the line, point to bijzondere bijstand
  (case-by-case) and Stichting Leergeld for school/sport costs instead of
  writing the whole municipal chapter off.
- **Label announced changes as proposals.** The Belastingplan package presented
  each September tightens the kindgebonden budget phase-out and asset ceiling
  for the following year; nothing is law before the vote and inwerkingtreding.
- **Do not read a stripped-text amount table's column position.** Empty cells
  vanish when HTML becomes text; take figures from PDFs whose columns are
  printed, or from a table whose row labels stayed intact.

## Verification

- Every figure traced to an official PDF or page, with the year stated in the
  sentence.
- Derived totals recomputed by tool and reconciled against a published total.
- Both household branches given, each labelled, whenever partner status is
  unknown.
- `sources.py verify <draft> --strict` exits clean and the reply ends with the
  rendered `Sources:` block.

## Reference

- `references/toeslagen-amounts.md` — verified per-year amount grid, thresholds,
  phase-out rates, asset ceilings, Den Haag norm table; re-verify and add the
  new column each January.
- `scripts/fetch_bd_brochures.sh` — downloads the current-year Dienst Toeslagen
  brochure PDFs for a given year.

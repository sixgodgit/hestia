# Toeslagen & benefits — amount grid by year

Amounts reset every 1 January (and kinderbijslag also on 1 July). **Re-verify
before quoting** against the Dienst Toeslagen brochures for the year
(`scripts/fetch_bd_brochures.sh <year>`), then add the new year here instead of
overwriting — the year-on-year delta is itself useful context.

Source of the 2026 grid: Dienst Toeslagen *Toeslagenkaart 2026* (code TG 710 /
1Z61PL), *Informatieblad kindgebonden budget 2026* (TG 722), *Berekening
kinderopvangtoeslag 2026* (TG 080), SVB kinderbijslag amounts, and the
Belastingdienst zorgtoeslag / huurtoeslag pages.

## Kinderbijslag (SVB, per child per quarter, paid after the quarter, income-independent)

| Age | 2026 Q1-Q2 | 2026 Q3+ |
|---|---|---|
| 0-5 | 295.07 | 298.40 |
| 6-11 | 358.30 | 362.35 |
| 12-17 | 421.53 | 426.29 |

Stops at 18. No income test, no asset test, does not feed the toeslagen income.

## Kindgebonden budget (2026)

- Base per child under 18: **2,580 / year**, every child equal (2 children =
  5,160 for a couple).
- Extra per child aged 12-15: **+724 / year**; aged 16-17: **+964 / year**
  (the higher amount replaces the lower, not stacked).
- Alleenstaande-ouderkop (no toeslagpartner): **+3,416 / year**.
- Full amount up to a toetsingsinkomen of **29,736** (single parent) /
  **39,141** (with toeslagpartner); above that phase-out **7.6%** of the excess.
- Assets on 1 January: **146,011** single / **184,633** with partner.
- Reconciliation check: 1 child + kop = 5,996; minus 2,580 base = the 3,416 kop.

## Zorgtoeslag (2026)

- Max **129 / month** single, **246 / month** with toeslagpartner.
- Income ceiling **40,857** single / **51,142** combined with partner.
- Assets 146,011 / 184,633 (same as kindgebonden budget).
- Belastingdienst publishes a 500-wide income bracket table — read the row for
  the bracket the income falls **into**, not the nearest lower label.

## Huurtoeslag (2026)

- Renters only; owner-occupied = 0.
- Since 2026 no maximum-rent eligibility gate, but the calculation caps at
  **932.93** (498.20 for households where everyone is under 21).
- Tiers: 100% up to the kwaliteitskortingsgrens **498.20**, 65% up to the
  aftoppingsgrens **713.02** (1-2 persons) / **764.14** (3+ persons), 40% up to
  932.93, 0% above. The household always pays roughly the first 200 itself.
- Income ijkpunt **23,425** (single) / **31,500** (multi-person); above it the
  toeslag falls linearly — 0.27 per euro of income for one-person households,
  0.22 for multi-person.
- Assets: **38,479 per resident**, 76,958 for partners.
- Vrijgesteld inkomen of a live-in child under 23: **6,218** before it counts.

## Kinderopvangtoeslag (2026)

- Max hourly rate: dagopvang **11.23**, BSO **9.98**, gastouder **8.49**.
- Max 230 hours per month per child, capped by the months worked.
- 96% of the capped cost for a combined income up to **56,412** (1st child);
  above that the percentage steps down in income brackets and the 2nd and later
  children keep a higher percentage than the 1st — read the bracket table in the
  brochure PDF rather than interpolating.

## Tax-credit context (2026)

- IACK (income-related combination credit): max **3,032** below AOW age,
  accrues at 11.45% x (arbeidsinkomen - 6,239), full from 32,711; requires a
  child under 12 on 1 January and goes to the single parent or the lower-earning
  partner.
- Useful for the net/gross sanity check: AHK max 3,115 with afbouwpunt 29,736
  (6.306% above), arbeidskorting max 5,712, box-1 rates 35.70% / 37.56% / 49.50%
  with bracket edges 38,883 and 79,137.

## Gemeente Den Haag minima norms

From 1 July 2026, monthly **net incl. vakantiegeld**:

| Household | 110% | 130% | 150% |
|---|---|---|---|
| Single (parent) | 1,484 | 1,754 | 2,023 |
| Gezin | 2,120 | 2,505 | 2,890 |
| Single, AOW age | 1,740 | 2,057 | 2,373 |
| Gezin, AOW age | 2,386 | 2,819 | 3,253 |

Ooievaarspas and the tegemoetkoming chronisch zieken en gehandicapten use 150%,
individuele inkomenstoeslag 110% (averaged over 36 months), and an entrepreneur's
business capital is excluded from the Ooievaarspas test. The underlying rules sit
in the Beleidsregels minimavoorzieningen of the gemeente on
lokaleregelgeving.overheid.nl — denhaag.nl content pages do not render for curl.

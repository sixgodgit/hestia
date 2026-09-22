# ZZP / eenmanszaak reference (Netherlands)

Verified: 2026 (figures fetched 2026-09). Tax year for all money figures: **2026**.
All amounts are **year-scoped**. Re-verify each January at `belastingdienst.nl` →
Winst → Inkomstenbelasting → *Veranderingen inkomstenbelasting <jaar>*, and on the
Zvw percentages page; Dutch thresholds and aftrekposten change every year. Treat
this file as structure, not as a current price list. Full URLs for every claim
below, plus which of them are year-scoped, are in `references/source-map.md`; the
line-by-line attribution here names the primary host only.

Primary sources are cited per line. Advisor/insurer pages were used only to
corroborate, never as the sole source of a number.

## 1. KVK stage and the KVK → Belastingdienst sequence

- Registering at KVK is the only act required; KVK forwards the details to the
  Belastingdienst, which then decides whether you are an entrepreneur for btw.
  There is **no separate VAT application**. (business.gov.nl)
- One-off registration fee **€85.15** (from 1 Jan 2026), tax-deductible for the
  entrepreneur, paid at the desk (pin/credit card, no cash). (kvk.nl)
- The Belastingdienst letters arrive by post — stated as **up to 10 working
  days**, in practice within about two weeks (business.gov.nl says within two
  weeks). A zzp'er gets **two separate letters**, one per number, because the
  vaststelling-belastingplicht letter names the ob-nummer and states the btw-id
  follows "in een aparte brief":
  - **btw-id** — format `NL` + 9 digits + `B` + 2 digits (e.g.
    `NL123456789B01`). For customers, suppliers, invoices, letterhead, website.
  - **omzetbelastingnummer (ob-nummer)** — format 9 digits + `B` + 2 digits
    (e.g. `111234567B01`); for a zzp'er the 9 digits are the BSN. Only for
    contact with the Belastingdienst, never on an invoice.
  Both are also readable in Mijn Belastingdienst Zakelijk under 'Btw'.
- Login: an eenmanszaak uses **DigiD** on Mijn Belastingdienst Zakelijk, free.
  eHerkenning (EH3, roughly €14–30/yr, partly compensated via RVO's scheme) is
  for forms that are not natural persons (BV/vof/maatschap) and intermediaries —
  do not send a zzp'er shopping for it. Since 6 August 2026 the login flow asks
  for the ondernemingsvorm first.
- Since 1 September 2026 businesses can opt to receive Belastingdienst post
  **digitally only** (starting with omzetbelasting messages) in Mijn
  Belastingdienst Zakelijk — useful to avoid missed letters and penalties.
- **Change duty: report changes within 1 week** via Mijn KVK (address, trade
  name, activities, functionaries, number of workers). Late reporting can create
  liability; the change counts from the moment it lands in the Handelsregister.
  (kvk.nl, ondernemersplein.overheid.nl)
- KVK forwards a **bezoekadres** change to the Belastingdienst itself, but a
  **postadres** change must be reported to the Belastingdienst yourself.
  (kvk.nl)
- Stop < 6 months: you may stay registered with a Dutch visiting address. Stop
  > 6 months: deregister; restarting later yields a new KVK number and a new btw
  number. (kvk.nl)
- Directeur-grootaandeelhouder, medegerechtigde and meewerkende partner are
  different regimes; an eenmanszaak is the default and needs no notary.
- A **business bank account is not legally required** for an eenmanszaak, but the
  administration must keep business and private money traceable for the whole
  retention period — which is what a separate account buys you. (A BV does
  effectively need one.) (business.gov.nl, Belastingdienst bewaarplicht page)

## 2. btw: aangiftetijdvak, deadlines, KOR

- Default **quarterly** aangifte; the Belastingdienst assigns the tijdvak and
  confirms it in the letter after registration. Monthly is imposed above roughly
  €15,000 btw per quarter, or after filing late; yearly is available on request
  when the btw due is under about **€1,883/year** and the other conditions are
  met. A change of tijdvak is requested by letter to the belastingkantoor, answer
  within 6 weeks, effective from the start of the next period.
  (belastingdienst.nl)
- Deadlines: last day of the month following the quarter — 2026: 30 April,
  31 July, 31 October, 31 January (next year). Returns can be filed from the
  24th of the month preceding the end of the period; earlier submissions are
  rejected with an error. (belastingdienst.nl)
- The **aangiftebrief** arrives each year before the end of the first tijdvak and
  lists periods, deadlines and betalingskenmerken. Keep it. A nil return
  (0-aangifte / nihilaangifte) is still due when there was no turnover.
  First-time filers may receive a one-off paper return. (belastingdienst.nl)
- **KOR (kleineondernemersregeling): turnover ≤ €20,000** per calendar year.
  Participants charge no btw, file no btw returns and cannot reclaim input btw.
  EU-KOR has existed since 1 January 2025 for cross-border trade.
  Anmelden/afmelden happens in Mijn Belastingdienst Zakelijk.
  (belastingdienst.nl)
- KOR decision rule of thumb: if clients are mainly private consumers, KOR saves
  administration and the input-btw loss is small; if clients are businesses and
  costs carry a lot of btw, staying in the normal regime usually wins. Whether to
  join therefore hinges on the turnover band and on the customer mix — ask, don't
  assume a turnover.

## 3. Invoicing and record-keeping

- Mandatory invoice fields: full legal name **and** address of both parties (a PO
  box alone is not enough; trade name allowed if registered with the address),
  **your btw-id**, **your KVK number** if registered, invoice date, a unique
  sequential invoice number, description plus quantity/scope of goods or
  services, the applied btw rate, and the btw amount. Reduced requirements for
  invoices ≤ **€100** incl. btw; extra fields for cross-border work.
  (belastingdienst.nl)
- Invoices to other businesses and to non-business legal entities
  (verenigingen, stichtingen) are compulsory; consumers need one only in
  distance-sales and cross-border service situations. Intracommunautaire
  levering always needs an invoice. (belastingdienst.nl)
- Retention: **7 years** for basic records (grootboek, debiteuren/crediteuren,
  in- en verkoopadministratie); **10 years** for immovable-property data and for
  One Stop Shop (Union/Import scheme) supplies. Shorter terms for other data are
  possible but must be agreed in writing. The clock starts when the data stops
  being current (e.g. a 4-year lease is kept 4 + 7). Storing only printed copies
  of digital files does not satisfy the obligation — programs and files must stay
  accessible and working. (belastingdienst.nl, business.gov.nl)
- The financial statement (jaarrekening) is the basis for the returns and is not
  filed with KVK. Outsourced bookkeeping runs roughly €500–€1,000/year.

## 4. Voorbelasting (input btw) and btw a supplier charged

- btw on business purchases is deducted as **voorbelasting** in rubriek 5b of the
  btw return. Conditions: the purchase serves *belaste* (taxed) turnover; the
  invoice is addressed to the business and shows the buyer's btw-id; the
  goods/services are not for private use (private use is deducted pro rata, and
  btw wrongly deducted on private use must be repaid). btw on costs belonging to
  vrijgestelde or niet-belaste turnover is not deductible, and KOR participants
  cannot deduct at all. (belastingdienst.nl)
- A negative return is not carried forward: the Belastingdienst refunds the
  balance, so a starter with no turnover yet gets the btw on hosting, software
  and tools back in cash through the ordinary quarterly return.
- **Same-country supplier:** the charge is a domestic supply and is correct —
  reclaim it as voorbelasting. **EU supplier to an EU business:** the invoice
  should be 0% with `btw verlegd` / reverse charge (art. 196 BTW-richtlijn) and
  the buyer's btw-id; the buyer self-assesses that btw as output and deducts it
  as input in the same return, netting to zero.
- **Cross-border refund** (foreign btw wrongly charged, or btw paid abroad):
  claim it from that country through the Dutch Belastingdienst, not from the
  supplier — Mijn Belastingdienst Zakelijk → `Btw` → `VAT refund` (the separate
  *Teruggaaf van btw uit andere EU-landen* site with its own login credentials is
  the older route). Conditions: the business is established in the Netherlands,
  files no btw return in that country, and uses the goods/services for taxed
  activity. Deadline **30 September of the year following** the refund period;
  thresholds **€50** for a claim covering the whole calendar year (or its
  December-including remainder) and **€400** for a claim covering at least 3
  months but less than a year. That country decides within 4 months and pays
  within 10 working days after. File early — the portal is overloaded in
  September. (belastingdienst.nl)
- **Non-EU supplier:** no EU btw exists, so nothing to reclaim; a foreign tax on
  the invoice is not deductible, and the service is self-assessed as verlegde btw
  in the Dutch return.

## 5. Inkomstenbelasting: aftrekposten

- **Urencriterium: 1,225 hours per calendar year** in the onderneming. Gates
  zelfstandigenaftrek and startersaftrek (not the mkb-winstvrijstelling).
  It has TWO conditions: 1,225 hours, **and** spending more time on the business
  than on other work (e.g. loondienst). The second condition is waived when the
  person was not an ondernemer in one of the 5 preceding calendar years — so
  **a full-time job does not by itself block the aftrek**; only the hour count
  can. Ask about loondienst before concluding either way. Reduced 800-hour
  threshold for starters with a disability. (business.gov.nl)
- **No pro-rating in the starting year.** 1,225 hours is always per calendar
  year — a mid-year start still owes the full 1,225 in that year (KVK: a 1 May
  start leaves ~117 working days ≈ 936 hours at 8 h/day). So a starter registered
  in autumn with a day job cannot realistically claim for that year: no
  zelfstandigenaftrek/startersaftrek, but the mkb-winstvrijstelling still applies
  automatically (12.7% in 2026).
- **The startersaftrek window can close before the hours become feasible.**
  2026 is its last year — KVK states the regeling vervalt in 2027 (Belastingplan
  2027, not yet enacted). A starter who cannot reach 1,225 hours in the part-year
  therefore loses the €2,123 permanently; check the hours plan before telling a
  starter they will "use it in a later year".
- **Hours administration is not a legal form but is the evidence.** Log date,
  hours, activity and client contemporaneously (a spreadsheet or timesheet is
  fine), keep it 7 years with the administratie, and make the hours *aannemelijk*
  — they must fit the turnover, which is what an inspection compares.
- **Zelfstandigenaftrek 2026: €1,200.** Capped at winst vóór ondernemersaftrek;
  the cap does not apply when the startersaftrek is claimed; unused amounts can
  be carried forward 9 years (non-gerealiseerde zelfstandigenaftrek, fixed by
  beschikking); halved from AOW age. (belastingdienst.nl)
- **Startersaftrek 2026: €2,123**, added to the zelfstandigenaftrek when the
  person was not an ondernemer in one or more of the previous 5 calendar years
  and applied the zelfstandigenaftrek at most twice. Usable up to 3 times in the
  first 5 years; it also lifts the cap at profit level.
- **Mkb-winstvrijstelling 2026: 12.7%** of the winst after ondernemersaftrek
  (also 12.7% in 2025; 13.31% in 2024). The benefit is calculated at 37.56%; it
  also reduces a loss, which is a disadvantage.
- **Stakingsaftrek: €3,630** (2026), once per lifetime.
- Box 1 rates 2026 for someone below AOW age: 35.75% up to €38,883, 37.56% to
  €78,426, 49.50% above.
- Announced but future: the zelfstandigenaftrek drops to €900 on 1 Jan 2027.
  Verify in the Belastingdienst 2027 subtree before quoting — corroborated by
  advisor pages only, so treat as *not yet verified*.

## 6. Health cover (Zvw) and disability insurance

- Everyone resident in the Netherlands is Zvw-insured; a self-employed person
  carries the whole cost with no employer contribution. Nominal premium plus an
  income-related contribution levied via a (voorlopige) aanslag: **2026: 4.85%**
  (5.26% in 2025) over a maximum bijdrage-inkomen of **€79,409**, i.e. at most
  about **€3,851/year**. Zorgtoeslag is possible below the income threshold.
  (belastingdienst.nl)
- Health-insurance premiums and the eigen risico, mandatory or voluntary: **not
  deductible**; amounts received from the insurer are not taxable.
  (belastingdienst.nl)
- **No ZW/WAO/WW for the self-employed**; maternity pay runs via UWV (16 weeks or
  more).
- **AOV is not compulsory.** Premium treatment: deductible in box 1 as `uitgaven
  voor inkomensvoorzieningen` **only if the policy pays a periodic benefit**, and
  you must be policyholder, insured and beneficiary yourself; it is *not* a
  business expense. A lump-sum policy: premium not deductible, payout untaxed.
  (belastingdienst.nl, ondernemersplein.overheid.nl)
- Public basisverzekering in the pipeline — **Wet BAZ** (wetsvoorstel 36912,
  submitted to the Tweede Kamer 24 Mar 2026 after a critical Raad van State
  advice, expected to start around **2030** at the earliest): premium ~5.4% of
  profit capped around €171 gross/month, benefit 70% of income up to minimum
  wage, 104-week waiting time, two-payer execution (UWV assesses/pays, the
  Belastingdienst collects). DGA's and resultaatgenieters fall outside it;
  meewerkende partners per current information too. Take out a qualifying private
  AOV **before the peildatum** to fall under the transition right (waiting time
  ≤ 24 months, cover to at least age 55, in the entrepreneur's own name); after
  it, only a stricter opt-out applies. A schenkkring/broodfonds does not replace
  the compulsory scheme but can bridge the waiting time.
- Liability: an eenmanszaak has no legal personality — business debts reach
  private savings and the home.

## 7. Gemeente Den Haag: business from home

No omgevingsvergunning needed when **all** of these hold: the work happens in the
home and its outbuildings; the owner is a zzp'er; at most **30% of the floor area
and at most 40 m²** (about one room) is used for work; the home still looks like a
home (no facade or exterior advertising); no products are sold from the home and
no food is prepared there for sale; no nuisance from traffic, parking, noise or
odour; no sexual services. A bed and breakfast usually does need an
omgevingsvergunning. The bedrijfsactiviteitenvergunning applies only to publicly
accessible businesses in designated shopping areas (Transvaal, Laak, Escamp,
Segbroek) — irrelevant to a home-based tech freelancer. Info: gemeente 14070.
Verify a specific address in the Omgevingsloket. (denhaag.nl)

## 8. Passed but pending / watch list

- Enforcement against schijnzelfstandigheid resumed on 1 January 2025 after the
  moratorium ended (initially without fines).
- The verduidelijking half of the Wet VBAR was dropped; the surviving bill
  (36.783) introduces a **rechtsvermoeden of employment below €38/hour**
  (peildatum 1 January 2026), shifting the burden of proof to the opdrachtgever.
  Adopted by the Tweede Kamer on 21 Apr 2026 and by the Eerste Kamer on 16 Jun
  2026, published in the Staatsblad on 29 June 2026 (Stb. 2026, 158), with entry
  into force at a date set by koninklijk besluit — so it applies only from that KB
  date, which the law text does not fix. Do not call it the Wet VBAR.
- A Zelfstandigenwet (initiatiefwet) on the employee/self-employed distinction
  is in preparation; do not quote its contents as law.

## 9. Output skeleton for the user answer

Order the reply so the *mandatory* items come first and the optional ones second,
which is what the user actually asks for ("what else do I need"):

- **必须做** = wait for and keep the two number letters, Mijn Belastingdienst
  Zakelijk + DigiD, know your aangiftetijdvak and deadlines, decide KOR, invoice
  correctly + keep records 7 years, log hours from day one, pay the Zvw
  contribution.
- **建议做** = business bank account, AOV timing, AVB, home-office rules, digital
  post.
- **Last:** the law-in-motion items as a single short note, clearly labelled as
  not-yet-in-force.

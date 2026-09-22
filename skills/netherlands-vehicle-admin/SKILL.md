---
name: netherlands-vehicle-admin
description: "Use for Dutch vehicle administration — RDW open data, kenteken (license plate) format and sidecode decoding, BPM/MRB/bijtelling/WAM, import and registration, and car insurance."
version: 1.0.0
author: sixgod
license: CC BY-NC 4.0
metadata:
  hermes:
    tags: [netherlands, rdw, kenteken, license-plate, sidecode, bpm, mrb, bijtelling, wam, insurance, import, registration, apk, schorsing, milieuzone]
    category: productivity
    related_skills: [pdf, docx, geely-starray-em-i, dutch-official-documents, dutch-parking]
---

# NL Vehicle Administration — plates, RDW data, taxes, insurance

Treats a car in the Netherlands as a public-record object: reading RDW open data, decoding and
validating the kenteken, the four separate vehicle taxes, the WAM insurance duty, and what
import and registration actually involve. Written for both a privately held car and a
B.V.-registered car driven by a private individual — the B.V. changes the insurance, BTW and
bijtelling answers, never the RDW facts.

Sibling skills: model/infotainment questions for a specific car live in `skills/geely-starray-em-i/`;
municipal permits, street tariffs and P+R live in `skills/dutch-parking/`; producing the
Dutch declarations and letters that vehicle admin sometimes needs lives in
`skills/dutch-official-documents/`.

## Rule 0 — ground every vehicle fact in RDW open data, not in what the user wrote

No API key needed. Run both before any kenteken, model, weight or price enters a document or an
answer (`XX999X` is a placeholder — substitute the plate you are actually looking up):

```bash
curl -s "https://opendata.rdw.nl/resource/m9d7-ebf2.json?kenteken=XX999X"   # voertuig
curl -s "https://opendata.rdw.nl/resource/8ys7-d773.json?kenteken=XX999X"   # brandstof + CO2
```

- Query param: uppercase, no dashes. In documents: with dashes (`XX-999-X`).
- `m9d7-ebf2` gives `merk`, `handelsbenaming` (RDW's spelling is authoritative; user-supplied model
  names are routinely misspelled), `massa_ledig_voertuig`, `massa_rijklaar`, `catalogusprijs`,
  `bruto_bpm`, `datum_tenaamstelling`, `datum_eerste_toelating`, `wam_verzekerd`.
  `8ys7-d773` gives fuel type, `emis_co2_gewogen_gecombineerd_wltp`,
  `klasse_hybride_elektrisch_voertuig`.
- Correct the spelling in the document to RDW's and say you did; never reproduce the user's typo in
  an official paper.

**`wam_verzekerd: "Nee"` is an act-now finding — raise it unprompted.** The WAM duty starts on the
tenaamstelling date, RDW cross-checks the register automatically and fines (up to ~€600, repeatable
within a year), and uninsured damage is the holder's own liability. Ask the user to confirm both
that the policy is live and that the insurer reported it to RDW — but check the timing first:
insurers report in batches, so a policy bought the same day can still show `Nee` legitimately.

## The kenteken (license plate): format, sidecode, validation

Dutch plates are **vehicle-bound** (voertuiggebonden), not person-bound as in Belgium: the plate
follows the car through a transfer, and the register is keyed on it, not on the owner.

- **Sidecode generations.** Since 1951 plates are issued in numbered *sidecodes* — **01–14** in RDW's
  series overview, and there is no 15 or 16. Each has a fixed letter/digit mask, so the mask alone
  dates a first registration. Full mask table, validation algorithm and the vision pipeline for
  reading a plate off a photo: `references/license-plate-sidecodes.md`.
- **Letter pool.** Vowels `A E I O U` and the confusion-prone `C Q W Y` are excluded, leaving
  `B D F G H J K L M N P R S T V X Z` (17 letters). Older generations (01–03) and special
  categories (diplomatic, export, temporary) can contain non-pool letters — flag those as
  non-standard rather than rejecting the plate.
- **Length.** Every Dutch plate is **6 characters** — only the hyphen grouping varies by sidecode.
  Display groups the characters with hyphens; RDW's API and most parking systems want them without.
- **Validate before you submit a plate anywhere.** Parking and municipal systems identify the user
  by plate, and a mistyped plate is a fine, not an error message. Use the bundled parser:

  ```bash
  python3 scripts/dutch_kenteken.py XX-999-X      # single plate
  python3 scripts/dutch_kenteken.py --batch plates.txt
  python3 scripts/dutch_kenteken.py --json XX999X
  ```

- **Ambiguity is real**: a bare 6-character string can regroup into more than one sidecode. Ask for
  the exact grouping shown on the car or the document instead of guessing the generation.
- **Only a kenteken unlocks public verification.** No public RDW channel accepts a VIN/chassisnummer,
  so a dealer who hands over a VIN-only paper is handing over a car that is not registered yet. What
  that means for a purchase, plus green dealer plates (`handelaarskenteken`):
  `references/import-registration-and-dealer-plates.md`.

## Taxes: four separate things, never conflated

- **BPM** (Belasting van personenauto's en motorrijwielen): one-off registration tax, CO2-bracketed,
  owed by the kentekenhouder, collected and remitted by the dealer — that is why it is its own line
  on a car invoice. Not a deductible input VAT; it is part of the asset's cost base. The figure
  charged on an imported car is lower than RDW's `bruto_bpm` because a depreciation date was
  approved — a gap is normal, not an error.
- **BTW**: deductible input tax for a company car with business use; private use by an employee
  needs a correction or runs through bijtelling. Say it is the bookkeeper's call rather than ruling
  on it.
- **MRB** (motorrijtuigenbelasting / wegenbelasting): per quarter, by weight + fuel + province.
  Calculate off `massa_rijklaar` (massa ledig + 100 kg), weight class = round up to the next 100 kg.
  PHEVs lost their discount from 2026 and pay the full petrol rate; only zero-emission cars get a
  discount (30% 2026–2028, 25% in 2029, none from 2030).
- **bijtelling**: taxable addition for private use, base = catalogusprijs incl. BTW and BPM; PHEVs
  sit on the standard rate. It is the employer's payroll matter — a one-line pointer, never the
  whole answer.

**Never multiply the national MRB rate by the opcenten percentage** — provincial opcenten are levied
over a frozen 1-4-1995 base table (art. 222 Provinciewet), far lower than the current tariff; using
the national figure inflates the total by roughly 2×. When published sources disagree on a
province's opcenten percentage (they do), name the discrepancy instead of averaging it. Exact
charge: the Belastingdienst tool "Motorrijtuigenbelasting berekenen" with the kenteken, or
0800-0749.

2026 figures, the rijksdeel/opcenten split and a worked calculation: `references/rdw-and-auto-taxes.md`.

## Insurance (WAM)

- The duty sits on the **kentekenhouder**: a company-registered car must be insured by the company
  on a business policy. A private policy for a company-plated car is refused, or refused at claim
  time — do not suggest it; the only clean route is transferring the tenaamstelling, which is an
  asset/tax event, not a paperwork trick.
- Declare every regular driver, the nightly parking address and the mileage. WA follows the car,
  casco follows the declared driver: an undeclared regular driver can mean a refused claim, regres
  against the driver, and a CIS registration ("fronting").
- New car → volledig casco, not WA/WA+ (WA+ covers only theft/fire/glass). Add
  Schadeverzekering inzittenden (WA does not cover the at-fault driver's own injury), extend
  nieuwwaarderegeling from the default 1 year to 3 (conditions: first owner, ≤1.000 km at purchase,
  not imported, below the insurer's price cap), and get written confirmation the traction battery is
  covered.
- Timing: policy live and reported to RDW at or before tenaamstelling; dealers usually release the
  car only against proof of cover.
- Young-driver surcharges typically start below ~25 years — check the driver's age before warning
  about them.
- Phone/email of the company are optional on a declaration; if they are missing, drop those lines
  entirely rather than leaving placeholder markers on a page meant to be signed.
- Schadevrije jaren sit nationally in Roy-data (SEPS), attach to the **policyholder**, and can be
  requested with the SEPS form at seps.nl/roy-data. A company policy builds no personal years for
  the driver — the mechanic, the claim cost and the `afstandsverklaring` route:
  `references/rdw-and-auto-taxes.md`.

## Import, registration and connected services

- A car whose `datum_eerste_toelating` sits well before its Dutch `datum_tenaamstelling` is an
  import — that gap is what explains both the approved BPM depreciation and the kenteken's history.
  Ask for the gap before quoting a tax or a history.
- New imports take roughly 1–2 weeks to register; an already-registered car changing hands is
  same-day ownership transfer. A car delivered on green dealer plates is **not** registered yet.
- **"No app control and no data" on a Dutch-plated car is usually a missing backend link, not user
  error.** Diagnosis order, the hotspot test that separates a missing data bundle from an unlinked
  VIN, and what to demand from a parallel importer in writing:
  `references/connected-services-and-apps.md`.

## Adjacent duties worth one line each

- **APK** — `vervaldatum_apk` in RDW; an expired APK carries its own fine (see the parking skill's
  rate notes).
- **Schorsing** — suspension stops both the MRB and the WAM duty; useful for a car standing still
  for months.
- **Milieuzone / emission zones decide access, not parking.** Check the fuel and emission class in
  RDW (Rule 0) before promising free passage into a city centre or warning about a ban — and check
  the vehicle, not the model name.
- Dutch paid-hours and permit-zone matters belong to `skills/dutch-parking/`; when a
  permit or a declaration does need vehicle data, take it from RDW rather than from what the user
  typed.

## Working rules

- Never invent identifiers, dates or amounts to fill a template — leave the marker, list it as
  missing, or ask.
- Flag substantive oddities in the user's own input instead of quietly going along with them.
- Re-check rate figures for the year asked about rather than reusing the ones above silently: BPM
  brackets and MRB rates are indexed annually.

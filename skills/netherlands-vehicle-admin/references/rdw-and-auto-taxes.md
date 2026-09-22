# RDW data, BPM/BTW/MRB/bijtelling, WAM — depth notes

## RDW open data (no API key)

| Dataset | URL | Use |
| --- | --- | --- |
| Gekentekende voertuigen | `https://opendata.rdw.nl/resource/m9d7-ebf2.json?kenteken=<KEN>` | merk, handelsbenaming, masses, catalogusprijs, bruto_bpm, dates, `wam_verzekerd` |
| Brandstof/uitstoot | `https://opendata.rdw.nl/resource/8ys7-d773.json?kenteken=<KEN>` | brandstof_omschrijving, CO2 WLTP, hybrid class |
| Assen / carrosserie / klasse | `3huj-srit`, `vezc-m2t6`, `jhie-znh9`, `kmfi-hrps` | sub-tables, linked from the voertuig record |

Query with the kenteken uppercased and without dashes. The voertuig record lists its own sub-table
URLs, so one call discovers the rest.

Fields that earn their keep:

- `handelsbenaming` — official model spelling; put this in documents.
- `massa_ledig_voertuig` / `massa_rijklaar` — the latter is the former + 100 kg.
- `catalogusprijs` — bijtelling base and the price that matters for value questions (includes BTW
  and BPM).
- `bruto_bpm` — gross BPM; when the invoice line is lower, an approved depreciation date
  (`registratie_datum_goedkeuring_afschrijvingsmoment_bpm`) explains it.
- `datum_tenaamstelling` vs `datum_eerste_toelating` — a gap means an imported/parallel-import car;
  explains BPM depreciation and the kenteken's history.
- `wam_verzekerd` — insurance status per RDW. `Nee` on a registered car = tell the user today, but
  check the timing first: insurers report policies in batches, so a policy bought the same day can
  still show `Nee` legitimately. Allow roughly one working day, re-query, and only then push the
  broker for confirmation plus an artikel 34 WAM-verklaring as paper proof.
- `vervaldatum_apk` — APK expiry; APK and schorsing are the two fields that answer "what does
  owning this cost / what can I let slide" questions.

## MRB calculation, the honest way

Components (per quarter, personenauto, Wet MRB art. 23):

1. **Rijksdeel** — from the weight class of `massa_rijklaar`. Workable 2026 shape: base class 900 kg
   = €64,24 plus **€17,27 per 100 kg above 900 kg**. Petrol and petrol+electric (PHEV) pay no fuel
   surcharge; diesel and "other" do (diesel also carries a fine-particle surcharge).
2. **Provinciale opcenten** — a percentage *of the frozen 1995 base table*, not of the rijksdeel.
   2026 provincial percentages run from roughly 82 (Noord-Holland) to roughly 104 (Zuid-Holland), so
   Zuid-Holland is the most expensive province for this. The 1995 base climbs by about €46,74 per
   year per 100 kg above the 1.000 kg class.
3. Zero-emission only: multiply by 0,70 (30% discount, 2026–2028).

Worked example (1.845 kg rijklaar, petrol PHEV, Zuid-Holland, 2026): rijksdeel ≈ €219,67 per quarter
→ ≈ €879/year; opcenten ≈ €145–158 per quarter → total ≈ **€1.400–1.550 per year, i.e.
≈€350–390 per quarter**. Present it as an estimate: the opcenten percentage had two conflicting
published values, and the Belastingdienst shifted its weight measure from massa ledig to massa
rijklaar mid-2026.

Rates move annually (indexation plus bracket tightening) — re-check the statute text or the
Belastingdienst page for the year asked about instead of reusing these numbers silently. Exact
figure: hulpmiddel "Motorrijtuigenbelasting berekenen" on belastingdienst.nl, or BelastingTelefoon
Auto 0800-0749.

A discount exists only for zero-emission cars (30% in 2026–2028, 25% in 2029, gone from 2030).
PHEVs lost their discount from 2026 and are charged the full petrol rate. **Schorsing** (suspension
of the registration) stops the MRB and the WAM duty for as long as it runs.

## BPM in one paragraph

A one-off tax on first registration in NL, CO2-bracketed (brackets narrow and per-gram rates rise
each year; 2026: thresholds −1,55%, rates +1,57%), owed by whoever registers the car, normally filed
and remitted by the dealer — hence its own invoice line. Zero-emission and some special vehicles get
a reduced rate. It is capital, not deductible VAT: a company buying the car capitalises it and
depreciates it, it does not reclaim it.

## BTW and bijtelling, kept short

- A company car used for business has deductible input BTW; private use needs a correction or runs
  through bijtelling. Which route applies is the bookkeeper's call — say so and hand the question on.
- bijtelling is the payroll addition for private use of a car the employer makes available. Base is
  `catalogusprijs` incl. BTW and BPM; PHEVs sit on the standard rate. One-line pointer only — it is
  a loonheffing matter, not a vehicle-register matter.

## WAM / insurance duty

- Art. 2 WAM: both the bezitter and the registered kentekenhouder must insure the vehicle, so a
  B.V.-held car needs a policyholder = the B.V., on a business policy.
- Insurers check the policyholder against the RDW register; a policy held by someone who is not the
  holder creates an ownership/claim problem, and Kifid case law backs refusing cover where the
  holder or regular driver was misrepresented.
- WA travels with the car: any driver with permission is covered towards third parties. Casco does
  not travel with an undeclared regular driver — refusal and regres are documented outcomes, and the
  insurer may log the case in CIS/incidentenregister.
- Schadevrije jaren: one per claim-free year, held nationally in Roy-data (SEPS). A claim costs 5
  years, and a driver with more than 15 drops back to 10; the years lapse after 3 years without a
  policy in your own name. They attach to the **policyholder**, so a company policy builds no
  personal years for the driver — someone who only ever drove a company car starts at 0 when they
  later insure privately. A named driver can recover years with an `afstandsverklaring` from the
  former insurer — worth telling a driver who is not the holder. Consumers request their own record
  through the SEPS form at seps.nl/roy-data (insurers query Roy-data directly; neither the user nor a
  broker can read it online). Never let a user guess or inflate the number in an application: the
  insurer checks Roy-data and a wrong answer is a mededelingsplicht breach that can void cover.
- Reporting is batched at the insurer's side, so a same-day policy can legitimately still show
  `Nee` in RDW. Allow about one working day, re-query, then ask the broker for confirmation plus an
  artikel 34 WAM-verklaring as paper proof.

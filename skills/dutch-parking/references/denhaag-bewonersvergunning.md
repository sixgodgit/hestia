# Den Haag bewonersvergunning (resident parking permit) for a company car

## Who applies, and what the permit is bound to

- The applicant must be a **resident registered in the BRP at the address** the permit is for — never the company, even when the company owns the car.
- The permit is bound to **person + kenteken + address**, is valid only in the vergunninggebied where the holder lives, and at most 3 resident permits are granted per address.
- A permit is only needed inside a **vergunninggebied**. Check the street on the municipality's parking-cost map before starting paperwork: in Laak, zones differ and some paid windows are evening-only (Laakkwartier 18.00–24.00). Outside a zone there is nothing to apply for.
- The applicant must not have usable parking on own premises, and not live in a building/complex excluded from resident permits. (Policy has moved this way explicitly: from April 2026 residents who have parking on their own property are no longer eligible for a street permit.)

## Company car → the holder must declare

A car registered to an employer/company needs a declaration from the holder with the application. Den Haag's own wording requires it to state the **kenteken**, the **period** the driver will use the car, and that the driver needs it for work for **at least three months**. The statutory berijder definition is "the fixed driver, with the holder's consent, for longer than three months", and the instrument is a **berijders-/werkgeversverklaring**. Where the kenteken sits with a lease company, a declaration between lease company and employer is also required.

Clause set that satisfies it (this is the skeleton that has been used for a delivered declaration; fill in the placeholders):

1. Company is the registered holder of kenteken `<kenteken>` (merk/type, VIN).
2. Car is placed at the disposal of the named driver, born `<date>`, BRP-registered at the address the permit is applied for; the driver is the fixed driver.
3. Period `<start>`→`<end>`, more than three months; variant A: the driver needs it structurally for work at the company — variant B: the holder consents to the driver using and parking it (no employment).
4. In that period the car is parked at/around the residential address; to the holder's knowledge the driver has no usable parking on own premises.
5. Issued for the permit application; the company expressly consents to use and parking at that location.
6. Change of holder, end of use, or anything affecting the permit's validity is reported to the municipality within five working days.
7. Municipality may contact the signatory via the details given.

Then place/date, signature, name, function, company stamp, and an attachments list (RDW registration extract showing the company as holder, KvK extract, signatory's ID on request, optionally the employment contract).

## Rules and risks to state plainly

- Variant A (driver actually works for the company) is what the municipality expects for a company car. Variant B (family member, not employed) is defensible on the berijder definition but may trigger a request for proof of employment — say so instead of implying both are equally safe.
- Keep the use period coherent: start before the application date, span more than three months. A term ending decades out reads as fabricated; offer either a near-term end date or "onbepaald, in ieder geval langer dan drie maanden" and let the user choose.
- Policy and forms change (residents have had to re-apply once); tell the user to re-check denhaag.nl before submitting.
- Use the company's registered address in the letterhead — spell the street exactly as the municipality does and verify that spelling against the postcode before it reaches the municipality; the city is spelled `Den Haag`. The residential address is the address the permit is applied for.
- Submission address: Handhavingsorganisatie, Antwoordnummer 1435, 2501 VE Den Haag (no postzegel). Parking desk: 14070. Permit portal: `parkervergunningen.denhaag.nl` (MijnDenHaag).

## After the grant — read the result back, then state the two limits

Read the granted `Zone omschrijving` back against the zone map already produced rather than re-deriving it, and check the validity window against the permit year (a permit year that runs 1 March to the last day of February makes an end date in late February the cycle, not an error). Then say the two limits the holder will actually hit:

- The zone is **only the outlined area**. With the Centrum permit zone the neighbouring Centrum Zuid zone starts a street or two to the south, so a car parked a few doors outside the outlined area is a violation, not a rounding error.
- The `01A`–`01D` street segments inside the Centrum zone are excluded from the permit.

Edge cases met in practice: an application against a company-held car is decided almost entirely on the berijders-/werkgeversverklaring, so a missing or vague declaration is the usual cause of a request for more information; the check that bites afterwards is the "no usable parking on own premises" condition, which is now enforced policy rather than a formality; and a granted permit still needs the zone geometry checked, because the portal's `Zone omschrijving` names the zone while only the map shows its outline.

## Bezoekersvergunning (visitor permit) — the constraint is hours, not area

A bewonersvergunning lets *the holder* park; a visitor permit buys *the holder's visitors* hours. One per address per calendar year, valid **in the zone of the address it was applied for** — so a zone-18C permit does nothing for visitors to a zone-01 home. Ask which address it is bound to before analysing it.

The year's allowance is set by the zone's **weekly operating hours** (art. 5.10 lid 5, Regeling parkeerregulering Den Haag):

| Weekly paid hours | Hours per year |
|---|---|
| ≤ 50 | **138** |
| 51–75 | 203 |
| 76–100 | 268 |
| 101–125 | 332 |
| 126+ | 366 (the Scheveningen zone, top band) |

Derive the weekly figure from the parsed `WERKINGSTIJDEN` windows (cross-midnight counted once, overlapping regimes the highest) rather than reading it off a page:

| Zone | Weekly hours | Quota |
|---|---|---|
| 18C Laakkwartier–Laak (daily 18.00–24.00) | 42 | 138 |
| 18F Noordpolderbuurt | 96 | 268 |
| 18B Laakhaven, 01 Centrum | 101 | 332 |

An evening-only zone therefore lands in the lowest band *while covering 2.13 km²* — larger than 18B (0.74), zone 30 (1.44) or zone 32 (1.28). Give both numbers, then the part that actually bites: **outside the paid window visitors park free and spend no quota**, so a small quota tracks a short window and only evening visits consume it. 138 hours ≈ 23 full six-hour evenings; Centrum's 332 ≈ 55.

Money and rules (denhaag.nl, page updated 2026): €34,10 per year; €50 buys 50 extra hours once a year; unused hours carry over up to 50. The holder must **check the visitor in and out himself** (the visitor never pays), may only park his own visitors, and loses the permit for selling hours. `De bezoekersvergunning geldt niet in winkelstraten tijdens winkeltijden` — the same class of exclusion as the `01A`–`01D` corridors. Not issued for Palaceplein, Energiekwartier, CS-Oost/Grotiusplaats.

## Producing the declaration package

Keep the package generated, not hand-written: a small JSON data file drives a script that emits the PDF/DOCX (page 1 Dutch = the submission version, page 2 a Chinese translation, page 3 instructions), and finished versions are archived into an `archief/` folder. Regenerate from the JSON instead of hand-editing the PDF, so the next change is one field rather than a re-layout.

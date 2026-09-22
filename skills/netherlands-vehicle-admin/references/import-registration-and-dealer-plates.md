# Import, registration and dealer plates

## Green dealer plates (handelaarskenteken)

Green plates in the Netherlands are **handelaarskenteken** — trade/dealer plates. They are
registered to the **dealership**, not to a vehicle, and can be temporarily mounted on any vehicle in
the dealer's inventory.

| Feature | Green plate (dealer) | Regular plate |
| --- | --- | --- |
| Colour | Green background, black text | Yellow background, black text + blue EU strip |
| Registered to | Dealership | Vehicle owner |
| Use | Test drives, transport, demos, repairs | Everyday driving |
| Insurance | Dealer's trade-plate policy | Owner's / holder's own policy |

### When you see them

- **Test drives.** The dealer mounts the green plate on an unregistered or freshly imported car so a
  prospective buyer can legally drive it. Standard practice, covered by the dealer's trade-plate
  insurance.
- **New imports.** A freshly imported car may not have its permanent Dutch registration yet; the
  green plate covers test drives and transport until the RDW registration completes.
- **Unregistered stock.** Cars sitting at the dealer without a kenteken can still be moved and
  displayed on green plates.

### Legal restrictions (they bind the dealer, not the buyer)

Enforced by RDW, including via ANPR:

- business use only — test drives, transport, demonstrations, repairs; no private or commuting use,
- no residential parking as if it were a regular plate,
- no lending to third parties,
- misuse → RDW intervention: warning, suspension or revocation of the dealer's recognition, plus
  fines.

### What it means for a buyer

A test drive on a green plate is normal and legal. It does **not** mean the car is used or damaged,
that the dealer is doing anything improper, or that the car cannot be registered. It **does** mean:

- the car was probably not registered yet (or only just imported) at the time of the test drive,
- ask the dealer for the **kenteken** at delivery — a car with only a VIN/chassisnummer and no
  kenteken means registration is still in progress,
- the dealer handles the RDW registration (`kenteken aanvragen`), which takes **~1–2 weeks** for a
  new import; an already-registered car changing hands is a same-day ownership transfer.

**At delivery the car should carry its permanent Dutch plates.** If it is still on green plates,
registration is not complete — do not accept delivery in that state.

## Why a VIN alone cannot be checked (RDW's public channels)

If all you have is a VIN/chassisnummer, you **cannot** verify Dutch registration status, mileage
history or ownership through any public RDW channel:

| Channel | Accepts VIN? | Accepts kenteken? |
| --- | --- | --- |
| RDW Kentekencheck (ovi.rdw.nl) | ❌ | ✅ Dutch plates only |
| RDW Open Data API (opendata.rdw.nl) | ❌ main dataset `m9d7-ebf2` has no `chassisnummer` column | ✅ |
| RDW OVI API endpoints / internal API | ❌ (404 or redirect to an HTML page) | ✅ |

This is by design: the VIN is treated as sensitive data, reachable only through authorised channels
(insurers, fleet operators, police, RDW-recognised parties). The Kentekencheck page says so itself —
"Vul hier uw kenteken in (alleen Nederlandse kentekens toegestaan)".

Practical consequences:

- **Dealer gives only a VIN, no kenteken** → the car is not registered yet, or registration is in
  progress. Normal for a new import, but it should be disclosed, and it means no public verification
  is possible until the plate exists.
- **Once the dealer registers the car, they must give you the kenteken.** That plate is the only key
  to the public register (`references/rdw-and-auto-taxes.md`).
- **Authorised VIN→kenteken routes do exist** — RDW's "Voertuiggegevens op basis van
  chassisnummer" for insurers and fleet operators, and paid business accounts at third-party
  services such as Autotrack or CarCheck. Private individuals cannot use them.

### If you must work from the VIN

1. Ask the dealer for the kenteken once registration completes.
2. Use the VIN for international checks — Carfax-style services, though coverage for Chinese-market
   cars is limited.
3. NHTSA's batch decoder (`https://vpic.nhtsa.dot.gov/api/vehicles/DecodeVINValuesBatch/`) can
   decode basic make/model/year, but often returns empty for Chinese-market VINs.

VIN structure, generically: characters 1–3 are the WMI (world manufacturer identifier), character 9
is the check digit, character 10 encodes the model year, and the tail is the production sequence.
Reading a VIN that way is not proof of registration — only the decode of a specific example, e.g. a
placeholder VIN `LB3P11SD6TH000000`: `LB3` = manufacturer, `T` in position 10 = 2026 model year,
`6` in position 9 = check digit, `000000` = sequence. That says "a 2026 car of that make", nothing
about a Dutch plate.

## Import-related pitfalls

- Take `datum_eerste_toelating` **and** `datum_tenaamstelling` from RDW before quoting a price, a tax
  or a history: a wide gap is the signature of a parallel import, and it explains why the BPM line is
  below `bruto_bpm`.
- A parallel import often never went through the importer's connected-car provisioning. Symptom and
  what to demand from the seller in writing:
  `references/connected-services-and-apps.md`.
- Warranty is a separate matter from provisioning: an EU-wide manufacturer warranty generally still
  applies to a parallel import, but the official network may charge for, or decline, connected-services
  work on a car that is not in its sales file.

## Sources

- RDW: green plates recognised by ANPR; misuse triggers investigation. Kentekencheck accepts Dutch
  plates only.
- Jurautotransport.nl: dealer plates for test drives, transport and demos.
- infopolitie.nl: green plates restricted to garages/dealers/repair shops.
- autoenfiscus.nl: no residential parking on green plates.

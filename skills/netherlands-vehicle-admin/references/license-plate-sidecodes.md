# Dutch kenteken — sidecode generations and validation

## What a sidecode is

Since 1951 the Netherlands issues plates in numbered **sidecode** generations (01–14 per RDW's
series overview — there is no 15 or 16). Each
generation has one fixed mask, so the mask of a plate dates the vehicle's first registration to an
era. Display uses hyphen-separated groups; RDW's API and most parking systems want the characters
without hyphens. A plate is **voertuiggebonden** — bound to the vehicle, so it travels with the car
through a transfer — unlike the Belgian person-bound plate.

## Letter pool

Plates exclude the vowels `A E I O U` and the confusion-prone `C Q W Y`, to avoid offensive words
and misreading. Left over:

```
B D F G H J K L M N P R S T V X Z   (17 letters)
```

Older generations (sidecode 01–03) and special categories (diplomatic, export, temporary) may
contain letters outside that pool. Flag those as *non-standard*; do not reject the plate outright.

## Sidecode table

Every Dutch plate is **6 characters**; only the hyphen grouping differs per sidecode. RDW's series
numbering ends at **14** — there is no generation 15 or 16.

| Code | Mask | From (any category) | Cars since | Notes |
| --- | --- | --- | --- | --- |
| 01 | `XX-99-99` | 1951 | — | earliest generation, may contain non-pool letters |
| 02 | `99-99-XX` | 1951 | — | |
| 03 | `99-XX-99` | 1951 | — | |
| 04 | `XX-99-XX` | 01-10-1988 | — | starts on trailers and semi-trailers |
| 05 | `XX-XX-99` | 03-01-1994 | — | starts on heavy goods vehicles |
| 06 | `99-XX-XX` | 20-01-2000 | 20-01-2000 | |
| 07 | `99-XXX-9` | 01-09-2005 | 19-05-2008 | |
| 08 | `9-XXX-99` | 26-02-2009 | 05-03-2013 | |
| 09 | `XX-999-X` | 11-08-2006 | 30-03-2015 | |
| 10 | `X-999-XX` | 11-12-2008 | 19-08-2019 | |
| 11 | `XXX-99-X` | 16-01-2015 | 04-06-2024 | |
| 12 | `X-99-XXX` | 01-12-2021 | — | not yet issued on cars |
| 13 | `9-XX-999` | 23-05-2016 | — | |
| 14 | `999-XX-9` | 13-06-2019 | — | |

Source: RDW, *Overzicht van kentekenseries* —
<https://www.rdw.nl/de-kentekenplaat/overzicht-van-kentekenseries>. RDW publishes dates per vehicle
category; "From" is the earliest launch date for any category, "Cars since" is when the series
reached passenger cars, which is the number that dates a car. A series can therefore be younger by
category: 09 and 10 ran on mopeds years before cars.

`XX-999-X` above is a placeholder showing the mask shape and the display format — substitute the
plate you are actually looking up.

## Validation algorithm

1. **Clean.** Uppercase, strip hyphens and spaces:
   `raw = plate.strip().upper().replace("-", "").replace(" ", "")`
2. **Length.** Exactly 6 characters — every Dutch plate is 6 characters regardless of sidecode.
   Anything else is invalid input.
3. **Regroup and match.** Re-slice the cleaned string into the hyphen groups of each generation's
   mask and regex-match. The first generation that matches wins — the masks are mutually exclusive
   once the grouping is known.
4. **Letter pool (optional).** `LETTERS = "BDFGHJKLMNPRSTVXZ"`; a letter outside that set is
   reported as non-standard rather than as invalid.

The executable form of this — masks, per-generation slicing and the letter-pool report — is
`scripts/dutch_kenteken.py`:

```bash
python3 scripts/dutch_kenteken.py XX-999-X      # single plate, also accepts XX999X and "XX 999 X"
python3 scripts/dutch_kenteken.py --batch plates.txt
python3 scripts/dutch_kenteken.py --json XX999X # machine-readable, for batch validation
python3 scripts/dutch_kenteken.py               # interactive, empty line to quit
```

Its output gives the normalised plate, the sidecode, the display grouping and the era
(e.g. sidecode 11 → 2015). Use it before a plate is submitted to any parking or municipal system,
and to date a vehicle from its plate when no RDW lookup is possible. The script is not a substitute
for RDW: sidecode gives an era, never the model, weight or tax data — those come from the RDW open
data endpoints in the main SKILL.md.

**Provenance of this table.** The mask table above was rebuilt from RDW's *Overzicht van
kentekenseries* and is exercised by the bundled script. An earlier version of this reference carried
a shifted table — sidecode 09 as `XXX-99-X`, 11 as `XX-999-X`, 13 as `99-X-XXX`, 14 as `XXX-X-99` —
plus two generations (15 and 16) that RDW does not issue, and a 7-character length rule. That
version rejected genuine plates of several generations. RDW remains the authority: re-check the
series overview before relying on a single row.

## Reading a plate from a photo

1. **Verify the vision path first with a synthetic image** (PIL): a yellow background, a dark border,
   an EU blue band on the left, then the plate characters. Save to `/tmp` and run `vision_analyze`
   on it, to confirm the model can read Dutch plates at all before trusting it on real input.
2. **Then run `vision_analyze` on the user's image** with a narrow prompt: "This is a Dutch license
   plate. Read the complete alphanumeric characters including hyphen positions. Output only the plate
   characters."
3. **Cross-validate the OCR result against the sidecode validator above.** An OCR misread usually
   produces a string that matches no generation, or one with non-pool letters — treat either as
   "ask the user to confirm", never as a value to submit.

## Pitfalls

- **Ambiguity without hyphens.** A bare 6-character string can regroup into more than one
  generation. Ask for the exact grouping printed on the vehicle or document; if the user cannot
  supply it, report the candidates rather than picking one silently.
- **Letter-pool exceptions.** Diplomatic plates start with `CD`; export and temporary plates have
  their own series. Accept them when the context fits, flagged as non-standard.
- **Motorcycles** use the sidecode system too, but their plates are physically smaller — a size cue
  is not a format cue.
- **Mopeds (bromfiets) are a different format** (and a different background colour). Do not validate
  them against the car sidecodes, and do not confuse them with the green dealer plate
  (`handelaarskenteken`) described in `references/import-registration-and-dealer-plates.md`.
- **A plate is not an identity.** It is vehicle-bound: it says nothing about who owns or drives the
  car, and after a sale the same plate appears on a different holder in the register.

## Integration with parking and municipal systems

- The system decides the accepted form: some fields want the **normalised** plate (no hyphens), others
  the **display** grouping. Confirm which, per system, before submitting.
- A mistyped plate in a parking system is a fine, not a validation error — validate first.
- For Den Haag visitor parking (`parkerendenhaag.denhaag.nl` and the digital parkeerloket), the plate
  must be registered in the permit holder's own account before it can be used.
- A plate listed on a permit or a grant screen can differ from the plate on the car that actually
  parks; check the two against each other.

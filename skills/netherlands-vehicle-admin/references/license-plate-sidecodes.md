# Dutch kenteken — sidecode generations and validation

## What a sidecode is

Since 1951 the Netherlands issues plates in numbered **sidecode** generations (01–16 to date). Each
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

Length is 6 characters for sidecodes 01–14 and 7 for generation 16.

| Code | Mask | From | Notes |
| --- | --- | --- | --- |
| 01 | `XX-99-99` | 1951 | earliest generation, may contain non-pool letters |
| 02 | `99-99-XX` | 1965 | |
| 03 | `99-XX-99` | 1973 | |
| 04 | `XX-99-XX` | 1978 | |
| 05 | `XX-XX-99` | 1991 | |
| 06 | `99-XX-XX` | 1999 | |
| 07 | `99-XXX-9` | 2004 | |
| 08 | `9-XXX-99` | 2006 | |
| 09 | `XXX-99-X` | 2009 | |
| 10 | `X-999-XX` | 2011 | |
| 11 | `XX-999-X` | 2013 | |
| 12 | `X-99-XXX` | 2015 | |
| 13 | `99-X-XXX` | 2017 | |
| 14 | `XXX-X-99` | 2019 | |
| 15 | `9-XX-99-X` | 2021 | first 7-character generation |
| 16 | `XX-9-XX-99` | 2023 | current generation at the time of writing |

`XX-999-X` above is a placeholder showing the mask shape and the display format — substitute the
plate you are actually looking up.

## Validation algorithm

1. **Clean.** Uppercase, strip hyphens and spaces:
   `raw = plate.strip().upper().replace("-", "").replace(" ", "")`
2. **Length.** 6 characters → candidates in sidecodes 01–14; 7 characters → candidates in 15–16.
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
(e.g. sidecode 11 → 2013). Use it before a plate is submitted to any parking or municipal system,
and to date a vehicle from its plate when no RDW lookup is possible. The script is not a substitute
for RDW: sidecode gives an era, never the model, weight or tax data — those come from the RDW open
data endpoints in the main SKILL.md.

**Known discrepancy in the script, inherited from the source rule (verified by running it):** the
6-/7-character split files generation 15 with the 7-character generations, while its mask
`9-XX-99-X` holds only 6 characters. Consequences: a genuine 6-character generation-15 plate places
report as "no match", and a 7-character input is reported as generation 15 with its last character
dropped. Generation 15 is the one row to check by hand — the mask table above is the authority, and
the script was left as written rather than silently re-specified.

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

- **Ambiguity without hyphens.** A bare 6- or 7-character string can regroup into more than one
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

---
name: dutch-official-documents
description: "Use when drafting Dutch official letters or declarations. Produces the submittable Dutch pages plus Chinese explanatory pages from one values file, and covers gemeente, KvK, RDW, Belastingdienst and IND paperwork."
version: 1.0.0
version: 1.0.0
author: sixgod
license: CC BY-NC 4.0
metadata:
  hermes:
    tags: [dutch, letter, declaration, gemeente, verklaring, bilingual, form-filling, vof, garantstelling, embassy, pdf]
    category: productivity
    related_skills: [pdf, docx, dutch-business-procedures, netherlands-vehicle-admin]
---

# Dutch Official Documents

Produce formal Dutch letters and declarations that a Dutch institution will
actually accept, for a user who writes Chinese: the Dutch pages are the
submittable artifact, the Chinese pages only explain it, and the fill-in
data lives in one values file so a re-run produces the file the user signs.

## When to Use

- The user needs a declaration, statement, notice or letter for a Dutch body:
  gemeente (parking permit, objection, permit application, signature
  legalisation for a garantstelling), KvK, RDW, Belastingdienst, IND, an
  insurer, a landlord or VvE.
- A partnership or business notice must be written — a VOF
  opzeggingsbrief (dissolution notice) or a letter to a partner/company.
- A statement for the Chinese embassy/consulate in the Netherlands
  (情况说明) is needed for a visa or residence file.
- A previously drafted declaration must be filled with real data — re-run
  the generator instead of re-drafting.
- A form must be signed in front of a gemeente official rather than mailed
  (garantstelling / IND Form 1310) — pre-fill it, then follow the signing
  appointment rules.
- Not for free-form correspondence with a private person, and not for
  translating an existing document (deliver a translation, not a declaration).
- For *reading* what a Dutch body has published rather than writing to it
  (budget day, a new rule, a ministry's plans), use the sibling skill
  `skills/dutch-government-briefings/`; the source map there covers
  rijksoverheid, rijksfinancien and CPB pages.
- Vehicle facts that go *into* a declaration (kenteken, RDW data, taxes,
  insurance, the permit zone) are grounded via
  `skills/netherlands-vehicle-admin/`; the KVK form catalogue behind a VOF
  exit lives in `skills/dutch-business-procedures/`. This skill writes the
  document, those skills supply the facts.

## Standing preferences (this user)

- Dutch submittable pages first and self-sufficient; Chinese translation and
  any explanation on later pages, each headed with `NIET MEESTUREN` /
  请勿提交 so nothing extra lands in the file.
- Parameterize instead of chatting the values: `[PLACEHOLDERS]` in the text,
  a values file (e.g. `gegevens.json`), and a generator script that emits
  docx + pdf. When the user returns with data, only the values file changes
  and one command re-produces the final document — he signs, nothing else.
- Pre-fill everything; ask for exactly the one value still missing rather
  than stalling the whole document (a kenteken, a date, an ID number).
- Keep a snapshot of the blank template (`archief/<YYYY-MM-DD>_leeg/`) plus a
  `README.md` listing every value to collect and the re-run command, so a later
  session can resume without re-reading the chat.
- Chat replies in Chinese, Dutch technical terms left in Dutch, short and
  concrete; name the file path and the fields still missing.
- When the values he supplies look wrong (model spelling, street spelling, an
  implausible period), correct the spelling against the official source, keep
  his version of the substance, and tell him plainly what you changed.

## Document types and skeletons

| Type | Skeleton | Detail |
| --- | --- | --- |
| Verklaring / berijdersverklaring (declaration to a gemeente) | letterhead → `Aan`/`Betreft`/`Ons kenmerk`/`Datum` → `Ondergetekende` block → intro + `Verklaring` with numbered clauses → statement of truth → `Plaats`/`Datum` + signature + `[Bedrijfsstempel]` → `Bijlagen` | below, and `references/nl-terminology-and-sources.md` |
| Bezwaarschrift / letter to an institution | as above, plus the decision's reference (`zaaknummer`, `beschikkingsnummer`) and the ground for objection | below |
| VOF opzeggingsbrief (dissolution notice) | `AANGETEKEND` header → sender/recipient → date → `Betreft: Opzegging VOF … KVK-nummer` → grounds → payment demand + 14-day deadline → consequences → signature → Chinese page → checklist | `references/vof-opzeggingsbrief.md` |
| 情况说明 (Chinese embassy declaration) | personal info → 在国内的情况 → 出国经过 → 在荷兰的情况 → 难民申报 | `references/embassy-situational-declaration.md` |
| Garantstelling (IND Form 1310, signed at the gemeente) | official form, pre-filled unsigned | `references/gemeente-invitation-and-signature-legalisation.md` |
| Any of the above as a "scan" of a signed paper | A4 PDF from the digital original | `references/scanned-pdf-effects.md` |

## Procedure

1. **Establish the institution's real requirement first.** Do not draft from
a generic template. Read the body's own site *and* the underlying regulation
(`lokaleregelgeving.overheid.nl` and `zoek.officielebekendmakingen.nl` carry
municipal verordeningen and regelingen; the gemeente topic page carries the
current attachments list). Extract, in writing: which document is required,
who must sign it, which facts it must contain, any minimum duration, and the
attachments. Cite these in the reply so the user can check them.
2. **Mirror the regulation's own vocabulary.** Use the terms the rule uses —
`houder`/`tenaamgestelde`, `berijder`, `verklaring van de werkgever`,
`kenteken`, `BRP`, `KvK-nummer`. Case workers map the document to the rule
by these words; a legally-correct but differently-worded letter gets bounced.
The working glossary is in `references/nl-terminology-and-sources.md`.
3. **Structure the document:** letterhead (company name, address, KvK, phone,
email) → `Aan` / `Betreft` / `Ons kenmerk` / `Datum` → `Ondergetekende` block
(naam, functie, namens + KvK, contact) → intro line + `Verklaring` with
numbered clauses 1..n → statement of truth → `Plaats`/`Datum` + signature
line + naam/functie + a `[Bedrijfsstempel]` marker → `Bijlagen` list.
4. **Never write a fact you cannot confirm.** Where the institution's expected
wording assumes something untrue (e.g. a clause stating the driver has needed
the car for work for at least three months, when the driver is a relative and
not an employee of the company that holds the kenteken), supply both variants
— clause A (employment) and clause B (holder authorises a named non-employee
as vaste bestuurder) — and state plainly which variant carries rejection or
follow-up risk, plus the contact route for confirming it. Silence about the
risk is the failure mode; inventing the fact is worse.
5. **Build the fill layer.** A `VAR` map from `[TOKEN]` (Dutch and Chinese
tokens) to values-file keys, substitution applied to every block before
rendering, empty values left as visible placeholders, and a `clausule_N` key
to switch clause variants. Print the still-missing fields at the end of the
run — that list is what you send the user. Mechanics, pruning rules and the
one-page autofit loop: `references/document-generator.md`.
6. **Render and verify** (see Verification), keep the submittable page to one
page, then snapshot the blank template and write the README.
7. **Forms signed in person** (garantstelling, legalisatie of a signature):
hand over a pre-filled *unsigned* document, an accepted ID type, the
co-signing partner where applicable, the current fee and validity window —
all in `references/gemeente-invitation-and-signature-legalisation.md`. Fees
and validity move; re-read the gemeente page before telling the user a figure.
8. **Delivery.** Send formal letters through the account configured for
official correspondence (SMTP with STARTTLS); never fall back to a personal or
secondary account unless explicitly requested. Attach PDFs with UTF-8 filename
encoding, or the recipient sees mojibake:

```python
attachment.add_header("Content-Disposition", "attachment", filename=("utf-8", "", filename))
```

## Pitfalls

- **Requirements are per-municipality and per-year**: a declaration that
satisfied another city, or last year's form, is not evidence. Re-read the
current regeling each time; gemeenten also re-issue resident permits and
change attachment lists.
- **The applicant is a person, not the company**: a permit or benefit is bound
  to the person with the required relationship to the address (e.g.
  BRP-registered there) and to the vehicle (houder or berijder). A company can
  hold the vehicle and still not be the applicant — settle who must apply
  before writing the letter.
- **Who signs is a separate question from who applies.** In an objection to a
  bill, a fine or a decision, the letter must come from the party the document
  names; a relative or adviser handling the file attaches a `machtiging` and is
  named as contactpersoon rather than as the author.
- **Lease versus ownership changes the paperwork**: kenteken in a
  leasemaatschappij's name needs an extra declaration between lease company and
  employer; kenteken in the employer's own name does not.
- **One page for the submittable sheet**: filled values are longer than
  placeholders, so fitting the blank template proves nothing — re-check the
  page count after filling with dummy data, or the signature block slides onto
  a second sheet.
- **A registered letter is the evidence, not the text.** For an opzegging or
  any notice with a deadline, the send method (`aangetekend`) and the
  day-stamp are part of the document's legal value; say so in the chat and in
  the checklist.
- **Dissolution ≠ deregistration** for a VOF: the notice ends the partnership,
  the KVK registration still has to be removed (and an uncooperative partner
  changes the route). Do not present the letter alone as the complete exit —
  see `references/vof-opzeggingsbrief.md`.
- **CJK in the generated PDF**: follow the pdf skill's CJK rule (embed a font
  covering both CJK and Latin; Noto CJK `.ttc` is CFF and reportlab rejects it;
  DroidSansFallback has no Latin, so every Latin character silently vanishes).
  Verify with `pdftotext` plus a rendered page (`pdftoppm` → `vision_analyze`),
  never by assuming the glyphs are there. The font list that was actually
  tested on this host is in `references/document-generator.md`.
- **CJK in the generated DOCX**: python-docx's `font.name` writes only
  `w:ascii`/`w:hAnsi`, so the Chinese pages render in whatever face Word
  substitutes for the script. Set `w:rFonts/@w:eastAsia` on each run and on the
  `Normal` style (e.g. to `SimSun` or `Noto Sans CJK SC`) when authoring with
  python-docx directly.
- **Avoid `fpdf2`'s `multi_cell(width=0)`** — it raises "not enough horizontal
  space" on some characters. Use reportlab, or weasyprint (HTML→PDF) when the
  document is plain enough that HTML is faster to lay out.
- **The Chinese page must be labelled non-submittable**, or it is treated as
  part of the submission; put the marker in the page heading, not a footer.
- **Do not paste an address, a service area or a company detail you have not
  checked.** Verify company details against KvK/address/phone, check that a
  utility or service really covers the address (the regional water companies
  differ, e.g. Waternet vs Dunea), flag grammar and spacing that look like LLM
  artifacts, and note geographic inconsistencies in the draft before it goes
  out.

## Verification

- Fill the values file with dummy data, regenerate, and confirm: zero `[`
  placeholders left, the submittable Dutch page is still one page, the clause
  variant switch produces the expected wording, and `pdftotext` shows the dummy
  values. Then restore the blank values file and regenerate the template.
- For CJK output, assert glyph coverage programmatically before rendering —
  `TTFont(path).face.charToGlyph` must contain `ord('A')`, `ord('[')` and a
  Chinese codepoint — then render page 1 and look at it.
- Check the attachments list against the regulation page; each item must be
  something the user can actually obtain.
- Verify company details against the register (KvK), and service/coverage
  claims against the provider, before the letter leaves.
- Report back only after both files (docx + pdf) exist and the missing-fields
  list came from a real run.

## Support files

- `references/nl-terminology-and-sources.md` — the Dutch terms these documents
  hinge on, which source publishes which requirement, and the worked example of
  a resident parking permit for a company/lease car.
- `references/document-generator.md` — the one-source/two-format generator
  pattern: block model, `gegevens.json` + token→key substitution, pruning,
  one-page autofit, archive, and the tested CJK font/renderer rules.
- `references/vof-opzeggingsbrief.md` — VOF dissolution notice: legal basis,
  structure, key phrases, KVK forms, and the practical path when a partner
  will not cooperate.
- `references/embassy-situational-declaration.md` — 情况说明 for the Chinese
  embassy/consulate: required sections and format preferences.
- `references/gemeente-invitation-and-signature-legalisation.md` —
  garantstelling / IND Form 1310 signing at the gemeente: documents, ID rules,
  appointment, fee and validity.
- `references/scanned-pdf-effects.md` — turning a digital original into an
  A4 PDF that reads as a scan (grayscale, skew, noise, blur, JPEG), with the
  size constraint.

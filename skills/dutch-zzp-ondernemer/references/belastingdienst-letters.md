# Belastingdienst letters: type, content, action

Read the **title line first** — it names the letter type, and the type decides
the answer. Never infer the type from a generic impression of the page.

## `Mededeling vaststelling belastingplicht` (subtitle: `Vaststelling belastingplicht <9 digits>`)

The first letter after KVK registration. Meaning: you are registered as
ondernemer. Multi-page (3 pages in practice); header block carries `Datum`,
`Kenmerk` (dossier number, format like `4446724-01`), and `Betreft:` with a
9-digit number — that 9-digit reference is the ob-nummer base (for a zzp'er the
9 digits are the BSN, which is why it must not be paraded around).

**Page 1 deliberately carries no operative numbers**: it announces that the tax
types, the tijdvak per tax and the matching number are listed further on, and
that each tax gets its own letter explaining how to file. What page 1 does say:

- you are registered as ondernemer; if an earlier letter already announced a
  registration, the existing registration was adjusted rather than created;
- a later assessment of your belastingplicht is possible, they may ask for more
  information, and they may rule that you are no longer liable for the listed
  taxes **with retroactive effect** — boilerplate, not a threat;
- for the omzetbelasting you receive 2 numbers: the omzetbelastingnummer
  (ob-nummer) further in this letter, used only for contact with the
  Belastingdienst, and the btw-identificatienummer (btw-id) in a **separate
  letter**, used on invoices, website and in contact with customers and
  suppliers;
- a closing `Startende ondernemers` block pointing to
  belastingdienst.nl/starters and belastingdienst.nl/mijnzakelijk.

Action: **none** — no payment, no reply, no form. Keep the letter, read the
remaining pages, watch for the separate btw-id letter, and be able to name the
tijdvak and deadlines.

## The two number letters

`btw-id` = `NL` + 9 digits + `B` + 2-digit subnumber (e.g. `NL123456789B01`) —
public: invoices, letterhead, website, customer and supplier contact.
`ob-nummer` = 9 digits + `B` + 2 digits (e.g. `111234567B01`); for a zzp'er the
9 digits are the BSN — Belastingdienst contact only, never on an invoice. A
zzp'er receives them in **two separate letters**, so both must be expected and
kept. Both are also readable in Mijn Belastingdienst Zakelijk under 'Btw'.

## `aangiftebrief`

Annual, arrives before the end of the first tijdvak: which periods you file,
the deadlines and the betalingskenmerken. Keep it; a nil return (0-aangifte) is
still due when there was no turnover.

## Adjacent letter: KVK `Bericht van registratie - KVK-nummer <8 digits>`

Not a Belastingdienst letter, but this is the one that answers "where is my KVK
number". Single page, opening `Op <date> is de onderneming van <name> gestart.`
It carries: Naam, Geboortedatum, Geboorteplaats, Woonadres; **Handelsnaam**;
Activiteit with its SBI code (e.g. `62100 - Ontwerpen van computerprogramma's`);
Aantal full-time / part-time werkzame personen; **Startdatum vestiging**;
**Vestigingsnummer**; Bezoekadres and Postadres (`gelijk aan het bezoekadres`
when identical); a free-text activiteitenomschrijving; importeert/produceert
flags; Telefoonnummer; E-mailadres; Domeinnaam.

The KVK number appears only in the title line and **never in a Belastingdienst
letter** — so when an invoice template needs `KVK-nummer`, ask for this letter
(or the KVK uittreksel), not the vaststelling letter. Compare the Handelsnaam
with the `name` VIES returns for the btw-id: a mismatch is worth flagging before
the name goes onto an invoice.

## Other headers you may see

- `Aanslag` / `voorlopige aanslag` — a payment demand with a betalingskenmerk and
  a due date. This one is money; do not file it with the informational letters.
- `Naheffingsaanslag`, `boete` — a correction and possibly a fine: check the
  response deadline.
- `Verzoek om informatie` — carries a deadline to respond; treat as urgent.

## Print artefacts, not information

Side codes such as `AL 781 - 12-2027` or `NW09442 09824 01 02`, the QR block and
`Pagina N van M` are print batch codes. Only the page count is meaningful (it
tells you whether you have the whole letter).

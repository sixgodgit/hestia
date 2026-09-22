# VOF opzeggingsbrief — partnership dissolution notice

A one-partner notice (opzegging) that ends a vennootschap onder firma, sent by
registered mail, with a Chinese translation page and a practical checklist page
behind the Dutch letter.

## Legal basis

- **Artikel 7A:1683 BW**: a VOF can be dissolved by notice (opzegging) from one
  partner to the others.
- **Artikel 7A:1686 lid 1 BW**: the other partners can oppose the notice if it
  is contrary to reasonableness and fairness.
- **Artikel 31 WvK**: the dissolution must be reported to the KVK.
- **Artikel 32 WvK**: liquidation of the partnership assets follows the
  dissolution.

## Key distinction

- **Ontbinding (dissolution)** = the VOF legally ends.
- **Uitschrijving (deregistration)** = removing it from the KVK Handelsregister.
- Both are required to fully exit a VOF. The letter alone is not the exit — say
  this plainly in the chat, or the user thinks the letter finished the job.
- The opzegging itself is **vormvrij** (no prescribed form; letter, email or
  even conduct can suffice) — which is exactly why the written letter plus the
  registered-mail proof matters, and why an `opzegtermijn` (notice period) that
  respects the other partners' interests should be visible in the letter.
  The full exit procedure, court route, costs and financial settlement live in
  `skills/dutch-business-procedures/` (VOF exit procedures); this file covers
  the document.

## KVK forms

- **Form 17**: report dissolution of a VOF/CV/maatschap/rederij — requires ALL
  partners' signatures.
- **Form 16**: change or deregister functionarissen — a partner can file this
  for themselves via Mijn KVK with DigiD, without the other partner's
  signature.
- The wider form catalogue and the registration side live in
  `skills/dutch-business-procedures/`; keep this file to what the letter itself
  has to invoke.

## Structure of the document

1. Header: `AANGETEKEND` / REGISTERED MAIL.
2. Sender info (name, address, contact).
3. Recipient info (partner name, address).
4. Date.
5. Subject: `Opzegging vennootschap onder firma (VOF) [business name]`,
   KVK-nummer `[KVK-NUMMER]`.
6. Body:
   - notice of dissolution with immediate effect;
   - grounds (see below);
   - optionally an outstanding payment demand with a 14-day deadline
     (`Binnen 14 dagen na dagtekening`) where money is owed;
   - consequences: the partnership ends and the KVK registration has to be
     removed (Form 17 / Mijn KVK deregistration).
7. Signature block.
8. Chinese translation page, headed 请勿提交 / NIET MEESTUREN.
9. Checklist page (practical steps the user has to take).

## Key phrases

- "Hierbij zeg ik de vennootschap onder firma ... op met onmiddellijke ingang"
- "Gronden voor deze opzegging"
- "Gevolgen van deze opzegging"
- "Binnen 14 dagen na dagtekening"

## Common grounds for dissolution

1. Duurzame verstoorde verhouding (permanently disturbed relationship).
2. Fundamentele meningsverschillen (fundamental disagreements).
3. Niet naleven van afspraken (breach of agreements).
4. Uitblijven van kapitaalinbreng (failure to contribute capital).

State the ground(s) that are true for this partnership; do not stack all four
as boilerplate. `clausule_N` in the values file switches which paragraphs are
included (see `document-generator.md`).

## Practical path (uncooperative partner)

1. Send the opzeggingsbrief by registered mail — the proof of the notice is the
   send method plus the day-stamp, not only the wording.
2. Self-deregister as functionaris via Mijn KVK (DigiD, Form 16).
3. If the partner will not sign Form 17 → apply to the rechtbank for
   dissolution.
4. The court can order dissolution for "gewichtige redenen" (weighty reasons),
   including a permanently disturbed relationship.

## Checklist to hand to the user

1. Send via PostNL aangetekende brief (registered mail) and keep the receipt.
2. Log into Mijn KVK with DigiD → deregister as functionaris/vennoot.
3. Consult the accountant for the final filings (BTW + IB).

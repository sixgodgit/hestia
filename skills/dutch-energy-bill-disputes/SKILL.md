---
name: dutch-energy-bill-disputes
description: "Use when auditing or disputing a Dutch energy bill."
version: 1.0.0
version: 1.0.0
author: sixgod
license: CC BY-NC 4.0
metadata:
  hermes:
    tags: [Netherlands, energie, Stedin, Enexis, verjaring, bezwaar, betalingsregeling]
    category: research
    related_skills: [dutch-bv-and-dga, dutch-official-documents]
---

# Dutch energy & utility bills: audit and dispute

Any bill for electricity/gas/warmte: a leverancier's jaarnota, a netbeheerder's
"energieverbruik zonder contract" (vangnet) invoice, a naheffing/correctiefactuur,
and the disconnection threat that follows not having a supply contract. Not tax
policy (dutch-tax-and-budget-changes) and not the bookkeeping decision of who
bears the cost inside a B.V. (dutch-bv-and-dga).

## Output shape (standing user preferences)

- Reply in Simplified Chinese; Dutch terms in parentheses on first use
  (netbeheerder, vangnetlevering, verjaring, bezwaar, betalingsregeling).
- Flat list of short bold labels. No nested headings, no process narration.
  Split into 必须做 / 建议做.
- Lead with the money: one line on what (if anything) must be paid, then why.
- Inline `[n]` on every outside fact plus the `Sources:` block from
  `grounded-citations`; register sources in the ledger at retrieval time.
- When a follow-up answer reuses the ledger from the previous answer, verify
  **without** `--strict`: sources registered but not cited in the new draft are
  reported as warnings, and `--strict` exits non-zero on them even when the
  citations themselves are correct.
- Never quote a possible saving as a precise euro figure when it depends on a
  specification you have not seen. Give the share of the billed period and name
  the missing pages.
- Close by offering the documents in signable state (bezwaarschrift +
  betalingsregeling request, later the ownership/rent agreement).

## Procedure

1. **Classify the bill from the header and the letter's own wording.**
   Netbeheerder letterhead (Stedin / Enexis / Liander) plus "In deze periode had
   u geen contract met een energieleverancier" = vangnet invoice: the
   netbeheerder advanced the consumption cost and recovers it afterwards. A
   leverancier invoice looks different (jaarnota, voorschot, leverancier name).
   **The debtor is the named klant**, not whoever lives there.
2. **Collect every page before auditing.** A photographed specificatie often
   shows one period block only. Cross-check a block against its own lines: a
   block labelled "…2022" carrying a "Vermindering Energiebelasting 2022" of
   roughly a quarter of that year's annual heffingskorting (€681,63 excl. btw
   for 2022) covers one quarter — the other years sit on pages you do not have.
   Ask for them instead of extrapolating.
3. **Check the btw split arithmetically.** excl + 21% + 9% must equal the total,
   and the 9% base must be plausible: the 9% rate for electricity/gas/warmte ran
   only for consumption 1 Jul – 31 Dec 2022. Solve
   `x = (excl*0.21 - (btw9 + btw21)) / (0.21 - 0.09)` for the 9% base, then
   `0.09x ≈ btw9` and `0.21(excl - x) ≈ btw21`. A split that does not close, or
   a 9% amount outside the 2022 window, is a concrete point to query. Also
   compare the leveringstarief per kWh/m³ with published rates for those months —
   a vangnet levy is not the outcome of a competitive market, so query it rather
   than assume it.
4. **Test verjaring first — it is usually the largest lever.** Energy supply to a
   consumer is a consumentenkoop: 2-year term (art. 7:5 + 7:28 BW) running from
   when the original annual bill became due, NOT from the later correction
   invoice. The netbeheerder's own claims carry a further 2-year vervaltermijn
   (E-wet art. 31 lid 10 / Gaswet art. 12b lid 3, held to apply to all afnemers,
   not only kleinverbruikers). Mark (first concrete claim date − 2 years) on the
   billed period and report the share of the period before that date as
   contested.
5. **Sequence: dispute before paying the contested part.** Payment can count as
   erkenning of the debt and interrupt verjaring (art. 3:318 BW), which revives
   the whole multi-year claim. Send the bezwaar/letter (invoke verjaring, demand
   the full specification) and pay only the undisputed part. Confirm consumer
   status first: business use of the address falls back to the 5-year term
   (art. 3:307 BW). In the letter, demand the send date of the earlier notice
   the invoice itself refers to, plus every aanmaning and collection act in the
   file: only such acts can have interrupted the term (art. 3:317 BW), and asking
   for the dates moves that burden to the creditor. If the creditor holds that
   the 2-year term does not apply, make it state the legal ground and the term it
   relies on instead.
6. **Separate technical defences from tax questions.** "We do not use the gas
   connection" does not remove the fixed charges — an unused aansluiting must be
   removed or closed or it keeps costing money.
7. **Name the exit.** Under the Energiewet (in force 1 Jan 2026) the regional
   netbeheerder may no longer act as supplier: it demands a
   leveringsovereenkomst or disconnects at the customer's cost, and decided
   cases add costs and incassokosten. Say this as the urgent, non-tax item.
8. **Use the real routes:** bezwaar with the netbeheerder (Stedin: binnen 14
   dagen, before the invoice is issued), betalingsregeling in instalments via
   the netbeheerder's site, Geschillencommissie Energie for consumers (binding
   advice; klachtengeld refunded if the consumer wins).

9. **Deliver the letter as files, not as chat text.** A signable Dutch bezwaar is
   an `.md` source, a `.docx` for edits and a `.pdf` to print, produced by a small
   generator run with a Python that has python-docx and reportlab available
   (write `EUR`, not the euro sign, with reportlab's built-in fonts),
   plus a `README.md` with the send steps and whatever is still missing. Verify
   every identifier you quote (klantnummer, factuurnummer, kenmerk, dagtekening,
   EAN-code, meternummer) on a cropped `vision_analyze` read of the original photo
   before it goes into the letter — a misread reference number weakens the whole
   letter.

Depth on the vangnet regime, prescription case law, tariff/rate checks and
source URLs: `references/netbeheerder-vangnet-en-verjaring.md`.
Letter skeleton, the numbered request list and the send channels:
`references/bezwaar-verjaring-letter.md`.

## Pitfalls

- **"Can we pay this from the company account?" is not a payment question.**
  Anyone may pay with the right betalingskenmerk (klantnummer + factuurnummer);
  the real question is who bears the cost under which title — route it to
  dutch-bv-and-dga.
- **Liability follows the named afnemer/owner, not the occupant.** Case law has
  held the owner of a house liable for energy delivered to tenants without a
  contract; "the tenants should have had a contract" is not a defence.
- **Never assume every billed year is still payable.** One-off catch-up invoices
  spanning years are the normal shape here, and step 4 is why.
- **Do not read a tariff label as a tariff error.** Confirm which period a block
  covers before calling the application wrong.
- **Do not present the prescription outcome as settled law.** Consumer status and
  the applicable regime change the term; state the argument, the share of the
  period, and that the accountant or lawyer must confirm before it is invoked.
- **The letter must come from the party named on the invoice.** The rights under
  the bill belong to that person; a relative handling the file signs only with an
  attached machtiging and is named as contactpersoon, not as the author. Quote the
  invoiced amount as billed even where most of it is disputed, so the creditor
  cannot answer that the invoice was never identified.

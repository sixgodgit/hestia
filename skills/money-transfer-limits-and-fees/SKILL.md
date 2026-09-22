---
name: money-transfer-limits-and-fees
description: Use when asked about remittance or card limits/fees.
version: 1.0.0
license: CC BY-NC 4.0
author: sixgod
---

# Money transfer, FX, and card limits

## Answer shape (standing user expectations)

- Reply in Simplified Chinese; technical terms, commands, and provider names stay English. Concise, restrained formatting, no nested headings.
- Lead with the conclusion in one line, then the layers, then what to actually do.
- Always name the **binding** constraint. "Is there a limit?" has two independent layers, and the headline provider number is usually not the one that blocks the user.
- End by offering to check the user's specific card — ask for issuer/card type rather than guessing their monthly limit.

## Procedure

1. Split the question into layers before searching:
   - **Provider layer** — per-transaction cap of the sending service (Remitly, Wise, WorldRemit, bank).
   - **Issuer layer** — the funding card's own monthly spend limit, and how the issuer classifies the transaction.
   - **Scheme/regulatory layer** — SCA/3DS verification, AML review on large amounts.
2. Read provider limits from the provider's own server-rendered pages:
   - `<site>/<country>/<lang>/landing/send-limits` — headline per-transfer figure.
   - `<site>/<country>/<lang>/money-transfer/send-money-to-<destination>` — FAQ block carries the supported payment methods, per-corridor caveats, and "sending limits vary" language.
   - Help-center articles (`/help/article/...`) are client-rendered: extraction returns only nav/footer shells with no body. Skip them; use the landing pages above and the User Agreement PDF (`/pdf/...`), which extracts cleanly and states funding-instrument and tier-review rules.
3. Read issuer constraints. Establish **who issues the card first** — Dutch banks issue their own cards as well as delegating to ICS, and both the monthly spending limit (`bestedingslimiet`, separate from the credit limit and normally the binding number on a consumer card) and its ceiling differ per issuer and card tier. Concrete numbers and sources: `references/remittances-and-nl-cards.md`.
4. Check classification: money transfer uses MCC 4829, and issuers may book it as the equivalent of a cash withdrawal (fee plus interest from the transaction date, no interest-free period). It is bill-dependent, so recommend a small test transfer (~1,000 EUR) and name what to inspect: how it books in the banking app (`aankoop` vs `geldopname`), whether the cash-withdrawal percentage fee appears, and that the issuer's cash-advance daily cap would refuse a large quasi-cash-booked payment outright.
5. Deliver: provider number, issuer number, which one binds, then the cheaper route (bank/iDEAL-funded tier vs card-funded Express tier).
6. Offer to verify the user's own card once they name the issuer/card type.

## Pitfalls

- Comparison and affiliate blogs (Wise's own blog, BiyaPay, frexpay, aggregator sites) republish stale or generic figures — e.g. a flat "$20,000 per transaction" or tier tables that no longer exist. Never quote them as the limit; use them only to corroborate a number already found on the provider's own page.
- Do not report a per-transaction cap as a daily or monthly cap, or vice versa. Per-transfer limits have no reset period.
- Do not answer with only the provider cap when the user cites their own card limit — the card's monthly spending cap is usually far lower and is the real answer.
- A high headline credit limit does not mean that amount is spendable in one month on a consumer card. Ask for the monthly spending limit rather than assuming the credit limit applies.
- Never generalize one issuer's monthly cap into "Dutch credit cards", and never restate that cap after the user names a different issuer or card. Premium/package cards can have no fixed monthly ceiling at all, which inverts the whole answer — identify the issuer and tier before quoting any number.
- A packaged premium card is often a charge card whose balance is direct-debited from the current account monthly, not revolving credit. Using it defers the payment to month-end rather than opening an interest-free window, so it buys nothing on FX — check the card's mechanics before recommending it.
- Do not attribute a foreign-currency surcharge (`koersopslag`) to a card payment to a provider that bills in EUR (Remitly Europe, Wise). It applies to non-EUR merchant transactions; the decision-relevant cost on such a payment is the quasi-cash classification, not FX markup.
- Issuer sites in NL often resolve through no fetch route at all. Pull the numbers from the issuer's own fee/conditions PDF (e.g. `assets.ing.com/...`), from `/pdf/...` agreement documents, or from Dutch comparison sites, and say plainly which figure still needs confirming in the user's app — "not retrievable from here" is an acceptable outcome, guessing is not.
- A card-funded transfer of tens of thousands will trip 3DS/fraud review. Say so instead of promising it will clear.

## References

- `references/remittances-and-nl-cards.md` — published provider per-transfer limits, Netherlands payment methods, and issuer-side card constraints (ICS spending limits, cash-withdrawal fees, MCC classification), with the URLs to re-verify.

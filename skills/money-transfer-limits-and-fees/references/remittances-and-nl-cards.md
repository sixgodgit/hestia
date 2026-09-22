# Provider limits and Netherlands issuer constraints

Re-verify every number before quoting it. Treat the figures below as "where to look and roughly what shape the answer takes" — providers and issuers change them without notice, and the sources are listed so a fresh session can confirm the current values.

## Remitly, sending from the Netherlands / Eurozone

- Per-transfer limit: **85,000 EUR** (Eurozone row of the provider's own per-country list: Austria, Belgium, Cyprus, Finland, France, Germany, Greece, Ireland, Italy, Latvia, Lithuania, Malta, Netherlands, Portugal, Slovakia, Spain).
- No official daily or monthly cap. Identity verification gates the limit, and destination country / delivery method / banking-partner limits can make it lower. Additional documentation may be requested.
- Payment methods from NL: iDEAL, Wero, Visa/Mastercard debit or credit card, Apple Pay / Google Pay, Maestro. Card funding = Express tier (faster, pricier); bank/iDEAL funding = Economy tier.
- Consumer-only service — business use breaches the User Agreement.
- Where to verify:
  - `https://www.remitly.com/nl/en/landing/send-limits` (headline per-transfer figure)
  - `https://www.remitly.com/nl/en` (FAQ block holds the per-country limit list and the debit/credit card requirements)
  - `https://www.remitly.com/nl/en/money-transfer/send-money-to-<country>` (payment-method list, corridor caveats)
  - User Agreement PDF under `https://www.remitly.com/pdf/...` (funding instruments, tier reviews, execution times)

## Netherlands credit cards (issuer side)

- Two independent numbers: the credit limit (total borrowing) and the `bestedingslimiet` (maximum spend per calendar month). Payments *and* reservations both consume the monthly limit; anything exceeding it is declined, and the room only returns as the balance is repaid.
- **The issuer decides the ceiling — split the answer by issuer, never by country:**
  - ICS-issued cards (ABN AMRO, ANWB, and others): roughly max **~5,000 EUR per card and ~10,000 EUR per month across all ICS cards held**. Spending room can be increased without an approval process by pre-funding the card (`geld storten`); ICS pays interest on a positive balance of 500 EUR or more.
  - ING issues its own Mastercards, so the ICS ceilings do **not** apply. ING's own published maxima per card type are roughly **1,000 EUR (student) / 5,000 EUR (regular) / 20,000 EUR (Platinum)**. The premium package card (ING Max plan → "Credit Card Max") is reported by Dutch comparison sites as having **no fixed monthly bestedingslimiet**; treat that as "check the figure shown in the app", not as a guarantee of unlimited spend.
- Cash-withdrawal fees and daily caps: ICS **4%** (around a 2.50 EUR minimum), ING **4%** with a higher minimum (around 4.50 EUR); withdrawal daily caps land around 1,000 EUR (Max card) up to 2,000–3,000 EUR (World/Gold/Platinum/Black), lower for recently issued cards. A large transfer booked as quasi-cash would be refused by these caps before the fee even matters.
- A packaged premium card is typically a charge card: the balance is direct-debited from the linked current account each month. It defers payment to month-end instead of granting an interest-free period.
- Foreign-currency transactions carry roughly a **2%** exchange-rate surcharge on ICS Visa and ING cards. A EUR-denominated payment to a provider billing in EUR (Remitly Europe Ltd is Irish) normally does not trigger it — confirm on the statement rather than adding it to the cost estimate.
- Money transfer merchants use **MCC 4829**; whether the issuer books that as a purchase or as quasi-cash/cash-withdrawal is issuer-dependent and only visible on the statement.
- Large first-time card payments hit SCA (`Mastercard ID Check` at ING) and cannot be assumed to clear.

## Where the NL issuer numbers come from

- `https://www.icscards.nl/...` help pages extract cleanly and carry the ICS limits, cash-withdrawal fees, and daily caps.
- Dutch comparison sites (`bank.nl`, `creditcard.nl`) list per-card limits, fees, and card mechanics (charge vs revolving). Provenance is aggregator — corroborate a figure before quoting it as fact.
- `ing.nl` HTML resolves through no fetch route (client-rendered; archive snapshots come back as empty shells that still pass a size check). Use ING's own fee/conditions PDFs under `https://assets.ing.com/...`, which extract cleanly, plus search-result snippets of the `ing.nl` pages for the specific label or figure.
- Wise's blog and similar provider-affiliated pages are corroboration only.

## Cheaper routes for large amounts from NL

- Bank-funded transfer (iDEAL/Wero) keeps no card limit in the loop and sits in the lowest fee tier; the sending provider's own iDEAL cap applies instead (e.g. Wise around 50,000 EUR per transfer).
- At large sizes a mid-market-rate provider (Wise, Degiro for FX) generally beats card-funded remittance, which adds spread plus possible cash-advance fee and interest.
- Using a credit card is only defensible when the interest-free period or a specific card benefit is the point — not for the exchange rate.

## This user's own setup (as stated in session)

- Holds the ING Max package card (Credit Card Max) and states a high credit limit (around 50,000 EUR); pushed back when an ICS-based monthly cap was applied to it. Lead with issuer identification, and treat ING's own card maxima as the relevant ones until the app figure says otherwise.

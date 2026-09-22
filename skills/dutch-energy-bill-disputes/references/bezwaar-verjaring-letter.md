# The bezwaar / verjaring letter (Dutch energy bill)

What the letter has to do, in the order the creditor reads it. The Dutch text is
the deliverable; the user signs and sends.

## 1. Identify the invoice verbatim

Sender = the klant named on the invoice. Recipient = the afdeling/retouradres
printed on the invoice (a netbeheerder's invoice carries a `Retouradres` postbus;
Stedin: Afdeling Debiteuren, Postbus 49, 3000 AA Rotterdam). Then a `Betreft:` line
and a reference block carrying klantnummer, factuurnummer, kenmerk, dagtekening,
EAN-codes with meternummers, and the billed period with amount. Read every one of
these off a cropped vision read of the photo before writing.

## 2. Invoke verjaring expressly and on two grounds

- **Consumentenkoop, two years:** art. 7:5 jo. 7:28 BW; the term starts the day
after the claim became due (art. 3:313 BW) and that is when the *original* annual
bill should have been paid, not the date of the catch-up invoice — Hof Den Haag
23 October 2018 (ECLI:NL:GHDHA:2018:3140) and Geschillencommissie Energie
(referentie 1322884/1327811).
- **The netbeheerder's own two-year vervaltermijn:** art. 31 lid 10
  Elektriciteitswet 1998 / art. 12b lid 3 Gaswet, held to reach all afnemers and
  not only kleinverbruikers (ECLI:NL:GHARL:2014:6767).

Then convert the ground into a concrete cut-off: everything — verbruik,
aansluit- en transportvergoedingen, heffingen and the btw charged on them — up to
(first claim date − 2 years) is prescribed and no longer owed. Add two clauses
that keep the argument honest and shift the work to the creditor:

- "voor zover uit uw administratie blijkt dat vorderingen over (delen van) die
  periode later opeisbaar zijn geworden, geldt de verjaring vanaf die latere
  datum";
- "indien u van mening bent dat de tweejarentermijn hier niet van toepassing is,
  verzoek ik u mij te berichten welke rechtsgrond en welke termijn u dan
  hanteert".

## 3. Numbered request list

a. full per-period specificatie with meterstanden, tarieven and heffingen over the
   whole billed period — naming explicitly which slice you already hold;
b. the opeisbaarheidsdatum per period;
c. a copy of the earlier notice the invoice refers to, with its send date, plus
   every aanmaning and other act in the file (this is what tests interruption);
d. a corrected invoice limited to the non-prescribed part;
e. written confirmation that incassokosten, rente and afsluitkosten are waived and
   that no connection is closed while the case runs and any plan is honoured;
f. a betalingsregeling for the non-prescribed part;
g. meterstanden and the status of any connection whose volumes are disputed
   ("not in use" does not remove fixed charges — the connection has to go).

## 4. Reservation block

No erkenning of the invoice or of any debt; willingness to pay the undisputed part,
which is not recognition of the disputed part and is made without prejudice;
response within fourteen days and before the payment deadline; otherwise
Geschillencommissie Energie and the courts; ask for the letter to be handled as a
bezwaar/klacht under their own procedure. Close by offering to conclude a
leveringsovereenkomst so the vangnet situation ends.

## 5. Sending

- E-mail the debtor department with a subject line carrying factuurnummer +
  klantnummer and the invoice plus specificatie attached (Stedin:
  debiteuren@stedin.net for payment/debt matters; fm_azc@stedin.net for general
  questions; 088 8963963).
- Post the same letter registered to the retouradres on the invoice. Do both and
  keep the send confirmation; have it delivered well before the payment deadline.
- Fill the contactpersoon phone/e-mail placeholders when a family member runs the
  file; the named klant signs. Where the signer is someone else, generate the
  machtiging as a second document.

## 6. Files

`<naam>_verjaringsbrief.md` (source, editable), `.docx` (edits), `.pdf` (print and
sign), a `make_docs.py` so a reworded source regenerates both, and a `README.md`
with the send steps, the deadlines and the items still missing from the user.

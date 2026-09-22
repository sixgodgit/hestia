# Connected services, car apps and imported cars

## The three links a remote-control feature needs

"No app control and no data" has one symptom but several causes. Check these in order and name which
link is broken:

1. **Embedded eSIM + data subscription** — the car has a permanently installed SIM, and the data
   bundle is activated as part of the market's sales process. Some markets bundle a fixed period
   (e.g. 2 years, up to 2 GB per month); afterwards it is a paid subscription or the car tethers to a
   phone hotspot.
2. **Backend link (VIN ↔ app account)** — the dealer registers the vehicle in the importer's
   connected-car backend and links it to the customer's account. The app account **e-mail must match
   the address recorded in the sales file**, and the vehicle shows up after roughly 1–2 working days.
3. **In-car switches** — connected services and location sharing must be turned on in the car's
   screen before remote commands work at all.

EU type approval (e.g. an `e9…` typegoedkeuringsnummer) proves EU-spec hardware but says nothing about
whether the market's connected services were ever provisioned — never infer link 2 from the type
approval.

## Parallel imports

A car whose `datum_eerste_toelating` sits well before its Dutch `datum_tenaamstelling`, bought from a
wholesaler or importer instead of a brand dealer, usually never went through link 2. Result: the app
cannot add the vehicle, the nav has no live traffic, no OTA ever arrives, and the car has no data.
The seller's own advertising normally listed the connected features, so ask them **in writing** (VIN +
kenteken in the message):

- Is the T-box/eSIM activated for this market?
- Which app account is the car bound to?
- Is a data bundle included, and until when?
- If not activated, who does it and when?

Then escalate with the VIN to the official importer's customer service. Brand footnotes typically say
connected services depend on "vehicle version, regional availability and subscription status", which
leaves them room to refuse — so record what the seller promised at the point of sale. Warranty is a
separate matter: an EU-wide manufacturer warranty generally still applies to a parallel import, but
the official network may charge for or decline connected-services work on a car that is not in its
sales file.

## The diagnostic that separates link 1 from link 2

Tether the car to a phone hotspot, then retry the app:

- **Status refreshes** → the backend link exists and only the data bundle is missing (activation or
  subscription problem, solvable with the seller/importer).
- **Still nothing** → the VIN is not linked; only the importer side can fix it.

Supporting evidence that costs nothing to collect: live traffic in the nav, whether any OTA ever
arrived, and whether the car's screen can even open the connected-services/location-sharing switches.

## App names

Use the global brand app for EU cars (for Geely: the "Geely App", iOS and Android, linked from the
brand's national site). China-market apps and third-party "control" apps do not work with EU cars;
apps that ask for brand credentials are a phishing risk — say so plainly rather than letting the user
try them.

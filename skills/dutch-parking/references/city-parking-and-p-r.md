# City parking and P+R (NL) — procedure + method

Re-verify every number here before quoting it: municipality tariffs change each January and pre-booked garage cards change more often. The figures below are one price level kept as a shape to re-check, not as standing truth. 费率按年变动，以市政官网为准。

## Where the numbers come from

- Street tariffs per stadsdeel, plus the per-street map and the gemeente garages: `https://www.amsterdam.nl/parkeren/parkeertarieven-kaart`
- City P+R rates, terms and live occupancy: `https://www.amsterdam.nl/en/parking/park-ride`
- Garage tariffs — the operator's own page only: `parkingcentrumoosterdok.nl/tarieven`, `q-park.nl/nl-nl/parkeren/amsterdam/<garage>`, `p1.nl`. These sites refuse generic scrapers; extract the operator URL directly, and when it still fails, give the user the garage phone number instead of an unverified price.
- Garage inventory, coordinates and loading bays: the maps skill (`nearby --near "<place>" --category parking --radius 900`). OSM carries `capacity`, `parking` type, `maxstay` and `access:conditional = yes @ loading`, which is how a laad- en losplaats is found.
- Den Haag equivalents: `denhaag.nl/nl/parkeren/<stadsdeel>` for hours and zones, `parkeren-denhaag.nl` for per-lot prices, and the WFS zone layers — see `denhaag-parkeerkaarten.md`.

## Procedure

1. Geocode the destination and list garages within roughly 1 km; note the loading bay on the nearest drivable street.
2. Per candidate collect: pre-booked card price, drive-up hourly rate and daily cap, opening hours, height limit (garage ceilings run 1.8–2.1 m; take the car's height from RDW `hoogte_voertuig` rather than a spec page).
3. Compute walk distance with a straight-line sanity check, then rank by total cost for the actual time window.
4. Answer keyed to arrival time: the same trip has a different cheapest ticket in the morning, the afternoon and the evening.
5. Name what not to do (street in the centre) with the arithmetic that shows why.

## Amsterdam — the shape of the data

The per-option table (street tariffs, the two usable centre garages, the expensive side of the comparison, the full P+R list with exits and transit, and the Chinatown details) lives in `amsterdam.md`; it is the single place to keep those figures so this file does not drift from it. Two things worth keeping here:

- The operator's own comparison pages quote competitors' caps (Q-Park Centraal €37.50 pre-booked / €65 cap; Q-Park Nieuwendijk €32.50/€65; Q-Park Waterlooplein €37.50/€65, hourly €13; Q-Park Bijenkorf cap €60; Markenhoven cap €90; Rokin cap €90). Their figures, useful as an order of magnitude — at these caps a pre-booked card is not a discount, it is the only sane way to buy a day.
- Route baseline for the Amsterdam run: see the drive baselines at the end of `amsterdam.md`.

## Booking the ticket — the form's own rules

- The operator's reservation page embeds a third-party engine in an iframe (`park-spot.com/parking/<parking>/<locale>/<parking>/product/<product>`; day-card slug `dagkaart`, evening card `avondkaart-18-00-23-59-uur-eur-10`). The space is only held once a date is picked; the draft then runs on a visible countdown ("Resterende tijd om uw reservering te voltooien") and expires if abandoned.
- To read the fields instead of guessing them, POST step 1 to the product URL with `arrival-date=YYYY-MM-DD`; the response is the step-2 page. A date in any other format (`20-09-2026`) returns `error=form.error.no_spots_available` — a misleading error meaning the format, not a full garage. Full probing method: `booking-flow-probing.md`.
- Fields on that page: `kenteken`, whose label tooltip reads *"HOOFDLETTERS zonder streepjes"* (capitals, no dashes), and `kenteken-landcode` (*"NL, D, B, PL, etc."*). Required: e-mail, herhaal e-mail, kenteken, landcode; achternaam and telefoon nummer are optional.
- **Read the field's own `data-validation` attribute rather than trusting the platform's validator.** The JS bundle ships a Dutch-plate validator listing only sidecodes 1–10 (`XX-99-XX` … `X-999-XX`) and stripping at most two dashes, so a sidecode 11 plate (`XXX-99-X`, issued for passenger cars since 04-06-2024) matches none of its patterns. On the live form the field carries only `data-validation="required"`, so it accepts the plate with or without dashes; the site's own capitals-no-dashes instruction is still what to pass on.
- The ticket summary (`Aankomst <date> vanaf 00:01` / `Vertrek … tot 23:59`, plus the amount) is the authoritative window and price for that date — quote those, not an advertised "from" price.
- Cancelling costs €2,50 and must be done by the previous calendar day.
- The ticket's navigation address can differ from the postal one (for Oosterdok: postal Oosterdoksstraat 140, navigate to De Ruijterkade 154; doorrijhoogte 2,10 m).

## P+R mechanics (that decide whether the cheap price is real)

- €6 per 24 h for weekday arrivals after 10:00, and all weekend and public holidays; €13 for the first 24 h on weekday arrivals before 10:00, then €6 per following 24 h. Max stay 96 h, except P+R RAI (24 h).
- The discount requires travelling to **and** from the centre by GVB with an **OV-chipkaart**, or a paper P+R GVB ticket bought from the blue machine at the site within 1 hour of entry. Bank-card/OVpay taps, mobile wallets and barcode e-tickets earn no discount, and payment is due within 1 hour of checking out.
- P+R GVB ticket: 1–2 people €6, 3 €7, 4 €8.50, 5 €9.50; valid 1 hour each way on GVB tram/metro/bus only — no night buses, no NS.
- Chinatown by metro: lines 53/54 stop at Nieuwmarkt, service roughly 05:30–01:00, so a 23:00 return still works. P+R ArenA (~2400 places) is a one-seat M54 ride to Nieuwmarkt — the cheapest credible plan when the car will not move all day.

## Emission zones and fines

- Inside the A10 (low-emission zone) diesel cars need **Euro 5 or higher**; Euro 4 and lower are banned, cars 40+ years old are exempt. The zero-emissiezone inside the S100 covers vans and lorries registered from 2025 and passenger cars from 2030. Fines: €130 for cars and vans, €320 for lorries, €90 for mopeds.
- Parking fine Amsterdam €79.10 plus the applicable tariff, issued by plate-reading scan cars — no grace period.

## Other cities

Rotterdam centre ≈ €4.24/h; Den Haag and Utrecht reach ≈ €7/h in their busiest zones (press figures — confirm on the gemeente's own tariff map, same procedure). Den Haag: from April 2026 residents who have parking on their own property are no longer eligible for a street permit.

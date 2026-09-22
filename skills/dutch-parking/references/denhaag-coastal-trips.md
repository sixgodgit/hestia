# Den Haag coastal and green-edge trips — parking, rates, food

Leisure destinations around Den Haag (beach, dunes, lakes) reached by car. Every
rate below was read off the page named in its entry — **re-read before quoting**
(tariffs change each January), and mind the hard 1 April / 1 October switches on
beach parking.

## Where to re-verify, in this order

- `parkeren-denhaag.nl` — per-garage and per-lot pages, plus explicit
  "Gratis Parkeren <straat>" pages for the free surface lots. Private site, but
  the only one that prices the individual lots; cross-check a claimed free lot
  against the stadsdeel page before promising it.
- `denhaag.nl/nl/parkeren/<stadsdeel>` — paid hours, permit zones, and the cheap
  groengele kort-parkeer zone (Loosduinse Hoofdstraat: €0.10 per use, max 1 h,
  Mon-Sat 10:00-18:00; re-register after 60 min).
- `bollenstreek.nl` — Langevelderslag zone code plus both seasonal tariff tables.
- `staatsbosbeheer.nl` → location → Bezoekersinformatie — names the free car
  parks of recreation areas (this is how Vlietland's two lots surface).
- `dunea.nl/duinen/praktisch` — dune entrances and where the car goes at each.
- `dezandmotor.nl/route` — official car access and beach entrance for the
  Zandmotor (its two southern strandslagen are foot/cycle only).

## Kijkduin / Zuiderstrand — closest beach to the city

- **Parkeergarage Deltaplein** — 685 places under the shopping centre, 24/7, some
  EV charging. First **1.5 h free**, then €1.75 per 30 min (€3.50/h), maximum
  €25 per 24 h. Good for a meal inside the free window, poor for an afternoon.
- **Machiel Vrijenhoeklaan 175 — free, no time limit.** Between restaurant de
  Haagsche Beek and the Roompot holiday park (52.0637, 4.2173); metres from the
  sand and quieter than the boulevard. The same lot is the official car access
  for the Zandmotor: from it to strandopgang 2, then ~15 min along the beach.
- Food by those lots: Beach Club Dunes (Deltaplein 204), Beachclub Titus
  (Zuiderstrand 12, seasonal Mar-Oct), Strandpaviljoen Suiderstrand
  (Strandslag 2a). Deltaplein itself has a coffee bar, a pannenkoekenhuis, an
  Italian and a Surinamese place, all a 1-2 min walk.
- Sitting: Zuiderstrand and the Zandmotor are the empty ones; the boulevard in
  front of Deltaplein is the busy one.

## Langevelderslag — Noordwijk north

- Large lot, ~700 cars, zone **22600**, address **Langevelderslag 20, 2204 AH
  Noordwijk** (52.3016, 4.4774). Machines on site and Parkmobile.
- First and second hour €1.20/h, from the third hour €3/h, **dagkaart €10
  (1 Apr - 30 Sep) / €5 (1 Oct - 31 Mar)**. Buy the day card for a long stay.
- Catering on or beside the lot (Nederzandt, Hoogies, Bella Bella) and an
  entrance to the Amsterdamse Waterleidingduinen. Quieter than the Noordwijk
  boulevard, which is why it suits sitting rather than strolling.

## Vlietland, Leidschendam — free, sheltered

- ~300 ha recreation lake between the Vliet and the A4; 8 km round. Free parking
  south at **Kniplaan** (52.1037, 4.4385) and north at **Pijlkruid,
  Rietpolderweg** (52.1233, 4.4631). No bus stop; the car is the normal access.
- The pick when wind or rain rules out the beach, or when "near" outranks
  "sea".

## Meijendel and the Wassenaarse Slag — Dunea dunes

- Wassenaar the town is free parking (three blue-disc zones), but the Meijendel
  reserve and the Wassenaarse Slag have their **own** regime outside it: quote
  the lot, never "parking is free in Wassenaar".
- Wassenaarse Slag entrance (Wassenaarseslag 26, 2242 PJ Wassenaar): park
  opposite Fletcher Boutique Hotel Duinoord, or at the De Kuil / Zeelust lots.
- De Kieviet entrance: visitor centre De Tapuit with parking **P1**
  (Parkeerplaats Meijendel, 2243 GN Wassenaar) — the largest lot, at the
  roundabout, then 1.5 km along the white-posts path. Wheelchair- and
  stroller-friendly routes start here.

## Drive baselines (from the centre of The Hague — 距海牙市区 X km)

Kijkduin 9.3 km / 16 min · Zandmotor 10.6 / 21 · Vlietland 19.5 / 17 ·
Langevelderslag 33.5 / 38 · Reeuwijkse Plassen 34.4 / 33. These were measured
from a residential address in The Hague, so read them as "距海牙市区 this far";
recompute rather than reuse if the origin changes:
`maps_client.py distance "<from>" --to "<to>" --mode driving`.

## Timing checks before recommending a beach or dune day

- Weather: `curl -s "https://wttr.in/Den+Haag?format=j1"` — read each day's
  summed `precipMM` and its max `windspeedKmph`. For sitting outdoors, low wind
  decides more than temperature does.
- Sunset: `https://api.sunrise-sunset.org/json?lat=52.1&lng=4.3&date=YYYY-MM-DD&formatted=0`
  (UTC — add the local offset), then name the best light window.
- Season: beach pavilions run Mar-Oct or May-Oct and the beach day card switches
  on 1 Oct. Say which side of the boundary the date is on rather than assuming
  the summer picture holds.

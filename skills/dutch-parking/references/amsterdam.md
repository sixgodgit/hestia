# Amsterdam parking baseline

Values below are a 2026 baseline for orientation — re-fetch the municipality page and the operator's own booking step for the trip at hand before quoting them (tariffs change each January, garage cards more often).

## Street parking
- Stadsdeel Centrum: EUR 5.37-8.05/h, 24/7 **including Sundays and evenings**, no night exemption. Other stadsdelen range from ~EUR 0.20 (outer edges) to ~EUR 6.98/h with shorter paid windows. (An older second-hand summary put the centre at EUR 5-7.50/h; the municipal per-stadsdeel figures above are the specific, current ones.)
- Fine for a violation: EUR 79.10 plus the applicable tariff. Enforcement is by scan car reading plates automatically; there is no paper ticket to chance it with.
- Free parking exists only in outer areas and on King's Day.

## Centre garages worth quoting
- **Parking Centrum Oosterdok** — Oosterdoksstraat 140 (navigation address Oosterdoksstraat 150; some sources also give De Ruijterkade 154), largest centre garage (~1369 spots), 24/7, doorrijhoogte 2.10 m, reachable from A10 via exit S116 (IJtunnel). Online cards: Dagkaart 00:00-23:59 from EUR 25 (date-dependent), Avondkaart EUR 10 for 18:00-23:59, Quick visit from EUR 15 for 14:00-17:00, Meerdagenkaart from EUR 25/day. Walk-in EUR 8/h with a EUR 45/day cap. ~600 day-card spots per day — when those are gone you can still drive in but pay the walk-in rate. Card = one entry and one exit. Cancellation EUR 2.50 and only until the previous calendar day. Booking entry point: https://parkingcentrumoosterdok.nl/reserveren/ (order form is a park-spot.com iframe — see booking-flow-probing.md).
- **P1 Centrum** — Prins Hendrikkade 20a, closest garage to the north end of Zeedijk (~500 m), 24/7, doorrijhoogte 1.9 m. Third-party pages give ~EUR 3.50/h and ~EUR 45/day (unverified; the operator's own price page does not render for scraping, phone 020-6385330). No online booking via Parclick.
- **Expensive side of the comparison** — Q-Park Waterlooplein (Valkenburgerstraat 238) ~EUR 13/h, Q-Park Centraal ~EUR 37.50-65/day, Q-Park De Bijenkorf ~EUR 60/day, municipal Rokin/Markenhoven up to ~EUR 90/day. Useful only as "this is what you avoid".

## P+R (municipal, all EUR 6/24 h at weekends and weekdays after 10:00; EUR 13 before 10:00 weekdays; max 96 h, RAI 24 h)
| Location | Address | A10 exit | Transit to centre |
|---|---|---|---|
| P1 ArenA | Burgemeester Stramanweg 130 (under the stadium) | Ouderkerk (A9/A2) | metro 54 from Strandvliet (~10 min walk from the garage) direct to Nieuwmarkt/Chinatown; outside the milieuzone; ~2400 spots, height 2.25 m |
| Zeeburg 2 | Zuiderzeeweg 8 | S114 | tram 26 / bus 37 to Centraal, then 6-8 min walk to Zeedijk |
| Zeeburg 3 | Anthonie van Akenstraat | S114 | tram 26 / bus 37 |
| Sloterdijk | Piarcoplein 1 | S102 | metro 50/51 or NS train to Centraal |
| RAI | Europaplein 24 | S109 | metro 51/52, tram 4 (max stay 24 h) |
| Olympisch Stadion | Laan der Hesperiden t/o 66 | S108 | tram 24 |
| Bos en Lommer | Leeuwendalersweg 23b | S104/S105 | tram 7 / bus 21 |
| Noord | Nieuwe Leeuwarderweg 25 | S116 | metro 52 / bus 37 |
| Boven 't Y | Buikslotermeerplein 237 | S116 | metro 52 / bus 37 |
| VUmc (weekends only) | Gustav Mahlerlaan 3004 | S108 | metro 51, trams 5/24 — open Fri 18:00 to Mon 04:00 |

- P+R GVB paper return tickets (EUR 6 for 1-2 people, 1 hour valid each way, GVB only, no night buses/NS) are sold at the blue machines at **Bos en Lommer, ArenA, Olympisch Stadion and RAI only**. At Zeeburg/Sloterdijk you need your own OV-chipkaart — or travel in paying by bank card and buy a paper GVB ticket in the city for the return leg, which the official page accepts.
- Event closures are published per location as date pairs (e.g. match weekends listed as both the day before and the match day), so verify the specific date on the location page rather than trusting a season listing.
- Ticket price by party size and the full discount conditions: `city-parking-and-p-r.md`.

## Chinatown / Zeedijk specifics
- Zeedijk is a pedestrian street (the municipality has discussed designating it car-free) — do not drive or park on it.
- Unload at the loading bay on the Prins Hendrikkade side of the north end of Zeedijk: OSM records four loading-only places there (tagged `access:conditional = yes @ loading`) — drop off there, then park.
- Nearest metro for Chinatown is **Nieuwmarkt** (lines 53/54). Metro runs roughly 05:30 to 00:30-01:00, so a 23:00 departure is comfortable; treat anything after midnight as needing a timetable check.
- Walking distances: Oosterdok garage to Zeedijk ~600-800 m (8-10 min); Oosterdok garage to Nieuwmarkt ~670 m; P1 Centrum to Zeedijk ~500 m (all straight-line sanity-checked, so treat as a lower bound).

## Drive baselines (from the centre of The Hague, free-flow — 距海牙市区 X km)
The figures below were measured from a residential address in The Hague and are kept as the shape of the trip: re-compute with `python maps/scripts/maps_client.py distance "<from>" --to "<to>" --mode driving` for the real origin rather than reusing them.

- Amsterdam Chinatown / Zeedijk ~64 km, ~55 min from The Hague (距海牙市区约 64 km); P+R ArenA ~59 km, ~47-60 min; P+R Sloterdijk ~58 km; P+R Zeeburg ~63 km.
- Chinatown to P+R ArenA is a ~12 km / 20-25 min detour each way, which is what makes park-then-ride uneconomic once you have already delivered.

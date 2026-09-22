# Probing a parking booking flow

Goal: get the price and the field rules for a SPECIFIC date from the operator's own order form, instead of quoting the marketing "vanaf" price or a blog.

1. **Find the real order form.** Fetch the product page and list its script/iframe sources:
   `curl -s -L -A 'Mozilla/5.0 (X11; Linux x86_64)' <product page> -o p.html` then `grep -oE 'src="https?://[^"]+"' p.html | sort -u`.
   Municipal garages in the Netherlands commonly run their booking through Park-Spot/InPublic, which appears as `park-spot.com/parking/<operator>/<locale>/<location>/product/<product>`.
2. **HTTP-check every link you intend to hand over** with `curl -s -o /dev/null -w '%{http_code}'`. Short slugs 404 while the long slug works (e.g. an `avondkaart` path failing while `avondkaart-18-00-23-59-uur-eur-10` returns 200).
3. **Read the price for one date.** Post the product form with a cookie jar:
   `curl -s -c jar -b jar -X POST "<product url>" --data "arrival-date=2026-09-20" -L -o step2.html`
   ISO `YYYY-MM-DD` is the accepted format (a `DD-MM-YYYY` value came back as an availability error `error=form.error.no_spots_available` — do not misread that as "sold out"). The response is the information/checkout step and shows the real total for that date plus the exact arrival/departure window, which may differ from the advertised "from" price.
4. **Read the field rules off that page**, not from assumption: `grep` it for `<input ... name="..."` together with `required` and `data-validation=`, and for the inline hints (a plate field may carry "HOOFDLETTERS zonder streepjes" and a separate `kenteken-landcode` field expecting `NL`). The attribute actually attached to the field wins over any validator merely defined in the JS bundle.
5. **Before telling a user their input is wrong**, read the validator itself: grep the minified bundle for the validator name and read its rule array. A Dutch-plate validator that strips only two dashes and lists sidecodes 1-10 will reject sidecode 11 plates (`XXX-99-X`, issued since mid-2024) — useful to know so you can separate a form bug from a typo.
6. **Verify the vehicle with RDW open data (no key)** — swap in the plate you actually want to look up (the API wants it without dashes; `XX-999-X` is a placeholder, not a real plate):
   `curl -s -G "https://opendata.rdw.nl/resource/m9d7-ebf2.json" --data-urlencode "kenteken=XX999X"`
   Returns voertuigsoort, merk, handelsbenaming, `hoogte_voertuig`, `lengte`, first registration and tenaamstelling. Use it to confirm a plate is valid and to compare vehicle height with a garage's doorrijhoogte. RDW sidecode list: 7 `99-XXX-9`, 8 `9-XXX-99`, 9 `XX-999-X`, 10 `X-999-XX`, 11 `XXX-99-X` (from mid-2024), 12 `X-99-XXX`.
7. **Clean up**: reaching a step-2 page creates an unpaid draft reservation that expires by itself; never complete payment while probing, and do not hand the user a link to a draft.
8. If a page blocks extraction, a plain `curl` with a normal browser User-Agent often still returns it.

## Mapping notes
- Use the maps skill script for geocoding, POIs and distances: `python maps/scripts/maps_client.py nearby|distance|directions|reverse`. It handles the Overpass/Nominatim etiquette that hand-rolled requests to those endpoints trip over.
- Treat its **walking** distance/duration as indicative only: routes can come back wildly long for a short hop (a ~500 m straight line reported as a 4 km walk) and durations are understated (900 m "2.8 min"). When the route looks wrong, fall back to `straight_line_km` and estimate walking at ~5 km/h (~12 min/km), and use driving figures as free-flow lower bounds.

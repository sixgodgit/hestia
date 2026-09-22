# Den Haag zone maps and the one-page permit sheet

Use when the user wants a parking-zone map, the exact extent of a permit's zone, or a printable one-page sheet for a granted permit (bewonersvergunning). Keep the pipeline in a working folder with its own `README.md`, one generator per artifact, a `gegevens_<zone>.json` data file, plus JSON snapshots of both WFS layers. Change the JSON and re-run the script; never hand-edit the PDF.

## Sources, in this order

1. **Official folder PDF, one per zone.** Pattern: `https://www.denhaag.nl/wp-content/uploads/2022/02/<nummer>_DSB_..._Gebied_<code>_..._v<n>.pdf`. The municipal page that lists them (per stadsdeel) is client-rendered — plain `curl` returns a ~18 KB shell whose only href is the homepage. Read it through a reader proxy (`https://r.jina.ai/<page-url>`) to get the accordion text and the current PDF links, or render it with headless Chromium. Compare the linked file size against the download to confirm you have the version the page points at.
2. **WFS vector layers (always current, no key).** `Gisib_Vergunninggebieden_DPZ_TeamWebsites` = permit zones including the sub-codes; `Gisib_Tariefgebieden_DPZ_Teamwebsites` = tariff zones with the hourly rate inside `WERKINGSTIJDEN`.
3. **The street list where the permit does NOT apply** is printed on the folder's map page and is only readable as page text: `pdftotext -f 2 -l 2 <folder>.pdf -` and read around `niet geldig`. Copy those streets verbatim into the sheet. Do **not** reconstruct this list from the sub-zone polygons: they are narrow corridor shapes, and a house centroid on one of those streets often sits 10–500 m outside the polygon.

## Finding a Leaflet map's data layer

Gemeente maps declare their layers in the markup. Render the page once (a Python environment with playwright + chromium available is enough) and read the rendered HTML for `data-draad-geojson` / `.draad-maps__dataset[data-draad-type]`, or capture the requests during load. That is where the WFS URL comes from — the same trick works for other municipalities' Leaflet maps, and it is what turns a picture into queryable geometry.

## Point test and geometry

No shapely/matplotlib needed — pure Python is enough and avoids an install:

- Geocode the address with Nominatim (`format=jsonv2`, `countrycodes=nl`); it returns `lon,lat` order. Sleep ≥ 1 s between calls.
- Point-in-polygon by ray casting, testing the outer ring and rejecting interior rings (holes).
- Area by shoelace on `lon * 111320 * cos(lat)` / `lat * 110574`.
- Report the hours of the **specific polygon** that contains the point, not the first feature carrying that code (a code can repeat across disjoint polygons with different `WERKINGSTIJDEN`).

## Rendering the map

Stitch OSM tiles (`https://tile.openstreetmap.org/{z}/{x}/{y}.png`, a plain User-Agent, cache to disk) and convert lat/lon with the Web Mercator formulas; z=16 for a zone, z=13 for a city overview. Colour by the paid-hours regime (two zones can share one code with different regimes), outline the requested zone in red, draw the exclusion sub-zones in a second strong colour, and label each code at the centre of its bounding box.

## The one-page sheet

- **Table cells must be `Paragraph` objects.** A plain string in a reportlab `Table` overflows into the neighbouring column and prints two texts on top of each other. Paragraphs wrap instead.
- Long Dutch compounds (`Vergunningsnummer`, `Parkeerproduct`) then wrap **mid-word** in a narrow label column. Size the label column to the longest label, or drop those cells to ~7 pt — do not rename the field to something shorter than the municipality's own wording.
- **Re-check the page count after every width/font/leading change.** Wrapping cells grow the table and can silently push the final line onto page 2.
- Embed the map as a downscaled JPEG (~1600 px wide, quality ~92) rather than the 300 dpi PNG: same print result at ~10 cm width, ~1.3 MB instead of ~7 MB.
- Put the pipeline in a script file and run that, rather than driving many steps through long inline one-liners — oversized inline payloads with regexes are refused by the command guard and cost a round trip.
- Verify before reporting: one page, real values present in the extracted text, no leftover placeholders, and page 1 rendered and looked at.

## The phone companion (optional)

A permit zone is easier to live with as a phone PWA that locates the user, names the zone, decides permit validity and says whether paid parking applies right now. Build it off the same zone data: a data-prep script turns the WFS snapshots into the app's data file, and a test script guards the hours parser. Read the folder's `README.md` before touching the map or the hours parser, and rebuild the app data after every zone change rather than editing the app's copy.

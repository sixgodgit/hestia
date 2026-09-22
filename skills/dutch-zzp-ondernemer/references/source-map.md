# Source map: where each eenmanszaak fact comes from

Authority order: Belastingdienst / KVK / gemeente / business.gov.nl /
ondernemersplein.overheid.nl (executive agencies) → eerstekamer.nl /
tweedekamer.nl / wetten.overheid.nl (law in motion) → advisor and insurer pages
(context only, never the sole source of a number).

## Fetch ladder — cheapest rung that works

1. **`scripts/nl_source_fetch.py`** — plain HTTP, ~0.3 s/page, clean text,
   deterministic and easy to quote. Correct for every server-rendered primary
   source below, so start here.
2. **`scripts/firefox_fetch.py`** — real headless Firefox via geckodriver,
   ~1 s/page after a ~4 s session start. Use when rung 1 returns 403/429 or 200
   with no prose (JS-only), or when you need the page as a user sees it.
   Measured 2026-09 on one host: denhaag.nl and belastingdienst.nl both 200 with
   full prose, where scripted fetches were each 403'd by one of them.
   Caveat: `innerText` includes the site's own chrome (cookie-consent banner,
   navigation) before the article body — read past the first screenful; keep
   rung 1 for citation-grade text.
3. **`--ua curl` on rung 1** — last resort. It works only because these gates
   are crude per-host header heuristics, so outcomes are arbitrary: a spoofed
   browser UA is blocked by denhaag.nl, a plain script UA by belastingdienst.nl.
   The default `--ua auto` tries the browser UA first and retries as the curl UA
   on 401/403/429, printing which one worked — so never conclude "gated" from a
   single 403. Never present it as impersonating a human; prefer rung 2 when a
   page resists, and never raise the request rate — single-page reads at human
   pace are the defensible line, not the UA string.

## What each host wants

| Host | Accepts | Blocks |
|---|---|---|
| belastingdienst.nl, kvk.nl, business.gov.nl, ondernemersplein.overheid.nl | browser UA | UA-less / script UA |
| denhaag.nl | curl/python/wget UA, or no UA | spoofed browser UA (403) |
| mijnzakelijk.belastingdienst.nl | needs a session | returns 200 + no prose |

Neither host has a usable sitemap (belastingdienst.nl `/sitemap.xml` serves the
404 page), and slugs are inconsistent inside one parent, so a wrong guess returns
HTTP 404 rather than a 200 shell. Discover URLs by `web_search`, or by `--links`
on a sibling page in the same subtree.

Snap-Firefox trap for rung 2: the snap `home` interface cannot read **hidden**
directories, so a WebDriver profile under `~/.cache/...` fails with
`Failed to set preferences: unknown error`. Use a non-hidden path —
`firefox_fetch.py` defaults to `~/ff-wd-profile` for that reason.

`web_search` / `web_extract` do not fetch from the local host: they go through
remote backends (Keenable/Firecrawl/Exa), so local IP reputation never enters
into their 403s — and a 403 there says nothing about what the local browser can
reach. The keyless backends also fail intermittently (`Keyless Firecrawl search
failed: 403`, `Unrecognized MCP response shape`); fire 2-4 independent searches
per round.

## Stable pages (URL and slug stay put)

| Topic | URL |
|---|---|
| btw-id vs omzetbelastingnummer, 10-working-day registration | https://www.belastingdienst.nl/wps/wcm/connect/nl/btw/content/btw-identificatienummer-en-omzetbelastingnummer |
| KOR (€20,000, opt-in/out, EU-KOR) | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/hoe_werkt_de_btw/kleineondernemersregeling/kleineondernemersregeling |
| Factuureisen | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/administratie_bijhouden/facturen_maken/factuureisen/factuureisen |
| Who must invoice | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/administratie_bijhouden/facturen_maken/wie_zijn_verplicht_te_factureren |
| Bewaarplicht 7/10 years, digital files | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/administratie_bijhouden/administratie_bewaren/administratie_bewaren |
| btw-aangifte: starter, aangiftebrief, nil returns | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/btw_aangifte_doen_en_betalen/btw-aangifte-waar-moet-u-aan-denken/ |
| Aangiftetijdvak switch (month/quarter/year, €1,883 rule) | https://www.belastingdienst.nl/wps/wcm/connect/nl/btw/content/wijziging-aangiftetijdvak-btw |
| Filing/payment deadline tables per period | https://www.belastingdienst.nl/wps/wcm/connect/nl/btw/content/uiterste-aangifte-en-betaaldatums |
| Btw aftrekken / voorbelasting (rubriek 5b, conditions) | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/btw_aftrekken/btw_aftrekken |
| Btw terugvragen uit andere EU-landen (route) | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/zakendoen_met_het_buitenland/btw_terugvragen_uit_het_buitenland/btw_terugvragen_uit_andere_eu_landen |
| When may you file such a request (deadline 30 Sep, thresholds €50/€400) | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/zakendoen_met_het_buitenland/btw_terugvragen_uit_het_buitenland/wanneer_kunt_u_een_verzoek_doen/ |
| Mkb-winstvrijstelling (percentage = a yearly page too) | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/mkb_winstvrijstelling |
| Ziektekostenverzekering premiums not deductible | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/ziektekostenverzekering |
| AOV for entrepreneurs: deductibility split | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/arbeidsongeschiktheidsverzekering-voor-ondernemers |
| AOV premiums as uitgaven voor inkomensvoorzieningen (FISIN) | https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/uitgaven_voor_inkomensvoorzieningen |
| Login options per rechtsvorm, DigiD suffices for eenmanszaak | https://www.belastingdienst.nl/wps/wcm/connect/nl/home/content/hulp-inloggen-belastingdienst-zakelijk |
| KVK inschrijfvergoeding (amount updated yearly, same URL) | https://www.kvk.nl/inschrijven/inschrijfvergoeding |
| KVK 1-week change duty | https://www.kvk.nl/hulp-en-contact/hulp-bij-wijzigen-en-uitschrijven/ |
| KVK address change, bezoekadres vs postadres forwarding | https://www.kvk.nl/wijzigen/adres-wijzigen/ |
| KVK tax-rate overview for the year (box 1 rates, handy cross-check) | https://www.kvk.nl/geldzaken/belastingtarieven-2026/ |
| business.gov.nl: sole proprietorship, urencriterium 1,225 h, liability | https://business.gov.nl/running-your-business/legal-forms-and-governance/sole-trader-or-sole-proprietorship-in-the-netherlands/ |
| business.gov.nl: keeping business records | https://business.gov.nl/regulations/keeping-business-records/ |
| Ondernemersplein: AOV premium is a box-1 deduction, not a business cost | https://ondernemersplein.overheid.nl/bedrijfsvoering/verzekeringen/arbeidsongeschiktheidsverzekering/ |
| Ondernemersplein: Handelsregister + 1-week change duty | https://ondernemersplein.overheid.nl/wetten-en-regels/inschrijven-in-het-handelsregister/ |
| Den Haag: bedrijf aan huis conditions (30% / 40 m², no permit) | https://www.denhaag.nl/nl/ondernemen/starters/bedrijf-en-beroep-aan-huis-starten/ |
| Den Haag: omgevingsvergunning tarieven / omgevingsplan | https://www.denhaag.nl/nl/vergunningen-en-ontheffingen/omgevingsvergunning-aanvragen/ |
| Den Haag: omgevingsplan rules for your surroundings | https://www.denhaag.nl/nl/vergunningen-en-ontheffingen/omgevingsplan-regels-over-uw-omgeving/ |

## Year-scoped pages — re-fetch every January

Belastingdienst keeps a subtree per tax year; the amounts live under it and the
generic parent page only links to it. Pattern:

```
.../zakelijk/winst/inkomstenbelasting/veranderingen-inkomstenbelasting-<JAAR>/
  ondernemersaftrek-<JAAR>/zelfstandigenaftrek-<JAAR>
  ondernemersaftrek-<JAAR>/stakingsaftrek-<JAAR>
  mkb-winstvrijstelling-<JAAR>
  investeringsaftrek-<JAAR>
  bijtelling-privegebruik-auto-<JAAR>
```

Also year-scoped but updated **in place** at a stable URL: Zvw percentages
(https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/prive/werk_en_inkomen/zorgverzekeringswet/veranderingen-bijdrage-zvw/percentages-zvw)
and the KVK/Belastingdienst tax-rate overviews. Check the wording ("Vanaf 2026")
rather than the URL to see which year the page describes.

## Law-in-motion trackers

| Item | Tracker |
|---|---|
| Wet BAZ (mandatory AOV for IB-ondernemers, ~2030, ~5.4% capped ~€171/m) | https://www.tweedekamer.nl/kamerstukken/wetsvoorstellen/detail?cfg=wetsvoorsteldetails&qry=wetsvoorstel%3A36912 |
| Rechtsvermoeden uurtarief (€38, Stb. 2026, 158, in force by KB) | https://www.eerstekamer.nl/wetsvoorstel/36783_wet_invoering |
| Effective-date search across all three | https://wetten.overheid.nl/ (search the wet name; "Geldend van … t/m heden") and https://www.eerstekamer.nl/ (phase field: *opgenomen in Staatsblad*) |

## Traps seen in the wild

- **Year drift in advisor blogs.** Guides dated for the current year quoted the
  previous year's zelfstandigenaftrek. Only the Belastingdienst year subtree
  settles it.
- **Stale wetstraject claims.** "Wet VBAR per 1 juli 2026" was written before the
  bill was split; the verduidelijking part was dropped and only the €38
  rechtsvermoeden survived as 36.783. Always re-check the bill's current phase
  instead of repeating a dated advisor summary.
- **"Mandatory AOV" without a date.** It is a wetsvoorstel with an expected start
  around 2030; the peildatum is not yet published.
- **Consent/chrome pages** (DPG Media titles, some bank blogs) return chrome and
  no prose to a fetcher — never write as if you read the body.
- **JS-only pages return 200 with no prose.** That is a page-source limit, not a
  fetch failure; say so instead of paraphrasing chrome. Escalate to the real
  browser rather than escalating the UA string.
- **Keyless `web_search` backends fail intermittently** (Firecrawl 403, Exa shape
  errors). Fire several searches per round and reword on failure.

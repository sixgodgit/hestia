# Where the Dutch budget numbers live

Map of the Prinsjesdag package and its follow-up documents — which page or
section holds which figure, so a future session fetches once instead of paging
through PDFs.

## Miljoenennota (full text: `rijksfinancien.nl/miljoenennota/<year>`)

| Section | Holds |
|---|---|
| §1.3.2 Actuele stand van de overheidsfinanciën | Cabinet's own EMU-saldo and debt path for the cabinet period. |
| Tabel 4 Inkomstenkader | Revenue-side measure list with per-year amounts (rates, heffingskortingen, accijnzen, abolished regelingen, innovatiebox, EIA). |
| "Toelichting maatregelen" (follows each measure table) | One paragraph per measure — the only place the effective date is stated in prose, and where you verify what a table row actually means. |
| §2.3.2 Koopkracht en energiepakket | Median koopkracht, armoedecijfer / kinderarmoede, the "technische invulling" of the buying-power package and how it is financed. |
| §2.7, verticale & horizontale toelichting | Per-ministry spend, kasschuiven, onderuitputting, in=uit-taakstelling. |

Measure tables print 2026..2031 + structureel columns, but empty cells vanish
on text extraction — never infer a column from position.

## Rijksbegroting

One hoofdstuk per ministry, plus the fondsen: Mobiliteitsfonds, Gemeentefonds,
Provinciefonds, Deltafonds, Defensiematerieelbegrotingsfonds, Klimaatfonds,
Nationaal Groeifonds, Diergezondheidsfonds, BES-fonds.

## Belastingplan package

Usually four wetsvoorstellen: Belastingplan, Overige fiscale maatregelen,
minimumbelasting amendments, and one thematic bill (the 2027 package carried a
startups/scale-ups bill). The pre-disclosure "voorlopige inhoud pakket" annex,
published before Prinsjesdag, is the earliest citable list of the whole package
and carries the per-measure effective dates the Miljoenennota table cannot.

## Independent checks (cite alongside the cabinet's own numbers)

- CPB MEV page (`cpb.nl/raming/raming-<maand>-<jaar>-mev-<jaar>`) — bbp,
  inflatie, median koopkracht, werkloosheid, EMU-saldo, plus the deviation from
  the cabinet's earlier cMEV, and which EU budget rule is missed.
- Tax-advisor roundups (Grant Thornton, EY, SRA, Rendement, Jongbloed) — fastest
  route to a measure list, because they read the wetsvoorstel text that the
  Miljoenennota only summarises.

## Rijksoverheid news items — the per-domain figures

Prinsjesdag publishes one news item per ministry, all timestamped the same
minute. The Financiën item carries the headline totals; the EZK / OCW / VWS /
BZK / VRO items carry the program-level numbers (subsidies, funds, per-sector
budgets) that never reach the main release. Sweep these when the user asks
about a specific sector.

## Troonrede

Full text at Rijksoverheid / Koninklijk Huis. Treat it as intent and political
framing — it carries no figures worth citing, but it is the best single source
for the cabinet's stated priorities and its "not everything at once" caveats.

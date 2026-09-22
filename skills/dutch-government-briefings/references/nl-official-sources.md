# Dutch Official Sources: Where Each Figure Lives

The publishing body's own page beats every summary of it. Dutch government
figures are consistent only within one document — the ministry's Miljoenennota
and the CPB's MEV both describe the same budget year and regularly disagree,
which is why the source map below matters more than the numbers in it.

## Endpoints

| What | URL pattern | Notes |
|---|---|---|
| Ministry press release | `rijksoverheid.nl/actueel/nieuws/<yyyy>/<mm>/<dd>/<slug>` | One per policy theme, all published at the same minute on budget day; carries that theme's sums and the minister's quote |
| Topic hub | `rijksoverheid.nl/onderwerpen/prinsjesdag` | That day's news list, plus links to Troonrede, Belastingplan, Miljoenennotaposter |
| Official stukken list | `rijksoverheid.nl/onderwerpen/prinsjesdag/miljoenennota-en-andere-officiele-stukken` | The PDF set, ministry by ministry. The `/themas/overheid-en-democratie/...` variant of the same page 404s — use the `/onderwerpen/` path |
| Miljoenennota, full text | `rijksfinancien.nl/miljoenennota/<year>` | Whole document as HTML with a table of contents — no PDF needed |
| Bijlagen / Belastingplan | `rijksfinancien.nl/miljoenennota/<year>/bijlage`, `rijksfinancien.nl/belastingplan-<year>` | The budgettaire kerngegevens table and the fiscal package |
| CPB raming | `cpb.nl/raming/raming-september-<year>-mev-<year+1>` | MEV page: the kerngegevens table plus the delta column against the August concept raming (cMEV) |
| Rule text, once enacted | `wetten.overheid.nl`, `zoek.officielebekendmakingen.nl`, `lokaleregelgeving.overheid.nl` | Where a September proposal becomes readable law; municipal verordeningen live in the last one |

The year in a Miljoenennota URL is the budget year, not the publication year:
the document opened in September of year N is `miljoenennota/N+1`.

## Which figure is authoritative where

| Figure | Read it from |
|---|---|
| EMU-saldo, debt path, uitgavenkader, the composition of the koopkrachtpakket | Miljoenennota, sections 1.3.2 (stand overheidsfinanciën), 2.1 (kerngegevens), 2.3.2 (koopkracht en energiepakket) |
| GDP growth, inflation, median koopkracht, unemployment, and the recalculated EMU-saldo | CPB MEV page (it also states the EMU-saldo 0.1pp away from the ministry's own figure — report both) |
| Tax rates, heffingskortingen, accijnzen, btw | Belastingplan + the day's fiscal press round-ups |
| Per-ministry spending | That ministry's own news item, and its begroting chapter in the stukken list |

## Reading the Miljoenennota as text

- Anchor on section headings, not on numbers: search for `2.3.2 Koopkracht en
  energiepakket`, `verticale toelichting`, `onderuitputting`, and read the
  surrounding prose. Tables arrive flattened, so a row's years appear as a run
  of figures (`450,7 488,7 510,6 532,7`) with the label somewhere before them.
- The prose sections answer the "how is it paid for" question that the press
  round-ups usually skip: `onderuitputting`, `In=uit-taakstelling`,
  `kasschuiven`, and the freezing of the toptarief threshold are all there as
  named measures with amounts.

## Fetch recipe when the extract tool is refused

A 403 from an extraction backend says nothing about the site. Re-issue the call
once (different backends serve successive requests), then fall back to a plain
fetch with a desktop user agent and strip the markup locally:

```bash
curl -sSL -A "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
(Gecko) Chrome/128 Safari/537.36" -o /tmp/page.html -w "%{http_code}\n" "$URL"
```

```python
import re
from html.parser import HTMLParser

class Text(HTMLParser):
    def __init__(self):
        super().__init__(); self.out = []; self.skip = 0
    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style", "noscript"): self.skip += 1
        if tag in ("p", "div", "li", "h1", "h2", "h3", "tr", "br"):
            self.out.append("\n")
    def handle_endtag(self, tag):
        if tag in ("script", "style", "noscript") and self.skip: self.skip -= 1
    def handle_data(self, data):
        if not self.skip: self.out.append(data)

def to_text(path):
    p = Text(); p.feed(open(path, encoding="utf-8", errors="ignore").read())
    t = "".join(p.out)
    t = re.sub(r"[ \t\xa0]+", " ", t)
    return re.sub(r"\n\s*\n+", "\n", t).strip()
```

## Domain behaviour

| Domain | Behaviour |
|---|---|
| rijksoverheid.nl, rijksfinancien.nl, cpb.nl | Full text; the ministry and CPB pages are the two you must read |
| nos.nl, nu.nl, iex.nl, dutchnews.nl | Full text; best for what the documents leave unsaid |
| parool.nl, ad.nl, volkskrant.nl, trouw.nl, telegraaf.nl | DPG/consent gate: HTTP 200 with an empty "Privacy Gate" body. Cite only the search snippet's literal wording and say the article was not read |
| nrc.nl | Analyses partly readable; treat gaps as gaps |

## Timing

Press liveblogs (NOS) are updated through the afternoon: the Troonrede lands
around 13:15, the koffertje around 15:30, and the ministry news items minutes
later. A brief written before those timestamps is written against leaks.

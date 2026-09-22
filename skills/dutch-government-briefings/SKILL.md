---
name: dutch-government-briefings
description: "Use when summarizing Dutch government or budget news."
version: 1.0.0
version: 1.0.0
license: CC BY-NC 4.0
author: sixgod
category: research
metadata:
  hermes:
    tags: [dutch, rijksoverheid, prinsjesdag, belastingplan, budget, briefing, citations]
    category: research
    related_skills: [dutch-official-documents, grounded-citations, blocked-page-recovery]
---

# Dutch Government Briefings

Answer "what did the Dutch government announce / what changes for me" from the
publishing ministry's own pages, with every figure attributed to the document
that states it. The user is a Chinese speaker living in the Netherlands: the
briefing is Chinese, the official documents and their titles stay Dutch.

## When to Use

- Budget day and its run-up (Prinsjesdag: Miljoenennota, Rijksbegroting,
  Belastingplan, Troonrede, CPB's MEV) and the debates that follow.
- A ministry announces plans on a theme (tax, zorg, wonen, asiel, klimaat,
  defensie, mkb) and the user asks what it means or wants the round-up.
- A recent decision or upcoming rule change the user is subject to, including
  gemeente-level decisions that ride on national policy.
- Not for drafting a submittable letter or declaration — that is
  `dutch-official-documents`. Not for private-company news — that is
  `competitor-news-monitor`.

## Standing preferences (this user)

- Reply in Chinese; keep document names and technical terms Dutch on first
  mention (Miljoenennota, Rijksbegroting, Belastingplan, koopkracht,
  eigen risico, vrijheidsbijdrage) — the user reads the Dutch sources too.
- Flat structure, no nested headings: bold one-line section labels, short
  bullets, each figure with its unit and base (%, bbp, mln/€ miljard).
- Inline `[n]` citations plus a `Sources:` block (run the
  `grounded-citations` ledger); never a bare URL, never a number without the
  source that states it.
- Say plainly which items are still proposals that need Tweede/Eerste Kamer
  approval, and which source you could not read in full.
- Close by offering one concrete follow-up (a deeper dive on the item that
  hits the user's own wallet, a PDF/Obsidian version) instead of restating
  the brief.

## Procedure

1. **Fix the date and the event before searching.** Run `date`; a budget day
is the third Tuesday of September, so confirm which budget year is being
published (in September of year N the plans are for N+1) before writing a
word. Getting the year wrong poisons every figure.
2. **Search in Dutch**, not Chinese or English translation: the ministry
pages, CPB and the Dutch press index on Dutch terms (`Prinsjesdag`,
`Miljoenennota`, the minister's name, `koopkracht`, `eigen risico`).
Chinese-language queries for NL policy return thin aggregator pages.
3. **Read the official pages first, one press release per theme.** On budget
day every ministry posts its own news item at the same minute; each one
carries the sums for its own policy area, and the hub page gives you the
list of what else was published that day. Take the headline framing
(theme title, three pillars, the minister's quote) from there.
4. **Pull the whole document as text, not as a PDF.** The Miljoenennota and
its bijlagen are served as full HTML with a table of contents; read the
sections you need (budgettaire kerngegevens, koopkracht, uitgavenkader,
verticale toelichting) out of that instead of parsing a 7 MB PDF. See
`references/nl-official-sources.md` for the URLs and the fetch recipe.
5. **Treat the Troonrede as direction, not data.** It is written by the PM
and is rhetorical: it names the priorities (stikstof, wonen, migratie,
sociale stelsel, defensie) and the honest limits ("niet alles kan
tegelijk", "de rekening niet vooruitschuiven"), but the numbers live in the
Miljoenennota and the MEV. Cite the speech for intent only.
6. **Then use the press for interpretation and for what the documents leave
unclear** — who the measures are a concession to, what a figure actually
adds up to after its own financing, which part is legally shaky.
7. **Label every item with its status** as you write: officially published /
announced in the speech / leaked before the day / proposal needing both
chambers. The user is deciding what to act on.
8. **Register sources in the ledger while retrieving, cite per line, then
verify** — one sentence per line, or the >3-citations check trips on a line
that carries two sentences.

## Pitfalls

- **The cabinet's own raming and the CPB doorrekening disagree, and both are
official.** The Miljoenennota's EMU-saldo, debt path and koopkracht figure
come from the ministry's own arithmetic; the MEV page recomputes the same
year for the CPB. Print both with attribution (which document, which
percentage) and name the difference as a口径 difference — do not average
them, pick the rounder one, or write a single headline deficit. Where the CPB
also flags it (e.g. net expenditure growth above the agreed EU path), that is
the strongest line in the brief.
- **Half the budget is in the press days before the official day.** Leaked
stukken are pre-coverage, not the announcement: write the brief against what
was actually published, and where a leak-derived figure was known to move
(gross koopkrachtpakket versus the net burden relief after its own
financing) use the published number and say the earlier one was superseded.
- **A package's headline size is not its effect.** Look for what finances the
package: measures described as koopkrachtreparatie are routinely paid for by
raising the tax on the group being "helped" (ouderenkorting,
top-schijf). Report the gross and the net, and who pays.
- **Politically overloaded words are the story, not a translation problem.**
`vrijheidsbijdrage` is a tax increase by another name (stopping full
inflation-correction of brackets and credits); "uitstel" of a bezuiniging is
a one-year deferral, "afstel" a cancellation; "onderuitputting" is budgeted
departments are assumed not to spend. Explain the mechanism in one clause
rather than rendering the word.
- **Paywalled DPG titles return an empty body with HTTP 200.** Parool, AD,
Volkskrant, Trouw and Telegraaf give a "DPG Media Privacy Gate" page: cite
only what the search snippet literally states, and say the article itself was
not read. rijksoverheid, rijksfinancien.nl, cpb.nl, NOS and IEX extract fine.
- **An extraction error is not proof the source is unreachable.** Re-issue
the search or extract (requests are served by different backends, so the same
call can fail once and succeed on retry); if it still fails, fetch with a
desktop user agent and strip the tags locally — the recipe is in
`references/nl-official-sources.md`.
- **Never cite a search snippet for a claim that needs the page body.**
Snippets from gelekte-stukken articles are how a superseded figure ends up in
the brief looking authoritative.

## The budget year at a glance

| Moment | When | What lands |
|---|---|---|
| cMEV + leaked stukken | August, and the week before Prinsjesdag | Press gets the plans early; treat as pre-coverage |
| Prinsjesdag | 3rd Tuesday of September | Troonrede; Miljoenennota + Rijksbegroting + Belastingplan for N+1; CPB MEV |
| Algemene Politieke Beschouwingen | The Wednesday and Thursday after | The political debate; opposition amendments announced here |
| Voting | From mid-November | Where the actual majorities are decided for a minority cabinet |
| Verantwoordingsdag | 3rd Wednesday of May | Year reports: what actually happened with last year's plans |
| Voorjaarsnota / Najaarsnota | Spring / autumn | In-year updates; the Voorjaarsnota is where coalition-agreement plans surface first |

New legislation trails the announcement by months and is routinely amended —
a "€400 eigen risico" or a tax rate in September is a proposal until the
Belastingplan passes.

## Verification

- Every figure in the reply maps to a `[n]` whose source states it; run
`sources.py verify <draft> --strict` until clean (see `grounded-citations`).
- Both sides of any disagreement between the ministry and the CPB appear, each
with its own citation.
- The reply states which items are proposals, and names any source read only
as a snippet.
- Sanity-check the arithmetic the brief asserts: totals against their parts,
and a per-household figure against its population (a per-m³ water tax against
a household's yearly litres).

## Support files

- `references/nl-official-sources.md` — the source map (which page publishes
which figure), the HTML-as-text fetch recipe, and the paywall behaviour per
domain.

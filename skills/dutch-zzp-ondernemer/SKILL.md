---
name: dutch-zzp-ondernemer
description: "Use when handling Dutch ZZP/eenmanszaak rules or duties: btw-id and voorbelasting, invoices, KOR, KVK/Belastingdienst post."
version: 1.0.0
author: sixgod
license: CC BY-NC 4.0
metadata:
  hermes:
    tags: [Netherlands, ZZP, eenmanszaak, KVK, Belastingdienst, Compliance]
    category: research
    related_skills: [dutch-tax-and-budget-changes, grounded-citations, dutch-official-documents]
---

# Dutch ZZP / eenmanszaak Operations

Running a Dutch sole trader (eenmanszaak / zzp'er): what has to be arranged after
KVK registration and kept up while trading — registering or changing the
business, the Belastingdienst numbers and login, btw / KOR / aangiftetijdvak,
invoicing and record-keeping, the Zvw and insurance position, municipal rules for
working from home, and the status of ZZP legislation that is passed but not yet
in force.

It does NOT cover the annual Prinsjesdag/Belastingplan package (that is
`skills/dutch-tax-and-budget-changes/`), BV/DGA structures, employer payroll, or
drafting official letters (`skills/dutch-official-documents/`).

## When to Use

- The user has just registered a KVK number and asks what is still needed
- Questions about btw-id vs omzetbelastingnummer, aangiftetijdvak, KOR,
  factuureisen, bewaarplicht, urencriterium, zelfstandigenaftrek/startersaftrek
- "Do I need insurance / a business bank account / a permit to work from home?"
- "Must I report this change to KVK?", "I got a letter from the Belastingdienst"
- Not for: BV/DGA, employer payroll, next year's fiscal package
  (`skills/dutch-tax-and-budget-changes/`), or drafting official letters

## Output shape (standing preferences)

- Reply in Simplified Chinese; Dutch terms in parentheses on first use
  (btw-id, omzetbelastingnummer, urencriterium, aangiftebrief, KOR).
- Flat list of short bold labels. No nested headings, no process narration, no
  restating the question.
- **Split the answer into 必须做 / 建议做.** These questions arrive as "what else
  do I need", and the user acts on the list; burying a legal obligation inside
  optional advice is the failure mode.
- Put the tax year on every figure (zelfstandigenaftrek, KOR threshold, Zvw %).
  Dutch amounts reset each January; a bare number reads as current when it may
  not be.
- Bracket citation per outside fact plus the `Sources:` block from
  the external `grounded-citations` skill.
- **Deliver the artifact into the chat, not a path to it.** When the answer
  produces a letter, form, invoice or template, send the file as
  `MEDIA:/absolute/path` on its own line. Naming a path the user then has to
  open themselves is not a delivery.
- Close by naming the one decision that changes the answer and offer to compute
  it (usually KOR: it hinges on the turnover band and on whether customers are
  businesses who want to reclaim input btw). Ask for those facts; never assume
  a turnover.

## Prerequisites

- `terminal` to run the scripts in `scripts/`. `nl_source_fetch.py`,
  `firefox_fetch.py` and `vies_check.py` are stdlib-only, so the system
  `python3` runs them even where system python has no third-party libraries.
  `make_factuur_template.py` needs `python-docx` and therefore the agent venv
  python.
- Rung 2 of the fetch ladder (`scripts/firefox_fetch.py`) needs `geckodriver`
  (snap: `/snap/bin/geckodriver`) and Firefox on the host. If the agent's toolset
  has no `browser_*` tool, geckodriver + Firefox is the only local real-browser
  route.
- `web_search` for URL discovery (keyless backends; they fail intermittently —
  see Pitfalls).

## Procedure

1. **Fix the tax year first.** Run `date`, then fetch the current-year
   Belastingdienst pages. Every money figure in this domain is year-scoped and
   changes on 1 January — never reuse last year's amounts from memory, from the
   reference file, or from a blog table. Completion: you have named the target
   year and know which claims are year-scoped.
2. **Primary sources, in this order:** Belastingdienst for amounts and
   obligations, KVK / business.gov.nl / ondernemersplein.overheid.nl for process
   steps, gemeente (Den Haag) for local permits, eerstekamer.nl /
   tweedekamer.nl / wetten.overheid.nl for law in motion. ZZP blogs and bank
   sites (zzp-pulse, Rabobank, Knab, Contabook) are useful to surface items the
   official pages bury, but they are leads — cite the official page for the rule
   itself and never let an advisor page carry a number alone.
3. **Check staleness of the reference file.** Its header carries a `Verified:`
   year. If that year ≠ the current year, re-fetch every URL marked *year-scoped*
   in `references/source-map.md`, deliver the answer, then update the reference
   file with `skill_manage(action='patch')`. Completion: the file either still
   says the current year or has been updated.
4. **Fetch with the right tool and read the status line.** Rung 1 is
   `scripts/nl_source_fetch.py` (plain HTTP, ~0.3 s/page, clean text,
   deterministic — correct for every server-rendered primary source). Escalate to
   rung 2, `scripts/firefox_fetch.py` (real headless Firefox), when rung 1 returns
   403/429 or 200 with no prose. Per-host behaviour, the UA profiles and the
   escalation caveats: `references/source-map.md`. Completion: each number in
   your draft is text a fetch in *this* session printed.
5. **Do not guess depth-linked URLs** — most plausible-looking paths return 404
   (and belastingdienst.nl has no usable sitemap: `/sitemap.xml` serves the 404
   page). Take the exact URL from a search result, or from `--links` on a sibling
   page in the same subtree, then fetch it.
6. **Establish the user's stage.** Registered at KVK? Which of the two number
   letters received? Which aangiftetijdvak? Completion: you know which checklist
   items are already done.
7. **Ask only the unknowns that change the answer** — turnover band (≤ / >
   €20,000, drives KOR), clients B2B vs B2C, EU cross-border work (drives ICP),
   home office or external premises. One `clarify` form, choices not prose.
   Completion: no recommendation rests on an assumed fact.
8. **Personalize and prune.** For a no-employee ZZP who does not own a company
   car, the following never apply and must not appear: employer premiums
   (Whk/Aof/Awf/Ufo), bijtelling and car costs, childcare, ouderenkorting,
   loondienst items. Municipal matters belong to the gemeente, not the
   Rijksoverheid.
9. **Register every URL in the citation ledger and verify before drafting** —
   bracket citation after every sentence carrying an outside fact, then the
   rendered `Sources:` block from the external `grounded-citations` skill.

## Incoming post: explaining a letter the user photographed

The user photographs official post (often sideways, phone camera) and opens with
"帮我看看是什么意思". The deliverable is not a translation only: one-line verdict,
letter metadata, paragraph-level plain-Chinese explanation, 必须做 / 建议做, and an
explicit list of what is still missing.

1. **Normalize the orientation before reading.** Phone photos carry an EXIF
   orientation (e.g. `upper-right`) that the vision tool ignores, so the first
   look comes back sideways and the text is unreadable. Rotate a copy and read
   that, using the agent venv python (Pillow installed):

   ```
   python -c "from PIL import Image; im=Image.open(SRC); im.rotate(-90, expand=True).save('rot_cw.jpg')"
   ```

   Try `+90` too and keep whichever reads left-to-right. Completion: the header
   line reads horizontally.
2. **Read the whole page for the letter type, then verify the fields you will
   quote** — `Datum`, `Kenmerk`, `Betreft:`, page count — with `vision_analyze`
   `region=[x1,y1,x2,y2]` crops. Pass ORIGINAL-image pixel coordinates: the tool
   reports its downscale factor ("multiply by N"), so a crop derived from the
   downscaled render lands on blank paper and looks like an illegible letter
   rather than a missed crop. A blank grey crop means wrong coordinates, never
   "can't read it" — recompute and retry. When coordinates are fiddly (small
   print on a rotated phone photo), crop-rotate-upscale with PIL instead —
   `im.crop(box).rotate(-90, expand=True)` then `.resize((w*2, h*2))` — and read
   that file; it beats fighting the coordinate arithmetic.
3. **Check "Pagina N van M" before drafting.** The opening paragraphs announce
   that the operative details sit later ("vindt u verderop in deze brief"), so
   from page 1 alone you can state neither the tax types, nor the tijdvak, nor
   the ob-nummer. Say which pages you still need and ask for them instead of
   filling the gap with a plausible guess.
4. **Translate the boilerplate clauses as boilerplate.** Clauses about later
   reassessment, information requests and retroactive loss of liability read as
   threats to a non-native reader; label them standard. Reassure explicitly when
   no payment, reply or application is involved.
5. **A `Datum` a few days ahead of `date` is a print/batch date**, not an error
   to investigate. Note it in one line at most.
6. Close by asking for the missing pages and offering to turn them into a dated
   "what to file, when" list — that is the follow-up this user wants.
7. **Archive one JPG per page and read those, not a merged PDF.** A scan carries
   no text layer, so sending it through a text reader ends in an OCR error and
   tempts you into a converter you do not need. Keep
   `brieven/<YYYY-MM-DD>_<type>/pageN_*.jpg`, read the JPGs with `vision_analyze`,
   and treat a combined PDF as archive-only.

Letter-type catalogue, standard clauses and formats:
`references/belastingdienst-letters.md`.

## The btw-id: verify it, then hand over the invoice

When the separate btw-id letter arrives (photographed, or forwarded as an image),
reading the number is the small half of the job.

1. **Read and archive the letter** — `Uw btw-identificatienummer (btw-id)`,
   usually `Pagina 1 van 2`; expect a second page of obligations.
2. **Check the number in VIES before it goes on any invoice**:
   `python3 scripts/vies_check.py NL123456789B01` (endpoint
   `https://ec.europa.eu/taxation_customs/vies/rest-api/ms/{CC}/vat/{number}`).
   `isValid: true` proves the registration is live, and the returned `name` is
   the **handelsnaam registered with the Belastingdienst** — the only cheap way
   to catch a letterhead that does not match what is registered.
3. **Archive the VIES output with every 0%-btw intracommunautaire levering.** The
   `requestDate` of the check on the invoice date is the evidence for the zero
   rate; without it a later inspection can tax the supply.
4. **Deliver a filled invoice template, not advice.** Mandatory fields:
   `references/zzp-checklist-nl.md` §3; generate the .docx with
   `scripts/make_factuur_template.py`, run with the agent venv python
   (python-docx is installed there; the system python3 has no third-party
   libraries). Leave only genuinely unknown values as `[placeholders]` — the
   KVK-nummer and IBAN are the usual two — and ask for exactly those.
5. **If the letter never comes or is lost**, the numbers are readable in Mijn
   Belastingdienst Zakelijk (DigiD) → `Btw` → `Btw-identificatienummer`; failing
   that, the BelastingTelefoon for ondernemers (take the current number from
   belastingdienst.nl → Contact) quoting the ob-nummer or the kenmerk from the
   vaststelling letter. Do not send the user hunting for a form — there is none.

## A supplier charged btw: reclaim, reverse charge, or nothing to do

"I entered my btw-id at checkout but the invoice still carries btw" is decided
by **one fact: the supplier's legal entity and country** — not by anything in
the checkout flow, and not by what the supplier's own help page says.

1. **Resolve the supplier's entity before answering.** Check the trading name
   against a company register (KVK number, registered address, VAT number): a
   foreign-sounding brand often sells through a Dutch B.V., and that flips the
   answer. For an EU VAT number, `scripts/vies_check.py <VAT>` returns
   `isValid`, the registered name and the address, and the `NL`/`DE`/… prefix
   names the country whose btw it is. Completion: you can state the supplier's
   country and its VAT number.
2. **Dutch supplier → the btw is correct and cannot be avoided.** A supplier
   established in the Netherlands charges Dutch btw on a sale to a
   Netherlands-established customer, and entering a btw-id does **not** remove
   it: the 0% / reverse-charge route (btw verlegd) exists only for cross-border
   EU B2B. Do not send the user to argue with support for a refund. The money
   returns as **voorbelasting**, deducted in rubriek 5b of the btw return; with
   little or no turnover the return comes out negative and the Belastingdienst
   pays the balance into the bank account. That payout — not a supplier credit
   note — is the refund mechanism.
3. **Non-Dutch EU supplier → a btw charge is a mistake.** The invoice should be
   0% with a reverse-charge clause (art. 196 BTW-richtlijn / "btw verlegd") plus
   the user's own btw-id. Ask for a corrected invoice first; if the foreign VAT
   was really paid and they refuse, claim it from that country through the Dutch
   Belastingdienst (route, deadline and thresholds:
   `references/zzp-checklist-nl.md` §4).
4. **Non-EU supplier → there is no EU btw to reclaim.** Any tax on the invoice
   is a foreign tax, not deductible and not recoverable through the EU route;
   the service is instead self-assessed as verlegde btw in the Dutch return.
5. **Check three conditions before promising money back:** the invoice must be
   addressed to the business and carry **the user's btw-id** (have it reissued
   if not — an invoice without it weakens the deduction), the purchase must
   serve belaste (taxed) turnover, and the user must **not** be in the KOR — KOR
   participation forfeits input-btw deduction entirely and turns that btw into a
   real cost.
6. **Never let the vendor's own help page decide this.** "Provide us your VAT
   number to avoid VAT charges" is written for customers outside the supplier's
   country and says nothing about a same-country B2B buyer. Cite the tax
   authority for the rule and the vendor only for what it actually charged.

## Pitfalls

- **btw-id and omzetbelastingnummer are not interchangeable.** btw-id (NL…B01)
  goes to customers, on invoices, letterhead and website; the ob-nummer is only
  for contact with the Belastingdienst, contains the BSN, and must never appear
  on an invoice or a website.
- **Belastingdienst letters are the trigger, not an application, and a zzp'er
  gets two of them.** KVK passes the registration on; the btw-id and the
  ob-nummer arrive **separately** by post (≤10 working days, one letter each —
  the vaststelling letter itself confirms the btw-id comes "in een aparte
  brief"). Tell the user to wait for and keep both, plus the yearly
  aangiftebrief (periods, deadlines, betalingskenmerken), instead of hunting for
  a form to submit. Treating it as one letter makes them stop watching the post
  for the btw-id, which is the number invoices may not go out without.
- **The urencriterium is lost silently.** 1,225 hours/year must be recorded from
  day one, or zelfstandigenaftrek and startersaftrek are gone for that year —
  flag hour-tracking whenever a starter asks what to do next.
- **Advisor blogs mix tax years on one page.** A current-year-dated guide quoting
  last year's zelfstandigenaftrek is the single most likely wrong-answer source
  here. Only the Belastingdienst's own `.../veranderingen-inkomstenbelasting-<jaar>/`
  subtree settles the figure for that year.
- **URL guessing mostly fails, and there is no sitemap to fall back on.**
  Slugs are inconsistent inside one parent: `.../ondernemers/ziektekostenverzekering`
  resolves while `.../urencriterium` and
  `.../arbeidsongeschiktheidsverzekering` do not — the real AOV page is
  `.../arbeidsongeschiktheidsverzekering-voor-ondernemers`. A wrong guess returns
  HTTP 404 (not a 200 shell), so read the status line before concluding a page
  was removed.
- **403 is host-specific and the hosts want opposite things, so never conclude
  "gated" from a single 403.** belastingdienst.nl, kvk.nl and business.gov.nl
  403 clients that do not look like a browser; denhaag.nl 403s *any* spoofed
  browser UA and accepts curl/python/wget/empty. The fetch script prints which UA
  profile worked. A JS-only page (`mijnzakelijk.belastingdienst.nl`) returns 200
  with no prose — that is a page-source limit, not a fetch failure; say so
  instead of paraphrasing chrome. Full host table: `references/source-map.md`.
- **Keyless `web_search` backends fail intermittently** (`Keyless Firecrawl
  search failed: 403`, `Unrecognized MCP response shape`). Reissue reworded and
  always fire 2-4 independent searches per round so one dead backend cannot
  block the batch.
- **A bill passed by both chambers is not yet in force, and no effective date may
  be stated from memory.** Check the inwerkingtreding (usually set by KB) before
  telling the user a rule applies; describe it as published-but-not-effective and
  give the expected date. The €38/hour rechtsvermoeden and the mandatory AOV both
  changed shape recently, so re-check the wetstraject (Tweede/Eerste Kamer,
  Staatsblad) instead of repeating a dated advisor summary.
- **Compulsory disability insurance for the self-employed is not in force.** The
  public AOV (Wet BAZ) is a bill; do not answer as if insurance is mandatory.
  The actionable half is timing: a qualifying private AOV taken out before the
  peildatum gets the transition right, after it only a stricter opt-out.
- **Separate "you must pay it" from "it is deductible", and keep the Zvw and the
  AOV premium apart.** Health-insurance premiums and the eigen risico are not
  deductible (Belastingdienst, Winst → Ziektekostenverzekering); an AOV premium is
  deductible only for policies paying a periodic benefit, and then in box 1 as
  `uitgaven voor inkomensvoorzieningen` — not as a business expense. Read the
  Belastingdienst page under Winst → Arbeidsongeschiktheidsverzekering rather
  than reasoning from the Zvw rules; getting this backwards is a common (costly)
  error.
- **Voluntary items must be labelled as such**: separate bank account, AOV, AVB,
  algemene voorwaarden, accounting software. An eenmanszaak has no separation
  between business and private assets — say so when liability comes up.

## Verification

- Every money figure matches text printed by a fetch in this session and carries
  its year explicitly ("2026: €1,200"), never a bare number.
- Every factual sentence cites a primary source: belastingdienst.nl, kvk.nl,
  denhaag.nl, business.gov.nl, ondernemersplein.overheid.nl, and for pending law
  eerstekamer.nl / tweedekamer.nl / wetten.overheid.nl. Advisor and insurer pages
  may add context but never carry a number alone.
- Nothing from the inapplicable list (employer premiums, car, childcare,
  ouderenkorting) appears in the answer.
- Any fact you had to assume is labelled as an assumption in the reply, or the
  `clarify` form was used instead of assuming it.

## Reference

- `references/belastingdienst-letters.md` — letter-type catalogue: what each
  Belastingdienst letter says, which page carries the numbers, which clauses are
  boilerplate, and the btw-id / ob-nummer formats.
- `references/zzp-checklist-nl.md` — the verified after-KVK checklist and
  Belastingdienst sequence: KVK stage, btw-id vs ob-nummer, aangiftetijdvak and
  KOR thresholds, invoice and retention rules, voorbelasting, aftrekposten, Zvw,
  insurance status, Den Haag home-business conditions, pending ZZP legislation,
  and the recommended skeleton of the answer. Figures there are labelled by tax
  year — re-verify before quoting.
- `references/source-map.md` — authoritative URL map (stable pages, year-scoped
  pages, law-in-motion trackers), the fetch ladder, per-host UA behaviour and the
  traps seen in the wild. Start here when a fetch misbehaves.
- `scripts/nl_source_fetch.py` — rung 1 fetch: plain HTTP with a per-host
  User-Agent profile, clean text, optional same-host link discovery.
- `scripts/firefox_fetch.py` — rung 2 fetch: real headless Firefox through
  geckodriver (hand-rolled WebDriver, no selenium), for 403/429 or JS-only pages.
- `scripts/vies_check.py` — VIES lookup for any EU VAT number (the user's own, or
  a supplier's, to identify whose btw an invoice charged), stdlib only; prints the
  registered handelsnaam, address and a dated evidence line.
- `scripts/make_factuur_template.py` — generates the invoice .docx with all
  mandatory fields present as `[placeholders]` (python-docx, agent venv python).

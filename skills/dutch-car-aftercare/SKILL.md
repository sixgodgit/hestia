---
name: dutch-car-aftercare
description: "Dutch car aftercare — warranty escalation when a dealer stops answering, checking an insurance policy line by line, and what the speed limits and camera enforcement actually are."
version: 1.0.0
author: sixgod
license: CC BY-NC 4.0
metadata:
  hermes:
    tags: [netherlands, car, warranty, dealer, consumer-rights, escalation, insurance, speed-limits, enforcement, trajectcontrole]
    category: productivity
    related_skills: [netherlands-vehicle-admin, geely-starray-em-i, dutch-official-documents]
---

# NL car aftercare — warranty, insurance, and the road

Starts where `netherlands-vehicle-admin` stops: the car is bought and registered, and now something
is wrong — a dealer has gone quiet, an insurance policy arrived with numbers you cannot check, or
you need to know what the cameras actually measure.

Vehicle identity, RDW data, plates, taxes and import live in `netherlands-vehicle-admin`. Connected
services (the three links a remote-control feature needs) live in its
`references/connected-services-and-apps.md`.

## Rule 0 — a dealer who does not answer is never a dead end

Manufacturer warranty (`garantie`) and the service network are **brand-level, not shop-level**. Any
authorised dealer can pull the vehicle's data, warranty status and service history from the VIN or
the plate. So "my dealer doesn't reply" is a routing problem, not a dead end — go to another
authorised dealer.

Two consequences that decide most cases:

- **Parallel-imported cars.** When you approach a dealer that did not sell you the car, say so
  plainly, together with the VIN, the plate, who the registered keeper is, and that you are the sole
  driver. Hiding the purchase channel is what gets a request bounced; disclosing it usually gets it
  accepted, because the dealer can then route it correctly. Close with "if you cannot handle this,
  please tell me who can."
- **Check the contract before you argue.** A function that was promised in the contract or in the
  marketing material but was never delivered is **non-conformiteit** under Dutch law — a seller's
  failure to perform, independent of which shop you visit. If it was never written down, you can
  argue about it but you will not win; accept it or take the commercial-complaint route.

## Escalation ladder — only advance when the previous step is silent

1. **A different authorised dealer** performs the diagnosis and gives you a **written conclusion**.
   Do not skip this: that written conclusion is the evidence every later step depends on.
2. **The national importer** — most brands have a separate Dutch legal entity. Attach the dealer's
   written conclusion and set a deadline for a reply.
3. **European / global customer service** — find the address on the brand's own Contact page rather
   than from a search-result snippet. Include VIN, plate, and a factual problem description.
4. **Formal written notice** (`aangetekende brief`) to the original dealer: the problem, the basis
   (contract or marketing material), the demand, and a deadline.
5. **Consumentenbond's Geschillencommissie** or **Juridisch Loket** (free legal advice).

**Send to the brand's customer service and to the nearest dealer in parallel** — whichever answers
first wins. Address the dealer letter to the branch manager.

**Language**: read the existing thread with that recipient first (sent-mail folder) and continue in
the same language. For a Dutch dealer or a Dutch customer-service desk, default to Dutch — do not
switch to English or Chinese because it is easier for you.

### Finding the right contact points

Corporate contact addresses and dealer lists change. Do not hardcode them; look them up at the time:

- Brand's Dutch site → Contact page → customer-service address and phone.
- Brand's European and global sites → separate addresses, often on different domains.
- Dealer locator → filter by city → open each branch card for phone and e-mail.

Some OEM dealer locators are served by a shared multi-brand gateway — a domain that does not match
the brand is not evidence you are on the wrong page.

To pick "the nearest dealer" objectively, geocode the address and compute a driving route rather
than picking a city by feel:

```
# Nominatim → coordinates (User-Agent header required, otherwise 403)
https://nominatim.openstreetmap.org/search?q=<address>&format=json&limit=1
# OSRM → driving distance and duration
https://router.project-osrm.org/route/v1/driving/<lon1>,<lat1>;<lon2>,<lat2>?overview=false
```

Report **kilometres and minutes**, plus the runner-up as a comparison — the user wants the basis for
the judgement, not the verdict alone.

## Insurance: check the policy line by line

When the car is registered to a company (B.V.) the insurance process has extra steps that stall
silently. Work through these in order (full checklist in
`references/nl-car-insurance-and-policies.md`):

1. **Answer the intended-use question in writing the same day.** The insurer (or its acceptance
   department) will ask separately whether the vehicle is used for **bezorgactiviteiten** (delivery)
   — which is normally an exclusion. The wording is usually "we can only proceed once we have your
   confirmation": **not replying means the file is frozen**, not "wait and see".
   → Establish the actual use before answering. **A false answer about use voids the claim** — far
   worse than paying a higher premium. If there genuinely is a delivery use, disclose it and accept
   the cover the insurer requires.
2. **Note the expiry of temporary cover (`voorlopige dekking`).** The confirmation usually says
   "valid 30 days" from the effective date. If no definitive policy has arrived by then, chase it —
   otherwise you are driving uninsured.
3. **Chase the definitive policy / certificate.** A common structure is a broker confirming cover
   and a separate underwriter issuing the certificate, so the two letters can come from different
   domains. If a letter says "you will receive X later" and X has not arrived within a week, ask.

### Once the policy is in hand

Check each of these against RDW where applicable:

- **Vehicle identity** — plate (with or without hyphens is the same car), VIN / `meldcode`, make and
  model must match the RDW registration.
- `cataloguswaarde` — should roughly match RDW's `catalogusprijs`; watch whether VAT is included.
- `dekking` (allrisk / WA+), `eigen risico`, annual mileage band, `schadevrije jaren`.
- `pechhulp` scope and level; territorial cover (NL + Europe).
- Monthly premium build-up, and **policy fees** — usually charged once on inception and once on
  termination. Do not look at the monthly figure alone.

### One admin item that is easy to miss

Official post about the car goes to the registered address. If a dealer ever submitted an RDW
address change on the keeper's behalf, **confirm RDW actually processed it** — a letter saying
"we hope to receive confirmation" is not evidence that anyone followed up.

## On the road: limits and enforcement

When asked whether the Dutch tolerate speeding, separate two things: the **legal threshold** and the
**enforcement density**. What people observe is low density, not a wide threshold.

Four numbers worth knowing (brackets and detail in
`references/nl-speed-limits-and-enforcement.md`):

| Item | Rule |
|---|---|
| Motorway limit | 06:00–19:00 generally **100**; 19:00–06:00 per signage, 120 / 130 |
| OM measurement correction | measured <100 → deduct 3 km/h; ≥100 → deduct **3%** |
| Prosecution floor | must still exceed 4 km/h after correction → ~**108** measured on a 100 road |
| **130-road exception** | the 4 km/h floor is **abolished**; 1 km/h over after correction is fined — the highest-limit roads are the strictest |

- **Trajectcontrole measures average speed over the whole section**; braking before the camera does
  nothing. In place on 11 motorway corridors and 20 N-roads in both directions.
- The Netherlands does **not** use following police cars for speed enforcement — it is fixed and
  mobile cameras plus average-speed sections. That gap is why driver behaviour differs between
  camera points, and crowdsourced apps turned the locations into public knowledge.
- Fines carry roughly €9 in administrative costs on top. Bracket jumps at 10→11 km/h. 50 km/h over
  after correction is an immediate licence withdrawal and a criminal route.
- The 100 limit by day dates from 2020-03, a political decision on nitrogen deposition
  (`stikstof`). Social acceptance is low and enforcement priority has been low, but the number of
  camera sites is **expanding**, not relaxing.

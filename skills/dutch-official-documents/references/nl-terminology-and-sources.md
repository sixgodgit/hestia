# Dutch terminology, sources, and a worked example

## Who publishes what

| Need | Source to read |
| --- | --- |
| Municipal rule behind a permit/declaration (verordening, regeling, uitwerkingsbesluit) | `lokaleregelgeving.overheid.nl` |
| Officially published municipal decisions (besluiten, tarieven) | `zoek.officielebekendmakingen.nl` |
| Which attachments a gemeente currently asks for | the topic page on the gemeente's own site (e.g. `denhaag.nl/nl/parkeren/...`) |
| Company data | KvK uittreksel |
| Vehicle registered keeper | RDW kentekenregister / kentekenbewijs |
| Address registration of a person | BRP (Basisregistratie Personen) — the gemeente can see it; the applicant usually cannot prove it on paper |
| Company/vehicle checks that go into an application | RDW open data and the KvK register — see `skills/netherlands-vehicle-admin/` for the RDW queries and `skills/dutch-business-procedures/` for the KVK forms |

Read the regeling, not only the topic page: the regeling carries the
definitions the case worker applies (who counts as houder, berijder, bewoner).

## Glossary that decides whether a declaration is accepted

| Term | Meaning in these documents |
| --- | --- |
| `houder` / `tenaamgestelde` | registered keeper of the vehicle (on the kentekenbewijs) — may be a company or a lease firm |
| `berijder` | the regular driver, defined in municipal rules as someone who, with the holder's consent, is the vaste bestuurder for longer than a set period (commonly three months) |
| `berijdersverklaring` / `verklaring van de werkgever` | the declaration itself: the vehicle's holder (employer, lease company) states the kenteken, the period, and consent for the driver to use and park the vehicle |
| `kenteken` / `chassisnummer (VIN)` | licence plate / VIN — quote both when known |
| `bewoner` | person registered in the BRP at the address; the applicant, not the company |
| `vergunninggebied` | zone where a permit is needed — outside it the whole exercise is unnecessary (check before drafting) |
| `bijlagen` | attachments list; the letter itself is only one item |
| `ondergetekende`, `namens`, `functie`, `bedrijfsstempel` | signature-block vocabulary: signatory, on behalf of, role, company stamp |
| `KvK-nummer` | Chamber of Commerce registration number of the company |
| `aangetekende brief` | registered mail — the proof that a notice was given, not just its wording |
| `ontbinding` vs `uitschrijving` | the legal end of a partnership vs its removal from the KVK register; both are needed |

## Worked example: Den Haag resident parking permit for a company/lease car

- The applicant is the person registered in the BRP at the address (max three
  resident permits per address) and must be houder **or** berijder of the car.
- Company car: a declaration by the employer is required, stating that the car
  is needed for the work for at least three months, plus the kenteken and the
  period during which the car will be driven. The permit is bound to person +
  kenteken + address.
- Lease car: a lease contract in the applicant's name, plus — if the kenteken
  is in the lease company's name — a declaration between lease company and
  employer.
- Own parking space that cannot be used: a declaration from the manager (not
  needed for some large operators).
- Fees, form versions, and the re-application cycle change; verify on
  `denhaag.nl` before submitting. Municipal question line: 14070.
- Where the vehicle is held by a company and the driver is not an employee,
  the declaration can still be drafted as a berijdersverklaring issued by the
  houder, but expect the gemeente to ask for proof of the employment
  relationship — warn the user instead of asserting the employment clause.

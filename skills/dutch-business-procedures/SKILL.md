---
name: dutch-business-procedures
description: Dutch business legal procedures — KVK registration, VOF/BV/maatschap formation and dissolution, partner exit, UBO registration, and Dutch commercial law basics. Use when the user asks about Dutch company formation, partnership disputes, KVK deregistration, or any Netherlands business legal matter.
version: 1.0.0
license: CC BY-NC 4.0
author: sixgod
tags: [netherlands, dutch, kvk, vof, bv, partnership, commercial-law, europe]
---

# Dutch Business Procedures

Covers common Dutch business legal structures and procedures, particularly for small businesses, restaurants, and partnerships.

## Key Dutch Business Structures

| Structure | Dutch name | Legal personality | Liability | Min. partners |
|-----------|-----------|-------------------|-----------|---------------|
| Sole proprietorship | Eenmanszaak | No | Unlimited personal | 1 |
| General partnership | VOF (Vennootschap onder Firma) | No | Joint & several, unlimited | 2 |
| Limited partnership | CV (Commanditaire Vennootschap) | No | Mixed (general + limited) | 2 |
| Private limited company | BV (Besloten Vennootschap) | Yes | Limited to shares | 1 |
| Professional partnership | Maatschap | No | Varies | 2 |

## KVK (Kamer van Koophandel) — Dutch Chamber of Commerce

All Dutch businesses must register with KVK. Key forms:

- **Form 1** — Register eenmanszaak (sole proprietorship)
- **Form 2** — Register VOF/CV/rederij
- **Form 11** — Register/deregister functionarissen (directors/partners) for legal entities
- **Form 15** — Change partnership/legal entity details
- **Form 16** — Change or deregister functionarissen (partners) — **can be done unilaterally via Mijn KVK with DigiD**
- **Form 17** — Report dissolution of VOF/CV/maatschap/rederij — **requires ALL partners' signatures**

### Critical distinction: Form 16 vs Form 17

- **Form 16 (functionaris uitschrijven):** A partner can deregister THEMSELVES unilaterally via Mijn KVK (DigiD login). No other partner's signature needed.
- **Form 17 (ontbinding melden):** Dissolving the VOF itself requires ALL partners to sign, OR a court order (rechtbank judgment).

## VOF Exit Procedures

See `references/vof-exit-procedures.md` for detailed step-by-step.

### Legal basis

- **Art. 7A:1683 BW** — VOF is dissolved by "opzegging" (notice) from one partner to the others. Unilateral, no consent needed.
- **Art. 7A:1686 lid 1 BW** — Other partners can only oppose the opzegging if it violates "redelijkheid en billijkheid" (reasonableness and fairness), e.g. done solely to harm the other partner.
- **Art. 31 WvK** — Dissolution must be reported to KVK.
- **Art. 32 WvK** — After dissolution, assets must be liquidated (vereffening).

### Practical steps for a partner to exit a VOF

1. **Send opzeggingsbrief** (termination notice) via registered mail (aangetekende brief) to all partners
2. **Log into Mijn KVK** with DigiD → deregister self as functionaris/vennoot (Form 16)
3. **Request remaining partner** to sign Form 17 for full dissolution
4. **If remaining partner refuses:** File for court-ordered dissolution (rechtbank ontbinding) based on "gewichtige redenen" (weighty reasons) such as permanently disturbed relationship
5. **Liquidation:** Assets sold/distributed, debts paid, final settlement

### Common misconceptions

- ❌ "Notaris is required for VOF exit" — FALSE. VOF creation and exit do NOT require a notary. Notaris can add evidentiary weight but cannot bypass KVK's cooperative requirements.
- ❌ "I need the other partner's permission to leave" — FALSE. Art. 7A:1683 BW allows unilateral opzegging.
- ✅ "I can remove my name from KVK unilaterally" — TRUE via Mijn KVK/DigiD (Form 16).
- ⚠️ "Removing my name stops all liability" — PARTIALLY. Liability for debts incurred during membership remains. Full protection requires KVK deregistration AND creditor notification.

## UBO Registration

All Dutch entities must register Ultimate Beneficial Owners (UBOs) — persons who ultimately own/control ≥25% of the entity. VOF partners are typically UBOs.

## Key Contacts

- **KVK:** 088 585 2222 | kvk.nl
- **Belastingdienst (Dutch Tax Authority):** 0550-333 0003
- **Mijn KVK:** kvk.nl/mijnkvk (DigiD login required)

## References

- `references/vof-exit-procedures.md` — Detailed VOF exit guide with template letter
- `references/kvk-eenmanszaak-form-fill.md` — **KVK Eenmanszaak 注册表单实填指引**：IT/SaaS 个人业务的荷兰语业务活动描述、SBI-code、客户问答、员工/授权代表选择、商号命名、现场面签、注册后必办事项。

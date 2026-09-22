---
name: dutch-bv-and-dga
description: "Use when a Dutch B.V. pays a private or DGA cost, or when cash retained in a B.V. has to be taken out."
version: 1.0.0
version: 1.0.0
author: sixgod
license: CC BY-NC 4.0
metadata:
  hermes:
    tags: [Netherlands, BV, DGA, rekening-courant, box2, dividendbelasting, excessief-lenen, werkkostenregeling, RDW, correspondentieadres, parallel-import]
    category: research
---

# Dutch B.V. / DGA: who may bear a cost, and how cash leaves the B.V.

Two questions that arrive together whenever a B.V. and its shareholder are the
same household wallet:

1. **The invoice question** — may the B.V. pay this cost at all, and under what
   title if it is really private? (Part 1, English.)
2. **The cash question** — money has piled up inside the B.V. and has to reach
   the shareholder's private account; which routes exist, at what tax cost, and
   how is the vehicle/RDW side of it handled? (Part 2, 中文.)

Scope boundary: not eenmanszaak/ZZP (`skills/dutch-zzp-ondernemer/` — an
eenmanszaak has no such boundary). A disputed energy bill itself is handled in
`skills/dutch-energy-bill-disputes/`.

---

# Part 1 — Dutch B.V./DGA: who may bear a cost

The boundary between a B.V. (including a holding) and private life: an invoice
addressed to the DGA or his family, a house used by the company or by its
workers, holding-versus-werkmaatschappij allocation, and what must be documented.

## Output shape (standing user preferences)

- Reply in Simplified Chinese; Dutch terms in parentheses on first use
  (rekening-courant, verkapt dividend, box 2, werkkostenregeling).
- One-line verdict first ("技术上可以付,但…"), then a flat list of short bold
  labels. No nested headings.
- Give the box 2 euro figure at the current year's rate, with the year named.
- Present the options as a numbered A/B/C choice, then close with the single fact
  that decides between them, and offer the paperwork (loan/RC agreement,
  use-lease agreement, doorbelasting note).
- Cite official pages (Belastingdienst, KVK, gemeente) inline with the
  `Sources:` block from the external `grounded-citations` skill.

## Procedure

1. **Start from the name on the invoice.** The party named is the debtor; the
   B.V. paying does not move the debt, the contract or the liability. Record the
   references (klantnummer, factuurnummer, dossier) before analysing.
2. **Find the real user of what was paid for.** The B.V. may book it as its own
   cost only if that B.V. (or its group) actually uses the good, energy or
   property. If the benefit belongs to a werkmaatschappij, the holding recharges
   (doorbelasten) or books a receivable — a holding that merely holds shares
   cannot deduct another entity's cost.
3. **If it is not a business cost, choose the title — always the same three:**
   - **A rekening-courant / loan to the DGA.** Businesslike conditions: written
     agreement, agreed market interest, real repayment, adequate security, and
     the B.V. must stay able to meet its obligations. A balance within €17,500
     during the whole year needs no interest calculation; once it exceeds that,
     interest is calculated over the entire balance for the year. Repay within
     the year or it is not a loan.
   - **B verkapt dividend.** No title at all → a distribution to the
     shareholder: box 2 at the current rate (2026: 24.5% up to €68,843, 31%
     above) and not deductible for the B.V.
   - **C wage.** Possible, usually the most expensive (progressive box 1 rate
     plus employer charges).
4. **Sort the btw separately from the Vpb.** Only the part genuinely used for
   the taxed business is deductible. Energy on a residential connection in a
   private name is not the B.V.'s input tax, and a partly private asset needs a
   private-use correction of both cost and btw.
5. **Housing someone: add the wage-tax layer.** Free or cheap housing for an
   employee is loon in natura, valued at the market rent (a dienstwoning is
   capped at 18% of the annual wage). Art. 31 lid 4 sub b Wet LB forbids
   designating "vergoedingen en verstrekkingen ter zake of in de vorm van een
   woning" as eindheffingsbestanddeel, so it generally cannot ride the WKR vrije
   ruimte — it lands in the employee's individual wage. If the occupants are not
   the company's own employees (uitzendbureau, subcontractor), the company has no
   business reason to pay at all.
   Where there is no lease and no housing agreement at all, the payment is doubly
   ambiguous — the same euro reads as the occupants' loon in natura or as a
   benefit to the shareholder — so the first deliverable is the facts (whose
   house, whose employees, is it the owner's hoofdverblijf) and a past/future
   split, not a title.
6. **Property: private versus B.V.-owned decides almost everything.**
   - **Private (DGA/family) property:** the B.V. paying is a benefit to the
     shareholder → route A, B or C, and never the B.V.'s deduction. Regularising
     it means a use/lease agreement plus a market rent to the owner — but price
     the tax cost first: an eigen woning must be the owner's (or his household's)
     hoofdverblijf held on the basis of ownership (art. 3.111 lid 1 Wet IB); once
     the house, or a part of it, serves others, that part leaves box 1, the
     mortgage-interest deduction goes with it, and partial letting can count as a
     partial disposal for the bijleenregeling. Only the kamerverhuurvrijstelling
     (long-term letting of part of your own home, not a self-contained dwelling,
     both parties registered at the address, income under the annual cap)
     preserves eigenwoning status — worker housing normally fails those
     conditions.
   - **B.V.-owned property:** energy and upkeep are the B.V.'s own costs —
     deductible and btw-reclaimable. The risk inverts: if the DGA or his family
     uses it, the B.V. must charge a market rent, otherwise the shortfall is a
     distribution.
   - **Identical in both cases:** the wage-tax layer of step 5, the municipal
     housing rules (Den Haag kamerbewoning: omzettingsvergunning, max 8 residents,
     ≥18 m² per person, only the owner may apply, only in listed districts), and
     the fact that company-paid utility bills are documentary evidence that the
     company uses the address. Since 1 July 2023 the Wet goed verhuurderschap adds
     general duties for every verhuurder (a written lease) and, when letting to
     arbeidsmigranten, a lease drawn up separately from the employment contract
     plus a municipal verhuurvergunning where the gemeente has introduced one.
7. **Close by computing the chosen route on the amount that will actually be
   paid** — after any verjaring or dispute reduces it — and offer the paperwork:
   RC/loan agreement, use-lease agreement, doorbelasting note, or the letter to
   the creditor.

## Pitfalls

- **Booking a private cost straight to "kosten" is the worst option:** not
  deductible, and easily reclassified as a distribution. Either the entity uses
  it, or it needs a title.
- **Do not propose "just let the house to the B.V." to legitimise a payment**
  before pricing the loss of the eigenwoningregeling — the fix can cost more than
  the bill.
- **€17,500 is not a dividend threshold.** It is the interest-free band for a
  DGA's rekening-courant; the excessief-lenen fiction starts at €500,000 (2026),
  and debts of blood/line relatives count toward it.
- **A holding is not automatically the employer or the user.** Recharge costs
  that benefit the werkmaatschappij rather than deducting them where they arise.
- **Decide the title in the same bookkeeping period.** A B.V. bank payment for an
  invoice addressed to a private person is a documented benefit; leaving it
  undecided until year end is what turns a loan into a dividend.
- **Say plainly that the choice needs the boekhouder's sign-off** before the
  entry is made — the answer is advice, not a filing.
- **Do not retro-fit a lease over years that had no arrangement.** A lease signed
  now does not change what those years were, and it turns the past into taxed
  rental income for the owner; settle the past on its own terms (the owner pays
  it, or the company advances it under a loan) and regularise only from the
  agreement's start date onwards.

---

# Part 2 — 荷兰 B.V. 滞留现金的合规取出与车辆归属

半年/年末盘账时，B.V. 账上现金堆积、个人账户缺钱，需要一条可解释的资金路径。
本节把可选路径、税务后果、车辆与 RDW 的连带问题放在一起判断。

## 基础参数与口径

- **Vpb（公司税）**：19%–25.8% 区间。
- **股息税（dividendbelasting）**：来源表述为 15%（上游来源此处写作「Anbi」，
  按原文保留用词）。注意这与 Part 1 的 box 2 是两个层面：Part 1 给的是股东个人
  层面的 box 2 税率（2026: €68,843 以内 24.5%，超过部分 31%），公司分配时又要
  考虑预提这一层。**两处数字不要混算**——到底哪一层实缴、能否抵扣，必须先问
  boekhouder/belastingadviseur。
- **excessief lenen 门槛的口径冲突**：上游的中文来源写的是「€700k（2025 年规则）」，
  英文来源（更新、更具体）写的是 **€500,000（2026）**。判断时按 **€500,000** 用，
  并且记住血亲/直系亲属名下的债务也算进这个额度。超过部分视为分红征税。
- 目的：在不越过红线的前提下让现金到达个人账户，并让每一步都留下可解释的文件。

## 路径目录（看速度 / 限额 / 税务三列）

### ① B.V. 购买个人名下资产（最快）
- B.V. 回购你个人名下的资产：车、表、艺术品、古董、高端电子产品等。
- 价格对标市场价（可略高，但不能高到税务局会质疑的程度）；单价过高需第三方
  估值报告。
- 税务处理：个人侧在 box 3（财富税）申报，约年化 1.2%–2%（相对低）。
- 速度：T+1。限额：不限（受估值约束）。
- 常见金额区间：€5 万–€20 万。

### ② 股东借款（最经典）
- B.V. 以借款形式把钱转到个人。
- **门槛口径见上**：按 €500,000（2026）判断，超过部分视为分红；低于门槛不等于
  免息无成本，仍要看 Part 1 的 rekening-courant 条件。
- Part 1 口径的硬条件必须满足：书面协议、约定市场利率、**真实还款**、足够担保，
  且 B.V. 自己仍能履行义务。€17,500 以内的余额全年免算利息；超过则**全年余额**
  都要算利息。
- 速度：T+1。税务处理：借款本身不是收入；box 3 中可作为负债申报。
- 上游来源提到「公司清算时应收账款转坏账损失」作为退出方式 —— 这与「真实还款」
  要求直接冲突，把它当备用叙述而不是默认方案；不做实质还款的借款很容易被重新
  定性为隐性分红。

### ③ 顾问费 / 授权费合同
- 你本人或亲属与 B.V. 签管理咨询、品牌授权类合同，按月分期支付。
- 个人侧按 box 1 申报（最高 49.5%）；现金流节奏优于一次性分红。
- 必须配合真实痕迹：邮件、报告、会议记录、交付物。

### ④ 艺术品 / 收藏品投资
- B.V. 购入艺术品、葡萄酒、珠宝等，个人以「借展」形式使用。
- 资产在 B.V. 账上折旧或持有增值；实物到手快（T+1），但流动性差，紧急时走典当行。

### ⑤ 年金保险产品
- B.V. 趸缴购买卢森堡/爱尔兰保险公司的年金产品，个人为受益人，以保单贷款形式
  提取大部分（来源举例 90%+）。
- 速度：T+7 至 T+30。来源口径：保单贷款不算应税收入。

### ⑥ B.V. 卖车给你个人（变现 + 解决车辆归属）
B.V. 以市场价把公司名下车辆卖给个人：
- 车从 B.V. 名下转到个人名下 → 所有 RDW 信件自然寄到个人住址；
- B.V. 收回车款 → 直接缓解「holding 钱出不来」；
- 个人成为车主后，保险、APK、罚单都走个人地址；
- 车款来源可以就是方案 ②（先向 B.V. 借，再付回去）。
- 税务影响：个人侧车辆价值计入 box 3；B.V. 侧卖价高于账面价值时产生 Vpb 应税利润。
- 适用场景：B.V. 名下有车 + 需要现金 + 不想再处理 RDW 通讯地址。

### ⑦ 组合配置（示例）
组合的意义是让每一笔都有独立、可解释的名义，而不是把所有钱挤进一条路径。
下面是一份金额示例（按需等比缩放）：

| 方式 | 示例金额 | 速度 | 税务 |
|------|------|------|------|
| B.V. 回购个人资产（车/表/艺术品） | €15 万 | T+1 | box 3 |
| 股东借款（低于 excessief-lenen 门槛） | €25 万 | T+1 | 借款本身不征税，box 3 负债 |
| **合计** | **€40 万** | **约 1 周** | **主要为 box 3** |

## B.V. 名下车辆管理与 RDW 通讯地址

### 问题
B.V. 名下车所有 RDW 信件（车税、APK、罚款、召回）默认寄到 B.V. 注册地址。
共享办公/虚拟办公室地址可能无人签收 → 滞纳金叠加。

### 方案对比

| 方案 | 成本 | 效果 |
|------|------|------|
| RDW Correspondentieadres | 免费 | RDW 信件转寄到个人住址；对公司不过期 |
| PostNL 邮件转寄（Doorsturen） | €30–50/年 | 所有信件都转（兜底） |
| DigiD Machtigen | 免费 | 电子化信件，无需纸质 |
| B.V. 卖车给你个人 | 过户费 | 一劳永逸 + 变现 |

**推荐组合**：RDW 通讯地址 + PostNL 转寄（双重保险）。

### 申请要点（完整流程见 `references/rdw-correspondence-address.md`）
1. 写一封**签字信**：请求设置/更改/取消通讯地址、荷兰境内地址、**详细解释为什么
   不能寄到注册地址**（如：B.V. 注册地址是共享办公地址，无人签收车辆信件，车辆
   实际由个人使用和保管）、KVK 号码 + vestigingsnummer、授权签字人的 BSN/全名/
   出生日期（无 BSN 则附有效身份证明复印件）。
2. 登录 RDW 门户 `https://www.rdw.nl/correspondentieadres` 上传签字信和文件。
3. RDW 5 个工作日内批复（是否批准由 RDW 决定，不是自动的）。
4. 通过后，该主体名下**所有车辆**的 RDW 信件都寄到通讯地址；只要 KVK 有效，
   对公司**不过期**，该地址不与其他机构共享。

### 边界（容易踩坑）
- RDW 通讯地址**只影响 RDW 发出的信**；Belastingdienst 的信仍寄 B.V. 注册地址，
  要转税务局信件得单独在 Belastingdienst 改地址。
- 罚款信（boete）默认寄车主注册地址，设置通讯地址后 RDW 会转；但**市政停车罚单**
  可能走不同系统 → 建议同时开 PostNL 转寄兜底。
- 保险信按投保时填的地址走，与 RDW 通讯地址无关。
- **预防性方案**：还没买车时，不做买断，改做 financial lease / operational lease —
  车登记在租赁公司名下，个人是**指定驾驶员**，信件由租赁公司电子化转发；B.V. 月付
  租金可抵税，车不进 B.V. 资产负债表。

## 平行进口与交易对手背景调查

### 荷兰公司研究技术（免费 → 付费）
1. **免费**：Drimble.nl 查注册地址/关联公司
2. **免费**：Faillissementen.com 查破产记录
3. **免费**：Panjiva 查进出口记录
4. **付费**：Creditsafe / Company.info 查董事/信用/财报
5. **官方**：KVK Handelsregister 买 uittreksel（€2–5）

**关键**：发票上的商号 ≠ KVK 注册名。必须用 KVK 号码确认法律主体。

### 平行进口车商评估要点
- 查 KVK 背景（经营年限、破产记录）。
- 确认是否带 fabrieksgarantie（原厂保修）。
- 对比官方 dealer 价格：差价 €2,000–8,000 属正常区间（部分渠道差价可达 €3k–5k）。
- 常见模式：独立进口商批量从中国采购 → 以公司名义注册 → 零售给个人。
- **但**：部分品牌官方可能不承认非授权渠道的保修，需在合同中明确写清。
- 确认售后网络（能否在任意授权服务中心维修）。
- 保留所有购车文件。

## 输出偏好与风险提示

- **格式**：结构化表格优先，给出「方式 / 金额 / 速度 / 税务」四列对比；先给可执行
  方案，风险提示集中放在末尾。
- **语言**：中文为主，关键荷兰语术语保留原文（Correspondentieadres、
  wet excessief lenen、rekening-courant、verkapt dividend）。
- 这些路径处在「合规边缘」，不是逃税建议。税务局若认定借款没有真实还款意图，
  可重新定性为隐性分红 → 追缴股息税 + 罚款。
- 必须配套：借款协议 + 象征性或实质还款记录 + 资产交易凭证 + 真实的顾问痕迹。
- 结论落到纸面前，先让荷兰税务顾问（belastingadviseur）或 boekhouder 过一遍；
  一笔咨询费通常远低于一次重新定性的代价。

## 参考法律
- Wet excessief lenen：自然人与 B.V. 之间的贷款超过门槛的部分视为分红（门槛口径
  见上文 §基础参数与口径）。
- Wet goed verhuurderschap（2023-07-01 起）：对 verhuurder 的一般义务，出租给
  arbeidsmigranten 时的额外要求（见 Part 1 步骤 6）。

## 参考文件

- `references/rdw-correspondence-address.md` — B.V. 名下车辆 RDW 通讯地址设置完整
  流程与备选方案。

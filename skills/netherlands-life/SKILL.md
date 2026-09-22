---
name: netherlands-life
description: "在荷兰生活的百科全书入口 — 从移民与身份、银行、医保、住房、交通到日常与荷兰语词汇。"
version: 1.0.0
version: 1.0.0
author: sixgod
license: CC BY-NC 4.0
metadata:
  hermes:
    tags: [netherlands, dutch, living, immigration, ind, digid, banking, healthcare, housing, transport]
    category: research
---

# 🇳🇱 在荷兰生活百科全书

面向在荷兰长期居住的华人居民的综合参考指南。

---

## 一、税务（Belastingdienst）

税务在这个仓库里被拆成互相独立的技能，避免同一个数字在多处各写一份、彼此矛盾：

- **自雇/ZZP 的日常义务**（btw-id 与 omzetbelastingnummer 的区别、发票规则、KOR、urencriterium、税局来信怎么处理）→ `skills/dutch-zzp-ondernemer/`
- **开公司与公司形式选择**（KVK 注册、eenmanszaak / VOF / BV、表格填写）→ `skills/dutch-business-procedures/`
- **B.V. 与 DGA 的税务处理、公司现金如何合规取出** → `skills/dutch-bv-and-dga/`
- **家庭补贴（toeslagen）怎么算** → `skills/dutch-toeslagen-and-benefits/`
- **年度税制与预算变化怎么读、对个人有什么影响** → `skills/dutch-tax-and-budget-changes/`

### 最小概念表（只保留不会逐年过期的东西）

| 术语 | 荷兰语 | 说明 |
|------|--------|------|
| 税号 | BSN | 所有税务/医疗/银行的基础，只用于和政府机构打交道 |
| 所得税 | Inkomstenbelasting (IB) | 工资与自雇所得 |
| 增值税 | BTW | 一般 21%，低档 9% |
| 津贴 | Toeslagen | 房租/医保/托儿/儿童津贴，必须自己申请 |

**Box 划分**：Box 1 工资与自雇所得；Box 2 大股东（持股 ≥5%）的股息与资本利得；Box 3 储蓄与投资——按**虚拟收益率**征税而不是按真实收益，且只看每年 1 月 1 日的资产净值。

**报税时间线**：1–4 月收到预填报税表，4–5 月报税窗口开放，提交后核对多退少补。

**关键网站**：Mijn Belastingdienst（belastingdienst.nl，DigiD 登录）、toeslagen.nl。

> ⚠ **数字时效**：荷兰的税率、档位、各类收入阈值每年随 Prinsjesdag / Belastingplan 调整。本仓库刻意**不**复制容易过期的具体金额——要具体数字就查官方页面，或走上面列出的对应技能。

---

## 二、移民与身份（IND / Gemeente）

### 核心机构
| 机构 | 职责 |
|------|------|
| IND | 签证、居留许可、入籍 |
| Gemeente | 户籍登记（BRP）、身份证 |

### 居留类型
| 类型 | 说明 |
|------|------|
| MVV | 临时居留签证，入境前申请 |
| VVR | 居留许可，入境后领取 |
| 无限期居留 | 满5年+荷兰语A2+融入考试 |
| 入籍 | 满5年+融入考试+放弃原国籍 |

### 新来荷兰步骤
1. 入境后 5 天内到 Gemeente 登记 BRP
2. 拿到 BSN 号码
3. 用 BSN 开银行账户、签医保
4. 申请 DigiD：digid.nl
5. 申请津贴

### 融入考试（Inburgeringsexamen）
- 荷兰语听说读写 + 社会知识（KNM）
- 最低 A2，B1 可申请无限期居留
- 费用约 €350

### DigiD
- 登录所有政府网站的数字身份证
- BSN + 荷兰地址申请，激活码邮寄到家

---

## 三、银行与金融

### 荷兰主要银行
| 银行 | 特点 |
|------|------|
| ING | 最大，App 好用 |
| ABN AMRO | 大型综合银行 |
| Rabobank | 合作制银行 |
| Bunq | 数字银行，多币种 |
| Revolut / Wise | 国际转账优选 |

### 开户要求
- BSN、有效护照、荷兰地址证明

### 荷兰支付特点
- **iDEAL**：最主流在线支付
- **Tikkie**：即时转账请求
- **SEPA 转账**：欧元区次日到账
- **Incasso**：固定扣款授权
- 荷兰以 **借记卡（PIN）** 为主，Maestro/V Pay 是主流

---

## 四、医疗保险（Zorgverzekering）

### 核心规则
- **强制参保**：每年1月1日前买好
- **基本险**：政府规定，覆盖基本医疗
- **自付额（Eigen risico）**：€385/年（参考）

### 常用保险
| 公司 | 特点 |
|------|------|
| CZ | 覆盖广，口碑好 |
| Zilveren Kruis | 最大，网络广 |
| FBTO | 数字优先，便宜 |

### 就医流程
1. 先去 **家庭医生（Huisarts）**
2. GP 转诊到专科
3. 急诊直接去医院

---

## 五、住房

### 租房 vs 买房
| | 租房 | 买房 |
|---|------|------|
| 门槛 | 押金+身份 | 贷款（收入4-4.5倍） |
| 税务 | 可申请 Huurtoeslag | 房贷利息可抵税 |
| 权利 | 租户保护强 | 自由处置 |

### 找房渠道
| 平台 | 说明 |
|------|------|
| Funda.nl | 最大房产网站 |
| Pararius.nl | 租房平台 |
| Kamernet.nl | 合租/单间 |
| Woningnet | 社会住房排队 |

### 社会住房
- 租金 < €880 可申请排队
- 阿姆斯特丹排队 10+ 年

---

## 六、交通

### 公共交通
| 系统 | 说明 |
|------|------|
| NS | 国家铁路 |
| GVB | 阿姆斯特丹本地交通 |
| OV-chipkaart | 公交卡 |

### 骑行
- 荷兰是自行车王国
- 必须有前灯（白）、后灯（红）、反光板
- 自行车被盗常见，锁好

### 开车
- 中国驾照 + IDP 可用 185 天
- 之后需换荷兰驾照（理论+路考）

---

## 七、日常生活

### 超市
| 超市 | 定位 |
|------|------|
| Albert Heijn | 最常见，中高端 |
| Jumbo | 性价比好 |
| Lidl / Aldi | 折扣超市 |
| 中超 | 中国食材 |

### 通讯
| 运营商 | 特点 |
|------|------|
| KPN | 老牌，覆盖广 |
| T-Mobile | 性价比好 |
| Simyo / Ben | MVNO，更便宜 |

### 消费者权益
- 网购 14 天无理由退货
- 至少 6 个月法律保修

---

## 八、关键荷兰语词汇

| 中文 | 荷兰语 |
|------|--------|
| 市政厅 | Gemeente |
| 家庭医生 | Huisarts |
| 药店 | Apotheek |
| 税务局 | Belastingdienst |
| 居留许可 | Verblijfsvergunning |
| 银行卡 | PIN-pas |
| 公交卡 | OV-chipkaart |

---

## 九、紧急联系

| 机构 | 电话 | 网站 |
|------|------|------|
| 紧急电话 | 112 | 报警/消防/急救 |
| Belastingdienst | 0800-0543 | belastingdienst.nl |
| IND | 088 043 04 30 | ind.nl |
| KVK | 088 585 22 22 | kvk.nl |
| DigiD | 088-123 65 00 | digid.nl |

---

## 十、注册个体户（Eenmanszaak）

完整的 KVK 注册流程、表格逐项填法、商号命名规则和 VOF 退出程序写在 `skills/dutch-business-procedures/`；注册**之后**的日常税务义务（btw-id、发票、KOR、urencriterium）写在 `skills/dutch-zzp-ondernemer/`。

这里只留最容易踩的四条：

- 通常要预约：先线上填表，再预约 KVK 柜台面签（少数情况可纯线上完成）。面签带有效证件原件 + 已激活的 DigiD（BSN 含在其中）。
- 一人只能有一家 eenmanszaak（可以挂多个商号/业务活动）。
- 注册地址默认是**私人地址且公开**；介意隐私就租商业地址。
- 注册后必须办三件事：向 Belastingdienst 报到（btw-id 与 omzetbelastingnummer 会**分两封信**寄到，约 10 个工作日）、买责任险（视行业而定）、建账本。领救济金的人要先与 UWV / 市政府报备。

> 一次性注册费随年份调整（2026 年为 €85.15，可抵税）；以 kvk.nl 当期公布为准。

**软件/订阅类业务的 BTW 要点**：数字服务出口到欧盟外通常 0%，欧盟内 B2B 反向征收（需要客户的 btw-id），境内 B2C 按 21% 征收；Tikkie / Stripe / Mollie / iDEAL 收款都要求先有 KVK 注册 + 银行账户；订阅制（recurring）收入用 Stripe / Mollie 定期扣款便于记账；开发与服务器成本发票留好做抵扣。

## 使用指南

1. 先判断问题属于哪一类：生活类（本技能）、税务与公司类、车辆与停车类、文书类、能源账单类、汇款类。
2. 本技能负责「在荷兰怎么生活」：身份与居留、银行、医保、住房、交通、日常生活、荷兰语词汇、紧急联系。
3. 专业问题转对应技能：`dutch-zzp-ondernemer`、`dutch-business-procedures`、`dutch-bv-and-dga`、`dutch-tax-and-budget-changes`、`dutch-toeslagen-and-benefits`、`dutch-official-documents`、`dutch-parking`、`netherlands-vehicle-admin`、`dutch-energy-bill-disputes`、`money-transfer-limits-and-fees`、`geely-starray-em-i`、`industrial-maintenance-netherlands`。

## 时效与免责

- 税率、费率、津贴门槛、机构地址与电话号码都会变动；具体数字以 Belastingdienst / KVK / IND / RDW / 市政厅的官方页面为准。
- 金融与法律内容为通用方法与经验参考，不构成税务或法律意见；重大决策请咨询 belastingadviseur / jurist。
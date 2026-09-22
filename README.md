# hestia · 荷兰生活知识库

> Hermes `SKILL.md` 格式的荷兰生活技能合集。**只收通用知识与可复用方法，不收任何个人案例或私人信息。**

面向在荷兰长期生活的人（尤其是华人居民）：税务与公司、官方文书、车辆与车牌、停车、补贴、能源账单、汇款、以及日常生活的百科入口。

## 技能清单

| 技能目录 | 主题 | 语言 |
|----------|------|------|
| [`netherlands-life`](skills/netherlands-life/) | 生活百科总入口：身份与居留（IND/Gemeente）、银行、医疗保险、住房、交通、日常生活、荷兰语词汇、紧急联系 | 中文 |
| [`dutch-business-procedures`](skills/dutch-business-procedures/) | 公司设立与法律程序：KVK 注册、eenmanszaak / VOF / BV / maatschap 的选择与退出、UBO 登记、商号规则 | 中文 / 英文 |
| [`dutch-zzp-ondernemer`](skills/dutch-zzp-ondernemer/) | ZZP / eenmanszaak 日常义务：btw-id 与 omzetbelastingnummer、发票规则、KOR、urencriterium、税局来信处理 | 英文 |
| [`dutch-bv-and-dga`](skills/dutch-bv-and-dga/) | B.V. 与 DGA：私人成本放在公司里的税务处理、公司现金如何合规取出、车辆归属与 RDW 通讯地址 | 中文 / 英文 |
| [`dutch-tax-and-budget-changes`](skills/dutch-tax-and-budget-changes/) | 年度税制与预算变化（Prinsjesdag / Belastingplan）怎么读、对个人有什么影响 | 英文 |
| [`dutch-toeslagen-and-benefits`](skills/dutch-toeslagen-and-benefits/) | 家庭补贴（huur/zorg/kinderopvang/kindgebonden budget）的资格与金额核算 | 英文 |
| [`dutch-government-briefings`](skills/dutch-government-briefings/) | 荷兰政府与预算新闻摘要（rijksoverheid、Prinsjesdag、Belastingplan），带出处 | 英文 |
| [`dutch-official-documents`](skills/dutch-official-documents/) | 官方文书与声明起草：gemeente 往来、verklaring、双语信件、填表与 PDF 生成校验 | 英文 / 中文 |
| [`netherlands-vehicle-admin`](skills/netherlands-vehicle-admin/) | 车辆行政：RDW 数据、BPM/MRB/bijtelling/WAM、进口登记、车牌 sidecode 解析与校验 | 英文 |
| [`geely-starray-em-i`](skills/geely-starray-em-i/) | Geely Starray EM-i（吉利银河星舰7 EM-i，P145）车型识别、手册与车机系统 | 英文 |
| [`dutch-parking`](skills/dutch-parking/) | 停车：路边计时、停车楼、居民许可（bewonersvergunning）、访客许可、P+R，按海牙/阿姆斯特丹/鹿特丹分组 | 中文 / 英文 |
| [`dutch-energy-bill-disputes`](skills/dutch-energy-bill-disputes/) | 能源与公用事业账单审计与异议：时效（verjaring）、bezwaar、netbeheerder vangnet | 英文 |
| [`money-transfer-limits-and-fees`](skills/money-transfer-limits-and-fees/) | 汇款、外币与银行卡限额/费率（含荷兰银行与 ICS 的差异） | 英文 |
| [`industrial-maintenance-netherlands`](skills/industrial-maintenance-netherlands/) | 机电与制冷：西门子/施耐德等电气元件识别与跨品牌替换、荷兰供应商、故障排查 | 英文 |

## 怎么用

每个技能目录是标准的 Hermes 技能：`SKILL.md` 加可选的 `references/`、`scripts/`。放进 agent 的技能目录即可被自动加载：

```bash
cp -r skills/* ~/.hermes/skills/<category>/
```

引用其他技能时使用仓库内相对路径 `skills/<name>/`。

## 关于本合集

- **来源合并**：本仓库由两套各自维护的荷兰生活技能合并而成（一套英文为主体，一套中文为主体），重叠主题（税务/公司、文书、车辆、停车、BV）已合并去重，同一份信息只保留一处。
- **语言**：技能正文保留各自来源的语言，不做机器翻译——税务与法律内容的精确性优先于语言统一。多数技能以英文为主体，生活百科与几处合并章节保持中文；README 是中文索引。
- **一处例外**：并入英文主导技能的两份中文参考（车牌 sidecode 表、gemeente 邀请函签字流程）被统一改写为英文——信息未删减，只是语言统一了。需要中文版可以再生成。
- **不收个人数据**：发布前做过系统性清理，姓名、住址、车牌、BSN/btw-id/KvK 号、账单号、内网地址与本地路径全部剔除；案例一律改写为通用方法与边界情况。

## 时效与免责

- 税率、费率、津贴门槛、机构地址与电话都会变动；具体数字以 **Belastingdienst / KVK / IND / RDW / 市政厅** 的官方页面为准。
- 金融与法律内容为通用方法与经验参考，**不构成**税务或法律意见；重大决策请咨询 `belastingadviseur` / `jurist`。

## 许可证

**CC BY-NC 4.0** — 可自由使用、修改、再分发，须署名 **sixgod**（[@sixgodgit](https://github.com/sixgodgit)），**禁止商用**。详见 [LICENSE](LICENSE)。

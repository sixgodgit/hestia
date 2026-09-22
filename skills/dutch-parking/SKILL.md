---
name: dutch-parking
description: "Use when parking in a Dutch city, at a beach/dune/lake destination, or when a resident needs a parking permit — choosing between street meters, garages, resident/visitor permits and P+R, pricing the trip for a concrete date, booking the ticket, and checking which permit zone an address is in."
version: 1.0.0
author: sixgod
license: CC BY-NC 4.0
metadata:
  hermes:
    tags: [parking, parkeren, netherlands, den-haag, amsterdam, rotterdam, p+r, vergunning, permits, digital-parking, trip-planning]
    category: productivity
    requires_toolsets: [terminal, web_search, web_extract]
---

# Dutch Parking

Pick ONE parking option for a concrete trip, price it for that actual date, book it, and hand over the on-site steps. The user wants a decision plus the link, not a menu of research.

## Parking types — decide which one this trip needs

停车类型：路边计时（parkeerautomaat）、停车楼/车库（parkeergarage）、许可区（vergunninggebied）、P+R、访客许可（bezoekersvergunning）—— 外加休闲目的地的免费/定额停车场。

| Type | Dutch | When it applies | How it is paid |
|---|---|---|---|
| Metered street (路边计时) | parkeerautomaat, digitale parkeerplaats | short stops; big-city centres are paid 24/7 including Sundays | machine (bank/credit/chip card — chipknip is dead), phone app, or the city's digital loket |
| Garage / car park (停车楼) | parkeergarage, parkeerterrein | whole-day centre trips and deliveries | walk-in hourly rate at the barrier, or a pre-booked dagkaart / avondkaart for the date |
| Permit zone (许可) | vergunninggebied | only where a zone exists; the resident and their visitors | bewonersvergunning (holder) or bezoekersvergunning (visitor hours) |
| P+R | P+R | the car stays put all day and you travel in **and** back by public transport | €6–13 per 24 h, but only with a qualifying return trip — see the P+R mechanics |
| Free / flat-rate lot | gratis parkeren | beach, dune and lake destinations and town edges | nothing, or one flat day card — the decision variables are time limit and season, not a tariff matrix |

## Always-on output rules

- Lead with one recommendation, then the runner-up in a line or two. A small table comparing cost / detour time / failure modes beats prose.
- Every price, time and address must come from a source fetched in this session: the municipality's rate page, the operator's own site, or the booking engine itself. Label anything only found on aggregator or blog pages as unverified.
- Hand over the exact booking URL, HTTP-checked with `curl -s -o /dev/null -w '%{http_code}'`. A marketing homepage is not a booking link — the real order form is usually a cross-origin iframe behind it.
- Reply in Chinese (the user writes Chinese), keeping Dutch on-screen terms in Dutch: Dagkaart, Avondkaart, Kenteken, landcode, doorrijhoogte.
- End with the on-site sequence (unload -> park -> ... -> exit before the card expires) and the address to put in navigation, not with a recap of the research.

## Decision ladder

1. **P+R** — cheapest (EUR 6/24 h at weekends and on weekdays after 10:00; EUR 13 before 10:00), but only if you travel in AND back by public transport on an OV-chipkaart or paper GVB ticket and do not need the car meanwhile.
2. **Garage with a day/evening card booked online** — the workhorse for centre trips; EUR 10-30/day against EUR 5.37-8.05/h on the street.
3. **Street parking** — short stops outside the centre only; the centre is 24/7 paid including Sundays and enforcement is by scan car.
4. **Park outside the paid zone and walk/metro** — niche; confirm the zone on the municipality's own map first.

Sequence that matters for deliveries: unload at the shop FIRST (designated loading bay; never a pedestrian street), then drive to the garage. Day cards are one-entry/one-exit, so never park before unloading.

## Tariffs, hours and seasons — how to treat every number in this skill

**费率按年变动，以市政官网为准** ("Tariffs change per year — the municipality's own site is authoritative.") Every rate, hour and cap here is a **baseline to re-check, not standing truth**: municipality tariffs are re-set each January and pre-booked garage cards move more often. Where two sources disagree the more **specific** and more **recently dated** figure is kept below and its year is named. Always quote the rate for the date at hand off the municipality's or operator's own page (or the booking step), never an advertised "vanaf" price.

## Paying: providers and apps

Dutch city parking is paid in three ways:

1. **parkeerautomaat** — bank / credit / chip card (chipknip is discontinued).
2. **Phone app or SMS** — through a registered provider.
3. **Digital parking system** — the city's own app or web loket (Den Haag, see below).

Mobile parking always runs through a registered **aanbieder** (provider), so the plate and payment method must be registered with one first:

- ANWB Onderweg (the Dutch touring club, ~43% share)
- EasyPark (~32%)
- Q-Park (~18%)
- Parkmobile / SMSParking / Stadsparkeren / Tango and others

**Key rule**: register with a provider (plate + payment method) first, then start/stop through the app, SMS or phone. A wrong plate is a fine (boete) — plate formats, validation and vehicle registration all live in `skills/netherlands-vehicle-admin/`.

## 海牙 (Den Haag)

### 数字停车系统（官方 loket）

- **入口**：`parkerendenhaag.nl`（Digitaal Parkeerloket）。
- **登录**：meldnummer（报号码）+ pincode。
- **操作**：输入访客车牌（kenteken）+ 开始/结束时间 → 点 "aanmelden"。
- **结束**：到点自动停，也可提前修改/取消。
- **覆盖**：所有收费停车位，包括**没有自动售票机的街道**。
- 注意口径不一致：市政的 stadsdeel 页面走 `denhaag.nl/nl/parkeren/<stadsdeel>`，而按单个停车场/车位计价的页面在私有站点 `parkeren-denhaag.nl`（含 "Gratis Parkeren <straat>" 页）。三个域名的分工用之前先在浏览器里核一遍，不要凭记忆引用。

### 费率与计费时段

- 市中心（Centrum）费率口径（2024–2025 上涨后）：多数区域 **€2.75/小时**，部分核心区域 **€7.15/小时**；计费时段通常 **09:00–24:00**，周日 **13:00–24:00**。
- 新闻口径（2026）把海牙、乌得勒支最繁忙区域记作 ≈ **€7/小时**，与上面的核心区数字方向一致，但不如市政费率表具体 —— 引用时用市政表。
- 免费的只是外圈：有些街道有小额 "groengele" 短停区（见下）和 Gratis Parkeren 车位，其余一律收费。

### 分区（vergunninggebied）与费率区

分区不是行政边界，是画出来的多边形，而且同一号码可以落在互不相连的多块区域上：

- 已知区域：`01 Centrum`、`18B Laakhaven`、`18C Laakkwartier–Laak`（**每日 18.00–24.00**，晚上才收费）、`18F Noordpolderbuurt`，另有 zone 30 / zone 32（Centrum Zuid 一带）以及 Scheveningen（自有区号，与 Centrum 不通用）。
- 短停区（groengele kort-parkeer zone）：Loosduinse Hoofdstraat **€0.10/次，最多 1 小时，周一至周六 10:00–18:00**，满 60 分钟后需重新登记。
- **怎么查一个地址在哪个区**：`denhaag.nl/nl/parkeren/<stadsdeel>`（收费时段与分区列表）→ 官方的分区 folder PDF（每区一份）→ WFS 矢量图层（永远最新、无需 key）：`Gisib_Vergunninggebieden_DPZ_TeamWebsites`（许可区，含子码）与 `Gisib_Tariefgebieden_DPZ_Teamwebsites`（费率区，小时费率写在 `WERKINGSTIJDEN` 里）。图层发现、点在多边形内判定与出图见 `references/denhaag-parkeerkaarten.md`。
- 判断某个地址是否需要许可：先查费率图 —— 街道在分区外就没有可申请的东西；在分区内才谈许可。

### 许可（vergunning）

- **bewonersvergunning**（居民停车证）：绑 **人 + 车牌 + 地址**，只在居住地的 vergunninggebied 内有效，每个地址上限 3 个；申请人必须是**在 BRP 里登记在该地址的居民**（不是公司），且名下不能有可用的自有车位。公司名下的车另需 berijders-/werkgeversverklaring —— 完整条款集、风险评估与提交地址见 `references/denhaag-bewonersvergunning.md`。
- **bezoekersvergunning**（访客证）：让访客按小时停车，每个地址每个日历年 1 个，年度额度取决于该区**每周计费小时数**（138 / 203 / 268 / 332 / 366 小时五档），只在**申请时那个地址所属的区**里有效 —— 别把 A 区的访客证拿去 B 区用。额度表、计费区间推导方法与金钱规则同上那份参考。
- 政策会变：自 2026 年 4 月起，自家院内已有停车位的居民不再有资格申请街边许可。提交/邮寄地址：Handhavingsorganisatie, Antwoordnummer 1435, 2501 VE Den Haag（免 postzegel）；停车服务台 14070；许可门户 `parkervergunningen.denhaag.nl`（MijnDenHaag）。

### 无自动售票机的街道

部分街道没有 parkeerautomaat，必须用手机（服务商 app 或上面的 loket）支付；海牙官网提供 PDF 清单，引用前先取当期版本。

## 阿姆斯特丹 (Amsterdam)

- **路边**：Stadsdeel Centrum **€5.37–8.05/小时，24/7 含周日和晚间**，无夜间豁免；其他 stadsdeel 从外圈约 €0.20 到约 €6.98/小时，计费窗口更短。违规罚款 **€79.10 + 对应费率**，由车牌扫描车开单，没有纸质小票可赌。免费车位只在最外围和国王节。（旧口径把市中心写为 €5–7.50/小时，已由市政 2026 费率区间取代。）
- **停车楼**：市中心首选 Parking Centrum Oosterdok（Oosterdoksstraat 140，导航地址 Oosterdoksstraat 150 / De Ruijterkade 154；约 1369 位、24/7、doorrijhoogte 2.10 m；预购 dagkaart €25–30 按日期定价、avondkaart €10、14:00–17:00 的 dagdeel 从 €15、walk-in €8/小时封顶 €45）。P1 Centrum（Prins Hendrikkade 20a，离 Zeedijk 最近约 500 m，1.9 m 限高，第三方页面报 ≈ €3.50/小时、€45–50/24 h，**未在运营方页面核实**，电话 020-6385330，不接受第三方平台预订）。对照用的贵档：Q-Park Waterlooplein（≈ €13/小时）、Q-Park Centraal、Q-Park Nieuwendijk €32.50、Q-Park Bijenkorf、Markenhoven / Rokin 封顶 ≈ €90/天。完整表与 P+R 清单见 `references/amsterdam.md`。
- **P+R**：€6/24 h（周末及工作日 10:00 后入场）、工作日 10:00 前首 24 h €13，最长 96 h（RAI 24 h）；折扣条件苛刻，见 `references/city-parking-and-p-r.md`。
- **排放区**：A10 以内柴油车需 Euro 5 以上（Euro 4 及以下禁入，40 年以上老爷车豁免）；S100 以内的零排放区 2025 年起管厢式车与货车、2030 年起管乘用车。罚款：小客车/厢式车 €130，货车 €320，轻便摩托 €90。
- **Chinatown / Zeedijk**：Zeedijk 是步行街（市政讨论过正式划为无车街），不要开进去。卸货在 Zeedijk 北端 Prins Hendrikkade 一侧的 laad- en losplaats（OSM 记 4 个仅装卸位，`access:conditional = yes @ loading`），然后停车。最近地铁站 Nieuwmarkt（53/54 线），运营约 05:30–01:00，23:00 回程有余量，午夜后要查时刻表。Oosterdok 车库到 Zeedijk ≈ 600–800 m（8–10 分钟），到 Nieuwmarkt ≈ 670 m；P1 Centrum ≈ 500 m。

## 鹿特丹与其他城市

- **鹿特丹**：市中心约 **€4.24/小时**（2026 口径；早前来源给的 €3–5/小时区间是旧口径，保留更具体的那个）。官方 App 方面只见到 "R-Charge" 之类的二手说法，未经核实 —— 报价前先查市政费率图。
- **乌得勒支 / 海牙**最繁忙区域 ≈ €7/小时（新闻口径），按上面海牙的方法在市政费率图上确认。
- 没有任何一个城市有统一的全国费率：每个城市的计费时段、免费日和 P+R 条件都不同，换城市就要重跑一遍下面的流程。

## 休闲与海岸目的地 —— 形状不一样

Beach, dune and lake destinations are not a smaller centre trip: usually one flat-rate or free surface lot, nothing to book, and the decision variable is **time limit and season**, not a tariff matrix.

### Answering a leisure-outing request

1. Price every candidate from the user's own address, not from the city centre:
   `python maps/scripts/maps_client.py distance "<home>" --to "<candidate>" --mode driving`.
   That km/minute figure is what decides the trip, so lead with it.
2. Shortlist places with `nearby` (restaurant, cafe, parking, park), then verify the facilities that decide the outing against whoever manages them — OSM parking nodes are usually unnamed and carry no fee, capacity or time-limit tags, and OSM hours on seasonal venues are a coarse range such as `Mar-Oct`.
3. Check whether to go today: weather (`curl -s "https://wttr.in/<city>?format=j1"` — per-day summed `precipMM` and max `windspeedKmph`) and sunset (`https://api.sunrise-sunset.org/json?lat=..&lng=..&date=YYYY-MM-DD&formatted=0`, UTC). For an outdoor destination low wind decides more than temperature.
4. Hand over coordinates plus a tap-to-open `https://www.google.com/maps/dir/?api=1&destination=<lat>,<lon>` link — a place name alone is not actionable in a car, and the address an operator publishes for navigation is often not its street address.
5. Lead with the closest option and keep the long scenic loop as the secondary one. "Near" beats "beautiful": a beautifully routed 77 km tour answers a question nobody asked when a 16-minute drive was available.

### Lot-level rules

- Price the two lots the destination actually has: the paid one at the front and the free one a kilometre back. The free lot is usually also the quieter and better place to sit, so recommend it as the default, not as the compromise (Kijkduin: Deltaplein garage 1.5 h free then €3.50/h vs free Machiel Vrijenhoeklaan).
- "First 1.5 hours free" is per entry: right for eating inside the window, wrong for an afternoon of sitting. Say which one the plan needs before quoting it.
- Beach parking switches its day card on fixed dates (1 April / 1 October in Noordwijk) and beach pavilions run Mar-Oct or May-Oct. Quote the rate for the season containing the requested date and name the pavilion's season, or the recommendation dies silently in the wrong month.
- Take rates from whoever manages the ground: the municipality's own parking site for lots and garages, the land manager (Staatsbosbeheer for provincial recreation areas, the water company for dune reserves) for the free car parks inside a nature area — those pages name lots no aggregator lists.
- Free does not always mean unrestricted: a town can be free parking while the nature reserve inside it runs its own regime. Check the reserve, not the town.

Concrete Den Haag coastal rates, lots, nature-area entrances and the eating spots that pair with each lot: `references/denhaag-coastal-trips.md`.

## Procedure

1. Fix constraints: destination address, arrival at the garage, departure time, whether the car must stay reachable. Departure time decides which card buys — day card = calendar day (00:00-23:59), evening card = from 18:00, and leaving after midnight re-triggers the hourly rate.
2. Pull the official zone rate for the destination street (Amsterdam: https://www.amsterdam.nl/parkeren/parkeertarieven-kaart, which gives per-stadsdeel ranges and paid hours; Den Haag: see the zone paragraph above).
3. Shortlist garages within ~1 km: `python maps/scripts/maps_client.py nearby --near "<destination>" --category parking --radius 900 --limit 20`, then keep the ones with a walkable route.
4. Probe each shortlisted operator's booking flow for the ACTUAL date — see `references/booking-flow-probing.md`. The "vanaf EUR X" on the marketing page is not what that date costs.
5. Evaluate transit-only options with `references/amsterdam.md` (Amsterdam data shape, P+R rules, event closures).
6. Compare money against detour time and state the break-even explicitly ("saves EUR 18 for ~55 extra minutes and two failure modes -> not worth it").
7. Then hand over: verified link, navigation address (garages often publish a different navigation address than their street address), height limit vs the car's height, card expiry time, and the barrier routine.

## Pitfalls

- **The advertised card price is a "from" price.** The same day card costs more on a given date. Read the total off the booking step for that date.
- **A P+R discount is revoked silently.** Conditions: own OV-chipkaart or paper GVB ticket (never OVpay/bank card/phone/QR/paper NS ticket), travel to and from the centre by public transport, last check-in inside the centre zone, and payment within 1 hour after the OV check-out. Break one and the walk-in tariff applies — often more than the centre day card. Always state these conditions so the user can decide whether P+R is really on the table.
- **P+R at stadiums and RAI closes for events.** The closure list sits on that location's own municipality page and lists date PAIRS around each event, so check the days either side of a match/concert, not just the event day.
- **Check the car against the garage clearance** before recommending it: `hoogte_voertuig` from RDW (see `references/booking-flow-probing.md`) vs `doorrijhoogte` (commonly 1.9-2.1 m; a modern SUV is ~1.69 m).
- **With a reservation the barrier reads the plate and opens automatically — do not pull a ticket.** Pulling one books you in as a walk-in at the hourly rate. The access code/barcode on the confirmation is the fallback when the barrier does not open.
- **Overstaying a card is charged hourly at the exit**, so give the exact expiry (23:59 for a day card) up front.
- **Plate fields**: CAPITALS, without dashes, country code `NL`. Read the field's own `data-validation` attribute instead of assuming a format rule — and expect platform-side Dutch-plate validators to lag RDW sidecodes (sidecode 11 `XXX-99-X` has been issued since mid-2024 and is still missing from many), so a rejection can be the form's bug rather than a typo.
- **A wrong plate is a fine.** Both the phone providers and Den Haag's loket park on the plate you enter; entering someone else's or a mistyped plate does not save the fine, it moves it to the wrong person.
- **Aggregator pages go stale** (rates, promo names, caps). Use the operator's own site or the booking engine; flag anything you can only source from a blog.
- **A permit grant is not the end of the check.** Read the granted `Zone omschrijving` back against the zone map already produced rather than re-deriving it, and state the two limits the holder will hit: the zone is only the outlined area (neighbouring zones are not covered even a street or two away), and the `01A`–`01D` street segments inside the Centrum zone are excluded from the permit.

Vehicle-side duties that are not parking (WA insurance, APK, road tax, export notification): `skills/netherlands-vehicle-admin/`.

## References

- `references/amsterdam.md` — Amsterdam street zones and centre-garage facts, the full P+R table with exits and transit, Chinatown/Zeedijk specifics, drive baselines to Amsterdam.
- `references/city-parking-and-p-r.md` — where the numbers come from, the garage-ranking procedure, P+R mechanics and fines, the booking form's own field rules, and the other cities.
- `references/booking-flow-probing.md` — reaching the real order form, reading the price for a date, reading field rules, and verifying plate/vehicle via RDW open data.
- `references/denhaag-coastal-trips.md` — Den Haag beach/dune/lake parking with verified rates, free lots, nature-area entrances, paired restaurants, drive baselines, and the weather/sunset checks.
- `references/denhaag-bewonersvergunning.md` — resident permit for a company car: who applies, the berijders-/werkgeversverklaring clause set, and the visitor-permit hour quota.
- `references/denhaag-parkeerkaarten.md` — finding Den Haag permit/tariff zones (folder PDFs, WFS layers, Leaflet tricks), point-in-polygon tests, map rendering, and the one-page permit sheet.

---
name: geely-starray-em-i
description: Use when asked about the Geely Starray EM-i car.
version: 1.0.0
version: 1.1.0
license: CC BY-NC 4.0
author: sixgod
metadata:
  hermes:
    tags: [geely, starray, galaxy-starship-7, flyme-auto, flyme-sound, phev, infotainment]
    category: productivity
    related_skills: [netherlands-vehicle-admin]
---

# Geely Starray EM-i — identity, manuals, infotainment

The Geely Starray EM-i is a plug-in hybrid that reaches the Netherlands mainly as a parallel import, so registration, tax and insurance questions go to `skills/netherlands-vehicle-admin/` (RDW open data is authoritative there). This skill covers what the car *is* and how its head unit works.

## Identity: one car, many nameplates

The car is Geely Galaxy Starship 7 EM-i (吉利银河星舰7 EM-i), model code **P145**, built in Linhai, Zhejiang on the GEA platform (shared with Galaxy E5/EX5).

- China: 吉利银河星舰7 EM-i
- Most export markets: Geely EX5 EM-i · South Africa: E5 EM-i · Kazakhstan: Galaxy EX5 EM-i · Belarus: BelGee X80 PHEV · Malaysia: Proton eMAS 7 PHEV · Australia/Indonesia/New Zealand/Spain/France/UK: **Starray EM-i**

**Check the build year before reusing "Starray" sources.** The Starray nameplate was previously the export name of the Geely Boyue L; only from 2025 does it map to Starship 7 EM-i. When hunting Chinese parts, manuals or forum posts, search 银河星舰7 EM-i, not Starray.

Spec deltas that catch people out: export cars ship the 18.4 kWh pack (WLTP EV range ~136 km) with a 1.5 L NordThor EM-i + E-DHT making 160 kW / 262 N·m, while China also sold an 8.5 kWh / 55 km CLTC entry version. Export trims are fixed bundles (AU/NZ: Complete, Inspire; UK: Pro, Max, Ultra).

## Owner's manual

Official English PDF (Starray EM-i, all trims):
`https://geelyprod-static2.oss-ap-southeast-5.aliyuncs.com/products/file/geely_starray_em_i_owner_manual.pdf`

Keep a local copy of the PDF plus its extracted text. Regenerate the text with `pdftotext -layout` (installed; emits harmless oc/font syntax warnings). Working on the text file beats scrolling the PDF — the section index sits at the end, and "Sound Settings" lands around line 7397 of the extracted text for this revision.

UK (geelyauto.co.uk) and EU (geelyauto.eu) sites also publish the manual and spec sheets; the NZ/AU spec sheets are the cleanest trim-by-trim equipment table.

## Digital key: no Apple Watch (and no iPhone key) path on this car

Asked "can I lock/unlock with my Apple Watch" — the answer is no, and don't go hunting for a setting:

- **None of Geely's official apps ship a watchOS target.** Verified via the public iTunes lookup API (`curl -s 'https://itunes.apple.com/lookup?id=<appid>&country=nl'`): the Geely Overseas app (6670387299, same id for NL/UK/AU, v2.0.5), 吉利汽车 (1518762715, v3.55.0) and 吉利银河 (6445883350, v1.56.0) all lack any `Watch*` entry in `supportedDevices`. Control check: apps that *do* have a Watch app (Tesla, Tessie, CARROT Weather) return an extra `Watch4-Watch4`. The App Store web page shows the same thing as "Compatibility: iPhone, iPod touch, Mac, Apple Vision" with no Apple Watch row.
- **The car is not in Apple Wallet's car-key programme.** CarKey is the only native route that puts a key on an Apple Watch (works without the phone, without network), and it needs the OEM to license it and fit NFC/UWB readers. Wallet car-key support runs BMW, MINI, Mercedes-Benz, Audi, Porsche, Genesis, Hyundai, Kia, Toyota, Volvo, Polestar, Lotus, Rivian, RAM, and among Chinese brands only **BYD (HAN) and NIO (ET7)** — no Geely brand, no Galaxy/Proton eMAS twin. Apple does not publish a model-by-model list; third-party trackers are the practical reference.
- **China-only keys don't travel to iOS either.** Domestic cars hand the digital key to Android vendor wallets (Huawei/Honor BLE+NFC digital key, listed for 银河E5/E8/星舰7/…). iOS has no equivalent third-party channel, so an iPhone owner gets no wallet key there either. The export owner's manual documents only the smart remote key (lock / vehicle-search / tailgate / mechanical emergency key) and never mentions an app key.

What the car *does* have (AU spec sheet for the Starray EM-i, matches export trims): `Remote Lock Unlock: yes` via the Geely app over the embedded 4G SIM, `Keyless Entry`, `Keyless Start`, `Walk Away Locking`, and a `Card Key`. Two limits to state up front:

- Remote unlock does **not** authorise driving — Australian owners confirm the app opens the car but the smart key must be present to start and drive it. A Watch-triggered unlock would only ever mean "open the door", never "drive off".
- The app path needs network (embedded SIM); the fob/card path needs no phone at all. For a wrist-only setup there is no solution short of a car that supports Apple Wallet car keys (BYD, NIO, BMW, …).

Before claiming "no Watch support", check whether the Geely app exposes **App Intents / Shortcuts actions** — if it did, a Shortcut could run on the Watch (still remote, still network-bound). No official documentation confirms this either way, so the fast check is: iPhone → Shortcuts → search "Geely".

## Flyme Auto head unit: sound settings

Top trim carries the 16-speaker, 1000 W Flyme Sound system: 4 tweeters, 5 mid-range, 4 woofers, 2 driver-headrest speakers, 1 subwoofer (China counts the headrest pair separately as "14扬声器+2头枕音响" — same hardware).

Verified menu tree (owner's manual, Sound Settings pp. 173–175):

```
Vehicle Settings → Sound Settings
  ├ Sound Effects
  │   └ Headrest Stereo (Intelligent Headrest Mode)
  ├ Volume Control
  └ Alerts and Tones
Spatial Sound (also via Vehicle Settings → Shortcuts, or the quick-access screen)
  ├ Sound Field Mode
  ├ Surround Sound
  ├ Headrest Stereo
  ├ Intelligent Headrest Mode
  └ Equaliser
```

Chinese-market wording for the same page (银河E5 车机评测, same Flyme Sound generation): 音效设置 splits into **空间音效** and **虚拟场馆**; 空间音效 offers 声场模式 (全车/主驾/后排/自由), 头枕音响模式 (共享/驾享/私享/智能) and 自定义调频; 虚拟场馆 offers 录音棚/音乐厅/歌剧院/演唱会. Wording drifts with OTA versions — describe the function, not the exact label.

Two behaviours worth knowing: Intelligent Headrest Mode auto-reverts the sound field to driver-centric when someone sits in the front passenger seat, and the driver headrest speakers sit in a headrest that can be height-adjusted but not removed.

**The manual does not enumerate the equaliser's bands, and OTA changes what the screen shows.** Never invent band counts or frequency labels for this car — describe how to tune whatever the screen exposes, or ask the user for a photo of the equaliser page and give values per band.

Tuning order that matters: defeat 虚拟场馆/surround first, pick the sound-field mode, set the headrest mode, and only then touch the equaliser — the venue and surround processing reshapes the response, so EQ work done before it has to be redone.

## "Intelligent Reminders" re-arm at every power-on — this is law, not a bug

Owners complain that `Vehicle Settings → Driver Assist → Safety Settings → Intelligent Reminders` (Speed Limit Information Recognition / Speed Limit Alert, Speed Limit Update Reminder, Driver Fatigue Detection, Occupant In-vehicle Alert) switches itself back on after every start. **Do not hunt for a menu combination that makes it stick — none exists.** EU GSR2, Regulation (EU) 2019/2144 Annex II point 3.2.1.1: ISA "shall be automatically reinstated in normal operation mode upon each activation of the vehicle master control switch"; permanent disabling is expressly not permitted. Driver drowsiness/attention warning is one of the seven Article 6 mandated systems. Export firmware therefore re-arms by design, whether or not the car was first registered in the EU.

What the regulation *does* allow the owner to silence permanently (point 3.4.1.4 — the "speed limit changed" audible notification "may be user configurable (e.g. sound, volume, permanently switched off)"):

- `Speed Limit Alert` → **Blinking Icon** (icon blinks, no chime) rather than Blinking Icon & Sound Alert
- `Speed Limit Update Reminder` → off

That leaves the icon on every trip but stops the bongs, with no software modification.

Real solutions, in order of cost:

1. **Official OTA "Drive Setup" one-touch profile.** The March 2026 OTA (Starray EM-i first OTA; also EX5 Flyme Auto S 1.2.0) stores drive mode, regen, Lane Keeping Assist, Emergency Lane Keeping, Driver Fatigue Detection, Speed Limit Alert (off / blinking icon / + sound) and Battery Hold as one driver profile, re-applied from a steering-wheel shortcut or the swipe-down menu. Geely AU/Israel publish it; it is the intended answer to this complaint. Requirements: car on that software (check the version page — the owner's manual PDF predates OTA and documents none of it), download over **home Wi-Fi**, because the built-in SIM route frequently fails.
2. **Third-party sideload** — EucalyptusSoftware "Geely Custom Profiles" (`eucalyptussoft.cc`, ~$25 via Buy Me a Coffee). Re-enforces settings on every head-unit boot and on gear change; toggles include Speed limit alert, Driver fatigue monitoring, Occupant detection, Lane Keeping Assist. Supports EX5 / EX5 EM-i / **Starray** / Starship 7 / Proton e.Mas 7 (Starray support added v3.4.0, same Antora 1000 head unit). Caveats to state up front: needs **USB ADB enabled on the head unit**, and MY26+ head units ship with ADB closed (only known unlock is opening the unit and jumping pins); unofficial; it also offers disabling vehicle OTA updates. Treat as a last resort behind option 1.

Do **not** suggest covering or unplugging the driver-monitoring camera to kill fatigue warnings — it lights a permanent fault indicator and degrades related AEB behaviour. Fatigue/distraction warnings arm above 35 km/h and release below 30 km/h (manual p.153), so slow urban driving is legitimately quiet.

---
name: industrial-maintenance-netherlands
description: Electrical procurement and refrigeration troubleshooting.
version: 1.0.0
license: CC BY-NC 4.0
author: sixgod
---

# Industrial Maintenance Netherlands

## Scope
- Industrial electrical component identification and cross-referencing
- Model number interpretation (Siemens, Schneider, ABB conventions)
- Cross-brand replacement workflows
- Netherlands/European supplier sourcing
- Refrigeration system basic troubleshooting
- Emergency technician finding in Netherlands

## Component Identification

### Siemens SIRIUS Model Number Structure
```
3RT2016-1AP02+SG
│    │   │  │   └── Suffix: +SG = elevator certified (CSA/UL)
│    │   │  └────── Coil voltage: AP01=24VDC, AP02=230VAC, BB41=24VDC
│    │   └───────── Current rating: 16=9A, 17=12A, 18=18A (x10 for size)
│    └───────────── Series: 20=standard, 21=economy
└────────────────── Product family: 3RT=contactor, 3RU=overload relay
```

### Schneider EasyPact Model Number Structure
```
LC1E0610M7
│  │ │  │ └── Coil voltage: M5=24VDC, M7=230VAC
│  │ │  └──── Auxiliary contacts: 10=1NO, 11=1NO+1NC
│  │ └─────── Current rating: 06=6A, 09=9A, 12=12A
│  └───────── Series: E=economy, D=standard
└──────────── Product family: LC1=contactor, LRE=overload relay
```

### Critical Matching Rules
| Parameter | Must Match | Notes |
|-----------|------------|-------|
| Coil voltage | ✅ Critical | 24VDC≠230VAC - causes short circuit if wrong |
| Current rating | ✅ Critical | Must exceed motor FLA |
| Phase count | ✅ Critical | 3P for 3-phase motors |
| Mounting style | ⚠️ Important | DIN rail vs panel mount |
| Brand compatibility | ⚠️ Important | Siemens overload won't fit Schneider contactor |

## Cross-Brand Replacement

### Siemens → Schneider Equivalents
| Siemens | Schneider | Notes |
|---------|-----------|-------|
| 3RT2016-1AP02 (9A, 230VAC) | LC1D09M7 (9A, 230VAC) | Direct replacement |
| 3RU2116-1HB0 (5.5-8A) | LRE12 (5.5-8A) | Direct replacement |

### ⚠️ Common Pitfalls
1. **Coil voltage mismatch** - Buying 24VDC coil for 230VAC system causes immediate short circuit and blown fuses
2. **Overload relay brand mismatch** - Schneider LRE won't physically plug into Siemens 3RT contactor (different pin spacing)
3. **Suffix confusion** - +SG suffix on Siemens means elevator certification, not needed for general refrigeration

## Netherlands Supplier Sources

### Industrial Components
| Supplier | Website | Specialty |
|----------|---------|-----------|
| TME.com | tme.eu | Broad range, competitive prices |
| Siemens Industry Mall | mall.industry.siemens.com | Official, full catalog |
| Distrelec | distrelec.nl | Dutch distributor |
| RS Components | rs-online.com | Industrial parts |

### Refrigeration Technicians (Koeltechnisch Monteur)

For urgent refrigeration repairs, source a local certified technician via
Google Maps / local directory search for "koeltechnisch monteur" near the
site, and verify they cover your region before dispatch. Mobile numbers of
individual technicians are not listed here (they change and are personal).

### Emergency Electricians

For emergency electrical call-outs, search Google Maps for a licensed
electrician (elektricien, "24/7 spoed") in the site's municipality, and
confirm they respond for your postal code area before dispatching.

## Refrigeration Troubleshooting

### Error Code Reference (Rivacold)
| Code | Meaning | Action |
|------|---------|--------|
| E4 | High pressure / sensor fault | Check condenser fan, check refrigerant level, check pressure switch |
| E1 | Low pressure | Check refrigerant level, check for leaks |
| E2 | Compressor overload | Check compressor current, check overload relay |

### Diagnostic Flowchart
```
1. Check controller display for error code
   └── If error code present → look up meaning
2. Check power supply
   └── Measure L1-L2-L3 (should be 380-420V 3-phase)
3. Check contactor coil voltage
   └── Measure A1-A2 (should match coil rating)
4. Check overload relay
   └── Check current setting matches motor FLA
   └── Press RESET - if trips immediately → overcurrent
5. Check fans
   └── Condenser fan not running → high pressure → E4
6. Check sensors
   └── Measure resistance (should be kΩ range, not 0 or ∞)
```

## Safety Warnings

### ⚠️ NEVER DO
- Connect 230VAC to a 24VDC coil contactor (causes immediate short circuit)
- Press RESET repeatedly on a tripping overload relay (indicates real fault)
- Mix contactor and overload relay brands without verifying physical compatibility

### ✅ ALWAYS DO
- Verify coil voltage BEFORE installing contactor
- Measure actual motor FLA before setting overload relay
- Disconnect power before working on control wiring
- Use correct fuse rating after a short circuit event
# Dyness Powerbrick Pro 14.3 kWh BMS Balancing and Charge-Control Behaviour

**Author:** Heiko Gerdes  
**Contact:** hgerdes@tehnosys.ro  
**Battery software version tested:** `2.50-71.10.11`
**Battery type tested:** `Dyness Powerbrick Pro 14.3 kWh`
**Report version:** 1.0.0  
**Publication date:** 2026-08-09

This repository is the publication and evidence package for an experimentally derived characterization of Dyness BMS balancing, CCL behaviour and charge-MOSFET protection.

## Key observed results

| Function | Criterion | Result |
|---|---|---|
| Global balancer enable | `Ibat >= 1.5 A` for 30 s | Balancing enabled |
| Global balancer disable | `Ibat <= 1.4 A` for 30 s | Balancing disabled |
| Individual resistor selection | `Vcell - Vmin >= 30 mV` | Cell resistor ON |
| Individual balancing channel current | Approx. `60 mA` per selected cell | Indirect matched-state estimate; approx. 50-70 mA interpretation range |
| Full detection | `Vmax >= 3.5 V` | SOC 100 %, CCL 0 A, Charge Enabled false |
| Charge MOSFET cutoff | `Vmax >= 3.6 V` | Charge MOSFET OFF |
| Charge MOSFET reset | `Vmax < 3.45 V` **or** effective-discharge bit set | Charge MOSFET ON; bit observed set at approx. 1-1.5 A discharge |
| Charge permission recovery | SOC `100 % -> 99 %` | CCL 56 A, Charge Enabled true |

The **30 s timing** is an engineering hypothesis derived from transition behaviour and is explicitly identified as such in the report.

## 16-cell telemetry note

The battery is a 16-cell series pack. Cells 1-15 are transmitted directly. Cell 16 is reconstructed in the CSV as:

`V16 = Vpack - sum(V1 ... V15)`

The reconstructed value is part of the complete 16-cell model, but its millivolt-scale trace contains additional quantization from pack voltage and subtraction. Direct cells 1-15 were therefore weighted more heavily when fitting millivolt-scale resistor switching thresholds.

## Contents

- `report/` - publication PDF and editable DOCX source
- `data/` - raw CSV telemetry and extracted switch-event table, including the balancing-current calculation source
- `report/Dyness_Passive_Balancing_Current_Estimation_Technical_Note-1.pdf` - accompanying indirect current-estimation note
- `report/dyness_balancing_cycle_projection_report_with_bleeder_hours.pdf` - quoted reference titled **Observed practical imbalance**; not duplicated as a full derivation in the main report
- `figures/` - UML and analysis figures
- `site/` - crawlable static HTML publication for search engines and AI retrieval
- `metadata/` - publication metadata and Zenodo field template
- `posts/` - ready-to-post community announcements
- `AGENTS.md` - durable instructions for Codex
- `CODEX_HANDOFF.md` - execution plan and approval checkpoints
- `.github/workflows/pages.yml` - GitHub Pages deployment

## Citation

Use `CITATION.cff`. Reserved Zenodo DOI for the definitive v1.0 record: `10.5281/zenodo.21860970`.

## Passive-balancing current evidence

The accompanying calculation note estimates an effective passive-balancing current of approximately 60 mA per selected cell or active channel between 3.5 V and 3.6 V. The fitted effective bleed resistance is approximately 58.7-60.7 ohm, with about 0.20-0.22 W dissipated per active channel and a conservative interpretation range of 50-70 mA. This is an indirect engineering calculation from matched-state telemetry, not a direct resistor-current measurement or an official Dyness specification.

The calculation source for this revision is `data/dyness-balancer-2026-08-09T11-28-32(3).csv` (3,207 rows, 62 columns, SHA-256 `a51d6d791e034922fdf1751ba24e98f9c1ad3997f61f968700f7107bc1acada6`). The technical note is preserved unchanged as an accompanying evidence document.

## Observed practical imbalance

The supplied `report/dyness_balancing_cycle_projection_report_with_bleeder_hours.pdf` is included unchanged as a quoted companion measurement reference. Its projection states: “Best working estimate: about 20-21 comparable balancing cycles, corresponding to about 21-22 cumulative effective cell-7 bleeder hours.” This is the author's own measured calculation under its documented assumptions, quoted here without duplicating its full derivation. SHA-256: `8eac7d25ae654babeb66347a2a87693a94329f15c5d25b0514f665b4ca99fcc8`.

The physical charge-MOSFET reset has two observed triggers after cutoff: the highest cell falling below approximately 3.45 V, giving approximately 150 mV of voltage hysteresis, or the `effective discharge` bit becoming set. In the tested system, that bit is set when discharge current reaches approximately 1-1.5 A. The 3.50 V full-detection/CCL threshold remains separate.

## Licensing

This repository, report and accompanying evidence are licensed under **CC BY 4.0**. See `LICENSE` and `LICENSE_DECISION.md`.

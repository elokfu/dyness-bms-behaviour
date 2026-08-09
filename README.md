# Dyness BMS Balancing Algorithm and Charge-Control Behaviour

**Author:** Heiko Gerdes  
**Contact:** hgerdes@tehnosys.ro  
**Battery software version tested:** `2.50-71.10.11`  
**Report version:** 1.0.0  
**Publication date:** 2026-08-09

This repository is the publication and evidence package for an experimentally derived characterization of Dyness BMS balancing, CCL behaviour and charge-MOSFET protection.

## Key observed results

| Function | Criterion | Result |
|---|---|---|
| Global balancer enable | `Ibat >= 1.5 A` for 30 s | Balancing enabled |
| Global balancer disable | `Ibat <= 1.4 A` for 30 s | Balancing disabled |
| Individual resistor selection | `Vcell - Vmin >= 30 mV` | Cell resistor ON |
| Full detection | `Vmax >= 3.5 V` | SOC 100 %, CCL 0 A, Charge Enabled false |
| Charge MOSFET cutoff | `Vmax >= 3.6 V` | Charge MOSFET OFF |
| Charge MOSFET recovery | `Vmax < 3.5 V` | Charge MOSFET ON |
| Charge permission recovery | SOC `100 % -> 99 %` | CCL 56 A, Charge Enabled true |

The **30 s timing** is an engineering hypothesis derived from transition behaviour and is explicitly identified as such in the report.

## 16-cell telemetry note

The battery is a 16-cell series pack. Cells 1-15 are transmitted directly. Cell 16 is reconstructed in the CSV as:

`V16 = Vpack - sum(V1 ... V15)`

The reconstructed value is part of the complete 16-cell model, but its millivolt-scale trace contains additional quantization from pack voltage and subtraction. Direct cells 1-15 were therefore weighted more heavily when fitting millivolt-scale resistor switching thresholds.

## Contents

- `report/` - publication PDF and editable DOCX source
- `data/` - raw CSV telemetry and extracted switch-event table
- `figures/` - UML and analysis figures
- `site/` - crawlable static HTML publication for search engines and AI retrieval
- `metadata/` - publication metadata and Zenodo field template
- `posts/` - ready-to-post community announcements
- `AGENTS.md` - durable instructions for Codex
- `CODEX_HANDOFF.md` - execution plan and approval checkpoints
- `.github/workflows/pages.yml` - GitHub Pages deployment

## Citation

Use `CITATION.cff`. A DOI should be reserved on Zenodo before the definitive v1.0 PDF is published, then inserted into the PDF, page metadata, `CITATION.cff` and repository metadata.

## Licensing

This repository, report and accompanying evidence are licensed under **CC BY 4.0**. See `LICENSE` and `LICENSE_DECISION.md`.

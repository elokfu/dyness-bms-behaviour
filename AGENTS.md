# AGENTS.md - Dyness BMS publication repository

## Mission
Publish and maintain the technical report so engineers, conventional search engines and AI search/retrieval systems can find, quote and cite concrete Dyness BMS behaviour.

## Non-negotiable technical facts
Do not change these values unless new measurement evidence is added and the author explicitly approves a revision:
- Tested battery software: `2.50-71.10.11`.
- 16 physical series cells. Cells 1-15 are direct telemetry; cell 16 is reconstructed as `Vpack - sum(V1..V15)` in the CSV.
- Balancer global enable: `Ibat >= 1.5 A`.
- Balancer global disable: `Ibat <= 1.4 A`.
- 30 s current qualification is an **engineering hypothesis**, not firmware-confirmed fact.
- Individual resistor selection: `Vcell - Vmin >= 30 mV`.
- Individual passive-balancing channel current: approximately `60 mA` per selected cell, derived indirectly from matched-state telemetry; this is not a manufacturer specification.
- Full detection: `Vmax >= 3.5 V` -> SOC 100 %, CCL 0 A, Charge Enabled false.
- CCL 0 A / Charge Enabled false do **not** open the physical charge MOSFET.
- Balancing continues between 3.5 and 3.6 V when balancing criteria remain fulfilled.
- Charge MOSFET OFF: `Vmax >= 3.6 V`.
- Physical charge-MOSFET reset after overvoltage cutoff: `Vmax < 3.45 V` (approximately 150 mV hysteresis from the 3.6 V cutoff), independent of discharge current.
- CCL restoration: SOC `100 % -> 99 %` -> CCL 56 A / Charge Enabled true.
- The 3.5-3.6 V region is not recommended for deliberate charging because that ignores CCL = 0 A and may create warranty implications.

## Editorial rules
- Preserve the report disclaimer distinguishing observation from manufacturer specification.
- Use nominal thresholds (30 mV, 3.5 V full detection, 3.6 V cutoff and approximately 3.45 V physical reset) in narrative text, keeping the control layers distinct.
- Never call the reconstructed cell 16 a nonexistent or ignored cell.
- Keep balancing, CCL communication control and charge-MOSFET protection as separate control layers.
- Prefer concrete question/answer headings on the web page because the publication is intended to answer real Dyness BMS searches.
- Do not introduce claims from forums as measured facts.

## Publication rules
- Before any irreversible publication, verify there are no placeholder DOI tokens and no broken links.
- Do not publish to Zenodo or submit a forum post without explicit author confirmation in the current session.
- The author confirmed CC BY 4.0 for the repository, report and evidence; keep that license consistent in all publication metadata.
- If a Zenodo DOI is reserved, insert the same DOI consistently into the PDF/DOCX title page, PDF metadata, `CITATION.cff`, web page structured metadata and repository metadata.
- The canonical target URL is currently `https://tehnosys.ro/dyness-bms/`; if hosting differs, update all canonical, sitemap and structured-data URLs consistently.

## Verification
Before proposing a release:
1. Run `python scripts/check_publication.py`.
2. Open `site/index.html` locally and verify content/links.
3. If DOCX/PDF is changed, render and visually inspect the complete PDF.
4. Confirm the three raw CSV files and figures are still downloadable.
5. Confirm `robots.txt` does not block OAI-SearchBot or general crawlers.

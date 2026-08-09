# Zenodo metadata - field values

Use these values in the Zenodo deposit UI or map them to the current Zenodo REST API schema.

- **Resource type:** Technical report / Report
- **Title:** Dyness Powerbrick Pro 14.3 kWh BMS Balancing Algorithm and Charge-Control Behaviour - Experimental Characterization, Firmware 2.50-71.10.11
- **Creators:** Heiko Gerdes
- **Publication date:** 2026-08-09
- **Version:** 1.0.0
- **Reserved DOI (draft):** 10.5281/zenodo.21860970
- **Language:** English
- **Description / Abstract:**

A Dyness Powerbrick Pro 14.3 kWh battery with a 16-cell Dyness BMS running battery software version 2.50-71.10.11 was experimentally characterized using continuous telemetry of cell voltages, battery current, SOC, CCL, charge-permission state, raw status bytes and BMS temperature. Cells 1-15 are transmitted directly and cell 16 is reconstructed from pack voltage minus the sum of cells 1-15. The observations separate passive balancing, communication-level charge control and physical charge-MOSFET protection. Balancing is enabled at a battery charge current of 1.5 A and disabled at 1.4 A, with a 30 s qualification time retained as an engineering hypothesis. Individual balancing resistors are selected when a cell is 30 mV above the minimum cell. An accompanying matched-state telemetry calculation estimates approximately 60 mA per selected cell or active passive-balancing channel between 3.5 V and 3.6 V, corresponding to approximately 58.7-60.7 ohm effective bleed resistance, 0.20-0.22 W per active channel and a conservative 50-70 mA interpretation range. This is an indirect engineering estimate, not a direct resistor-current measurement or manufacturer specification. At 3.5 V maximum cell voltage the BMS enters full state, reports SOC 100 %, CCL 0 A and Charge Enabled false while the charge MOSFET remains on. Balancing continues in the 3.5-3.6 V region if its current and cell-delta criteria remain fulfilled. At 3.6 V the charge MOSFET opens; permanent physical reset occurs below approximately 3.45 V, giving approximately 150 mV hysteresis independent of discharge current. CCL returns to 56 A when SOC changes from 100 % to 99 %. A separate supplied projection PDF is retained as a quoted reference titled Observed practical imbalance, as the author's measured companion report; its headline result is quoted below rather than re-derived in this report.

- **Keywords:** Dyness, Dyness BMS, battery management system, LiFePO4, passive balancing, 60 mA balancing current, balancing current estimation, cell balancing, BMS balancing algorithm, CCL, Charge Current Limit, charge MOSFET, charge FET, SOC, RS485, CAN, Victron, DVCC, cell voltage, firmware 2.50-71.10.11, PowerBrick
- **Access:** Open
- **License:** CC BY 4.0 (author confirmed)
- **Publisher:** Zenodo (default after deposit)
- **Related identifier - source code/data:** https://github.com/elokfu/dyness-bms-behaviour
- **Related identifier - web version:** https://elokfu.github.io/dyness-bms-behaviour/

## Current-estimation evidence

- **Calculation note:** `report/Dyness_Passive_Balancing_Current_Estimation_Technical_Note-1.pdf` (SHA-256 `f1e9327e8f3ad1a5a14037d4d42810438050990ef6c77736a4b3d4a9f2005c7e`)
- **Calculation CSV:** `data/dyness-balancer-2026-08-09T11-28-32(3).csv` (3,207 rows, 62 columns, SHA-256 `a51d6d791e034922fdf1751ba24e98f9c1ad3997f61f968700f7107bc1acada6`)
- **Result:** approximately 60 mA per selected cell / active channel; indirect matched-state estimate, not a manufacturer specification.

## Quoted reference: Observed practical imbalance

- **Reference PDF:** `report/dyness_balancing_cycle_projection_report_with_bleeder_hours.pdf`
- **SHA-256:** `8eac7d25ae654babeb66347a2a87693a94329f15c5d25b0514f665b4ca99fcc8`
- **Quoted projection:** “Best working estimate: about 20-21 comparable balancing cycles, corresponding to about 21-22 cumulative effective cell-7 bleeder hours.”
- This document is included unchanged as the author's quoted companion measurement report. Its headline result is quoted in the main report without duplicating the full derivation.

## DOI workflow
Reserve the DOI in the Zenodo draft before publishing. Insert that reserved DOI into the PDF title page and all machine-readable metadata, then upload the definitive files and publish only after author approval.

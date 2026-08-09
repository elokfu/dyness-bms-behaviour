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

A Dyness Powerbrick Pro 14.3 kWh battery with a 16-cell Dyness BMS running battery software version 2.50-71.10.11 was experimentally characterized using continuous telemetry of cell voltages, battery current, SOC, CCL, charge-permission state, raw status bytes and BMS temperature. Cells 1-15 are transmitted directly and cell 16 is reconstructed from pack voltage minus the sum of cells 1-15. The observations separate passive balancing, communication-level charge control and physical charge-MOSFET protection. Balancing is enabled at a battery charge current of 1.5 A and disabled at 1.4 A, with a 30 s qualification time retained as an engineering hypothesis. Individual balancing resistors are selected when a cell is 30 mV above the minimum cell. At 3.5 V maximum cell voltage the BMS enters full state, reports SOC 100 %, CCL 0 A and Charge Enabled false while the charge MOSFET remains on. Balancing continues in the 3.5-3.6 V region if its current and cell-delta criteria remain fulfilled. At 3.6 V the charge MOSFET opens; after the highest cell falls below 3.5 V the MOSFET closes again. CCL returns to 56 A when SOC changes from 100 % to 99 %.

- **Keywords:** Dyness, Dyness BMS, battery management system, LiFePO4, passive balancing, cell balancing, BMS balancing algorithm, CCL, Charge Current Limit, charge MOSFET, charge FET, SOC, RS485, CAN, Victron, DVCC, cell voltage, firmware 2.50-71.10.11, PowerBrick
- **Access:** Open
- **License:** CC BY 4.0 (author confirmed)
- **Publisher:** Zenodo (default after deposit)
- **Related identifier - source code/data:** https://github.com/elokfu/dyness-bms-behaviour
- **Related identifier - web version:** https://elokfu.github.io/dyness-bms-behaviour/

## DOI workflow
Reserve the DOI in the Zenodo draft before publishing. Insert that reserved DOI into the PDF title page and all machine-readable metadata, then upload the definitive files and publish only after author approval.

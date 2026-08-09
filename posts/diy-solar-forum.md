# Suggested title
Dyness BMS reverse-characterization: balancing 1.5 A / 30 mV, full at 3.5 V, charge MOSFET cutoff at 3.6 V

# Post
I have published an experimental report on Dyness BMS behaviour (battery software **2.50-71.10.11**) with raw CSV evidence.

The short version is:

- balancing enable: **Ibat >= 1.5 A**
- balancing disable: **Ibat <= 1.4 A**
- working timing hypothesis: **30 s qualification**
- cell resistor selection: **Vcell >= Vmin + 30 mV**
- full detection: **Vmax = 3.5 V** -> SOC 100 %, CCL 0 A, Charge Enabled false
- charge MOSFET remains ON at the 3.5 V full threshold
- balancing can continue between **3.5 and 3.6 V**
- charge MOSFET OFF: **Vmax = 3.6 V**
- charge MOSFET ON again: **Vmax < 3.5 V**
- CCL returns to **56 A** when SOC changes from 100 % to 99 %

The report also documents that the pack is 16S: cells 1-15 are direct telemetry and cell 16 is reconstructed from pack voltage in the CSV.

Report: https://elokfu.github.io/dyness-bms-behaviour/
DOI: 10.5281/zenodo.21860970
Raw data/source: https://github.com/elokfu/dyness-bms-behaviour

These are experimental observations for firmware 2.50-71.10.11, not official Dyness specifications. I am especially interested in comparable logs from other firmware versions.

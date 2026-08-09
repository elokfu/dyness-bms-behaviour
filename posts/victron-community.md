# Suggested title
Dyness Powerbrick Pro 14.3 kWh BMS balancing algorithm measured: 1.5 A current gate, 30 mV cell delta, CCL and charge-MOSFET behaviour

# Post
I have published a detailed experimental characterization of a Dyness Powerbrick Pro 14.3 kWh BMS running battery software **2.50-71.10.11**. The report is based on continuous RS485 telemetry and controlled charge-current experiments rather than manufacturer firmware documentation.

Main observed results:

- Passive balancing globally enables at **1.5 A** battery charging current and disables at **1.4 A**. A **30 s qualification time** is my engineering hypothesis from the observed transition timing.
- Once balancing is enabled, an individual cell's balancing resistor is selected at **Vcell - Vmin >= 30 mV**.
- The accompanying matched-state calculation estimates **approximately 60 mA per selected cell / active balancing channel** (roughly **50-70 mA** as a conservative interpretation range), not a manufacturer specification.
- The battery has **16 physical cells**. Cells 1-15 are transmitted directly; cell 16 is reconstructed in the logger from pack voltage minus the sum of cells 1-15.
- At **Vmax = 3.5 V**, the BMS sets the full state: **SOC = 100 %, CCL = 0 A, Charge Enabled = false**.
- CCL = 0 A does **not** open the physical charge MOSFET. Current can still physically flow if the external charger ignores CCL.
- Passive balancing continues in the **3.5-3.6 V** region when its current and cell-delta conditions remain fulfilled.
- At **Vmax = 3.6 V**, the BMS opens the charge MOSFET and physically interrupts charging.
- After the overvoltage cutoff at approximately **3.60 V**, the charge MOSFET is permanently reset below approximately **3.45 V**, independent of discharge current; the protection hysteresis is approximately **150 mV**.
- Normal communication-level charging permission returns separately when SOC falls from **100 % to 99 %**, at which point CCL returns to **56 A**.
- No explicit passive-balancing bit was found in the decoded status bytes. The full/high-cell transition does change `status3` from `0x80` to `0x88`.

The report includes the UML state-machine model, raw CSV measurements and the analysis figures so the conclusions can be checked independently.

**Canonical report:** https://elokfu.github.io/dyness-bms-behaviour/
**DOI:** 10.5281/zenodo.21860970
**Data / source repository:** https://github.com/elokfu/dyness-bms-behaviour

Important: values are experimentally observed for the tested firmware and are not presented as official Dyness specifications. The report also explains why deliberately charging between 3.5 and 3.6 V is not recommended even though balancing continues there: doing so ignores the BMS request CCL = 0 A and could have warranty implications.

I would be interested in measurements from other Dyness firmware versions to see whether these thresholds and timing are firmware-dependent.

# ⚡ EPCS Specification 03: Hardware Components & Hydraulic Loop
**Document ID:** EPCS-SPEC-03  
**Author:** Steve Campbell (KL8T)  
**License:** CERN-OHL-S-2.0 (Hardware) / CC BY-SA 4.0 (Docs)  
**Status:** Open Standard / Public Specification  

---

## 1. Electrochemical Core (VRFB Stack)
* **Vanadium Electrolyte:** Aqueous $V^{2+}/V^{3+}$ (anolyte) and $VO^{2+}/VO_{2}^{+}$ (catholyte) solutions in sulfuric acid carrier fluid.
* **Proton Exchange Membrane (PEM):** High-selectivity fluoropolymer ion-exchange membrane (e.g., Nafion or custom ion-exchange membrane).
* **Graphite Felt Electrodes & Bipolar Plates:** Highly conductive, acid-resistant current collectors and flow-field plates.

## 2. Thermal & Hydraulic Loop (The "Blood Circulatory" System)
* **Electrolyte Storage Tanks:** Chemically inert (HDPE/PVDF) dual-reservoir storage vessels.
* **Variable-Speed Chemical Pumps:** Magnetic-drive, seal-less acid pumps.
* **Direct-to-Chip Cold Plates:** Microchannel cooling blocks attached directly to server silicon heat loads.
* **Sensors & Telemetry:** Flow meters, pH sensors, thermocouples, and inline pressure transducers.

## 3. Power Electronics & Control
* **Bidirectional DC-DC Converters:** Manages charge/discharge voltage to server bus bars.
* **BMS / Microcontroller:** (e.g., ESP32, Raspberry Pi, or PLC) reading telemetry and dynamically adjusting pump speeds via analytical models in `02_Thermal_Power_Analysis/`.
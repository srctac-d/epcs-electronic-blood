# EPCS: Direct-DC "Electronic Blood" Power & Cooling Architecture
**Open Hardware Specification & Reference Design**  
*A modular, EMP-hardened, point-of-load electrochemical power and thermal management system for high-density compute.*

---

## 🏛️ Executive Overview

Modern AI workloads and high-performance computing (HPC) face two existential bottlenecks:
1. **The Transformer Delay & Energy Tax:** Traditional AC-to-DC conversion and multi-stage copper stepping incur severe energy losses (15%+) and multi-year lead times for grid transformers.
2. **The Thermal Wall:** Cooling high-density silicon with air or passive external liquid plates creates a "thermal tax" where massive amounts of energy are wasted simply trying to pull heat away from the chips.

The **Electrochemical Power & Cooling System (EPCS)**—nicknamed **"Electronic Blood"**—solves both issues simultaneously. By replacing traditional copper-wound transformers and isolated cooling loops with a single, dual-purpose **Vanadium Redox Flow ($V^{2+}/V^{3+}$ and $VO^{2+}/VO_{2}^{+}$)** fluid circuit, EPCS delivers point-of-load DC power directly at the chip substrate while actively removing waste heat.

---

## 🩸 The "Electronic Blood" Hemodynamic Model

Applying hemodynamic biological principles to computing infrastructure redefines how power and cooling interact:

* **Dual-Action Carrier Fluid:** Liquid vanadium electrolyte serves as both the electrochemical energy carrier and the primary thermal transport fluid.
* **Direct-to-Chip Circulation:** Electrolyte is pumped through direct-to-substrate microchannel cold plates, continuously cooling silicon while providing stable DC power buffering.
* **Decoupled Capacity:** Power output (stack footprint) and energy capacity (electrolyte volume in tanks) scale independently, enabling ultra-dense rack configurations.

---

## 📂 Repository Navigation

For complete architectural details, calculation models, and component specs, consult the directory index:

* `INDEX.md` — Full directory matrix & file index.
* `01_Architecture_Specs/` — Mechanical, electrical, and subterranean utilidor specifications.
* `02_Thermal_Power_Analysis/` — Analytical flow rate & sizing calculator scripts.

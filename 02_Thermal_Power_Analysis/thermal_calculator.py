#!/usr/bin/env python3
"""
EPCS "Electronic Blood" Thermal & Power Flow Rate Calculator
Author: Steve Campbell (KL8T)
"""

def calculate_epcs_parameters(rack_power_kw: float = 100.0, delta_t_c: float = 15.0):
    SPECIFIC_HEAT_J_KG_C = 3150
    DENSITY_KG_L = 1.35
    heat_dissipation_kw = rack_power_kw * 0.95
    mass_flow_rate_kg_s = (heat_dissipation_kw * 1000) / (SPECIFIC_HEAT_J_KG_C * delta_t_c)
    volumetric_flow_l_min = (mass_flow_rate_kg_s / DENSITY_KG_L) * 60
    print(f"Required Flow Rate: {volumetric_flow_l_min:.2f} L/min")

if __name__ == "__main__":
    calculate_epcs_parameters()

#!/usr/bin/env python3
"""
EPCS "Electronic Blood" Thermal & Power Flow Rate Calculator
Author: Steve Campbell (KL8T)
Repository: https://github.com/srctac-d/epcs-electronic-blood

Description:
    Calculates required Vanadium Redox Flow Battery (VRFB) electrolyte flow rates 
    and minimum reservoir storage volumes to simultaneously supply point-of-load 
    DC power (0.8V - 1.2V) and absorb waste heat from high-density compute racks.
"""

def calculate_epcs_parameters(rack_power_kw: float, delta_t_c: float = 15.0):
    """
    Calculates electrolyte volumetric flow rates and reservoir sizing.
    
    Parameters:
        rack_power_kw (float): Total compute load per rack or pod in kW.
        delta_t_c (float): Allowed temperature rise across the microfluidic manifold (°C).
                           Default is 15°C (e.g., 30°C inlet -> 45°C outlet).
    """
    # Physical Constants for Vanadium Electrolyte (Approx. 1.6M V in H2SO4)
    SPECIFIC_HEAT_J_KG_C = 3150  # Specific heat capacity in Joules / (kg * °C)
    DENSITY_KG_L = 1.35          # Density in kg per Liter
    ENERGY_DENSITY_WH_L = 25.0    # Typical VRFB energy density in Wh/L

    # 1. Thermal Management Math
    # Heat energy to remove (Joules per second) assuming ~92% system efficiency
    # 8% converted to waste heat, plus direct silicon thermal dissipation.
    heat_dissipation_kw = rack_power_kw * 0.95  # 95% of total draw converted to heat
    heat_joules_per_sec = heat_dissipation_kw * 1000

    # Flow rate (kg/s) = Heat (J/s) / (Specific Heat * Delta T)
    mass_flow_rate_kg_s = heat_joules_per_sec / (SPECIFIC_HEAT_J_KG_C * delta_t_c)
    
    # Volumetric Flow Rate
    volumetric_flow_l_s = mass_flow_rate_kg_s / DENSITY_KG_L
    volumetric_flow_l_min = volumetric_flow_l_s * 60
    volumetric_flow_gpm = volumetric_flow_l_min * 0.264172

    # 2. Electrochemical Power Storage Math (4-Hour Passive Inertia Target)
    required_kwh = rack_power_kw * 4.0
    required_liters = (required_kwh * 1000) / ENERGY_DENSITY_WH_L
    required_gallons = required_liters * 0.264172

    # Print Output Summary
    print(f"\n=======================================================")
    print(f"  EPCS 'ELECTRONIC BLOOD' SYSTEM CALCULATIONS")
    print(f"=======================================================")
    print(f"Compute Rack Load Input      : {rack_power_kw:.2f} kW")
    print(f"Target Delta-T Across Rack   : {delta_t_c:.1f} °C")
    print(f"-------------------------------------------------------")
    print(f"REQUIRED COOLING FLOW RATE   :")
    print(f"  * Liters / Minute          : {volumetric_flow_l_min:.2f} L/min")
    print(f"  * Gallons / Minute (GPM)   : {volumetric_flow_gpm:.2f} GPM")
    print(f"-------------------------------------------------------")
    print(f"RESERVOIR SIZING (4-Hr Passive Thermal/Power Inertia):")
    print(f"  * Required Electrolyte     : {required_liters:,.0f} Liters")
    print(f"  * Required Electrolyte     : {required_gallons:,.0f} Gallons")
    print(f"=======================================================\n")

if __name__ == "__main__":
    import sys
    print("EPCS Flow Rate & Thermal Calculator v1.0")
    
    # Allow command line argument for kW, or default to standard 100 kW AI Rack Pod
    if len(sys.argv) > 1:
        try:
            input_kw = float(sys.argv[1])
        except ValueError:
            print("Invalid input. Defaulting to 100 kW rack pod.")
            input_kw = 100.0
    else:
        input_kw = 100.0  # Default 100 kW High-Density Compute Pod

    calculate_epcs_parameters(rack_power_kw=input_kw)

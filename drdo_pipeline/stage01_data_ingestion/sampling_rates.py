# DRDO Stage 1 – Data Ingestion
# MIL-STD-2124A Category II (F/A/T) – Sampling Rates
# Source: Table II, MIL-STD-2124A

SAMPLING_RATES_HZ = {
    # Flight profile
    "altitude_barometric_ft": 1,
    "airspeed_kts": 1,
    "heading_deg": 4,
    "angle_of_attack": 4,

    # Attitude
    "pitch_deg": 4,
    "roll_deg": 8,
    "yaw_deg": 1,

    # Acceleration
    "accel_vertical_g": 8,
    "accel_longitudinal_g": 2,
    "accel_lateral_g": 4,

    # Engine
    "rpm_n1_pct": 1,
    "rpm_n2_pct": 1,
    "exhaust_gas_temp_c": 1,
    "fuel_flow_kgph": 1,
    "fuel_quantity_kg": 1,

    # Controls
    "rudder_pct": 4,
    "aileron_pct": 4,
    "elevator_pct": 4,

    # Discrete (event / low-rate)
    "master_warning": 0.5
}

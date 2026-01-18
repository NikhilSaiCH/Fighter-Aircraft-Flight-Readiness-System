# DRDO Stage 2 – Data Transformation & Feature Engineering
# Tool: Pandas
# MIL-STD-2124A Category II Canonical Schema

CANONICAL_SCHEMA = [
    # Time
    "timestamp",

    # Flight profile
    "altitude_barometric_ft",
    "airspeed_kts",
    "heading_deg",
    "angle_of_attack",

    # Attitude
    "pitch_deg",
    "roll_deg",
    "yaw_deg",

    # Acceleration
    "accel_vertical_g",
    "accel_longitudinal_g",
    "accel_lateral_g",

    # Engine
    "rpm_n1_pct",
    "rpm_n2_pct",
    "exhaust_gas_temp_c",
    "fuel_flow_kgph",
    "fuel_quantity_kg",

    # Controls
    "rudder_pct",
    "aileron_pct",
    "elevator_pct",

    # Discrete
    "master_warning"
]

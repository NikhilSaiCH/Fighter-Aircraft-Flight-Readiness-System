"""
Sampling expectations for Category II fighter aircraft.
These are used for governance & analytics assumptions.
"""

SAMPLING_RULES_HZ = {
    "timestamp": 1.0,  # minimum 1 Hz for analytics

    # High-dynamics parameters
    "accel_vertical_g": 10.0,
    "accel_lateral_g": 10.0,
    "accel_longitudinal_g": 10.0,

    # Engine parameters
    "rpm_n1_pct": 5.0,
    "exhaust_gas_temp_c": 5.0,

    # Air data
    "airspeed_kts": 2.0,
    "altitude_barometric_ft": 1.0,
}

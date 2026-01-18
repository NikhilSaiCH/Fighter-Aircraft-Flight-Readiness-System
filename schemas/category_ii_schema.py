"""
MIL-STD-2124A
Category II – Fighter / Attack Aircraft
Authoritative parameter schema
"""

CATEGORY_II_SCHEMA = {
    "timestamp": {"type": "numeric", "required": True},

    # Air data
    "airspeed_kts": {"type": "numeric", "min": 0, "max": 1200},
    "altitude_barometric_ft": {"type": "numeric", "min": -1000, "max": 60000},

    # Attitude
    "pitch_deg": {"type": "numeric", "min": -90, "max": 90},
    "roll_deg": {"type": "numeric", "min": -180, "max": 180},
    "yaw_deg": {"type": "numeric", "min": 0, "max": 360},

    # Accelerations (Category II critical)
    "accel_longitudinal_g": {"type": "numeric", "min": -5, "max": 10},
    "accel_lateral_g": {"type": "numeric", "min": -5, "max": 10},
    "accel_vertical_g": {"type": "numeric", "min": -5, "max": 10},

    # Engine parameters
    "rpm_n1_pct": {"type": "numeric", "min": 0, "max": 110},
    "exhaust_gas_temp_c": {"type": "numeric", "min": 0, "max": 1000},
    "fuel_flow_kgph": {"type": "numeric", "min": 0, "max": 10000},
    "oil_pressure_psi": {"type": "numeric", "min": 0, "max": 200},
    "oil_temp_c": {"type": "numeric", "min": -40, "max": 200},

    # Warnings
    "engine_warning": {"type": "boolean"},
    "overheat_warning": {"type": "boolean"},
    "flight_control_warning": {"type": "boolean"},
}

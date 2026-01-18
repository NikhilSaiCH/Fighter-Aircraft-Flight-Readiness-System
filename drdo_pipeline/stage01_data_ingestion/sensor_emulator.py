# DRDO Stage 1 – Data Ingestion
# Tool: Apache NiFi (Emulated)
# MIL-STD-2124A Category II Fighter/Attack Aircraft
# Sampling-rate enforced sensor emission

import random
import time
from .sampling_rates import SAMPLING_RATES_HZ



class FighterAircraftSensorEmulator:
    """
    Emits Category II aircraft sensor data
    strictly respecting MIL-STD-2124A sampling rates
    """

    def __init__(self):
        self.last_emitted = {
            key: 0.0 for key in SAMPLING_RATES_HZ
        }

    def _should_emit(self, param, now):
        rate = SAMPLING_RATES_HZ[param]
        period = 1.0 / rate
        return (now - self.last_emitted[param]) >= period

    def read_sensors(self):
        now = time.time()
        frame = {"timestamp": now}

        def emit(param, value):
            frame[param] = value
            self.last_emitted[param] = now

        # Flight profile
        if self._should_emit("altitude_barometric_ft", now):
            emit("altitude_barometric_ft", random.uniform(0, 50000))

        if self._should_emit("airspeed_kts", now):
            emit("airspeed_kts", random.uniform(120, 1500))

        if self._should_emit("heading_deg", now):
            emit("heading_deg", random.uniform(0, 360))

        if self._should_emit("angle_of_attack", now):
            emit("angle_of_attack", random.uniform(-10, 30))

        # Attitude
        if self._should_emit("pitch_deg", now):
            emit("pitch_deg", random.uniform(-90, 90))

        if self._should_emit("roll_deg", now):
            emit("roll_deg", random.uniform(-180, 180))

        if self._should_emit("yaw_deg", now):
            emit("yaw_deg", random.uniform(-180, 180))

        # Acceleration
        if self._should_emit("accel_vertical_g", now):
            emit("accel_vertical_g", random.uniform(-6, 15))

        if self._should_emit("accel_longitudinal_g", now):
            emit("accel_longitudinal_g", random.uniform(-6, 2))

        if self._should_emit("accel_lateral_g", now):
            emit("accel_lateral_g", random.uniform(-4, 4))

        # Engine
        if self._should_emit("rpm_n1_pct", now):
            emit("rpm_n1_pct", random.uniform(60, 110))

        if self._should_emit("rpm_n2_pct", now):
            emit("rpm_n2_pct", random.uniform(60, 110))

        if self._should_emit("exhaust_gas_temp_c", now):
            emit("exhaust_gas_temp_c", random.uniform(400, 900))

        if self._should_emit("fuel_flow_kgph", now):
            emit("fuel_flow_kgph", random.uniform(500, 6000))

        if self._should_emit("fuel_quantity_kg", now):
            emit("fuel_quantity_kg", random.uniform(500, 8000))

        # Controls
        if self._should_emit("rudder_pct", now):
            emit("rudder_pct", random.uniform(-100, 100))

        if self._should_emit("aileron_pct", now):
            emit("aileron_pct", random.uniform(-100, 100))

        if self._should_emit("elevator_pct", now):
            emit("elevator_pct", random.uniform(-100, 100))

        # Discrete
        if self._should_emit("master_warning", now):
            emit("master_warning", random.choice([0, 1]))

        return frame

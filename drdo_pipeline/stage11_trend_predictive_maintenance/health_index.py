# DRDO Stage 11 – Trend Monitoring & Predictive Maintenance
# Tool: Time-series analytics (DRDO-compliant)
# Responsibility: Health index computation

import numpy as np


class HealthIndexCalculator:
    """
    Computes normalized health indices for aircraft subsystems
    """

    def compute_engine_health(self, df):
        """
        Engine health index based on thermal & RPM stress
        Higher = healthier
        """
        egt_norm = df["exhaust_gas_temp_c"] / df["exhaust_gas_temp_c"].max()
        rpm_norm = df["rpm_n1_pct"] / df["rpm_n1_pct"].max()

        stress = 0.6 * egt_norm + 0.4 * rpm_norm
        health_index = 1.0 - stress

        return health_index.clip(0, 1)

    def compute_flight_envelope_health(self, df):
        """
        Flight envelope stress indicator
        """
        g_load = abs(df["accel_vertical_g"]) / abs(df["accel_vertical_g"]).max()
        aoa = abs(df["angle_of_attack"]) / abs(df["angle_of_attack"]).max()

        stress = 0.5 * g_load + 0.5 * aoa
        return (1.0 - stress).clip(0, 1)

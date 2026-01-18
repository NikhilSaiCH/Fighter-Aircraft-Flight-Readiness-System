import numpy as np

class HealthIndexCalculator:
    """
    Computes interpretable subsystem health indices
    """

    def engine_health(self, df):
        thermal_health = 1 - (df["exhaust_gas_temp_c"] / 1000)
        oil_health = df["oil_pressure_psi"] / df["oil_pressure_psi"].max()
        rpm_stability = 1 - df["rpm_n1_pct"].diff().abs().fillna(0) / 100

        health = (
            0.4 * thermal_health +
            0.3 * oil_health +
            0.3 * rpm_stability
        )

        return health.clip(0, 1)

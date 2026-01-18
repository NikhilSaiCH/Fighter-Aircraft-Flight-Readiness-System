import pandas as pd
import numpy as np

class FeatureEngineer:
    """
    Derives analytics-ready features from
    MIL-STD-2124A Category II parameters
    """

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        features = pd.DataFrame()
        features["timestamp"] = df["timestamp"]

        # ---------- ENGINE FEATURES ----------
        features["thermal_margin"] = 950 - df["exhaust_gas_temp_c"]
        features["rpm_egt_ratio"] = (
            df["rpm_n1_pct"] / (df["exhaust_gas_temp_c"] + 1)
        )

        features["oil_pressure_norm"] = (
            df["oil_pressure_psi"] / df["oil_pressure_psi"].max()
        )

        features["fuel_efficiency"] = (
            df["rpm_n1_pct"] / (df["fuel_flow_kgph"] + 1)
        )

        # ---------- FLIGHT ENVELOPE ----------
        features["g_total"] = np.sqrt(
            df["accel_longitudinal_g"] ** 2 +
            df["accel_lateral_g"] ** 2 +
            df["accel_vertical_g"] ** 2
        )

        features["g_exceedance"] = (features["g_total"] > 9).astype(int)

        # ---------- CONTROL & STABILITY ----------
        features["vertical_g_variance"] = (
            df["accel_vertical_g"].rolling(20).std().fillna(0)
        )

        return features

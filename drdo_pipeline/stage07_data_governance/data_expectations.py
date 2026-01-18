# DRDO Stage 7 – Data Governance, Catalog & Lineage
# Tool: Great Expectations–class Data Quality Rules (Emulated)

import pandas as pd


class DataExpectations:
    """
    Defines and validates data quality expectations
    """

    def validate_schema(self, df: pd.DataFrame, expected_columns: list) -> dict:
        missing = [c for c in expected_columns if c not in df.columns]
        unexpected = [c for c in df.columns if c not in expected_columns]

        return {
            "schema_valid": len(missing) == 0,
            "missing_columns": missing,
            "unexpected_columns": unexpected
        }

    def validate_ranges(self, df: pd.DataFrame) -> dict:
        """
        Domain sanity checks for fighter aircraft parameters
        """
        results = {}

        if "airspeed_kts" in df.columns:
            results["airspeed_valid"] = df["airspeed_kts"].between(0, 2000).all()

        if "altitude_barometric_ft" in df.columns:
            results["altitude_valid"] = df["altitude_barometric_ft"].between(-1000, 80000).all()

        if "accel_vertical_g" in df.columns:
            results["accel_valid"] = df["accel_vertical_g"].between(-10, 20).all()

        return results

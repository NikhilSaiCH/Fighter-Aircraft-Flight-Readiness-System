# DRDO Stage 2 – Data Transformation & Feature Engineering
# Tool: Pandas
# Baseline-relative normalization (MIL-STD compliant)

import pandas as pd


def normalize_against_baseline(df: pd.DataFrame, baseline: dict) -> pd.DataFrame:
    """
    Normalize numeric columns relative to baseline values.
    Discrete fields are left unchanged.
    """
    normalized = df.copy()

    for col in df.columns:
        if col not in baseline:
            continue

        if pd.api.types.is_numeric_dtype(df[col]):
            base = baseline[col]
            if base is not None and base != 0:
                normalized[col] = (df[col] - base) / abs(base)

    return normalized

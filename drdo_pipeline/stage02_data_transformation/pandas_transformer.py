# DRDO Stage 2 – Data Transformation & Feature Engineering
# Tool: Pandas (Strict)
# Consumes Stage 1 output only

import pandas as pd
from .schema_definition import CANONICAL_SCHEMA
from .normalization import normalize_against_baseline



class PandasTransformer:
    """
    Implements DRDO Stage 2 using Pandas only
    """

    def __init__(self):
        self.df = pd.DataFrame(columns=CANONICAL_SCHEMA)

    def ingest_stage1_output(self, stage1_packet: dict):
        """
        Converts sparse Stage 1 frame into structured row
        """
        sensor_data = stage1_packet["sensor_data"]
        row = {}

        for field in CANONICAL_SCHEMA:
            row[field] = sensor_data.get(field, None)

        self.df = pd.concat(
            [self.df, pd.DataFrame([row])],
            ignore_index=True
        )

    def clean(self):
        """
        Forward-fill to handle multi-rate sparsity
        """
        self.df.sort_values("timestamp", inplace=True)
        self.df.ffill(inplace=True)

    def transform(self, baseline: dict) -> pd.DataFrame:
        """
        Full Stage 2 pipeline:
        - Cleaning
        - Normalization
        """
        self.clean()
        transformed = normalize_against_baseline(self.df, baseline)
        return transformed

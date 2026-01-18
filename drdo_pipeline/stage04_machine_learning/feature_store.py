# DRDO Stage 4 – Machine Learning & Feature Store
# Tool: scikit-learn (Feature Store support)
# Responsibility: Store and serve feature matrices

class FeatureStore:
    """
    Simple in-memory feature store.
    Acts as the Feature Store referenced in DRDO Stage 4.
    """

    def __init__(self):
        self.features = None
        self.feature_names = None

    def save(self, dataframe):
        self.features = dataframe.values
        self.feature_names = list(dataframe.columns)

    def load(self):
        return self.features, self.feature_names

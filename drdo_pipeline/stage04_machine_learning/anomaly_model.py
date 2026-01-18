# DRDO Stage 4 – Machine Learning & Feature Store
# Tool: scikit-learn
# Unsupervised anomaly detection for Category II aircraft

from sklearn.ensemble import IsolationForest


class AircraftAnomalyModel:
    """
    Trains an Isolation Forest on transformed flight data
    """

    def __init__(self, contamination=0.01, random_state=42):
        self.model = IsolationForest(
            n_estimators=100,
            contamination=contamination,
            random_state=random_state
        )
        self.trained = False

    def train(self, feature_matrix):
        self.model.fit(feature_matrix)
        self.trained = True

    def score(self, feature_matrix):
        if not self.trained:
            raise RuntimeError("Model must be trained before scoring")
        # Higher score = more normal, lower = anomalous
        return self.model.decision_function(feature_matrix)

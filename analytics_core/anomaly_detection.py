from sklearn.ensemble import IsolationForest

class AnomalyDetector:
    """
    Unsupervised anomaly detection
    for fighter aircraft data
    """

    def __init__(self):
        self.model = IsolationForest(
            n_estimators=150,
            contamination=0.03,
            random_state=42
        )

    def fit_predict(self, feature_df):
        scores = self.model.fit_predict(feature_df)
        anomaly_score = self.model.decision_function(feature_df)
        return scores, anomaly_score

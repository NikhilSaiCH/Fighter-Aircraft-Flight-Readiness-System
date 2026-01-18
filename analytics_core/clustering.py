from sklearn.cluster import KMeans

class FlightRegimeClustering:
    """
    Identifies operating regimes
    (normal, aggressive, abnormal)
    """

    def cluster(self, feature_df, n_clusters=3):
        model = KMeans(
            n_clusters=n_clusters,
            random_state=42,
            n_init=10
        )
        return model.fit_predict(feature_df)

# DRDO Stage 9 – Clustering & Streaming AI Analytics
# Tool: Mini-Batch K-Means
# Responsibility: Streaming-aware maintenance clustering

import numpy as np
from sklearn.cluster import MiniBatchKMeans
from .cluster_state import ClusterState



class StreamingMaintenanceClusterer:
    """
    Performs incremental clustering on streaming flight data
    """

    def __init__(self, n_clusters=3, batch_size=20, random_state=42):
        self.model = MiniBatchKMeans(
            n_clusters=n_clusters,
            batch_size=batch_size,
            random_state=random_state
        )
        self.state = ClusterState()
        self.initialized = False

    def process_batch(self, feature_batch):
        """
        feature_batch: numpy array (batch_size x num_features)
        """
        if not self.initialized:
            self.model.partial_fit(feature_batch)
            self.initialized = True
        else:
            self.model.partial_fit(feature_batch)

        labels = self.model.predict(feature_batch)
        self.state.update(self.model.cluster_centers_, labels.tolist())

        return labels

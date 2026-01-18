# DRDO Stage 9 – Clustering & Streaming AI Analytics
# Tool: Mini-Batch K-Means (scikit-learn)
# Responsibility: Cluster state & centroids

class ClusterState:
    """
    Stores cluster centroids and assignments
    """

    def __init__(self):
        self.centroids = None
        self.labels = []

    def update(self, centroids, labels):
        self.centroids = centroids
        self.labels.extend(labels)

    def get_state(self):
        return {
            "centroids": self.centroids,
            "labels": self.labels
        }

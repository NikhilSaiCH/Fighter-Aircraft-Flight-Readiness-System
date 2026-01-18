# DRDO Stage 7 – Data Governance, Catalog & Lineage
# Tool: Data Catalog & Lineage (Emulated)

class LineageTracker:
    """
    Tracks dataset lineage across DRDO stages
    """

    def __init__(self):
        self.lineage = []

    def register_dataset(self, dataset_name: str, source_stage: str, description: str):
        self.lineage.append({
            "dataset": dataset_name,
            "source_stage": source_stage,
            "description": description
        })

    def get_lineage(self):
        return self.lineage

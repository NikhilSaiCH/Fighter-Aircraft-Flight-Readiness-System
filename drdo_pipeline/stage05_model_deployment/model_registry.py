# DRDO Stage 5 – Model Deployment & MLOps
# Tool: FastAPI (Emulated)
# Responsibility: Model lifecycle & versioning

class ModelRegistry:
    """
    Lightweight offline model registry.
    """

    def __init__(self):
        self.model = None
        self.model_version = None
        self.metadata = {}

    def register(self, model, version: str, metadata: dict):
        self.model = model
        self.model_version = version
        self.metadata = metadata

    def get_model(self):
        if self.model is None:
            raise RuntimeError("No model registered")
        return self.model

    def get_info(self):
        return {
            "version": self.model_version,
            "metadata": self.metadata
        }

# DRDO Stage 1 – Data Ingestion
# MIL-STD-2124A §3.7 Baseline Data

class BaselineBuffer:
    def __init__(self):
        self.baseline = None

    def capture(self, sensor_frame):
        if self.baseline is None:
            self.baseline = sensor_frame.copy()

    def get(self):
        return self.baseline


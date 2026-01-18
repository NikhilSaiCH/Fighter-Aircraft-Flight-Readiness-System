import numpy as np

class TrendAnalyzer:
    """
    Detects degradation trends
    """

    def compute_trend(self, signal):
        x = np.arange(len(signal))
        slope = np.polyfit(x, signal, 1)[0]
        return slope

    def classify_trend(self, slope):
        if slope < -0.0005:
            return "DEGRADING"
        elif slope > 0.0005:
            return "IMPROVING"
        else:
            return "STABLE"

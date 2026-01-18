# DRDO Stage 11 – Trend Monitoring & Predictive Maintenance
# Tool: Trend analysis / predictive maintenance analytics
# Responsibility: Degradation trend detection

import numpy as np
from sklearn.linear_model import LinearRegression


class TrendAnalyzer:
    """
    Detects degradation trends over time
    """

    def compute_trend_slope(self, timestamps, health_index):
        """
        Computes degradation slope using linear regression
        Negative slope => degradation
        """
        t = np.array(timestamps).reshape(-1, 1)
        h = np.array(health_index)

        model = LinearRegression()
        model.fit(t, h)

        return model.coef_[0]

    def summarize_trend(self, slope):
        """
        Interpretable trend summary (NO decision logic)
        """
        if slope < -1e-6:
            return "DEGRADING_TREND"
        elif slope > 1e-6:
            return "IMPROVING_TREND"
        else:
            return "STABLE_TREND"

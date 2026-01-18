# DRDO Stage 13 – Continuous Feedback Loop & Retraining
# Tool: Model monitoring / drift detection
# Responsibility: Drift detection ONLY

import numpy as np


class DriftMonitor:
    """
    Detects statistical drift in model inputs or outputs
    """

    def compute_distribution_shift(self, baseline_values, current_values):
        """
        Computes normalized mean shift
        """
        baseline_mean = np.mean(baseline_values)
        current_mean = np.mean(current_values)

        if baseline_mean == 0:
            return 0.0

        return abs(current_mean - baseline_mean) / abs(baseline_mean)

    def detect_drift(self, baseline_values, current_values, threshold=0.2):
        """
        Returns drift flag and magnitude
        """
        shift = self.compute_distribution_shift(
            baseline_values, current_values
        )
        return {
            "drift_detected": shift > threshold,
            "shift_magnitude": shift
        }

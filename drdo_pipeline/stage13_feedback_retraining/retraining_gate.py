# DRDO Stage 13 – Continuous Feedback Loop & Retraining
# Tool: Controlled retraining governance
# Responsibility: Human approval gate ONLY

class RetrainingGate:
    """
    Controls retraining recommendations (NO automatic retraining)
    """

    def evaluate(self, drift_report: dict):
        if drift_report["drift_detected"]:
            return {
                "retraining_recommended": True,
                "reason": f"Detected distribution shift of {drift_report['shift_magnitude']:.2f}"
            }
        else:
            return {
                "retraining_recommended": False,
                "reason": "No significant drift detected"
            }

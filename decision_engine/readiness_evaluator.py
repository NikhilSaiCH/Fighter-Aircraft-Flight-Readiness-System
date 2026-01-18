import numpy as np


class FlightReadinessEvaluator:
    """
    Final decision engine for fighter aircraft flight readiness.
    Calibrated to distinguish healthy variance from real degradation.
    """

    def evaluate(
        self,
        engine_health_index,
        anomaly_scores,
        trend_summary,
        governance_status,
        root_causes
    ):
        issues = []

        # ----------------- Governance -----------------
        if governance_status != "PASS":
            issues.append("Data governance validation failed")

        # ----------------- Anomaly Assessment -----------------
        # Isolation-based models always flag some anomalies.
        # Use ratio instead of absolute count.
        critical_anomalies = anomaly_scores < -0.3
        anomaly_ratio = critical_anomalies.sum() / len(anomaly_scores)

        if anomaly_ratio > 0.10:  # >10% is concerning
            issues.append("High frequency of critical anomalies detected")

        # ----------------- Engine Health -----------------
        avg_health = float(np.mean(engine_health_index))

        if avg_health < 0.65:
            issues.append("Low overall engine health index")

        # ----------------- Trend Assessment -----------------
        # Ignore trend for very short datasets
        if (
            trend_summary.get("trend") == "DEGRADING"
            and len(engine_health_index) > 300
        ):
            issues.append("Degrading performance trend detected")

        # ----------------- Root Cause -----------------
        if root_causes:
            issues.append("Underlying technical root causes identified")

        # ----------------- Final Decision -----------------
        if issues:
            status = "NOT READY FOR FLIGHT"
        else:
            status = "READY FOR FLIGHT"

        return {
            "status": status,
            "issues": issues,
            "summary": (
                "All systems operating within acceptable limits."
                if status == "READY FOR FLIGHT"
                else "Operational issues detected requiring attention."
            )
        }

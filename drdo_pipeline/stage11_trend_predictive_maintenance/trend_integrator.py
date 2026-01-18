class TrendIntegrator:
    """
    Integrates trend analysis
    into readiness & RCA context
    """

    def summarize(self, trend_label, health_index_mean):
        summary = {}

        summary["trend"] = trend_label
        summary["health_index"] = round(float(health_index_mean), 3)

        if trend_label == "DEGRADING" and health_index_mean < 0.7:
            summary["maintenance_risk"] = "HIGH"
        elif trend_label == "DEGRADING":
            summary["maintenance_risk"] = "MEDIUM"
        else:
            summary["maintenance_risk"] = "LOW"

        return summary

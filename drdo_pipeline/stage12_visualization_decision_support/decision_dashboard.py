# DRDO Stage 12 – Visualization & Decision Support
# Tool: Plotly
# Responsibility: Human decision-support visualization ONLY

import plotly.graph_objects as go


class DecisionSupportDashboard:
    """
    Integrates analytics, trends, and RCA outputs
    to support human decision-making.
    """

    def plot_health_trend(self, timestamps, health_index, subsystem_name):
        """
        Visualizes subsystem health over time
        """
        fig = go.Figure()
        fig.add_trace(
            go.Scatter(
                x=timestamps,
                y=health_index,
                mode="lines",
                name=f"{subsystem_name} Health Index"
            )
        )

        fig.update_layout(
            title=f"{subsystem_name} Health Trend (Decision Support)",
            xaxis_title="Time",
            yaxis_title="Health Index (0–1)",
            showlegend=True
        )
        return fig

    def plot_anomaly_vs_health(self, anomaly_scores, health_index):
        """
        Correlates instantaneous anomalies with long-term health
        """
        fig = go.Figure()
        fig.add_trace(
            go.Scatter(
                x=anomaly_scores,
                y=health_index,
                mode="markers",
                name="Anomaly vs Health"
            )
        )

        fig.update_layout(
            title="Anomaly Scores vs Health Index",
            xaxis_title="Anomaly Score (Higher = Normal)",
            yaxis_title="Health Index",
            showlegend=True
        )
        return fig

    def summarize_rca(self, rca_explanations):
        """
        Produces a textual RCA summary for human review
        """
        summary = []
        for chain in rca_explanations:
            chain_desc = " → ".join(
                [step["from"] for step in chain] + [chain[-1]["to"]]
            )
            summary.append(chain_desc)
        return summary

    def decision_context(self, trend_label):
        """
        Provides contextual cue (NOT a decision)
        """
        if trend_label == "DEGRADING_TREND":
            return "Observed degradation trend. Recommend closer monitoring."
        elif trend_label == "STABLE_TREND":
            return "Subsystem behavior appears stable."
        elif trend_label == "IMPROVING_TREND":
            return "Subsystem health improving."
        else:
            return "Trend status unavailable."

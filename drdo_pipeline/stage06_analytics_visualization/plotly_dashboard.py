# DRDO Stage 6 – Analytics, BI & Visualization
# Tool: Plotly
# Responsibility: Visual analytics ONLY

import plotly.graph_objects as go


class FlightAnalyticsDashboard:
    """
    Generates interactive Plotly-based analytics dashboards
    for Category II aircraft flight data
    """

    def plot_anomaly_timeline(self, timestamps, anomaly_scores):
        """
        Time-series visualization of anomaly scores
        """
        fig = go.Figure()
        fig.add_trace(
            go.Scatter(
                x=timestamps,
                y=anomaly_scores,
                mode="lines",
                name="Anomaly Score"
            )
        )

        fig.update_layout(
            title="Aircraft Health – Anomaly Score Timeline",
            xaxis_title="Time",
            yaxis_title="Anomaly Score (Higher = Normal)",
            showlegend=True
        )

        return fig

    def plot_flight_parameter(self, timestamps, values, parameter_name, unit):
        """
        Generic flight parameter visualization
        """
        fig = go.Figure()
        fig.add_trace(
            go.Scatter(
                x=timestamps,
                y=values,
                mode="lines",
                name=parameter_name
            )
        )

        fig.update_layout(
            title=f"{parameter_name} vs Time",
            xaxis_title="Time",
            yaxis_title=f"{parameter_name} ({unit})",
            showlegend=True
        )

        return fig

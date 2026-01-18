class RCAEngine:
    """
    Maps analytics & ML outputs
    to root causes using causal graph
    """

    def __init__(self, causal_graph):
        self.cg = causal_graph

    def analyze(self, analytics_summary):
        causes = set()

        # Engine stress
        if analytics_summary.get("high_egt", False):
            causes.add("High_EGT")

        if analytics_summary.get("rpm_instability", False):
            causes.add("High_RPM")

        # Lubrication
        if analytics_summary.get("low_oil_pressure", False):
            causes.add("Low_Oil_Pressure")

        # Structural stress
        if analytics_summary.get("high_g_events", 0) > 3:
            causes.add("High_G_Load")

        # Expand to root causes
        root_causes = set()
        for c in causes:
            root_causes.update(self.cg.find_root_causes(c))
            root_causes.add(c)

        return list(root_causes)

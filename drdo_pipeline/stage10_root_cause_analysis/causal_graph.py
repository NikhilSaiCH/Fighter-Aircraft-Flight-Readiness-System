import networkx as nx

class CausalGraph:
    """
    Graph-based Root Cause Analysis
    for fighter aircraft systems
    """

    def __init__(self):
        self.graph = nx.DiGraph()
        self._build_graph()

    def _build_graph(self):
        # Engine causal chain
        self.graph.add_edge("High_RPM", "High_EGT")
        self.graph.add_edge("High_EGT", "Thermal_Stress")
        self.graph.add_edge("Thermal_Stress", "ENGINE_OVERHEAT")

        # Lubrication chain
        self.graph.add_edge("Low_Oil_Pressure", "Engine_Wear")
        self.graph.add_edge("Engine_Wear", "ENGINE_DEGRADATION")

        # Flight envelope chain
        self.graph.add_edge("High_G_Load", "Structural_Stress")
        self.graph.add_edge("Structural_Stress", "AIRFRAME_RISK")

    def find_root_causes(self, observed_event):
        if observed_event not in self.graph:
            return []

        return list(nx.ancestors(self.graph, observed_event))

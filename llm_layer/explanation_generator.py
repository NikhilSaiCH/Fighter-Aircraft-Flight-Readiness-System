class LLMExplanationGenerator:
    """
    LLM explanation layer.
    Emulator version produces deterministic, data-aligned explanations.
    """

    def __init__(self, use_emulator=True):
        self.use_emulator = use_emulator

    def generate(self, prompt):
        if self.use_emulator:
            return self._emulator_response(prompt)

        # Placeholder for real LLM API
        return {
            "Explanation": "LLM integration pending.",
            "Defects": [],
            "Recommendations": []
        }

    def _emulator_response(self, prompt):
        # READY CASE
        if "READY FOR FLIGHT" in prompt:
            return {
                "Explanation": (
                    "All analyzed fighter aircraft parameters remain within "
                    "approved operational limits. No significant anomaly "
                    "patterns or degradation trends were detected. "
                    "The aircraft is assessed to be ready for flight."
                ),
                "Defects": [],
                "Recommendations": [
                    "Proceed with standard pre-flight inspection",
                    "Continue routine monitoring"
                ]
            }

        # NOT READY CASE
        return {
            "Explanation": (
                "Analysis indicates abnormal operational patterns and "
                "performance degradation that could affect safe flight. "
                "Corrective actions are recommended before clearance."
            ),
            "Defects": [
                "Engine performance anomalies detected",
                "Thermal or stress indicators outside nominal range",
                "Degradation trend observed"
            ],
            "Recommendations": [
                "Conduct detailed engine inspection",
                "Review operational and maintenance data",
                "Delay flight until issues are resolved"
            ]
        }

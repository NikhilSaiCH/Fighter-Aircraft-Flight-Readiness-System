class PromptBuilder:
    def build_prompt(self, readiness_output):
        status = readiness_output["status"]
        confidence = readiness_output.get("confidence", 0)

        issues = readiness_output.get("issues", [])
        recommendations = readiness_output.get("recommendations", [])

        if status == "READY":
            explanation = (
                "All analyzed fighter aircraft parameters remain within approved "
                "operational limits. No significant anomaly patterns or degradation "
                "trends were detected during the analysis window."
            )

            issues_text = "No critical issues detected."

            recommendations_text = (
                "Proceed with standard pre-flight inspection procedures. "
                "Continue routine condition monitoring as per maintenance guidelines."
            )

        else:  # NOT READY
            explanation = (
                "The analysis identified abnormal patterns and degradation trends "
                "in key fighter aircraft parameters, indicating that the aircraft "
                "is not currently fit for safe flight operations."
            )

            issues_text = (
                ", ".join(issues)
                if issues
                else "Multiple performance anomalies detected."
            )

            recommendations_text = (
                ", ".join(recommendations)
                if recommendations
                else "Conduct detailed inspection and corrective maintenance."
            )

        prompt = f"""
FLIGHT READINESS ASSESSMENT SUMMARY

Status: {status}
Confidence Score: {confidence:.1f}%

Explanation:
{explanation}

Identified Issues:
{issues_text}

Recommendations:
{recommendations_text}
"""

        return prompt


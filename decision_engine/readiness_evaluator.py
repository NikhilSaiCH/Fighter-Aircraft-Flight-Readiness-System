class FlightReadinessEvaluator:
    """
    Fighter Aircraft Flight Readiness Decision Engine
    (Category II – Safety-Critical)

    Decision priority:
    1. Hard fighter aircraft safety limits
    2. Degradation trends
    3. ML anomaly evidence (supporting only)
    """

    def evaluate(
        self,
        flight_df,
        feature_df,
        anomaly_ratio: float,
        trend_slope: float,
    ):
        issues = []
        recommendations = []

        # ================================
        # 1️⃣ HARD SAFETY PARAMETER CHECKS
        # ================================

        # ---- Engine Temperature (EGT) ----
        mean_egt = flight_df["exhaust_gas_temp_c"].mean()
        if mean_egt > 750:
            issues.append(
                f"Exhaust Gas Temperature too high (avg {mean_egt:.1f} °C)"
            )
            recommendations.append(
                "Inspect engine cooling system, fuel-air mixture, and turbine blades"
            )

        # ---- Engine RPM ----
        max_rpm = flight_df["rpm_n1_pct"].max()
        if max_rpm > 100:
            issues.append(
                f"Engine RPM exceeds safe limit (max {max_rpm:.1f}%)"
            )
            recommendations.append(
                "Check throttle control, FADEC system, and engine governor"
            )

        # ---- Oil Pressure ----
        min_oil_pressure = flight_df["oil_pressure_psi"].min()
        if min_oil_pressure < 40:
            issues.append(
                f"Oil pressure below safe limit (min {min_oil_pressure:.1f} psi)"
            )
            recommendations.append(
                "Inspect lubrication system, oil pump, and oil lines"
            )

        # ---- Oil Temperature ----
        max_oil_temp = flight_df["oil_temp_c"].max()
        if max_oil_temp > 120:
            issues.append(
                f"Oil temperature exceeds safe limit (max {max_oil_temp:.1f} °C)"
            )
            recommendations.append(
                "Check oil cooling system and reduce engine thermal stress"
            )

        # ---- Structural G-load ----
        if "g_total" in feature_df.columns:
            max_g = feature_df["g_total"].max()
            if max_g > 9:
                issues.append(
                    f"Excessive G-load detected (max {max_g:.2f} g)"
                )
                recommendations.append(
                    "Inspect airframe structure and restrict high-G maneuvers"
                )

        # ================================
        # 2️⃣ TREND-BASED DEGRADATION CHECK
        # ================================

        if trend_slope < -0.10:
            issues.append(
                "Sustained degradation trend observed in engine health"
            )
            recommendations.append(
                "Schedule preventive maintenance and detailed engine inspection"
            )

        # ================================
        # 3️⃣ ML ANOMALY SUPPORT CHECK
        # ================================

        if anomaly_ratio > 0.25:
            issues.append(
                f"High anomaly rate detected ({anomaly_ratio:.2f})"
            )
            recommendations.append(
                "Investigate abnormal sensor patterns and validate subsystems"
            )

        # ================================
        # FINAL DECISION
        # ================================

        if issues:
            return {
                "status": "NOT READY",
                "issues": issues,
                "recommendations": recommendations,
            }

        return {
            "status": "READY",
            "issues": [],
            "recommendations": [
                "Proceed with standard pre-flight inspection",
                "Aircraft parameters within Category II operational limits",
            ],
        }

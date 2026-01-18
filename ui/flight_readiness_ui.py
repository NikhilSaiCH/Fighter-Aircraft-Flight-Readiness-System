import streamlit as st
import pandas as pd
from reporting.flight_readiness_report import FlightReadinessReportGenerator
import tempfile
import os
# ================= ANALYTICS CORE =================
from analytics_core import (
    FeatureEngineer,
    AnomalyDetector,
    HealthIndexCalculator,
    TrendAnalyzer
)

# ================= DRDO PIPELINE =================
from drdo_pipeline.stage10_root_cause_analysis import CausalGraph, RCAEngine
from drdo_pipeline.stage11_trend_predictive_maintenance import TrendIntegrator

# ================= DECISION & LLM =================
from decision_engine import FlightReadinessEvaluator
from llm_layer import PromptBuilder, LLMExplanationGenerator


# ================= UI CONFIG =================
st.set_page_config(
    page_title="Aircraft Flight Readiness Analyzer",
    layout="wide"
)

st.title("✈️ Aircraft Flight Readiness Analyzer")
st.subheader("Category II – Fighter / Attack Aircraft")
st.caption(
    "CSV-based Fighter Aircraft Flight Readiness Analytics | "
    "MIL-STD-2124A | DRDO 14-Stage | ML + LLM"
)

st.markdown("---")

# ================= SINGLE CSV UPLOAD =================
st.sidebar.header("Upload Fighter Aircraft Flight Data")

uploaded_csv = st.sidebar.file_uploader(
    "Upload Fighter Aircraft Data (CSV only)",
    type=["csv"]
)

flight_df = None

# ================= LOAD CSV =================
if uploaded_csv:
    try:
        flight_df = pd.read_csv(uploaded_csv)
        st.sidebar.success("Fighter aircraft data loaded successfully")
    except Exception as e:
        st.sidebar.error(f"Failed to read CSV file: {e}")

# ================= ANALYSIS =================
if flight_df is not None:

    st.success("Running fighter aircraft flight readiness analysis...")

    # ---------- FEATURE ENGINEERING ----------
    fe = FeatureEngineer()
    feature_df = fe.transform(flight_df)

    # ---------- ANOMALY DETECTION ----------
    ad = AnomalyDetector()
    _, anomaly_scores = ad.fit_predict(
        feature_df.drop(columns=["timestamp"])
    )

    # ---------- HEALTH INDEX ----------
    hic = HealthIndexCalculator()
    engine_health = hic.engine_health(flight_df)

    # ---------- TREND ANALYSIS ----------
    ta = TrendAnalyzer()
    slope = ta.compute_trend(engine_health)
    trend_label = ta.classify_trend(slope)

    trend_summary = TrendIntegrator().summarize(
        trend_label,
        engine_health.mean()
    )

    # ---------- ROOT CAUSE ANALYSIS ----------
    cg = CausalGraph()
    rca_engine = RCAEngine(cg)

    analytics_flags = {
        "high_egt": flight_df["exhaust_gas_temp_c"].mean() > 750,
        "rpm_instability": flight_df["rpm_n1_pct"].std() > 10,
        "low_oil_pressure": flight_df["oil_pressure_psi"].mean() < 40,
        "high_g_events": (feature_df["g_total"] > 9).sum()
    }

    root_causes = rca_engine.analyze(analytics_flags)

    # ---------- DECISION ENGINE ----------
    evaluator = FlightReadinessEvaluator()
    readiness = evaluator.evaluate(
        engine_health_index=engine_health,
        anomaly_scores=anomaly_scores,
        trend_summary=trend_summary,
        governance_status="PASS",
        root_causes=root_causes
    )

    # ---------- LLM EXPLANATION ----------
    prompt = PromptBuilder().build_prompt(
        readiness_output=readiness,
        root_causes=root_causes,
        analytics_summary=readiness["summary"],
        maintenance_text=""  # No PDF now
    )

    llm_output = LLMExplanationGenerator(
        use_emulator=True
    ).generate(prompt)

    # ================= OUTPUT =================
    st.markdown("---")
    st.header("🛫 Flight Readiness Assessment")

    color = "green" if readiness["status"] == "READY FOR FLIGHT" else "red"
    st.markdown(
        f"<h2 style='color:{color}'>{readiness['status']}</h2>",
        unsafe_allow_html=True
    )

    st.markdown("### 🧠 Explanation")
    st.write(llm_output["Explanation"])

    st.markdown("### ❌ Identified Issues")
    if llm_output["Defects"]:
        for issue in llm_output["Defects"]:
            st.warning(issue)
    else:
        st.success("No critical issues detected")

    st.markdown("### 🛠️ Recommendations")
    for rec in llm_output["Recommendations"]:
        st.info(rec)

    st.markdown("### 📊 Engine Health Trend")
    st.line_chart(engine_health)

    st.caption(
        "Decision-support system only. "
        "Final flight clearance remains with authorized authorities."
    )

else:
    st.info(
        "Upload a fighter aircraft flight data CSV file to begin analysis."
    )

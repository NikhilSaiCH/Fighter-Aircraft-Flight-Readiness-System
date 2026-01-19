import streamlit as st
import pandas as pd

# ================= ANALYTICS CORE =================
from analytics_core import (
    FeatureEngineer,
    AnomalyDetector,
    HealthIndexCalculator,
    TrendAnalyzer
)

# ================= DECISION ENGINE =================
from decision_engine.readiness_evaluator import FlightReadinessEvaluator

# ================= LLM =================
from llm_layer.prompt_builder import PromptBuilder
from llm_layer.explanation_generator import LLMExplanationGenerator


# ================= UI CONFIG =================
st.set_page_config(
    page_title="Fighter Aircraft Flight Readiness System",
    layout="wide"
)

st.title("✈️ Fighter Aircraft Flight Readiness System")
st.subheader("Category II – Fighter / Attack Aircraft")
st.caption(
    "MIL-STD-2124A | DRDO 14-Stage Analytics | "
    "Rule-Based Safety + ML + Explainable AI"
)

st.markdown("---")

# ================= CSV UPLOAD =================
st.sidebar.header("Upload Fighter Aircraft Flight Data")

uploaded_csv = st.sidebar.file_uploader(
    "Upload Fighter Aircraft CSV File",
    type=["csv"]
)

if uploaded_csv is None:
    st.info("Upload a fighter aircraft CSV file to begin analysis.")
    st.stop()

# ================= LOAD DATA =================
try:
    flight_df = pd.read_csv(uploaded_csv)
    st.sidebar.success("Flight data loaded successfully")
except Exception as e:
    st.error(f"Failed to load CSV file: {e}")
    st.stop()

# ================= ANALYSIS =================
st.success("Running fighter aircraft flight readiness analysis...")

# ---------- FEATURE ENGINEERING ----------
fe = FeatureEngineer()
feature_df = fe.transform(flight_df)

# ---------- ANOMALY DETECTION ----------
ad = AnomalyDetector()
_, anomaly_scores = ad.fit_predict(
    feature_df.drop(columns=["timestamp"], errors="ignore")
)
anomaly_ratio = anomaly_scores.mean()

# ---------- ENGINE HEALTH ----------
hic = HealthIndexCalculator()
engine_health_series = hic.engine_health(flight_df)
engine_health_index = engine_health_series.mean()

# ---------- TREND ANALYSIS ----------
ta = TrendAnalyzer()
trend_slope = ta.compute_trend(engine_health_series)

# ---------- DECISION ENGINE (DOMAIN-CORRECT) ----------
evaluator = FlightReadinessEvaluator()
readiness = evaluator.evaluate(
    flight_df=flight_df,
    feature_df=feature_df,
    anomaly_ratio=anomaly_ratio,
    trend_slope=trend_slope
)

# ---------- LLM EXPLANATION ----------
prompt = PromptBuilder().build_prompt(
    readiness_output=readiness
)

llm_output = LLMExplanationGenerator(
    use_emulator=True
).generate(prompt)

# ================= OUTPUT =================
st.markdown("---")
st.header("🛫 Flight Readiness Assessment")

if readiness["status"] == "READY":
    st.success("✅ READY FOR FLIGHT")
else:
    st.error("❌ NOT READY FOR FLIGHT")

# ---------- EXPLANATION ----------
st.markdown("### 🧠 Explanation")
st.write(llm_output.get("Explanation", "Explanation not available."))

# ---------- ISSUES ----------
st.markdown("### ❌ Identified Issues")
if readiness["issues"]:
    for issue in readiness["issues"]:
        st.warning(issue)
else:
    st.success("No safety-critical parameter violations detected.")

# ---------- RECOMMENDATIONS ----------
st.markdown("### 🛠️ Recommendations")
for rec in readiness["recommendations"]:
    st.info(rec)

# ---------- ENGINE HEALTH TREND ----------
st.markdown("### 📊 Engine Health Trend")
st.line_chart(engine_health_series)

# ---------- DEBUG (OPTIONAL – COMMENT OUT FOR FINAL SUBMISSION) ----------
with st.expander("🔎 Diagnostic Metrics (for validation)"):
    st.write(f"Anomaly Ratio: {anomaly_ratio:.3f}")
    st.write(f"Average Engine Health Index: {engine_health_index:.3f}")
    st.write(f"Health Trend Slope: {trend_slope:.4f}")

st.caption(
    "This system is a decision-support tool. "
    "Final flight clearance rests with authorized flight safety personnel."
)

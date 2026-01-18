# Fighter Aircraft Flight Readiness System
Fighter Aircraft Flight Readiness System is a data analytics and decision-support system
designed to assess the flight readiness of Category II fighter / attack aircraft using
machine learning, analytics, and explainable AI.
The system is aligned with:
**MIL-STD-2124A (Category II parameters)**
**DRDO 14-stage data analytics architecture**
It provides an end-to-end pipeline from flight data ingestion to
readiness decision, confidence scoring, root cause analysis, and
actionable recommendations.

# Key Features
CSV-based fighter aircraft flight data ingestion  
Feature engineering and data transformation  
Anomaly detection using machine learning  
Engine health index computation  
Trend monitoring and predictive maintenance indicators  
Root Cause Analysis (RCA) using causal graphs  
Flight readiness decision (READY / NOT READY)    
LLM-based explanation and recommendations  
Interactive Streamlit UI   


# System Architecture
The project follows a modular, UI-driven architecture.
Rather than a linear script-based pipeline, each DRDO stage is implemented
as a logical module and invoked dynamically through the UI, reflecting
real-world aerospace analytics systems.


# DRDO 14-Stage Mapping (Summary)
| DRDO Stage            | Implementation                |
|-----------------------|-------------------------------|
| Data Ingestion        | CSV upload, NiFi emulator     |
| Data Transformation   | Pandas feature engineering    |
| Orchestration         | Logical workflow orchestration|
| Machine Learning      | Anomaly detection, clustering |
| MLOps                 | Model inference emulation     |
| Analytics & BI        | Health metrics, trends        |
| Data Governance       | Schema & range validation     |
| Streaming             | Kafka emulator (conceptual)   |
| AI Analytics          | Pattern detection             |
| Root Cause Analysis   | Causal graph (NetworkX)       |
| Trend Monitoring      | Predictive maintenance logic  |
| Decision Support      | Readiness evaluator           |
| Feedback & Retraining | Emulated hooks                |
| Infrastructure        | Modular Python architecture   |


# Input Data
**Format:** CSV  
**Aircraft Type:** Category II – Fighter / Attack Aircraft  
**Sampling:** Time-series flight telemetry  

# Example Parameters
Airspeed, altitude
Pitch, roll, yaw
Acceleration (G-loads)
Engine RPM, EGT
Fuel flow
Oil pressure & temperature
Warning indicators
> CSV is used as the authoritative analytics input format.
> PDFs are considered presentation/report formats and are not used for ingestion.


# Output
**Flight Readiness Status:** READY FOR FLIGHT / NOT READY FOR FLIGHT  
**Identified Issues (if any)**  
**Root Causes**  
**Maintenance & operational recommendations**  
**Engine health trend visualization**  


# How to Run the Project
**Install Dependencies**
pip install -r requirements.txt
**RUN**
py -m streamlit run ui/flight_readiness_ui.py

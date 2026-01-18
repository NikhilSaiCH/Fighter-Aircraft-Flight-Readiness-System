# DRDO Stage 3 – Orchestration & Workflow Management
# Tool: Apache Airflow (Emulated)
# DAG enforcing DRDO pipeline order

from .airflow_emulator import DAG, Task

# Import stage executors (already implemented)
from stage01_data_ingestion.nifi_emulator import NiFiEmulator
from stage02_data_transformation.pandas_transformer import PandasTransformer


def stage1_task(context):
    nifi = NiFiEmulator()
    packets = nifi.run(cycles=20)
    context["stage1_packets"] = packets
    context["baseline"] = packets[0]["baseline"]


def stage2_task(context):
    transformer = PandasTransformer()
    for pkt in context["stage1_packets"]:
        transformer.ingest_stage1_output(pkt)

    context["stage2_dataframe"] = transformer.transform(
        baseline=context["baseline"]
    )


def build_dag():
    dag = DAG(dag_id="aircraft_fdr_pipeline")

    t1 = Task("stage1_ingestion", stage1_task)
    t2 = Task("stage2_transformation", stage2_task)

    t1.set_downstream(t2)

    dag.add_task(t1)
    dag.add_task(t2)

    return dag

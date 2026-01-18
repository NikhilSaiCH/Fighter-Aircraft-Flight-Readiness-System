# DRDO Stage 3 – Orchestration & Workflow Management
# Tool: Apache Airflow (Emulated)
# Responsibility: DAG execution ONLY

class Task:
    """
    Represents a single Airflow task
    """

    def __init__(self, task_id, callable_fn):
        self.task_id = task_id
        self.callable_fn = callable_fn
        self.downstream = []

    def set_downstream(self, task):
        self.downstream.append(task)


class DAG:
    """
    Minimal DAG engine enforcing execution order
    """

    def __init__(self, dag_id):
        self.dag_id = dag_id
        self.tasks = {}

    def add_task(self, task: Task):
        self.tasks[task.task_id] = task

    def execute(self, context: dict):
        visited = set()

        def run_task(task: Task):
            if task.task_id in visited:
                return
            task.callable_fn(context)
            visited.add(task.task_id)
            for downstream_task in task.downstream:
                run_task(downstream_task)

        # Entry points = tasks with no upstream dependencies
        for task in self.tasks.values():
            run_task(task)

# DRDO Stage 14 – Supporting Infrastructure
# Tool: Logging Infrastructure
# Responsibility: Deterministic, auditable logs

import datetime


class SystemLogger:
    """
    Simple deterministic logger for DRDO audit trails
    """

    def log(self, stage: str, message: str):
        timestamp = datetime.datetime.utcnow().isoformat()
        print(f"[{timestamp}] [{stage}] {message}")

# DRDO Stage 14 – Supporting Infrastructure
# Tool: Reproducibility Infrastructure
# Responsibility: Run fingerprinting

import hashlib
import json


class ReproducibilityTracker:
    """
    Generates reproducibility fingerprints for pipeline runs
    """

    def fingerprint(self, config: dict, audit_manifest: dict):
        payload = {
            "config": config,
            "audit": audit_manifest
        }
        raw = json.dumps(payload, sort_keys=True).encode()
        return hashlib.sha256(raw).hexdigest()

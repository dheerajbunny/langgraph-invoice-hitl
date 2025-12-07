import uuid
import time
from checkpoint_store import save_checkpoint

class CheckpointNode:
    def run(self, state, config):

        if state.get("match_result") != "FAILED":
            return {}

        checkpoint_id = str(uuid.uuid4())
        created_at = time.strftime("%Y-%m-%dT%H:%M:%S")

        invoice_id = state["invoice_payload"]["invoice_id"]

        save_checkpoint(checkpoint_id, invoice_id, state, created_at)

        url = f"http://localhost:8000/human-review/{checkpoint_id}"

        print(f"[CHECKPOINT] Created checkpoint {checkpoint_id}")

        return {
            "checkpoint_id": checkpoint_id,
            "review_url": url,
            "paused_reason": "MATCH_FAILED"
        }

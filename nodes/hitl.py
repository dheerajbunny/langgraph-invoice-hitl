import time
from checkpoint_store import get_checkpoint

class HumanReviewNode:
    def run(self, state, config):

        cp_id = state.get("checkpoint_id")

        if not cp_id:
            print("[HITL] No checkpoint to wait for.")
            return {}

        print(f"[HITL] Waiting for decision on {cp_id} ...")

        waited = 0

        while waited < 300:
            cp = get_checkpoint(cp_id)

            if cp and cp["decision"]:

                if cp["decision"] == "ACCEPT":
                    print("[HITL] Accepted by human.")
                    return {"human_decision": "ACCEPT", "next_stage": "RECONCILE"}

                else:
                    print("[HITL] Rejected.")
                    return {"human_decision": "REJECT", "next_stage": "MANUAL_HANDOFF"}

            time.sleep(2)
            waited += 2

        print("[HITL] No decision received (timeout).")

        return {"human_decision": "TIMEOUT", "next_stage": "MANUAL_HANDOFF"}

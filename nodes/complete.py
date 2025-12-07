class CompleteNode:
    def run(self, state, config):

        print("[COMPLETE] Workflow completed successfully.")

        return {
            "final_payload": {
                "invoice_id": state["invoice_payload"]["invoice_id"],
                "amount": state["invoice_payload"]["amount"],
                "status": "COMPLETED"
            },
            "audit_log": ["workflow_completed"],
            "status": "COMPLETED"
        }

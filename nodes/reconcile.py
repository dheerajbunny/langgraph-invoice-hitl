class ReconciliationNode:
    def run(self, state, config):

        print("[RECONCILE] Building accounting entries...")

        entries = [
            {
                "debit": state["invoice_payload"]["amount"],
                "credit": 0
            }
        ]

        return {
            "accounting_entries": entries
        }

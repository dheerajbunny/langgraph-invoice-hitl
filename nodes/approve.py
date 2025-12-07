class ApprovalNode:
    def run(self, state, config):

        amount = state["invoice_payload"]["amount"]

        status = "AUTO_APPROVED" if amount < 10000 else "ESCALATED"

        print(f"[APPROVE] approval_status={status}")

        return {
            "approval_status": status
        }

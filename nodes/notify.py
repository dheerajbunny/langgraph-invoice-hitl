class NotifyNode:
    def run(self, state, config):

        print("[NOTIFY] Sending notifications...")

        return {
            "notify_status": {
                "vendor_email": "sent",
                "finance_slack": "sent"
            },
            "notified_parties": ["vendor@example.com", "finance-team"]
        }

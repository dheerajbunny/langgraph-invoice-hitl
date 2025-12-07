class ErpFetchNode:
    def run(self, state, config):

        print("[RETRIEVE] Fetching mock PO/GRN from ERP...")

        matched_pos = [
            {"po_id": "PO123", "amount": state["invoice_payload"]["amount"]}
        ]

        matched_grns = [
            {"grn_id": "GRN123", "qty": 1}
        ]

        return {
            "matched_pos": matched_pos,
            "matched_grns": matched_grns,
            "history": []
        }

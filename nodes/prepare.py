class NormalizeEnrichNode:
    def run(self, state, config):
        vendor = state["invoice_payload"].get("vendor_name", "unknown")
        normalized = vendor.strip().title()

        profile = {
            "normalized_name": normalized,
            "tax_id": state["invoice_payload"].get("vendor_tax_id", "UNKNOWN"),
            "enrichment_meta": {"source": "mock", "confidence": 0.9}
        }

        flags = {
            "missing_info": [],
            "risk_score": 0.1
        }

        print(f"[PREPARE] Normalized vendor -> {normalized}")

        return {
            "vendor_profile": profile,
            "normalized_invoice": state["invoice_payload"],
            "flags": flags
        }

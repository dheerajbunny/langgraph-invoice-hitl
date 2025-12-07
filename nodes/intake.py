import time

class IngestNode:
    def run(self, state, config):
        invoice = state.get("invoice_payload", {})
        raw_id = f"raw_{invoice.get('invoice_id', 'unknown')}"
        ingest_ts = time.strftime("%Y-%m-%dT%H:%M:%S")

        print(f"[INTAKE] Persisted raw_id={raw_id}")

        return {
            "raw_id": raw_id,
            "ingest_ts": ingest_ts,
            "validated": True
        }

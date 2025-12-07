class OcrNlpNode:
    def run(self, state, config):
        inv = state.get("invoice_payload", {})

        print("[UNDERSTAND] Running mocked OCR & parsing...")

        parsed = {
            "invoice_text": "Dummy OCR for invoice " + str(inv.get("invoice_id")),
            "parsed_line_items": inv.get("line_items", []),
            "detected_pos": [],
            "currency": inv.get("currency"),
            "parsed_dates": {
                "invoice_date": inv.get("invoice_date"),
                "due_date": inv.get("due_date")
            }
        }

        return {"parsed_invoice": parsed}

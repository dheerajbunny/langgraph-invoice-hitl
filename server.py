from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from checkpoint_store import get_checkpoint, set_decision, init_db

app = FastAPI()
init_db()

class DecisionPayload(BaseModel):
    checkpoint_id: str
    decision: str   # ACCEPT or REJECT
    reviewer_id: str
    notes: str | None = None

@app.get("/human-review/pending")
def list_pending():

    import sqlite3
    conn = sqlite3.connect("demo.db")
    c = conn.cursor()

    c.execute("SELECT id, invoice_id, created_at FROM checkpoints WHERE decision IS NULL")
    rows = c.fetchall()

    conn.close()

    return [
        {
            "checkpoint_id": r[0],
            "invoice_id": r[1],
            "created_at": r[2]
        }
        for r in rows
    ]

@app.post("/human-review/decision")
def decide(payload: DecisionPayload):

    cp = get_checkpoint(payload.checkpoint_id)
    if not cp:
        raise HTTPException(status_code=404, detail="Checkpoint not found")

    if cp.get("decision"):
        raise HTTPException(status_code=400, detail="Decision already provided")

    set_decision(payload.checkpoint_id, payload.decision.upper(), payload.reviewer_id)

    return {
        "resume_token": f"resume_{payload.checkpoint_id}",
        "next_stage": "RECONCILE"
    }

import sqlite3
import json

DB_PATH = "demo.db"

def _conn():
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    return conn

def init_db():
    conn = _conn()
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS checkpoints (
            id TEXT PRIMARY KEY,
            invoice_id TEXT,
            blob TEXT,
            created_at TEXT,
            decision TEXT,
            reviewer_id TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_checkpoint(checkpoint_id: str, invoice_id: str, state_blob: dict, created_at: str):
    conn = _conn()
    c = conn.cursor()
    blob = json.dumps(state_blob)
    c.execute("""
        INSERT OR REPLACE INTO checkpoints 
        (id, invoice_id, blob, created_at, decision, reviewer_id)
        VALUES (?, ?, ?, ?, ?, ?)
    """,
    (checkpoint_id, invoice_id, blob, created_at, None, None))
    conn.commit()
    conn.close()
    return checkpoint_id

def get_checkpoint(checkpoint_id: str):
    conn = _conn()
    c = conn.cursor()
    c.execute("SELECT id, invoice_id, blob, created_at, decision, reviewer_id FROM checkpoints WHERE id = ?", 
              (checkpoint_id,))
    r = c.fetchone()
    conn.close()

    if not r:
        return None

    return {
        "id": r[0],
        "invoice_id": r[1],
        "blob": json.loads(r[2]),
        "created_at": r[3],
        "decision": r[4],
        "reviewer_id": r[5]
    }

def set_decision(checkpoint_id: str, decision: str, reviewer_id: str):
    conn = _conn()
    c = conn.cursor()
    c.execute("UPDATE checkpoints SET decision = ?, reviewer_id = ? WHERE id = ?",
              (decision, reviewer_id, checkpoint_id))
    conn.commit()
    conn.close()

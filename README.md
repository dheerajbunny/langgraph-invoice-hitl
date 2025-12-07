# LangGraph Invoice Processing with HITL

This project demonstrates a LangGraph-based invoice processing workflow with Human-in-the-Loop (HITL) checkpointing and resume.

## Overview

The workflow performs the following steps:

- Invoice intake
- OCR & parsing
- Data normalization and enrichment
- ERP PO/GRN retrieval
- Two-way invoice matching
- Conditional checkpoint pause on match failure
- Human review and decision via API
- Workflow resume from reconciliation
- Approval, posting, and notification stages

## Human-In-The-Loop (HITL)

When invoice matching fails, the workflow creates a persistent checkpoint and pauses execution.

A FastAPI service exposes endpoints for:

- Viewing pending checkpoints
- Submitting human review decisions (ACCEPT or REJECT)

On ACCEPT, the workflow resumes automatically from the reconciliation stage.

## How to Run

### Install

```bash
pip install -r requirements.txt
Start HITL API Server
bash
Copy code
uvicorn server:app --reload
Run Workflow
In another terminal:

bash
Copy code
python main.py
HITL Action
Submit human review decision:

bash
Copy code
# PowerShell example
Invoke-RestMethod `
 -Uri "http://127.0.0.1:8000/human-review/decision" `
 -Method POST `
 -Headers @{ "Content-Type" = "application/json" } `
 -Body '{"checkpoint_id":"<UUID>","decision":"ACCEPT","reviewer_id":"demo"}'

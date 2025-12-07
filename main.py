import json
from graph import StateGraph
from checkpoint_store import init_db

from nodes.intake import IngestNode
from nodes.understand import OcrNlpNode
from nodes.prepare import NormalizeEnrichNode
from nodes.retrieve import ErpFetchNode
from nodes.match import TwoWayMatcherNode
from nodes.checkpoint import CheckpointNode
from nodes.hitl import HumanReviewNode
from nodes.reconcile import ReconciliationNode
from nodes.approve import ApprovalNode
from nodes.posting import PostingNode
from nodes.notify import NotifyNode
from nodes.complete import CompleteNode

init_db()

with open("workflow.json", "r") as f:
    wf = json.load(f)

config = wf.get("config", {})

graph = StateGraph()

# register nodes
graph.add_node("INTAKE", lambda s,c: IngestNode().run(s,c))
graph.add_node("UNDERSTAND", lambda s,c: OcrNlpNode().run(s,c))
graph.add_node("PREPARE", lambda s,c: NormalizeEnrichNode().run(s,c))
graph.add_node("RETRIEVE", lambda s,c: ErpFetchNode().run(s,c))
graph.add_node("MATCH_TWO_WAY", lambda s,c: TwoWayMatcherNode().run(s,c))
graph.add_node("CHECKPOINT_HITL", lambda s,c: CheckpointNode().run(s,c))
graph.add_node("HITL_DECISION", lambda s,c: HumanReviewNode().run(s,c))
graph.add_node("RECONCILE", lambda s,c: ReconciliationNode().run(s,c))
graph.add_node("APPROVE", lambda s,c: ApprovalNode().run(s,c))
graph.add_node("POSTING", lambda s,c: PostingNode().run(s,c))
graph.add_node("NOTIFY", lambda s,c: NotifyNode().run(s,c))
graph.add_node("COMPLETE", lambda s,c: CompleteNode().run(s,c))

# define execution order from workflow.json
order = [s["id"] for s in wf["stages"]]
graph.set_order(order)

# load sample input
with open("sample_invoice.json","r") as f:
    sample_invoice = json.load(f)

print("\n🚀 Starting Invoice Processing Workflow...\n")

result = graph.run({"invoice_payload": sample_invoice}, config)

print("\n FINAL OUTPUT:\n")
import json as j
print(j.dumps(result["final_state"], indent=2))

from typing import Callable, Dict, List

class StateGraph:
    def __init__(self):
        self.nodes = {}
        self.order = []
        self.edges = {}

    def add_node(self, node_id: str, fn: Callable):
        self.nodes[node_id] = fn

    def set_order(self, order: List[str]):
        self.order = order
        for i in range(len(order) - 1):
            self.edges[order[i]] = order[i + 1]

    def run(self, initial_state: Dict, config: Dict):
        state = dict(initial_state)
        logs = []
        idx = 0

        while idx < len(self.order):
            node_id = self.order[idx]
            fn = self.nodes.get(node_id)

            print(f"\n--- RUN NODE: {node_id} ---")

            out = fn(state, config)
            if out:
                for k, v in out.items():
                    state[k] = v

            idx += 1

        return {"final_state": state, "logs": logs}

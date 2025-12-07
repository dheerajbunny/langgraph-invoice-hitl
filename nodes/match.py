class TwoWayMatcherNode:
    def run(self, state, config):

        # Force a failure to ALWAYS trigger HITL demo
        score = 0.75
        result = "FAILED"

        print(f"[MATCH_TWO_WAY] score={score}, result={result}")

        return {
            "match_score": score,
            "match_result": result
        }

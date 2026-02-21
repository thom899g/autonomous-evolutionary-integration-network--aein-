from typing import Dict, Any
from logging import getLogger
from collections import deque

logger = getLogger(__name__)

class PerformanceFeedbackLoop:
    def __init__(self):
        self.metrics_history = deque(maxlen=100)
        self.last_error = None

    def collect_metrics(self, module_id: str, metrics: Dict[str, Any]) -> None:
        """Collect performance metrics from a module."""
        try:
            if not all(key in metrics for key in ["latency", "accuracy", "throughput"]):
                raise ValueError("Missing required metrics keys")
            self.metrics_history.append((module_id, metrics))
            logger.info(f"Metrics collected from {module_id}: {metrics}")
        except Exception as e:
            self.last_error = str(e)
            logger.error(f"Failed to collect metrics: {e}")

    def analyze_performance(self) -> Dict[str, Any]:
        """Analyze collected metrics and generate feedback."""
        try:
            analysis = {}
            for module_id, metrics in self.metrics_history:
                if metrics["accuracy"] < 0.8:
                    analysis[module_id] = "Underperforming"
                elif metrics["throughput"] > 100:
                    analysis[module_id] = "Overloaded"
                else:
                    analysis[module_id] = "Operational"
            return {"timestamp": datetime.now().isoformat(), "analysis": dict(analysis)}
        except Exception as e:
            self.last_error = str(e)
            logger.error(f"Failed to analyze performance: {e}")

    def dispatch_feedback(self, feedback: Dict[str, Any]) -> None:
        """Dispatch performance feedback to relevant modules."""
        try:
            if not isinstance(feedback, dict) or "target_module" not in feedback:
                raise ValueError("Invalid feedback format")
            logger.info(f"Dispatching feedback to {feedback['target_module']}: {feedback}")
            # Simulated dispatch mechanism
        except Exception as e:
            self.last_error = str(e)
            logger.error(f"Failed to dispatch feedback: {e}")

# Example usage
if __name__ == "__main__":
    loop = PerformanceFeedbackLoop()
    test_metrics = {"latency": 0.1, "accuracy": 0.85, "throughput": 90}
    loop.collect_metrics("module_1", test_metrics)
    feedback = loop.analyze_performance()
    print(feedback)
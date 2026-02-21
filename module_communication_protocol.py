import json
from typing import Dict, Any
from logging import getLogger
from datetime import datetime

logger = getLogger(__name__)

class ModuleCommunicationProtocol:
    def __init__(self):
        self.last_error = None

    def encode_message(self, message: Dict[str, Any]) -> str:
        """Encode a message into JSON format for transmission."""
        try:
            return json.dumps(message)
        except TypeError as e:
            logger.error(f"Failed to encode message: {e}")
            raise

    def decode_message(self, message_str: str) -> Dict[str, Any]:
        """Decode a JSON-formatted string into a dictionary."""
        try:
            return json.loads(message_str)
        except json.JSONDecodeError as e:
            logger.error(f"Failed to decode message: {e}")
            raise

    def send_feedback(self, module_id: str, feedback: Dict[str, Any]) -> None:
        """Send performance feedback to a specific module."""
        try:
            # Simulated sending mechanism
            timestamp = datetime.now().isoformat()
            feedback_with_time = {"timestamp": timestamp, **feedback}
            logger.info(f"Sending feedback to {module_id}: {feedback_with_time}")
        except Exception as e:
            self.last_error = str(e)
            logger.error(f"Failed to send feedback: {e}")

    def receive_message(self, message_str: str) -> Dict[str, Any]:
        """Receive and process an incoming message."""
        try:
            data = self.decode_message(message_str)
            if "module_id" not in data or "payload" not in data:
                raise ValueError("Invalid message format")
            logger.info(f"Received message from {data['module_id']}: {data}")
            return data
        except Exception as e:
            self.last_error = str(e)
            logger.error(f"Failed to process incoming message: {e}")

# Example usage
if __name__ == "__main__":
    protocol = ModuleCommunicationProtocol()
    test_message = {"status": "heartbeat", "timestamp": datetime.now().isoformat()}
    encoded = protocol.encode_message(test_message)
    decoded = protocol.decode_message(encoded)
    print(decoded)
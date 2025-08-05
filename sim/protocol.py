import json
import time
from typing import Dict, Any, Optional

def encode_message(src: str, dst: str, command: str, data: Any) -> str:
    """
    Encode a message into JSON format
    """
    message = {
        "src": src,
        "dst": dst, 
        "cmd": command,
        "data": data,
        "timestamp": time.time()
    }
    return json.dumps(message)

def decode_message(json_string: str) -> Dict[str, Any]:
    """
    Decode a JSON message
    """
    try:
        return json.loads(json_string)
    except json.JSONDecodeError as e:
        print(f"[Protocol] Error decoding message: {e}")
        return {}

def create_motor_command(motor_id: int, action: str, **kwargs) -> Dict[str, Any]:
    """
    Create a standardized motor command
    """
    return {
        "motor_id": motor_id,
        "action": action,
        **kwargs
    }

def create_status_request(request_type: str = "all") -> Dict[str, Any]:
    """
    Create a status request message
    """
    return {
        "request_type": request_type,
        "timestamp": time.time()
    }

def create_status_response(node_id: str, status_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Create a status response message
    """
    return {
        "node_id": node_id,
        "status": status_data,
        "timestamp": time.time()
    }

def validate_message(message: Dict[str, Any]) -> bool:
    """
    Validate that a message has required fields
    """
    required_fields = ["src", "dst", "cmd"]
    return all(field in message for field in required_fields)

# Common message types for motor control
class MessageTypes:
    MOTOR_START = "motor_start"
    MOTOR_STOP = "motor_stop"
    MOTOR_SET_SPEED = "motor_set_speed"
    STATUS_REQUEST = "status_request"
    STATUS_RESPONSE = "status_response"
    EMERGENCY_STOP = "emergency_stop"
    HEARTBEAT = "heartbeat"
    ERROR = "error"
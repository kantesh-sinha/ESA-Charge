"""
ISA/CHARGE Modular Motor Control Simulation Package
"""
from .network import VirtualBus
from .node import Node
from .protocol import (
    encode_message, 
    decode_message, 
    create_motor_command,
    create_status_request,
    create_status_response,
    MessageTypes
)

__version__ = "0.1.0"
__author__ = "ISA/CHARGE Team - Kantesh Kumar Sinha"
__all__ = [
    "VirtualBus",
    "Node",
    "encode_message",
    "decode_message",
    "create_motor_command",
    "create_status_request", 
    "create_status_response",
    "MessageTypes"
]

from .protocol import encode_message, decode_message

class Node:
    """
    Base node class for motor control units
    """
    def __init__(self, node_id, bus):
        self.node_id = node_id
        self.bus = bus
        self.message_handlers = {}
        self.bus.register_node(self)

    def send_command(self, dst, command, data):
        """Send a command to another node"""
        message = encode_message(self.node_id, dst, command, data)
        parsed_message = decode_message(message)
        self.bus.send_message(parsed_message)

    def send_direct_message(self, dst, message_dict):
        """Send a direct message dictionary"""
        message_dict["src"] = self.node_id
        message_dict["dst"] = dst
        self.bus.send_message(message_dict)

    def broadcast_command(self, command, data):
        """Broadcast a command to all nodes"""
        message = encode_message(self.node_id, "broadcast", command, data)
        parsed_message = decode_message(message)
        self.bus.broadcast_message(parsed_message, self.node_id)

    def receive_message(self, message):
        """Handle incoming messages"""
        print(f"[{self.node_id}] Received message: {message}")
        
        # Try to handle the message if we have a handler
        command = message.get("cmd")
        if command and command in self.message_handlers:
            try:
                self.message_handlers[command](message)
            except Exception as e:
                print(f"[{self.node_id}] Error handling command '{command}': {e}")

    def register_handler(self, command, handler_function):
        """Register a handler for a specific command"""
        self.message_handlers[command] = handler_function
        print(f"[{self.node_id}] Registered handler for command: {command}")

    def get_node_id(self):
        """Get this node's ID"""
        return self.node_id
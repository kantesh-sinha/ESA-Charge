# sim/network.py
import threading
import queue

class VirtualBus:
    """
    Virtual bus to simulate network (CAN / Ethernet)
    """
    def __init__(self):
        self.nodes = {}
        self.message_queue = queue.Queue()
        self.running = False
    
    def register_node(self, node):
        self.nodes[node.get_node_id()] = node
        print(f"[VirtualBus] Node registered: {node.get_node_id()}")
    
    def list_nodes(self):
        return list(self.nodes.keys())
    
    def get_node_count(self):
        return len(self.nodes)
    
    def send_message(self, message):
        """Send a direct message"""
        self.message_queue.put(message)
    
    def broadcast_message(self, message, exclude_node=None):
        """Broadcast to all nodes except sender (if given)"""
        for node_id, node in self.nodes.items():
            if node_id != exclude_node:
                msg_copy = message.copy()
                msg_copy["dst"] = node_id
                self.message_queue.put(msg_copy)
    
    def start(self):
        self.running = True
        threading.Thread(target=self._process_messages, daemon=True).start()
        print("[VirtualBus] Bus started")
    
    def stop(self):
        self.running = False
    
    def _process_messages(self):
        while self.running:
            try:
                message = self.message_queue.get(timeout=0.1)
                dst_id = message.get("dst")
                if dst_id in self.nodes:
                    self.nodes[dst_id].receive_message(message)
                else:
                    print(f"[VirtualBus] Unknown destination: {dst_id}")
            except queue.Empty:
                continue

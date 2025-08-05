#!/usr/bin/env python3
"""
ISA/CHARGE Modular Motor Control Simulation
Main test script using your existing architecture
"""

import time
from sim.network import VirtualBus
from sim.node import Node  
from sim.protocol import create_motor_command, MessageTypes

class MotorControlNode(Node):
    """
    Motor Control Unit Node - extends your base Node class
    """
    def __init__(self, node_id, bus, num_motors=4):
        super().__init__(node_id, bus)
        self.num_motors = num_motors
        self.motor_states = {}
        
        # Initialize motors
        for i in range(num_motors):
            self.motor_states[i] = {
                "running": False,
                "speed": 0,
                "current": 0.0
            }
        
        # Register command handlers
        self.register_handler(MessageTypes.MOTOR_START, self.handle_motor_start)
        self.register_handler(MessageTypes.MOTOR_STOP, self.handle_motor_stop)
        self.register_handler(MessageTypes.MOTOR_SET_SPEED, self.handle_motor_set_speed)
        self.register_handler(MessageTypes.STATUS_REQUEST, self.handle_status_request)
        self.register_handler(MessageTypes.EMERGENCY_STOP, self.handle_emergency_stop)
        
        print(f"[{self.node_id}] Motor Control Node initialized with {num_motors} motors")

    def handle_motor_start(self, message):
        """Handle motor start command"""
        data = message.get("data", {})
        motor_id = data.get("motor_id")
        speed = data.get("speed", 100)
        
        if motor_id is not None and motor_id < self.num_motors:
            self.motor_states[motor_id]["running"] = True
            self.motor_states[motor_id]["speed"] = speed
            self.motor_states[motor_id]["current"] = abs(speed) * 0.01  # Simulate current
            print(f"[{self.node_id}] ✅ Motor {motor_id} started at speed {speed}")
        else:
            print(f"[{self.node_id}] ❌ Invalid motor ID: {motor_id}")

    def handle_motor_stop(self, message):
        """Handle motor stop command"""
        data = message.get("data", {})
        motor_id = data.get("motor_id")
        
        if motor_id is not None and motor_id < self.num_motors:
            self.motor_states[motor_id]["running"] = False
            self.motor_states[motor_id]["speed"] = 0
            self.motor_states[motor_id]["current"] = 0.0
            print(f"[{self.node_id}] ⏹️  Motor {motor_id} stopped")
        else:
            print(f"[{self.node_id}] ❌ Invalid motor ID: {motor_id}")

    def handle_motor_set_speed(self, message):
        """Handle motor speed change"""
        data = message.get("data", {})
        motor_id = data.get("motor_id")
        speed = data.get("speed", 0)
        
        if motor_id is not None and motor_id < self.num_motors:
            if self.motor_states[motor_id]["running"]:
                self.motor_states[motor_id]["speed"] = speed
                self.motor_states[motor_id]["current"] = abs(speed) * 0.01
                print(f"[{self.node_id}] ⚡ Motor {motor_id} speed set to {speed}")
            else:
                print(f"[{self.node_id}] ⚠️  Motor {motor_id} is not running")
        else:
            print(f"[{self.node_id}] ❌ Invalid motor ID: {motor_id}")

    def handle_status_request(self, message):
        """Handle status request"""
        print(f"[{self.node_id}] 📊 Status Request from {message.get('src')}")
        
        # Send back status
        status_data = {
            "node_id": self.node_id,
            "motors": self.motor_states,
            "timestamp": time.time()
        }
        
        self.send_direct_message(
            message.get("src"), 
            {
                "cmd": MessageTypes.STATUS_RESPONSE,
                "data": status_data
            }
        )

    def handle_emergency_stop(self, message):
        """Handle emergency stop"""
        print(f"[{self.node_id}] 🚨 EMERGENCY STOP!")
        for motor_id in self.motor_states:
            self.motor_states[motor_id]["running"] = False
            self.motor_states[motor_id]["speed"] = 0
            self.motor_states[motor_id]["current"] = 0.0

    def start_motor_local(self, motor_id, speed):
        """Start motor locally (for testing)"""
        if motor_id < self.num_motors:
            self.motor_states[motor_id]["running"] = True
            self.motor_states[motor_id]["speed"] = speed
            self.motor_states[motor_id]["current"] = abs(speed) * 0.01
            print(f"[{self.node_id}] 🔄 Local start: Motor {motor_id} at speed {speed}")

def main():
    print("🎯 ISA/CHARGE Modular Motor Control Simulation")
    print("=" * 60)
    
    # Create virtual bus (your NetworkSimulator)
    print("📡 Creating virtual bus...")
    bus = VirtualBus()
    bus.start()
    
    # Create motor control nodes
    print("\n🔧 Creating motor control nodes...")
    mcu1 = MotorControlNode("MCU_001", bus, num_motors=4)
    mcu2 = MotorControlNode("MCU_002", bus, num_motors=3) 
    mcu3 = MotorControlNode("MCU_003", bus, num_motors=4)
    
    print(f"\n📊 Network Status: {bus.get_node_count()} nodes registered")
    print(f"   Nodes: {', '.join(bus.list_nodes())}")
    
    time.sleep(1)
    
    try:
        # Test 1: Local motor control
        print("\n" + "="*60)
        print("🧪 TEST 1: Local Motor Control")
        print("="*60)
        
        mcu1.start_motor_local(0, 500)
        mcu1.start_motor_local(1, -300)
        time.sleep(1)
        
        # Test 2: Network motor commands
        print("\n" + "="*60)  
        print("🧪 TEST 2: Network Motor Commands")
        print("="*60)
        
        # MCU_001 commands MCU_002 to start motor
        print("MCU_001 -> MCU_002: Start motor 0 at speed 800")
        motor_cmd = create_motor_command(motor_id=0, action="start", speed=800)
        mcu1.send_command("MCU_002", MessageTypes.MOTOR_START, motor_cmd)
        
        time.sleep(1)
        
        # MCU_001 commands MCU_003 to start motor  
        print("MCU_001 -> MCU_003: Start motor 2 at speed 400")
        motor_cmd = create_motor_command(motor_id=2, action="start", speed=400)
        mcu1.send_command("MCU_003", MessageTypes.MOTOR_START, motor_cmd)
        
        time.sleep(1)
        
        # Test 3: Status requests
        print("\n" + "="*60)
        print("🧪 TEST 3: Status Requests")
        print("="*60)
        
        print("MCU_001 requesting status from MCU_002...")
        mcu1.send_command("MCU_002", MessageTypes.STATUS_REQUEST, {"request_type": "all"})
        
        time.sleep(1)
        
        print("MCU_001 requesting status from MCU_003...")
        mcu1.send_command("MCU_003", MessageTypes.STATUS_REQUEST, {"request_type": "all"})
        
        time.sleep(1)
        
        # Test 4: Broadcast emergency stop
        print("\n" + "="*60)
        print("🧪 TEST 4: Emergency Stop Broadcast")
        print("="*60)
        
        print("Broadcasting emergency stop from MCU_001...")
        mcu1.broadcast_command(MessageTypes.EMERGENCY_STOP, {"reason": "Safety test"})
        
        time.sleep(1)
        
        # Test 5: Motor speed changes
        print("\n" + "="*60)
        print("🧪 TEST 5: Motor Speed Control")
        print("="*60)
        
        # Restart a motor and change its speed
        motor_cmd = create_motor_command(motor_id=1, action="start", speed=200)
        mcu2.send_command("MCU_002", MessageTypes.MOTOR_START, motor_cmd)
        
        time.sleep(0.5)
        
        # Change speed
        speed_cmd = create_motor_command(motor_id=1, action="set_speed", speed=600)
        mcu2.send_command("MCU_002", MessageTypes.MOTOR_SET_SPEED, speed_cmd)
        
        time.sleep(1)
        
        print("\n✅ All tests completed!")
        print("🎯 Simulation demonstrates:")
        print("   • Virtual bus communication (CAN/Ethernet simulation)")
        print("   • Motor control node messaging")
        print("   • Status requests and responses")
        print("   • Emergency stop broadcasting")
        print("   • Speed control over network")
        
    except KeyboardInterrupt:
        print("\n⚠️  Simulation interrupted by user")
    
    finally:
        print("\n🔌 Shutting down...")
        bus.stop()
        print("👋 Simulation ended")

if __name__ == "__main__":
    main()
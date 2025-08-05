# ISA / CHARGE Modular Motor Control Simulation

This project simulates a modular motor control unit system for the ISA / CHARGE project. It demonstrates decentralized, message-based control of multiple motor controller nodes.

---

## 🚀 Key Features

✅ **Virtual Bus Communication**  
✅ **Local and Remote Motor Commands**  
✅ **Emergency Stop Broadcasting**  
✅ **Status Requests / Responses**  
✅ **Runs in Local & CI/CD (GitLab) Environments**

---

## 🔧 Simulation Architecture

- **VirtualBus:** Simulates CAN / Ethernet communication.
- **MotorControlNode:** Each node controls multiple motors and handles commands.
- **Protocol:** Defines message structure (JSON-based).

---

## 📂 Project Structure
modular-motor-control-sim/
├── main.py # Main simulation test script
├── .gitlab-ci.yml # CI/CD config
└── sim/
├── init.py
├── network.py # VirtualBus
├── node.py # Node base class
├── protocol.py # Message creation/validation
└── ethernet_comm.py # Ethernet socket simulation 

✅ How to Run:

Locally: python3 main.py

GitLab CI/CD: auto-runs on push

Ethernet simulation: run ethernet_comm.py server/client

✅ Expected Outputs:
Show key logs like motor start/stop, status responses, emergency stops, etc.

✅ Why This Simulation Matters:

Validates communication architecture before hardware tests

Confirms message structure, modularity, scalability




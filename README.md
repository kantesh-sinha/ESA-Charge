# ESA-Charge
Design a modular and decentralized motor control system for a particle-sorting rover using a multi-stage screen. Each unit must be robust, networked, and support motors with encoders.

ISA / CHARGE Project: Modular Particle Sorting Rover
Objective:
To develop a mobile rover system equipped with a multi-stage screen mechanism capable of sorting particles based on size, controlled via modular, decentralized motor control units.

Overview:
The system features a vibrating screen assembly that separates materials into different size fractions while mounted on a mobile rover. The key innovation lies in the modular motor control architecture, which uses microcontroller-based units to independently drive motors for screen vibration, stage actuation, and rover movement.

Each motor control module is:

Designed to support motor voltage ranges between 5V and 24V.
Equipped with its own low-power microcontroller (e.g., ESP32).
Capable of robust communication with other modules and a central controller using protocols like CAN Bus or RS485.
Easily replicable, enabling scalability and reconfigurability.

Subsystems:
Mechanical Sorting Assembly: Multi-stage sieving with vibratory or rotational motion.
Rover Platform: Motorized chassis enabling mobility across test terrain.
Motor Driver Hardware: Custom PCBs featuring H-bridge drivers, current sensing, and power regulation.
Firmware Stack: Code for motor control, inter-device communication, and diagnostics.
Communication Layer: A master-slave protocol with fault tolerance and plug-and-play compatibility.

Key Features:
Modular and scalable hardware
Firmware with real-time control
Reliable communication between modules
Easy unit replacement or expansion

Applications:

Field particle analysis
Modular automation systems
Educational and research platforms



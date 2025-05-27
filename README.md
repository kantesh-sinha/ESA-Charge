# Modular Motor Control System – ISA/CHARGE Project

Welcome to the official repository for the **Modular Motor Control System** developed under the **ISA/CHARGE project**.
The goal of this project is to design and implement a modular, decentralized motor control system for use in a particle-sorting rover application. The system will control various motors involved in the operation of a multi-stage screen-based particle sorting mechanism, but the mechanical implementation is not within the scope of this work. This system is designed for autonomous, scalable, and decentralized control of motors in applications such as particle-sorting rovers. Each unit is modular, low-power, and network-capable, allowing for flexible and robust motor management.

---

## 🚀 Project Overview

The system consists of **Modular Motor Control Units (MCUs)**, each responsible for controlling 3–4 motors. These units are designed to be easily scalable and can communicate with each other or a central controller via **Ethernet (UDP)** or **CAN bus**, depending on system configuration.

The current focus is on **communication design and implementation** using Ethernet via the **Wiznet W55RP20-EVB Pico board**, which combines:

* **RP2040 microcontroller**
* **W5500 Ethernet chip**
* **2MB onboard Flash**

The board provides networking, processing, and storage in one unit, ideal for this modular setup.

---

## 🎯 Objectives

* ✅ **Modular control**: Each unit manages 3–4 motors using daisy-chained SPI motor drivers (e.g., **BTM9021EP**).
* ✅ **Low-power operation**: Supports sleep modes and isolated power regulation.
* ✅ **Flexible communication**: Primary protocol is **Ethernet (UDP)**, with **CAN** as a fallback or future extension.
* ✅ **Decentralized control**: Supports both centralized command systems and peer-to-peer networking.
* ✅ **Open and scalable**: Designed to grow in motor count and communication nodes.

---

## 📡 Communication Architecture

Each unit:

* Listens for commands via **UDP sockets** over Ethernet.
* Parses and routes commands (like motor speed, direction, enable/disable) to motor driver ICs via SPI.
* Responds with acknowledgments or feedback over the network.

The protocol is being designed to include:

```json
{
  "unit_id": 1,
  "motor_id": 2,
  "command": "set_speed",
  "value": 150,
  "direction": "CW"
}
```

---

## 🔧 Hardware Involved

* **W55RP20-EVB Pico Board**
* **BTM9021EP SPI-based motor drivers**
* **Custom PCBs (upcoming) for power and SPI distribution**
* Optional: ESP32 or STM32 as central/master node

---

## 📁 Structure (Planned)

```
/firmware         → Code for RP2040 (Ethernet + SPI communication)
/docs             → Diagrams, architecture flowcharts, and meeting notes
/hardware         → Schematics and board files (to be added)
/test             → PC scripts for sending test UDP packets
README.md
```

---

## 🧠 Learn More

To better understand the context, check out:

* [W55RP20 Product Page](https://docs.wiznet.io/Product/ioNIC/W55RP20)
* [W5500 Ethernet Controller](https://www.wiznet.io/product-item/w5500/)
* [RP2040 Docs (Raspberry Pi Foundation)](https://www.raspberrypi.com/documentation/microcontrollers/rp2040.html)

---

## 🛠️ TODOs

* [x] Initial communication planning (Ethernet UDP preferred)
* [x] Simplified block diagrams
* [ ] Test UDP socket server on W55RP20
* [ ] Define communication protocol
* [ ] SPI control integration with BTM9021EP
* [ ] Multi-unit communication simulation
* [ ] Power regulation & sleep mode testing
* [ ] CAN bus backup implementation (future)

---

## 🤝 Contributions

This is a work in progress under active development. Contributions and suggestions are welcome, especially in:

* Network protocol optimization
* Efficient embedded design
* Motor driver firmware
* Multi-unit addressing and coordination

---

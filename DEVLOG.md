# 🛠 DEVLOG.md — PLC Bridge

_Development log for bridging Linux serial comms with Arduino Opta PLC (UI CDA Research Project)_

---

## 🔄 Project Setup

**May 8, 2025**  
- Initialized GitHub repository: [`plc-bridge`](https://github.com/tank208/plc-bridge)  
- Linked to `@vandals.uidaho.edu` email for academic contribution credit  
- Wrote initial README: problem scope, intended audience, and build instructions  
- Created `.gitignore` and `LICENSE` (MIT)

---

## 🧰 Goals

- Create Python-based serial communication layer between Linux host and Arduino Opta PLC
- Modular command structure: allow future additions of sensor/relay messages
- Respect real-time logic constraints — debounce, confirm, and verify handshake
- Maintain compatibility with field deployment: systemd-safe, lightweight, and testable

---

## 🧪 Current Work

**May 8, 2025**  
- Prototyping `serial_bridge.py` for USB connection using `pyserial`  
- Testing handshake between `/dev/ttyACM0` and Opta USB port  
- Working on robust error handling: USB disconnect / buffer overflow

---

## ⏭️ Next Steps

- Implement serial command parsing (command → response structure)  
- Integrate config file to define available commands for multi-project reuse  
- Build logging wrapper for terminal + file logging (`/logs/bridge.log`)  
- Push first working MVP by next research sync (May 13)

---

## 📝 Notes

- SFML not used — not a visual project, just CLI + logs  
- Will eventually include basic `systemd` service for auto-start on lab devices  
- UI CDA research credit expected for Fall 2025 enrollment

---

> _"Structure systems. Defend mission. Protect purpose."_  
> — W. Hall, UI CDA Research Assistant

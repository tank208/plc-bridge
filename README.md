# plc-bridge

**A Linux-to-Arduino serial communication bridge** for use in OT/ICS research and prototyping.

This project is a Python-based tool designed to simulate and interact with microcontroller-based PLCs over a serial connection. The goal is to build a modular, extensible framework for sending control signals and reading sensor output as part of a SCADA-style system simulation — with future integration into dashboards, protocols (MQTT, Modbus), or industrial device emulation.

---

## Project Goals

- Provide a Linux-native communication layer for Arduino-based PLC systems
- Emulate control systems for SCADA/ICS research and educational labs
- Parse structured sensor data over serial (`KEY=VALUE` format)
- Send actuator commands (`PUMP=ON`, `LIGHT=128`, etc.)
- Serve as a bridge for future dashboard, MQTT, or OT protocol integration

---

## Project Structure

```plaintext
plc-bridge/
├── bridge/                  # Python module
│   ├── __init__.py
│   ├── serial_interface.py  # Serial port logic
│   └── parser.py            # Sensor/command parsing logic
├── main.py                  # CLI entry point
├── arduino_sim.py           # Simulated Arduino output (for dev)
├── requirements.txt         # Python dependencies
├── DEVLOG.md                # Project dev log / research notebook
├── .gitignore
└── README.md
```

## How It Works
```
TEMP=72.5
PUMP=ON
```
  - Python bridge reads and parses the serial output
  - Command-line or script sends back instructions like:
```
LIGHT=255
STATUS?
```

## Development Goals
  - Serial parser engine
  - Arduino simulator
  - Command sender logic
  - MQTT/Modbus layer
  - Real-time dashboard

## Target Audience
  - ICS/OT security researchers
  - Cybersecurity students working with PLC-systems
  - Educators teach I/O logic with Arduino-based kits

## Author & Research Content
  This tool is being developed by Will Hall as part of his undergraduate work-study and independent research under faculty at the University of Idaho Coeur d'Alene (UICDA). It is intended as a foundational tool for future research into OT/ICS cybersecurity and Linux-based field device integration.


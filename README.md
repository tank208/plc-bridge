# PLC Bridge

**Python-based serial bridge for Arduino PLC communication on Linux**

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Overview

PLC Bridge is a Python-based tool that provides seamless serial communication between Linux systems and Arduino-based PLCs. Created to address Arduino's discontinued Linux support for PLC IDE, this bridge enables SCADA-style control systems, industrial automation prototyping, and cybersecurity research.

### Key Features

- **Cross-platform serial communication** with Arduino PLCs
- **KEY=VALUE protocol parsing** for structured sensor data
- **Real-time bidirectional communication** (read sensors, send commands)
- **Configurable connection parameters** (port, baud rate, timeouts)
- **Comprehensive logging** with debug modes
- **Type-safe data conversion** (automatic bool/int/float parsing)
- **Robust error handling** and connection management
- **Extensible architecture** for future MQTT/Modbus integration

## Quick Start

### Prerequisites

- Python 3.8 or higher
- Serial port access (Arduino via USB)
- Compatible Arduino running KEY=VALUE protocol

### Installation

```bash
# Clone the repository
git clone https://github.com/tank208/plc-bridge.git
cd plc-bridge

# Install dependencies
pip install -r requirements.txt

# Make sure your user has serial port access (Linux/Mac)
sudo usermod -a -G dialout $USER  # logout/login required
```

### Basic Usage

```bash
# Linux/Mac
python run.py --port /dev/ttyUSB0 --baudrate 9600

# Windows
python run.py --port COM3 --baudrate 9600

# With verbose logging
python run.py --port COM3 --baudrate 9600 --verbose
```

### Arduino Protocol

Your Arduino should send data in KEY=VALUE format:

```
TEMP=72.5
HUMIDITY=45.2
PUMP=ON
LIGHT=128
STATUS=RUNNING
```

And respond to commands like:

```
PUMP=OFF
LIGHT=255
STATUS?
```

## Architecture

### Project Structure

```
plc-bridge/
├── plc_bridge/              # Main Python package
│   ├── __init__.py         # Package initialization
│   ├── main.py             # Application entry point
│   ├── serial_interface.py # Serial communication layer
│   ├── parser.py           # Protocol parsing logic
│   └── config.py           # Configuration management
├── tests/                   # Unit tests
├── examples/               # Arduino code and usage examples
├── docs/                   # Documentation
├── run.py                  # Simple launcher script
└── requirements.txt        # Python dependencies
```

### Core Components

**SerialBridge** (`serial_interface.py`)
- Manages serial port connections
- Handles connection errors and timeouts
- Provides bidirectional communication

**Parser** (`parser.py`)
- Parses KEY=VALUE protocol messages
- Automatic type conversion (bool, int, float, string)
- Input validation and sanitization

**Main Application** (`main.py`)
- Command-line interface
- Logging configuration
- Main communication loop

## Configuration

### Command Line Options

```
usage: run.py [-h] [--port PORT] [--baudrate BAUDRATE] [--verbose]

Arduino PLC Bridge - Serial communication bridge

optional arguments:
  -h, --help            show this help message and exit
  --port PORT           Serial port (default: /dev/ttyUSB0)
  --baudrate BAUDRATE   Baud rate (default: 9600)
  --verbose, -v         Enable verbose logging
```

### Protocol Specification

The bridge uses a simple KEY=VALUE protocol over serial:

**Data Types:**
- **Boolean**: `ON`/`OFF`, `TRUE`/`FALSE`, `1`/`0`, `HIGH`/`LOW`
- **Numbers**: Integer or floating-point values
- **Strings**: Any other text values

**Special Commands:**
- `STATUS?` - Request immediate status update
- Comments start with `#` and are ignored

## Use Cases

### Industrial Automation
- SCADA system prototyping
- Sensor data collection
- Actuator control systems
- Process monitoring

### Education & Research
- **Cybersecurity Education**: OT/ICS security labs
- **Industrial Control Systems**: Teaching PLC concepts
- **IoT Prototyping**: Bridge to cloud services

### Development & Testing
- Hardware-in-the-loop testing
- Industrial protocol development
- Automation system prototyping

## Development

### Running Tests

```bash
# Run all tests
python -m pytest tests/

# Run with coverage
python -m pytest tests/ --cov=plc_bridge
```

### Code Quality

This project follows Python best practices:

- **PEP 8** style guidelines
- **Type hints** for better code documentation
- **Comprehensive error handling**
- **Modular architecture** for easy extension
- **Unit testing** for reliability

### Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature-name`)
3. Make your changes with tests
4. Run the test suite
5. Submit a pull request

## Future Roadmap

- [ ] **MQTT Integration** - Publish sensor data to MQTT brokers
- [ ] **Modbus Support** - Industrial protocol compatibility
- [ ] **Web Dashboard** - Real-time monitoring interface
- [ ] **Data Logging** - Historical data storage
- [ ] **Configuration Files** - YAML/JSON configuration support
- [ ] **Multi-device Support** - Connect multiple PLCs
- [ ] **RESTful API** - HTTP interface for remote control

## Hardware Compatibility

### Tested Platforms
- **Arduino Uno/Nano** - Primary development platform
- **ESP32/ESP8266** - WiFi-enabled variants
- **Arduino Mega** - Multi-sensor applications

### Serial Interface Requirements
- **Baud Rate**: 9600-115200 (configurable)
- **Data Format**: 8N1 (8 data bits, no parity, 1 stop bit)
- **Flow Control**: None required

## Troubleshooting

### Common Issues

**"Module 'serial' not found"**
```bash
pip install pyserial
```

**"Permission denied" on Linux**
```bash
sudo usermod -a -G dialout $USER
# Then logout and login again
```

**"Port already in use"**
- Close Arduino IDE Serial Monitor
- Check for other programs using the port
- Restart the Arduino

### Debug Mode

Use verbose logging to diagnose issues:
```bash
python run.py --port COM3 --verbose
```

## Academic Context

This project was developed by **Will Hall** as part of undergraduate research at the **University of Idaho Coeur d'Alene (UICDA)** under faculty supervision. It serves as a foundational tool for:

- **OT/ICS Cybersecurity Research**
- **Industrial Control Systems Education**
- **Linux-based Field Device Integration**

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- University of Idaho Coeur d'Alene faculty for research guidance
- Arduino community for protocol inspiration
- Python serial communication library contributors

## Contact

**Will Hall**  
University of Idaho Coeur d'Alene  
[GitHub: @tank208](https://github.com/tank208)

---

**Keywords**: Arduino, PLC, SCADA, Industrial Automation, OT Security, ICS, Serial Communication, Linux, Python
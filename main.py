from bridge.parser import parse_line
from bridge.serial_interface import SerialBridge
import time

def main():
    bridge = SerialBridge(port='/dev/ttyUSB0', baudrate=9600)
    bridge.connect()

    try:
        while True:
            line = bridge.read_line()
            if line:
                print(f"Raw: {line}")
                parsed = parse_line(line)
                if parsed:
                    print(parsed)
                else:
                    print(f"Ignored line: {line}")
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        bridge.close()

if __name__ == "__main__":
    main()

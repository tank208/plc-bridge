import serial

class SerialBridge:
    def __init__(self, port='/dev/ttyUSB0', baudrate=9600):
        self.port = port
        self.baudrate = baudrate
        self.ser = None

    def connect(self):
        self.ser = serial.Serial(self.port, self.baudrate, timeout=1)
        print(f"Connected to {self.port} at {self.baudrate} baud.")

    def read_line(self):
        if self.ser.in_waiting:
            line = self.ser.readline().decode('utf-8').strip()
            return line
        return None

    def send_command(self, command):
        if self.ser:
            self.ser.write((command + "\n").encode('utf-8'))

    def close(self):
        if self.ser:
            self.ser.close()

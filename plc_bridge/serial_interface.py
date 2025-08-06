"""
Serial interface for communicating with Arduino PLC
"""

import serial
import logging
import time

logger = logging.getLogger(__name__)

class SerialBridge:
    """Serial communication bridge to Arduino PLC"""
    
    def __init__(self, port='/dev/ttyUSB0', baudrate=9600, timeout=1):
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.ser = None
        
    def connect(self):
        """Establish serial connection"""
        try:
            self.ser = serial.Serial(
                self.port, 
                self.baudrate, 
                timeout=self.timeout
            )
            # Give Arduino time to reset after connection
            time.sleep(2)
            logger.info(f"Connected to {self.port} at {self.baudrate} baud")
            
        except serial.SerialException as e:
            logger.error(f"Failed to connect to {self.port}: {e}")
            raise
    
    def read_line(self):
        """Read a line from the serial port"""
        if not self.ser or not self.ser.is_open:
            return None
            
        try:
            if self.ser.in_waiting > 0:
                line = self.ser.readline().decode('utf-8').strip()
                return line if line else None
        except (UnicodeDecodeError, serial.SerialException) as e:
            logger.warning(f"Error reading from serial port: {e}")
        
        return None
    
    def send_command(self, command):
        """Send a command to the Arduino"""
        if not self.ser or not self.ser.is_open:
            logger.error("Serial connection not established")
            return False
            
        try:
            message = f"{command}\n"
            self.ser.write(message.encode('utf-8'))
            logger.debug(f"Sent command: {command}")
            return True
        except serial.SerialException as e:
            logger.error(f"Failed to send command '{command}': {e}")
            return False
    
    def close(self):
        """Close the serial connection"""
        if self.ser and self.ser.is_open:
            self.ser.close()
            logger.info("Serial connection closed")
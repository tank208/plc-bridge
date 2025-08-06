#!/usr/bin/env python3
"""
Main entry point for PLC Bridge application
"""

import argparse
import logging
import time
import sys

from .parser import parse_line
from .serial_interface import SerialBridge

def setup_logging(verbose=False):
    """Configure logging for the application"""
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    return logging.getLogger(__name__)

def main():
    """Main application entry point"""
    parser = argparse.ArgumentParser(
        description='Arduino PLC Bridge - Serial communication bridge'
    )
    parser.add_argument(
        '--port', 
        default='/dev/ttyUSB0',
        help='Serial port (default: /dev/ttyUSB0)'
    )
    parser.add_argument(
        '--baudrate', 
        type=int, 
        default=9600,
        help='Baud rate (default: 9600)'
    )
    parser.add_argument(
        '--verbose', '-v', 
        action='store_true',
        help='Enable verbose logging'
    )
    
    args = parser.parse_args()
    logger = setup_logging(args.verbose)
    
    logger.info(f"Starting PLC Bridge on {args.port} at {args.baudrate} baud")
    
    # Create and connect to serial bridge
    bridge = SerialBridge(port=args.port, baudrate=args.baudrate)
    
    try:
        bridge.connect()
        logger.info("Successfully connected to Arduino")
        
        while True:
            line = bridge.read_line()
            if line:
                logger.debug(f"Raw: {line}")
                parsed = parse_line(line)
                if parsed:
                    logger.info(f"Parsed data: {parsed}")
                    # Here you could add logic to handle the parsed data
                    # e.g., send to MQTT, update database, etc.
                else:
                    logger.warning(f"Could not parse line: {line}")
            
            time.sleep(0.1)  # Small delay to prevent CPU spinning
            
    except KeyboardInterrupt:
        logger.info("Received interrupt signal, shutting down...")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        sys.exit(1)
    finally:
        bridge.close()
        logger.info("PLC Bridge stopped")

if __name__ == "__main__":
    main()
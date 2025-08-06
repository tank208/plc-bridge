"""
PLC Bridge - Python-based serial bridge to Arduino PLC
"""

__version__ = "0.1.0"
__author__ = "Will Hall"

# Make key classes easily importable
from .serial_interface import SerialBridge
from .parser import parse_line

__all__ = ['SerialBridge', 'parse_line']
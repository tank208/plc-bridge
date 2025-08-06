#!/usr/bin/env python3
"""
Simple launcher for the PLC Bridge application
"""

import sys
import os

# Add the project directory to Python path
project_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_dir)

# Import and run the main application
from plc_bridge.main import main

if __name__ == "__main__":
    main()
"""
Data parser for Arduino PLC KEY=VALUE protocol
"""

import logging

logger = logging.getLogger(__name__)

def parse_line(line):
    """
    Parse a KEY=VALUE line from Arduino PLC
    
    Args:
        line (str): Input line from serial port
        
    Returns:
        dict: Parsed key-value pair with type conversion, or empty dict if invalid
    """
    if not line or "=" not in line:
        return {}
    
    try:
        key, value = line.strip().split("=", 1)
        key = key.strip().upper()  # Standardize key format
        value = value.strip()
        
        # Convert value to appropriate type
        converted_value = convert_value(value)
        
        logger.debug(f"Parsed {key}={converted_value} (type: {type(converted_value).__name__})")
        return {key: converted_value}
        
    except Exception as e:
        logger.warning(f"Failed to parse line '{line}': {e}")
        return {}

def convert_value(value_str):
    """
    Convert string value to appropriate Python type
    
    Args:
        value_str (str): String value to convert
        
    Returns:
        Converted value (bool, int, float, or str)
    """
    value_upper = value_str.upper()
    
    # Boolean conversion
    if value_upper in ['ON', 'TRUE', '1', 'HIGH', 'ENABLED']:
        return True
    elif value_upper in ['OFF', 'FALSE', '0', 'LOW', 'DISABLED']:
        return False
    
    # Numeric conversion
    try:
        if '.' in value_str:
            return float(value_str)
        else:
            return int(value_str)
    except ValueError:
        # Keep as string if conversion fails
        return value_str
def parse_line(line):
    """
    Takes a line like 'TEMP=72.5' and returns {'TEMP': '72.5'}.
    If the line doesn't contain '=', returns None.
    """
    if "=" in line:
        key, value = line.strip().split("=", 1)
        return {key: value}
    return None

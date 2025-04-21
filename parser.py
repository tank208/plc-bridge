def parse_line(line):
    if "=" in line:
        key, value = line.strip().split("=", 1)
        return {key: value}
    return {}

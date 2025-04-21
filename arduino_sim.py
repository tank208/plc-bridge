import time
import random

with open("simulated_serial.txt", "w") as f:
    while True:
        temp = round(70 + random.random() * 10, 2)
        pump = "ON" if random.random() > 0.5 else "OFF"

        f.write(f"TEMP={temp}\n")
        f.write(f"PUMP={pump}\n")
        f.flush()
        time.sleep(1)

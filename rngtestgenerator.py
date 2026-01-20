import math
from pathlib import Path
NUM_STREAMS = 20
BITS_PER_STREAM = 1000000
output_path = Path.home() / "Documents" / "rngtest.txt"

def hash01(x, k):
    y = x + 0.6180339887498949 * (k + 1)
    y = (y * 1e5) % 1
    return y

def fractal_stopping_time(x, p=0.7, max_depth=30):
    depth = 0
    while depth < max_depth:
        h = hash01(x, depth)
        if h >= p:
            break
        x = (2 * x) % 1
        depth += 1
    return depth + 1

def fp_step(x, p=0.7):
    tau = fractal_stopping_time(x, p=p)
    for _ in range(tau):
        x = 4 * x * (1 - x)
    return x

def extract_bit(x):
    return (int(x * (1 << 53)) >> 52) & 1

with open(output_path, "w") as f:
    x = 0.123456789
    for i in range(NUM_STREAMS):
        x += 1e-9 * i
        for _ in range(BITS_PER_STREAM):
            x = fp_step(x, p=0.68)
            f.write(str(extract_bit(x)))
        f.write("\n")
        print(f"Finished stream {i+1}/{NUM_STREAMS}")

print("Saved file to:", output_path)

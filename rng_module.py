import math
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

def fp_rng(seed=0.314159, steps=10, p=0.7, scale=10000):
    x = seed
    out = []

    for _ in range(steps):
        tau = fractal_stopping_time(x, p=p)
        for _ in range(tau):
            x = 4 * x * (1 - x)
        out.append(math.floor(scale * x)) 

    return out

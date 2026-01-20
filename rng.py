import math
# Deterministic hash mapping (x, k) -> [0, 1)
def hash01(x, k):
    y = x + 0.6180339887498949 * (k + 1)   # golden ratio rotation different offset for different values of k
    y = (y * 1e5) % 1 # multiply bu 10^5, then consider the fractional part
    return y

# Deterministic analogue of fractal percolation stopping time.
def fractal_stopping_time(x, p=0.7, max_depth=30):
    depth = 0
    while depth < max_depth:
        h = hash01(x, depth)
        if h >= p:
            break
        x = (2 * x) % 1    # zoom into next dyadic subinterval
        depth += 1
    return depth + 1

# The actual part of the Random Number Generator
def fp_rng(seed=0.314159, steps=10, p=0.7):
    x = seed
    out = [] # This stores the generated values
    for _ in range(steps):
        tau = fractal_stopping_time(x, p=p) # Tau Determines how long the chaotic system would run, and the value of tau is not so deterministic at all
        for _ in range(tau):
            x = 4 * x * (1 - x)   # logistic map (chaotic core)
        out.append(math.floor(10000 * x)) # This converts the random number between (0,1) to a random number between (0,10000) -- this can be modified
    return out

# Generting 1000 Random Numbers
if __name__ == "__main__":
    sequence = fp_rng(seed=0.271828, steps=1000, p=0.68)
    for i, val in enumerate(sequence):
        print(f"{i+1:2d}: {val}")

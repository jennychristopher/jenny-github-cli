# main.py

import math

def sigmoid(x: float) -> float:
    """Compute the sigmoid activation."""
    return 1 / (1 + math.exp(-x))

if __name__ == "__main__":
    print(sigmoid(0))   # Should print 0.5


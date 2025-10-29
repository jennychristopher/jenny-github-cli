# main.py

import math

def sigmoid(x: float) -> float:
    """Compute the sigmoid activation."""
    return 1 / (1 + math.exp(-x))
    
def add(a,b):
    return a+b
    
def mul(a,b):
    return a * b
   
def sub(a,b):
    return a - b
    
def div(a,b):
    return a / b

if __name__ == "__main__":
    print(sigmoid(0))   # Should print 0.5


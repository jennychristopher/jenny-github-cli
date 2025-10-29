# test_main.py

from main import sigmoid
import math

def test_sigmoid_basic():
    assert math.isclose(sigmoid(0), 0.5, rel_tol=1e-9)

def test_sigmoid_positive():
    assert sigmoid(5) > 0.99

def test_sigmoid_negative():
    assert sigmoid(-5) < 0.01


import math
from adddiv_model import addmul

def test_sigmoid_basic():
    assert math.isclose(addmul(1,1,1), 2)
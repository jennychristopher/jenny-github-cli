import math
from addcdiv_model.addcdiv_model import addcdiv

def test_addcdiv():
    assert math.isclose(addcdiv(1,1,1), 2)

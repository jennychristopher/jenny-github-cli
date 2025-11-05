import math
from addmul_model import addmul

def test_addmul():
    assert math.isclose(addmul(1,1,1),2)
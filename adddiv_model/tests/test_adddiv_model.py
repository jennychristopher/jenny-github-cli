
import math
from adddiv_model import adddiv

def test_sigmoid_basic():
    assert math.isclose(adddiv(1,1,1), 2)
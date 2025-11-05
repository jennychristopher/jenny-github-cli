# Add Pytest for addmul custom model 
import math
from addmul_model.addmul_model import addmul

def test_sigmoid_basic():
    assert math.isclose(addmul(1,1,1), 2)
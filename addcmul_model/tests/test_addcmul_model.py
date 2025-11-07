import math
from addcmul_model.addcmul_model import addcmul

def test_addcmul():
    assert math.isclose(addcmul(1,1,1), 2)

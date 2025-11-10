# Pytest file for testing addcdiv
import math
from addcdiv_model.addcdiv_model import addcdiv
from compound_model.compound_model import compound_model

def test_addcdiv():
    assert math.isclose(addcdiv(1,1,1), 2)
    assert math.isclose(compound_model(1,1,1), 4)

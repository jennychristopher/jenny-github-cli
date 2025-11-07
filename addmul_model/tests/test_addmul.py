# Add Pytest for addmul custom model - new
import math
from addmul_model.addmul_model import addmul
from compound_model.compound_model import compound_model
import pytest


def test_addmul():
    assert math.isclose(addmul(1,1,1), 2)
    assert math.isclose(compound_model(1,1,1), 4)
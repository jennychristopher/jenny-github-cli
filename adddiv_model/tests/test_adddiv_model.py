# Add test for adddiv op
import math
from adddiv_model.adddiv_model import adddiv
import pytest

def test_adddiv():
    assert math.isclose(adddiv(1,1,1), 2)
# Add test for adddiv op
import math
from adddiv_model.adddiv_model import adddiv
import pytest

@pytest.mark.adddiv_model
def test_adddiv():
    assert math.isclose(adddiv(1,1,1), 2)
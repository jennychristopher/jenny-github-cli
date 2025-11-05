# Add Pytest for addmul custom model - new
import math
from addmul_model.addmul_model import addmul
import pytest

@pytest.mark.addmul
def test_addmul():
    assert math.isclose(addmul(1,1,1), 2)
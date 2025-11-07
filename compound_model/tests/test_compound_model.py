
import math
from compound_model.compound_model import compound_model
import pytest


def test_compound():
    assert math.isclose(compound_model(1,1,1), 4)
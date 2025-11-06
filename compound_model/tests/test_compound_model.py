import math
import pytest
from compound_model.compound_model import compound_model
from adddiv_model.adddiv_model import adddiv

def test_compound_model():
    return math.isclose(compound_model(1,1,1), 4)
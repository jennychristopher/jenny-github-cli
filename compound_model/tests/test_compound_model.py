# Pytest for testing compound op
import math
from compound_model.compound_model import compound_model
def test_compound_model():
    assert math.isclose(compound_model(1,1,1), 4)
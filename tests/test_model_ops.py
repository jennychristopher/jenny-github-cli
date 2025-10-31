# test_main.py
import src
from src.model_ops import sigmoid,add,mul,sub,div
import math
import pytest

@pytest.mark.activation
def test_sigmoid_basic():
    assert math.isclose(sigmoid(0), 0.5, rel_tol=1e-9)

@pytest.mark.activation
def test_sigmoid_positive():
    assert sigmoid(5) > 0.99

@pytest.mark.activation
def test_sigmoid_negative():
    assert sigmoid(-5) < 0.01
    
@pytest.mark.math_ops
def test_add():
    assert math.isclose(add(2,3),5)

@pytest.mark.math_ops
def test_div():
    assert math.isclose(div(10,5),2)


@pytest.mark.math_ops
def test_mul():
    assert math.isclose(mul(10,50),500)
    
@pytest.mark.math_ops
def test_sub():
    assert math.isclose(sub(40,50),-10)

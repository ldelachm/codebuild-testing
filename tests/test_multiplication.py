import pytest
from calculator import multiply

def test_multiply_positive_numbers():
    assert multiply(3, 4) == 12

def test_multiply_negative_numbers():
    assert multiply(-3, -4) == 12

def test_multiply_mixed_numbers():
    assert multiply(-3, 4) == -12

def test_multiply_by_zero():
    assert multiply(5, 0) == 0
    assert multiply(0, 5) == 0

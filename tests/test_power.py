import pytest
from calculator import power

def test_power_positive_numbers():
    assert power(2, 3) == 8

def test_power_negative_base():
    assert power(-2, 3) == -8

def test_power_zero_exponent():
    assert power(5, 0) == 1

def test_power_negative_exponent():
    assert power(2, -2) == 0.25

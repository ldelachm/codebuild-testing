import pytest
from calculator import divide

def test_divide_positive_numbers():
    assert divide(8, 2) == 4

def test_divide_negative_numbers():
    assert divide(-8, -2) == 4

def test_divide_mixed_numbers():
    assert divide(-8, 2) == -4

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(5, 0)

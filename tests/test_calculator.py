'''Testing My Calculator'''
from calculator import add, subtract, multiply, divide

def test_addition():
    assert add(2,2) == 4

def test_subtraction():
    assert subtract(2,2) == 0

def test_multiplication():
    assert multiply(3,3) == 9

def test_division():
    assert divide(6,2) == 3


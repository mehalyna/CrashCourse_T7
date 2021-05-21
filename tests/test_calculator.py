import pytest
from src.calculator import Calculator


def test_add1():
    calculator = Calculator()
    assert calculator.add(10, 7) == 17


def test_subtract1():
    calculator = Calculator()
    assert calculator.subtract(10, 7) == 3


def test_multiply1():
    calculator = Calculator()
    assert calculator.multiply(10, 7) == 70


def test_divide1():
    calculator = Calculator()
    assert calculator.divide(10, 7) == 10 / 7


def test_add2():
    calculator = Calculator()
    assert calculator.add(10, -7) == 3


def test_subtract2():
    calculator = Calculator()
    assert calculator.subtract(10, -7) == 17


def test_multiply2():
    calculator = Calculator()
    assert calculator.multiply(10, -7) == -70


def test_divide2():
    calculator = Calculator()
    assert calculator.divide(-10, -7) == 10 / 7
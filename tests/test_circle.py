import pytest
from src.circle import Circle

def test_get_area1():
    circo = Circle(20)
    assert circo.getArea() == 1257


def test_get_perimeter1():
    circo = Circle(20)
    assert circo.getPerimeter() == 126


def test_get_area2():
    circo = Circle(4.4)
    assert circo.getArea() == 61


def test_get_perimeter2():
    circo = Circle(4.4)
    assert circo.getPerimeter() == 28
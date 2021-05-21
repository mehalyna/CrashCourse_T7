import pytest
from src.player import Player

def test_get_age1():
    p1 = Player("Jhon", 22, 175, 64)
    assert p1.get_age() == "Jhon is age 22"


def test_get_height1():
    p1 = Player("Jhon", 22, 175, 64)
    assert p1.get_height() == "Jhon is 175cm"


def test_get_weight1():
    p1 = Player("Jhon", 22, 175, 64)
    assert p1.get_weight() == "Jhon weighs 64kg"

import pytest
from src.ones_threes_nines import OnesThreesNines

def test_ones_threes_nines1():
    n1 = OnesThreesNines(0)
    assert n1.ones == 0


def test_ones_threes_nines2():
    n2 = OnesThreesNines(1)
    assert n2.threes == 0


def test_ones_threes_nines3():
    n2 = OnesThreesNines(1)
    assert n2.threes == 0


def test_ones_threes_nines4():
    n4 = OnesThreesNines(17)
    assert n4.ones == 17
    assert n4.threes == 5
    assert n4.nines == 1


def test_ones_threes_nines5():
    n5 = OnesThreesNines(31)
    assert n5.ones == 31
    assert n5.threes == 10
    assert n5.nines == 3



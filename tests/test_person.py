import pytest
from src.person import Person

def test_taste1():
    p1 = Person("Sam", ["ice cream", "pie", "apples"], ["carrots", "bananas", "cheese", "lettuce"])
    assert p1.taste("ice cream") == "Sam eats the ice cream and loves it!"
    assert p1.taste("carrots") == "Sam eats the carrots and hates it!"
    assert p1.taste("brocolli") == "Sam eats the brocolli!"
    assert p1.taste("lettuce") == "Sam eats the lettuce and hates it!"
    assert p1.taste("cheese") == "Sam eats the cheese and hates it!"
    assert p1.taste("pie") == "Sam eats the pie and loves it!"
    assert p1.taste("apples") == "Sam eats the apples and loves it!"
    assert p1.taste("bananas") == "Sam eats the bananas and hates it!"

def test_taste2():
    p2 = Person("Mitchell", [], ["brocolli", "lettuce", "cheese", "pie", "apples", "bananas", "ice cream", "carrots"])
    assert p2.taste("ice cream") == "Mitchell eats the ice cream and hates it!"
    assert p2.taste("carrots") == "Mitchell eats the carrots and hates it!"
    assert p2.taste("brocolli") == "Mitchell eats the brocolli and hates it!"
    assert p2.taste("lettuce") == "Mitchell eats the lettuce and hates it!"
    assert p2.taste("cheese") == "Mitchell eats the cheese and hates it!"
    assert p2.taste("pie") == "Mitchell eats the pie and hates it!"
    assert p2.taste("apples") == "Mitchell eats the apples and hates it!"
    assert p2.taste("bananas") == "Mitchell eats the bananas and hates it!"


def test_taste3():
    p3 = Person("Julie", ["brocolli", "lettuce", "cheese", "pie", "apples", "bananas", "ice cream", "carrots"], [])
    assert p3.taste("ice cream") == "Julie eats the ice cream and loves it!"
    assert p3.taste("carrots") == "Julie eats the carrots and loves it!"
    assert p3.taste("brocolli") == "Julie eats the brocolli and loves it!"
    assert p3.taste("lettuce") == "Julie eats the lettuce and loves it!"
    assert p3.taste("cheese") == "Julie eats the cheese and loves it!"
    assert p3.taste("pie") == "Julie eats the pie and loves it!"
    assert p3.taste("apples") == "Julie eats the apples and loves it!"
    assert p3.taste("bananas") == "Julie eats the bananas and loves it!"


def test_taste5():
    p5 = Person("Joshua", ["ice cream", "pie", "cheese", "bananas"], ["lettuce", "apples"])
    assert p5.taste("ice cream") == "Joshua eats the ice cream and loves it!"
    assert p5.taste("carrots") == "Joshua eats the carrots!"
    assert p5.taste("brocolli") == "Joshua eats the brocolli!"
    assert p5.taste("lettuce") == "Joshua eats the lettuce and hates it!"
    assert p5.taste("cheese") == "Joshua eats the cheese and loves it!"
    assert p5.taste("pie") == "Joshua eats the pie and loves it!"
    assert p5.taste("apples") == "Joshua eats the apples and hates it!"
    assert p5.taste("bananas") == "Joshua eats the bananas and loves it!"



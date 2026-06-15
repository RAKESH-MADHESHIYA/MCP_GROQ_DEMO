from mathserver import add, multiply
from weather import get_weather


def test_add():
    assert add(10, 20) == 30


def test_multiply():
    assert multiply(18, 12) == 216


def test_weather():
    result = get_weather("California")

    assert "California" in result
    assert "sunny" in result
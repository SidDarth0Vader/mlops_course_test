from src.math_utils import add, subtract


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(1, 0) == 1


def test_subtract():
    assert subtract(2, 3) == -1
    assert subtract(-1, 1) == -2
    assert subtract(0, 0) == 0
    assert subtract(1, 0) == 1

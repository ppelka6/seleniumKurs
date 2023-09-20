import pytest

@pytest.mark.skip
def test_method():
    x=5
    y=2
    assert x + y  == 7,"assertion failed, expected 7"
    assert x + y == 2,"assertion failed, expected 2"

@pytest.mark.xfail
def test_method2():
    x=5
    y=2
    assert x + y == 7, "assertion failed, expected 7"
    assert x + y == 2, "assertion failed, expected 2"

def random_name():
    x=5
    y=2
    assert x + y == 7, "assertion failed, expected 7"
    assert x + y == 2, "assertion failed, expected 2"

def random_name_test():
    x=5
    y=2
    assert x + y == 7, "assertion failed, expected 7"
    assert x + y == 2, "assertion failed, expected 2"
import pytest

@pytest.fixture
def number():
    a=10
    b=20
    c=25
    return [a,b,c]

@pytest.mark.xfail
def test_method1(number):
    x=15
    assert number[0] ==x
@pytest.mark.skip
def test_method2(number):
    y=20
    assert number[1]==y
def test_method3(number):
    Z=25
    assert number[2]==Z


#TO RUN
#   pytest test_fixture.py 
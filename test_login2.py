import pytest

@pytest.mark.regression
def testlogin():
    print('login successfull')

def testlogoff():
    print("logofffff")

@pytest.mark.sanity
def testcalc():
    assert 2+2 == 4

@pytest.mark.xfail
def testcalc1():
    assert 2+2 == 6

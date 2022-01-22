import pytest


def testlogin():
    print('login successfull')

def testlogoff():
    print("logofffff")

@pytest.mark.skip
def testcalc():
    assert 2+2 == 4

@pytest.mark.regression
def testcalc2():
    assert 2+2 == 4


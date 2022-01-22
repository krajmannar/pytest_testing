import pytest

@pytest.fixture(scope = "session", autouse = True)
def test_setUp(browser):
    if browser == "chrome":
        print("launch chrome")
    elif browser == "ff":
        print("Launch Firefox")
    else:
        print("provide valid browser")

    # print('Launch browser')
    print('Login')
    print('Browse product')
    # return 'rajmannar'
    #
    yield
    print('Logoff')
    print('Close Browser')
#
# @pytest.fixture()
# def setup_list():
#     print('in setup_list fixture...')
#     city = ['newyork', 'delhi', 'bangalore', 'chennai']
#     return city

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope = "session", autouse = True)
def browser(request):
    return request.config.getoption("--browser")

def func():
    pass

def func1():
    pass


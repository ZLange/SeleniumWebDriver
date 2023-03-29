import pytest


@pytest.fixture()
def setup():
    print("Running method level setUp")
    yield  # needed to run the same in the end of tests
    print("Running method level tearDown")


@pytest.fixture(scope="class")
def onetimesetup(request, browser):
    print("Running one time setup")
    if browser == "firefox":
        value = 10
        print("running tests on FF")
    else:
        value = 20
        print("running tests on chrome")

    if request.cls is not None:
        request.cls.value = value

    yield value  # needed to run the same in the end of tests
    print("Running one time tearDown")


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of os")


@pytest.fixture(scope="session")  # define command line options
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")  # define command line options
def osType(request):
    return request.config.getoption("--osType")

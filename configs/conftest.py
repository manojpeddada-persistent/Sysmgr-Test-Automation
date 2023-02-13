import pytest

def pytest_addoption(parser):
    parser.addoption("--name", action="store")
    parser.addoption("--test", action="store")
    parser.addoption("--server", action="store")

@pytest.fixture(scope='session')
def name(request):
    name_value = request.config.option.name
    if name_value is None:
        pytest.skip()
    return name_value

def test(request):
    test_value = request.config.option.test
    if test_value is None:
        pytest.skip()
    return test_value

def server(request):
    server_value = request.config.option.server
    if server_value is None:
        pytest.skip()
    return server_value


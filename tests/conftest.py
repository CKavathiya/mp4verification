import pytest
def pytest_addoption(parser):
    parser.addoption("--path", action="store", default="path to the MP4 file")


@pytest.fixture
def path(request):
    return request.config.getoption("--path")
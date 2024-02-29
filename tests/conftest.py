import pytest

def pytest_addoption(parser):
    parser.addoption("--num_records", action="store", default=10, help="Number of records to generate")

@pytest.fixture
def num_records(request):
    return int(request.config.getoption("--num_records"))

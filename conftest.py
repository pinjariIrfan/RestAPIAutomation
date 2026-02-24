import pytest

@pytest.fixture(scope="session", autouse=True)
def print_suite_info():
    print("\n===== REST API Automation Suite Started =====")
    yield
    print("\n===== Suite Completed =====")
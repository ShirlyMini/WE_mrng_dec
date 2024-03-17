import pytest

@pytest.fixture()
def setup1():
    print("TC SETUP1")
    yield
    print('TC TEARDOWN1')

@pytest.fixture()
def setup2():
    print("TC SETUP2")
    yield True, "return value"
    print('TC TEARDOWN1')

@pytest.fixture(scope='class')
def setup3():
    print("TS SETUP CLASS")
    yield
    print("TS TEARDOWN CLASS")

@pytest.fixture(scope='module')
def setup4():
    print("SETUP MODULE")
    yield
    print("TEARDOWN MODULE")


def pytest_configure(config):
    # <markers: <name: desc>>
    config.addinivalue_line("markers", "functionality: functional testing")
    config.addinivalue_line("markers", "sanity: sanity testing")
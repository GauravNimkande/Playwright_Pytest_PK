import pytest


@pytest.fixture
def setup():
    print("Setup Envirnment")

    yield
    print("Tear Down")


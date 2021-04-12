import pytest

@pytest.fixture
def app():
    from src import app
    yield app

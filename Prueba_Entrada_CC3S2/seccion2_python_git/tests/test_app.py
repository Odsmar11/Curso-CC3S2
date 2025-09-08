import pytest
from app.app import summarize

@pytest.fixture
def sample():
    return ["1", "2", "3"]

def test_ok(sample):
    # Arrange–Act–Assert
    # Act
    with pytest.raises(NotImplementedError):
        summarize(sample)

def test_empty():
    with pytest.raises(Exception):
        summarize([])

def test_non_numeric():
    with pytest.raises(Exception):
        summarize(["a", "2"])
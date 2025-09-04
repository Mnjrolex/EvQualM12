import pytest

# A fixture providing setup for tests
@pytest.fixture(scope="function")
def setup_data():
    print("Setting up data")
    return {"key": "value"}

# A test with a marker and uses the fixture
@pytest.mark.smoke
@pytest.mark.positive
def test_example_positive(setup_data):
    assert setup_data["key"] == "value"

# Another test with a different marker, also using the fixture
@pytest.mark.negative
def test_example_negative(setup_data):
    assert setup_data.get("missing_key") is None

# Test without markers but using the fixture
def test_no_marker(setup_data):
    assert isinstance(setup_data, dict)

# Fixture with a marker on the fixture itself (rare usage)
@pytest.fixture
@pytest.mark.usefixtures("setup_data")
def another_fixture():
    # Setup or return something else
    return "some resource"

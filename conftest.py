import pytest

@pytest.fixture
def base_url():
    return "https://jsonplaceholder.typicode.com"

@pytest.fixture
def sample_post():
    return {
        "title": "My Test Post",
        "body": "This is test body content",
        "userId": 1
    }

@pytest.fixture
def sample_user():
    return {
        "name": "Test User",
        "username": "testuser",
        "email": "test@example.com"
    }
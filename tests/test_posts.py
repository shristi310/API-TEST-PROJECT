import requests
import pytest

BASE_URL = "https://jsonplaceholder.typicode.com"

# TEST 1 - Check if API responds
def test_get_all_posts_status():
    response = requests.get(f"{BASE_URL}/posts")
    assert response.status_code == 200

# TEST 2 - Check total number of posts
def test_get_all_posts_count():
    response = requests.get(f"{BASE_URL}/posts")
    data = response.json()
    assert len(data) == 100

# TEST 3 - Check single post exists
def test_get_single_post_status():
    response = requests.get(f"{BASE_URL}/posts/1")
    assert response.status_code == 200

# TEST 4 - Check post has correct fields
def test_single_post_structure():
    response = requests.get(f"{BASE_URL}/posts/1")
    data = response.json()
    assert "id" in data
    assert "title" in data
    assert "body" in data
    assert "userId" in data

# TEST 5 - Check post data is correct
def test_single_post_data():
    response = requests.get(f"{BASE_URL}/posts/1")
    data = response.json()
    assert data["id"] == 1
    assert type(data["title"]) == str
    assert type(data["userId"]) == int

# TEST 6 - Check wrong post id gives 404
def test_invalid_post_id():
    response = requests.get(f"{BASE_URL}/posts/9999")
    assert response.status_code == 404

# TEST 7 - Check creating a new post
def test_create_post(sample_post):
    response = requests.post(f"{BASE_URL}/posts", json=sample_post)
    data = response.json()
    assert response.status_code == 201
    assert data["title"] == "My Test Post"

# TEST 8 - Check response time is fast
def test_response_time():
    response = requests.get(f"{BASE_URL}/posts")
    assert response.elapsed.total_seconds() < 3

# TEST 9 - Check deleting a post
def test_delete_post():
    response = requests.delete(f"{BASE_URL}/posts/1")
    assert response.status_code == 200

# TEST 10 - Check updating a post
def test_update_post():
    updated = {
        "title": "Updated Title",
        "body": "Updated body",
        "userId": 1
    }
    response = requests.put(f"{BASE_URL}/posts/1", json=updated)
    data = response.json()
    assert response.status_code == 200
    assert data["title"] == "Updated Title"
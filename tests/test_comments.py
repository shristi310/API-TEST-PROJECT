import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

# TEST 1 - Get all comments
def test_get_all_comments_status():
    response = requests.get(f"{BASE_URL}/comments")
    assert response.status_code == 200

# TEST 2 - Check total comments count
def test_get_all_comments_count():
    response = requests.get(f"{BASE_URL}/comments")
    data = response.json()
    assert len(data) == 500

# TEST 3 - Check comment structure
def test_comment_structure():
    response = requests.get(f"{BASE_URL}/comments/1")
    data = response.json()
    assert "id" in data
    assert "name" in data
    assert "email" in data
    assert "body" in data
    assert "postId" in data

# TEST 4 - Check comment email format
def test_comment_email_format():
    response = requests.get(f"{BASE_URL}/comments/1")
    data = response.json()
    assert "@" in data["email"]

# TEST 5 - Get comments by post
def test_get_comments_by_post():
    response = requests.get(f"{BASE_URL}/posts/1/comments")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
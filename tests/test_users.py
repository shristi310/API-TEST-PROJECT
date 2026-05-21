import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

# TEST 1 - Get all users
def test_get_all_users_status():
    response = requests.get(f"{BASE_URL}/users")
    assert response.status_code == 200

# TEST 2 - Check total users count
def test_get_all_users_count():
    response = requests.get(f"{BASE_URL}/users")
    data = response.json()
    assert len(data) == 10

# TEST 3 - Check single user exists
def test_get_single_user():
    response = requests.get(f"{BASE_URL}/users/1")
    assert response.status_code == 200

# TEST 4 - Check user has correct fields
def test_user_structure():
    response = requests.get(f"{BASE_URL}/users/1")
    data = response.json()
    assert "id" in data
    assert "name" in data
    assert "email" in data
    assert "username" in data

# TEST 5 - Check email has @ symbol
def test_user_email_format():
    response = requests.get(f"{BASE_URL}/users/1")
    data = response.json()
    assert "@" in data["email"]

# TEST 6 - Check invalid user gives 404
def test_invalid_user():
    response = requests.get(f"{BASE_URL}/users/9999")
    assert response.status_code == 404

# TEST 7 - Check user data types
def test_user_data_types():
    response = requests.get(f"{BASE_URL}/users/1")
    data = response.json()
    assert type(data["id"]) == int
    assert type(data["name"]) == str
    assert type(data["email"]) == str
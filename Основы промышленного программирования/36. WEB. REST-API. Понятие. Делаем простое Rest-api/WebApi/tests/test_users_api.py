import requests

BASE_URL = "http://127.0.0.1:8080"


def test_get_all_users():
    resp = requests.get(f"{BASE_URL}/api/users")
    users = resp.json()["users"]
    assert "address" in users[-1]


def test_get_user():
    resp = requests.get(f"{BASE_URL}/api/users/1")
    user = resp.json()["users"][0]
    assert "address" in user


def test_wrong_get_user():
    resp = requests.get(f"{BASE_URL}/api/users/0")
    assert resp.status_code == 404 and "Not Found" in resp.json()["error"]


def test_wrong_type_get_user():
    resp = requests.get(f"{BASE_URL}/api/users/string")
    assert resp.status_code == 400 and "Bad Request" in resp.json()["error"]

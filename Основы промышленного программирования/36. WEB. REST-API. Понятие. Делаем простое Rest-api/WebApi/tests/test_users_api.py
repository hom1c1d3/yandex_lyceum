import requests

BASE_URL = "http://127.0.0.1:8080"


def test_get_all_users():
    resp = requests.get(f"{BASE_URL}/api/users")
    users = resp.json()["users"]
    assert "address" in users[-1]
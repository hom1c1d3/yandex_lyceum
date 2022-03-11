import datetime

import requests
from werkzeug.security import generate_password_hash

BASE_URL = "http://127.0.0.1:8080"
API_VERSION = "api/v2"


def test_get_all_users():
    resp = requests.get(f"{BASE_URL}/{API_VERSION}/users")
    users = resp.json()["users"]
    assert "address" in users[-1]


def test_get_user():
    resp = requests.get(f"{BASE_URL}/{API_VERSION}/users/1")
    user = resp.json()["users"][0]
    assert "address" in user


def test_get_missing_user():
    resp = requests.get(f"{BASE_URL}/{API_VERSION}/users/0")
    assert resp.status_code == 404 and "Not Found" in resp.json()["message"]


def test_user_post():
    data = {
        "id": 6,
        "surname": "Sanders",
        "name": "Teddy",
        "age": 27,
        "position": "programmer",
        "speciality": "IT specialist",
        "address": "module_2",
        "email": "sanders@mars.org",
        "hashed_password": generate_password_hash("teddy_bear27"),
        "modified_date": datetime.datetime.now().isoformat(),
    }
    resp = requests.post(f"{BASE_URL}/{API_VERSION}/users", params=data)
    resp.raise_for_status()
    resp = requests.get(f"{BASE_URL}/{API_VERSION}/users")
    users = resp.json()["users"]
    assert users[-1]["name"] == "Teddy"


def test_missing_user_edit():
    # Редактирование несуществующего пользователя
    user_id = 0
    data = {}
    resp = requests.put(f"{BASE_URL}/{API_VERSION}/users/{user_id}", json=data)
    assert resp.status_code == 404 and "Not Found" in resp.json()["message"]


def test_user_edit():
    user_id = 2
    data = {
        "id": 2,
        "surname": "Sanders",
        "name": "Teddy",
        "age": 27,
        "position": "programmer",
        "speciality": "IT specialist",
        "address": "module_2",
        "email": "sanders_manders@mars.org",  # уникальная почта из-за предыдущих тестов
        "hashed_password": generate_password_hash("teddy_bear27"),
        "modified_date": datetime.datetime.now().isoformat(),
    }
    resp = requests.put(f"{BASE_URL}/{API_VERSION}/users/{user_id}", params=data)
    resp.raise_for_status()
    resp = requests.get(f"{BASE_URL}/{API_VERSION}/users/{user_id}")
    users = resp.json()["users"][0]
    assert users["name"] == "Teddy"


def test_missing_user_delete():
    user_id = 0
    resp = requests.delete(
        f"{BASE_URL}/{API_VERSION}/users/{user_id}")  # несуществующий пользователь
    assert resp.status_code == 404 and "Not Found" in resp.json()["message"]


def test_user_delete():
    user_id = 1
    resp = requests.delete(f"{BASE_URL}/{API_VERSION}/users/{user_id}")
    resp.raise_for_status()
    resp = requests.get(f"{BASE_URL}/{API_VERSION}/users/{user_id}")  # проверяем что такого
    # пользователя уже нет
    assert resp.status_code == 404 and "Not Found" in resp.json()["message"]
import datetime

import requests
from werkzeug.security import generate_password_hash

BASE_URL = "http://127.0.0.1:8080"
API_VERSION = "api"


def test_get_all_users():
    resp = requests.get(f"{BASE_URL}/{API_VERSION}/users")
    users = resp.json()["users"]
    assert "address" in users[-1]


def test_get_user():
    resp = requests.get(f"{BASE_URL}/{API_VERSION}/users/1")
    user = resp.json()["users"][0]
    assert "address" in user


def test_wrong_get_user():
    resp = requests.get(f"{BASE_URL}/{API_VERSION}/users/0")
    assert resp.status_code == 404 and "Not Found" in resp.json()["error"]


def test_wrong_type_get_user():
    resp = requests.get(f"{BASE_URL}/{API_VERSION}/users/string")
    assert resp.status_code == 400 and "Bad Request" in resp.json()["error"]


def test_user_post_empty():
    # пустой запрос
    data = {}
    resp = requests.post(f"{BASE_URL}/{API_VERSION}/users", json=data)
    assert resp.status_code == 400 and "Empty request" in resp.json()["error"]


def test_user_post_with_missing_fields():
    # Поле modified_date отсутсвует
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
    }
    resp = requests.post(f"{BASE_URL}/{API_VERSION}/users", json=data)
    assert resp.status_code == 400 and "Missing fields" in resp.json()["error"]


def test_user_post_wrong_type_hash():
    data = {
        "id": 6,
        "surname": "Sanders",
        "name": "Teddy",
        "age": 27,
        "position": "programmer",
        "speciality": "IT specialist",
        "address": "module_2",
        "email": "sanders@mars.org",
        "hashed_password": generate_password_hash("teddy_bear27", method="pbkdf2:sha1"),
        "modified_date": datetime.datetime.now().isoformat(),
    }
    resp = requests.post(f"{BASE_URL}/{API_VERSION}/users", json=data)
    assert resp.status_code == 400 and "Wrong type hash" in resp.json()["error"]


def test_user_post_with_existing_id():
    # существующий пользователь
    data = {
        "id": 1,
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
    resp = requests.post(f"{BASE_URL}/{API_VERSION}/users", json=data)
    assert resp.status_code == 400 and "Id already exists" in resp.json()["error"]


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
    resp = requests.post(f"{BASE_URL}/{API_VERSION}/users", json=data)
    resp.raise_for_status()
    resp = requests.get(f"{BASE_URL}/{API_VERSION}/users")
    users = resp.json()["users"]
    assert users[-1]["name"] == "Teddy"


def test_wrong_type_edit_user():
    resp = requests.put(f"{BASE_URL}/{API_VERSION}/users/string")
    assert resp.status_code == 400 and "Bad Request" in resp.json()["error"]


def test_missing_user_edit():
    # Редактирование несуществующего пользователя
    user_id = 0
    data = {}
    resp = requests.put(f"{BASE_URL}/{API_VERSION}/users/{user_id}", json=data)
    assert resp.status_code == 404 and "Not Found" in resp.json()["error"]


def test_user_empty_edit():
    user_id = 1
    data = {}
    resp = requests.put(f"{BASE_URL}/{API_VERSION}/users/{user_id}", json=data)
    assert resp.status_code == 400 and "Empty request" in resp.json()["error"]


def test_user_edit_with_missing_fields():
    # Поле modified_date отсутсвует
    user_id = 1
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
    }
    resp = requests.put(f"{BASE_URL}/{API_VERSION}/users/{user_id}", json=data)
    assert resp.status_code == 400 and "Missing fields" in resp.json()["error"]


def test_user_edit_wrong_type_hash():
    user_id = 1
    data = {
        "id": 6,
        "surname": "Sanders",
        "name": "Teddy",
        "age": 27,
        "position": "programmer",
        "speciality": "IT specialist",
        "address": "module_2",
        "email": "sanders@mars.org",
        "hashed_password": generate_password_hash("teddy_bear27", method="pbkdf2:sha1"),
        "modified_date": datetime.datetime.now().isoformat(),
    }
    resp = requests.put(f"{BASE_URL}/{API_VERSION}/users/{user_id}", json=data)
    assert resp.status_code == 400 and "Wrong type hash" in resp.json()["error"]


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
    resp = requests.put(f"{BASE_URL}/{API_VERSION}/users/{user_id}", json=data)
    resp.raise_for_status()
    resp = requests.get(f"{BASE_URL}/{API_VERSION}/users/{user_id}")
    users = resp.json()["users"][0]
    assert users["name"] == "Teddy"


def test_missing_user_delete():
    user_id = 0
    resp = requests.delete(f"{BASE_URL}/{API_VERSION}/users/{user_id}")  # несуществующий пользователь
    assert resp.status_code == 404 and "Not Found" in resp.json()["error"]


def test_wrong_type_delete_user():
    resp = requests.delete(f"{BASE_URL}/{API_VERSION}/users/string")
    assert resp.status_code == 400 and "Bad Request" in resp.json()["error"]


def test_user_delete():
    user_id = 1
    resp = requests.delete(f"{BASE_URL}/{API_VERSION}/users/{user_id}")
    resp.raise_for_status()
    resp = requests.get(f"{BASE_URL}/{API_VERSION}/users/{user_id}")  # проверяем что такого
    # пользователя уже нет
    assert resp.status_code == 404 and "Not Found" in resp.json()["error"]
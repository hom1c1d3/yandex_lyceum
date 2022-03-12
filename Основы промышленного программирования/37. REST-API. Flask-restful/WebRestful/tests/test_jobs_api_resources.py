import datetime

import requests

BASE_URL = "http://127.0.0.1:8080"
API_VERSION = "api/v2"


def test_get_all_jobs():
    resp = requests.get(f"{BASE_URL}/{API_VERSION}/jobs")
    jobs = resp.json()["jobs"]
    assert "is_finished" in jobs[-1]


def test_get_job():
    resp = requests.get(f"{BASE_URL}/{API_VERSION}/jobs/1")
    job = resp.json()["jobs"][0]
    assert "is_finished" in job


def test_get_missing_job():
    resp = requests.get(f"{BASE_URL}/{API_VERSION}/jobs/0")
    assert resp.status_code == 404 and "Not Found" in resp.json()["message"]


def test_job_post():
    data = {
        "team_leader_id": 4,
        "job": "Working hard",
        "work_size": 100,
        "collaborators": "1, 2, 3",
        "start_date": datetime.datetime.now().isoformat(),
        "end_date": None,
        "is_finished": False
    }
    resp = requests.post(f"{BASE_URL}/{API_VERSION}/jobs", params=data)
    resp.raise_for_status()
    resp = requests.get(f"{BASE_URL}/{API_VERSION}/jobs")
    jobs = resp.json()["jobs"]
    assert jobs[-1]["job"] == "Working hard"


def test_missing_job_delete():
    job_id = 0
    resp = requests.delete(f"{BASE_URL}/{API_VERSION}/jobs/{job_id}")  # несуществующая работа
    assert resp.status_code == 404 and "Not Found" in resp.json()["message"]


def test_job_delete():
    job_id = 1
    resp = requests.delete(f"{BASE_URL}/{API_VERSION}/jobs/{job_id}")
    resp.raise_for_status()
    resp = requests.get(
        f"{BASE_URL}/{API_VERSION}/jobs/{job_id}")  # проверяем что такой работы уже нет
    assert resp.status_code == 404 and "Not Found" in resp.json()["message"]


def test_missing_job_edit():
    job_id = 0
    resp = requests.put(f"{BASE_URL}/{API_VERSION}/jobs/{job_id}")  # несуществующая работа
    assert resp.status_code == 404 and "Not Found" in resp.json()["message"]


def test_job_edit():
    job_id = 2
    data = {
        "team_leader_id": 4,
        "job": "Working hard",
        "work_size": 100,
        "collaborators": "1, 2, 3",
        "start_date": datetime.datetime.now().isoformat(),
        "end_date": None,
        "is_finished": False
    }
    resp = requests.put(f"{BASE_URL}/{API_VERSION}/jobs/{job_id}", params=data)
    resp.raise_for_status()
    resp = requests.get(f"{BASE_URL}/{API_VERSION}/jobs/{job_id}")
    resp.raise_for_status()
    job = resp.json()["jobs"][0]
    assert job["job"] == "Working hard"

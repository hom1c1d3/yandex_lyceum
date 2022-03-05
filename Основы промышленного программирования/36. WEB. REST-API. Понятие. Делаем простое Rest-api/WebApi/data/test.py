import requests


BASE_URL = "http://127.0.0.1:8080"


def test_get_all_jobs():
    resp = requests.get(f"{BASE_URL}/api/jobs")
    jobs = resp.json()["jobs"]
    assert "is_finished" in jobs[-1]


def test_get_job():
    resp = requests.get(f"{BASE_URL}/api/jobs/1")
    job = resp.json()["jobs"][0]
    assert "is_finished" in job


def test_wrong_get_job():
    resp = requests.get(f"{BASE_URL}/api/jobs/0")
    assert resp.status_code == 404 and resp.json()["error"] == "Not found"


def test_wrong_type_get_job():
    resp = requests.get(f"{BASE_URL}/api/jobs/string")
    assert resp.status_code == 400 and resp.json()["error"] == "Bad request"

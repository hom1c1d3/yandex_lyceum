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
    assert resp.status_code == 404 and "Not Found" in resp.json()["error"]


def test_wrong_type_get_job():
    resp = requests.get(f"{BASE_URL}/api/jobs/string")
    assert resp.status_code == 400 and "Bad Request" in resp.json()["error"]


def test_job_post():
    import datetime
    data = {
        "id": 5,
        "team_leader_id": 4,
        "job": "Working hard",
        "work_size": 100,
        "collaborators": "1, 2, 3",
        "start_date": datetime.datetime.now().isoformat(),
        "send_date": None,
        "is_finished": False}
    resp = requests.post(f"{BASE_URL}/api/jobs", json=data)
    resp.raise_for_status()
    resp = requests.get(f"{BASE_URL}/api/jobs")
    jobs = resp.json()["jobs"]
    assert jobs[-1]["job"] == "Working hard"


def test_job_post_with_existing_id():
    import datetime
    data = {
        "id": 1,
        "team_leader_id": 4,
        "job": "Working hard",
        "work_size": 100,
        "collaborators": "1, 2, 3",
        "start_date": datetime.datetime.now().isoformat(),
        "send_date": None,
        "is_finished": False}
    resp = requests.post(f"{BASE_URL}/api/jobs", json=data)
    assert resp.status_code == 400 and "Id already exists" in resp.json()["error"]
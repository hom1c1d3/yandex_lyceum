import requests
from datetime import datetime


def prize(host, port, **kwargs):
    resp = requests.get(f"http://{host}:{port}")
    data = resp.json()
    deltas = {}
    for boat, date in kwargs.items():
        schedule_date = data[boat]
        date = datetime.strptime(date, "%d.%m")
        schedule_date = datetime.strptime(schedule_date, "%d.%m")
        delta = date - schedule_date
        delta = delta.days
        if delta:
            deltas[boat] = delta
    return deltas

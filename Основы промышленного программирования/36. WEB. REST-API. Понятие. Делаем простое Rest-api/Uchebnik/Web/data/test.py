import requests


print(requests.get("http://127.0.0.1:8080/api/news").json())
print(requests.get("http://127.0.0.1:8080/api/news/2").json())
print(requests.get("http://127.0.0.1:8080/api/news/7").json())
print(requests.get("http://127.0.0.1:8080/api/news/erew").json())
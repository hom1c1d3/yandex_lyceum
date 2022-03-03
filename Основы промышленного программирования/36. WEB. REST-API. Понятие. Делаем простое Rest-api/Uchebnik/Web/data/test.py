import requests


print(requests.get("http://127.0.0.1:8080/api/news").json())
print(requests.get("http://127.0.0.1:8080/api/news/2").json())
print(requests.get("http://127.0.0.1:8080/api/news/7").json())
print(requests.get("http://127.0.0.1:8080/api/news/erew").json())

print(requests.post('http://localhost:8080/api/news').json())

print(requests.post('http://localhost:8080/api/news',
           json={'title': 'Заголовок'}).json())

print(requests.post('http://localhost:8080/api/news',
           json={'title': 'Заголовок',
                 'content': 'Текст новости',
                 'user_id': 1,
                 'is_private': False}).json())


print(requests.delete('http://localhost:8080/api/news/999').json())
# новости с id = 999 нет в базе

print(requests.delete('http://localhost:8080/api/news/1').json())
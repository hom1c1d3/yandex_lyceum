from requests import get, post, delete

print(get('http://localhost:8080/api/v2/news').json())
print(get('http://localhost:8080/api/v2/news/4').json())
print(get('http://localhost:8080/api/v2/news/6').json())
print(get('http://localhost:8080/api/v2/news/q').json())
print(post('http://localhost:8080/api/v2/news').json())
print(post('http://localhost:8080/api/v2/news', json={'title': 'Заголовок'}).json())
print(post('http://localhost:8080/api/v2/news', json={
    'title': 'Первая запись',
    'content': 'Текст новости1',
    'user_id': 2,
    'is_private': False,
    'is_published': True}).json())
print(delete('http://localhost:8080/api/v2/news/999').json()) # новости с id = 999 нет в базе
print(delete('http://localhost:8080/api/v2/news/10').json())

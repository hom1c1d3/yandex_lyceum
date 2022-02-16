# Импорт библиотеки
import sqlite3

# Подключение к БД
con = sqlite3.connect("films_db.sqlite")

# Создание курсора
cur = con.cursor()

# Выполнение запроса и получение всех результатов
result = cur.execute("""SELECT * FROM films
            WHERE year = 2010""").fetchall()

# Вывод результатов на экран
for elem in result:
    print(elem)

con.close()
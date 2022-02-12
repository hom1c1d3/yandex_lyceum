from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def mission_name():
    return "Миссия Колонизация Марса"


@app.route('/index')
def mission_deviz():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    promotion_lines = ['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
                       'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!',
                       'Присоединяйся!']
    return '<br>'.join(promotion_lines)


@app.route('/image_mars')
def image_mars():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/mars.png')}" width="256" height="256">
                    <p>Вот какая она, красная планета!</p>
                  </body>
                </html>"""


if __name__ == '__main__':
    app.run(port=8080, host="")

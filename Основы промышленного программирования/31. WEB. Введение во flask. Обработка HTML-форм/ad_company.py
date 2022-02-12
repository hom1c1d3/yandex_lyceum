from flask import Flask

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


if __name__ == '__main__':
    app.run(port=8080, host="")

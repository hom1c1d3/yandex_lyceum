from flask import Flask

app = Flask(__name__)


@app.route('/')
def mission_name():
    return "Миссия Колонизация Марса"


@app.route('/index')
def mission_deviz():
    return "И на Марсе будут яблони цвести!"


if __name__ == '__main__':
    app.run(port=8080, host="")

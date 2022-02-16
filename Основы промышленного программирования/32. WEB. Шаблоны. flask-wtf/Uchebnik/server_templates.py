import json

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
@app.route('/index')
def index():
    params = {'username': "Ученик Яндекс.Лицея", "title": "Домашняя страница 1501"}
    return render_template("index.html",
                           **params)


@app.route('/odd_even')
def odd_even():
    params = {"number": 0}
    return render_template("odd_even.html",
                           **params)


@app.route('/news')
def news():
    with open('json/news.json', 'r', encoding='utf8') as fd:
        params = json.load(fd)
    return render_template("news.html",
                           news=params)


@app.route('/queue')
def queue():
    return render_template("queue.html")


@app.route('/software')
def software():
    params = {'username': "Ученик Яндекс.Лицея", "title": "Приложение"}
    return render_template("software.html", **params)


if __name__ == '__main__':
    app.run(port=8080, host="")

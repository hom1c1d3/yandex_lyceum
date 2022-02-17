from flask import Flask, render_template
from data import db_session
from data.news import News


app = Flask(__name__)
app.config["SECRET_KEY"] = "SECRETTOKEN"


@app.route("/")
def index():
    db_sess = db_session.create_session()
    news = db_sess.query(News).filter(News.is_private == False).all()
    return render_template("index.html", news=news)


def main():
    db_session.global_init("db/blogs.db")
    app.run("", port=8080)


if __name__ == '__main__':
    main()
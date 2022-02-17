from flask import Flask
from data import db_session
from data.news import News


app = Flask(__name__)
app.config["SECRET_KEY"] = "SECRETTOKEN"


def main():
    db_session.global_init("db/blogs.db")
    db_sess = db_session.create_session()

    news = News()
    news.title = "Первая новость"
    news.content = "Привет блог"
    news.user_id = 1
    news.is_private = False

    db_sess.add(news)

    db_sess.commit()
    db_sess.close()


if __name__ == '__main__':
    main()
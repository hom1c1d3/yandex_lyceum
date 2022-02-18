from flask import Flask
from data import db_session


app = Flask(__name__)
app.config["SECRET_KEY"] = "SECRETTOKEN"


def main():
    db_session.global_init("db/blogs.db")
    app.run("", port=8080)


if __name__ == '__main__':
    main()
from flask import Flask, make_response, jsonify
from flask_restful import reqparse, abort, Api, Resource

from data import db_session, news_resources


app = Flask(__name__)
app.config["SECRET_KEY"] = "verysecretkeyblin"
api = Api(app, catch_all_404s=True)


def main():
    db_session.global_init("db/blogs.db")
    api.add_resource(news_resources.NewsListResource, "/api/v2/news")
    api.add_resource(news_resources.NewsResource, "/api/v2/news/<int:news_id>")
    app.run("", port=8080)


if __name__ == '__main__':
    main()
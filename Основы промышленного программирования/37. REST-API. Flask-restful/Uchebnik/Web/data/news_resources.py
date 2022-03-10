from flask import jsonify
from flask_restful import abort, Resource

from . import db_session
from .news import News
from .reqparse import parser


def abort_news_missing(news_id):
    db_sess = db_session.create_session()
    news = db_sess.get(News, news_id)
    if not news:
        abort(404, message=f"News {news_id} not found")


class NewsResource(Resource):

    def get(self, news_id):
        abort_news_missing(news_id)
        db_sess = db_session.create_session()
        news = db_sess.get(News, news_id)
        return jsonify(
            {"news": [news.to_dict(only=("title", "content", "user_id", "user.name", "is_private"))]})

    def delete(self, news_id):
        abort_news_missing(news_id)
        db_sess = db_session.create_session()
        news = db_sess.get(News, news_id)
        db_sess.delete(news)
        db_sess.commit()
        return jsonify({"success": "OK"})


class NewsListResource(Resource):

    def get(self):
        db_sess = db_session.create_session()
        news = db_sess.query(News).all()
        return jsonify(
            {"news": [item.to_dict(only=("title", "content", "user_id", "user.name", "is_private")) for
                      item in news]})

    def post(self):
        args = parser.parse_args()
        db_sess = db_session.create_session()
        news = News(
            title=args["title"],
            content=args["content"],
            is_private=args["is_private"],
            user_id=args["user_id"],
        )
        db_sess.add(news)
        db_sess.commit()
        return jsonify({"success": "OK"})

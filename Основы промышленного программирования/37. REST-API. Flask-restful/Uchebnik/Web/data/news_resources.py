from flask import jsonify
from flask_restful import abort, Resource

from . import db_session
from .news import News


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
        return jsonify({"news": [news.to_dict(only=("title", "content", "user_id", "is_private"))]})

    def delete(self, news_id):
        abort_news_missing(news_id)
        db_sess = db_session.create_session()
        news = db_sess.get(News, news_id)
        db_sess.delete(news)
        db_sess.commit()
        return jsonify({"success": "OK"})
    
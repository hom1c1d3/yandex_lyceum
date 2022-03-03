import flask
from flask import request, jsonify
from . import db_session
from .news import News


blueprint = flask.Blueprint(
    "news_api",
    __name__,
    template_folder="templates"
)


@blueprint.route("/api/news")
def get_news():
    db_sess = db_session.create_session()
    news = db_sess.query(News).all()
    return jsonify(
        {
            "news": [item.to_dict(only=("title", "content", "user.name")) for item in news]
        }
    )


@blueprint.route("/api/news/<int:news_id>", methods=['GET'])
def get_news_1(news_id):
    db_sess = db_session.create_session()
    news = db_sess.query(News).get(news_id)
    if not news:
        return jsonify({"error": "Not found"})
    return jsonify(
        {
            "news": news.to_dict(only=("title", "content", "user_id", "is_private"))
        }
    )

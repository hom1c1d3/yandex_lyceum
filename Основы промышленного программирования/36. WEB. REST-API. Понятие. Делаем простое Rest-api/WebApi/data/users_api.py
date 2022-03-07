from flask import Blueprint, jsonify
from werkzeug.exceptions import BadRequest

from . import db_session
from .users import User

users_api = Blueprint("users_api", __name__, template_folder="templates", url_prefix="/api/users")


@users_api.route("/")
def get_users():
    db_sess = db_session.create_session()
    users = db_sess.query(User).all()
    return jsonify(
        {"users": [user.to_dict() for user in users]}
    )


@users_api.route("/<path:_>", methods=["GET", "DELETE", "PUT"])
def handle_invalid_path(_):
    raise BadRequest()


@users_api.errorhandler(404)
def not_found(error):
    return jsonify({"error": f"{error.name}. {error.description}"}), error.code


@users_api.errorhandler(400)
def not_found(error):
    return jsonify({"error": f"{error.name}. {error.description}"}), error.code

from datetime import datetime

from flask import Blueprint, jsonify, request
from werkzeug.exceptions import BadRequest, NotFound

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


@users_api.route("/<int:user_id>")
def get_user(user_id):
    db_sess = db_session.create_session()
    user: User = db_sess.get(User, user_id)
    if not user:
        raise NotFound()
    return jsonify(
        {"users": [user.to_dict()]}
    )


@users_api.route("/", methods=["POST"])
def create_user():
    if not request.json:
        raise BadRequest("Empty request")
    allowed_fields = ["id", "surname", "name", "age", "position", "speciality", "address", "email",
                      "hashed_password", "modified_date", ]
    if not all(key in request.json for key in allowed_fields):
        raise BadRequest("Missing fields")
    db_sess = db_session.create_session()
    password_hash = request.json["hashed_password"]
    hash_method = password_hash.split("$")[0]
    if ":".join(hash_method.split(':')[:2]) != "pbkdf2:sha256":
        raise BadRequest("Wrong type hash. Must be werkzeug type.")
    modified_date = request.json["modified_date"]
    if modified_date:
        modified_date = datetime.fromisoformat(modified_date)
    user = User(
        id=request.json["id"],
        surname=request.json["surname"],
        name=request.json["name"],
        age=request.json["age"],
        position=request.json["position"],
        speciality=request.json["speciality"],
        address=request.json["address"],
        email=request.json["email"],
        hashed_password=password_hash,
        modified_date=modified_date,
    )
    if db_sess.query(User).filter(User.id == user.id).first():
        raise BadRequest("Id already exists")
    db_sess.add(user)
    db_sess.commit()
    return jsonify({'success': 'OK'})


@users_api.route("/<int:user_id>", methods=["PUT"])
def edit_user(user_id):
    db_sess = db_session.create_session()
    user = db_sess.get(User, user_id)
    if not user:
        raise NotFound()
    if not request.json:
        raise BadRequest("Empty request")
    allowed_fields = ["id", "surname", "name", "age", "position", "speciality", "address", "email",
                      "hashed_password", "modified_date", ]
    if not all(key in request.json for key in allowed_fields):
        raise BadRequest("Missing fields")
    password_hash = request.json["hashed_password"]
    hash_method = password_hash.split("$")[0]
    if ":".join(hash_method.split(':')[:2]) != "pbkdf2:sha256":
        raise BadRequest("Wrong type hash. Must be werkzeug type.")
    modified_date = request.json["modified_date"]
    if modified_date:
        modified_date = datetime.fromisoformat(modified_date)
    user.id = request.json["id"]
    user.surname = request.json["surname"]
    user.name = request.json["name"]
    user.age = request.json["age"]
    user.position = request.json["position"]
    user.speciality = request.json["speciality"]
    user.address = request.json["address"]
    user.email = request.json["email"]
    user.hashed_password = password_hash
    user.modified_date = modified_date
    db_sess.commit()
    return jsonify({'success': 'OK'})


@users_api.route("/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    db_sess = db_session.create_session()
    user = db_sess.get(User, user_id)
    if not user:
        raise NotFound()
    db_sess.delete(user)
    db_sess.commit()
    return jsonify({'success': 'OK'})


@users_api.route("/<path:_>", methods=["GET", "DELETE", "PUT"])
def handle_invalid_path(_):
    raise BadRequest()


@users_api.errorhandler(404)
def not_found(error):
    return jsonify({"error": f"{error.name}. {error.description}"}), error.code


@users_api.errorhandler(400)
def not_found(error):
    return jsonify({"error": f"{error.name}. {error.description}"}), error.code

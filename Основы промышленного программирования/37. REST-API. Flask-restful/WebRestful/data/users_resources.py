from flask import jsonify
from flask_restful import Resource, abort, Api

from . import db_session
from .reqparse_user import parser
from .users import User


def abort_missing_user(user_id):
    db_sess = db_session.create_session()
    user = db_sess.get(User, user_id)
    if not user:
        abort(404, message=f"User {user_id} Not Found")


class UsersResource(Resource):

    def get(self, user_id):
        abort_missing_user(user_id)
        db_sess = db_session.create_session()
        user: User = db_sess.get(User, user_id)
        return jsonify(
            {"users": [user.to_dict()]}
        )

    def delete(self, user_id):
        abort_missing_user(user_id)
        db_sess = db_session.create_session()
        user = db_sess.get(User, user_id)
        db_sess.delete(user)
        db_sess.commit()
        return jsonify({'success': 'OK'})

    def put(self, user_id):
        abort_missing_user(user_id)
        args = parser.parse_args()
        db_sess = db_session.create_session()
        user = db_sess.get(User, user_id)
        user.surname = args["surname"]
        user.name = args["name"]
        user.age = args["age"]
        user.position = args["position"]
        user.speciality = args["speciality"]
        user.address = args["address"]
        user.email = args["email"]
        user.hashed_password = args["hashed_password"]
        user.modified_date = args.get("modified_date")
        db_sess.commit()
        return jsonify({'success': 'OK'})


class UsersListResource(Resource):

    def get(self):
        db_sess = db_session.create_session()
        users = db_sess.query(User).all()
        return jsonify(
            {"users": [user.to_dict() for user in users]}
        )

    def post(self):
        args = parser.parse_args()
        db_sess = db_session.create_session()
        user = User(
            surname=args["surname"],
            name=args["name"],
            age=args["age"],
            position=args["position"],
            speciality=args["speciality"],
            address=args["address"],
            email=args["email"],
            hashed_password=args["hashed_password"],
            modified_date=args.get("modified_date"),
        )
        db_sess.add(user)
        db_sess.commit()
        return jsonify({'success': 'OK'})


def init_api_routes(api: Api):
    url_prefix = "/api/v2/users"
    api.add_resource(UsersResource, f"{url_prefix}/<int:user_id>")
    api.add_resource(UsersListResource, url_prefix)

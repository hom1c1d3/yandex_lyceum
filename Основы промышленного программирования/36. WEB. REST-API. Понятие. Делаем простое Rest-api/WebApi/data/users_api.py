from flask import Blueprint, jsonify
from werkzeug.exceptions import BadRequest

users_api = Blueprint("users_api", __name__, template_folder="templates", url_prefix="/api/users")


@users_api.route("/<path:_>", methods=["GET", "DELETE", "PUT"])
def handle_invalid_path(_):
    raise BadRequest()


@users_api.errorhandler(404)
def not_found(error):
    return jsonify({"error": f"{error.name}. {error.description}"}), error.code


@users_api.errorhandler(400)
def not_found(error):
    return jsonify({"error": f"{error.name}. {error.description}"}), error.code

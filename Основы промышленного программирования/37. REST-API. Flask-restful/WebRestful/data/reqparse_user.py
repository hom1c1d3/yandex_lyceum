from datetime import datetime
from flask_restful import reqparse


def check_password_hash(password_hash):
    hash_method = password_hash.split("$")[0]
    if ":".join(hash_method.split(':')[:2]) != "pbkdf2:sha256":
        raise ValueError("Wrong type hash. Must be werkzeug type.")
    return password_hash


parser = reqparse.RequestParser()
parser.add_argument("surname", required=True)
parser.add_argument("name", required=True)
parser.add_argument("age", required=True, type=int)
parser.add_argument("position", required=True)
parser.add_argument("speciality", required=True)
parser.add_argument("address", required=True)
parser.add_argument("email", required=True)
parser.add_argument("hashed_password", required=True, type=check_password_hash)
parser.add_argument("modified_date", type=lambda arg: datetime.fromisoformat(arg))
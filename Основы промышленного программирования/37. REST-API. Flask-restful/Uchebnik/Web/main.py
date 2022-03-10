from flask import Flask, make_response, jsonify
from flask_restful import reqparse, abort, Api, Resource

from data import db_session


app = Flask(__name__)
app.config["SECRET_KEY"] = "verysecretkeyblin"



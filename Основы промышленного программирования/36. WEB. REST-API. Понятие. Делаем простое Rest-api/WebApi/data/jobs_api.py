from flask import Blueprint, jsonify

from . import db_session
from .jobs import Jobs


jobs_api = Blueprint("jobs_api", __name__, template_folder="templates")


@jobs_api.route("/api/jobs")
def get_jobs():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    return jsonify(
        {"jobs": [job.to_dict() for job in jobs]}
    )
from flask import Blueprint, jsonify
from werkzeug.exceptions import BadRequest, NotFound

from . import db_session
from .jobs import Jobs


jobs_api = Blueprint("jobs_api", __name__, template_folder="templates", url_prefix="/api/jobs")


@jobs_api.route("/")
def get_jobs():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    return jsonify(
        {"jobs": [job.to_dict() for job in jobs]}
    )


@jobs_api.route("/<int:job_id>")
def get_job(job_id):
    db_sess = db_session.create_session()
    job: Jobs = db_sess.get(Jobs, job_id)
    if not job:
        raise NotFound()
    return jsonify(
        {"jobs": [job.to_dict()]}
    )


@jobs_api.route("/<path:_>")
def handle_invalid_path(_):
    raise BadRequest()


@jobs_api.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found"}), error.code


@jobs_api.errorhandler(400)
def not_found(error):
    return jsonify({"error": "Bad request"}), error.code

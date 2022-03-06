from datetime import datetime

from flask import Blueprint, jsonify, request
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


@jobs_api.route("/", methods=["POST"])
def create_job():
    if not request.json:
        raise BadRequest("Empty request")
    allowed_fields = ["team_leader_id", "job", "work_size", "collaborators", "start_date",
                      "end_date", "is_finished"]
    if not all(key in request.json for key in allowed_fields):
        raise BadRequest("Missing fields")
    db_sess = db_session.create_session()
    start_date = request.json["start_date"]
    if start_date:
        start_date = datetime.fromisoformat(start_date)
    end_date = request.json["end_date"]
    if end_date:
        end_date = datetime.fromisoformat(end_date)
    job = Jobs(
        id=request.json["id"],
        team_leader_id=request.json["team_leader_id"],
        job=request.json["job"],
        work_size=request.json["work_size"],
        collaborators=request.json["collaborators"],
        start_date=start_date,
        end_date=end_date,
        is_finished=request.json["is_finished"],
    )
    if db_sess.query(Jobs).filter(Jobs.id == job.id).first():
        raise BadRequest("Id already exists")
    db_sess.add(job)
    db_sess.commit()
    return jsonify({'success': 'OK'})


@jobs_api.route("/<int:job_id>", methods=["DELETE"])
def delete_job(job_id):
    db_sess = db_session.create_session()
    job: Jobs = db_sess.get(Jobs, job_id)
    if not job:
        raise NotFound()
    db_sess.delete(job)
    db_sess.commit()
    return jsonify({'success': 'OK'})


@jobs_api.route("/<int:job_id>", methods=["PUT"])
def edit_job(job_id):
    db_sess = db_session.create_session()
    job: Jobs = db_sess.get(Jobs, job_id)
    if not job:
        raise NotFound()
    if not request.json:
        raise BadRequest("Empty request")
    allowed_fields = ["team_leader_id", "job", "work_size", "collaborators", "start_date",
                      "end_date", "is_finished"]
    if not all(key in request.json for key in allowed_fields):
        raise BadRequest("Missing fields")
    start_date = request.json["start_date"]
    if start_date:
        start_date = datetime.fromisoformat(start_date)
    end_date = request.json["end_date"]
    if end_date:
        end_date = datetime.fromisoformat(end_date)
    job.id = request.json["id"]
    job.team_leader_id = request.json["team_leader_id"]
    job.job = request.json["job"]
    job.work_size = request.json["work_size"]
    job.collaborators = request.json["collaborators"]
    job.start_date = start_date
    job.end_date = end_date
    job.is_finished = request.json["is_finished"]
    db_sess.commit()
    return jsonify({'success': 'OK'})


@jobs_api.route("/<path:_>", methods=["GET", "DELETE", "PUT"])
def handle_invalid_path(_):
    raise BadRequest()


@jobs_api.errorhandler(404)
def not_found(error):
    return jsonify({"error": f"{error.name}. {error.description}"}), error.code


@jobs_api.errorhandler(400)
def not_found(error):
    return jsonify({"error": f"{error.name}. {error.description}"}), error.code

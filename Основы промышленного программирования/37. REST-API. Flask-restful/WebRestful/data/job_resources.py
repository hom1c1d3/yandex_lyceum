from flask import jsonify
from flask_restful import Resource, abort, Api

from . import db_session
from .reqparse_job import parser
from .jobs import Jobs


def abort_missing_job(job_id):
    db_sess = db_session.create_session()
    job = db_sess.get(Jobs, job_id)
    if not job:
        abort(404, message=f"Job {job_id} Not Found")


class JobResource(Resource):

    def get(self, job_id):
        abort_missing_job(job_id)
        db_sess = db_session.create_session()
        job: Jobs = db_sess.get(Jobs, job_id)
        return jsonify(
            {"jobs": [job.to_dict()]}
        )

    def delete(self, job_id):
        abort_missing_job(job_id)
        db_sess = db_session.create_session()
        job: Jobs = db_sess.get(Jobs, job_id)
        db_sess.delete(job)
        db_sess.commit()
        return jsonify({'success': 'OK'})

    def put(self, job_id):
        abort_missing_job(job_id)
        args = parser.parse_args()
        db_sess = db_session.create_session()
        job: Jobs = db_sess.get(Jobs, job_id)
        job.team_leader_id = args["team_leader_id"]
        job.job = args["job"]
        job.work_size = args["work_size"]
        job.collaborators = args["collaborators"]
        job.start_date = args["start_date"]
        job.end_date = args.get("end_date")
        job.is_finished = args.get("is_finished", False)
        db_sess.commit()
        return jsonify({'success': 'OK'})


class JobsListResource(Resource):

    def get(self):
        db_sess = db_session.create_session()
        jobs = db_sess.query(Jobs).all()
        return jsonify(
            {"jobs": [job.to_dict() for job in jobs]}
        )

    def post(self):
        args = parser.parse_args()
        db_sess = db_session.create_session()
        job = Jobs(
            team_leader_id=args["team_leader_id"],
            job=args["job"],
            work_size=args["work_size"],
            collaborators=args["collaborators"],
            start_date=args["start_date"],
            end_date=args.get("end_date"),
            is_finished=args.get("is_finished", False),
        )
        db_sess.add(job)
        db_sess.commit()
        return jsonify({'success': 'OK'})


def init_api_routes(api: Api):
    url_prefix = "/api/v2/jobs"
    api.add_resource(JobResource, f"{url_prefix}/<int:job_id>")
    api.add_resource(JobsListResource, url_prefix)
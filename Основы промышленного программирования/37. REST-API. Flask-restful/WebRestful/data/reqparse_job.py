from datetime import datetime
from flask_restful import reqparse


parser = reqparse.RequestParser()
parser.add_argument("team_leader_id", required=True, type=int)
parser.add_argument("job", required=True)
parser.add_argument("work_size", required=True, type=int)
parser.add_argument("collaborators", required=True)
parser.add_argument("start_date", required=True, type=lambda arg: datetime.fromisoformat(arg))
parser.add_argument("end_date", type=lambda arg: datetime.fromisoformat(arg))
parser.add_argument("is_finished", type=bool)

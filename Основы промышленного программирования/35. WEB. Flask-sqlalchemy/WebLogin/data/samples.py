from datetime import datetime

from werkzeug.security import generate_password_hash

from data import db_session
from data.jobs import Jobs
from data.users import User


def get_users_data():
    users_data = [
        {
            "surname": "Scott",
            "name": "Ridley",
            "age": 21,
            "position": "captain",
            "speciality": "research engineer",
            "address": "module_1",
            "email": "scott_chief@mars.org",
            "hashed_password": generate_password_hash("secret_of_cap"),
            "modified_date": datetime.now()
        },
        {
            "surname": "Weer",
            "name": "Andy",
            "age": 23,
            "position": "science pilot",
            "speciality": "drone pilot",
            "address": "module_2",
            "email": "andy_story@mars.org",
            "hashed_password": generate_password_hash("andy_23"),
            "modified_date": datetime.now()
        },
        {
            "surname": "Watney",
            "name": "Mark",
            "age": 22,
            "position": "mission specialist",
            "speciality": "astrogeologist",
            "address": "module_3",
            "email": "mark3@mars.org",
            "hashed_password": generate_password_hash("marsWWWatney"),
            "modified_date": datetime.now()
        },
        {
            "surname": "Kapoor",
            "name": "Venkata",
            "age": 25,
            "position": "flight engineer",
            "speciality": "cyberengineer",
            "address": "module_4",
            "email": "kapoor_astro@mars.org",
            "hashed_password": generate_password_hash("cyberkapoor25"),
            "modified_date": datetime.now()
        },
    ]
    return users_data


def create_users():
    db_sess = db_session.create_session()
    users = get_users_data()
    for user_data in users:
        user = User(**user_data)
        db_sess.add(user)
    db_sess.commit()


def get_jobs_data():
    jobs_data = [
        {
            "team_leader_id": 1,
            "job": "Deployment of residential modules 1 and 2",
            "work_size": 15,
            "collaborators": "2, 3",
            "start_date": datetime.now(),
            "is_finished": False,
        },
        {
            "team_leader_id": 2,
            "job": "Exploration of mineral sources",
            "work_size": 15,
            "collaborators": "4, 3",
            "start_date": datetime.now(),
            "is_finished": False,
        },
        {
            "team_leader_id": 3,
            "job": "Development of management system",
            "work_size": 25,
            "collaborators": "5",
            "start_date": datetime.now(),
            "is_finished": False,
        },
        {
            "team_leader_id": 4,
            "job": "Fix ventilation system",
            "work_size": 20,
            "collaborators": "2, 5",
            "start_date": datetime.now(),
            "is_finished": True,
        },
    ]
    return jobs_data


def create_jobs():
    db_sess = db_session.create_session()
    jobs = get_jobs_data()
    for job_data in jobs:
        job = Jobs(**job_data)
        db_sess.add(job)
    db_sess.commit()


def add_data_to_db():
    create_users()
    create_jobs()

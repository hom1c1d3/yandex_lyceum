from datetime import datetime

from data import db_session
from data.users import User
from data.jobs import Jobs


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
        },
        {
            "surname": "Weer",
            "name": "Andy",
            "age": 23,
            "position": "science pilot",
            "speciality": "drone pilot",
            "address": "module_2",
            "email": "andy_story@mars.org",
        },
        {
            "surname": "Watney",
            "name": "Mark",
            "age": 22,
            "position": "mission specialist",
            "speciality": "astrogeologist",
            "address": "module_3",
            "email": "mark3@mars.org",
        },
        {
            "surname": "Kapoor",
            "name": "Venkata",
            "age": 25,
            "position": "flight engineer",
            "speciality": "cyberengineer",
            "address": "module_4",
            "email": "kapoor_astro@mars.org",
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
            "team_leader": 1,
            "job": "deployment of residential modules 1 and 2",
            "work_size": 15,
            "collaborators": "2, 3",
            "start_date": datetime.now(),
            "is_finished": False,
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


def main():
    db_session.global_init("db/blogs.db")
    add_data_to_db()


if __name__ == '__main__':
    main()

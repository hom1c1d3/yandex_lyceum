from datetime import datetime

from data import db_session
from data.jobs import Jobs, Category
from data.users import User
from data.departments import Department
from werkzeug.security import generate_password_hash


def get_users_data():
    users_data = [
        {
            "surname": "Scott",
            "name": "Ridley",
            "age": 21,
            "position": "captain",
            "speciality": "research engineer",
            "address": "module_1",
            "city_from": "Washington",
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
            "city_from": "Wellington",
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
            "city_from": "Moscow",
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
            "city_from": "Tunis",
            "email": "kapoor_astro@mars.org",
            "hashed_password": generate_password_hash("cyberkapoor25"),
            "modified_date": datetime.now()
        },
        {
            "surname": "Bean",
            "name": "Sean",
            "age": 17,
            "position": "chief engineer",
            "speciality": "builder",
            "address": "module_1",
            "city_from": "Roma",
            "email": "bean@mars.org",
            "hashed_password": generate_password_hash("seanlikesbeans1"),
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


def get_categories_data():
    categories_data = [
        {
            "name": "life support",
        },
        {
            "name": "exploring planet",
        },
        {
            "name": "terraforming",
        },
    ]
    return categories_data


def create_categories():
    db_sess = db_session.create_session()
    categories = get_categories_data()
    for category_data in categories:
        category = Category(**category_data)
        db_sess.add(category)
    db_sess.commit()


def get_jobs_data():
    jobs_data = [
        {
            "team_leader_id": 1,
            "job": "Deployment of residential modules 1 and 2",
            "work_size": 15,
            "collaborators": "2, 3",
            "start_date": datetime.now(),
            "categories": [1],
            "is_finished": False,
        },
        {
            "team_leader_id": 2,
            "job": "Exploration of mineral sources",
            "work_size": 15,
            "collaborators": "4, 3",
            "start_date": datetime.now(),
            "categories": [2],
            "is_finished": False,
        },
        {
            "team_leader_id": 3,
            "job": "Development of management system",
            "work_size": 25,
            "collaborators": "5",
            "start_date": datetime.now(),
            "categories": [1, 3],
            "is_finished": False,
        },
        {
            "team_leader_id": 4,
            "job": "Fix ventilation system",
            "work_size": 20,
            "collaborators": "2, 5",
            "start_date": datetime.now(),
            "categories": [1],
            "is_finished": True,
        },
    ]
    return jobs_data


def create_jobs():
    db_sess = db_session.create_session()
    jobs = get_jobs_data()
    for job_data in jobs:
        categories_id = job_data.pop("categories")
        categories = []
        for category_id in categories_id:
            category = db_sess.get(Category, category_id)
            categories.append(category)
        job = Jobs(**job_data)
        for category in categories:
            job.categories.append(category)
        db_sess.add(job)
    db_sess.commit()


def get_departments_data():
    departments_data = [
        {
            "title": "Department of geological exploration",
            "chief_id": 2,
            "members": "3, 4, 5",
            "email": "geo@mars.org",
        },
        {
            "title": "Department of biological research",
            "chief_id": 3,
            "members": "7, 10, 11",
            "email": "bio@mars.org",
        },
        {
            "title": "Department of construction",
            "chief_id": 5,
            "members": "16, 17, 28",
            "email": "build@mars.org",
        },
        {
            "title": "Department of transportation",
            "chief_id": 4,
            "members": "26, 37, 19",
            "email": "transport@mars.org",
        },
        {
            "title": "Department of terraforming",
            "chief_id": 1,
            "members": "1, 2, 5",
            "email": "terra@mars.org",
        },
    ]
    return departments_data


def create_departments():
    db_sess = db_session.create_session()
    departments = get_departments_data()
    for department_data in departments:
        department = Department(**department_data)
        db_sess.add(department)
    db_sess.commit()


def add_data_to_db():
    create_users()
    create_categories()
    create_jobs()
    create_departments()

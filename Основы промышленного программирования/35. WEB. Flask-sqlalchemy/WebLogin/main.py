from datetime import datetime

from flask import Flask, render_template, redirect

from data import db_session
from data.jobs import Jobs
from data.users import User
from forms.users import RegisterForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "SECRETTOKEN"


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


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = User(
            surname=form.surname.data,
            name=form.name.data,
            age=form.age.data,
            position=form.position.data,
            speciality=form.speciality.data,
            address=form.address.data,
            email=form.login.data,
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect("/login")
    return render_template("register.html", title="Регистрация", form=form)


@app.route("/login")
def login():
    return render_template("login.html", title="Авторизация")


@app.route("/")
def work_log():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    return render_template("work_log.html", jobs=jobs)


def main():
    db_session.global_init("db/blogs.db")
    app.run("", port=8080)


if __name__ == '__main__':
    main()

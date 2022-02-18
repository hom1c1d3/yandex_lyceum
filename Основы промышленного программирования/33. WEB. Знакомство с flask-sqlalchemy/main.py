from data import db_session
from data.users import User


def get_users():
    users = [
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
    return users


def main():
    db_session.global_init("db/blogs.db")
    db_sess = db_session.create_session()
    users = get_users()
    for user_data in users:
        user = User()
        user.surname = user_data["surname"]
        user.name = user_data["name"]
        user.age = user_data["age"]
        user.position = user_data["position"]
        user.speciality = user_data["speciality"]
        user.address = user_data["address"]
        user.email = user_data["email"]
        db_sess.add(user)
    db_sess.commit()


if __name__ == '__main__':
    main()

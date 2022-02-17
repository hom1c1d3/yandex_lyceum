from data.users import User
from data import db_session


def main():
    db_session.global_init("db/blogs.db")
    db_sess = db_session.create_session()
    # for i in range(1, 4):
    #     user = User()
    #     user.name = f"Пользователь {i}"
    #     user.about = f"Важная информация о пользователе {i}"
    #     user.email = f"user{i}@email.com"
    #     db_sess.add(user)
    # db_sess.commit()

    user = db_sess.query(User).first()
    print(user)
    db_sess.close()


if __name__ == '__main__':
    main()
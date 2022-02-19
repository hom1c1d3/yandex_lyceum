# доступны функции global_init(db_name), create_session(), а также классы моделей User и Jobs.


def main():
    db_name = input()
    global_init(db_name)
    db_sess = create_session()
    res_users = db_sess.query(User)\
        .filter(User.age < 18)
    for i in res_users:
        print(i, i.age, "years")


if __name__ == '__main__':
    main()
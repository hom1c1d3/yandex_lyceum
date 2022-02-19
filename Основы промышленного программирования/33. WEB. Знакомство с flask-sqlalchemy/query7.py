# доступны функции global_init(db_name), create_session(), а также классы моделей User и Jobs.


def main():
    db_name = input()
    global_init(db_name)
    db_sess = create_session()
    res_users = db_sess.query(User)\
        .filter(User.address == "module_1", User.age < 21)
    for i in res_users:
        i.address = "module_1"
    db_sess.commit()


if __name__ == '__main__':
    main()
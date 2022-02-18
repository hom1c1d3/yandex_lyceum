# доступны функции global_init(db_name), create_session(), а также классы моделей User и Jobs.


def main():
    db_name = input()
    global_init(db_name)
    db_sess = create_session()
    res = db_sess.query(User.id)\
        .filter(User.address == "module_1")\
        .filter(User.speciality.notlike("%engineer%"), User.position.notlike("%engineer%"))
    for i in res:
        print(*i)


if __name__ == '__main__':
    main()
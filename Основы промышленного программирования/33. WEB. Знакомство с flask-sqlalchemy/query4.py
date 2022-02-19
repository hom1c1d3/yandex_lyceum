# доступны функции global_init(db_name), create_session(), а также классы моделей User и Jobs.


def main():
    db_name = input()
    global_init(db_name)
    db_sess = create_session()
    res_users = db_sess.query(User)\
        .filter(User.position.like("%chief%") | User.position.like("%middle%"))
    for i in res_users:
        print(i, i.position)


if __name__ == '__main__':
    main()
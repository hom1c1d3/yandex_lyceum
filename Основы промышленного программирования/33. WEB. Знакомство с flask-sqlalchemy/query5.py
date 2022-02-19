# доступны функции global_init(db_name), create_session(), а также классы моделей User и Jobs.


def main():
    db_name = input()
    global_init(db_name)
    db_sess = create_session()
    res = db_sess.query(Jobs) \
        .filter(Jobs.work_size < 20, ~Jobs.is_finished)
    for i in res:
        print(i)


if __name__ == '__main__':
    main()

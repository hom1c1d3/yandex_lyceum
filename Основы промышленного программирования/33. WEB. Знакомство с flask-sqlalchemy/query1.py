# доступны функции global_init(db_name), create_session(), а также классы моделей User и Jobs.


def main():
    db_name = input()
    global_init(db_name)
    db_sess = create_session()
    res = db_sess.query(User).filter(User.address == "model_1").all()
    print(*res, sep='\n')


if __name__ == '__main__':
    main()
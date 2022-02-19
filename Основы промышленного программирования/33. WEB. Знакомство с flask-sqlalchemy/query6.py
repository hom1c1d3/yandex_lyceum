# доступны функции global_init(db_name), create_session(), а также классы моделей User и Jobs.


def main():
    db_name = input()
    global_init(db_name)
    db_sess = create_session()
    jobs = db_sess.query(Jobs).all()
    jobs = sorted(jobs, key=lambda x: len(x.collaborators), reverse=True)
    max_team_jobs = []
    max_team_size = float("-inf")
    for i in jobs:
        team_size = len(i.collaborators)
        if team_size > max_team_size:
            max_team_size = team_size
        if team_size == max_team_size:
            max_team_jobs.append(i)
        else:
            break
    leaders = set()
    for i in max_team_jobs:
        name = db_sess.query(User.name, User.surname).filter(User.id == i.team_leader).first()
        name = " ".join(name)
        leaders.add(name)
    print(*leaders, sep='\n')


if __name__ == '__main__':
    main()

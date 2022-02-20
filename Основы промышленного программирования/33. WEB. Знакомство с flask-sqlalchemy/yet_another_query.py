# доступны функции global_init(db_name), create_session(), а также классы моделей User,
# Jobs и Department.


def main():
    db_name = input()
    global_init(db_name)
    db_sess = create_session()
    department_id = 1
    members = db_sess.query(Department.members).filter(Department.id == department_id).first()[0]
    members = list(map(int, members.split(', ')))
    users = db_sess.query(User).filter(User.id.in_(members)).all()
    users_jobs = {}
    jobs = db_sess.query(Jobs).all()
    for user in users:
        for job in jobs:
            if (user.id in set(map(int, job.collaborators.split(', ')))
                    or user.id == job.team_leader):
                try:
                    users_jobs[user].append(job)
                except KeyError:
                    users_jobs[user] = [job]
    users_work_times = {user: sum(job.work_size for job in user_jobs)
                        for user, user_jobs in users_jobs.items()}
    res_users = [user for user, work_time in users_work_times.items() if work_time > 25]
    for user in res_users:
        print(user.surname, user.name)


if __name__ == '__main__':
    main()

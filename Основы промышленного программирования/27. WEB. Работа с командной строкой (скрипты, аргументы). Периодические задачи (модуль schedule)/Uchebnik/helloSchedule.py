import datetime
import schedule

i = 1


def job():
    global i
    print(f"Запустился {i} раз")
    i += 1
    print(datetime.datetime.now())
    if i > 3:
        return schedule.CancelJob


schedule.every(5).seconds.do(job)

while schedule.get_jobs():
    schedule.run_pending()

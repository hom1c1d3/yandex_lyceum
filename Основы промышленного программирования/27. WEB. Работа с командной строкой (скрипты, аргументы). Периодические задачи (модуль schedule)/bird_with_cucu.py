import datetime
import schedule


def job():
    hour = datetime.datetime.now().hour
    cucu_count = hour % 12
    if cucu_count == 0:
        cucu_count = 12
    print("Ку " * cucu_count)


schedule.every(1).hour.at(':00').do(job)


while True:
    schedule.run_pending()
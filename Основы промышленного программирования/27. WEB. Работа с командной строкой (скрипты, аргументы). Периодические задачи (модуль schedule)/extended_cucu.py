import datetime
import schedule


print_text = input("Что выводить будем? ")
silence_time = input("Когда молчать будем? (В часах, например: 00-07) ")
silence_time = silence_time.split('-')
silence_time = int(silence_time[0]), int(silence_time[1])


def job(display_text):
    hour = datetime.datetime.now().hour
    if hour in range(silence_time[0], silence_time[1] + 1):
        return
    cucu_count = hour % 12
    if cucu_count == 0:
        cucu_count = 12
    print((display_text + " ") * cucu_count)


schedule.every(1).hour.at(':00').do(job, print_text)


while True:
    schedule.run_pending()
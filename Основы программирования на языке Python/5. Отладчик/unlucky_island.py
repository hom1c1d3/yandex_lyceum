import datetime

day = int(input())
month = int(input())
year = int(input())

print(datetime.date(year, month, day).isoweekday() % 7)

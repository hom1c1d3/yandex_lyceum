import datetime

now = datetime.datetime.strptime('01.09.2019', '%d.%m.%Y')
left = datetime.timedelta(int(input()))
birthday = now + left
print(birthday.day, birthday.month)
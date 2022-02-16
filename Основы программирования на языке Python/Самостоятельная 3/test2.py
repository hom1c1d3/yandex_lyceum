import datetime

date_from = datetime.datetime.strptime(input(), '%Y.%m.%d')
date_to = datetime.datetime.strptime(input(), '%Y.%m.%d')

if (date_from.month + date_from.day) % 2 == 0:
    date_from += datetime.timedelta(days=1)

date_list = [date_from + datetime.timedelta(days=i) for i in range((date_to - date_from).days + 1)]
date_list = filter(lambda x: x.weekday() not in (0, 3), date_list[::3])
date_list = sorted(date_list)
for i in date_list:
    print(i.strftime('%d %B %Y'))


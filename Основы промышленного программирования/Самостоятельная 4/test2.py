import csv
import json
from collections import defaultdict


weather_table_name = input()


with open(weather_table_name, "r") as fd:
    reader = csv.DictReader(fd, delimiter="^")
    data = list(reader)

date_weather = defaultdict(list)

for row in data:
    date = row["date"]
    weather = row["weather"]
    date_weather[date].append(weather)


for weathers in date_weather.values():
    weathers = weathers.sort(reverse=True)

with open("weather.json", "w", encoding="utf-8") as fd:
    json.dump(date_weather, fd)

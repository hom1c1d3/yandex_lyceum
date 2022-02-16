import requests
import json
import csv


with open("treats.json", 'r', encoding="utf8") as fp:
    treats = json.load(fp)

server = treats['server']
port = treats["port"]
animal_sort = treats['sort']


resp = requests.get(f"http://{server}:{port}")
animal_data = resp.json()

result = []

for animal in animal_data:
    if animal['sort'] != animal_sort:
        continue
    for meal in animal["meal"]:
        animal_result = {'animal': animal['animal'], 'habitat': animal['habitat'], "meal": meal}
        result.append(animal_result)

result = sorted(result, key=lambda x: (x["animal"], x["meal"]))


with open("dishes.csv", 'w', newline="") as fd:
    writer = csv.writer(fd, delimiter=":")
    writer.writerow(["animal", "habitat", "meal"])
    for row in result:
        writer.writerow([row["animal"], row["habitat"], row["meal"]])
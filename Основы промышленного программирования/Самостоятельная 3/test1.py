import csv
import sys
from collections import defaultdict
import json


data = csv.reader(sys.stdin, delimiter=":")

riddle = {
    "mammal": defaultdict(list),
    "reptile": defaultdict(list),
    "insect": defaultdict(list),
}

for animal_class, name, feature in data:
    riddle[animal_class][feature].append(name)

riddle = {k: {feature: sorted(names) for feature, names in v.items()} for k, v in riddle.items()}


with open("riddle.json", 'w', encoding='utf8') as fd:
    json.dump(riddle, fd)
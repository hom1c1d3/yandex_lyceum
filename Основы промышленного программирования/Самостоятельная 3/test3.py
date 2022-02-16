import argparse
import json
from collections import defaultdict

import requests


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("host")
    parser.add_argument("port")
    parser.add_argument("animal_kinds", nargs="+")
    parser.add_argument("--min_amount", type=int, default=0)
    parser.add_argument("--length", type=int, default=20)
    args = parser.parse_args()
    host = args.host
    port = args.port
    animal_kinds = args.animal_kinds
    min_amount = args.min_amount
    length = args.length

    resp = requests.get(f"http://{host}:{port}")
    animals_data = resp.json()

    result_animals = defaultdict(list)

    for animal in animals_data:
        if (animal["kind"] in animal_kinds
                and animal["amount"] >= min_amount
                and len(animal["habitat"]) <= length):
            habitat = animal["habitat"]
            animal_value = [animal["name"], animal["amount"]]
            result_animals[habitat].append(animal_value)

    result_animals = {k: sorted(v, key=lambda x: (x[1], x[0])) for k, v in result_animals.items()}

    with open("polar_zoo.json", 'w', encoding="utf8") as fd:
        json.dump(result_animals, fd)


if __name__ == '__main__':
    main()
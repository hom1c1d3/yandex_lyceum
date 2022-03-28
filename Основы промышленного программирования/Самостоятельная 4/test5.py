import argparse
import json
from collections import defaultdict

from flask import Flask, jsonify


app = Flask(__name__)
res_rules = {}


@app.route("/offense")
def get_offensive():
    return jsonify(res_rules)


def get_rules(filename, punishment_type):
    with open(filename, "r") as fd:
        data = json.load(fd)

    rules = defaultdict(list)
    for rule in data:
        if rule["punishment"] == punishment_type:
            country = rule["country"]
            rules[country].append(rule["rule"])

    for country in rules:
        rules[country].sort()
    return rules


def parse_rules():
    parser = argparse.ArgumentParser()

    parser.add_argument("--address")
    parser.add_argument("--port")
    parser.add_argument("--filename")
    parser.add_argument("--type", choices=["crime", "administrative", "none"])

    args = parser.parse_args()

    rules = get_rules(args.filename, args.type)
    res_rules.clear()
    for k, v in rules.items():
        res_rules[k] = v
    return args


def main():
    args = parse_rules()
    app.run(args.address, args.port)


if __name__ == '__main__':
    main()
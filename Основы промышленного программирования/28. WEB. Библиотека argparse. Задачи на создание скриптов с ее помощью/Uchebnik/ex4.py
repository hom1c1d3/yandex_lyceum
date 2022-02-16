"""
Тренировочное задание (примеры работы):
python ex4.py --help
python ex4.py -up --no-name

Попробуй самостоятельно поработать с программой ниже, поизменяй параметры и посмотри, что получается.
Добейся вывода строки из оператора print. Ответь на вопросы учителя из презентации.
"""

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--name")
parser.add_argument("-up", "--up_case", action="store_true",
                    help="convert name to upper register")
parser.add_argument(
    "--number", choices=[0, 1, 2], type=int, default=0,
    help="select number", required=True)
parser.add_argument("--no-name", action="store_const", const="no",
                    dest="name")
args = parser.parse_args()

name = args.name
if (args.up_case):
    name = name.upper()

print(f"The name is {name}. And the number = {args.number}")


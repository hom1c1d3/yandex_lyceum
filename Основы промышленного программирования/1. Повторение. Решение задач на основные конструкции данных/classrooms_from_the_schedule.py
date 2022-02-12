import sys
import re
from collections import defaultdict

text = sys.stdin.read()
subjects_and_classrooms = re.findall(r'(.*) (\d+)', text)

classrooms = defaultdict(list)
for subj, classroom in subjects_and_classrooms:
    if subj not in classrooms[classroom]:
        classrooms[classroom] += [subj]
classrooms = sorted(((int(a), b) for a, b in classrooms.items()), key=lambda x: x[0])

for classroom, subjects in classrooms:
    print(f'{classroom}:', ', '.join(subjects))
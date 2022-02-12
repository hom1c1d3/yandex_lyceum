import re
import sys

text = sys.stdin.read()
scenes = text.splitlines()
delek_count = 0
for scene in scenes:
    words = re.findall(r'\w*', scene)
    if any(i.lower().startswith('далек') for i in words):
        delek_count += 1
print(delek_count)

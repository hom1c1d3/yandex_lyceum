from zipfile import ZipFile
import json


moscow_count = 0
with ZipFile('input.zip') as myzip:
    for file_name in myzip.namelist():
        if not file_name.endswith('.json'):
            continue
        with myzip.open(file_name, 'r') as fd:
            person_data = json.load(fd)
        if person_data['city'] == 'Москва':
            moscow_count += 1
print(moscow_count)
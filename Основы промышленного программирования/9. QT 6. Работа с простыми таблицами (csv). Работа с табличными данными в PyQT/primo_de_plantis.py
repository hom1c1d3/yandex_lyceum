import csv
import sys

headers = ['nomen', 'definito', 'pluma', 'Russian nomen', 'familia',
           'Russian nomen familia']
data = [line.rstrip().split('\t') for line in sys.stdin]
with open('plantis.csv', 'w',
          encoding='utf-8', newline='') as f:
    writer = csv.writer(f, delimiter=';')
    writer.writerow(headers)
    writer.writerows(data)

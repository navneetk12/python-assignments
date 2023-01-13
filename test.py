import csv

import csv

with open('testwrite.csv', 'r') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

print(rows)
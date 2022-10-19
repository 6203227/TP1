import os
import csv
f = open('new.csv')
csv_f = csv.reader(f)

with open('new.csv', 'r') as fich:
    pp = csv.reader(fich)
    for row in csv_f:
        print(row[2])



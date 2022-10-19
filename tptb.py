import os
import csv
f = open('new.csv')
csv_f = csv.reader(f)

with open('new.csv') as fich:
    pp = csv.reader(fich)
    for row in csv_f:
        print('\t')
        print(''.join(row[2]), '\t', end=" ")
        print(''.join(row[3]), '\t')



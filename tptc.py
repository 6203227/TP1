import os
import csv
f = open('new.csv')
csv_f = csv.reader(f)

with open('new.csv') as fich:
    pp = csv.reader(fich)
    for row in csv_f:
        print('\t')
        print('Description: ', '\t', row[2] + row[3])
        print('Energ_Kcal: ', '\t', row[3])

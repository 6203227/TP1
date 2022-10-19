import os
import csv
f = open('new.csv')

with open('new.csv', 'r') as fich:
    pp = csv.reader(fich)
    with open('sortie1.csv', 'w') as sortie1:
        s1 = csv.writer(sortie1,  delimiter=' ')
        for row in pp:
            s1.writerow(str(row[5] + row[6]))



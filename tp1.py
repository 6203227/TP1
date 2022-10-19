import os
import csv

f = open('nutrition.csv')
csv_f = csv.reader(f)

erreur = ('''
          Erreur, choix invalide ... 

            SVP recommencer :      ''')
men = ('''
*************************************************************************
     choix 1 - Afficher l’ensemble des valeurs nutritives
     choix 2 - Afficher les aliments en fonction d’une valeurs nutritives
     choix 3 - Afficher les valeurs nutritives d’un aliment (avec #)  
     choix 4 - Modification d’une valeur nutritive d’un aliment (avec #)
     choix 5 - Insertion d'une entree
     choix 6 - Quitter  
*************************************************************************
''')
ch = 0
xy = 'y'
print(men)


while ch < 5:
    ch = int(input("faitez votre choix SVP :  "))
    if ch == 1:
        print(f.read())
    elif ch == 2:
        print("test 2")
        for row in csv_f:
            print(row)
        xy = 'o'
        break
    elif ch == 3:
        print("test 3")
        for row in csv_f:
            print(row['first_name'], row['last_name'])
        xy = 'o'
        break
    elif ch == 4:
        print("test 4")
        with open('nutrition.csv', newline='') as csvfile:
            pp = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in pp:
                print(', '.join(row))
        print("Total number: ", (pp.line_num))
    elif ch == 5:
        print("test 5")
    elif ch == 6:
        print("Vous voulez quitter?")
        xy = input('''
        Oui (o)/ Non  (n):  
        Confirmez
        ''')
    else:
        print("Erreur final")
        exit()
while xy not in 'on':
    xy = input("Choix, invalide, Confirmez :  ")
    if xy == 'o':
        print("Au Revoir")
        exit()
    elif xy == 'n':
        os.open(path + "tp1.py")


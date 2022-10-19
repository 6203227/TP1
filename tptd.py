import os
import csv

f = open('new.csv')
csv_f = csv.reader(f)

y = str('m')
erreur = ('''
          Erreur, choix invalide ... 

            SVP recommencer :      ''')
men = ('''
******************************************************************************
     choix 1 - Afficher l’ensemble des valeurs nutritives
     choix 2 - Afficher les aliments en fonction d’une valeurs nutritives
     choix 3 - Afficher les valeurs nutritives d’un aliment (avec #)  
     choix 4 - Modification d’une valeur nutritive d’un aliment (avec #)
     choix 5 - Insertion d'une entree
     choix 6 - Quitter  
******************************************************************************
''')
men2 = ('''
******************************************************************************
    Afficher les aliments en fonction d’une valeurs nutritives choisie
     choix 1 - Afficher selon contenu de * sodium * le plus haut
     choix 2 - Afficher selon contenu de * calories * le plus haut
     choix 3 - Afficher selon contenu de * gras * le plus haut  
     choix 4 - Afficher selon contenu de * proteine * le plus haut
     choix 5 - Afficher selon contenu de * cholesterol * le plus haut
     choix 6 - Quitter
******************************************************************************
''')

print(men)
ch = int(input("faitez le choix SVP: "))
if ch == 1:
    print('''
    ******************************************************************************
    Voici les valeurs completes, en entier
    ******************************************************************************
    ''')
    with open('new.csv') as fich:
        pp = csv.reader(fich)
        for row in csv_f:
            print(row[0], '\t', row[1], '\t', row[4], '\t', row[5], '\t', row[6], '\t', row[7],'\t', row[2])
elif ch == 2:
    print(men2)
    ch2 = int(input("faitez le choix SVP: "))
    if ch2 == 2:
        print("choix 2 -2 ")
    elif ch2 == 3:
        print("test 3 - 3")
    elif ch2 == 4:
        print("test 4 - 4")
    elif ch2 == 5:
        print("test5 - 5 ")
    elif ch2 == 6:
        print("Quitter?")
        y = input("Vous etez sur? ")
    else:
        print("choix invalide, fermeture")
elif ch == 3:
    print("test 3")
elif ch == 4:
    print("test 4")
elif ch == 5:
    print("test5")
elif ch == 6:
    print("Quitter?")
    y = input("Vous etez sur? ")
else:
    print("choix invalide, fermeture")
if y == 'o':
    exit()
elif y == 'n':
    print("tant pis, on ferme quand meme")
    exit()
elif y == 'm':
    print('''
    Merci! 
    ''')
else:
    print("nous sommes pas rendu ici")
    exit()
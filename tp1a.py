import csv
file = open('nutrition.csv')


erreur = ('''
          Erreur, choix invalide ... 

            SVP recommencer :      ''')
def ch():
    print('''
    ***********************************************
    ''')
    print("    choix 1 x")
    print("     choix 2 y   ")
    print("     choix 3 z    ")
    print("     choix 4 u    ")
    print("***********************************************")


while True:
    ch()
    ch = int(input("faitez votre choix SVP :  "))
    if ch == 1:
        print(file.read())
    elif ch == 2:
        print("test 2")
    elif ch == 3:
        print("test 3")
    elif ch == 4:
        print("test 4")
    elif ch == 5:
        print("test 5")
    elif ch == 6:
        print("Vous voulez quitter?")
        xy = input('''
        Oui (o)/ Non  (n):  
        Confirmez
        ''')
    else:
        exit()
while xy not in 'on':
    xy = input("Choix, invalide, Confirmez :  ")
if xy == 'o':
    print("Au Revoir")
    exit()
elif xy == 'n':
    ch = int(input("faitez votre choix SVP :  "))



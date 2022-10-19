import time
import datetime
now = datetime.datetime.now()
block =('''
    SVP proceder au paiement :
	Faitez un choix

    [b] pour carte bancaire
    [c] pour argent comptant

    [q] pour annuler la transaction
''')
quit = ('''
    ******************************************* 
        La transaction a ete annule  
                  
        Bonne journee
    *******************************************
    ''')
erreur = ('''
          Erreur, choix invalide ... 
    
            SVP recommencer :      ''')
succ = ('''
    La transaction est termine avec succes
    N'oubliez pas de prendre votre billet
    
    Merci et bonne journee    ''')
print('''
    *******************************************
               Bienvenue à la STM              
          SVP choisissez votre categorie       
                d'age pour commencer           
    *******************************************
         o      Tarif Ordinaire
         e      Etudiants 18+
         j      12-17 ans
         a      Age d'Or 65+
         
         q      Quitter
    *******************************************
    ''')
x1 = str(input("      Faitez un choix SVP : "))
print('''


''')
while x1 not in "qoeja":
    x1 = str(input(erreur))
if x1 == 'e':
    print('''
    ******************************************* 
         Veuillez choisir le titre desire  
    choix [a]  :  1 passage        @ $3.50
    choix [b]  :  2 passages       @ $6.50
    choix [c]  :  10 passages      @ $31.50
    choix [d]  :  24 heures        @ $11.00
    choix [e]  :  3 jours          @ $21.25
    choix [f]  :  Semaine          @ $29.00
    choix [g]  :  Mensuel          @ $56.50
    choix [h]  :  4 mois           @ $220.00
    choix [i]  :  Soiree illimite  @ $5.75
    choix [j]  :  Weekend illimite @ $14.75
    
    choix [q]  :  Annuler la transaction
    ''')
    x2 = str(input("Votre choix : "))
    while x2 not in 'abcdefghijq':
        x2 = str(input(erreur))
    if x2 == 'a':
        print(block)
        print('''
        Tarif Etudiants 18+
        1 passage      @ $3.50
        ''')
    elif x2 == 'b':
        print(block)
        print('''
        Tarif Etudiants 18+
        2 passages       @ $6.50
        ''')
    elif x2 == 'c':
        print(block)
        print('''
        Tarif Etudiants 18+
        10 passages      @ $31.50
        ''')
    elif x2 == 'd':
        print(block)
        print('''
        Tarif Etudiants 18+
        24 heures        @ $11.00
        ''')
    elif x2 == 'e':
        print(block)
        print('''
        Tarif Etudiants 18+
        3 jours          @ $21.25
        ''')
    elif x2 == 'f':
        print(block)
        print('''
        Tarif Etudiants 18+
        Semaine          @ $29.00
        ''')
    elif x2 == 'g':
        print(block)
        print('''
        Tarif Etudiants 18+
        Mensuel          @ $56.50
        ''')
    elif x2 == 'h':
        print(block)
        print('''
        Tarif Etudiants 18+
        4 mois           @ $220.00
        ''')
    elif x2 == 'i':
        print(block)
        print('''
        Tarif Etudiants 18+
        Soiree illimite  @ $5.75
        ''')
    elif x2 == 'j':
        print(block)
        print('''
        Tarif Etudiants 18+
        Weekend illimite @ $14.75
        ''')
elif x1 == 'a':
    print('''
    ******************************************* 
         Veuillez choisir le titre desire  
    choix [a]  :  1 passage        @ $1.25
    choix [b]  :  2 passages       @ $2.25
    choix [c]  :  10 passages      @ $10.50
    choix [d]  :  24 heures        @ $11.00
    choix [e]  :  3 jours          @ $21.25
    choix [f]  :  Semaine          @ $8.75
    choix [g]  :  Mensuel          @ $28.25
    choix [h]  :  4 mois           @ $110.00
    choix [i]  :  Soiree illimite  @ $5.75
    choix [j]  :  Weekend illimite @ $14.75
    
    choix [q]  :  Annuler la transaction
    ''')
    x2 = str(input("Votre choix : "))
    while x2 not in 'abcdefghijq':
        x2 = str(input(erreur))
    if x2 == 'a':
        print(block)
        print('''
        Tarif age d'or 65+
        1 passage        @ $1.25
        ''')
    elif x2 == 'b':
        print(block)
        print('''
        Tarif age d'or 65+
        2 passages       @ $2.25
        ''')
    elif x2 == 'c':
        print(block)
        print('''
        Tarif age d'or 65+
        10 passages      @ $10.50
        ''')
    elif x2 == 'd':
        print(block)
        print('''
        Tarif age d'or 65+
        24 heures        @ $11.00
        ''')
    elif x2 == 'e':
        print(block)
        print('''
        Tarif age d'or 65+
        3 jours          @ $21.25
        ''')
    elif x2 == 'f':
        print(block)
        print('''
        Tarif age d'or 65+
        Semaine          @ $8.75
        ''')
    elif x2 == 'g':
        print(block)
        print('''
        Tarif age d'or 65+
        Mensuel          @ $28.25
        ''')
    elif x2 == 'h':
        print(block)
        print('''
        Tarif age d'or 65+
        4 mois           @ $110.00
        ''')
    elif x2 == 'i':
        print(block)
        print('''
        Tarif age d'or 65+
        Soiree illimite  @ $5.75
        ''')
    elif x2 == 'j':
        print(block)
        print('''
        Tarif age d'or 65+
        Weekend illimite @ $14.75
        ''')
elif x1 == 'j':
    print('''
    ******************************************* 
         Veuillez choisir le titre desire  
    choix [a]  :  1 passage        @ $2.50
    choix [b]  :  2 passages       @ $4.50
    choix [c]  :  10 passages      @ $21.00
    choix [d]  :  24 heures        @ $11.00
    choix [e]  :  3 jours          @ $21.25
    choix [f]  :  Semaine          @ $17.50
    choix [g]  :  Mensuel          @ $56.50
    choix [h]  :  4 mois           @ $220.00
    choix [i]  :  Soiree illimite  @ $5.75
    choix [j]  :  Weekend illimite @ $14.75
    
    choix [q]  :  Annuler la transaction
    ''')
    x2 = str(input("Votre choix : "))
    while x2 not in 'abcdefghijq':
        x2 = str(input(erreur))
    if x2 == 'a':
        print(block)
        print('''
        Tarif 12-17 ans
        1 passage      @ $2.50
        ''')
    elif x2 == 'b':
        print(block)
        print('''
        Tarif 12-17 ans
        2 passages       @ $4.50
        ''')
    elif x2 == 'c':
        print(block)
        print('''
        Tarif 12-17 ans
        10 passages      @ $21.00
        ''')
    elif x2 == 'd':
        print(block)
        print('''
        Tarif 12-17 ans
        24 heures        @ $11.00
        ''')
    elif x2 == 'e':
        print(block)
        print('''
        Tarif 12-17 ans
        3 jours          @ $21.25
        ''')
    elif x2 == 'f':
        print(block)
        print('''
        Tarif 12-17 ans
        Semaine          @ $17.50
        ''')
    elif x2 == 'g':
        print(block)
        print('''
        Tarif 12-17 ans
        Mensuel          @ $56.50
        ''')
    elif x2 == 'h':
        print(block)
        print('''
        Tarif 12-17 ans
        4 mois           @ $220.00
        ''')
    elif x2 == 'i':
        print(block)
        print('''
        Tarif 12-17 ans
        Soiree illimite  @ $5.75
        ''')
    elif x2 == 'j':
        print(block)
        print('''
        Tarif 12-17 ans
        Weekend illimite @ $14.75
        ''')
elif x1 == 'o':
    print('''
    ******************************************* 
         Veuillez choisir le titre desire  
    choix [a]  :  1 passage        @ $3.50
    choix [b]  :  2 passages       @ $6.50
    choix [c]  :  10 passages      @ $31.50
    choix [d]  :  24 heures        @ $11.00
    choix [e]  :  3 jours          @ $21.25
    choix [f]  :  Semaine          @ $29.00
    choix [g]  :  Mensuel          @ $94.00
    choix [i]  :  Soiree illimite  @ $5.75
    choix [j]  :  Weekend illimite @ $14.75
    
    choix [q]  :  Annuler la transaction
    ''')
    x2 = str(input("Votre choix : "))
    while x2 not in 'abcdefgijq':
        x2 = str(input(erreur))
    if x2 == 'a':
        print(block)
        print('''
        Tarif Ordinaire
        1 passage      @ $3.50
        ''')
    elif x2 == 'b':
        print(block)
        print('''
        Tarif Ordinaire
        2 passages       @ $6.50
        ''')
    elif x2 == 'c':
        print(block)
        print('''
        Tarif Ordinaire
        10 passages      @ $31.50
        ''')
    elif x2 == 'd':
        print(block)
        print('''
        Tarif Ordinaire
        24 heures        @ $11.00
        ''')
    elif x2 == 'e':
        print(block)
        print('''
        Tarif Ordinaire
        3 jours          @ $21.25
        ''')
    elif x2 == 'f':
        print(block)
        print('''
        Tarif Ordinaire
        Semaine          @ $29.00
        ''')
    elif x2 == 'g':
        print(block)
        print('''
        Tarif Ordinaire
        Mensuel          @ $94.00
        ''')
    elif x2 == 'i':
        print(block)
        print('''
        Tarif Ordinaire
        Soiree illimite  @ $5.75
        ''')
    elif x2 == 'j':
        print(block)
        print('''
        Tarif Ordinaire
        Weekend illimite @ $14.75
        ''')
elif x1 == 'q':
    print(quit)
    exit()
if x2 == 'q':
    print(quit)
    exit()
x3 = str(input("Choisissez le paiement : "))
while x3 not in 'bcq':
    x3 = str(input(erreur))
if x3 == 'q':
    print(quit)
    exit()
elif x3 == 'b':
    print('''
    SVP inserer la carte bancaire
    ''')
    time.sleep(2)
    print("    Lecture de la carte")
    print("   ")
    time.sleep(3)
    print("    Entrez votre NIP :")
    time.sleep(2)
    print('''
    Veuillez patienter pendant le traiment...
    
    *****    ''')
    time.sleep(1)
    print("    ****")
    time.sleep(1)
    print("    ***")
    time.sleep(1)
    print("    **")
    time.sleep(1)
    print("    *")
    time.sleep(1)
    print("   ")
    print("    Heure de la transaction : ")
    print(now.strftime("    %Y-%m-%d %H:%M:%S"))
    time.sleep(1)
    print(succ)
elif x3 == 'c':
    print('''
        SVP inserer la monnaie...

        ''')
    time.sleep(3)
    print("    Total restant : $0.00")
    print("   ")
    time.sleep(2)
    print("    Heure de la transaction : ")
    print(now.strftime("    %Y-%m-%d %H:%M:%S"))
    time.sleep(1)
    print(succ)
    exit()
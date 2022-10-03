# Aplikace je spustitelná s verzí Python 3.5 v režimu CMD.

from ast import If, main
from email.mime import application
from pdb import Restart


print("© Tomáš Machač | Aplikace Kalkulačka BETA VERZE")
print("------------------------------------------------")
print("Vítejte v aplikaci Kalkulačka.")
print("Pro následující matematickou operaci zvolte písmeno:")
print("Sčítání [S]")
print("Odčítání [O]")
print("Násobení [N]")
print("Dělení [D]")
print("======================================================")
zadejV=input()

#SČÍTÁNÍ
if (zadejV=="S"):
    try:
        print()
        print("Budeme sčítat !")
        print("Zadejte první číslo:")
        cislo1=input()
        print("Zadejte druhé číslo:")
        cislo2=input()
        X=int(cislo1)
        Y=int(cislo2)
        vysledek=X+Y
        print("")
        print("Výsledek je:")
        print(vysledek)
    except:
        print()
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("ERROR: DOŠLO K CHYBĚ V APLIKACI")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
#ODČÍTÁNÍ
if (zadejV=="O"):
    try:   
        print()
        print("Budeme odčítat !")
        print("Zadejte první číslo:")
        cislo1=input()
        print("Zadejte druhé číslo:")
        cislo2=input()
        X=int(cislo1)
        Y=int(cislo2)
        vysledek=X-Y
        print("")
        print("Výsledek je:")
        print(vysledek)
    except:
        print()
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("ERROR: DOŠLO K CHYBĚ V APLIKACI")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
#NÁSOBENÍ
if (zadejV=="N"):
    try:
        print()
        print("Budeme násobit !")
        print("Zadejte první číslo:")
        cislo1=input()
        print("Zadejte druhé číslo:")
        cislo2=input()
        X=int(cislo1)
        Y=int(cislo2)
        vysledek=X*Y
        print("")
        print("Výsledek je:")
        print(vysledek)
    except:
        print()
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("ERROR: DOŠLO K CHYBĚ V APLIKACI")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
#DĚLENÍ
if (zadejV=="D"):
    try:
        print()
        print("Budeme dělit !")
        print("Zadejte první číslo:")
        cislo1=input()
        print("Zadejte druhé číslo:")
        cislo2=input()
        X=int(cislo1)
        Y=int(cislo2)
        vysledek=X/Y
        print("")
        print("Výsledek je:")
        print(vysledek)
    except:
        print()
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("ERROR: DOŠLO K CHYBĚ V APLIKACI")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print("")
print("Stiskněte ENTER pro ukončení aplikace ...")
input()

# Jedná se o soukromou aplikaci, ve které se mohou nacházet chyby.
# Beta verze
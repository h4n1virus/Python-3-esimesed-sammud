# Sander Viirmaa
# 19.12.2018
# Ülesanne 07 - 03

from os import system
from math import pi

def kuup(a):
    v = a**3
    return v

def kera(r):
    v = 4 / 3 * pi * r**3
    return v

def koonus(h, sp):
    v = 1 / 3 * sp * h
    return v

def silinder(h, r):
    v = pi * r**2 * h
    return v

while True:
    system('cls')
    print("********** LEIAME RUUMALA **********")
    print("Vali kujund")
    print("1 Kuup")
    print("2 Kera")
    print("3 Koonus")
    print("4 Silinder")
    print("5 Tagasi\n")
    a = int(input("Sisesta soovitud kujundi number: "))

    if a == 1:
        a = float(input("Valisid kuubi. Sisesta kuubi külg: "))
        print('\nKuubi ruumala on: {}'.format(kuup(a)))
        input()
        continue
    elif a == 2:
        r = float(input("Valisid kera. Sisesta kera raadius: "))
        print('\nKera ruumala on: {}'.format(kuup(r)))
        input()
        continue
    elif a == 3:
        h = float(input("Valisid koonuse. Sisesta koonuse kõrgus: "))
        sp = float(input("Valisid koonuse. Sisesta koonuse põhjapindala: "))
        print("Koonuse ruumala on: {}".format(koonus(h, sp)))
        input()
        continue
    elif a == 4:
        h = float(input("Valisid Silindri. Sisesta silindri kõrgus: "))
        r = float(input("Valisid Silindri. Sisesta silindri raadius: "))
        print("Silindri ruumala on: {}".format(silinder(h, r)))
        input()
        continue
    elif a == 5:
        break
# Sander Viirmaa
# 19.12.2018
# Ülesanne 07 - 03

from os import system
from math import pi

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
        v = a**3
        print('\nKuubi ruumala on: {}'.format(v))
        input()
        continue
    elif a == 2:
        r = float(input("Valisid kera. Sisesta kera raadius: "))
        v = 4 / 3 * pi * r**3
        print('\nKera ruumala on: {}'.format(v))
        input()
        continue
    elif a == 3:
        sp = float(input("Valisid koonuse. Sisesta koonuse kõrgus: "))
        st = float(input("Valisid koonuse. Sisesta koonuse põhjapindala: "))
        v = 1 / 3 * sp * st
        print("Koonuse ruumala on: {}".format(v))
        input()
        continue
    elif a == 4:
        h = float(input("Valisid Silindri. Sisesta silindri kõrgus: "))
        r = float(input("Valisid Silindri. Sisesta silindri raadius: "))
        v = pi * r**2 * h
        print("Silindri ruumala on: {}".format(v))
        input()
        continue
    elif a == 5:
        break
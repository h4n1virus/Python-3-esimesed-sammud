# Sander Viirmaa
# 19.12.2018
# Ülesanne 07 - 03

from os import system
from math import pi


def kuupV(a):
    v = a**3
    return v


def keraV(r):
    v = 4 / 3 * pi * r**3
    return v


def koonuseV(sp, st):
    v = 1 / 3 * sp * st
    return v


def silinderV(h, r):
    v = pi * r**2 * h
    return v


def yl03():
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
            print('\nKuubi ruumala on: {}'.format(kuupV(a)))
            input()
            continue
        elif a == 2:
            r = float(input("Valisid kera. Sisesta kera raadius: "))
            print('\nKera ruumala on: {}'.format(keraV(r)))
            input()
            continue
        elif a == 3:
            sp = float(input("Valisid koonuse. Sisesta koonuse kõrgus: "))
            st = float(
                input("Valisid koonuse. Sisesta koonuse põhjapindala: "))
            print("Koonuse ruumala on: {}".format(koonuseV(sp, st)))
            input()
            continue
        elif a == 4:
            h = float(input("Valisid Silindri. Sisesta silindri kõrgus: "))
            r = float(input("Valisid Silindri. Sisesta silindri raadius: "))
            print("Silindri ruumala on: {}".format(silinderV(h, r)))
            input()
            continue
        elif a == 5:
            break

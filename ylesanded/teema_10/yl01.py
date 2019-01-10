# Sander Viirmaa
# 19.12.2018
# Ülesanne 10 - 01

from re import compile

f = open('tekstifailid\\yl10.txt', 'r')
b = f.read().splitlines()
c = compile(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$')
print("Filtreeritud IP\n")

for x in b:
    if c.match(x):
        print(x)

f.close()
# Sander Viirmaa
# 19.12.2018
# Ülesanne 10 - 02

from re import compile

f = open('tekstifailid\\yl10.txt', 'r')
b = f.read().splitlines()
c = compile('[A-Z]')
d = compile('[a-z]')
e = compile('[0-9]')

for x in b:
    if c.search(x) and d.search(x) and e.search(x):
        print(x)

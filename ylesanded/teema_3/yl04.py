# Sander Viirmaa
# 19.12.2018
# Ülesanne 03 - 04

from math import floor

a = input('Mis kell algavad teie tunnid?: ')
b = input('Mis kell lõpevad teie tunnid?: ')

c = a.split(':')
d = b.split(':')

e = int(c[0]) * 60 + int(c[1])
f = int(d[0]) * 60 + int(d[1])
g = floor((f - e) / 60)
h = (f - e) % 60

print('{0}:{1}'.format(g, h))
# Sander Viirmaa
# 19.12.2018
# Ülesanne 02 - 06

from math import floor

a = int(input('Mitu minutit: '))
b = a % 60
c = a / 60
d = floor(c)
print('{}:{}'.format(d, b))

# Sander Viirmaa
# 19.12.2018
# Ülesanne 05 - 05

from random import randint

c = '*'
a = []
i = 0

while i < 6:
    a.append(randint(1, 10))
    i = i + 1

for x in a:
    print("{0}: {1}".format(x, (c * x)))
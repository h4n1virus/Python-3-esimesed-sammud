# Sander Viirmaa
# 19.12.2018
# Ülesanne 06 - 01

a = open('tekstifailid\\s6pru_l6ustaraamatus.txt', 'r')
b = a.read()
c = b.splitlines()

for x in c:
    h = x.split()
    print('{:20}{:<20}{:<10}{:<}'.format(h[0], h[1], h[2], h[3]))

a.close()

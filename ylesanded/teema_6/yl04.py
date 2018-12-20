# Sander Viirmaa
# 19.12.2018
# Ülesanne 06 - 04


a = open('tekstifailid\\s6pru_l6ustaraamatus.txt', 'r')
b = open('tekstifailid\\teema6_yl04.txt', 'w')
c = a.read()
d = c.splitlines()

for x in d:
    h = x.split()
    b.write('{:15}{:<15}\n'.format(h[0], h[1]))

a.close()
b.close()


# Sander Viirmaa
# 19.12.2018
# Ülesanne 06 - 03

a = open('tekstifailid\\s6pru_l6ustaraamatus.txt', 'r')
b = a.read()
c = b.splitlines()
d = list()

print('{:15}{:<15}{:<10}{:<}'.format('Eesnimi', 'Perenimi', 'Erakond',
                                     'Number'))

for x in c:
    h = x.split()
    d.append(h[2])
    print('{:15}{:<15}{:<10}{:<}'.format(h[0], h[1], h[2], h[3]))

print('\nReformikaid: {}'.format(d.count('RE')))
print('Kesikuid: {}'.format(d.count('KE')))
d.sort()
print('Erakondi kokku: {}'.format(len(d)))

a.close()
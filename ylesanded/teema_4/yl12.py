# Sander Viirmaa
# 19.12.2018
# Ülesanne 04 - 12

a = float(input('Kui palju raha te soovite hoiustada?: '))
b = int(input('Mitmeks aastaks, te soovite raha hoiustada?: '))
c = 0.05
e = a
h = a
print('{:<5}{:<13}{:<13}{:<10}'.format('Aasta', 'Algsumma', 'Intress',
                                       'Aastalõpp'))

for i in range(1, b + 1):
    d = round((a * c), 2)
    a = round((a + d), 2)
    print('{:<5}{:<13}{:<13}{:<10}'.format(i, e, d, a))
    e = a
    g = round((a - h), 2)

print('Summa kokku: {} eurot'.format(a))
print('Kasum: {} eurot'.format(g))
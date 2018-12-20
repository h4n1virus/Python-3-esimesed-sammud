# Sander Viirmaa
# 19.12.2018
# Ülesanne 04 - 11

from random import randint

a = int(input('Andke väikseim arv: '))
b = int(input('Andke suurim arv: '))
c = randint(a, b)

print('Teil on kolm korda võimalik ära arvata')

i = 0
while i <= 3:
    d = input('Arvake ära suvaline arv: ')
    i = i + 1
    if i == 3:
        print('Te olete oma kolm korda ära arvanud')
        e = str(input('Kas te soovite edasi proovida? (J/E)')).lower()
        if 'e' in e:
            break
        elif 'j' in e:
            i = 0
    elif d == c:
        print('Õnnitleme te arvasite ära')
    elif d != c:
        print('Proovige uuesti')

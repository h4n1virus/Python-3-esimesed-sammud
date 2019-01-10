# Sander Viirmaa
# 19.12.2018
# Ülesanne 05 - 02

a = ['Juhan', 'Kati', 'Maarja', 'Mario', 'Mati']

while True:
    for b in a:
        print('{}'.format(b))

    print('Sisestage x kui soovite harjutust sulgeda.')
    c = input('Kas te soovite kellegi nime muuta?: ')

    if 'x' in c:
        break
    elif c in a:
        a.remove(c)
        d = input('Uus nimi: ')
        a.append(d)
    else:
        print('\nSellist nime pole!\n')
        input('Vajutage RETURN klahvi, et jätakata\n')
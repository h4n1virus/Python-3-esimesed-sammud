# Sander Viirmaa
# 19.12.2018
# Ülesanne 04 - 04


a = float(input('Kui palju toode maksab?: '))
if a < float(10):
    b = a * 0.10
    c = round((a - b), 2)
    print('Toote soodushind on: {}'.format(c))
else:
    b = a * 0.20
    c = round((a - b), 2)
    print('Toote soodushind on: {}'.format(c))



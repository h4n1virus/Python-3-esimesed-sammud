# Sander Viirmaa
# 19.12.2018
# Ülesanne 03 - 05

a = input('Sisestage palindroom: ')

if a == a[::-1]:
    print('Palindroom')
else:
    print('Ei ole palindroom')

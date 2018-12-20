# Sander Viirmaa
# 19.12.2018
# Ülesanne 04 - 02


a = float(input('Sisestage arv: '))
b = float(input('Sisestage arv: '))
c = input('Mis tehet te soovite teha? + - * / : ')

if '*' in c:
    d = a * b
    print('Korrutamise vastuseks tuli: {}'.format(d))
elif '/' in c:
    d = a / b
    print('Jagamise vastuseks tuli: {}'.format(d))
elif '+' in c:
    d = a + b
    print('Liitmise vastuseks tuli: {}'.format(d))
elif '-' in c:
    d = a - b
    print('Lahutamise vastuseks tuli: {}'.format(d))



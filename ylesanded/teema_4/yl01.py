# Sander Viirmaa
# 19.12.2018
# Ülesanne 04 - 01

a = float(input('Külg a: '))
b = float(input('Külg b: '))
c = float(input('Külg c: '))
d = float(input('Külg d: '))

if a == b and a == c and a == d:
    print('Tegemist on ristküliku erijuhuga, ehk ruuduga')
else:
    print('Tegemist on mingisuguse muu kujundiga')
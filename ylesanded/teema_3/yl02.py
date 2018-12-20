# Sander Viirmaa
# 19.12.2018
# Ülesanne 03 - 02


from re import compile, I


a = input('Kogemata vandumist ja muud teksti paluks: ')
b = compile('kurat', I)
c = b.sub('***', a)

print('{}'.format(c))



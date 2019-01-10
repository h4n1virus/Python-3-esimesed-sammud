# Sander Viirmaa
# 19.12.2018
# Ülesanne 05 - 01

a = []

for i in range(0, 5):
    b = str(input('Paluks nime: '))
    a.append(b)
    
c = a[4]
a.sort()

for d in a:
    print(d)

print('Viimaseks nimeks oli: {}'.format(c))
# Sander Viirmaa
# 19.12.2018
# Ülesanne 03 - 03

from datetime import datetime

a = int(input('Mis on teie sünniaasta: '))
b = datetime.now()
c = b.year - a
if c % 10 == 0:
    print('Teil on juubel see aasta')
else:
    print('Teil ei ole juubel see aasta')
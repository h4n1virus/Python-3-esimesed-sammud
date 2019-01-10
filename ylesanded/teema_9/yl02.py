# Sander Viirmaa
# 19.12.2018
# Ülesanne 09 - 02

from datetime import datetime

date = datetime.today()

b = str(input("Sisestage isikukood: "))
c = int(b[0])
d = b[1:3]
e = b[3:5]
f = b[5:7]

if c == 3 or c == 4:
    z = "19"
if c == 5 or c == 6:
    z = "20"

g = datetime((int(z + d)), int(e), int(f))
f = date.year - g.year - ((date.month, date.day) < (g.month, g.day))
print("Teie sünnikuupäevaks on: {}.{}.{}".format(g.day, g.month, g.year))
print("Te olete: {} aastane vanune".format(f))
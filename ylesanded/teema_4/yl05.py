# Sander Viirmaa
# 19.12.2018
# Ülesanne 04 - 05


from datetime import datetime


a = str(input('Mis soost te olete (m/n): ')).lower()
a = a[0]

if 'n' in a:
    print("Te ei ole sobilik")
elif 'm' in a:
    b = int(input('Mis aastal te sündinud olete: '))
    c = datetime.now().year - b
    if c < 16 and c > 18:
        print("Teretulemast meeskonda!")
    elif c < 16:
        print("Paari aasta pärast proovi uuesti")
    elif c > 18:
        print("Te ei ole sobilik")
else:
    print("Te ei ole sobilik")



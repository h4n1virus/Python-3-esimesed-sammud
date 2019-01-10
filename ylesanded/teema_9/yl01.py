# Sander Viirmaa
# 19.12.2018
# Ülesanne 09 - 01

from datetime import datetime

date = datetime.today()

def switcher(a):
    if date.month == 1:
        return "Jaanuar"
    elif date.month == 2:
        return "Veebruar"
    elif date.month == 3:
        return "Märts"
    elif date.month == 4:
        return "Aprill"
    elif date.month == 5:
        return "Mai"
    elif date.month == 6:
        return "Juuni"
    elif date.month == 7:
        return "Juuli"
    elif date.month == 8:
        return "August"
    elif date.month == 9:
        return "September"
    elif date.month == 10:
        return "Oktoober"
    elif date.month == 11:
        return "November"
    elif date.month == 12:
        return "Detsember"

print('{}. {} {}'.format(date.day, date.strftime("%B"), date.year))
print('{}. {}. {}'.format(date.day, switcher(date.month), date.year))
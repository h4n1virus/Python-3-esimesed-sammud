# Sander Viirmaa
# 19.12.2018
# Ülesanne 09 - 01

from datetime import datetime


def switcher(month):
    if month == 1:
        return "Jaanuar"
    elif month == 2:
        return "Veebruar"
    elif month == 3:
        return "Märts"
    elif month == 4:
        return "Aprill"
    elif month == 5:
        return "Mai"
    elif month == 6:
        return "Juuni"
    elif month == 7:
        return "Juuli"
    elif month == 8:
        return "August"
    elif month == 9:
        return "September"
    elif month == 10:
        return "Oktoober"
    elif month == 11:
        return "November"
    elif month == 12:
        return "Detsember"

date = datetime.today()
print('{}. {} {}'.format(date.day, date.strftime("%B"), date.year))
print('{}. {}. {}'.format(date.day, switcher(date.month), date.year))

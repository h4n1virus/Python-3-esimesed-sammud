# Sander Viirmaa
# 19.05.2022
# Ülesanne 09 - 01

from datetime import datetime

months = ["", "Jaanuar", "Veebruar", "Märts",
          "Aprill", "Mai", "Juuni",
          "Juuli", "August", "September",
          "Oktoober", "November", "Detsember"] 

date = datetime.today()
print('{}. {} {}'.format(date.day, date.strftime("%B"), date.year))
print('{}. {}. {}'.format(date.day, months[date.month], date.year))

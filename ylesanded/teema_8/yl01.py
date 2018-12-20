# Sander Viirmaa
# 19.12.2018
# Ülesanne 08 - 01


class auto:
    mark = ' '
    aasta = 0
    hind = 0

    def __init__(self, x, y, z):
        self.mark = x
        self.aasta = y
        self.hind = z

    def lisaMark(self, x):
        self.mark = x
    
    def lisaAasta(self, x):
        self.aasta = x
    
    def kuva(self):
        print("\nMark: {0}\nAasta: {1}\nHind: {2}".format(self.mark, self.aasta, self.hind))


liikur = auto("Audi", 1988, 600)
liikur.kuva()

liikur2 = auto("Mercedes-Benz", 1980, 2400)
liikur2.kuva()



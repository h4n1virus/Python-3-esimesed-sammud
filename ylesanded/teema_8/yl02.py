# Sander Viirmaa
# 19.12.2018
# Ülesanne 08 - 02


class auto:
    mark = ' '
    aasta = 0
    hind = 0
    värv = ' '
    kiirus = 0

    def __init__(self, x, y, z, q, w):
        self.mark = x
        self.aasta = y
        self.hind = z
        self.kiirus = q
        self.varv = w

    def lisaMark(self, x):
        self.mark = x

    def lisaAasta(self, x):
        self.aasta = x

    def lisaVarv(self, x):
        self.varv = x

    def lisaKiirus(self, x):
        self.kiirus = x

    def kuva(self):
        print(
            '\nMark: {0}\nAasta: {1}\nHind: {2}\nVärvus: {3}\nTippkiirus: {4}'.
            format(self.mark, self.aasta, self.hind, self.varv, self.kiirus))


liikur = auto('Audi', 1988, 600, 180, 'Kirss Punane')
liikur.kuva()

liikur2 = auto('Mercedes-Benz', 1980, 2400, 140, 'Sinine')
liikur2.kuva()

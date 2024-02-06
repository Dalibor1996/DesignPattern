# class Napoj:
#     def cena(self):
#         raise NotImplementedError

class Kava:
    def cena(self):
        return 2

class Caj:
    def cena(self):
        return 3

class PrisadaDecorator:
    def __init__(self, napoj):
        self.napoj = napoj

    def cena(self):
        return self.napoj.cena()

class Mlieko(PrisadaDecorator):
    def cena(self):
        return self.napoj.cena() +5

class Cukor(PrisadaDecorator):
    def cena(self):
        return self.napoj.cena() + 2

moja_kava = Kava()
moja_kava = Mlieko(moja_kava)
moja_kava = Cukor(moja_kava)
print(moja_kava.cena())

moj_caj = Caj()
moj_caj = Cukor(moj_caj)
print(moj_caj.cena())

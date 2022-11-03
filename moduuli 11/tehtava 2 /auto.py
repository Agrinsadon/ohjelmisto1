class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nopeus = 0, kokonaismatka = 0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.kokonaismatka = kokonaismatka

    def kiihtyvyys(self, uusinopeus):
        if self.nopeus + uusinopeus >= 0 and self.nopeus + uusinopeus <= self.huippunopeus:
            self.nopeus = self.nopeus + uusinopeus
        elif self.nopeus + uusinopeus < 0:
            self.nopeus = 0
        elif self.nopeus + uusinopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus

    def matka_tunti(self, tunti):
        self.kokonaismatka = self.kokonaismatka + self.nopeus * tunti

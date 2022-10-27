import random
class Car:
    def __init__(self, rekisterinumero, huippunopeus, nopeus, kokonaismatka):
        self.kokonaismatka = kokonaismatka
        self.nopeus = nopeus
        self.huippunopeus = huippunopeus
        self.rekisterinumero = rekisterinumero

    def kiihtyvyys(self, speed):
        self.nopeus = self.nopeus + speed
        if self.nopeus > self.nopeus:
            self.nopeus = self.nopeus
        elif self.nopeus < 0:
            self.nopeus = 0

    def matka_aika(self, tunti):
        self.kokonaismatka = self.kokonaismatka + (self.nopeus * tunti)


# Pääohjelma
cars = []

for i in range(10):
    cars.append(Car(f"ABC-{i + 1}", random.randint(100, 200), 0, 0))

stopper = False
while not stopper:
    for i in cars:
        i.kiihtyvyys(random.randint(-10, 15))
        i.matka_aika(1)
        if i.kokonaismatka >= 10000:
            for n in cars:
                print(f"|{n.rekisterinumero}|{n.huippunopeus}|{n.nopeus}|{n.kokonaismatka}|")
                stopper = True
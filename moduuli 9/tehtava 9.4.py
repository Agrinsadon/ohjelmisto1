from prettytable import PrettyTable
import random
class Car:
    def __init__(self, rekisterinumero, huippunopeus, nopeus, kokonaismatka):
        self.kokonaismatka = kokonaismatka
        self.nopeus = nopeus
        self.huippunopeus = huippunopeus
        self.rekisterinumero = rekisterinumero

    def kiihtyvyys(self, nopeuden_muunnos):
        if self.nopeus + nopeuden_muunnos >= 0 and self.nopeus + nopeuden_muunnos <= self.huippunopeus:
            self.nopeus = self.nopeus + nopeuden_muunnos

        elif self.nopeus + nopeuden_muunnos < 0:
            self.nopeus = 0

        elif self.nopeus + nopeuden_muunnos > self.huippunopeus:
            self.nopeus = self.huippunopeus

    def matka_aika(self, tunti):
        self.kokonaismatka = self.kokonaismatka + (self.nopeus * tunti)

def moi():
    x.field_names = ["Rekisterinumero", "Huippunopeus", "Hetkellinen nopeus", "Kokomatka"]
    for i in cars:
        x.add_row([i.rekisterinumero, f"{i.huippunopeus}KM/H", f"{i.nopeus}KM/H", f"{i.kokonaismatka}KM"])

x = PrettyTable()
cars = []

for i in range(10):
    cars.append(Car(f"ABC-{i + 1}", random.randint(100, 200), 0, 0))

stopper = False
while not stopper:
    for i in cars:
        i.kiihtyvyys(random.randint(-10, 15))
        i.matka_aika(1)
        if i.kokonaismatka >= 10000:
            stopper = True
moi()
print(x)
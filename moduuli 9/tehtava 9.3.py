# Laajenna ohjelmaa siten, että mukana on kulje-metodi, joka saa parametrinaan tuntimäärän.
# Metodi kasvattaa kuljettua matkaa sen verran kuin auto on tasaisella vauhdilla annetussa
# tuntimäärässä edennyt. Esimerkki: auto-olion tämänhetkinen kuljettu matka on 2000 km.
# Nopeus on 60 km/h. Metodikutsu auto.kulje(1.5) kasvattaa kuljetun matkan lukemaan 2090 km.

class auto:

    def __init__(self, rekisteritunnus, huippunopeus, nopeus = 0, kuljettu_matka = 0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.kuljettu_matka = kuljettu_matka


    def accelerate(self, nopeuden_muunnos):
        if self.nopeus + nopeuden_muunnos >= 0 and self.nopeus + nopeuden_muunnos <= self.huippunopeus:
            self.nopeus = self.nopeus + nopeuden_muunnos

        elif self.nopeus + nopeuden_muunnos < 0:
            self.nopeus = 0

        elif self.nopeus + nopeuden_muunnos > self.huippunopeus:
            self.nopeus = self.huippunopeus

    def kulje(self, tunti):
        self.kuljettu_matka = self.kuljettu_matka + self.nopeus * tunti

#PÄÄOHJELMA
auto1 = auto(f"HIZ-709", 142)

print(f"auto1\nrekisterinumero on {auto1.rekisteritunnus} \nHuippunopeus on {auto1.huippunopeus} KM/H"
f"\nHetkellinen nopeus on {auto1.nopeus} KM/H \nKuljettumatka on {auto1.kuljettu_matka} M")

auto1.accelerate(60)

print(f"Nopeus nyt: {auto1.nopeus}")
auto1.kuljettu_matka = 2000
print(f"Kuljettu matka: {auto1.kuljettu_matka}")
auto1.kulje(1.5)
print(f"Kuljettu matka: {auto1.kuljettu_matka}")

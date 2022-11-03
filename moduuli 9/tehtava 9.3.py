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
        self.kuljettu_matka += self.nopeus * tunti
    def info(self):
        print(f"rekisterinumero on {auto1.rekisteritunnus}, Huippunopeus on {auto1.huippunopeus} KM/H,"
             f"Hetkellinen nopeus on {auto1.nopeus} KM/H, Kuljettumatka on {auto1.kuljettu_matka} KM")

#PÄÄOHJELMA
auto1 = auto(f"HIZ-709", 200)
auto1.accelerate(60)
auto1.kulje(1)
auto1.info()

auto1.accelerate(50)
auto1.kulje(2)
auto1.info()



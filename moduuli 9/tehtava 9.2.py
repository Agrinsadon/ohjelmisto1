#Jatka ohjelmaa kirjoittamalla Auto-luokkaan kiihdytä-metodi, joka saa parametrinaan
# nopeuden muutoksen (km/h). Jos nopeuden muutos on negatiivinen, auto hidastaa.
# Metodin on muutettava auto-olion nopeus-ominaisuuden arvoa. Auton nopeus ei saa
# kasvaa huippunopeutta suuremmaksi eikä alentua nollaa pienemmäksi. Jatka pääohjelmaa
# siten, että auton nopeutta nostetaan ensin +30 km/h, sitten +70 km/h ja lopuksi +50 km/h.
# Tulosta tämän jälkeen auton nopeus. Tee sitten hätäjarrutus määräämällä nopeuden muutos
# -200 km/h ja tulosta uusi nopeus. Kuljettua matkaa ei tarvitse vielä päivittää.


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

#PÄÄOHJELMA
auto1 = auto(f"HIZ-709", 142)

print(f"auto1\nrekisterinumero on {auto1.rekisteritunnus} \nHuippunopeus on {auto1.huippunopeus} KM/H"
f"\nHetkellinen nopeus on {auto1.nopeus} KM/H \nKuljettumatka on {auto1.kuljettu_matka} M")

auto1.accelerate(30)
auto1.accelerate(70)
auto1.accelerate(50)

print(f"Nopeus nyt: {auto1.nopeus}")
auto1.accelerate(-200)
print(f"Nopeus nyt: {auto1.nopeus}")



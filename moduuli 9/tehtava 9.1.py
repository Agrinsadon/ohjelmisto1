# Kirjoita Auto-luokka, jonka ominaisuuksina ovat rekisteritunnus, huippunopeus,
# tämänhetkinen nopeus ja kuljettu matka. Kirjoita luokkaan alustaja, joka
# asettaa ominaisuuksista kaksi ensin mainittua parametreina saatuihin arvoihin.
# Uuden auton nopeus ja kuljetut matka on asetettava automaattisesti nollaksi.
# Kirjoita pääohjelma, jossa luot uuden auton (rekisteritunnus ABC-123, huippunopeus 142 km/h).
# Tulosta pääohjelmassa sen jälkeen luodun auton kaikki ominaisuudet.

class auto:

    def __init__(self, rekisteritunnus, huippunopeus, nopeus = 0, kuljettu_matka = 0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.kuljettu_matka = kuljettu_matka
        print("Uusi auto luotu")

    def info(self):
        print(f"rekisterinumero: {self.rekisteritunnus}, Huippunopeus: {self.huippunopeus} KM/H"
              f"\nHetkellinen nopeus: {self.nopeus} KM/H, Kuljettumatka: {self.kuljettu_matka} M")

auto1 = auto(f"HIZ-709", 200)
auto1.info()
print("------------------------------------------------")
auto2 = auto(f"GUG-112", 180)
auto2.info()

from auto import Auto
class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, tankki, nopeus = 0, kokonaismatka = 0):
        self.tankki = tankki
        super().__init__(rekisteritunnus, huippunopeus, nopeus, kokonaismatka)
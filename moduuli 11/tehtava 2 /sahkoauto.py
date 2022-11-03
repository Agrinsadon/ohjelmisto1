from auto import Auto
class Sahkoauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akku, nopeus = 0, kokonaismatka = 0):
        self.akku = akku
        super().__init__(rekisteritunnus, huippunopeus, nopeus, kokonaismatka)
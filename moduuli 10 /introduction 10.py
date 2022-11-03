class Auto:
    def __init__(self, rekisteritunnus, vari):
        self.rekisteritunnus = rekisteritunnus
        self.vari = vari

class Maalaamo:
    def maalaa(self, auto, vari):
        auto.vari = vari

bmw = Auto("ABC-123", "viherä")

print("Auto on " + bmw.vari)

suomenmaalaamo = Maalaamo()

suomenmaalaamo.maalaa(bmw, "punainen")

print("Auto on nyt " + bmw.vari)
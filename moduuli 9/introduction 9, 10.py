class kissa:
    jalka_maara = 4
    tehty = 0

    def __init__(self, nimi, syntymavuosi, rotu, paino, haukahdus="vyh vyh"):
        self.nimi = nimi
        self.syntymavuosi = syntymavuosi
        self.rotu = rotu
        self.paino = paino
        self.haukahdus = haukahdus
        kissa.tehty = kissa.tehty + 1

    def hauku(self, kerrat):
        for i in range(kerrat):
            print(self.haukahdus)

class Hoitola:
    def __init__(self):
        self.kissat = []

    def kissa_sisaan(self, kissa):
        self.kissat.append(kissa)
        print(kissa.nimi + ": kirjattu sisään")
        return

    def kissa_ulos(self, kissa):
        self.kissat.remove(kissa)
        print(kissa.nimi + ": kirjattu ulos")
        return

    def tervehdi_kissa(self):
        for kissa in self.kissat:
            kissa.hauku(1)

# PÄÄOHJELMA
hoitola = Hoitola()

kissa1 = kissa("Pekka", 1999, "Saksanpaimenkissa", 25, "miaw miaw")
print(f"kissa1\nnimi on {kissa1.nimi:s} \nSyntymävuosi on {kissa1.syntymavuosi:d} "
      f"\nRotu on {kissa1.rotu:s} \nPaino on {kissa1.paino:d}KG")
kissa1.hauku(2)

print("--------------------------")

kissa2 = kissa("Seppo", 2003, "Agueropainen", 10, "ggrpaw ggrrrpaw")
print(f"kissa2\nnimi on {kissa2.nimi:s} \nSyntymävuosi on {kissa2.syntymavuosi:d} "
      f"\nRotu on {kissa2.rotu:s} \nPaino on {kissa2.paino:d}KG")
kissa2.hauku(3)

print("--------------------------")

print("Kissojen jalkamäärät")
print(f"Kissa1: {kissa1.jalka_maara} jalkaa")
print(f"Kissa2: {kissa2.jalka_maara} jalkaa")

print("--------------------------")

print("Kissojen määrä")
print(f"Kissoja on nyt {kissa.tehty}")
kissa1.tehty = 10
print(f"Kissoja on nyt {kissa1.tehty}")

print("--------------------------")

hoitola = Hoitola()

hoitola.kissa_sisaan(kissa1)
hoitola.kissa_sisaan(kissa2)
hoitola.tervehdi_kissa()

hoitola.kissa_ulos(kissa1)
hoitola.tervehdi_kissa()
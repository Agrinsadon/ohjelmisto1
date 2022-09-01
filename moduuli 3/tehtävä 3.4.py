#lasketaan karkausvuodet
vuosiluku = int(input("Kerro vuosiluku:"))
if vuosiluku % 4 == 0 and (vuosiluku % 100 != 0 or vuosiluku % 400 == 0):
    print("Annettu vuosi oli karkausvuosi.")
else:
    print("Annettu vuosi ei ollut karkausvuosi.")
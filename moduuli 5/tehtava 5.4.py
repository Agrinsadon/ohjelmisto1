#Kirjoita ohjelma, joka kysyy käyttäjältä viiden kaupungin
#nimet yksi kerrallaan ja tallentaa ne listarakenteeseen.
#Lopuksi ohjelma tulostaa kaupunkien nimet yksi kerrallaan
#allekkain samassa järjestyksessä kuin ne syötettiin

kaupungit = []

for _ in range(5):
    kaupunki = input("Anna kaupunki: ")
    kaupungit.append(kaupunki)
for k in kaupungit:
    print(k)



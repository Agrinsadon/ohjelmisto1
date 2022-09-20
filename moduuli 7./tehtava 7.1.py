#joka kysyy käyttäjältä kuukauden numeron,
#jonka jälkeen ohjelma tulostaa sitä vastaavan vuodenajan
#(kevät, kesä, syksy, talvi). (monikko rakenne)

vuodenajat = ("Talvi", "Kevät", "Kesä", "Syksy")
kuukaudet = int(input("Anna kuukauden numerot (1-12): "))

print(type(vuodenajat))



if 0 < kuukaudet <= 2 :
    print(vuodenajat[0])

elif 2 < kuukaudet <= 5:
    print(vuodenajat[1])

elif 5 < kuukaudet <= 8:
    print(vuodenajat[2])

elif 8 < kuukaudet <= 11:
    print(vuodenajat[3])

elif kuukaudet == 12:
    print(vuodenajat[0])

else:
    print("Väärä kuukausi anna 1-12 väiltä!")

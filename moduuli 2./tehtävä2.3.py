#Suorakulman kanta ja korkeus laskettuna piiri ja pinta-alaan.

kanta = input("Anna suorakolmion kanta (cm): ")
korkeus = input("Anna suorakolmion korkeus (cm): ")
kanta = float(kanta)
korkeus = float(korkeus)
area = kanta * korkeus
piiri = (kanta + korkeus) * 2
print(f"suorakolmion pinta-ala on {area:.2f} neliömetriä.")
print(f"suorakolmion piiri on {piiri:.2f}.")
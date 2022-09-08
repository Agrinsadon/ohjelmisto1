#Kirjoita funktio, joka saa parametrinaan listan
#kokonaislukuja. Ohjelma palauttaa listassa olevien
#lukujen summan. Kirjoita testausta varten
#pääohjelma, jossa luot listan, kutsut funktiota
#ja tulostat sen palauttaman summan.

luvut = []

def numerot(luvut):
    num = 0
    for i in luvut:
        num = num + i
    summa = print(f"Listan Summa on {num}")
    return

luku = input("Anna kokonaisluku: ")
while luku != "":
    luvut.append(int(luku))
    luku = input("Anna kokonaisluku: ")

else:
    print(luvut)
    numerot(luvut)











#väliltä 1..6. Kirjoita pääohjelma, joka
#heittää noppaa niin kauan kunnes tulee kuutonen.
#Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun.


import random


def noppa():
    row=[]
    randomnum = random.randint(1, 6)
    row.append(randomnum)
    return randomnum

while True:
    heitto = noppa()
    print(heitto)
    if heitto == 6:
        print("Numero 6 saatu!")
        print("Onneksi olkoa!")
        break

#Agrin_Sadon

#Muokkaa edellistä funktiota siten, että funktio
#saa parametrinaan nopan tahkojen yhteismäärän
#Edellisestä tehtävästä poiketen nopan heittelyä jatketaan
#pääohjelmassavkunnes saadaan nopan maksimisilmäluku,
#joka kysytään käyttäjältä ohjelman suorituksen alussa.

import random
inputti = int(input("Anna nopan maksimisilmäluku: "))

def noppa():
    lista = []
    roundnum = random.randint(1, inputti)
    lista.append(roundnum)
    return roundnum

while True:
    heitto = noppa()
    print(heitto)
    if heitto == inputti:
        print(f"Sait {inputti}")
        break

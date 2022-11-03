#arpa kone ja kertoo kuinka lähellä on tulosta

import random

random = random.randint(1, 10)
numero = int(input("Arvaa luku: "))

while numero != random:
    if numero > random:
       print("Liian suuri arvaus.")
    elif numero < random:
     print("Liian pieni arvaus. ")
    numero = int(input("Arvaa luku: "))

else:
    print("Oikein.")

#Agrin_Sadon



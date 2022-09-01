#arpa kone ja kertoo kuinka lähellä on tulosta

import random

random = random.randint(1, 10)
numero = ""

while numero != random:
    numero = int(input("Arvaa luku: "))
    if numero > random:
       print("Liian suuri arvaus.")
    elif numero < random:
     print("Liian pieni arvaus. ")

else:
    print("Oikein.")




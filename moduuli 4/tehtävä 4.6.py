#algoritmi

import random
maara = int(input("Montako kertaan arvotaan pisteiden määrää: "))
maara_2 = 0

for i in range(maara):
    x = random.uniform(-1, 1)
    y = random.uniform(1, -1)
    if x**2 + y**2 < 1:
        maara_2 += 1

pi = maara_2 / maara * 4
print(f"Pi on {pi}")

#Agrin_Sadon




import random
summa1 = []
arpakuutio = int(input("Anna arpakuutioiden lukumäärä: "))
for i in range(arpakuutio):
    numerot = random.randint(1, 6)
    summa1.append(numerot)
    print(numerot)
print("Yhteensä summa on:",sum(summa1))



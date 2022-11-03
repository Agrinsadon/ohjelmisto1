import math
taulu = []

cm1 = float(input("Anna pizza1 cm: "))
euro1 = int(input("Anna pizza1 euro: "))
cm2 = float(input("Anna pizza2 cm: "))
euro2 = int(input("Anna pizza2 euro: "))

def pizza(cm1, euro1, cm2, euro2):
    lista = []
    r = cm1 / 2
    area = math.pi * (r**2)
    nm1 = euro1 / 2
    lista.append(nm1)

    r2 = cm2 / 2
    area2 = math.pi * (r2**2)
    nm2 = euro2 / 2
    lista.append(nm2)
    return taulu.extend(lista)

print(pizza(cm1, euro1, cm2, euro2))
if taulu[0] > taulu[1]:
    print("Pizza1 on kalliimpi kuin pizza2")
elif taulu[0] < taulu[1]:
    print("Pizza1 on halvempi kuin pizza2")

#Agrin_Sadon


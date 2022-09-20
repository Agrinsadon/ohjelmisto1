
lista = set()
print(type(lista))

nimi = input("Anna nimi: ")
print("Tämä on uusi nimi")
while nimi != "":
    lista.add(nimi)
    nimi = str(input("Anna nimi: "))
    if nimi in lista:
        print("Nimi on annettu jo")
    elif nimi not in lista:
        print("Tämä on uusi nimi")
for _ in lista:
    print(_)
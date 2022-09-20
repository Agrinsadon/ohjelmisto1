
lento= {"Helsinki-Vantaan ":"ICAO-koodi on EFHK"}
command = input("Anna komento: ").lower()
if command == "haku":
    print("Anna ICAO-koodi")



def o():
    while True:
        command = input("Anna komento: ").lower()

        if command == "haku":
            print("Anna ICAO-koodi")

        elif command == "lopeta":
            print("Ohjelma lopetetaan")

        elif command == "uusi lentoasema":
            print("Anna ICAO-koodi")
            print("Anna lentoaseman nimi")

        else:
            print("Anna Uusi lentoasema, haku tai lopeta")



print(o())
print(command)

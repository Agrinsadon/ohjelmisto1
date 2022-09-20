


lento= {"Helsinki-Vantaan ":"ICAO-koodi on EFHK"}
command = input("Anna komento: ").lower()
if command == "haku":
    print("Anna ICAO-koodi")
for command in command:
    print("Helsinki-Vantaan")






def o():
    while True:
        command = input("Anna komento: ").lower()

        if command == "haku":
            print("Anna ICAO-koodi")

        elif command == "lopeta":
            print("Ohjelma lopetetaan")

        elif command == "uusi lentoasema":
            print("Anna ICAO-koodi ja nimi")

        else:
            print("Anna Uusi lentoasema, haku tai lopeta")



print(o())
print(command)


"""""""""# Sijoitetaan avaimella "aku" sama aravo, joka löytyy avaimella "Viivi"
phone_numbers["aku"] = phone_numbers["Viivi"]
print("2",phone_numbers)"""
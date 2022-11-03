"""num = 1
print(type(1))

numbers = [1, 2, 3, 4, 5]
numbers.append(6)
print(type(numbers))
print(numbers)

#1. alkio
print(numbers[0])
numbers[0] = 9
print(numbers[0])

"""
#monikko (tuple)
numbers = (1, 2, 3, 4, 5)
print(numbers)
print(numbers[0])
for n in numbers:
    print(n)


    print("----\nJoukku\n----")
# Joukko (set)
inverntory = {"Valomiekka", "Pyssy", "Kolikko", }
print(inverntory)

#lisää listaan
inverntory.add("porkkana")
print(inverntory)

#poista listasta
inverntory.remove("Pyssy")
print(inverntory)

# new set = {} <- ei toimi
new_set = set()
print(type(new_set))
new_set.add("item 1")
new_set.add("asia 2")
for item in new_set:
    print(item)

# joukon koko (eli pituus) samoin kuin listoilla.
print(len(new_set))
"""""
# sanakirja (dictionary)
hi = input("asd")
phone_numbers = {"Helsinki-Vantaan ":"ICAO-koodi on EFHK"}
phone_numbers["Viivi"] = "03405435034"
#lisätään uusi avain arvo-pari
print("1",phone_numbers)
print("Akun numero:", {phone_numbers["Aku"]})

# Sijoitetaan avaimella "aku" sama aravo, joka löytyy avaimella "Viivi"
phone_numbers["aku"] = phone_numbers["Viivi"]
print("2",phone_numbers)

for n in phone_numbers:
    print("avaimelle" + n + " palautuu arvo" + phone_numbers[n])"""
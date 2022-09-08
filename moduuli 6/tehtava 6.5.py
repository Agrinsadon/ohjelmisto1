#Anna lukuja kunnes pysähtyy enterillä ja anna kaikki luvut yhteen listaan
#ja tasaluvut yhteen listaan
tasaluvut = []

def tasainen_luku(tasaluvut):
    outputti = [x for x in tasaluvut if x % 2 == 0]
    return outputti

luku = input("Anna luku: ")
while luku != "":
    tasaluvut.append(int(luku))
    luku = input("Anna luku: ")
else:
    print(f"Kaikki luvut:",tasaluvut)
    print(f"Tasaluvut:",tasainen_luku(tasaluvut))




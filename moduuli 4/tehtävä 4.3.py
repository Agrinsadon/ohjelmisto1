#lukuja siihen saakka,
#kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
#tulosta saaduista luvuista pienimmän ja suurimman.
tulot = []
while True:
 luku = input("Anna luku: ")
 if luku == "":
    break
 luku1 = int(luku)
 tulot.append(luku1)

print("pienin luku on: ", min(tulot))
print("Suurin luku on: ", max(tulot))

#Agrin_Sadon
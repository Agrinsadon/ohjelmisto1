#massojen kg ja g

leiviskat = float(input("Anna leiviskat: "))
naulat = float(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))

tulo1 = (leiviskat * 20 * 32 * 13.3)
tulo2 = (naulat * 32 * 13.3)
tulo3 = (luodit * 13.3)

tulo1 = float(tulo1)
tulo2 = float(tulo2)
tulo3 = float(tulo3)

kilo = float(tulo1 + tulo2 + tulo3) / 1000
gram = float(tulo1 + tulo2 + tulo3)
kilot = int(kilo // 1)
grammat = round((kilo % 1) * 1000, 2)

print(f"Annettujen lukumaarijen massa on {kilot: .0f} kilogrammaa ja {grammat: } grammaa")
#pituus = float(input("Kuinka pitkä olet?"))

#if 1.5 <= pituus <=2.0:
    #print("Olet normaali pituinen.")

#if pituus >= 1.5 and pituus <= 2.0:
    #print("Olet normaalipituinen")

#if pituus <1.5 or pituus > 2.0:
    #print("Et ole normaalimittainen")

#mjono1 = input("anna eläinlaji: ")
#mjono2 = input("anna toinen eläinlaji: ")
#if mjono1 == mjono2:
    #print("annoit saman eläinlajin")

#muuttuja1 = 5
# int-tyyppinen, koska sinne sijoitettiin kokonaisluku 5

#muuttuja2 = 1.49
# float/double-tyyppinen, koska sinne sijoitettiin desimaaliluku

#muuttuja3 = "Churro"
#str-tyyppinen, koska sinne sijoitettiin merkkijono

#muuttuja4 = input("Kirjota numero ")
# String-tyyppinen, jos halutaan vertailla suuruutta tai laskea, pitää muuttaa int tai float

#Merkintä	Vertailuoperaattori
#>	        suurempi kuin
#<	        pienempi kuin
#>=	        suurempi tai yhtäsuuri kuin
#<=	        pienempi tai yhtäsuuri kuin
#==	        yhtä suuri kuin
#!=	        eri suuri kuin

#Ei kaadu koska ika testataan ennen kuin paino ja jos ika ei ole yli 15 niin painoa ei ikinä päädytä vertaamaan
"""ika = int(input("Anna ikäsi: "))
if ika >= 15 and ika < 18:
    paino = float(input("anna painosi: "))
if ika >= 18 or (ika >= 15 and paino >= 55):
    print("Lääkkeen käyttö sallittu")
else:
    print("Lääkkeen käyttö ei ole sallittua")"""

#Ei yhtään kikkaa versio, uutena asiana kaksi sisäkkäistä if rakennetta
"""if ika >= 15 and ika <18:
    paino = float(input("Anna painosi: "))
if ika >= 18:
    print("lääkkeen käyttö sallittu")
if ika >= 15 and ika <18:
    if paino >= 55:
     print("lääkkeen käyttö sallitu")"""


"""ika = int(input("Anna ikäsi:"))
if ika >= 18:
    print("Lääkkeen käyttö sallittu")
elif ika < 15:
    print("Lääkkeen käyttö ei ole sallittu")
else:
    paino = float(input("Anna painosi:"))
    if paino >= 55:
        print("Lääkkeen käyttö sallittu")
    else:
        print("Lääkkeen käyttö ei sallittu")
print("Kiitos kun käytit lääkeohjelmaa churro")"""

#if = jos , if = elif , else = jotain muuta.

# While esim.1
"""hinta = int(input("Paljon maksaa? "))
maksettu = 1000
while maksettu < hinta:
    maksettu = maksettu +1
    print("maksetaan 1 euro ")
    print(f"maksetttava jäljellä + {hinta - maksettu} ")
print("Kahvi maksettu kokonaan")"""

# While esim. 2. Ohjelmavalikko
# while not (command == "lopeta" or command == "Lopeta
# command = command.lower() (voi kirjoittaa isolla tai pienellä)
"""command = ""
while command != "lopeta":
    command = input("Anna kometo: ").lower()
if command == "tulosta":
    print("tulostetaan")
    print("jotain")
elif command == "help":
    print("Komennot: tulosta, help, lopeta")
elif command == "lopeta":
    print("ohjelma sammutetaan")
else:
    print("en ymmärtänyt, yritä uudestaan, kirjoita help jos tarvitsette apua.")
    print ("ohjelma sammutettu")"""





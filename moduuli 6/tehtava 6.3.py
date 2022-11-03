#Kirjoita pääohjelma, joka kysyy gallonamäärän
#käyttäjältä ja muuntaa sen litroiksi.
#Muuntamista jatketaan siihen saakka,
#kunnes käyttäjä syöttää negatiivisen gallonamäärän.
gl = float(input("Anna bensiinin gallonmäärä: "))

def muuntaa(gl):
    litra = 2.043984
    litroina = gl * litra
    return litroina

while True:
    litra = muuntaa(gl)
    print(f"{gl} gallonia on {litra} litraa")
    gl = float(input("Anna galloina: "))
    if gl > litra:
        print("Annoit negatiivisen numeron!")
        break

#Agrin_Sadon
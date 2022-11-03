"""""
nimi = "J"
while nimi != "JEEEE":
    print(nimi)
    nimi = nimi + "E"

luku = 1
while luku < 10:
    print(luku)
    luku = luku + 2

for a in range(5, 1, -1):
    print(f"Kierros: {a}")

num1 = 7
num2 = 3

def churro(c,s):
    piiri = (c + s) * 2
    return piiri
print(churro(num1,num2))

#TAI

def churro():
    piiri = (num1 + num2) * 2
    return piiri
print(churro())

#ja

def vertaa(juttu1,juttu2):
    if juttu1 > juttu2:
        return juttu1
    else:
        return juttu2
juttu1 = 4
juttu2 = 7
print(vertaa(juttu1,juttu2))

luvut = [12, 5, 21, 4, 8, 0, 11]

def parittomat(luvut):
    pariton = []
    for i in luvut:
        if i % 2 != 0:    # jos haluat parillisen se on if i % 2 == 0:
            pariton.append(i)
    return pariton
print("parittomat luvut:", parittomat(luvut))

#miten yhdistää mysql
#1  asennetaan mysql ja import kirjasto esim. mysql.connector
#2 yhdeyden luominen = hostin , port , database , user , password ja autocommit = True
#3 sql lauseen luominen = Select from where
#4 kursorin tekeminen = yhteys.cursor(), kursori.execute(sql) ja tulos = kursori.fetchall()
#5 käsitellään sql tulos esim for rivi in tulos: print(rivi)
"
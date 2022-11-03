import mysql.connector

yhteys = mysql.connector.connect(
         host="127.0.0.1",
         port=3306,
         database="lentopelih",
         user= "root",
         password= "kirkuk123",
         autocommit=True
         )

maa = input("Maakoodi: ")
sql = "SELECT type, count(*) FROM airport WHERE iso_country = '"+ maa +"' Group by type"
kursori = yhteys.cursor()
kursori.execute(sql)
tulos = kursori.fetchall()
for rivi in tulos:
    print(f"{rivi[0]}, {rivi[1]}")

#Agrin_Sadon
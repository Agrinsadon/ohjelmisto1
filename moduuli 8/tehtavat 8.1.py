import mysql.connector

yhteys = mysql.connector.connect(
         host="127.0.0.1",
         port=3306,
         database="flight_game",
         user= "root",
         password= "Sadon19999",
         autocommit=True
         )

icao = input("Anna lentokentän ICAO-koodi: ")
sql = "SELECT name, municipality FROM airport WHERE ident = '"+ icao +"'"
kursori = yhteys.cursor()
kursori.execute(sql)
tulos = kursori.fetchall()
for rivi in tulos:
    print(f"{rivi[0]}, {rivi[1]}")

maa = input("Maakoodi: ")
sql = "SELECT type, count(*) FROM airport WHERE iso_country = '"+ maa +"' Group by type"
kursori = yhteys.cursor()
kursori.execute(sql)
tulos = kursori.fetchall()
for rivi in tulos:
    print(f"{rivi[0]}, {rivi[1]}")



import mysql.connector
yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port= 3306,
    database='flight_game',
    user='testaaja',
    password='j33s',
    autocommit=True,
)
#Valmiina: Lentokentän valitseminen,
#Tarvitsee vielä mukaillun tietokannan ja loopin lentokentän määrien valitsemiseksi.
#Tarvitsee myös tiedon reitin pituudesta, mutta näiden pitäisi olla helppoja koodata.
#Pyrin hoitamaan loput tästä valmiiksi ennen ensi viikkoa.
import random


def lentokentan_valitsin():
    numero = random.randint(1, 100000)
    sql = f"select airport.name, country.name from airport inner join country on airport.iso_country = country.iso_country and airport.id = {numero} and airport.type = 'large_airport';"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    while kursori.rowcount == 0:
        numero = random.randint(1, 100000)
        sql = f"select airport.name, country.name from airport inner join country on airport.iso_country = country.iso_country and airport.id = {numero} and airport.type = 'large_airport';"
        kursori = yhteys.cursor()
        kursori.execute(sql)
        tulos = kursori.fetchall()
    else:
        for rivi in tulos:
            print(f"The airport is {rivi[0]} in the country of {rivi[1]}")
    return
lentokentan_valitsin()


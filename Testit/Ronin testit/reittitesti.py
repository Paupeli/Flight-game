import mysql.connector
yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port= 3306,
    database='flight_game',
    user='testaaja',
    password='j33s',
    autocommit=True,
)

import random
route_length = int(input("Give the desired length of the route in numbers: "))
country_list = []
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
            country_list.append(rivi[1])
    return
while route_length > len(country_list):
    lentokentan_valitsin()
else: print(country_list)


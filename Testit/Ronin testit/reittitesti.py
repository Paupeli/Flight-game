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


def lentokentan_valitsin():
    sql = f"select name from airport where id={random.randint(1,10000)};"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    while kursori.rowcount == 0:
        kursori = yhteys.cursor()
        kursori.execute(sql)
        tulos = kursori.fetchall()
    else:
        for rivi in tulos:
            print(rivi[0])
    return
lentokentan_valitsin()


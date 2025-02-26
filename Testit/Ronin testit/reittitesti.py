import mysql.connector
yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port= 3306,
    database='flight_game',
    user='testaaja',
    password='j33s',
    autocommit=True,
)
#Valmiina: Lentokentän valitseminen
#Tarvitsee vielä mukaillun tietokannan ja loopin lentokentän määrien valitsemiseksi.
#Tarvitsee myös tiedon reitin pituudesta, mutta näiden pitäisi olla helppoja koodata.
#Pyrin hoitamaan loput tästä valmiiksi ennen ensi viikkoa.
import random


def lentokentan_valitsin():
    sql = f"select name, iso_country from airport where id={random.randint(1,10000)};"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    while kursori.rowcount == 0:
        kursori = yhteys.cursor()
        kursori.execute(sql)
        tulos = kursori.fetchall()
    else:
        for rivi in tulos:
            print(rivi[0], rivi[1])
    return
lentokentan_valitsin()


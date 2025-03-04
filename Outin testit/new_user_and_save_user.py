# Tämän ohjelman tarkoituksena on
# 1) antaa käyttäjälle mahdollisuus valita uusi tai olemassa oleva käyttäjä
# 2) luoda uusi käyttäjä
# 3) tallentaa uusi käyttäjä tai hakea vanhan käyttäjän tiedot
# 4) luoda mekanismi tallentamaan käyttäjän pelidata / highscore systeemiin > scoreboardin printtaus

# Mietinnän alla:
# "Lukitut käyttäjät", joita ei voida valita mutta joilla on läsnäolo scoreboardissa? Kilpailun olon luomiseksi :)
# Peliohjeet?
# ****

# ! Oletetaan, että tässä kohtaa on tietokantayhteys


# 2) MAIN MENU, SCOREBOARD (**OUTI**) JA UUDEN PELIN LUONTI (**RONI**)
    # > Start a new game
        # >> Valitse hahmo (huom. game.location pitää päivittää)
        # >> Luo uusi hahmo
            # >>> Valitse, kuinka pitkä peli (**RONI**)
                # Tässä kohtaa "tallennetaan" arvotut Euroopan maat ja kentät alkavaa peliä varten ! (Ronin koodi)
    # > Check scoreboard
    # > Instructions
    # > Close game


import mysql.connector
import urwid

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user= 'root',
         password='MetroHylje334',
         autocommit=True
         collation='utf8mb3_general_ci'


def main_menu():
    menu = ['New Game', 'Scoreboard', 'Instructions', 'Quit Game']

    print("*** Main Menu ***")


def start_new_game():
    selection = input("Time to go Across Europe!\n-------------------\nDo you want to play with an existing user?").lower()
    if selection == "yes":
        all_users = all_users_fetch()
        user_select = input("Which user would you like to choose?")
        #SELVITÄ MITEN TÄSSÄ TALLENTUU ?
        #RESET LOCATION !!! VAI ei?

def all_users_fetch ():
    sql = "select screen_name from game"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    users = kursori.fetchall()
    print("Excisting users:")
    for user in users:
        print(user)
    return users

def new_user():
    kursori = yhteys.cursor()
    screen_name = input("Type your screen name: ")
    sql = "insert into game (screen_name) values (%s)"
    kursori.execute(sql)

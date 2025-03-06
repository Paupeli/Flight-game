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
    user='root',
    password='MetroHylje334',
    autocommit=True,
    collation='utf8mb3_general_ci'

)
#def main_menu(menu_selection):
 #   body = [urwid.Text("Across Europe\nMain Menu"), urwid.Divider()]
  #  for option in menu_selection:
   #     button = urwid.Button(option)
    #    urwid.connect_signal(button, "click", main_menu_options, user_args=(option))  #
     #   body.append(urwid.AttrMap(button, None, focus_map="reversed"))
    # return urwid.ListBox(urwid.SimpleFocusListWalker(body))

def main_menu(menu_selection):
    print(menu_selection)
    option = input("Please choose an opition: ")
    return option

def main_menu_options(option):
    if option == "New Game":
        new_game()
    elif option == "Scoreboard":
        scoreboard()
    elif option == "Instructions":
        instructions()
    elif option == "Quit Game":
        quit(button)

def new_game():
    # options = ['Old user', 'New user']
    user = ""
    option = input("Do you want to play as an old user or create a new user?")
    if option == "Old user":
        user = old_user()
    elif option == "New user":
        user = new_user()
    return user

    #def new_game_menu(options):
     #   body = [urwid.Text("Please choose:"), urwid.Divider()]
      #  for option in options:
       ##     button = urwid.Button(option)
         #   urwid.connect_signal(button, "click", main_menu_options, user_args=(option))
          #  body.append(urwid.AttrMap(button, None, focus_map="reversed"))
        #return urwid.ListBox(urwid.SimpleFocusListWalker(body))

   # def new_game_menu_choice(button, option):
    #    if option == "Old user":
     #       old_user()
      #  elif option == "New user":
       #     new_user()
        #raise urwid.ExitMainLoop()

def old_user():
    def all_users_fetch():
        sql = "'select screen_name from game'"
        kursori = yhteys.cursor()
        kursori.execute(sql)
        users = kursori.fetchall()
        print("Excisting users:")
        for user in users:
            print(user)
        return users
    users = all_users_fetch()
    print(f"Excisting users: {users}")
    user = input("Which user would you like to choose? ")
    return user                                                             #!!! Tähän tallennusmekanismi !!! > score, high_score

def new_user():
    user = input("What is your username? ")
    sql = (f"INSERT INTO game (screen_name) VALUES ('{user})'")
        # sql = (f"INSERT INTO game (screen_name, current_score, high_score) VALUES ({user_name}, 0, 0)")
    kursori = yhteys.cursor()
    kursori.execute(sql)
    print("User created.\nProceeding to the game...\n----------")
    return user

#def start_new_game():
 #   selection = input("Time to go Across Europe!\n-------------------\nDo you want to play with an existing user?").lower()
  #  if selection == "yes":
   #     all_users = all_users_fetch()
    #    user_select = input("Which user would you like to choose?")
     #   #SELVITÄ MITEN TÄSSÄ TALLENTUU ?
      #  #RESET LOCATION !!! VAI ei?

def scoreboard():
    pass

def quit_game(button):
    pass

def instructions():
    pass

menu_selection = ['New Game', 'Scoreboard', 'Instructions', 'Quit Game']

run = main_menu(menu_selection)
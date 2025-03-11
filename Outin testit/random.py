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
import pyfiglet

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='keltanokat',
    password='lentopeli',
    autocommit=True,
    collation='utf8mb3_general_ci'

)

def continue_game():
    return
def scoreboard():
    sql = f"select screen_name, high_score from game order by high_score desc limit 5;"
    cursor = yhteys.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    print (f"\n______________________________\n{'USER':<15} | {'HIGH SCORE':<10} |\n_______________________________")
    for row in result:
        screen_name = row[0] if row[0] is not None else "N/A"
        high_score = row[1] if row[1] is not None else "N/A"
        print(f"{screen_name:<15} | {high_score:<10} |\n______________________________")
    return

def quit_game():
    print("-----------\nQuitting game...\n____________")
    exit()


def instructions():
    print(
        "___________\n\n\nWelcome to Across Europe!\nThe rules are simple:\n\n 1) You start in Helsinki Vantaa Airport\n\n 2) You get a clue where you should go next"
        "\n  - Right guess: +100 points\n  - Wrong guess: -50 points\n  - Guess wrong 3 times: game over!\n\n 3) Once you get to the correct airport, you get a task\n  - Complete the task and get +50 points!\n"
        "  - Fail the task, shame on you, -25 points \n\n 4) Finish the game by arriving to the final airport! :)")
    return

def quit_game():
    print("-----------\nQuitting game...\n____________")
    exit()


def pause_menu():
    global pause_option
    while True:
        pause_menu_text = pyfiglet.figlet_format("Game Paused", font="slant")
        print(f"\n\n{pause_menu_text}")
        print(f"\nOptions:\n>Continue\n>Check scoreboard\n>Rules\n>Main Menu\n>Quit\n")
        pause_option = input("\nWhat would you like to do? >").lower()
        if pause_option == "continue":
            break
        elif pause_option == "check scoreboard":
            scoreboard()
        elif pause_option == "rules":
            instructions()
        elif pause_option == "main Menu":
            main_menu(menu_selection)   #Tässä tarkistus, sekottaako pääkoodin? Tai, miten pääkoodin saa rullaamaan tän kanssa
        elif pause_option == "quit":
            quit_game_text = pyfiglet.figlet_format("quitting game...", font="slant")
            quit()
    return

flying_text = pyfiglet.figlet_format("Flying to destination...", font="slant")
print(flying_text)
print(r'''
                                                          _
                                            -=\`\
                                        |\ ____\_\__
                                      -=\c`""""""" "`)
                                         `~~~~~/ /~~`
                                           -==/ /
                                             '-'

                                             _  _
                                            ( `   )_
                                           (    )    `)
                                         (_   (_ .  _) _)
                                                                        _
                                                                       (  )
                                        _ .                         ( `  ) . )
                                      (  _ )_                      (_, _(  ,_)_)
                                    (_  _(_ ,)
                                     ''')



# !!!! TÄSSÄ KOHTAA "USER" KÄYTTÖÖN JA PELI STARTTAA HELSINGISTÄ
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

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='MetroHylje334',
    autocommit=True,
    collation='utf8mb3_general_ci'

)

def main_menu(menu_selection):
    print("\n-------------------------\n")
    main_menu_text = """▐▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▌
▐ ███╗   ███╗ █████╗ ██╗███╗   ██╗    ███╗   ███╗███████╗███╗   ██╗██╗   ██╗ ▌
▐ ████╗ ████║██╔══██╗██║████╗  ██║    ████╗ ████║██╔════╝████╗  ██║██║   ██║ ▌
▐ ██╔████╔██║███████║██║██╔██╗ ██║    ██╔████╔██║█████╗  ██╔██╗ ██║██║   ██║ ▌
▐ ██║╚██╔╝██║██╔══██║██║██║╚██╗██║    ██║╚██╔╝██║██╔══╝  ██║╚██╗██║██║   ██║ ▌
▐ ██║ ╚═╝ ██║██║  ██║██║██║ ╚████║    ██║ ╚═╝ ██║███████╗██║ ╚████║╚██████╔╝ ▌
▐ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝    ╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝  ▌
▐▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▌
                                                                          """
    print(main_menu_text)
    print("-------------------------\n")
    print(f"\n{(menu_selection)}\n") #Muotoillaan nää vielä listaksi?
    option = input(">>> Write down your selection: ").lower()
    return option


def main_menu_options(option):
    global user
    while True:
        if option == "new game":
            user = new_game()
            break
        elif option == "scoreboard":
            scoreboard()
            main_menu(menu_selection)
        elif option == "instructions":
            instructions()
            main_menu(menu_selection)
        elif option == "quit game":
            quit()
    return user


def new_game():
        # options = ['Old user', 'New user']
    global user
    option = input("Do you want to play as an old user or create a new user? ").lower()
    if option == "old user":
        user = old_user()
    elif option == "new user":
        user = new_user()
    return user

def old_user():
    def all_users_fetch():
        sql = "select screen_name from game;"
        kursori = yhteys.cursor()
        kursori.execute(sql)
        users = kursori.fetchall()
        print("\nExcisting users:")
        for user in users:
            print(user)
        return
    users = all_users_fetch()

    while True:
        user = input("Which user would you like to choose? ")
        sql1 = f"select screen_name from game where screen_name = '{user}';"
        cursor = yhteys.cursor()
        cursor.execute(sql1)
        result = cursor.fetchall()
        if not result:
            print("Please select an existing user.")
            users = all_users_fetch()
        else:
            break

    return user  # !!! Tähän tallennusmekanismi !!! > score, high_score

def new_user():                                                                                        #Pycharm väittää että on unreachable, not true
    while True:
        user = input("What is your username? ")
        sql1 = f"select screen_name from game where screen_name = '{user}';"
        cursor = yhteys.cursor()
        cursor.execute(sql1)
        result = cursor.fetchall()
        if cursor.rowcount == 0:
            cursor.execute("SELECT COALESCE(MAX(id), 0) + 1 FROM game;")
            next_id = cursor.fetchone()[0]

            sql = f"INSERT INTO game (id, screen_name, location) VALUES ({next_id}, '{user}');" #({next_id}, '{user}', EFHK) !!!!!!
                #entä pisteet?
            kursori = yhteys.cursor()
            kursori.execute(sql)
            print("User created.\nProceeding to the game...\n----------")
            break
        else:
            print("User already exists. Please type in a new username.")
                # tähän vois jotenkin keksiä, voisko palata tonne hahmovalintaan?
    return user


def scoreboard():
    sql = f"select screen_name, co2_consumed from game order by co2_consumed desc limit 5;"   #NYT CO2 CONSUMED !!!!! VAIHDA "SCORE"
    cursor = yhteys.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    print (f"\n______________________________\n{'USER':<15} | {'HIGHSCORE':<10} |\n_______________________________")
    for row in result:
        screen_name = row[0] if row[0] is not None else "N/A"
        score = row[1] if row[1] is not None else "N/A"
        print(f"{screen_name:<15} | {score:<10} |\n______________________________")
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


menu_selection = ['New Game', 'Scoreboard', 'Instructions', 'Quit Game']

option = main_menu(menu_selection)
user = main_menu_options(option)

# !!!! TÄSSÄ KOHTAA "USER" KÄYTTÖÖN JA PELI STARTTAA HELSINGISTÄ
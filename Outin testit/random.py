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
    print"\n-------------------------\n\nWELCOME TO MAIN MENU\n\n-------------------------"
    print(f"Options:\n{(menu_selection)}")
    option = input("\nPlease choose an opition: ")
    return option


def main_menu_options(option):
    global user
    while True:
        if option == "New Game":
            user = new_game()
            break
        elif option == "Scoreboard":
            scoreboard()
            main_menu(menu_selection)
        elif option == "Instructions":
            instructions()
            main_menu(menu_selection)
        elif option == "Quit Game":
            quit()
    return user


def new_game():
        # options = ['Old user', 'New user']
    global user
    option = input("Do you want to play as an old user or create a new user?")
    if option == "Old user":
        user = old_user()
    elif option == "New user":
        user = new_user()
    return user

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

    while True:
        user = input("Which user would you like to choose? ")

        sql1 = f"select screen_name from game where screen_name = '{user};'"
        cursor = yhteys.cursor()
        cursor.execute(sql1)
        result = cursor.fetchall()

        if cursor.rowcount == 0:
            print("Please select an existing user.")
        else:
            break

    return user  # !!! Tähän tallennusmekanismi !!! > score, high_score

def new_user():
    while True:
        user = input("What is your username? ")
        sql1 = f"select screen_name from game where screen_name = '{user}';"
        cursor = yhteys.cursor()
        cursor.execute(sql1)
        result = cursor.fetchall()
        if cursor.rowcount == 0:
            cursor.execute("SELECT COALESCE(MAX(id), 0) + 1 FROM game;")
            next_id = cursor.fetchone()[0]

            sql = f"INSERT INTO game (id, screen_name) VALUES ({next_id}, '{user}');"
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
    for row in result:
        print(f"Name: {row[0]}points{row[1]}")
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

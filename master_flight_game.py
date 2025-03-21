#
#
#
#
# !!!!! MUISTA TEHDÄ OMA BRANCH !!!!!!!! ENNEN KUIN MUOKKAAT !!!!! (ohjeet discordissa #repo)


#
# Pushataan tänne vain valmista (tai melkein valmista) koodia, testata voi vapaasti
# Aluksi saattaa olla ettei mikään vielä toimi, ok tehtä "raakile"

# Muista kommentoida koodiasi !!!


# PELIN RAKENNE (jokainen rivi on suurin piirtein "koodaustehtävä")



# 0 A ) SQL-connector (yhteinen salasana)
import mysql.connector
import ast

from just_playback import Playback
import defer
playback = Playback()
playback.load_file('musa.mp3')



playback.play()
from defer import return_value


#pyfiglet, creates slanted text etc
import pyfiglet                             #Muista asentaa python packages, uusin versio

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port= 3306,
    database='flight_game',
    user='keltanokat',
    password='lentopeli',
    autocommit=True,
    collation='utf8mb3_general_ci'

)
# 0 B ) IMPORTIT TÄHÄN (import.random, jne)
import random
# 0 C ) FUNKTIOT / DEF TAITAA TULLA TÄNNE AINAKIN LOPUKSI
country_list = []
airport_list = []
wrong_country_list = []
done_country_list = []
cluelist = []
count = 0
total_points = 0
wrong_answers = 0
points = 0

# STARTING SCREEN
def start_screen():
    startscreen_text = pyfiglet.figlet_format("Journey Across Europe!", font = "slant"  )
    print(startscreen_text)
    print(r'''
                ______
                _\ _~-\___
        =  = ==(____AA____D
                    \_____\___________________,-~~~~~~~`-.._
                    /     o O o o o o O O o o o o o o O o  |\_
                    `~-.__        ___..----..                  )
                          `---~~\___________/------------`````
                          =  ===(_________D
                          ''')
    start_press = input("Press ENTER to start")
    return

# GAME OVER SCREEN
def game_over():
    gameover_screen_text = pyfiglet.figlet_format("Game Over!", font="slant")
    print(gameover_screen_text)
    print(r'''
                     uuuuuuu
                 uu$$$$$$$$$$$uu
              uu$$$$$$$$$$$$$$$$$uu
             u$$$$$$$$$$$$$$$$$$$$$u
            u$$$$$$$$$$$$$$$$$$$$$$$u
           u$$$$$$$$$$$$$$$$$$$$$$$$$u
           u$$$$$$$$$$$$$$$$$$$$$$$$$u
           u$$$$$$"   "$$$"   "$$$$$$u
           "$$$$"      u$u       $$$$"
            $$$u       u$u       u$$$
            $$$u      u$$$u      u$$$
             "$$$$uu$$$   $$$uu$$$$"
              "$$$$$$$"   "$$$$$$$"
                u$$$$$$$u$$$$$$$u
                 u$"$"$"$"$"$"$u
      uuu        $$u$ $ $ $ $u$$       uuu
     u$$$$        $$$$$u$u$u$$$       u$$$$
      $$$$$uu      "$$$$$$$$$"     uu$$$$$$
    u$$$$$$$$$$$uu    """""    uuuu$$$$$$$$$$
    $$$$"""$$$$$$$$$$uuu   uu$$$$$$$$$"""$$$"
     """      ""$$$$$$$$$$$uu ""$"""
               uuuu ""$$$$$$$$$$uuu
      u$$$uuu$$$$$$$$$uu ""$$$$$$$$$$$uuu$$$
      $$$$$$$$$$""""           ""$$$$$$$$$$$"
       "$$$$$"                      ""$$$$""
         $$$"                         $$$$"


                ''')
    over_press = input("Press ENTER to see scoreboard")
    return

#SCOREBOARD
def scoreboard():
    sql = f"select screen_name, high_score from game where high_score != 0 order by high_score desc limit 5;"
    cursor = yhteys.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    print (f"\n______________________________\n{'USER':<15} | {'HIGH SCORE':<10} |\n_______________________________")
    for row in result:
        screen_name = row[0] if row[0] is not None else "N/A"
        high_score = row[1] if row[1] is not None else "N/A"
        print(f"{screen_name:<15} | {high_score:<10} |\n______________________________")
    return

def route_creator():
    num = random.randint(1, 261)
    sql = f"select airport.name, country.name from airport inner join country on airport.iso_country = country.iso_country and airport.id = {num} order by rand();"
    cursor = yhteys.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    while cursor.rowcount == 0:
        num = random.randint(1, 261)
        sql = f"select airport.name, country.name from airport inner join country on airport.iso_country = country.iso_country and airport.id = {num} order by rand();"
        cursor = yhteys.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
    else:
        for row in result:
            if row[1] not in country_list:
                airport_list.append(row[0])
                country_list.append(row[1])
    return
def country_selector_for_questions():
    num = random.randint(1, 130)
    sql = f"select airport.name, country.name from airport inner join country on airport.iso_country = country.iso_country and airport.id = {num} order by rand();"
    cursor = yhteys.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    while cursor.rowcount == 0:
        num = random.randint(1, 130)
        sql = f"select airport.name, country.name from airport inner join country on airport.iso_country = country.iso_country and airport.id = {num} order by rand();"
        cursor = yhteys.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
    else:
        for row in result:
            if row[1] not in country_list and row[1] not in wrong_country_list:
                wrong_country_list.append(row[1])
    return

def question_sheet_creator():
    global points
    global wrong_answers
    global country3
    global count
    global route_length
    while True:
        num1 = random.randint(1, len(wrong_country_list))
        num2 = random.randint(1, len(wrong_country_list))
        num3 = random.randint(1, len(country_list))
        country1 = wrong_country_list[num1 - 1]
        country2 = wrong_country_list[num2 - 1]
        country3 = country_list[num3 - 1]
        selection_list = [country1, country2, country3]
        if country1 not in done_country_list and country2 not in done_country_list and country3 not in done_country_list:
            break
    while True:
        snum1 = random.randint(1, len(selection_list))
        snum2 = random.randint(1, len(selection_list))
        snum3 = random.randint(1, len(selection_list))
        if snum1 != snum2 and snum1 != snum3 and snum2 != snum3:
            break
    A = selection_list[snum1-1]
    B = selection_list[snum2-1]
    C = selection_list[snum3-1]
    sql = f"select clue from clues where iso_country in (select iso_country from country where name = '{country3}') ORDER BY RAND() LIMIT 1;"
    cursor = yhteys.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:
        clue = row [0]
    if cursor.rowcount == 0:
        sql = f"select clue from clues where iso_country in (select iso_country from country where name = '{country3}') ORDER BY RAND() LIMIT 1;"
        cursor = yhteys.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        for row in result:
            clue = row[0]
    print(clue)
    print(f"A: {A}, B: {B}, C: {C}")
    correct_answer_position = ''
    if country3 == A:
        correct_answer_position = 'A'
    elif country3 == B:
        correct_answer_position = 'B'
    elif country3 == C:
        correct_answer_position = 'C'
    country2_position = ''
    if country2 == A:
        country2_position = 'A'
    elif country2 == B:
        country2_position = 'B'
    elif country2 == C:
        country2_position = 'C'
    country1_position = ''
    if country1 == A:
        country1_position = 'A'
    elif country1 == B:
        country1_position = 'B'
    elif country1 == C:
        country1_position = 'C'
    answer = input("Give your answer as A, B or C ").upper()
    while True:
        if answer == correct_answer_position:
            print(f"\nCorrect, you got {100 * mult} points!")
            done_country_list.append(country3)
            points = points + (100 * mult)
            cluelist.clear()
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
            count = count + 1
            print(f"\nYour points: {points}")
            task_data = get_task_from_flight_game()
            if task_data:
                task = task_data["task"]
                option_a = task_data["option_a"]
                option_b = task_data["option_b"]
                option_c = task_data["option_c"]
                correct_answer = task_data["correct_answer"]
                if count != route_length:
                    correct_message = f"\nCorrect! You get {50*mult} points and a clue to your next destination."
                    wrong_message = f"\nWrong answer! You loose {25*mult} points. Here is a clue to your next destination."
                else:
                    correct_message = f"\nCorrect! You get {50*mult} points"
                    wrong_message = f"\nWrong answer! You loose {25*mult} points. Here is a clue to your next destination."
                ask_task(task, option_a, option_b, option_c, correct_answer)
            else:
                print("No task found in the database")
            break
        elif answer == country2_position or answer == country1_position:
            print(f"\nIncorrect, you lost {50 * mult} points!")
            done_country_list.append(country2)
            points = points - (50 * mult)
            wrong_answers += 1
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
            print(f"\nYour points: {points}\n")
            break
        else:
            print("\nYou didn't give your answer as A, B or C")
            answer = input("Give your answer as A, B or C ").upper()
    return points, wrong_answers, total_points, country3, count

# Lisätty points määrittäväksi, muuten pointsilla ei arvoa -outi
def score_board_insert(user, points):
    sql1 = f"select high_score from game where screen_name = 'user';"
    cursor = yhteys.cursor()
    cursor.execute(sql1)
    result = cursor.fetchone()
    if result is None or result[0] < points:
        sql2 = f"update game set high_score = {points} where screen_name = '{user}';"
        cursor = yhteys.cursor()
        cursor.execute(sql2)
        yhteys.commit()
        print(f"\nCurrent high score: {points}!")
        scoreboard()
        inp = input("Press ENTER to quit the game >>>")
    else:
        scoreboard()
        inp = input("Press ENTER to quit the game >>>")
    return

def length():
    global route_length
    while True:
        route_length = int(input("\nGive the desired length of the route in numbers (5, 10, 15): "))
        if route_length == 5 or route_length == 10 or route_length == 15:
            break
        else:
            print("Please enter a valid route length")
    global mult
    if route_length == 5:
        mult = 1.5
    elif route_length == 10:
        mult = 1
    elif route_length == 15:
        mult = 0.5
    return mult, route_length

def get_task_from_flight_game():
    try:
        cursor = yhteys.cursor(dictionary=True)
        sql = f"SELECT task, option_a, option_b, option_c, answer FROM tasks where iso_country in(select iso_country from country where name = '{country3}') ORDER BY RAND() LIMIT 1;"
        cursor.execute(sql)

        result = cursor.fetchone()

        if result:
            task = result['task']
            option_a = result['option_a']
            option_b = result['option_b']
            option_c = result['option_c']
            correct_answer = result['answer']

            return {
                "task": task,
                "option_a": option_a,
                "option_b": option_b,
                "option_c": option_c,
                "correct_answer": correct_answer
            }
        else:
            return None
    except mysql.connector.Error as err:
        print(f"Error: {err}")


def ask_task(task, option_a, option_b, option_c, correct_answer,):
    global points, mult
    print(f"\nTask from country: {country3}\n")
    print(task)

    print(f"{option_a}")
    print(f"{option_b}")
    print(f"{option_c}")

    user_answer = input("Enter your answer (a,b, or c): ").lower()

    while user_answer not in ['a', 'b', 'c'] or user_answer == '':
        print("\nYou didn't give your answer as a, b or c.")
        user_answer = input("Give your answer as a, b or c: ").lower()

    if user_answer == correct_answer.lower():
        points = points + (50*mult)
        print("\nCorrect")
        print(f"You got {50*mult} points! ")
        print(f"\nYour points: {points}")
        inp = input(f"\n-------------------------\nPress ENTER to continue // Press P to pause game >>\n\n").lower()
        if inp == "pause" or inp == "p":
            pause_menu()
        if count != route_length:
            print(f"\nHere is a clue to your next destination: \n")

    else:
        points = points-(25*mult)
        print("\nIncorrect")
        print(f"Oh no, you lost {25*mult} points! ")
        print(f"\nYour points: {points}")
        inp = input(f"\n-------------------------\nPress ENTER to continue // Press P to pause game >> \n\n").lower()
        if inp == "pause" or inp == "p":
            pause_menu()
        print(f"\nHere is a clue to your next destination: \n")

#PAUSE_MENU
def pause_menu():
    global pause_option
    while True:
        pause_menu_text = pyfiglet.figlet_format("Game Paused", font="slant") #emt, tän vois muotoilun vuoks laittaa vaan kerran eli ennen while-looppia? -outi
        print(f"\n\n{pause_menu_text}")
        print(f"\nOptions:\n>Continue\n>Check scoreboard\n>Rules\n>Quit\n")
        pause_option = input("\nWhat would you like to do? >").lower()
        if pause_option == "continue".lower():
            break
        elif pause_option == "check scoreboard" or pause_option == "scoreboard".lower():
            scoreboard()           #HUOM. PAUSEN AIKAINEN SCOREBOARD: Koodi on nyt kahdesti eli scoreboard() ja score_board_print() kts. ylhäällä - onko päivitetty?
        elif pause_option == "rules".lower():
            instructions()
        elif pause_option == "quit".lower():
            quit_game_text = pyfiglet.figlet_format("quitting game...", font="slant")
            print(quit_game_text)
            quit()
    return

def main_menu():

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
    global option
    global user

    while True:
        #Looppaa main menuun kunnes pelaaja haluaa alottaa uuden pelin
        print("-------------------------\n")
        print(f"\n>New Game\n>Scoreboard\n>Rules\n>Quit\n")
        option = input("Please select >").lower()
        if option == "new game" or option == "new":
            user = new_game()
            break
        elif option == "scoreboard":
            scoreboard()
        elif option == "rules":
            instructions()
        elif option == "quit":
            quit()
    return user


def new_game():
        # options = ['Old user', 'New user']
    global option
    print(f"\nPlease select:\n>Old user\n>New user")
    option = input("Please select >").lower()
    while True:
        if option == "old user" or option == "old":
            user = old_user()
            break
        if option == "new user" or option == "new":
            user = new_user()
            break
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
        user = input("\nWhich user would you like to choose? ")
        sql1 = f"select screen_name from game where screen_name = '{user}';"
        kursori = yhteys.cursor()
        kursori.execute(sql1)
        result = kursori.fetchall()
        if not result:
            print("Please select an existing user.")
            users = all_users_fetch()
        else:
            sql2 = f"update game set location = (select ident from airport where ident = 'EFHK') where screen_name = '{user}';"
            kursori = yhteys.cursor()
            kursori.execute(sql2)
            yhteys.commit()
            break

    return user  # !!! Tähän tallennusmekanismi !!! > score, high_score

def new_user():                                                                                        #Pycharm väittää että on unreachable, not true
    while True:
        user = input("What is your username? ")
        kursori = yhteys.cursor()
        sql_check = f"SELECT screen_name FROM game WHERE screen_name = '{user}';"
        kursori.execute(sql_check)
        result = kursori.fetchall()
        if not result:
            new_id = "SELECT COALESCE(MAX(id), 0) + 1 FROM game;"
            kursori = yhteys.cursor()
            kursori.execute(new_id)
            next_id = kursori.fetchone()[0]

            sql_add = f"INSERT INTO game (id, location,screen_name, score, high_score) VALUES ('{next_id}', 'EFHK', '{user}', 0, 0);"
            kursori = yhteys.cursor()
            kursori.execute(sql_add)
            print("User created.\nProceeding to the game...\n----------")
            break
        else:
            print("User already exists. Please type in a new username.")
    return user

def quit_game():
    quit_game_text = pyfiglet.figlet_format("quitting game...", font="slant")
    quit()

def instructions():
    print(
        "___________\n\n\nWelcome to Journey Across Europe!\nThe rules are simple:\n\n 1) You start in Helsinki Vantaa Airport\n\n 2) You get a clue where you should go next"
        "\n  - Right guess: +150, +100 or +50 points depending on the length of the route\n  - Wrong guess: -75, -50 or -25 points\n  - Guess wrong 3 times: game over!\n\n 3) Once you get to the correct airport, you get a task\n  - Complete the task and get +75, +50 or +25 points!\n"
        "  - Fail the task, shame on you, -37.5, -25 or -12.5 points \n\n 4) Finish the game by arriving to the final airport! :)")
    return

## NÄMÄ ALLA KÄYNNISTÄÄ FUNKTIOT YLLÄ

start_screen()

user = main_menu()

length()
              # Tässä kohtaa "tallennetaan" arvotut Euroopan maat ja kentät alkavaa peliä varten ! (Ronin koodi)
while route_length > len(country_list):
        route_creator()
while route_length * 1.5 > len(wrong_country_list):
    country_selector_for_questions()

print("\nWelcome to your starting point at Helsinki-Vantaa airport, traveler!\nYour amazing journey across Europe starts here~\nYou need to solve clues to get to your destination and do different tasks there.\nHere’s an envelope with a clue to your first destination: \n ")

while True:
    if wrong_answers >= 3:
        print("Too many wrong answers, game over")
        print(f"Total points: {points}")
        print (user)
        print (points)
        game_over()
        score_board_insert(user,points)             #Lisäsin tämän tänne, menee gameover näkymään -outi
        break
    elif count == route_length:
        print("You completed the game!")
        print(f"Total points: {points}")
        game_completed_text = pyfiglet.figlet_format("Congrats!", font="slant")
        print(game_completed_text)
        print('\nYou have arrived to your final destination! Well done!\n')
        score_board_insert(user, points)
        break
    else:
        question_sheet_creator()

exit() #vai quit?
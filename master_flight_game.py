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
from just_playback import Playback
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
    start_press = input("Press any key to start")
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
            print(f"Correct, you got {100 * mult} points!")
            done_country_list.append(country3)
            points = points + (100 * mult)
            cluelist.clear()
            print(f"Moving to {country3}")
            count = count + 1
            print(f"Your points: {points}")
            task_data = get_task_from_flight_game()
            if task_data:
                task = task_data["task"]
                option_a = task_data["option_a"]
                option_b = task_data["option_b"]
                option_c = task_data["option_c"]
                correct_answer = task_data["correct_answer"]
                if count != route_length:
                    correct_message = f"Correct! You get {50*mult} points and a clue to your next destination."
                    wrong_message = f"Wrong answer! You loose {25*mult} points. Here is a clue to your next destination."
                else:
                    correct_message = f"Correct! You get {50*mult} points"
                    wrong_message = f"Wrong answer! You loose {25*mult} points. Here is a clue to your next destination."



                ask_task(task, option_a, option_b, option_c, correct_answer)
            else:
                print("No task found in the database")
            break
            # printtaa siirtymän
            # Tarvii flying to destination artin
        elif answer == country2_position or answer == country1_position:
            print(f"Incorrect, you lost {50 * mult} points!")
            done_country_list.append(country2)
            points = points - (50 * mult)
            wrong_answers += 1
            print(f"Moving to {country2}")
            print(f"Your points: {points}")
            # printtaa siirtymän
            # Tarvii flying to destination artin
            break

        else:
            print("You didn't give your answer as A, B or C")
            answer = input("Give your answer as A, B or C ").upper()
    return points, wrong_answers, total_points, country3, count

def score_board_insert():
    global points
    global screen_name
    sql = f"update game set score = {points} where screen_name = '{user}';"
    cursor = yhteys.cursor()
    cursor.execute(sql)
    sql = f"select high_score from game where high_score in (select max(high_score) from game) order by high_score desc limit 1;"
    cursor = yhteys.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:
        if str(row[0]) < str(points):
            print("New High Score!")
    sql = f"select high_score from game where screen_name = '{user}' order by high_score desc limit 1;"
    cursor = yhteys.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:
        if str(row[0]) < str(points):
            sql = f"update game set high_score = {points} where screen_name = '{user}'"
            cursor = yhteys.cursor()
            cursor.execute(sql)
            print("New personal best!")
    return
def length():
    global route_length
    while True:
        route_length = int(input("Give the desired length of the route in numbers (5, 10, 15): "))
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
    print(f"Task from country: {country3}")
    print(task)

    print(f"{option_a}")
    print(f"{option_b}")
    print(f"{option_c}")

    user_answer = input("Enter your answer (a,b, or c): ").lower()

    if user_answer == correct_answer.lower():
        points = points + (50*mult)
        print("Correct")
        print(f"You got {50*mult} points! ")
        print(f"Your points: {points}")
        if count != route_length:
            print(f"Here is a clue to your next destination: ")

    elif user_answer not in  ['A', 'B' or 'C']:
        print("You didn't give your answer as A, B or C")
        answer = input("Give your answer as A, B or C ").upper()


    else:
        points = points-(25*mult)
        print("Incorrect")
        print(f"Oh no, you lost {25*mult} points! ")
        print(f"Your points: {points}")
        print(f"Here is a clue to your next destination: ")

# 1) ALOITUSRUUTU (Grafiikka, ääni?) (**JOHANNA**)

# 2) MAIN MENU, SCOREBOARD (**OUTI**) JA UUDEN PELIN LUONTI (**RONI**)
    # > Start a new game
        # >> Valitse hahmo (huom. game.location pitää päivittää helsingiksi)
        # >> Luo uusi hahmo
            # >>> Valitse, kuinka pitkä peli (**RONI**)


#HUOM! NÄMÄ OVAT FUNKTIOT, JOTKA KÄYNNISTYVÄT ALLA MAIN MENUN PÄÄKOODIN TOIMESTA (MERKITTY MISTÄ ALKAA)

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
    while True:                                     #Looppaa main menuun kunnes pelaaja haluaa alottaa uuden pelin
        option = main_menu(menu_selection)
        if option == "new game":
            user = new_game()
            break
        elif option == "scoreboard":
            scoreboard()
        elif option == "instructions":
            instructions()
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
        sql = f"select screen_name from game;"
        kursori = yhteys.cursor()
        kursori.execute(sql)
        users = kursori.fetchall()
        print("\nExcisting users:")
        for user in users:
            print(user)
        return                                  #Haetaan käyttäjät

    users = all_users_fetch()

    while True:                                 #Valitaan millä käyttäjällä aletaan pelata
        user = input("Which user would you like to choose? ")
        sql1 = f"select screen_name from game where screen_name = '{user}';"
        kursori = yhteys.cursor()
        kursori.execute(sql1)
        result = kursori.fetchall()
        if not result:
            print("Please select an existing user.")
            users = all_users_fetch()
        else:
            break
        #TÄHÄN TULEE VIELLÄ VANHAN KÄYTTÄJÄN DATAN NOLLAUS
    return user

def new_user():
    while True:
        user = input("What is your username? ")
        kursori = yhteys.cursor()
        sql_check = f"SELECT screen_name FROM game WHERE screen_name = '{user}';"
        kursori.execute(sql_check)
        result = kursori.fetchall()

        if not result:
            new_id = "SELECT COALESCE(MAX(id), 0) + 1 FROM game;"                                   #Tässä oma uus id pelaajille, joka on +1 edellisestä
            kursori = yhteys.cursor()
            kursori.execute(new_id)
            next_id = kursori.fetchone()[0]

            sql_add = f"INSERT INTO game (id, location,screen_name, score, high_score) VALUES ('{next_id}', 'EFHK', '{user}', 0, 0);"   #Aloituskenttä on HKI!
            kursori = yhteys.cursor()
            kursori.execute(sql_add)
            print("User created.\nProceeding to the game...\n----------")
            break
        else:
            print("User already exists. Please type in a new username.")
    return user


def scoreboard():
    sql = f"select screen_name, high_score from game order by high_score desc limit 5;"
    cursor = yhteys.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    print (f"\n______________________________\n{'USER':<15} | {'HIGH SCORE':<10} |\n_______________________________")
    for row in result:
        screen_name = row[0] if row[0] is not None else "N/A"
        high_score = row[1] if row[1] is not None else "N/A"
        print(f"{screen_name:<15} | {high_score:<10} |\n______________________________")                        #Printtaa feikki-taulukon, älä sorki jos et näe mitä teet
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

## NÄMÄ ALLA KÄYNNISTÄÄ FUNKTIOT YLLÄ

start_screen()

option = ""
user = main_menu_options(option)
# ^^^^^^^^^^^^^^^^^^^^

length()
                # Tässä kohtaa "tallennetaan" arvotut Euroopan maat ja kentät alkavaa peliä varten ! (Ronin koodi)
while route_length > len(country_list):
        route_creator()
while route_length * 1.5 > len(wrong_country_list):
    country_selector_for_questions()
    # > Check scoreboard
    # > Instructions
    # > Close game

# 3) PELIN PERUSKULKU: LIIKKUMINEN, KYSYMYKSET JA TEHTÄVÄT
    # Pelaaja aloittaa Helsingistä: Peli ilmoittaa sijainnin (grafiikka, ääni?)

    # Peli kysyy vihjekysymyksen (**PAULIINA**)
     #Huom. Pelin pitää hakea maatiedot 2-vaiheen tallennetusta maa-arvonnasta ja siirtyä seuraavaan maahan listasta vasta kun tulee oikea vastaus

            #VÄÄRÄ VASTAUS
                # -50 pistettä
                # Ilmoitus väärästä vastauksesta, siirtyminen vastauksen mukaiselle kentälle
                # Uusi vihjekysymys oikeasta kentästä / kaupungista
                # 3 kentän jälkeen peli loppuu >> Kohta 4, pelin päättyminen

            #OIKEA VASTAUS
                # +100 pistettä
                # Ilmoitus oikeasta vastauksesta, siirtyminen oikealle mukaiselle kentälle
print("Welcome to your starting point at Helsinki-Vantaa airport! Here is a clue to your first destination: ")
while True:
    if wrong_answers >= 3:
        print("Too many wrong answers, game over")
        print("Total points: " + str(points))
        score_board_insert()
        game_over()                             #Lisäsin tämän tänne, menee gameover näkymään
        print("Scoreboard: ")
        scoreboard()
        break
    elif count == route_length:
        print("You completed the game")
        print("Total points: " + str(points))
        score_board_insert()
        print("Scoreboard: ")
        scoreboard()
        #Voittoscreeni tähän? (Jopo)
        break
    question_sheet_creator()




    # Tehtävä kohteessa (**PAULIINA**)
        # Oikea vastaus +50, väärä vastaus -25
        # Ilmoitus käyttäjälle vastauksesta ja pisteistä
        # >>> Peli kysyy vihjekysymyksen uudesta kohteesta (edellinen osio)



    # Pisteet tallennetaan game.current_score

# 4) PELIN PÄÄTTYMINEN
    # 3 väärää vastausta > GAME OVER -ruutu

    # Saapuminen maaliin > FINISH LINE REACHED -ruutu

    # Jos game.current_score > game.high_score >>> pisteet tallennetaan game.high_score
        #Ilmoitus high scoresta?

    # Näytetään päivitetty scoreboard

    # Valinta:
#           > Main menu >> kohta 1, main menu
#           > Close game >> Lopetusruutu? > peli lopettaa toiminnan

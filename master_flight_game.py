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
#from defer import return_value

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port= 3306,
    database='flight_game',
    user='keltanokat',
    password='lentopeli',
    autocommit=True,
    #collation='utf8mb3_general_ci'

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


def route_creator():
    num = random.randint(1, 261)
    sql = f"select airport.name, country.name from airport inner join country on airport.iso_country = country.iso_country and airport.id = {num} and airport.type = 'large_airport';"
    cursor = yhteys.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    while cursor.rowcount == 0:
        num = random.randint(1, 261)
        sql = f"select airport.name, country.name from airport inner join country on airport.iso_country = country.iso_country and airport.id = {num} and airport.type = 'large_airport';"
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
    sql = f"select airport.name, country.name from airport inner join country on airport.iso_country = country.iso_country and airport.id = {num} and airport.type = 'large_airport';"
    cursor = yhteys.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    while cursor.rowcount == 0:
        num = random.randint(1, 130)
        sql = f"select airport.name, country.name from airport inner join country on airport.iso_country = country.iso_country and airport.id = {num} and airport.type = 'large_airport';"
        cursor = yhteys.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
    else:
        for row in result:
            if row[1] not in country_list and row[1] not in wrong_country_list:
                wrong_country_list.append(row[1])
    return
def question_sheet_creator():
    global total_points
    global wrong_answers
    global country3
    global count
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
    points = 0
    if answer == correct_answer_position:
        print(f"Correct, you got {100*mult} points!")
        done_country_list.append(country3)
        points += 100*mult
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

            correct_message = "Correct! You get 50 points and a clue to your next destination."
            wrong_message = "Wrong answer! You loose 25 points. Here is a clue to your next destination."

            ask_task(task, option_a, option_b, option_c, correct_answer, correct_message, wrong_message)
        else:
            print("No task found in the database")
        # sql koodi siiŕtymää varten
        # printtaa siirtymän
    elif answer == country2_position:
        print(f"Incorrect, you lost {50*mult} points!")
        done_country_list.append(country2)
        points -= (50*mult)
        wrong_answers += 1
        cluelist.clear()
        print(f"Moving to {country2}")
        print(f"Your points: {points}")
        # sql koodi siiŕtymää varten
        # printtaa siirtymän
    elif answer == country1_position:
        print(f"Incorrect, you lost {50*mult} points!")
        done_country_list.append(country1)
        points -= (50*mult)
        wrong_answers += 1
        cluelist.clear()
        print(f"Moving to {country1}")
        print(f"Your points: {points}")
        #sql koodi siiŕtymää varten
        #printtaa siirtymän

    total_points = total_points + points
    return points, wrong_answers, total_points, country3, count

def score_board_insert():
    global total_points
    global screen_name
    sql = f"select score from game where score in (select max(score) from game);"
    cursor = yhteys.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:
        if row[0] < total_points:
            print("New High Score!")
    sql = f"update game set points = {total_points} where user_name = '{screen_name}';"
    cursor = yhteys.cursor()
    cursor.execute(sql)
    return
def score_board_print():
    sql = f"select user_name, points from game;"
    cursor = yhteys.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:
        print(f"Name {row[0]}, points{row[1]}")
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
        points =+ (50*mult)
        print(f"You got {50*mult} points! ")
        print(f"Your points: {points}")
        print(f"Here is a clue to your next destination: ")
    else:
        points =- (25*mult)
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


def main_menu_options(option):                                                                  #TÄMÄ PALAUTTAA USERIN PELIN ALOITTAMISEKSI
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
    return user         # WHILE LOOP EI ETENE ENNEN KUN def new_game() PALAUTTAA user-arvon


def new_game():                                                                                #TÄMÄ ON VALIKKO UUDEN PELIN LUOMISEKSI
        # options = ['Old user', 'New user']
    global user
    option = input("Do you want to play as an old user or create a new user? ").lower()
    if option == "old user":
        user = old_user()
    elif option == "new user":
        user = new_user()
    return user              #PALAUTTAA user-arvon AIEMMALLE FUNKTIOLLE main_menu_options

def old_user(): #Muutettu funktioksi
    def all_users_fetch():
        sql = "select screen_name from game;"
        kursori = yhteys.cursor()
        kursori.execute(sql)
        users = kursori.fetchall()
        print("\nExcisting users:")
        for user in users:
            print(user)
        return
    users = all_users_fetch()                                                                   #Tämä on vähän höpö funktio, että voidaan listata olemassa olevat käyttävät old_user funktiossa

    while True:
        user = input("Which user would you like to choose? ")
        sql1 = f"select screen_name from game where screen_name = '{user}';"
        cursor = yhteys.cursor()
        cursor.execute(sql1)
        result = cursor.fetchall()
        if not result:                                                  #Tarkistaa että käyttäjä on olemassa, muute while-loop jatkuu
            print("Please select an existing user.")
            users = all_users_fetch()
        else:
            break
    # !!!! TÄHÄN VIELÄ SIJAINNIN NOLLAUS HELSINKIIN kun uusi tietokanta
    return user

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
    sql = f"select screen_name, co2_consumed from game order by co2_consumed desc limit 5;"                                 #NYT CO2 CONSUMED !!!!! VAIHDA "SCORE tms"
    cursor = yhteys.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    print (f"\n______________________________\n{'USER':<15} | {'HIGHSCORE':<10} |\n_______________________________")
    for row in result:
        screen_name = row[0] if row[0] is not None else "N/A"
        score = row[1] if row[1] is not None else "N/A"
        print(f"{screen_name:<15} | {score:<10} |\n______________________________")                    #TÄMÄ PRINTTAA TAULUKON pisteistä, älä sörki muotoilua jos et näe mitä teet :D
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

# TÄMÄ ALLA OLEVA ON **MAIN MENUN PÄÄKOODI**, JOKA KÄYNNISTÄÄ FUNKTIOT YLLÄ!!!

option = main_menu(menu_selection)
user = main_menu_options(option)

# ^^^^^^^^^^


length()
                # Tässä kohtaa "tallennetaan" arvotut Euroopan maat ja kentät alkavaa peliä varten ! (Ronin koodi)
while route_length > len(country_list):
        route_creator()
while route_length * 3 > len(wrong_country_list):
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

while True:
    if wrong_answers >= 3:
        print("Too many wrong answers, game over")
        print("Total points: " + str(total_points))
        score_board_insert()
        score_board_print()
        #Häviöscreeni tähän?
        break
    elif count == route_length:
        print("You completed the game")
        print("Total points: " + str(total_points))
        score_board_insert()
        score_board_print()
        #Voittoscreeni tähän?
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

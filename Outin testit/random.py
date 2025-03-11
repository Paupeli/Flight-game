
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
            inp = input("Press enter to continue or write pause or p to pause")
            if inp == "pause".lower() or inp == "p".lower():
                pause_menu()
            elif inp == '':
                break
            else:
                break
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
            print(f"Your points: {points}")
            inp = input("Press enter to continue or write pause or p to pause")
            if inp == "pause".lower() or inp == "p".lower():
                pause_menu()
            elif inp == '':
                break
            else:
                break
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
            # printtaa siirtymän
            # flying to destination screen
            break
        elif answer == country2_position or answer == country1_position:
            print(f"Incorrect, you lost {50 * mult} points!")
            done_country_list.append(country2)
            points = points - (50 * mult)
            wrong_answers += 1
            inp = input("Press enter to continue or write pause or p to pause")
            if inp == "pause".lower() or inp == "p".lower():
                pause_menu()
            elif inp == '':
                break
            else:
                break
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
            print(f"Your points: {points}")
            break
            # printtaa siirtymän

        else:
            print("You didn't give your answer as A, B or C")
            inp = input("Press enter to continue or write pause or p to pause")
            if inp == "pause".lower() or inp == "p".lower():
                pause_menu()
            elif inp == '':
                break
            else:
                break
            answer = input("Give your answer as A, B or C ").upper()
    return points, wrong_answers, total_points, country3, count

def score_board_insert(user, points):                                                                 # Lisätty points määrittäväksi, muuten pointsilla ei arvoa -outi
    global screen_name
    sql = f"update game set high_score = {points} where screen_name = '{user}';"
    cursor = yhteys.cursor()
    cursor.execute(sql)
    sql = f"select high_score from game where high_score in (select max(high_score) from game) order by high_score desc limit 1;"
    cursor = yhteys.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:
        if int(row[0]) < points:
            print("New High Score!")
    sql = f"select high_score from game where screen_name = '{user}' order by high_score desc limit 1;"
    cursor = yhteys.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:
        if int(row[0]) < points:
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
        inp = input("Press enter to continue or write pause or p to pause")
        if inp == "pause".lower() or inp == "p".lower():
            pause_menu()
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
        inp = input("Press enter to continue or write pause or p to pause")
        if inp == "pause".lower() or inp == "p".lower():
            pause_menu()
        print(f"Here is a clue to your next destination: ")

start_screen()

user = main_menu()      #tämä käynnistää hahmon valinnan yms (Outi)

length()             # Tässä kohtaa "tallennetaan" arvotut Euroopan maat ja kentät alkavaa peliä varten ! (Ronin koodi)

while route_length > len(country_list):
    route_creator()
while route_length * 1.5 > len(wrong_country_list):
    country_selector_for_questions()

print("Welcome to your starting point at Helsinki-Vantaa airport! Here is a clue to your first destination: ")

while True:
    if wrong_answers >= 3:                                                          #Ei vaikuta toimivan -outi
        print("Too many wrong answers, game over")
        print(f"Total points: {points}")
        score_board_insert(user,points)
        game_over()                                                                  #Lisäsin tämän tänne, menee gameover näkymään -outi
        print("Scoreboard: ")
        scoreboard()
        break
    elif count == route_length:
        print("You completed the game")
        print(f"Total points: {points}")
        score_board_insert(user, points)
        print("Scoreboard: ")
        game_completed_text = pyfiglet.figlet_format("Congrats!", font="slant")
        print(game_completed_text)
        print('\nYou have arrived to your final destination! Well done!\n')
        scoreboard()
        break
    else:
        inp = input("Press enter to continue or write pause or p to pause")
        if inp == "pause".lower() or inp == "p".lower():
            pause_menu()
        elif inp == '':
            question_sheet_creator()
        else:
            question_sheet_creator()


            ####

while route_length > len(country_list):
    route_creator()
while route_length * 1.5 > len(wrong_country_list):
    country_selector_for_questions()

print("Welcome to your starting point at Helsinki-Vantaa airport! Here is a clue to your first destination: ")

while True:
    if wrong_answers >= 3:                                                          #Ei vaikuta toimivan -outi
        print("Too many wrong answers, game over")
        print(f"Total points: {points}")
        score_board_insert(user,points)
        game_over()                                                                  #Lisäsin tämän tänne, menee gameover näkymään -outi
        print("Scoreboard: ")
        scoreboard()
        break
    elif count == route_length:
        print("You completed the game")
        print(f"Total points: {points}")
        score_board_insert(user, points)
        print("Scoreboard: ")
        game_completed_text = pyfiglet.figlet_format("Congrats!", font="slant")
        print(game_completed_text)
        print('\nYou have arrived to your final destination! Well done!\n')
        scoreboard()
        break
    else:
        inp = input("Press enter to continue or write pause or p to pause").lower()
        if inp == "pause" or inp == "p":
            pause_menu()
        elif inp == '':
            question_sheet_creator()
        else:
            question_sheet_creator()
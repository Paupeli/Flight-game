#the player is given a task and needs to choose the correct answer (a,b or c)
#if the player chooses correct answer, they get 50 points and a clue to the next destination
#if the player chooses incorrect answer, they loose 25 points but still get a clue to the next destination


#def task(iso_country, task, option_a, option_b, option_c, answer, correct_message, wrong_message):
    #print(task)
    #for option in options:
        #print(option)

    #user_answer = input("Enter your answer (a,b or c): ")

    #if user_answer.lower() == correct_answer:
        #print(correct_message)
    #else:
        #print(wrong_message)

#Albania
#ask_question(
    #"Say thank you in Albanian",
    #["a. Faleminderit", "b. Hvala", "c. Czesc"],
    #"a",
    #"Correct! You get 50 points and a clue to your next destination.",
    #"Wrong answer! You loose 25 points. Here is a clue to your next destination."
#)

#Armenia
#ask_question(
    #"Play a traditional Armenian string instrument",
    #["a. Sitar", "b. Balalaika", "c. Duduk"],
    #"c",
    #"Correct! You get 50 points and a clue to your next destination.",
    #"Wrong answer! You loose 25 points. Here is a clue to your next destination."
#)

##Austria
#ask_question(
    #"Bake a traditional Austrian dessert that consists of layers of sponge cake, jam and chocolate.",
    #["a. Apfelstrudel", "b. Sachertorte", "c. Linzer Torte"],
    #"b",
    #"Correct! You get 50 points and a clue to your next destination.",
    #"Wrong answer! You loose 25 points. Here is a clue to your next destination."
#)


import mysql.connector

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port= 3306,
    database='flight_game',
    user='pauliina',
    password='tikru123!',
    autocommit=True,
    collation='utf8mb3_general_ci'

)

def get_task_from_flight_game():
    try:
     cursor = yhteys.cursor(dictionary = True)

     cursor.execute("SELECT * FROM tasks ORDER BY RAND() LIMIT 1")

     result = cursor.fetchone()

     if result:
         iso_country = result['iso_country']
         task = result['task']
         option_a = result['option_a']
         option_b = result['option_b']
         option_c = result['option_c']
         correct_answer = result['answer']

         return {
             "iso_country": iso_country,
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
    finally:
        if cursor:
            cursor.close()
        if yhteys:
            yhteys.close()

def ask_task(iso_country, task, option_a, option_b, option_c, correct_answer, correct_message, wrong_message):
    print(f"Task from country: {iso_country}")
    print(task)

    print(f"{option_a}")
    print(f"{option_b}")
    print(f"{option_c}")

    user_answer = input("Enter your answer (a,b, or c): ").lower()

    if user_answer == correct_answer.lower():
        print(correct_message)
    else:
        print(wrong_message)

task_data = get_task_from_flight_game()

if task_data:
    iso_country = task_data["iso_country"]
    task = task_data["task"]
    option_a = task_data["option_a"]
    option_b = task_data["option_b"]
    option_c = task_data["option_c"]
    correct_answer = task_data["correct_answer"]

    correct_message = "Correct! You get 50 points and a clue to your next destination."
    wrong_message = "Wrong answer! You loose 25 points. Here is a clue to your next destination."

    ask_task(iso_country, task, option_a, option_b, option_c, correct_answer, correct_message, wrong_message)
else:
    print("No task found in the database")








       













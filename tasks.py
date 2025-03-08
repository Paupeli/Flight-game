#the player is given a task and needs to choose the correct answer (a,b or c)
#if the player chooses correct answer, they get 50 points and a clue to the next destination
#if the player chooses incorrect answer, they loose 25 points but still get a clue to the next destination


#def ask_question(question, options, correct_answer, correct_message, wrong_message):
    #print(question)
    #for option in options:
        #print(option)

    #user_answer = input("Enter your answer (a,b or c): ")

    #if user_answer.lower() == correct_answer:
        #print(correct_message)
    #lse:
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

#from defer import return_value

def get_task_by_country(iso_country):
    try:
       yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='keltanokat',
         password='lentopeli',
         autocommit=True,
         collation='utf8mb3_general_ci'

       )

       cursor = yhteys.cursor()

       query = """"
       
       SELECT task, option_a, option_b, option_c
       FROM tasks
       WHERE iso_country = %s
       """

       cursor.execute(query, (iso_country,))
       result = cursor.fetchone()

       if result:
           task, option_a, option_b, option_c = result
           print(f"Task: {task}")
           print(f"Options:\h{option_a}\n{option_b}\n{option_c}")
       else:
           print(f"No task found for country code: {iso_country}")

    except mysql.connector.Error as err:
       print(f"Error: {err}")
    finally:

         if yhteys.is_connected():
             cursor.close()
             yhteys.close()

iso_country = "AL"
get_task_by_country(iso_country)


       













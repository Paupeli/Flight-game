import mysql.connector

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port= 3306,
    database='flight_game',
    user='keltanokat',
    password='lentopeli',
    autocommit=True,
    collation='utf8mb3_general_ci'

)

def vanha_update():
    sql = f"update game set score = {points} where screen_name = '{user}';"
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

def score_board_insert(user, points):
    sql1 = f"select high_score from game where screen_name = '{user}';"
    cursor = yhteys.cursor()
    cursor.execute(sql1)
    score = cursor.fetchone()
    if int(score[0]) < points:
            sql2 = f"update game set high_score = '{points}'  where screen_name = '{user}';"
            cursor = yhteys.cursor()
            cursor.execute(sql2)
            yhteys.commit()
            print(f"New high score: {points}!")
    scoreboard()
    return

user = "Leena"
points = 700
score_board_insert(user, points)

inp = input(f"\n-------------------------\nPress ENTER to continue // Press P to pause game >>").lower()
if inp == "pause".lower() or inp == "p".lower():
    pause_menu()

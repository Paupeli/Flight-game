import mysql.connector

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port= 3306,
    database='flight_game',
    user='keltanokat',
    password='lentopeli',
    autocommit=True,
    #collation='utf8mb3_general_ci'

)
import random
route_length = int(input("Give the desired length of the route in numbers (max 20): "))
if route_length > 20:
    print("The desired length is too long")
    route_length = int(input("Give the desired length of the route in numbers (max 20): "))
country_list = []
airport_list = []
wrong_country_list = []
done_country_list = []
def route_creator():
    num = random.randint(1, 5000)
    sql = f"select airport.name, country.name from airport inner join country on airport.iso_country = country.iso_country and airport.id = {num} and airport.type = 'large_airport';"
    cursor = yhteys.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    while cursor.rowcount == 0:
        num = random.randint(1, 5000)
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
    num = random.randint(1, 5000)
    sql = f"select airport.name, country.name from airport inner join country on airport.iso_country = country.iso_country and airport.id = {num} and airport.type = 'large_airport';"
    cursor = yhteys.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    while cursor.rowcount == 0:
        num = random.randint(1, 5000)
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
    print(f"A: {A}, B: {B}, C: {C}")
    correct_answer_position = ''
    if country3 == A:
        correct_answer_position = 'A'
    elif country3 == B:
        correct_answer_position = 'B'
    elif country3 == C:
        correct_answer_position = 'C'
    answer = input("Give your answer as A, B or C ").upper()
    if answer == correct_answer_position:
        print("Correct!")
        done_country_list.append(country3)
    else:
        print("Incorrect!")
    return

while route_length > len(country_list):
    route_creator()
else: print(country_list)
print(airport_list)
while route_length * 3 > len(wrong_country_list):
    country_selector_for_questions()
else: print(wrong_country_list)
count = 0
while count < route_length:
    question_sheet_creator()
    count = count + 1




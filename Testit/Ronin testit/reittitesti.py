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
while route_length > len(country_list):
    route_creator()
else: print(country_list)
print(airport_list)

wrong_country_list = []
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
            if row[1] not in country_list:
                wrong_country_list.append(row[1])
    return
while route_length * 3 > len(wrong_country_list):
    country_selector_for_questions()
else: print(wrong_country_list)

def question_sheet_creator():
    num1 = random.randint(1, len(wrong_country_list))
    num2 = random.randint(1, len(wrong_country_list))
    num3 = random.randint(1, len(country_list))
    country1 = wrong_country_list[num1-1]
    country2 = wrong_country_list[num2-1]
    country3 = country_list[num3-1]
    selection_list = [country1, country2, country3]
    snum1 = random.randint(1, len(selection_list))
    snum2 = random.randint(1, len(selection_list))
    snum3 = random.randint(1, len(selection_list))
    if snum1 == snum2 or snum1 == snum3 or snum3 == snum2 :
        snum2 = random.randint(1, len(selection_list))
        snum3 = random.randint(1, len(selection_list))
    else:
        A = selection_list[snum1-1]
        B = selection_list[snum2-1]
        C = selection_list[snum3-1]
        print(f"A={A}, B={B}, C={C}")
    return
question_sheet_creator()

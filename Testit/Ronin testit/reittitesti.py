import mysql.connector
yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port= 3306,
    database='flight_game',
    user='testaaja',
    password='j33s',
    autocommit=True,
    #remember to add collation here if you are not on linux!
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
            while row[1] not in country_list:
                wrong_country_list.append(row[1])
            else:
                num = random.randint(1, 5000)
                sql = f"select airport.name, country.name from airport inner join country on airport.iso_country = country.iso_country and airport.id = {num} and airport.type = 'large_airport';"
                cursor = yhteys.cursor()
                cursor.execute(sql)
                result = cursor.fetchall()
    return
while route_length * 3 > len(wrong_country_list):
    country_selector_for_questions()
else: print(wrong_country_list)









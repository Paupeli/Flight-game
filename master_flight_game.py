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
count = 0
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
total_points = 0
wrong_answers = 0
def question_sheet_creator():
    global total_points
    global wrong_answers
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
        print("Correct!")
        done_country_list.append(country3)
        points += 100
    elif answer == country2_position:
        print("Incorrect!")
        done_country_list.append(country2)
        points -= 50
        wrong_answers += 1
    elif answer == country1_position:
        print("Incorrect!")
        done_country_list.append(country1)
        points -= 50
        wrong_answers += 1

    total_points = total_points + points
    return points, wrong_answers
# 1) ALOITUSRUUTU (Grafiikka, ääni?) (**JOHANNA**)

# 2) MAIN MENU, SCOREBOARD (**OUTI**) JA UUDEN PELIN LUONTI (**RONI**)
    # > Start a new game
        # >> Valitse hahmo (huom. game.location pitää päivittää helsingiksi)
        # >> Luo uusi hahmo
            # >>> Valitse, kuinka pitkä peli (**RONI**)
route_length = int(input("Give the desired length of the route in numbers (max 20): "))
if route_length > 20:
    print("The desired length is too long")
    route_length = int(input("Give the desired length of the route in numbers (max 20): "))
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

while count < route_length or wrong_answers < 3:
    question_sheet_creator()
    count = count + 1



    # Tehtävä kohteessa (**PAULIINA**)
        # Oikea vastaus +50, väärä vastaus -25
        # Ilmoitus käyttäjälle vastauksesta ja pisteistä
        # >>> Peli kysyy vihjekysymyksen uudesta kohteesta (edellinen osio)

    # Pisteet tallennetaan game.current_score

# 4) PELIN PÄÄTTYMINEN
    # 3 väärää vastausta > GAME OVER -ruutu
if wrong_answers == 3:
    print("Too many wrong answers. Game over!")
    print("Total points: " + str(total_points))
    # Saapuminen maaliin > FINISH LINE REACHED -ruutu
elif count == route_length:
    print("You win!")
    print("Total points: " + str(total_points))
    # Jos game.current_score > game.high_score >>> pisteet tallennetaan game.high_score
        #Ilmoitus high scoresta?
    # Näytetään päivitetty coreboard
    # Valinta:
#           > Main menu >> kohta 1, main menu
#           > Close game >> Lopetusruutu? > peli lopettaa toiminnan

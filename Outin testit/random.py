
import mysql.connector

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='keltanokat',
    password='lentopeli',
    autocommit=True,
    collation='utf8mb3_general_ci'

)

sql = f"select screen_name, high_score from game order by high_score desc limit 5;"
cursor = yhteys.cursor()
cursor.execute(sql)
result = cursor.fetchall()
print (f"\n______________________________\n{'USER':<15} | {'HIGH SCORE':<10} |\n_______________________________")
for row in result:
    screen_name = row[0] if row[0] is not None else "N/A"
    high_score = row[1] if row[1] is not None else "N/A"
    print(f"{screen_name:<15} | {high_score:<10} |\n______________________________")

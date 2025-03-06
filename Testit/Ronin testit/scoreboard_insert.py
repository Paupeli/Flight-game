
def score_board_insert():
    global total_points
    global screen_name
    sql = f"update game set points = {total_points} where user_name = '{screen_name}'"
    cursor = yhteys.cursor()
    cursor.execute(sql)
    return
def score_board_print():
    sql = f"select user_name, points from game"
    cursor = yhteys.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:
        print(f"Name {row[0]}, points{row[1]}")
    return

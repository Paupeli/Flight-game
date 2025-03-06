def user_name():
    global screen_name
    sql1 = f"select user_name from game where user_name = '{screen_name}'"
    cursor = yhteys.cursor()
    cursor.execute(sql1)
    result = cursor.fetchall()
    if cursor.rowcount == 0:
        sql2 = f"insert into game (user_name) values('{screen_name}')"
        cursor = yhteys.cursor()
        cursor.execute(sql2)
    return
def move_to_start():
    global screen_name
    #laita sql:n #:n kohdalle Helsinki-Vantaan ID!
    sql = f"update game set locations = (select id from airport where id = '#') where user_name = {screen_name}"
    cursor = yhteys.cursor()
    cursor.execute(sql)
    return
user_name()
move_to_start()
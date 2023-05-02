import psycopg2

conn = None
cur = None

try:
    conn = psycopg2.connect(
        host='localhost',
        database='Snake',
        user='postgres',
        password='LeeReyD'
    )
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS user_score")
    cur.execute("DROP TABLE IF EXISTS user1")

    user_table = """CREATE TABLE user1(
        user_id SERIAL PRIMARY KEY,
        username VARCHAR(50) NOT NULL UNIQUE  
    )"""
    cur.execute(user_table)

    insert_script = 'INSERT INTO user1 (user_id, username) VALUES (%s, %s)'
    insert_value = (1, "LeeD")
    cur.execute(insert_script, insert_value)

    user_score_table = """CREATE TABLE user_score(
        score_id SERIAL PRIMARY KEY,
        user_id INTEGER NOT NULL REFERENCES user1(user_id),
        score INTEGER NOT NULL
    )"""
    cur.execute(user_score_table)

    insert_script2 = 'INSERT INTO user_score (user_id, score) VALUES (%s, %s)'
    insert_value2 = (1, 12)
    cur.execute(insert_script2, insert_value2)

    username = input("Enter your username: ")
    cur.execute("SELECT * FROM user1 WHERE username = %s", (username,))
    user = cur.fetchone()
    if user is not None:
        cur.execute("SELECT * FROM user_score WHERE user_id = %s", (user[0],))
        score = cur.fetchone()[2]
    else:
        print(f"User {username} does not exist in the database.")

    if score is None:
        level = 1
    elif score < 10:
        level = 2
    elif score < 20:
        level = 3
    else:
        level = 4

    print(f"Welcome back, {username}! You are on level {level}.")




except (Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()
        print('Database connection closed.')

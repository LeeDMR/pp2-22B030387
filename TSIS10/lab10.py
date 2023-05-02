import psycopg2
import csv
conn = None
cur = None
try:
    conn = psycopg2.connect(
        host='localhost',
        database='PhoneBook',
        user='postgres',
        password='LeeReyD'
    )
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS PhoneBook")

    PhoneBookTable = """CREATE TABLE PhoneBook(
        id SERIAL PRIMARY KEY,
        first_name VARCHAR(50) NOT NULL,
        last_name VARCHAR(50) NOT NULL,
        phone_number VARCHAR(50) NOT NULL
    )"""
    cur.execute(PhoneBookTable)


    with open('phonebook.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            cur.execute(
                "INSERT INTO PhoneBook (id, first_name, last_name, phone_number) VALUES (%s, %s, %s, %s)",
                row)


    """""
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    phone_number = input("Enter phone number: ")
    cur.execute(
        "INSERT INTO phonebook (first_name, last_name, phone_number) VALUES (%s, %s, %s)",
        (first_name, last_name, phone_number))
    """""


    update = "UPDATE PhoneBook SET phone_number = 87773077305"
    cur.execute(update)


    cur.execute("SELECT * FROM PhoneBook")
    for record in cur.fetchall():
        print(record)
    """""
    cur.execute("SELECT * FROM PhoneBook WHERE first_name = %s", ('John',))
    rows = cur.fetchall()
    print(rows)
    """""

    delete = "DELETE from PhoneBook WHERE first_name = %s"
    cur.execute(delete, ('John',))

    cur.execute("SELECT * FROM PhoneBook")
    for record in cur.fetchall():
        print(record)

except (Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()
        print('Database connection closed.')


import psycopg


connection = psycopg.connect(
    host='localhost',
    port=5432,
    dbname='demo',
    user="app_user",
    password="password"
)

cursor = connection.cursor()

cursor.execute("SELECT current_database(), current_user;")
row = cursor.fetchone()
print(row)
print(row[0])
print(row[1])
print(type(row))

cursor.close()
# cursor.execute("select * from users")


connection.close()

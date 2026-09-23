import psycopg


connection = psycopg.connect(
    host='localhost',
    port=5432,
    dbname='demo',
    user="app_user",
    password="password"
)

print(connection)

connection.close()


print(connection.closed)

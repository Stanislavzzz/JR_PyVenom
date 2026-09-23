import psycopg


connection = psycopg.connect(
    host='localhost',
    port=5432,
    dbname='demo',
    user="app_user",
    password="password"
)

cursor = connection.cursor()

cursor.execute(
    """
    SELECT
        user_id,
        user_name,
        email,
        balance
    FROM training.users
    ORDER BY user_id
    LIMIT 5;
    """
)

rows = cursor.fetchall()

for row in rows:
    print(row[1], row[2])
# print(rows)


cursor.close()
connection.close()

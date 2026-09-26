import psycopg
from psycopg.rows import dict_row


email = "ivan@mail.ru"
user_id = 11

sql = """
    SELECT
        user_id,
        user_name,
        email,
        balance
    FROM training.users
    WHERE user_id = %s OR email = %s
    ORDER BY user_id;
"""

print(sql)

with psycopg.connect(
    host='localhost',
    port=5432,
    dbname='demo',
    user="app_user",
    password="password",
    row_factory=dict_row,
) as connection:

    with connection.cursor() as cursor:
        cursor.execute(
            sql,
            (user_id, email),
        )

        row = cursor.fetchall()

        print(row)
        print(type(row))

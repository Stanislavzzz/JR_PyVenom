import psycopg


email = "ivan@mail.ru"

sql = """
    SELECT
        user_id,
        user_name,
        email,
        balance
    FROM training.users
    WHERE email = '%s'
    ORDER BY user_id;
"""

print(sql)

with psycopg.connect(
    host='localhost',
    port=5432,
    dbname='demo',
    user="app_user",
    password="password"
) as connection:

    with connection.cursor() as cursor:
        cursor.execute(
            """
            SELECT user_id,
                   user_name,
                   email,
                   balance
            FROM training.users
            WHERE email = %s
            ORDER BY user_id;
            """,
            (email, ),
        )

        row = cursor.fetchall()

        print(row)

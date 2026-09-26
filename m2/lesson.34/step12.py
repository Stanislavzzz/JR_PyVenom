import psycopg


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

async with await psycopg.AsyncConnection.connect(
    host='localhost',
    port=5432,
    dbname='demo',
    user="app_user",
    password="password"
) as connection:

    async with connection.cursor() as cursor:
        await cursor.execute(
            sql,
            (user_id, email),
        )

        row = await cursor.fetchall()

        print(row)

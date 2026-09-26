import psycopg


params = {
    'email': "ivan@mail.ru",
    'user_id': 11,
}




sql = """
    SELECT
        user_id,
        user_name,
        email,
        balance
    FROM training.users
    WHERE user_id = %(user_id)s OR email = %(email)s
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
            sql,
            params,
        )

        row = cursor.fetchall()

        print(row)

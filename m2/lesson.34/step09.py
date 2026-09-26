import psycopg


params = {
    'email': "ivan@mail.ru",
    'user_id': 11,
}

table_name = 'training.users'


sql = """
    SELECT
        user_id,
        user_name,
        email,
        balance
    FROM %s;
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
            (table_name,),
        )

        row = cursor.fetchall()

        print(row)

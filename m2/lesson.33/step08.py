import psycopg


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
            SELECT
                user_id,
                user_name,
                email,
                balance
            FROM training.users
            ORDER BY user_id;
            """
        )

        row_1 = cursor.fetchall()

        print(cursor.rowcount)


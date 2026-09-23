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
            ORDER BY user_id
            LIMIT 5;
            """
        )

        row_1 = cursor.fetchmany(3)
        row_2 = cursor.fetchmany(3)
        row_3 = cursor.fetchmany(3)
        row_4 = cursor.fetchmany(3)

        print(row_1)
        print(row_2)
        print(row_3)
        print(row_4)

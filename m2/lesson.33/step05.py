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

        row_1 = cursor.fetchone()
        row_2 = cursor.fetchone()

        print(row_1[1], row_1[2])
        print(row_2[1], row_2[2])

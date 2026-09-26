import psycopg
from psycopg import sql


table_name = 'users'


sql_query = """
    SELECT
        user_id,
        user_name,
        email,
        balance
    FROM training.{};
"""

print(sql_query)



with psycopg.connect(
    host='localhost',
    port=5432,
    dbname='demo',
    user="app_user",
    password="password"
) as connection:

    with connection.cursor() as cursor:
        query = sql.SQL(
            sql_query
        ).format(
            sql.Identifier(table_name)
        )

        print(query)

        cursor.execute(query)
        #
        row = cursor.fetchall()
        #
        print(row)

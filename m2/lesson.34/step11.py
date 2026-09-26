import psycopg


# params = {
#     'user_name': 'New_Bob',
#     'email': "Bob@yandex.ru",
#     'age': 45,
#     "phone": "1234567"
# }
#
#
#
# sql = """
#     INSERT INTO training.users (
#         user_name,
#         email,
#         age,
#         contact_phone,
#     )
#     VALUES (
#         %(user_name)s,
#         %(email)s,
#         %(age)s,
#         %(phone)s
#     );
# """
#
# print(sql)
#
# with psycopg.connect(
#     host='localhost',
#     port=5432,
#     dbname='demo',
#     user="app_user",
#     password="password"
# ) as connection:
#
#     with connection.cursor() as cursor:
#         cursor.execute(
#             sql,
#             params,
#         )


user_name = 'New_Bob1'
email = "Bob1@yandex.ru"
age = 41
phone = "12345671"


user_name2 = 'New_Bob2'
email2 = "Bob2@yandex.ru"
age2 = 42
phone2 = "12345672"



sql1 = """
    INSERT INTO training.users (
        user_name,
        email,
        age,
        contact_phone
    )
    VALUES (
        %s,
        %s,
        %s,
        %s
    );
"""

sql2 = """
    INSERT INTO training.users (
        user_name,
        email,
        age,
        contact_phone,
    )
    VALUES (
        %s,
        %s,
        %s,
        %s
    );
"""


# email = "ivan@mail.ru"
# user_id = 11
#
#
# sql1 = """
#     SELECT
#         user_id,
#         user_name,
#         email,
#         balance
#     FROM training.users
#     WHERE user_id = %s OR email = %s
#     ORDER BY user_id;
# """

# print(sql)

with psycopg.connect(
    host='localhost',
    port=5432,
    dbname='demo',
    user="app_user",
    password="password"
) as connection:

    with connection.cursor() as cursor:
        # cursor.execute(
        #     sql,
        #     (user_name, email, age, phone),
        # )
        cursor.execute(
            sql1,
            (user_name, email, age, phone),
        )

        # row = cursor.fetchall()
        #
        # print(row)
        cursor.execute(
            sql2,
            (user_name2, email2, age2, phone2),
        )
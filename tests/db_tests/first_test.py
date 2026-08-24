import os
import random
import psycopg2
import pytest
from faker import Faker
from psycopg2._psycopg import cursor

f = Faker()

# Параметри підключення
# База даних повинна існувати на зазначеному хості, та юзер повинен мати право на читання цього запису
dbname = os.getenv('POSTGRES_DB', 'education_platform')
user = os.getenv('POSTGRES_USER', 'teacher')
password = os.getenv('POSTGRES_PASSWORD', 'super_password')
host = '172.23.48.1'
port = '5432'


@pytest.fixture(scope="session")
def connection():
    connection = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host,
        port=port
    )
    print("Connected to the database successfully!")

    # Для виконання запитів ви можете створити курсор
    cursor = connection.cursor()
    yield cursor, connection

    if cursor:
        cursor.close()

    if connection:
        # connection.commit()
        # connection.rollback()
        connection.close()
        print("PostgreSQL connection is closed")

@pytest.mark.db_test
def test_first_db(connection):
    exp_result_name, exp_result_desc = f.name(), f.job()
    cursor, conn = connection
    cursor.execute(f'''insert into "user" ("name", "desc") VALUES ('{exp_result_name}', '{exp_result_desc}') returning "id";''')
    id_result = cursor.fetchone()[0] # (id, )
    cursor.execute(f'''select * from "user" where id ={id_result}''') #(id, name, desc)
    actual_id, actual_name, actual_desc = cursor.fetchone()
    cursor.execute(f'''select * from "user"''')
    tes_all = cursor.fetchall()
    assert actual_id == id_result
    assert actual_name == exp_result_name
    assert actual_desc == exp_result_desc
    conn.commit()


@pytest.mark.db_test
def test_2(connection):
    cursor, conn = connection

    cursor.execute('''SELECT "id", "name", "user_id", "phone"
                      FROM "user"
                               full OUTER JOIN "user_details"
                                               ON "user"."id" = "user_details"."user_id"
                      where "user"."id" is null
                         or "user_details"."user_id" is NULL;
                   ''')
    tes_all = cursor.fetchall()
    for row in tes_all:
        if row[0] is None:
            assert row[2] is not None
            assert row[3] is not None
        if row[2] is None:
            assert row[0] is not None
            assert row[1] is not None
    conn.rollback()


def test_3(connection):
    cursor, conn = connection
    id_random = random.choice([0, 1, 2, 3, 6, 7, 8, 9])
    cursor.execute(f'''select * from "user" where id ={id_random}''') #(id, name, desc)
    actual_id, actual_name, actual_desc = cursor.fetchone()
    name_random = f.name()
    cursor.execute(f'''UPDATE "user" set name = '{name_random}' where "id" = {id_random} returning "id", "name", "desc";''')
    after_update_id, after_update_name, after_update_desc = cursor.fetchone()
    assert after_update_id == actual_id
    assert actual_name != after_update_name
    assert after_update_name == name_random
    assert after_update_desc == after_update_desc




    conn.rollback()

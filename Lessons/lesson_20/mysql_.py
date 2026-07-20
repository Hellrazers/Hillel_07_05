import sqlite3

from constans import BASE_DIR

# Спроба підключитись до бази даних
try:
    connection = sqlite3.connect(BASE_DIR / 'data.db')
    cursor = connection.cursor()
    print("Connected to the database successfully!")

    # Для виконання запитів ви можете створити курсор
    cursor = connection.cursor()

    # Для виконання SQL запитів ви можете викликати метод execute() курсора
    # Тут можна виконати будь який запит на мові SQL, і він виконається в БД


    # Отримання результатів запиту
    cursor.execute( '''CREATE TABLE IF NOT EXISTS User (
	Column2 INTEGER NOT NULL,
	Column3 TEXT NOT NULL,
	CONSTRAINT User_PK PRIMARY KEY (Column2)
);

                   ''')
    cursor.execute( '''insert into "user" ("Column2", "Column3") VALUES (1, 'QA') ''')
    return_values = cursor.fetchall()
    connection.commit()
except (Exception, sqlite3.Error) as error:
    print( error)

finally:
    # Закриваємо підключення
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
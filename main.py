import psycopg2
from config import host, user, password, db_name


try:
    # connect to exist database
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    connection.autocommit = True

    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT version();"
        )

        print(f"Server version: {cursor.fetchone()}")

    """Каждый стеллаж create в последовательности логики создания.
    А-Б-Ж-дополнительные от зависимости,затем insert данных"""

    # Стеллаж А

    try:
        with (connection.cursor() as cursor):
            cursor.execute(
                """CREATE TABLE Стеллаж_А(
                id serial PRIMARY KEY UNIQUE,
                name_id varchar(50) UNIQUE,
                type_id serial NOT NULL UNIQUE,
                quantity integer NOT NULL);"""
            )
            print("[INFO] Table created successfully")
            # connection_commit()
    except Exception as _ex:
        print("[INFO] Pass1")

        with connection.cursor() as cursor:
            cursor.execute(
                """INSERT INTO Стеллаж_А(name_id, quantity) VALUES
                ('Ноутбук', 8),
                ('Телевизор', 9);"""
            )
            print("[INFO] Date inserted successfully")
    except Exception as _ex:
        print("[INFO] Pass2")

    # Доп.Стеллаж А

    try:
        with (connection.cursor() as cursor):
            cursor.execute(
                """CREATE TABLE доп_стеллаж_а(
                name_id varchar(50) UNIQUE,
                quantity integer NOT NULL) INHERITS (Стеллаж_Ж);"""
            )
            # connection_commit()
            print("[INFO] Table created successfully")
    except Exception as _ex:
        print("[INFO] Pass3")

        with connection.cursor() as cursor:
            cursor.execute(
                """INSERT INTO доп_стеллаж_а(name_id, quantity) VALUES
                ('Часы', 5);"""
            )
    except Exception as _ex:
        print("[INFO] Pass4")

    # Стеллаж Б

    try:
        with (connection.cursor() as cursor):
            cursor.execute(
                """CREATE TABLE Стеллаж_Б(
                id serial PRIMARY KEY UNIQUE,
                name_id varchar(50) UNIQUE,
                type_id serial NOT NULL,
                quantity integer NOT NULL);"""
            )
            # connection_commit()
            print("[INFO] Table created successfully")
    except Exception as _ex:
        print("[INFO] Pass")

        with connection.cursor() as cursor:
            cursor.execute(
                """INSERT INTO Стеллаж_Б(name_id, quantity) VALUES
                ('Ноутбук', 0),
                ('Телевизор', 0),
                ('Телефон', 0);"""
            )

    # Доп.Стеллаж З

    try:
        with (connection.cursor() as cursor):
            cursor.execute(
                """CREATE TABLE доп_стеллаж_з(
                name_id varchar(50) UNIQUE,
                quantity integer NOT NULL) INHERITS (Стеллаж_Б);"""
            )
            # connection_commit()
            print("[INFO] Table created successfully")
    except Exception as _ex:
        print("[INFO] Pass")

        with connection.cursor() as cursor:
            cursor.execute(
                """INSERT INTO доп_стеллаж_з(name_id, quantity) VALUES
                ('Телефон', 1);"""
            )

    # Доп.Стеллаж В

    try:
        with (connection.cursor() as cursor):
            cursor.execute(
                """CREATE TABLE доп_стеллаж_в(
                name_id varchar(50) UNIQUE,
                quantity integer NOT NULL) INHERITS (Стеллаж_Б);"""
            )
            # connection_commit()
            print("[INFO] Table created successfully")
    except Exception as _ex:
        print("[INFO] Pass")

        with connection.cursor() as cursor:
            cursor.execute(
                """INSERT INTO доп_стеллаж_в(name_id, quantity) VALUES
                ('Телефон', 1);"""
            )

    # Стеллаж Ж

    try:
        with (connection.cursor() as cursor):
            cursor.execute(
                """CREATE TABLE Стеллаж_Ж(
                id serial PRIMARY KEY UNIQUE,
                name_id varchar(50) UNIQUE,
                type_id serial NOT NULL,
                quantity integer NOT NULL);"""
            )
            # connection_commit()
            print("[INFO] Table created successfully")
    except Exception as _ex:
        print("[INFO] Pass")

        with connection.cursor() as cursor:
            cursor.execute(
                """INSERT INTO Стеллаж_Ж(name_id, quantity) VALUES
                ('Системный блок', 4),
                ('Микрофон', 1);"""
            )


except Exception as _ex:
    print("[INFO] Error while working with PostgresSQL:", _ex)
finally:
    if connection:
        connection.close()
        print("[INFO] PostgresSQL connection closed")
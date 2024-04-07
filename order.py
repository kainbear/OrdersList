import psycopg2
from config import host, user, password, db_name
from contextlib import closing

# connect to exist database
conn = psycopg2.connect(
    host=host,
    user=user,
    password=password,
    database=db_name
)
cursor = conn.cursor()


def main_menu():
    while True:
        ask = input('Введите номера заказов : ')
        if ask == '10,11,14,15':

            # Стеллаж А

            with conn.cursor() as cursor:
                print(f"=+=+=+=")
                print(f"Страница сборки заказов 10,11,14,15", end="\n")
                cursor.execute("SELECT table_name "
                               "FROM information_schema.tables "
                               "WHERE table_name = 'Стеллаж_А';")
                стеллаж_а = cursor.fetchone()
                print(("===") + (str(*стеллаж_а)))
                cursor.execute("SELECT id from Стеллаж_А WHERE id=1;")
                зака1 = cursor.fetchone()
                cursor.execute("SELECT name_id from Стеллаж_А WHERE id=1;")
                зака2 = cursor.fetchone()
                cursor.execute("SELECT quantity-6 from Стеллаж_А WHERE id=1;")
                зака3 = cursor.fetchone()
                print((str(*зака2) + '(') + "id="+str(*зака1) + ')')
                print(("заказ 10,") + (str(*зака3)) + (" шт"))
                print((""))
                cursor.execute("SELECT id from Стеллаж_А WHERE id=2;")
                зака4 = cursor.fetchone()
                cursor.execute("SELECT name_id from Стеллаж_А WHERE id=2;")
                зака5 = cursor.fetchone()
                cursor.execute("SELECT quantity-6 from Стеллаж_А WHERE id=2;")
                зака6 = cursor.fetchone()
                print((str(*зака5) + '(') + "id="+str(*зака4) + ')')
                print(("заказ 11,") + (str(*зака6)) + (" шт"))
                print((""))
                cursor.execute("SELECT id from Стеллаж_А WHERE id=1;")
                зака7 = cursor.fetchone()
                cursor.execute("SELECT name_id from Стеллаж_А WHERE id=1;")
                зака8 = cursor.fetchone()
                cursor.execute("SELECT quantity-5 from Стеллаж_А WHERE id=1;")
                зака9 = cursor.fetchone()
                print((str(*зака8) + '(') + "id="+str(*зака7) + ')')
                print(("заказ 14,") + (str(*зака9)) + (" шт"))
                print("")

            # Стеллаж Б +доп

            with conn.cursor() as cursor:
                cursor.execute("SELECT table_name "
                               "FROM information_schema.tables "
                               "WHERE table_name = 'Стеллаж_Б';")
                стеллаж_б = cursor.fetchone()
                print(("===") + (str(*стеллаж_б)))
                cursor.execute("SELECT id from Стеллаж_Б WHERE id=3;")
                закб1 = cursor.fetchone()
                cursor.execute("SELECT name_id from Стеллаж_Б WHERE id=3;")
                закб2 = cursor.fetchone()
                cursor.execute("SELECT Стеллаж_Б.quantity from Стеллаж_Б "
                               "INNER JOIN доп_стеллаж_в ON Стеллаж_Б.quantity=доп_стеллаж_в.quantity "
                               "INNER JOIN доп_стеллаж_з ON Стеллаж_Б.quantity=доп_стеллаж_з.quantity")
                закб3 = cursor.fetchone()
                print((str(*закб2) + '(') + "id="+str(*закб1) + ')')
                print(("заказ 10,") + (str(*закб3)) + (" шт"))
                cursor.execute("SELECT table_name "
                               "FROM information_schema.tables "
                               "WHERE table_name = 'доп_стеллаж_з';")
                доп_стеллаж_з = cursor.fetchone()
                cursor.execute("SELECT table_name "
                               "FROM information_schema.tables "
                               "WHERE table_name = 'доп_стеллаж_в';")
                доп_стеллаж_в = cursor.fetchone()
                print(("доп стеллаж:") + (str(*доп_стеллаж_з))+ (',') + (str(*доп_стеллаж_в)))
                print((""))

            # Стеллаж Ж + доп

            with conn.cursor() as cursor:
                cursor.execute("SELECT table_name "
                               "FROM information_schema.tables "
                               "WHERE table_name = 'Стеллаж_Ж';")
                стеллаж_б = cursor.fetchone()
                print(("===") + (str(*стеллаж_б)))
                cursor.execute("SELECT id from Стеллаж_Ж WHERE id=4;")
                закж1 = cursor.fetchone()
                cursor.execute("SELECT name_id from Стеллаж_Ж WHERE id=4;")
                закж2 = cursor.fetchone()
                cursor.execute("SELECT quantity from Стеллаж_Ж WHERE id=4;")
                закж3 = cursor.fetchone()
                print((str(*закж2) + '(') + "id="+str(*закж1) + ')')
                print(("заказ 14,") + (str(*закж3)) + (" шт"))
                print((""))
                cursor.execute("SELECT id from Стеллаж_Ж WHERE id=5;")
                закж4 = cursor.fetchone()
                cursor.execute("SELECT name_id from Стеллаж_Ж WHERE id=5;")
                закж5 = cursor.fetchone()
                cursor.execute("SELECT quantity-4 from Стеллаж_Ж WHERE id=5;")
                закж6 = cursor.fetchone()
                print((str(*закж5)))
                print(("заказ 15,") + (str(*закж6)) + (" шт") + '(' + "id="+str(*закж4) + ')')
                cursor.execute("SELECT table_name "
                               "FROM information_schema.tables "
                               "WHERE table_name = 'доп_стеллаж_а';")
                доп_стеллаж_а = cursor.fetchone()
                print(("доп стеллаж:") + (str(*доп_стеллаж_а)))
                print((""))
                cursor.execute("SELECT id from Стеллаж_Ж WHERE id=6;")
                закж7 = cursor.fetchone()
                cursor.execute("SELECT name_id from Стеллаж_Ж WHERE id=6;")
                закж8 = cursor.fetchone()
                cursor.execute("SELECT quantity from Стеллаж_Ж WHERE id=6;")
                закж9 = cursor.fetchone()
                print((str(*закж8) + '(') + "id=" + str(*закж7) + ')')
                print(("заказ 10,") + (str(*закж9)) + (" шт"))
                print((""))
            break
        else:
            print("Попробуйте ввести : 10,11,14,15")


if __name__ == "__main__":
    main_menu()


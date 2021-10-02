import psycopg2

from psycopg2 import Error
from settings import *
from faker import Faker


try:
    connection = psycopg2.connect(
        user=USER,
        password=PASSWORD,
        host=HOST,
        port=PORT,
        database='shop_db'
    )
    fake = Faker()

    for _ in range(50):
        add_city = """INSERT INTO city (id,city_name,country_id) VALUES (%s,%s)"""
        cursor.executemany(add_city, fake.city())

    connection.commit()
    print('Done')
except(Exception, Error) as error:
    print("Error connection: ", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print('Connection was closed')

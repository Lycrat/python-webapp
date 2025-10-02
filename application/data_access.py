from dotenv import load_dotenv
import pymysql
import os

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_NAME = os.getenv("DB_NAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")


# Connect to MySQL server
def get_connection():
    connection = pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )
    return connection


connection = get_connection()
try:
    with connection.cursor() as cursor:
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
        cursor.execute(f"use {DB_NAME}")
        cursor.execute(f"""CREATE TABLE IF NOT EXISTS jokes (
                       ID int auto_increment,
                       Setup varchar(255),
                       Punchline varchar(255),
                       PRIMARY KEY (ID)
                       )""") 
        print(f"Database '{DB_NAME}' created or already exists.")

        cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT,
                username VARCHAR(50) NOT NULL UNIQUE,
                password_hash VARCHAR(255) NOT NULL,
                PRIMARY KEY (id)
            )
        """)
finally:
    connection.close()


def get_joke():
    connection = get_connection()
    joke = ()
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM vGetJokes ORDER BY RAND()")
        joke = cursor.fetchone()
    connection.close()
    return joke

def get_jokes_count():
    connection = get_connection()
    count = 0
    with connection.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) FROM jokes")
        count = cursor.fetchone() 
    connection.close()

    return count

def add_joke_to_database(setup, punchline):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("CALL pAddJoke(%s, %s);", (setup, punchline))
            connection.commit()
            print("added joke to database")
    except Exception as e:
        print(e)
    finally:
        connection.close()


def add_user(username, password):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("CALL pAddUser(%s, %s);",(username, password))
            connection.commit()
    finally:
            connection.close()

def get_user(username):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
            return cursor.fetchone()
    finally:
            connection.close()






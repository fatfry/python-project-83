import psycopg2
from psycopg2.extras import NamedTupleCursor
from functools import wraps
from flask import Flask
import os
from flask import abort


app = Flask(__name__)
app.config['DATABASE_URL'] = os.getenv('DATABASE_URL')


def connect_db(app):
    try:
        conn = psycopg2.connect(
            app.config['DATABASE_URL'],
            cursor_factory=NamedTupleCursor
        )
        return conn
    except psycopg2.Error as e:
        # Обработка ошибок подключения
        print(f"Ошибка подключения к базе данных: {e}")
        return None


with connect_db(app) as conn:
    if conn is not None:
        with conn.cursor() as curs:
            curs.execute("SELECT * FROM users")
            results = curs.fetchall()







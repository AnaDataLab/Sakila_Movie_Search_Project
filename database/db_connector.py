from pymysql import connect, MySQLError
from pymysql.cursors import DictCursor
import os
from dotenv import load_dotenv

env_path = os.path.join(os.getcwd(), ".env")
load_dotenv(dotenv_path = env_path)

read_db_config = {
    "host": os.getenv("HOST1"),
    "user": os.getenv("USER1"),
    "password": os.getenv("PASSWORD1"),
    "database": os.getenv("DATABASE1"),
    "cursorclass": DictCursor
}

write_db_config = {
    "host": os.getenv("HOST2"),
    "user": os.getenv("USER2"),
    "password": os.getenv("PASSWORD2"),
    "database": os.getenv("DATABASE2"),
    "cursorclass": DictCursor
}

def create_read_connection():
    try:
        conn = connect(**read_db_config)
        return conn
    except MySQLError as e:
        print(f"Connection error to sakila database: {e}")
        return None

def create_write_connection():
    try:
        conn = connect(**write_db_config)
        return conn
    except MySQLError as e:
        print(f"Connection error to movie_requests_db: {e}")
        return None

def close_connection(conn):
    if conn:
        conn.close()

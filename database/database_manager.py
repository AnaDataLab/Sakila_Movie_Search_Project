from database.db_connector import create_read_connection, create_write_connection, close_connection
from database.sql_queries import (
    SEARCH_MOVIES_BY_TITLE,
    SEARCH_MOVIES_BY_GENRE_AND_YEAR,
    SEARCH_MOVIES_BY_ACTOR,
    TOP_10_POPULAR_MOVIES,
    SAVE_SEARCH_QUERY,
    GET_POPULAR_QUERIES_DATA
)

def create_tables():
    #таблицa user_requests в локальной базе, если её нет
    conn = create_write_connection()
    if not conn:
        return

    try:
        with conn.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS user_requests (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    search_type VARCHAR(50),
                    query VARCHAR(255),
                    search_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
            """)
            conn.commit()
            #print("✅Table user_requests checked/created.")
    except Exception as e:
        print(f"Error creating the table: {e}")
    finally:
        close_connection(conn)


def search_movies_by_title(title):
    conn = create_read_connection()
    if not conn:
        return []

    try:
        with conn.cursor() as cursor:
            cursor.execute(SEARCH_MOVIES_BY_TITLE, (f"%{title}%",))
            movies = cursor.fetchall()
            return movies
    except Exception as e:
        print(f"Error searching for movies by title: {e}")
        return []
    finally:
        close_connection(conn)


def search_movies_by_genre_and_year(genre, year):
    conn = create_read_connection()
    if not conn:
        return []

    try:
        with conn.cursor() as cursor:
            cursor.execute(SEARCH_MOVIES_BY_GENRE_AND_YEAR, (genre, year))
            movies = cursor.fetchall()
            return movies
    except Exception as e:
        print(f"Error searching for movies by genre and year: {e}")
        return []
    finally:
        close_connection(conn)


def search_movies_by_actor(actor_name):
    conn = create_read_connection()
    if not conn:
        return []

    try:
        with conn.cursor() as cursor:
            cursor.execute(SEARCH_MOVIES_BY_ACTOR, (f"%{actor_name}%", f"%{actor_name}%"))
            movies = cursor.fetchall()
            return movies
    except Exception as e:
        print(f"Error searching for movies by actor: {e}")
        return []
    finally:
        close_connection(conn)


def get_top_10_popular_movies():
    #список 10 самых популярных фильмов по количеству просмотров
    conn = create_read_connection()
    if not conn:
        return []

    try:
        with conn.cursor() as cursor:
            cursor.execute(TOP_10_POPULAR_MOVIES)
            movies = cursor.fetchall()
            return movies
    except Exception as e:
        print(f"Error retrieving the top 10 popular movies: {e}")
        return []
    finally:
        close_connection(conn)


def save_search_query(search_type, query):
    conn = create_write_connection()
    if not conn:
        return

    try:
        with conn.cursor() as cursor:
            cursor.execute(SAVE_SEARCH_QUERY, (search_type, query))
            conn.commit()
    except Exception as e:
        print(f"Error saving the search query: {e}")
    finally:
        close_connection(conn)


def get_popular_queries_data():
    #Возвращает данные для визуализации популярных запросов
    conn = create_write_connection()

    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute(GET_POPULAR_QUERIES_DATA)
            results = cursor.fetchall()
            return [row["query"] for row in results], [row["count"] for row in results]  #Разделяем данные на два списка
        except Exception as e:
            print(f"Error retrieving data for visualization: {e}")
            return [], []
        finally:
            close_connection(conn)
    else:
        print("Failed to connect to the database.")
        return [], []
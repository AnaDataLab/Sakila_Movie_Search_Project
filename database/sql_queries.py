SEARCH_MOVIES_BY_TITLE = """
SELECT title, release_year, description, rating 
FROM film 
WHERE title LIKE %s
ORDER BY release_year DESC 
LIMIT 10;
"""

SEARCH_MOVIES_BY_GENRE_AND_YEAR = """
SELECT f.film_id, f.title, f.release_year, f.description, f.rating
FROM film as f
JOIN film_category as fc ON f.film_id = fc.film_id
JOIN category as c ON fc.category_id = c.category_id
WHERE c.name = %s AND f.release_year = %s
ORDER BY f.release_year DESC
LIMIT 10;
"""

SEARCH_MOVIES_BY_ACTOR = """
SELECT a.first_name, a.last_name, f.title, f.release_year, f.description, f.rating
FROM film as f
JOIN film_actor as fa ON f.film_id = fa.film_id
JOIN actor as a ON fa.actor_id = a.actor_id
WHERE a.first_name LIKE %s OR a.last_name LIKE %s
ORDER BY f.release_year DESC
LIMIT 10;
"""

#ТОП-10 самых просматриваемых фильмов
TOP_10_POPULAR_MOVIES = """
SELECT f.title, f.release_year, f.rating, f.description, COUNT(r.rental_id) AS views
FROM rental as r
JOIN inventory as i ON r.inventory_id = i.inventory_id
JOIN film as f ON i.film_id = f.film_id
GROUP BY f.title, f.release_year, f.rating
ORDER BY views DESC
LIMIT 10;
"""

#запрос для сохранения поисковых запросов в локальную базу movie_requests_db
SAVE_SEARCH_QUERY = """
INSERT INTO user_requests (search_type, query) 
VALUES (%s, %s);
"""

#визуализация популярных запросов
GET_POPULAR_QUERIES_DATA = """
SELECT query, COUNT(*) as count 
FROM user_requests 
GROUP BY query 
ORDER BY count DESC 
LIMIT 10;
"""
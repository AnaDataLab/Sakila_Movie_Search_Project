--  Запросы к удалённой базе sakila
USE sakila;

-- Поиск фильмов по названию
SELECT title, release_year, description, rating
FROM film
-- WHERE title LIKE '%way%' -- пример
ORDER BY release_year DESC
LIMIT 10;

-- Поиск фильмов по жанру и году
SELECT f.title, c.name, f.release_year, f.description, f.rating
FROM film as f
JOIN film_category as fc ON f.film_id = fc.film_id
JOIN category as c ON fc.category_id = c.category_id
-- WHERE c.name = 'travel' AND f.release_year = 2025 -- пример
ORDER BY f.release_year DESC
LIMIT 10;

-- Поиск фильмов по актёру
SELECT a.first_name, a.last_name, f.title, f.release_year, f.description, f.rating
FROM sakila.film f
JOIN sakila.film_actor fa ON f.film_id = fa.film_id
JOIN sakila.actor a ON fa.actor_id = a.actor_id
-- WHERE a.first_name LIKE '%meg%' OR a.last_name LIKE '%hawke%' -- пример
ORDER BY f.release_year DESC
LIMIT 10;

-- ТОП-10 самых популярных фильмов (по просмотрам)
SELECT f.title, f.release_year, COUNT(r.rental_id) AS views
FROM sakila.rental r
JOIN sakila.inventory i ON r.inventory_id = i.inventory_id
JOIN sakila.film f ON i.film_id = f.film_id
GROUP BY f.title, f.release_year
ORDER BY views DESC
LIMIT 10;




-- 1. Создание локальной базы (если ещё не создана)

CREATE DATABASE IF NOT EXISTS movie_requests_db;
USE movie_requests_db;

-- 2. Создание таблицы для хранения поисковых запросов
CREATE TABLE IF NOT EXISTS user_requests (
    id INT AUTO_INCREMENT PRIMARY KEY,
    search_type VARCHAR(50),
    query VARCHAR(255),
    search_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Сохранение поискового запроса (тестирование)
INSERT INTO user_requests (search_type, query) VALUES ('title', 'Inception');

-- Проверка
SELECT * FROM user_requests;

-- Получение популярных запросов
SELECT query, COUNT(*) as count
FROM user_requests
GROUP BY query
ORDER BY count DESC
LIMIT 10;








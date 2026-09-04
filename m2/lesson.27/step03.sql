-- SELECT country
-- FROM airports;


-- SELECT DISTINCT country
-- FROM airports;

SELECT DISTINCT country, city
FROM airports
ORDER BY  country DESC, city ASC;
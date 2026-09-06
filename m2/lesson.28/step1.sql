-- SELECT
-- 	airport_code,
-- 	airport_name,
-- 	city
-- FROM airports
-- WHERE city = 'Moscow';


-- SELECT
-- 	airport_code,
-- 	airport_name,
-- 	city
-- FROM airports
-- WHERE city LIKE 'Mos%';



-- SELECT
-- 	airport_code,
-- 	airport_name,
-- 	city
-- FROM airports
-- WHERE city LIKE 'Mos___';

-- SELECT
-- 	airport_code,
-- 	airport_name,
-- 	city
-- FROM airports
-- WHERE city LIKE '_o%';


-- SELECT
-- 	airport_code,
-- 	airport_name,
-- 	city
-- FROM airports
-- WHERE city LIKE 'm%';


-- SELECT
-- 	airport_code,
-- 	airport_name,
-- 	city
-- FROM airports
-- WHERE city ILIKE 'mo%';


-- SELECT
-- 	airport_code,
-- 	airport_name,
-- 	city
-- FROM airports
-- WHERE city NOT ILIKE 'mo%';



-- SELECT
-- 	airport_code,
-- 	LOWER(airport_code) AS lower_code,
-- 	airport_name,
-- 	city
-- FROM airports;


-- SELECT
-- 	airport_code,
-- 	airport_name,
-- 	city,
-- 	UPPER(city) AS upper_city,
-- 	LENGTH(city) AS len_city
-- FROM airports;


-- SELECT
-- 	airport_code,
-- 	airport_name,
-- 	city,
-- 	UPPER(city) AS upper_city,
-- 	LENGTH(city) AS len_city
-- FROM airports
-- WHERE LENGTH(city) > 20;


-- SELECT
-- 	airport_code,
-- 	airport_name,
-- 	city,
-- 	REPLACE(city, ' ', '__') AS upper_city,
-- 	LENGTH(city) AS len_city
-- FROM airports
-- WHERE LENGTH(city) > 20;


SELECT
	UPPER(TRIM('     Bob Name    ')) as result

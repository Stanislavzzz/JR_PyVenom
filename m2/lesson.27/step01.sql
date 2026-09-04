-- SELECT version();

-- SELECT current_user;

SELECT current_database();





-- SELECT current_database();

-- SELECT * 
-- FROM airplanes;


-- SELECT * 
-- FROM airports;


SELECT 
	country AS "Страна", 
	city AS "Город Аэропорта"	
FROM airports
LIMIT 10;



-- SELECT model, 
-- 	   range / 1000 AS range_1000,
-- 	   speed,
-- 	   speed * 2 AS speed_2

-- FROM airplanes;

-- select *
-- FROM airplanes;



-- SELECT airplane_code || ' -!- ' || model AS airplane


-- FROM airplanes;



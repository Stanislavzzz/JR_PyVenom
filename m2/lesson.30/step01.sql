-- https://sql-ex.ru/?Lang=0


-- SELECT *
-- FROM flights
-- WHERE actual_departure IS NOT NULL;

-- SELECT
-- 	model,
-- 	range,
-- 	CASE
-- 		WHEN range >= 10000 THEN 'Дальний'
-- 		WHEN range >= 5000 THEN 'Средний'
-- 		ELSE 'Ближний'
-- 	END AS range_category
-- FROM airplanes
-- ORDER BY range DESC;


-- SELECT
-- 	COUNT(*)
-- FROM bookings;


-- SELECT
-- 	COUNT(actual_departure) AS dep
-- FROM flights



-- SELECT
-- 	COUNT(DISTINCT(country)) AS d_c
-- FROM airports;

-- SELECT
-- 	SUM(total_amount)
-- FROM bookings;



-- SELECT
-- 	AVG(total_amount)
-- FROM bookings;


-- SELECT
-- 	MIN(total_amount)
-- FROM bookings;

-- SELECT
-- 	MAX(total_amount),
-- 	MIN(total_amount)
-- FROM bookings;


-- SELECT
-- 	fare_conditions,
-- 	COUNT(*) AS aegments_count,
-- 	AVG(price) AS  avg_price,
-- 	MIN(price) AS  min_price,
-- 	MAX(price) AS  max_price
-- FROM segments
-- GROUP BY fare_conditions;



-- SELECT
-- 	status,
-- 	COUNT(*) AS count_f
-- FROM flights
-- WHERE scheduled_departure > bookings.now()
-- GROUP BY status
-- ORDER BY count_f;

-- SELECT
-- *
-- FROM flights
-- WHERE scheduled_departure > bookings.now()


-- SELECT
-- 	status,
-- 	COUNT(*) AS count_f
-- FROM flights
-- WHERE scheduled_departure > bookings.now()
-- GROUP BY status
-- HAVING COUNT(*) > 15
-- ORDER BY count_f;


-- SELECT
-- 	*
-- FROM bookings
-- WHERE total_amount > (
-- 	SELECT
-- 		AVG(total_amount)
-- 	FROM bookings
-- )
-- ORDER BY total_amount ASC;

-- WITH exp_booking AS (
-- 	SELECT
-- 		book_ref,
-- 		book_date,
-- 		total_amount
-- 	FROM bookings
-- 	WHERE total_amount > 30000
-- )

-- SELECT
-- 	book_ref,
-- 	total_amount
-- FROM exp_booking
-- ORDER BY total_amount DESC;




-- WITH fare_stats_one AS (
-- 	SELECT
-- 		fare_conditions,
-- 		COUNT(*) AS s_count,
-- 		AVG(price) AS a_price
-- 	FROM segments
-- 	GROUP BY fare_conditions
-- ),

-- fare_stats_two AS (
-- 	SELECT
-- 		fare_conditions,
-- 		COUNT(*) AS s_count,
-- 		AVG(price) AS a_price
-- 	FROM segments
-- 	GROUP BY fare_conditions
-- )

-- SELECT
-- 	fare_conditions,
-- 	a_price
-- FROM fare_stats_two
-- WHERE a_price > 6000;



-- SELECT
-- 	route_no
-- FROM flights
-- WHERE status = 'Delayed'

-- UNION ALL

-- SELECT
-- 	route_no
-- FROM flights
-- WHERE status = 'Cancelled';



SELECT
	route_no
FROM flights
WHERE status = 'Delayed'

UNION

SELECT
	route_no
FROM flights
WHERE status = 'Delayed';

-- SELECT
-- 	model, range
-- FROM airplanes
-- WHERE range > 10000;

-- SELECT DISTINCT status
-- FROM flights;

-- SELECT flight_id, route_no, status
-- FROM flights
-- WHERE status != 'Delayed';
-- -- WHERE status = 'Delayed';


SELECT *
FROM bookings
WHERE total_amount > 500000
ORDER BY total_amount DESC
LIMIT 10;
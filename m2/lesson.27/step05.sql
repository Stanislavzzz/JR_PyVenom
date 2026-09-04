-- SELECT
-- 	model, range, speed
-- FROM airplanes
-- WHERE range > 10000 OR speed > 900;

-- SELECT flight_id, route_no, status
-- FROM flights
-- WHERE NOT status != 'Delayed';


-- SELECT flight_id, route_no, status
-- FROM flights
-- WHERE status in ('Delayed', 'Cancelled');
-- -- WHERE status = 'Delayed' OR status = 'Cancelled'


-- SELECT *
-- FROM airports
-- WHERE airport_code NOT IN ('SVO', 'DME', 'VKO') AND city = 'Moscow';
-- -- WHERE city = 'Moscow';


SELECT *
FROM bookings
WHERE total_amount NOT BETWEEN 500000 AND 1000000;
-- WHERE total_amount >= 500000 AND total_amount <= 1000000;
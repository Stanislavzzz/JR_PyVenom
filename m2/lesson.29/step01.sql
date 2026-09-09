-- SELECT
-- 	bookings.book_ref,
-- 	bookings.book_date,
-- 	tickets.passenger_name
-- FROM bookings
-- INNER JOIN tickets ON bookings.book_ref = tickets.book_ref
-- LIMIT 100;


-- SELECT
-- 	b.book_ref,
-- 	b.book_date,
-- 	t.passenger_name
-- FROM bookings AS b
-- INNER JOIN tickets AS t
-- 	ON b.book_ref = t.book_ref
-- LIMIT 10;


-- SELECT
-- 	b.book_ref,
-- 	b.book_date,
-- 	t.passenger_name
-- FROM bookings b
-- INNER JOIN tickets t
-- 	ON b.book_ref = t.book_ref
-- LIMIT 15;


-- SELECT
-- 	b.book_ref,
-- 	b.book_date,
-- 	t.passenger_name,
-- 	b.total_amount
-- FROM bookings b
-- INNER JOIN tickets t
-- 	ON b.book_ref = t.book_ref

-- WHERE b.total_amount < 700000
-- ORDER BY b.total_amount DESC
-- LIMIT 15;


-- SELECT
-- 	b.book_ref,
-- 	b.book_date,
-- 	t.passenger_name,
-- 	b.total_amount
-- FROM bookings b
-- JOIN tickets t
-- 	ON b.book_ref = t.book_ref

-- WHERE b.total_amount < 700000
-- ORDER BY b.total_amount DESC
-- LIMIT 15;


-- SELECT
-- 	*
-- 	-- b.book_ref,
-- 	-- b.book_date,
-- 	-- t.passenger_name,
-- 	-- b.total_amount
-- FROM bookings b
-- JOIN tickets t
-- 	ON b.book_ref = t.book_ref
-- JOIN segments s
-- 	ON t.ticket_no = s.ticket_no
-- JOIN flights f
-- 	ON s.flight_id = f.flight_id
-- WHERE b.total_amount < 700000 AND b.book_ref = 'JU35I4'
-- ORDER BY b.total_amount DESC
-- LIMIT 15;


-- SELECT
-- 	*
-- 	-- b.book_ref,
-- 	-- b.book_date,
-- 	-- t.passenger_name,
-- 	-- b.total_amount
-- FROM bookings b
-- JOIN tickets t
-- 	ON b.book_ref = t.book_ref
-- JOIN segments s
-- 	ON t.ticket_no = s.ticket_no
-- JOIN flights f
-- 	ON s.flight_id = f.flight_id
-- WHERE b.total_amount < 700000 AND b.book_ref = 'JU35I4'
-- ORDER BY b.total_amount DESC
-- LIMIT 15;

-- SELECT *
-- FROM airplanes as a
-- JOIN seats AS s
-- 	ON a.airplane_code = s.airplane_code
-- ORDER BY
-- 	a.airplane_code,
-- 	s.seat_no


-- SELECT *
-- FROM airplanes as a
-- LEFT JOIN seats AS s
-- 	ON a.airplane_code = s.airplane_code
-- ORDER BY
-- 	s.seat_no DESC,
-- 	a.airplane_code


-- SELECT *
-- FROM airplanes_data as a
-- LEFT JOIN seats AS s
-- 	ON a.airplane_code = s.airplane_code
-- ORDER BY
-- 	s.seat_no DESC,
-- 	a.airplane_code


-- SELECT *
-- FROM airplanes as a
-- LEFT JOIN seats AS s
-- 	ON a.airplane_code = s.airplane_code
-- WHERE s.seat_no IS NULL
-- ORDER BY
-- 	a.airplane_code;

-- SELECT *
-- FROM airplanes as a
-- LEFT JOIN seats AS s
-- 	ON a.airplane_code = s.airplane_code
-- 	AND s.fare_conditions = 'Business'

-- ORDER BY
-- 	a.airplane_code ASC;


-- SELECT *
-- FROM airplanes as a
-- RIGHT JOIN seats AS s
-- 	ON a.airplane_code = s.airplane_code
-- WHERE a.airplane_code IS NULL
-- -- ORDER BY
-- -- 	a.airplane_code ASC;


-- SELECT *
-- FROM airplanes as a
-- FULL OUTER JOIN seats AS s
-- 	ON a.airplane_code = s.airplane_code
-- WHERE a.airplane_code IS NULL


-- SELECT *
-- FROM airplanes as a
-- FULL JOIN seats AS s
-- 	ON a.airplane_code = s.airplane_code


SELECT
	a.model,
	fc.fare_conditions
FROM airplanes as a
CROSS JOIN (
	VALUES
		('Economy'),
		('Comfort'),
		('Business')
) AS fc(fare_conditions);




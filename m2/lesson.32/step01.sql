-- ALTER TABLE training.users
-- ADD COLUMN phone text;


-- ALTER TABLE training.users
-- ADD COLUMN language text
-- 	NOT NULL
-- 	DEFAULT 'ru';


-- ALTER TABLE training.users
-- RENAME COLUMN phone TO contact_phone;


-- ALTER TABLE training.orders
-- ALTER COLUMN status
-- SET DEFAULT 'created';


-- ALTER TABLE training.orders
-- ALTER COLUMN status
-- DROP DEFAULT;


-- ALTER TABLE training.orders
-- ALTER COLUMN status
-- SET DEFAULT 'new';


-- ALTER TABLE training.users
-- ALTER COLUMN contact_phone
-- SET NOT NULL;


-- ALTER TABLE training.orders
-- ADD CONSTRAINT chk_orders_status
-- CHECK (
-- 	status IN ('new', 'paid', 'cancelled')
-- );


-- ALTER TABLE training.orders
-- DROP CONSTRAINT chk_orders_status;


-- ALTER TABLE training.users
-- DROP COLUMN IF EXISTS language;


-- ALTER TABLE training.users
-- ALTER COLUMN user_name
-- TYPE varchar(100);


-- DROP TABLE IF EXISTS training.contacts;


-- INSERT INTO training.users (
-- 	user_name,
-- 	email,
-- 	age,
-- 	birth_date,
-- 	contact_phone
-- )

-- VALUES (
-- 	'Bob',
-- 	'bob@mail.ru',
-- 	31,
-- 	'1999-01-03',
-- 	'1234567'
-- );


-- SELECT *
-- FROM training.users;


-- INSERT INTO training.users (
-- 	email,
-- 	birth_date,
-- 	age,
-- 	contact_phone,
-- 	user_name
-- )

-- VALUES (
-- 	'anna@mail.com',
-- 	'2001-07-05',
-- 	27,
-- 	'7654321',
-- 	'Anna'
-- );


-- SELECT *
-- FROM training.users;


-- INSERT INTO training.users (
-- 	user_name,
-- 	email,
-- 	age,
-- 	birth_date,
-- 	contact_phone
-- )

-- VALUES
-- 	(
-- 		'Mary',
-- 		'mary@mail.ru',
-- 		35,
-- 		'1995-10-03',
-- 		'3456789'
-- 	),
-- 	(
-- 		'Ivan',
-- 		'ivan@mail.ru',
-- 		37,
-- 		'1993-12-15',
-- 		'9875763'
-- 	);


-- SELECT *
-- FROM training.users;


-- INSERT INTO training.users (
-- 	user_name,
-- 	email,
-- 	age,
-- 	birth_date,
-- 	contact_phone,
-- 	balance
-- )

-- VALUES
-- 	(
-- 		'John',
-- 		'john@mail.ru',
-- 		32,
-- 		'1992-10-03',
-- 		'2256789',
-- 		100.12
-- 	);


-- INSERT INTO training.users (
-- 	user_name,
-- 	email,
-- 	age,
-- 	birth_date,
-- 	contact_phone,
-- 	balance
-- )

-- VALUES
-- 	(
-- 		'Sara',
-- 		'sara@mail.ru',
-- 		45,
-- 		'1984-10-03',
-- 		'3333789',
-- 		DEFAULT
-- 	);


-- SELECT *
-- FROM training.users;


-- INSERT INTO training.users (
-- 	user_name,
-- 	email,
-- 	age,
-- 	birth_date,
-- 	contact_phone,
-- 	balance
-- )

-- VALUES
-- 	(
-- 		'Max',
-- 		'max@mail.ru',
-- 		41,
-- 		'1985-10-03',
-- 		'4444789',
-- 		150.07
-- 	)
-- RETURNING user_id;


-- INSERT INTO training.users (
-- 	user_name,
-- 	email,
-- 	age,
-- 	birth_date,
-- 	contact_phone,
-- 	balance
-- )

-- VALUES
-- 	(
-- 		'Anton',
-- 		'ant@mail.ru',
-- 		21,
-- 		'2005-10-03',
-- 		'5555589',
-- 		450.07
-- 	)
-- RETURNING user_id, user_name, email, balance;


-- UPDATE  training.users
-- SET balance = 1000;


-- SELECT *
-- FROM training.users;


-- UPDATE  training.users
-- SET balance = 2500
-- WHERE email = 'sara@mail.ru';



-- UPDATE  training.users
-- SET balance += 1000;



-- UPDATE  training.users
-- SET
-- 	user_name = 'Bobs',
-- 	age = age + 1,
-- 	is_active = False,
-- 	balance = balance + 1000
-- WHERE user_name = 'Bob';


-- SELECT *
-- FROM training.users;


-- UPDATE  training.users
-- SET
-- 	user_name = 'Bob1',
-- 	age = age + 1,
-- 	is_active = True,
-- 	balance = balance + 2000
-- WHERE user_name = 'Bobs'


-- RETURNING *;

-- DELETE FROM training.users
-- WHERE user_id = 2;


-- SELECT *
-- FROM training.users;


-- DELETE FROM training.users
-- WHERE user_id = 10

-- RETURNING user_name, email, age;


-- DELETE FROM training.users;


SELECT *
FROM training.users;

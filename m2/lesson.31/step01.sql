-- SELECT
-- 	schema_name
-- FROM information_schema.schemata;

-- CREATE SCHEMA IF NOT EXISTS training;


-- SELECT
-- 	schema_name
-- FROM information_schema.schemata
-- WHERE schema_name = 'training';


-- SHOW search_path;


-- SELECT *
-- FROM flights;


-- SELECT *
-- FROM bookings.flights;


-- CREATE TABLE training.users (
-- 	user_id bigint,
-- 	user_name text,
-- 	age integer
-- );


-- CREATE TABLE training.contacts (
-- 	email text
-- );


-- DROP TABLE IF EXISTS training.users;


-- CREATE TABLE training.users (
-- 	user_id bigint,
-- 	user_name text,
-- 	email text,
-- 	age integer,
-- 	balance numeric(12, 2),
-- 	is_active boolean,
-- 	birth_date date,
-- 	created_at timestamptz,
-- 	external_id uuid,
-- 	profile jsonb
-- );


-- SELECT
-- 	column_name,
-- 	data_type
-- FROM information_schema.columns
-- WHERE table_schema = 'training'
-- 	AND table_name = 'users';


-- DROP TABLE IF EXISTS training.users;

-- CREATE TABLE training.users (
-- 	user_id bigint
-- 		GENERATED ALWAYS AS IDENTITY
-- 		PRIMARY KEY,
-- 	user_name text
-- 		NOT NULL
-- 		CHECK (length(trim(user_name)) > 0),
-- 	email text
-- 		NOT NULL
-- 		UNIQUE,
-- 	-- age integer CHECK (age >= 0),
-- 	age integer
-- 		NOT NULL
-- 		CHECK (age BETWEEN 0 AND 150),
-- 	balance numeric(12, 2)
-- 		NOT NULL
-- 		DEFAULT 0
-- 		CHECK (balance >= 0),
-- 	is_active boolean
-- 		NOT NULL
-- 		DEFAULT TRUE,
-- 	birth_date date,
-- 	created_at timestamptz
-- 		NOT NULL
-- 		DEFAULT now(),
-- 	external_id uuid,
-- 	profile jsonb
-- );


-- SELECT
-- 	column_name,
-- 	data_type,
-- 	is_nullable,
-- 	column_default
-- FROM information_schema.columns
-- WHERE table_schema = 'training'
-- 	AND table_name = 'users';


-- DROP TABLE IF EXISTS training.orders;

-- CREATE TABLE training.orders (
-- 	order_id bigint
-- 		GENERATED ALWAYS AS IDENTITY
-- 		PRIMARY KEY,
-- 	user_id bigint
-- 		NOT NULL,
-- 	total_amount numeric(12, 2)
-- 		NOT NULL
-- 		CHECK (total_amount >= 0),
-- 	status text
-- 		NOT NULL
-- 		DEFAULT 'new',
-- 	created_at timestamptz
-- 		NOT NULL
-- 		DEFAULT now(),

-- 	CONSTRAINT fk_orders_user
-- 		FOREIGN KEY (user_id)
-- 			REFERENCES training.users(user_id)
-- 		ON DELETE RESTRICT
-- );


SELECT
	constraint_name,
	constraint_type
FROM information_schema.table_constraints
WHERE table_schema = 'training'
	AND table_name = 'orders';
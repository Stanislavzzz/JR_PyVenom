-- CREATE ROLE app_user
-- 	WITH
-- 	LOGIN
-- 	PASSWORD 'password'
-- 	NOSUPERUSER
-- 	NOCREATEDB
-- 	NOCREATEROLE
-- 	NOREPLICATION;


-- SELECT
-- 	rolname,
-- 	rolcanlogin,
-- 	rolsuper,
-- 	rolcreatedb,
-- 	rolcreaterole
-- FROM pg_roles
-- WHERE rolname = 'app_user';



-- SELECT
-- 	*
-- FROM pg_roles;



-- GRANT CONNECT
-- ON DATABASE demo
-- TO app_user;


-- GRANT USAGE
-- ON SCHEMA training
-- TO app_user;


-- GRANT
--     SELECT,
--     INSERT,
--     UPDATE,
--     DELETE
-- ON ALL TABLES IN SCHEMA training
-- TO app_user;


-- GRANT USAGE
-- ON ALL SEQUENCES IN SCHEMA training
-- TO app_user;
-- Script creates the database
-- hbtn_0d_2
-- Also creates the user
-- user_0d_2 with password user_0d_2_pwd
-- Handles Duplicates of DB_name and DB_User
CREATE DATABASE IF NOT EXISTS 'hbtn_0d_2';

CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Granting only Select global permission
GRANT SELECT on 'hbtn_0d_2'.* TO 'user_0d_2'@'localhost';


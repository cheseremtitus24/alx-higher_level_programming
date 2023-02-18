-- Script creates the database
-- hbtn_0d_usa
-- Also creates the user
-- user_0d_2 with password user_0d_2_pwd
-- Handles Duplicates of DB_name and DB_User
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- script creates a database TABLE
-- states that has 2 fields
-- id and name
-- the id field has a default value of 1
-- id filed is constrained as being UNIQUE
-- is a primary key and auto_increments
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states(id INT UNIQUE NOT NULL  PRIMARY KEY AUTO_INCREMENT, name VARCHAR(256) NOT NULL);


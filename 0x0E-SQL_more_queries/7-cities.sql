-- Script creates the database
-- hbtn_0d_usa
-- Also creates the user
-- user_0d_2 with password user_0d_2_pwd
-- Handles Duplicates of DB_name and DB_User
CREATE DATABASE IF NOT EXISTS 'hbtn_0d_usa';

-- script creates a database TABLE
-- cities that has 3 fields
-- id, state_id and name
-- the id field has a default value of 1
-- id filed is constrained as being UNIQUE
-- is a primary key and auto_increments
-- Makes use of FOREIGN key CONSTRAINT
CREATE TABLE IF NOT EXISTS 'cities'(id INT PRIMARY KEY AUTO_INCREMENT, state_id INT NOT NULL, FOREIGN KEY(state_id) REFERENCES states(id), name VARCHAR(256) NOT NULL); 
